"""Compare or update one explicitly selected package, preserving local changes."""
import argparse
import hashlib
import json
import os
import shutil
import stat
import subprocess
import tempfile
import uuid
from pathlib import Path


def digest(path):
    h = hashlib.sha256()
    with path.open('rb') as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b''):
            h.update(chunk)
    return h.hexdigest()


def inventory(root):
    if not root.is_dir():
        raise ValueError(f'Package directory not found: {root}')
    files = {}
    for parent, directories, names in os.walk(root, followlinks=False):
        for name in directories + names:
            path = Path(parent) / name
            info = path.lstat()
            if stat.S_ISLNK(info.st_mode) or getattr(info, 'st_file_attributes', 0) & 0x400:
                raise ValueError(f'Package contains a link or reparse point: {path}')
            if path.is_file():
                files[path.relative_to(root).as_posix()] = digest(path)
    return files


def text_info(path):
    if path is None or path.stat().st_size > 2 * 1024 * 1024:
        return None
    raw = path.read_bytes()
    encoding, bom = 'utf-8', b''
    for marker, codec in [(b'\xef\xbb\xbf', 'utf-8'), (b'\xff\xfe', 'utf-16-le'), (b'\xfe\xff', 'utf-16-be')]:
        if raw.startswith(marker):
            bom, encoding = marker, codec
            break
    try:
        text = raw[len(bom):].decode(encoding)
    except UnicodeDecodeError:
        return None
    if '\x00' in text:
        return None
    return text.replace('\r\n', '\n'), encoding, bom, '\r\n' if '\r\n' in text else '\n'


def equivalent(a, b):
    if a is None or b is None:
        return a is b
    if digest(a) == digest(b):
        return True
    ta, tb = text_info(a), text_info(b)
    return ta is not None and tb is not None and ta[0] == tb[0]


def encode_for(text, current):
    info = text_info(current)
    assert info is not None
    return info[2] + text.replace('\n', info[3]).encode(info[1])


def merged_text(current, base, incoming, work):
    texts = [text_info(p) for p in [current, base, incoming]]
    if any(t is None for t in texts) or not shutil.which('git'):
        return None
    with tempfile.TemporaryDirectory(prefix='merge-', dir=work) as directory:
        paths = []
        for i, info in enumerate(texts):
            p = Path(directory) / str(i)
            p.write_bytes(info[0].encode('utf-8'))
            paths.append(str(p))
        result = subprocess.run(['git', 'merge-file', '-p', '--diff3', *paths], capture_output=True)
        if result.returncode != 0:
            return None
        return encode_for(result.stdout.decode('utf-8'), current)


def within(path, root):
    return path == root or root in path.parents


def update_package(current, incoming, base=None, apply=False, work_dir=None, before_apply=None):
    current, incoming = Path(current).resolve(), Path(incoming).resolve()
    base = Path(base).resolve() if base else None
    roots = [current, incoming] + ([base] if base else [])
    if any(within(current, p) or within(p, current) for p in roots[1:]):
        raise ValueError('Installed package must be separate from source snapshots')
    if work_dir:
        work = Path(work_dir).resolve()
        if any(within(work, p) or within(p, work) for p in roots):
            raise ValueError('Work directory must be separate from package directories')
        work.mkdir(parents=True, exist_ok=True)
    else:
        if apply:
            raise ValueError('An external --work-dir is required to retain update backups')
        work = None
    original = inventory(current)
    new = inventory(incoming)
    prior = inventory(base) if base else {}
    plan = []
    for name in sorted(set(original) | set(new) | set(prior)):
        c = current / name if name in original else None
        n = incoming / name if name in new else None
        b = base / name if name in prior else None
        entry = {'path': name, 'status': 'unchanged'}
        target = current / name
        topology_change = name in new and (target.is_dir() or any(p.is_file() for p in target.parents if p != current and within(p, current)))
        if topology_change:
            entry.update(status='conflict', reason='File/directory replacement needs a reviewed migration')
        elif name not in new and name not in prior:
            entry['status'] = 'preserved-local'
        elif equivalent(c, n):
            pass
        elif base is not None and equivalent(b, n):
            entry['status'] = 'preserved-local'
        elif equivalent(c, b):
            entry['status'] = 'remove' if n is None else 'replace'
            if c and n and text_info(c) and text_info(n):
                entry['_content'] = encode_for(text_info(n)[0], c)
        elif c and b and n:
            merged = merged_text(c, b, n, work)
            if merged is None:
                entry['status'] = 'conflict'
            elif digest(c) == hashlib.sha256(merged).hexdigest():
                entry['status'] = 'preserved-local'
            else:
                entry.update(status='merge', _content=merged)
        else:
            entry['status'] = 'conflict'
        plan.append(entry)
    changes = [e for e in plan if e['status'] in ['replace', 'remove', 'merge']]
    result = {'mode': 'update' if apply else 'check', 'current': str(current), 'incoming': str(incoming), 'base': str(base) if base else None,
              'status': 'conflict' if any(e['status'] == 'conflict' for e in plan) else 'changes' if changes else 'unchanged',
              'files': [{k: v for k, v in e.items() if not k.startswith('_')} for e in plan], 'changed_count': 0}
    if not apply or result['status'] in ['conflict', 'unchanged']:
        return result
    if before_apply:
        before_apply()
    if inventory(current) != original or inventory(incoming) != new or (base and inventory(base) != prior):
        result.update(status='conflict', error='Files changed after comparison; compare again')
        return result
    run = work / ('package-' + uuid.uuid4().hex)
    backup, stage = run / 'backup', run / 'stage'
    backup.mkdir(parents=True)
    stage.mkdir()
    applied = []
    created_dirs = []
    try:
        for entry in changes:
            name = entry['path']
            if name in original:
                dest = backup / name
                dest.parent.mkdir(parents=True, exist_ok=True)
                shutil.copy2(current / name, dest)
            if entry['status'] != 'remove':
                dest = stage / name
                dest.parent.mkdir(parents=True, exist_ok=True)
                if '_content' in entry:
                    dest.write_bytes(entry['_content'])
                    shutil.copymode(current / name, dest)
                else:
                    shutil.copy2(incoming / name, dest)
        # Recheck both inputs after staging, before the first target mutation.
        if inventory(current) != original or inventory(incoming) != new or (base and inventory(base) != prior):
            raise RuntimeError('Files changed while preparing the update')
        for entry in changes:
            name = entry['path']
            target = current / name
            if (digest(target) if target.exists() else None) != original.get(name):
                raise RuntimeError(f'Concurrent change: {name}')
            pending_dirs = []
            parent = target.parent
            while parent != current and not parent.exists():
                pending_dirs.append(parent)
                parent = parent.parent
            for directory in reversed(pending_dirs):
                directory.mkdir()
                created_dirs.append(directory)
            expected = None if entry['status'] == 'remove' else digest(stage / name)
            if entry['status'] == 'remove':
                target.unlink()
            else:
                # A sibling temporary file allows replacement across volumes.
                temp = target.with_name(target.name + '.knowledge-update-' + uuid.uuid4().hex)
                try:
                    shutil.copy2(stage / name, temp)
                    os.replace(temp, target)
                finally:
                    if temp.exists():
                        temp.unlink()
            applied.append((name, expected))
        for name, expected in applied:
            target = current / name
            if (digest(target) if target.exists() else None) != expected:
                raise RuntimeError(f'Readback differs: {name}')
        result.update(status='updated', changed_count=len(changes), backup=str(backup))
    except Exception as error:
        recovery = []
        for name, expected in reversed(applied):
            target = current / name
            try:
                if (digest(target) if target.exists() else None) != expected:
                    recovery.append(name)
                    continue
                if name in original:
                    shutil.copy2(backup / name, target)
                elif target.exists():
                    target.unlink()
            except OSError:
                recovery.append(name)
        for directory in reversed(created_dirs):
            try:
                directory.rmdir()
            except OSError:
                pass
        result.update(status='failed', error=str(error), backup=str(backup), recovery_conflicts=recovery)
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--current', required=True)
    parser.add_argument('--incoming', required=True)
    parser.add_argument('--base')
    parser.add_argument('--apply', action='store_true')
    parser.add_argument('--work-dir')
    args = parser.parse_args()
    try:
        result = update_package(args.current, args.incoming, args.base, args.apply, args.work_dir)
    except (OSError, ValueError) as error:
        result = {'status': 'failed', 'error': str(error)}
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 2 if result['status'] in ['conflict', 'failed'] else 0


if __name__ == '__main__':
    raise SystemExit(main())
