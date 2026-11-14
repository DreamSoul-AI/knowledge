"""Preview or create configurable directory symlinks for explicitly selected Git repos."""
import argparse
import json
import os
from pathlib import Path, PurePosixPath
import stat
import subprocess
import sys


class ConfigurationError(ValueError):
    pass


def unique_object(pairs):
    result = {}
    for key, value in pairs:
        if key in result:
            raise ConfigurationError(f'Duplicate configuration key: {key}')
        result[key] = value
    return result


def fields(value, allowed, required, context):
    if not isinstance(value, dict):
        raise ConfigurationError(f'{context} must be an object')
    if set(value) - allowed or required - set(value):
        raise ConfigurationError(f'Invalid fields in {context}: {list(value)}')


def configured_path(value, base):
    if not isinstance(value, str) or not value.strip() or any(char in value for char in '\x00\r\n'):
        raise ConfigurationError('Paths must be nonempty strings without NUL or line breaks')
    path = Path(value)
    return path if path.is_absolute() else base / path


def redirected(path):
    """Recognize symlinks and Windows reparse points, including junctions."""
    try:
        info = path.lstat()
    except FileNotFoundError:
        return False
    return stat.S_ISLNK(info.st_mode) or bool(
        getattr(info, 'st_file_attributes', 0) & getattr(stat, 'FILE_ATTRIBUTE_REPARSE_POINT', 1024))


def ordinary_parent_chain(path, root):
    current = path.parent
    while current != root:
        if redirected(current) or (current.exists() and not current.is_dir()):
            raise ConfigurationError(f'Link parent must be an ordinary directory: {current}')
        current = current.parent


def git(repo, *args):
    command = ['git', '-c', f'safe.directory={repo.as_posix()}']
    if args[0] == 'ls-files':
        command.append('--literal-pathspecs')
    command.extend(['-C', str(repo), *args])
    result = subprocess.run(command, capture_output=True)
    if result.returncode not in (0, 1) or (result.returncode and args[0] != 'check-ignore'):
        raise ConfigurationError(result.stderr.decode('utf-8', errors='replace').strip()
                                 or f'Git failed for {repo}')
    return result


def link_state(link, target):
    if link.is_symlink():
        if not link.exists():
            raise ConfigurationError(f'Broken existing link; inspect before repair: {link}')
        if not target.is_dir() or not os.path.samefile(link, target):
            raise ConfigurationError(f'Existing link points elsewhere: {link}')
        return 'reuse'
    if os.path.lexists(link):
        raise ConfigurationError(f'Entry occupied; no replacement or migration: {link}')
    return 'create'


def make_plan(config_path, selected=None):
    config_path = Path(config_path).resolve(strict=True)
    config = json.loads(config_path.read_text(encoding='utf-8-sig'), object_pairs_hook=unique_object)
    fields(config, {'version', 'resources', 'repositories'},
           {'version', 'resources', 'repositories'}, 'configuration')
    if type(config['version']) is not int or config['version'] != 1:
        raise ConfigurationError('Unsupported configuration version')
    resources, repositories = config['resources'], config['repositories']
    if not isinstance(resources, dict) or not resources:
        raise ConfigurationError('resources must be a nonempty object')
    if not isinstance(repositories, dict) or not repositories:
        raise ConfigurationError('repositories must be a nonempty object')
    chosen = list(repositories) if selected is None else list(dict.fromkeys(selected))
    if not chosen or set(chosen) - set(repositories):
        raise ConfigurationError('Select known repository keys')
    entries, roots, mounts = [], set(), []
    for key in chosen:
        spec = repositories[key]
        fields(spec, {'path', 'links'}, {'path', 'links'}, f'repository {key}')
        repo = configured_path(spec['path'], config_path.parent).resolve(strict=True)
        if not repo.is_dir() or not (repo / '.git').exists():
            raise ConfigurationError(f'Expected Git repository root: {repo}')
        normalized_root = os.path.normcase(str(repo))
        if normalized_root in roots:
            raise ConfigurationError(f'Repository root listed twice: {repo}')
        roots.add(normalized_root)
        ignore = repo / '.gitignore'
        if redirected(ignore) or (ignore.exists() and not ignore.is_file()):
            raise ConfigurationError(f'Expected ordinary .gitignore: {ignore}')
        if not isinstance(spec['links'], dict) or not spec['links']:
            raise ConfigurationError(f'repository {key} needs nonempty links')
        for relative, resource_key in spec['links'].items():
            if (not isinstance(relative, str) or not relative or '\\' in relative
                    or any(char in relative for char in '\x00\r\n')):
                raise ConfigurationError('Link paths must use nonempty forward-slash relative paths')
            parts = PurePosixPath(relative).parts
            if (not parts or PurePosixPath(relative).is_absolute() or
                    any(part in ('.', '..') or part.casefold() == '.git' or ':' in part for part in parts)
                    or parts[0].casefold() == '.gitignore'):
                raise ConfigurationError(f'Unsafe repository-relative link: {relative}')
            link = repo.joinpath(*parts)
            if link == repo:
                raise ConfigurationError('A repository root cannot be a link entry')
            if any(link == other or link in other.parents or other in link.parents for other in mounts):
                raise ConfigurationError(f'Overlapping link entries: {link}')
            mounts.append(link)
            ordinary_parent_chain(link, repo)
            if not isinstance(resource_key, str) or resource_key not in resources:
                raise ConfigurationError(f'Unknown resource for {key}/{relative}: {resource_key}')
            resource = resources[resource_key]
            fields(resource, {'path', 'create'}, {'path'}, f'resource {resource_key}')
            create = resource.get('create', False)
            if type(create) is not bool:
                raise ConfigurationError('resource.create must be a boolean')
            configured_target = configured_path(resource['path'], config_path.parent)
            for path in (configured_target, *configured_target.parents):
                if redirected(path) and not path.exists():
                    raise ConfigurationError(f'Broken resource path: {path}')
            target = configured_target.resolve()
            if target.exists() and not target.is_dir():
                raise ConfigurationError(f'Resource must be a directory: {target}')
            if not target.exists() and not create:
                raise ConfigurationError(f'Resource missing and create is false: {target}')
            if target == link or target in link.parents or link in target.parents:
                raise ConfigurationError(f'Resource and link would overlap: {link} -> {target}')
            if git(repo, 'ls-files', '-z', '--', relative).stdout:
                raise ConfigurationError(f'Git-tracked content at link entry: {link}')
            entries.append({'repository': key, 'resource': resource_key, 'repo': str(repo),
                            'relative': PurePosixPath(relative).as_posix(), 'link': str(link),
                            'target': str(target), 'create_resource': create,
                            'action': link_state(link, target)})
    # A resource cannot depend on another planned mount, even in another repo.
    for entry in entries:
        target = Path(entry['target'])
        if any(target == mount or mount in target.parents for mount in mounts):
            raise ConfigurationError(f'Resource depends on a configured link: {target}')
    return entries


def ignore_pattern(relative):
    return '/' + ''.join('\\' + char if char in '*?[]\\ ' else char for char in relative)


def ensure_ignored(repo, relative):
    if git(repo, 'check-ignore', '--quiet', '--', relative).returncode == 0:
        return False
    path = repo / '.gitignore'
    if redirected(path) or (path.exists() and not path.is_file()):
        raise ConfigurationError(f'Expected ordinary .gitignore: {path}')
    content = path.read_bytes() if path.exists() else b''
    pattern = ignore_pattern(relative).encode('utf-8')
    if pattern in content.splitlines():
        raise ConfigurationError(f'Existing ignore rule is ineffective; inspect nested rules: {path}')
    newline = b'\r\n' if b'\r\n' in content else b'\n'
    addition = b'' if not content or content.endswith(b'\n') else newline
    addition += pattern + newline
    with path.open('ab') as stream:
        stream.write(addition)
    if git(repo, 'check-ignore', '--quiet', '--', relative).returncode:
        raise ConfigurationError(f'Git ignore ineffective; inspect rules: {path}')
    return True


def execute(entries, completed):
    for entry in entries:
        repo, link, target = (Path(entry[key]) for key in ('repo', 'link', 'target'))
        ordinary_parent_chain(link, repo)
        if git(repo, 'ls-files', '-z', '--', entry['relative']).stdout:
            raise ConfigurationError(f'Entry became Git-tracked: {link}')
        action = link_state(link, target)
        if target.exists() and not target.is_dir():
            raise ConfigurationError(f'Resource is no longer a directory: {target}')
        if not target.exists():
            if not entry['create_resource']:
                raise ConfigurationError(f'Resource disappeared before execution: {target}')
            target.mkdir(parents=True, exist_ok=True)
        if action == 'create':
            link.parent.mkdir(parents=True, exist_ok=True)
            os.symlink(str(target), str(link), target_is_directory=True)
        if not link.is_symlink() or not os.path.samefile(link, target):
            raise ConfigurationError(f'Link verification failed: {link}')
        ignored = ensure_ignored(repo, entry['relative'])
        completed.append({**entry, 'action': action, 'verified': True, 'gitignore_updated': ignored})


def main(argv=None):
    for stream in (sys.stdout, sys.stderr):
        if hasattr(stream, 'reconfigure'):
            stream.reconfigure(encoding='utf-8', errors='backslashreplace')
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--config', type=Path, required=True)
    parser.add_argument('--repositories', nargs='+', help='Selected repository keys; defaults to all configured')
    parser.add_argument('--apply', action='store_true', help='Create explicitly allowed directories, links and ignore rules')
    args = parser.parse_args(argv)
    completed = []
    try:
        entries = make_plan(args.config, args.repositories)
        if args.apply:
            execute(entries, completed)
        print(json.dumps({'status': 'applied' if args.apply else 'preview',
                          'entries': entries, 'completed': completed}, ensure_ascii=False))
        return 0
    except (ValueError, OSError) as error:
        print(json.dumps({'status': 'failed', 'error': str(error), 'completed': completed,
                          'recovery': 'Inspect actual links and targets, then rerun; nothing is removed or overwritten.'},
                         ensure_ascii=False))
        return 1


if __name__ == '__main__':
    raise SystemExit(main())
