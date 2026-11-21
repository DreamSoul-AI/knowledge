"""Behavioral tests; all writes stay in newly created temporary repositories."""
from pathlib import Path
import importlib.util
import json
import os
import subprocess
import tempfile
import unittest

SCRIPT = Path(__file__).parents[1] / "scripts/github_summary.py"
spec = importlib.util.spec_from_file_location("github_summary", SCRIPT)
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)


class Intake(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory(prefix="github-summary-")
        self.root = Path(self.tmp.name).resolve()
        self.repo = self.root / "repo"
        self.repo.mkdir()
        self.out = self.root / "received"
        self.git("init", "-b", "main")
        self.git("config", "user.email", "test@example.invalid")
        self.git("config", "user.name", "Synthetic tester")
        self.put("AGENTS.md", "经验位置：notes/decisions。按项目约定选取该目录。\n")
        self.put("README.md", "<<<<<<< HEAD\n[missing](docs/gone.md)\n=======\nother\n>>>>>>> side\n")
        self.put(".gitignore", "docs/经验 Learnings/local.md\ndocs/经验 Learnings/ignored.md\n")
        self.put("docs/经验 Learnings/shared.md", "原文\r\nA condition and evidence.\r\n")
        self.put("docs/经验 Learnings/image.bin", b"\x00\xff\x01")
        self.put("notes/decisions/custom.md", "custom project source\n")
        self.put("src/sklearn/data/readme.md", "not an experience source\n")
        self.put("tmp/Learnings/cached.md", "not a current source\n")
        self.git("add", ".")
        self.git("commit", "-m", "initial")
        self.git("branch", "dev")
        # A registered worktree under an excluded directory must still be scanned.
        self.wt = self.repo / "tmp/second-worktree"
        self.git("worktree", "add", str(self.wt), "dev")
        self.put("docs/经验 Learnings/local.md", "dirty and ignored\n")
        p = self.wt / "docs/经验 Learnings/ignored.md"
        p.write_text("other-worktree ignored original\n", encoding="utf-8")

    def tearDown(self):
        # TemporaryDirectory owns this verified synthetic root; no business data.
        self.tmp.cleanup()

    def git(self, *args):
        return mod.git(self.repo, *args)

    def put(self, path, content):
        p = self.repo / path
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_bytes(content if isinstance(content, bytes) else content.encode("utf-8"))

    def cli(self, *args, ok=True):
        p = subprocess.run([os.sys.executable, "-X", "utf8", "-B", str(SCRIPT), *args],
                           capture_output=True, text=True, encoding="utf-8")
        self.assertEqual(p.returncode, 0 if ok else 1, p.stdout + p.stderr)
        return json.loads(p.stdout)

    def collect(self):
        return self.cli("collect", "--repo", str(self.repo), "--name", "test/repo",
                        "--ref", "main", "--ref", "dev", "--source-path", "notes/decisions",
                        "--out", str(self.out))

    def index(self):
        return json.loads((self.out / "index.json").read_text(encoding="utf-8"))

    def row(self, path):
        return next((sid, r) for sid, r in self.index()["sources"].items()
                    if r["path"] == path and r["kind"] == "worktree"
                    and r["worktree"] == str(self.repo) and r.get("present"))

    def test_discovery_worktrees_ignored_originals_and_navigation(self):
        r = self.collect()
        self.assertTrue(r["coverage_complete"])
        rows = self.index()["sources"].values()
        self.assertFalse(any("sklearn" in x["path"] or "cached.md" in x["path"] for x in rows))
        self.assertTrue(any(x.get("ignored") and x["path"].endswith("ignored.md") for x in rows))
        self.assertTrue(any(x["path"] == "notes/decisions/custom.md" for x in rows))
        refs = {x.get("ref") for x in rows if x["path"].endswith("shared.md") and x["kind"] == "git"}
        self.assertEqual(refs, {"main", "dev"})
        kinds = {x["kind"] for x in self.index()["last_run"]["navigation"]}
        self.assertIn("missing-relative-target", kinds)
        self.assertIn("conflict-markers-candidate", kinds)
        self.assertTrue(self.index()["last_run"]["duplicate_content_groups"])
        sid, row = self.row("docs/经验 Learnings/shared.md")
        self.cli("restore", "--out", str(self.out), "--source-id", sid, "--dest", str(self.root / "restored"))
        self.assertEqual((self.root / "restored" / row["path"]).read_bytes(),
                         b"\xe5\x8e\x9f\xe6\x96\x87\r\nA condition and evidence.\r\n")
        sid, row = self.row("docs/经验 Learnings/image.bin")
        self.cli("restore", "--out", str(self.out), "--source-id", sid, "--dest", str(self.root / "restored"))
        self.assertEqual((self.root / "restored" / row["path"]).read_bytes(), b"\x00\xff\x01")

    def test_rerun_one_change_move_and_cleanup_guard(self):
        self.collect()
        old_ids = set(self.index()["sources"])
        r = self.collect()
        self.assertEqual(set(r["changes"]), {"unchanged"})
        self.assertEqual(set(self.index()["sources"]), old_ids)
        sid, old = self.row("docs/经验 Learnings/local.md")
        self.assertTrue(self.cli("check-cleanup", "--out", str(self.out), "--source-id", sid)["eligible"])
        self.put("docs/经验 Learnings/local.md", "new content; preserve concurrent edit\n")
        blocked = self.cli("check-cleanup", "--out", str(self.out), "--source-id", sid)
        self.assertFalse(blocked["eligible"])
        self.assertIn("preserve concurrent edit", (self.repo / "docs/经验 Learnings/local.md").read_text())
        r = self.collect()
        self.assertEqual(r["changes"].get("changed"), 1)
        original = self.repo / "docs/经验 Learnings/local.md"
        moved = self.repo / "docs/经验 Learnings/renamed.md"
        assert original.resolve().is_relative_to(self.root) and moved.resolve().is_relative_to(self.root)
        original.rename(moved)
        r = self.collect()
        self.assertEqual(r["changes"].get("moved"), 1)
        self.assertEqual(self.row("docs/经验 Learnings/renamed.md")[1]["entry_id"], old["entry_id"])

    def test_corrupt_receipt_and_restore_conflict_are_preserved(self):
        self.collect()
        sid, row = self.row("docs/经验 Learnings/shared.md")
        target = self.root / "restore" / row["path"]
        target.parent.mkdir(parents=True)
        target.write_text("existing user edit", encoding="utf-8")
        self.cli("restore", "--out", str(self.out), "--source-id", sid, "--dest", str(self.root / "restore"), ok=False)
        self.assertEqual(target.read_text(), "existing user edit")
        (self.out / "index.json").write_text("{corrupt", encoding="utf-8")
        self.cli("collect", "--repo", str(self.repo), "--name", "test/repo", "--out", str(self.out), ok=False)
        self.assertEqual((self.out / "index.json").read_text(), "{corrupt")

    def test_registered_unavailable_worktree_is_reported(self):
        self.collect()
        moved = self.root / "saved-worktree"
        assert self.wt.resolve().is_relative_to(self.root) and moved.resolve().is_relative_to(self.root)
        self.wt.rename(moved)
        r = self.collect()
        self.assertGreater(r["errors"], 0)
        self.assertFalse(r["coverage_complete"])

    def test_restore_junction_rejected_before_creating_any_outside_directory(self):
        self.collect()
        sid, row = self.row("docs/经验 Learnings/shared.md")
        restore_root, outside = self.root / "restore-target", self.root / "restore-outside"
        restore_root.mkdir()
        outside.mkdir()
        redirect = restore_root / "docs"
        assert redirect.parent.resolve().is_relative_to(self.root)
        assert outside.resolve().is_relative_to(self.root)
        if os.name == "nt":
            r = subprocess.run(["cmd", "/c", "mklink", "/J", str(redirect), str(outside)],
                               capture_output=True)
            self.assertEqual(r.returncode, 0, r.stderr)
        else:
            redirect.symlink_to(outside, target_is_directory=True)
        original_children = list(outside.iterdir())
        self.cli("restore", "--out", str(self.out), "--source-id", sid,
                 "--dest", str(restore_root), ok=False)
        self.assertEqual(list(outside.iterdir()), original_children)
        self.assertFalse((outside / "经验 Learnings").exists())
        self.assertTrue(redirect.exists())

    def test_remote_manifest_identity_integrity_and_migration(self):
        raw = self.root / "raw.md"
        raw.write_bytes(b"remote original\r\n")
        out = self.root / "remote-received"
        manifest = self.root / "remote.json"
        def run(paths):
            data = {"repository": "owner/project", "heads": {"main": "a"*40, "dev": "b"*40},
                    "complete_refs": ["main", "dev"],
                    "sources": [{"repository": "owner/project", "ref": ref, "commit": commit,
                                 "path": p, "file": str(raw), "sha256": mod.digest(raw.read_bytes())}
                                for ref, commit, p in paths]}
            manifest.write_text(json.dumps(data), encoding="utf-8")
            return self.cli("ingest", "--manifest", str(manifest), "--out", str(out))
        paths = [("main", "a"*40, "docs/Learnings/old.md"), ("dev", "b"*40, "docs/Learnings/old.md")]
        run(paths)
        r = run(paths)
        self.assertEqual(r["changes"], {"unchanged": 2})
        r = run([("main", "a"*40, "docs/Learnings/new.md"), paths[1]])
        self.assertEqual(r["changes"]["moved"], 1)
        self.assertEqual(len(list((out/"objects").iterdir())), 1)
        manifest.write_text(json.dumps({"sources": [{"repository": "owner/project", "ref": "main",
                          "commit": "a"*40, "path": "docs/Learnings/file.md", "file": str(raw), "sha256": "wrong"}]}))
        self.cli("ingest", "--manifest", str(manifest), "--out", str(out), ok=False)

    def test_receiver_inside_linked_worktree_source_rejected_without_writes(self):
        target = self.wt / "docs/经验 Learnings/self-intake"
        before = set((self.wt / "docs/经验 Learnings").iterdir())
        self.cli("collect", "--repo", str(self.repo), "--name", "test/repo",
                 "--out", str(target), ok=False)
        self.assertFalse(target.exists())
        self.assertEqual(set((self.wt / "docs/经验 Learnings").iterdir()), before)

    def test_partial_manifest_is_not_complete_and_ambiguous_move_is_not_guessed(self):
        raw = self.root / "raw.md"
        raw.write_bytes(b"one original")
        manifest = self.root / "manifest.json"
        out = self.root / "remote"
        def run(paths, complete):
            manifest.write_text(json.dumps({
                "repository": "owner/project", "heads": {"main": "a"*40},
                "complete_refs": ["main"] if complete else [],
                "sources": [{"repository": "owner/project", "ref": "main", "commit": "a"*40,
                             "path": p, "file": str(raw), "sha256": mod.digest(raw.read_bytes())}
                            for p in paths]}), encoding="utf-8")
            return self.cli("ingest", "--manifest", str(manifest), "--out", str(out))
        self.assertFalse(run(["Learnings/old.md"], False)["coverage_complete"])
        run(["Learnings/old.md"], True)
        result = run(["Learnings/copy-a.md", "Learnings/copy-b.md"], True)
        self.assertNotIn("moved", result["changes"])
        index = json.loads((out / "index.json").read_text(encoding="utf-8"))
        entries = [r["entry_id"] for r in index["sources"].values() if r["present"]]
        self.assertEqual(len(set(entries)), 2)


if __name__ == "__main__":
    unittest.main()

