"""Synthetic boundary tests; real-session integration evidence is saved separately."""

import json
import subprocess
import sys
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

import archive


def message(identifier, text, role="user", phase=None):
    return {"type": "response_item", "payload": {
        "type": "message", "id": identifier, "role": role, "phase": phase,
        "status": "completed", "content": [{"type": "input_text", "text": text}],
        "internal_chat_message_metadata_passthrough": {"content_item_kinds": ["user.text"]}}}


def source(*records):
    rows = [{"type": "session_meta", "payload": {"id": "session-one"}}, *records]
    return b"".join(archive.encode(row).replace(b"\n", b" ") + b"\n" for row in rows)


class ArchiveTests(unittest.TestCase):
    def test_explicit_skill_injection_is_not_user_speech(self):
        injected = message("skill-context", "INJECTED_SKILL_INSTRUCTIONS")
        injected["payload"]["internal_chat_message_metadata_passthrough"]["content_item_kinds"] = [
            "skills.selected_skill_instructions"]
        direct = message("u1", "用 $codex-conversation-archive 归档，原话不能改。")
        records, exclusions, _ = archive.extract(source(injected, direct), "session-one", "u1")
        self.assertEqual([r["id"] for r in records], ["u1"])
        self.assertEqual(records[0]["text"], direct["payload"]["content"][0]["text"])
        self.assertEqual(exclusions["injected_context"], 1)
        injected["payload"]["internal_chat_message_metadata_passthrough"]["content_item_kinds"].append("future.unknown")
        with self.assertRaises(ValueError):
            archive.extract(source(injected, direct), "session-one")

    def test_standalone_cli_uses_bundled_rules(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            raw = root / "source.jsonl"
            raw.write_bytes(source(message("u1", "独立安装的用户原话。\n"),
                                   message("a1", "正式回复保持原样。\n", "assistant", "final_answer")))
            command = [sys.executable, "-I", "-S", "-B", "-X", "utf8", str(Path(archive.__file__).resolve()),
                       "--source", str(raw), "--session", "session-one", "--title", "首次归档",
                       "--output", str(root / "output")]
            first = subprocess.run(command, cwd=root, capture_output=True, text=True, check=True)
            result = json.loads(first.stdout)
            self.assertEqual(result["added"], 2)
            self.assertIn("独立安装的用户原话。\n", Path(result["document"]).read_text(encoding="utf-8"))
            second = json.loads(subprocess.run(command, cwd=root, capture_output=True, text=True, check=True).stdout)
            self.assertFalse(second["changed"])
            self.assertEqual(second["added"], 0)
            invalid = subprocess.run(command + ["--rules", str(root / "missing.md")],
                                     cwd=root, capture_output=True, text=True)
            self.assertNotEqual(invalid.returncode, 0)

    def test_text_order_and_hidden_exclusion(self):
        original = "# 原文标题\n\n- 用户列表，不能改！\n```\ncode\n```\n"
        reply = "正式回复原话。\n"
        records = source(message("u1", original),
                         {"type": "response_item", "payload": {"type": "reasoning", "text": "HIDDEN_SENTINEL"}},
                         message("a1", reply, "assistant", "final_answer"))
        events, exclusions, _ = archive.extract(records, "session-one")
        doc, spans, fenced = archive.render(events, archive.default_summary(), "session-one", "test")
        self.assertNotIn("HIDDEN_SENTINEL", doc)
        self.assertEqual(exclusions["reasoning"], 1)
        self.assertEqual([x["id"] for x in spans], ["u1", "a1"])
        self.assertEqual(fenced, ["u1"])
        self.assertEqual(doc[spans[0]["start"]:spans[0]["end"]], original)
        self.assertEqual(doc[spans[1]["start"]:spans[1]["end"]], reply)

    def test_repeat_increment_and_changed_history(self):
        a, _, _ = archive.extract(source(message("u1", "first")), "session-one")
        b, _, _ = archive.extract(source(message("u1", "first"), message("u2", "next")), "session-one")
        self.assertEqual(archive.check_increment(a, a), 0)
        self.assertEqual(archive.check_increment(a, b), 1)
        for invalid in [[], [dict(a[0], text="changed")], list(reversed(b))]:
            with self.assertRaises(ValueError):
                archive.check_increment(a, invalid)

    def test_normal_reply_formatting_not_fenced(self):
        self.assertFalse(archive.conflicts("结论：\n\n- 第一项\n- 第二项\n\n```md\n# 代码示例里的标题\n```\n"))
        self.assertTrue(archive.conflicts("标题\n=====\n"))
        self.assertTrue(archive.conflicts("```\n未闭合"))

    def test_unknown_provenance_and_incomplete_lines(self):
        bad = message("u", "unknown")
        bad["payload"]["internal_chat_message_metadata_passthrough"] = {}
        with self.assertRaises(ValueError):
            archive.extract(source(bad), "session-one")
        good = source(message("u", "kept"))
        events, _, warnings = archive.extract(good + b'{"unfinished":', "session-one")
        self.assertEqual(len(events), 1)
        self.assertTrue(warnings)
        with self.assertRaises(json.JSONDecodeError):
            archive.extract(good + b'{invalid}\n', "session-one")
        with self.assertRaises(ValueError):
            archive.extract(good, "wrong-session")
        with self.assertRaises(ValueError):
            archive.extract(good, "session-one", "missing-cutoff")
        pending = message("a2", "partial", "assistant", "final_answer")
        pending["payload"]["status"] = "in_progress"
        events, _, warnings = archive.extract(good + source(pending).split(b"\n", 1)[1], "session-one")
        self.assertEqual([x["id"] for x in events], ["u"])
        self.assertTrue(warnings)

    def test_relay_images_and_escaped_quote(self):
        relay = {"type": "response_item", "payload": {"type": "function_call_output", "id": "r1",
                 "call_id": "c1", "output": "<codex_delegation><source_thread_id>origin</source_thread_id>"
                 "<input>转达原话 &amp; 内容</input></codex_delegation>"}}
        events, _, _ = archive.extract(source(relay), "session-one")
        self.assertEqual(events[0]["text"], "转达原话 & 内容")
        self.assertEqual(events[0]["source_thread_id"], "origin")
        self.assertEqual(archive.public_output([{"type": "input_image", "image_url": "SECRET_IMAGE"}]),
                         [{"type": "input_image", "omitted": "non-text content"}])
        for text in ["  indent\n> - item\n", "a\\b `code` \n\n", "*x* [link](path)", "error\n====\n~~~"]:
            self.assertEqual(archive.unquoted(archive.quoted(text)), text)
        self.assertNotIn("> ====", archive.quoted("error\n===="))

    def test_atomic_pointer_and_manual_edits(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            raw, rules, out = root / "source.jsonl", root / "rules.md", root / "out"
            raw.write_bytes(source(message("u", "first")))
            rules.write_text("#### 推理与操作记录", encoding="utf-8")
            kwargs = dict(source=raw, session="session-one", title="测试", output=out, rules=rules)
            first = archive.run(**kwargs)
            pointer_bytes = (out / "current.json").read_bytes()
            second = archive.run(**kwargs)
            self.assertFalse(second["changed"])
            self.assertEqual(second["added"], 0)
            self.assertEqual(pointer_bytes, (out / "current.json").read_bytes())
            raw.write_bytes(source(message("u", "first"), message("u2", "new")))
            third = archive.run(**kwargs)
            self.assertEqual(third["added"], 1)
            self.assertTrue(Path(first["document"]).is_file())
            old_pointer = (out / "current.json").read_bytes()
            Path(third["document"]).write_text("manual edit", encoding="utf-8")
            with self.assertRaises(ValueError):
                archive.run(**kwargs)
            self.assertEqual(old_pointer, (out / "current.json").read_bytes())

    def test_failed_commit_keeps_old_version_and_can_retry(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            raw, rules, out = root / "source.jsonl", root / "rules.md", root / "out"
            raw.write_bytes(source(message("u", "first")))
            rules.write_text("#### 推理与操作记录", encoding="utf-8")
            kwargs = dict(source=raw, session="session-one", title="测试", output=out, rules=rules)
            archive.run(**kwargs)
            before = (out / "current.json").read_bytes()
            raw.write_bytes(source(message("u", "first"), message("u2", "new")))
            with patch.object(archive.os, "replace", side_effect=OSError("simulated write failure")):
                with self.assertRaises(OSError):
                    archive.run(**kwargs)
            self.assertEqual(before, (out / "current.json").read_bytes())
            self.assertEqual(archive.run(**kwargs)["added"], 1)


if __name__ == "__main__":
    unittest.main()
