"""Focused tests for whole-conversation reading and the archive dependency contract."""

import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest

from records import locate_source, prepare
from review import page


def session(messages):
    rows = [{"type": "session_meta", "payload": {"id": "test-session"}}]
    for identifier, text in messages:
        rows.append({"type": "response_item", "payload": {
            "type": "message", "role": "user", "id": identifier,
            "content": [{"type": "input_text", "text": text}],
            "internal_chat_message_metadata_passthrough": {"content_item_kinds": ["user.text"]}}})
    return ("\n".join(json.dumps(row) for row in rows) + "\n").encode()


class ReviewTests(unittest.TestCase):
    def test_all_pages_retain_early_goal_and_late_correction(self):
        with tempfile.TemporaryDirectory() as directory:
            source = Path(directory) / "test-session.jsonl"
            messages = [(f"m{i}", f"公开消息{i}") for i in range(123)]
            messages[0] = ("m0", "最初要求自动发布")
            messages[-1] = ("m122", "纠正：只要草稿，不发布")
            source.write_bytes(session(messages))
            prepared = prepare(source, "test-session")
            seen, offset = [], 0
            while True:
                current = page(prepared, offset, 17)
                seen.extend((i["id"], i["text"]) for i in current["items"])
                if current["next_offset"] is None:
                    break
                offset = current["next_offset"]
            self.assertEqual(seen, messages)

    def test_fixed_cutoff_and_prefix_across_reads(self):
        with tempfile.TemporaryDirectory() as directory:
            source = Path(directory) / "test-session.jsonl"
            source.write_bytes(session([("m1", "原话"), ("m2", "后续纠正")]))
            original = prepare(source, "test-session", "m1")
            prefix = original["timing"]["source_prefix_sha256"]
            source.write_bytes(session([("m1", "原话"), ("m2", "后续纠正"), ("m3", "之后消息")]))
            appended = prepare(source, "test-session", "m1")
            self.assertEqual(page(appended, expect_prefix_sha256=prefix)["total_items"], 1)
            source.write_bytes(session([("m1", "被改写"), ("m2", "后续纠正")]))
            with self.assertRaisesRegex(ValueError, "prefix changed"):
                page(prepare(source, "test-session", "m1"), expect_prefix_sha256=prefix)

    def test_source_identity_ambiguity_and_bounds(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            a = root / "test-session.jsonl";a.write_bytes(session([("m1", "原话")]))
            self.assertEqual(locate_source("test-session", sessions_root=root), a)
            (root / "copy-test-session.jsonl").write_bytes(a.read_bytes())
            with self.assertRaisesRegex(ValueError, "found 2"):
                locate_source("test-session", sessions_root=root)
            with self.assertRaisesRegex(ValueError, "does not match"):
                prepare(a, "wrong-session")
            for offset, limit in [(-1, 2), (0, 0), (0, 201)]:
                with self.assertRaises(ValueError):
                    page(prepare(a, "test-session"), offset, limit)

    def test_complete_packages_and_explicit_dependency(self):
        review_root = Path(__file__).resolve().parents[1]
        archive_root = review_root.parent / "conversation-archive"
        if not archive_root.is_dir():
            self.skipTest("Archive integration requires its separate complete package")
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            installed = root / "installed"
            review_copy = installed / "conversation-review"
            archive_copy = installed / "conversation-archive"
            shutil.copytree(review_root, review_copy, ignore=shutil.ignore_patterns("__pycache__"))
            shutil.copytree(archive_root, archive_copy, ignore=shutil.ignore_patterns("__pycache__"))
            source = root / "test-session.jsonl";source.write_bytes(session([("m1", "独立包原话")]))
            review_cmd = [sys.executable, "-B", str(review_copy / "scripts/review.py"),
                          "--source", str(source), "--session", "test-session"]
            read = subprocess.run(review_cmd, cwd=root, capture_output=True, text=True, check=True)
            self.assertEqual(json.loads(read.stdout)["items"][0]["text"], "独立包原话")
            cmd = [sys.executable, "-B", str(archive_copy / "scripts/archive.py"),
                   "--source", str(source), "--session", "test-session", "--title", "独立包",
                   "--output", str(root / "output")]
            result = subprocess.run(cmd, cwd=root, capture_output=True, text=True, check=True)
            self.assertTrue(json.loads(result.stdout)["changed"])
            moved = root / "separate-review"
            shutil.move(str(review_copy), moved)
            # review remains usable without archive beside it.
            read = subprocess.run([sys.executable, "-B", str(moved / "scripts/review.py"),
                                   "--source", str(source), "--session", "test-session"],
                                  cwd=root, capture_output=True, text=True, check=True)
            self.assertEqual(json.loads(read.stdout)["total_items"], 1)
            missing = subprocess.run(cmd, cwd=root, capture_output=True, text=True)
            self.assertNotEqual(missing.returncode, 0)
            self.assertIn("Missing conversation-review dependency", missing.stderr)
            rerun = subprocess.run(cmd + ["--review-skill", str(moved)], cwd=root,
                                   capture_output=True, text=True, check=True)
            self.assertFalse(json.loads(rerun.stdout)["changed"])


if __name__ == "__main__":
    unittest.main()
