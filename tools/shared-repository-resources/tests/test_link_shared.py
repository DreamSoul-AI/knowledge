"""Isolated filesystem integration checks; no existing repositories or resource data."""
import copy
import importlib.util
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch

SCRIPT = Path(__file__).resolve().parents[1] / 'link_shared.py'
SPEC = importlib.util.spec_from_file_location('configurable_shared_resources', SCRIPT)
TOOL = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(TOOL)


class SharedResourcesTests(unittest.TestCase):
    def setUp(self):
        parent = Path(os.environ.get('SHARED_RESOURCES_TEST_ROOT', tempfile.gettempdir())).resolve()
        parent.mkdir(parents=True, exist_ok=True)
        self.temp = tempfile.TemporaryDirectory(prefix='shared-config-', dir=parent)
        self.root = Path(self.temp.name).resolve()
        assert self.root.is_relative_to(parent)
        self.addCleanup(self.temp.cleanup)

    def git(self, repo, *args):
        result = subprocess.run(['git', '-c', f'safe.directory={repo.as_posix()}',
                                 '-C', str(repo), *args], capture_output=True)
        self.assertEqual(result.returncode, 0, result.stderr)
        return result.stdout

    def fixture(self, design=False):
        if design:
            locations = ['studio teams/Designer 甲', 'pipelines/Exporter']
            resources = {'icons': {'path': 'library/icons'},
                         'fonts': {'path': 'another library/fonts'},
                         'render_reports': {'path': 'scratch/reports', 'create': True}}
            links = [{'design references/icons[1]': 'icons', 'cache/fonts': 'fonts'},
                     {'inputs/icons': 'icons', 'build/reports': 'render_reports'}]
        else:
            locations = ['projects/encoder', 'other projects/evaluator']
            resources = {'corpus': {'path': 'shared/text corpus'},
                         'checkpoint': {'path': 'shelves/checkpoints'}}
            links = [{'.inputs/text': 'corpus', '.weights/base': 'checkpoint'},
                     {'fixtures/common': 'corpus', 'cache/reference': 'checkpoint'}]
        repositories = {}
        for index, location in enumerate(locations):
            repo = self.root / location
            repo.mkdir(parents=True)
            self.git(repo, 'init', '-q')
            (repo / '.gitignore').write_bytes(b'# keep existing rule\r\nkeep-me\r\n')
            repositories[f'repo-{index}'] = {'path': location, 'links': links[index]}
        for name, resource in resources.items():
            if not resource.get('create', False):
                folder = self.root / resource['path']
                folder.mkdir(parents=True)
                (folder / 'sentinel.txt').write_text(name, encoding='utf-8')
        config = {'version': 1, 'resources': resources, 'repositories': repositories}
        path = self.root / 'mapping.json'
        self.save(path, config)
        return path, config

    def save(self, path, config):
        path.write_text(json.dumps(config, ensure_ascii=False, indent=2), encoding='utf-8')

    def cli(self, config, *args, script=SCRIPT, expected=0):
        result = subprocess.run([sys.executable, '-B', str(script), '--config', str(config), *args],
                                cwd=self.root.parent, capture_output=True)
        report = json.loads(result.stdout.decode('utf-8'))
        self.assertEqual(result.returncode, expected, report)
        return report

    def verify_layout(self, config, report):
        for entry in report['completed']:
            link, target = Path(entry['link']), Path(entry['target'])
            self.assertTrue(link.is_symlink())
            self.assertTrue(os.path.samefile(link, target))
            if (target / 'sentinel.txt').exists():
                self.assertEqual((link / 'sentinel.txt').read_bytes(), (target / 'sentinel.txt').read_bytes())
            ignored = subprocess.run(['git', '-c', f"safe.directory={entry['repo']}",
                                      '-C', entry['repo'], 'check-ignore', '--quiet', '--', entry['relative']])
            self.assertEqual(ignored.returncode, 0, entry)
        for resource in config['resources'].values():
            if not resource.get('create', False):
                self.assertTrue((self.root / resource['path'] / 'sentinel.txt').is_file())

    def test_research_repositories_apply_and_repeat(self):
        path, config = self.fixture()
        first = self.cli(path, '--apply')
        self.assertEqual(len(first['completed']), 4)
        self.verify_layout(config, first)
        ignore_files = {p: p.read_bytes() for p in self.root.rglob('.gitignore')}
        second = self.cli(path, '--apply')
        self.assertTrue(all(entry['action'] == 'reuse' for entry in second['completed']))
        self.assertTrue(all(not entry['gitignore_updated'] for entry in second['completed']))
        self.assertEqual({p: p.read_bytes() for p in ignore_files}, ignore_files)

    def test_design_repositories_relocated_tool(self):
        path, config = self.fixture(design=True)
        relocated = self.root / 'standalone tool/links.py'
        relocated.parent.mkdir()
        relocated.write_bytes(SCRIPT.read_bytes())
        first = self.cli(path, '--apply', script=relocated)
        self.verify_layout(config, first)
        second = self.cli(path, '--apply', script=relocated)
        self.assertTrue(all(entry['action'] == 'reuse' for entry in second['completed']))
        self.assertTrue((self.root / 'scratch/reports').is_dir())

    def test_preview_does_not_create_resources_links_or_ignore(self):
        path, config = self.fixture(design=True)
        before = {p: p.read_bytes() for p in self.root.rglob('.gitignore')}
        report = self.cli(path)
        self.assertEqual(report['status'], 'preview')
        self.assertEqual(report['completed'], [])
        self.assertFalse((self.root / 'scratch/reports').exists())
        self.assertTrue(all(not os.path.lexists(entry['link']) for entry in report['entries']))
        self.assertEqual({p: p.read_bytes() for p in before}, before)

    def test_selected_repository_does_not_change_other_repo(self):
        path, config = self.fixture()
        first_repo = self.root / config['repositories']['repo-0']['path']
        before = (first_repo / '.gitignore').read_bytes()
        report = self.cli(path, '--apply', '--repositories', 'repo-1')
        self.assertEqual(len(report['completed']), 2)
        self.assertFalse((first_repo / '.inputs').exists())
        self.assertEqual((first_repo / '.gitignore').read_bytes(), before)

    def test_research_profile_uses_the_same_generic_interface(self):
        example = SCRIPT.parent / 'examples/research.config.example.json'
        config = json.loads(example.read_text(encoding='utf-8'))
        for repo_spec in config['repositories'].values():
            repo = self.root / repo_spec['path']
            repo.mkdir(parents=True)
            self.git(repo, 'init', '-q')
        for resource in config['resources'].values():
            if not resource.get('create', False):
                target = self.root / resource['path']
                target.mkdir(parents=True)
                (target / 'sentinel.txt').write_bytes(b'profile resource')
        path = self.root / 'research.json'
        self.save(path, config)
        report = self.cli(path, '--apply')
        self.assertEqual(len(report['completed']), 6)
        self.verify_layout(config, report)
        self.assertNotEqual((self.root / 'repositories/project-a/.local/artifacts').resolve(),
                            (self.root / 'repositories/project-b/.local/artifacts').resolve())

    def test_later_entity_conflict_prevents_all_writes(self):
        path, config = self.fixture(design=True)
        conflict = self.root / config['repositories']['repo-1']['path'] / 'build/reports'
        conflict.mkdir(parents=True)
        (conflict / 'keep.txt').write_bytes(b'original')
        report = self.cli(path, '--apply', expected=1)
        self.assertEqual(report['completed'], [])
        first_repo = self.root / config['repositories']['repo-0']['path']
        self.assertFalse((first_repo / 'design references').exists())
        self.assertEqual((conflict / 'keep.txt').read_bytes(), b'original')
        self.assertFalse((self.root / 'scratch/reports').exists())

    def test_wrong_target_link_preserved(self):
        path, config = self.fixture()
        repo = self.root / config['repositories']['repo-0']['path']
        link = repo / '.inputs/text'
        link.parent.mkdir()
        wrong = self.root / 'shelves/checkpoints'
        os.symlink(str(wrong), str(link), target_is_directory=True)
        report = self.cli(path, '--apply', expected=1)
        self.assertIn('points elsewhere', report['error'])
        self.assertTrue(os.path.samefile(link, wrong))

    def test_broken_link_does_not_recreate_empty_resource(self):
        path, config = self.fixture(design=True)
        repo = self.root / config['repositories']['repo-1']['path']
        link = repo / 'build/reports'
        link.parent.mkdir()
        target = self.root / 'scratch/reports'
        os.symlink(str(target), str(link), target_is_directory=True)
        report = self.cli(path, '--apply', expected=1)
        self.assertIn('Broken existing link', report['error'])
        self.assertTrue(link.is_symlink())
        self.assertFalse(target.exists())

    def test_git_tracked_content_is_not_untracked_or_replaced(self):
        path, config = self.fixture()
        repo = self.root / config['repositories']['repo-0']['path']
        link = repo / '.inputs/text'
        link.mkdir(parents=True)
        (link / 'tracked.txt').write_bytes(b'keep')
        self.git(repo, 'add', '.inputs/text/tracked.txt')
        index_before = self.git(repo, 'ls-files', '--stage')
        report = self.cli(path, '--apply', expected=1)
        self.assertIn('Git-tracked', report['error'])
        self.assertEqual(self.git(repo, 'ls-files', '--stage'), index_before)
        self.assertEqual((link / 'tracked.txt').read_bytes(), b'keep')

    def test_parent_symlink_is_not_followed(self):
        path, config = self.fixture()
        repo = self.root / config['repositories']['repo-0']['path']
        outside = self.root / 'outside'
        outside.mkdir()
        os.symlink(str(outside), str(repo / '.inputs'), target_is_directory=True)
        report = self.cli(path, '--apply', expected=1)
        self.assertIn('ordinary directory', report['error'])
        self.assertFalse((outside / 'text').exists())

    @unittest.skipUnless(os.name == 'nt', 'Windows junction behavior')
    def test_windows_junction_parent_is_not_followed(self):
        path, config = self.fixture()
        repo = self.root / config['repositories']['repo-0']['path']
        target = self.root / 'junction target'
        target.mkdir()
        result = subprocess.run(['cmd', '/c', 'mklink', '/J', str(repo / '.inputs'), str(target)],
                                capture_output=True)
        self.assertEqual(result.returncode, 0, result.stderr)
        report = self.cli(path, '--apply', expected=1)
        self.assertIn('ordinary directory', report['error'])
        self.assertFalse((target / 'text').exists())

    def test_symlinked_gitignore_is_not_modified(self):
        path, config = self.fixture()
        repo = self.root / config['repositories']['repo-0']['path']
        target = self.root / 'external-ignore'
        target.write_bytes(b'keep external rules')
        (repo / '.gitignore').unlink()
        os.symlink(str(target), str(repo / '.gitignore'))
        report = self.cli(path, '--apply', expected=1)
        self.assertIn('ordinary .gitignore', report['error'])
        self.assertEqual(target.read_bytes(), b'keep external rules')

    def test_nested_ignore_conflict_does_not_append_duplicates_on_retry(self):
        path, config = self.fixture()
        repo = self.root / config['repositories']['repo-0']['path']
        parent = repo / '.inputs'
        parent.mkdir()
        (parent / '.gitignore').write_bytes(b'!text\n')
        first = self.cli(path, '--apply', expected=1)
        self.assertIn('Git ignore ineffective', first['error'])
        before = (repo / '.gitignore').read_bytes()
        second = self.cli(path, '--apply', expected=1)
        self.assertIn('Existing ignore rule is ineffective', second['error'])
        self.assertEqual((repo / '.gitignore').read_bytes(), before)

    def test_path_escape_and_overlapping_mappings_rejected(self):
        path, config = self.fixture()
        for entry in ('../outside', '/outside', '.git/resources', 'C:/outside', 'x\ny'):
            with self.subTest(entry=entry):
                candidate = copy.deepcopy(config)
                candidate['repositories']['repo-0']['links'] = {entry: 'corpus'}
                self.save(path, candidate)
                with self.assertRaises(TOOL.ConfigurationError):
                    TOOL.make_plan(path)
        config['repositories']['repo-0']['links'] = {'cache': 'corpus', 'cache/nested': 'checkpoint'}
        self.save(path, config)
        with self.assertRaisesRegex(TOOL.ConfigurationError, 'Overlapping'):
            TOOL.make_plan(path)

    def test_missing_resource_requires_explicit_create(self):
        path, config = self.fixture()
        config['resources']['corpus']['path'] = 'not-created'
        self.save(path, config)
        report = self.cli(path, '--apply', expected=1)
        self.assertIn('create is false', report['error'])
        self.assertFalse((self.root / 'not-created').exists())

    def test_interruption_resumes_from_real_link_state(self):
        path, config = self.fixture()
        plan = TOOL.make_plan(path)
        real_symlink = os.symlink
        calls = []

        def interrupted(*args, **kwargs):
            calls.append(1)
            if len(calls) == 2:
                raise PermissionError('injected second-link interruption')
            return real_symlink(*args, **kwargs)

        completed = []
        with patch.object(TOOL.os, 'symlink', interrupted):
            with self.assertRaises(PermissionError):
                TOOL.execute(plan, completed)
        self.assertEqual(len(completed), 1)
        report = self.cli(path, '--apply')
        self.assertEqual(report['completed'][0]['action'], 'reuse')
        self.verify_layout(config, report)


if __name__ == '__main__':
    class RecordingResult(unittest.TextTestResult):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.records = []

        def record(self, test, status, detail=None):
            self.records.append({'case': test.id(), 'status': status, 'detail': detail})
            filename = os.environ.get('SHARED_RESOURCES_TEST_REPORT')
            if filename:
                path = Path(filename)
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_text(json.dumps({'cases': self.records}, ensure_ascii=False, indent=2),
                                encoding='utf-8')

        def addSuccess(self, test):
            super().addSuccess(test)
            self.record(test, 'pass')

        def addFailure(self, test, error):
            super().addFailure(test, error)
            self.record(test, 'fail', str(error[1]))

        def addError(self, test, error):
            super().addError(test, error)
            self.record(test, 'error', str(error[1]))

        def addSkip(self, test, reason):
            super().addSkip(test, reason)
            self.record(test, 'skip', reason)

    runner = unittest.TextTestRunner(verbosity=2, resultclass=RecordingResult)
    unittest.main(testRunner=runner)
