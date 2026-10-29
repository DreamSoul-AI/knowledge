import copy
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
from sync_state import decide, decide_batch


class SyncStateTests(unittest.TestCase):
    def test_change_matrix(self):
        base = {'local': 'L0', 'remote': 'R0'}
        for direction in ('upload', 'download', 'both'):
            with self.subTest(direction=direction):
                self.assertEqual(decide(direction, 'L0', 'R0', base)['action'], 'unchanged')
                self.assertEqual(decide(direction, 'L1', 'R1', base)['action'], 'conflict')
                self.assertEqual(decide(direction, 'L1', 'R0', base)['action'], 'upload' if direction != 'download' else 'needs_confirmation')
                self.assertEqual(decide(direction, 'L0', 'R1', base)['action'], 'download' if direction != 'upload' else 'needs_confirmation')
                for local, remote in ((None, 'R0'), ('L0', None), (None, None)):
                    self.assertEqual(decide(direction, local, remote, base)['action'], 'needs_confirmation')

    def test_bootstrap_requires_unique_source(self):
        for direction in ('upload', 'download', 'both'):
            self.assertEqual(decide(direction, 'L', 'R')['action'], 'needs_confirmation')
            self.assertEqual(decide(direction, None, None)['action'], 'needs_confirmation')
        self.assertEqual(decide('upload', 'L', None)['action'], 'upload')
        self.assertEqual(decide('download', None, 'R')['action'], 'download')
        self.assertEqual(decide('download', 'L', None)['action'], 'needs_confirmation')
        self.assertEqual(decide('upload', None, 'R')['action'], 'needs_confirmation')

    def test_invalid_input_cannot_choose_a_write(self):
        for args in [('mirror', 'L', 'R', None), ('both', '', 'R', None), ('both', 'L', 'R', {'local': 'L'})]:
            with self.assertRaises(ValueError):
                decide(*args)

    def test_conflict_does_not_advance_baseline(self):
        base = {'local': 'L0', 'remote': 'R0'}
        self.assertEqual(decide('both', 'L1', 'R1', base), decide('both', 'L1', 'R1', base))
        self.assertEqual(base, {'local': 'L0', 'remote': 'R0'})


def item(key, **changes):
    value = {'id': key, 'direction': 'both', 'local': 'L0', 'remote': 'R0',
             'baseline': {'local': 'L0', 'remote': 'R0'}, 'local_path': f'input/{key}.md',
             'receipt': f'state/{key}.json', 'remote_key': f'feishu:docx:{key}'}
    value.update(changes)
    return value


class BatchTests(unittest.TestCase):
    def test_conflict_and_failure_do_not_block_other_documents(self):
        items = [item('upload', local='L1'), item('conflict', local='L1', remote='R1'),
                 item('invalid', direction='mirror'), item('download', remote='R1'), item('same')]
        before = copy.deepcopy(items)
        result = decide_batch(items)
        self.assertEqual([r['action'] for r in result['items']], ['upload', 'conflict', 'failed', 'download', 'unchanged'])
        self.assertEqual(result['counts'], {'upload': 1, 'conflict': 1, 'failed': 1, 'download': 1, 'unchanged': 1})
        self.assertEqual(items, before)
        self.assertEqual(decide_batch(items), result)

    def test_duplicate_identity_rejects_the_entire_batch(self):
        for field in ('id', 'local_path', 'receipt', 'remote_key'):
            with self.subTest(field=field):
                a, b = item('a'), item('b')
                b[field] = a[field]
                with self.assertRaisesRegex(ValueError, 'duplicate'):
                    decide_batch([a, b])

    def test_path_aliases_and_cross_item_receipt_collision(self):
        for field in ('local_path', 'receipt'):
            with self.subTest(field=field):
                a, b = item('a'), item('b')
                a[field] = 'Output/../Files/Review.md'
                b[field] = './files/review.MD' if os.name == 'nt' else './Files/Review.md'
                with self.assertRaisesRegex(ValueError, 'duplicate'):
                    decide_batch([a, b])
        a, b = item('a'), item('b')
        a['receipt'] = b['local_path']
        with self.assertRaisesRegex(ValueError, 'overlaps'):
            decide_batch([a, b])
        a['receipt'] = 'input'
        with self.assertRaisesRegex(ValueError, 'overlaps'):
            decide_batch([a, b])

    @unittest.skipIf(os.name == 'nt', 'Windows paths are case-insensitive')
    def test_posix_paths_preserve_case(self):
        a, b = item('a'), item('b')
        a['local_path'] = 'Files/Review.md'
        b['local_path'] = 'Files/review.md'
        a['receipt'] = 'state/Review.json'
        b['receipt'] = 'state/review.json'
        self.assertEqual(decide_batch([a, b])['counts'], {'unchanged': 2})

    def test_remote_keys_are_case_sensitive_on_every_platform(self):
        a, b = item('a'), item('b')
        a['remote_key'] = 'feishu:docx:TokenA'
        b['remote_key'] = 'feishu:docx:tokena'
        self.assertEqual(decide_batch([a, b])['counts'], {'unchanged': 2})

    def test_malformed_mappings_are_not_partial_write_plans(self):
        for entries in (None, {}, [], [None], [item('a'), {'id': 'b'}], [item('a', receipt=' ')]):
            with self.subTest(entries=entries), self.assertRaises(ValueError):
                decide_batch(entries)

    def test_missing_or_wrong_direction_is_isolated_without_guessing(self):
        missing = item('missing'); del missing['direction']
        bad = item('bad', local=[])
        blocked = item('blocked', direction='download', local='L1')
        result = decide_batch([missing, bad, blocked, item('valid')])
        self.assertEqual([r['action'] for r in result['items']], ['failed', 'failed', 'needs_confirmation', 'unchanged'])

    def test_single_and_batch_cli_and_manifest_relative_paths(self):
        script = Path(__file__).with_name('sync_state.py').resolve()
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory); folder = root / 'manifest'; folder.mkdir()
            single = folder / 'single.json'; single.write_text(json.dumps({'direction': 'upload', 'local': 'L', 'remote': None}), encoding='utf-8')
            command = [sys.executable, '-B', str(script)]
            result = subprocess.run(command + [str(single)], cwd=root, capture_output=True, text=True, check=True)
            self.assertEqual(json.loads(result.stdout)['action'], 'upload')
            a, b = item('a'), item('b')
            b['local_path'] = str(folder / a['local_path'])
            manifest = folder / 'batch.json'; manifest.write_text(json.dumps({'items': [a, b]}), encoding='utf-8')
            result = subprocess.run(command + [str(manifest)], cwd=root, capture_output=True, text=True)
            self.assertEqual(result.returncode, 2)
            self.assertIn('duplicate batch local_path', result.stderr)
            manifest.write_text(json.dumps({'items': [a, item('b')]}), encoding='utf-8')
            result = subprocess.run(command + [str(manifest)], cwd=root, capture_output=True, text=True, check=True)
            self.assertEqual(json.loads(result.stdout)['counts'], {'unchanged': 2})
            manifest.write_text(json.dumps({'items': [a], 'direction': 'upload'}), encoding='utf-8')
            result = subprocess.run(command + [str(manifest)], cwd=root, capture_output=True, text=True)
            self.assertEqual(result.returncode, 2)


if __name__ == '__main__':
    unittest.main()
