"""Run with unittest discovery; all writes use isolated temporary packages."""
import importlib.util
import os
from pathlib import Path
import shutil
import subprocess
import tempfile
import unittest
from unittest.mock import patch

SCRIPT = Path(__file__).resolve().parents[2] / 'skills/knowledge-update/scripts/update_package.py'
SPEC = importlib.util.spec_from_file_location('update_package', SCRIPT)
updater = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(updater)


class PackageUpdateTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.current, self.base, self.new, self.work = [self.root / x for x in ['current', 'base', 'new', 'work']]
        for p in [self.current, self.base, self.new]:
            p.mkdir()

    def put(self, root, name, content):
        path = root / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(content.encode() if isinstance(content, str) else content)

    def seed(self, name, content):
        for root in [self.current, self.base, self.new]:
            self.put(root, name, content)

    def snapshot(self):
        return {str(p.relative_to(self.current)): (p.read_bytes(), p.stat().st_mtime_ns)
                for p in self.current.rglob('*') if p.is_file()}

    def run_update(self, **kwargs):
        return updater.update_package(self.current, self.new, self.base, work_dir=self.work, **kwargs)

    def test_check_has_no_target_changes(self):
        self.seed('SKILL.md', 'old\n')
        self.put(self.new, 'SKILL.md', 'new\n')
        before = self.snapshot()
        self.assertEqual(self.run_update()['status'], 'changes')
        self.assertEqual(self.snapshot(), before)

    def test_complete_package_and_local_extra_then_noop(self):
        self.seed('SKILL.md', 'old\n')
        self.seed('retired.md', 'old reference\n')
        (self.new / 'retired.md').unlink()
        self.put(self.new, 'SKILL.md', 'new\n')
        self.put(self.new, 'agents/openai.yaml', 'interface: {}\n')
        self.put(self.new, 'references/new.md', 'new reference\n')
        self.put(self.current, 'personal.md', 'keep me\n')
        result = self.run_update(apply=True)
        self.assertEqual(result['status'], 'updated')
        self.assertFalse((self.current / 'retired.md').exists())
        self.assertEqual((self.current / 'personal.md').read_text(), 'keep me\n')
        self.assertEqual((self.current / 'references/new.md').read_text(), 'new reference\n')
        before = self.snapshot()
        self.assertEqual(updater.update_package(self.current, self.new, self.new, True, self.work)['status'], 'unchanged')
        self.assertEqual(self.snapshot(), before)

    @unittest.skipUnless(shutil.which('git'), 'Text merge needs Git')
    def test_customization_merges_and_preserves_utf16_crlf(self):
        text = 'title\nline2\nline3\nline4\nline5\nline6\nend\n'
        self.seed('SKILL.md', text)
        self.put(self.current, 'SKILL.md', b'\xff\xfe' + text.replace('title', 'local title').replace('\n', '\r\n').encode('utf-16-le'))
        self.put(self.new, 'SKILL.md', text.replace('end', 'new end'))
        result = self.run_update(apply=True)
        self.assertEqual(result['status'], 'updated')
        raw = (self.current / 'SKILL.md').read_bytes()
        self.assertTrue(raw.startswith(b'\xff\xfe'))
        decoded = raw[2:].decode('utf-16-le')
        self.assertIn('local title\r\n', decoded)
        self.assertIn('new end\r\n', decoded)
        before = self.snapshot()
        self.assertEqual(updater.update_package(self.current, self.new, self.new, True, self.work)['status'], 'unchanged')
        self.assertEqual(self.snapshot(), before)

    def test_overlap_keeps_entire_package(self):
        self.seed('SKILL.md', 'old\n')
        self.put(self.current, 'SKILL.md', 'local\n')
        self.put(self.new, 'SKILL.md', 'upstream\n')
        self.put(self.new, 'references/new.md', 'new\n')
        before = self.snapshot()
        self.assertEqual(self.run_update(apply=True)['status'], 'conflict')
        self.assertEqual(self.snapshot(), before)

    def test_without_base_does_not_replace_unknown_content(self):
        self.put(self.current, 'SKILL.md', 'local\n')
        self.put(self.new, 'SKILL.md', 'incoming\n')
        before = self.snapshot()
        self.assertEqual(updater.update_package(self.current, self.new, apply=True, work_dir=self.work)['status'], 'conflict')
        self.assertEqual(self.snapshot(), before)

    def test_retired_custom_file_is_conflict(self):
        self.seed('reference.md', 'old\n')
        self.put(self.current, 'reference.md', 'local custom\n')
        (self.new / 'reference.md').unlink()
        self.assertEqual(self.run_update(apply=True)['status'], 'conflict')
        self.assertEqual((self.current / 'reference.md').read_text(), 'local custom\n')

    def test_binary_replace_and_overlap_conflict(self):
        self.seed('asset.bin', b'\x00\xffold')
        self.put(self.new, 'asset.bin', b'\x00\xffnew')
        self.assertEqual(self.run_update(apply=True)['status'], 'updated')
        self.put(self.current, 'asset.bin', b'\x00custom')
        self.assertEqual(self.run_update(apply=True)['status'], 'conflict')

    def test_concurrent_change_before_apply_preserved(self):
        self.seed('SKILL.md', 'old\n')
        self.put(self.new, 'SKILL.md', 'new\n')
        result = self.run_update(apply=True, before_apply=lambda: self.put(self.current, 'SKILL.md', 'another writer\n'))
        self.assertEqual(result['status'], 'conflict')
        self.assertEqual((self.current / 'SKILL.md').read_text(), 'another writer\n')

    def test_failed_second_write_rolls_back_first(self):
        for name in ['a.txt', 'b.txt']:
            self.seed(name, 'old\n')
            self.put(self.new, name, 'new\n')
        original_replace = os.replace
        def fail_second(src, dest):
            if Path(dest).name == 'b.txt':
                raise PermissionError('injected denied write')
            return original_replace(src, dest)
        with patch.object(updater.os, 'replace', side_effect=fail_second):
            result = self.run_update(apply=True)
        self.assertEqual(result['status'], 'failed')
        self.assertEqual(result['recovery_conflicts'], [])
        for name in ['a.txt', 'b.txt']:
            self.assertEqual((self.current / name).read_text(), 'old\n')

    def test_rollback_keeps_another_writers_edit(self):
        for name in ['a.txt', 'b.txt']:
            self.seed(name, 'old\n')
            self.put(self.new, name, 'new\n')
        original_replace = os.replace
        def concurrent_failure(src, dest):
            if Path(dest).name == 'b.txt':
                self.put(self.current, 'a.txt', 'another writer\n')
                raise PermissionError('injected failure')
            return original_replace(src, dest)
        with patch.object(updater.os, 'replace', side_effect=concurrent_failure):
            result = self.run_update(apply=True)
        self.assertEqual(result['recovery_conflicts'], ['a.txt'])
        self.assertEqual((self.current / 'a.txt').read_text(), 'another writer\n')

    @unittest.skipUnless(os.name == 'nt', 'Windows Junction test')
    def test_junction_rejected_without_outside_writes(self):
        outside = self.root / 'outside'
        outside.mkdir()
        link = self.current / 'linked'
        command = "$null = New-Item -ItemType Junction -Path '" + str(link) + "' -Target '" + str(outside) + "'"
        completed = subprocess.run(['powershell', '-NoProfile', '-Command', command], capture_output=True)
        self.assertEqual(completed.returncode, 0, completed.stderr.decode(errors='replace'))
        try:
            with self.assertRaisesRegex(ValueError, 'reparse point'):
                self.run_update(apply=True)
            self.assertEqual(list(outside.iterdir()), [])
        finally:
            os.rmdir(link)

    def test_work_directory_overlap_rejected_before_creation(self):
        work = self.current / 'new-output'
        with self.assertRaisesRegex(ValueError, 'Work directory'):
            updater.update_package(self.current, self.new, self.base, work_dir=work)
        self.assertFalse(work.exists())

    @unittest.skipIf(os.name == 'nt', 'POSIX executable mode')
    def test_updated_text_keeps_execute_permission(self):
        self.seed('run.sh', '#!/bin/sh\necho old\n')
        (self.current / 'run.sh').chmod(0o755)
        self.put(self.new, 'run.sh', '#!/bin/sh\necho new\n')
        self.assertEqual(self.run_update(apply=True)['status'], 'updated')
        self.assertEqual((self.current / 'run.sh').stat().st_mode & 0o777, 0o755)

    def test_file_directory_replacement_requires_review(self):
        self.seed('entry', 'old file\n')
        (self.new / 'entry').unlink()
        self.put(self.new, 'entry/new.md', 'new nested file\n')
        before = self.snapshot()
        self.assertEqual(self.run_update(apply=True)['status'], 'conflict')
        self.assertEqual(self.snapshot(), before)

    def test_directory_file_replacement_requires_review(self):
        self.seed('entry/old.md', 'old nested file\n')
        (self.new / 'entry/old.md').unlink()
        (self.new / 'entry').rmdir()
        self.put(self.new, 'entry', 'new file\n')
        before = self.snapshot()
        self.assertEqual(self.run_update(apply=True)['status'], 'conflict')
        self.assertEqual(self.snapshot(), before)


if __name__ == '__main__':
    unittest.main()
