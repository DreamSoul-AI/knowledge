import unittest
from sync_state import decide


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


if __name__ == '__main__':
    unittest.main()
