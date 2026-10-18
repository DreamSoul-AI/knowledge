"""Archive one Codex session; adapted from the project's verified offline scripts."""

import argparse
from collections import Counter
import hashlib
import json
import os
from pathlib import Path
import re
import tempfile
from xml.etree import ElementTree


CONTEXT_KINDS = {
    "agents_md.instructions", "environments.environment_context",
    "additional_content.codex_apps_open_page",
}
TOOL_TYPES = {"custom_tool_call", "custom_tool_call_output", "function_call", "function_call_output"}


def digest(data):
    return hashlib.sha256(data).hexdigest()


def encode(value):
    return (json.dumps(value, ensure_ascii=False, indent=2) + "\n").encode("utf-8")


def read_json(path):
    return json.loads(path.read_text(encoding="utf-8-sig"))


def public_output(value):
    if isinstance(value, str):
        return [{"type": "input_text", "text": value}]
    if not isinstance(value, list):
        raise ValueError("Unsupported tool output shape")
    return [part if part.get("type") in {"input_text", "output_text"}
            else {"type": part.get("type"), "omitted": "non-text content"} for part in value]


def extract(data, session_id, through_id=None):
    events, excluded, warnings = [], Counter(), []
    session_seen = cutoff_found = False
    for number, line in enumerate(data.splitlines(keepends=True), 1):
        if not line.endswith(b"\n"):
            warnings.append("末尾未完成行未处理，下次读取时重试")
            break
        row = json.loads(line)
        p = row.get("payload", {})
        if row.get("type") == "session_meta":
            if p.get("id", p.get("session_id")) != session_id:
                raise ValueError("Source session ID does not match request")
            session_seen = True
        if row.get("type") != "response_item":
            continue
        if not session_seen:
            raise ValueError("Missing session_meta before response records")
        kind = p.get("type")
        event = None
        if kind in {"reasoning", "additional_tools"}:
            excluded[kind] += 1
        elif kind == "message":
            role, phase = p.get("role"), p.get("phase")
            meta = p.get("internal_chat_message_metadata_passthrough") or {}
            if role == "user":
                kinds = set(meta.get("content_item_kinds", []))
                if "user.text" in kinds:
                    selected = "user"
                elif kinds and kinds <= CONTEXT_KINDS:
                    excluded["injected_context"] += 1
                    selected = None
                else:
                    raise ValueError(f"Unknown user provenance at line {number}: {sorted(kinds)}")
            elif role == "assistant" and phase in {"commentary", "final_answer"}:
                if p.get("status") != "completed":
                    warnings.append("尚未完成的回复及其后记录留待下次读取")
                    break
                selected = phase
            elif role in {"system", "developer"}:
                excluded["system_or_developer"] += 1
                selected = None
            else:
                raise ValueError(f"Unknown message role/phase at line {number}: {role}/{phase}")
            if selected:
                content = p.get("content", [])
                text = "".join(part["text"] for part in content
                               if part.get("type") in {"input_text", "output_text"})
                nontext = [part.get("type") for part in content
                           if part.get("type") not in {"input_text", "output_text"}]
                if nontext:
                    warnings.append(f"{p.get('id')}: 非文字内容未取得原件：{nontext}")
                if (selected == "user" and text.lstrip().startswith("# Files pasted by the user:")
                        and "## My request:" in text and not text.split("## My request:")[-1].strip()):
                    selected = "attachment_context"
                event = {"kind": selected, "text": text, "nontext": nontext}
        elif kind in TOOL_TYPES:
            event = {"kind": "tool_output" if kind.endswith("output") else "tool_call",
                     "call_id": p.get("call_id"), "tool_type": kind}
            if kind.endswith("output"):
                output = public_output(p.get("output", []))
                event["output"] = output
                text = "".join(part.get("text", "") for part in output)
                if kind == "function_call_output" and text.startswith("<codex_delegation>"):
                    relay = ElementTree.fromstring(text)
                    event = {"kind": "relay", "text": relay.findtext("input"),
                             "source_thread_id": relay.findtext("source_thread_id"),
                             "source_tool": p.get("name", "function_call_output")}
                    if event["text"] is None or not event["source_thread_id"]:
                        raise ValueError("Relay lacks original text or source")
            else:
                event.update(name=p.get("name"), namespace=p.get("namespace"),
                             input=p.get("input", p.get("arguments")))
        else:
            raise ValueError(f"Unsupported response record type at line {number}: {kind}")
        if event:
            if not p.get("id"):
                raise ValueError(f"Selected record lacks stable ID at line {number}")
            event.update(id=p["id"], recorded_timestamp=row.get("timestamp"),
                         source_line=number)
            events.append(event)
        if through_id is not None and p.get("id") == through_id:
            cutoff_found = True
            break
    if not session_seen or (through_id and not cutoff_found):
        raise ValueError("Session metadata or requested cutoff not found in complete records")
    if not events:
        raise ValueError("No public records selected")
    ids = [event["id"] for event in events]
    if len(ids) != len(set(ids)):
        raise ValueError("Duplicate source record IDs")
    return events, dict(excluded), warnings


def check_increment(old, new):
    """Same-ID changes or lost/reordered history must not overwrite a valid archive."""
    if len(new) < len(old) or old != new[:len(old)]:
        raise ValueError("Archived records changed, disappeared or reordered; retain previous version")
    return len(new) - len(old)


def quoted(text):
    # Escape Markdown inside operation quotes; the inverse is checked before publishing.
    escaped = re.sub(r"([\\`*_{}\[\]()#+.!>|~=-])", r"\\\1", text)
    return "\n".join("> " + line for line in escaped.split("\n"))


def unquoted(value):
    return re.sub(r"\\([\\`*_{}\[\]()#+.!>|~=-])", r"\1",
                  "\n".join(line[2:] for line in value.split("\n")))


def fence(text):
    marker = "`" * max(3, 1 + max((len(x) for x in re.findall(r"`+", text)), default=0))
    return marker + "text\n", "\n" + marker + "\n"


def conflicts(text):
    marker = None
    previous = ""
    for line in text.splitlines():
        opening = re.match(r"^ {0,3}(`{3,}|~{3,})(.*)$", line)
        if opening:
            run, tail = opening.groups()
            if marker is None:
                marker = run
            elif run[0] == marker[0] and len(run) >= len(marker) and not tail.strip():
                marker = None
            previous = ""
            continue
        if marker:
            continue
        if re.match(r"^ {0,3}#{1,4}(?:\s|$)", line):
            return True
        if previous.strip() and re.fullmatch(r" {0,3}(?:=+|-+)\s*", line):
            return True
        previous = line
    return marker is not None


def command_results(output):
    """Reuse the sample's structured-result detection; never parse embedded logs recursively."""
    results = []

    def visit(value):
        if isinstance(value, dict):
            if {"chunk_id", "exit_code", "output"} <= value.keys():
                results.append({"exit_code": value["exit_code"], "output": value["output"]})
            else:
                for child in value.values():
                    visit(child)
        elif isinstance(value, list):
            for child in value:
                visit(child)

    decoder = json.JSONDecoder()
    for part in output:
        text = part.get("text", "").lstrip()
        while text.startswith(("{", "[")):
            try:
                value, end = decoder.raw_decode(text)
            except json.JSONDecodeError:
                break
            visit(value)
            text = text[end:].lstrip()
    return results


def render(events, summary, session, title):
    if not summary.startswith("# 一、流程摘要\n") or re.search(r"(?m)^# 二、沟通记录", summary):
        raise ValueError("Summary must contain only the first section")
    document = summary.rstrip() + (
        f"\n\n记录范围：会话 `{session}`，截止记录 `{events[-1]['id']}`。\n\n"
        "原文与工具证据：[公开记录](archive.json)、[完整工具记录](tools.json)、[核对报告](verification.json)。"
        "本地 Markdown 不保存默认折叠状态。\n\n# 二、沟通记录\n\n")
    spans, agent_open, operations_open, fenced = [], False, False, []
    for event in events:
        kind = event["kind"]
        if kind in {"user", "attachment_context"}:
            document += "## 用户\n\n"
            agent_open = operations_open = False
        elif not agent_open:
            document += "### Agent\n\n"
            agent_open = True
        if kind in {"commentary", "tool_call", "tool_output"}:
            if not operations_open:
                document += "#### 推理与操作记录\n\n"
                operations_open = True
            if kind.startswith("tool_"):
                label = "工具调用" if kind == "tool_call" else "工具返回"
                detail = label + " " + event["id"]
                if kind == "tool_call":
                    detail += "：" + str(event.get("namespace") or "") + "." + str(event.get("name"))
                else:
                    text = "".join(p.get("text", "") for p in event["output"])
                    results = command_results(event["output"])
                    if results:
                        detail += "；退出码：" + "、".join(str(r["exit_code"]) for r in results)
                    if "truncated" in text.lower():
                        detail += "；原返回含截断标记，缺失内容未补写"
                    for result in results:
                        if result["exit_code"] not in (0, None) and result["output"]:
                            document += quoted("非零退出的实际输出：\n" + result["output"]) + "\n\n"
                document += quoted(detail) + "\n>\n> 完整可取得参数或返回见 [工具记录](tools.json)。\n\n"
                continue
            text, transformation = quoted(event["text"]), "escaped_quote"
        else:
            operations_open = False
            if kind == "final_answer":
                document += "#### 正式回复\n\n"
            elif kind == "relay":
                document += ("**转达消息开始（Agent 转达，非用户直接发言）**\n\n"
                             f"来源会话 ID：`{event['source_thread_id']}`；来源工具：`{event['source_tool']}`。\n\n")
            elif kind == "attachment_context":
                document += "### 附件与上下文\n\n平台提供的附件包装，非用户直接发言。\n\n"
            text, transformation = event["text"], "none"
            if kind == "attachment_context" or conflicts(text):
                opening, closing = fence(text)
                document += opening
                fenced.append(event["id"])
            else:
                closing = ""
        start = len(document)
        document += text
        spans.append({"id": event["id"], "kind": kind, "start": start, "end": len(document),
                      "sha256": digest(event["text"].encode("utf-8")), "transformation": transformation})
        if kind != "commentary":
            document += closing
        document += "\n\n"
        if kind == "relay":
            document += "**转达消息结束**\n\n"
    originals = {e["id"]: e["text"] for e in events if "text" in e}
    if len(spans) != len(originals):
        raise ValueError("Not every original message was rendered")
    for span in spans:
        value = document[span["start"]:span["end"]]
        if span["transformation"] == "escaped_quote":
            value = unquoted(value)
        if value != originals[span["id"]]:
            raise ValueError("Original text altered: " + span["id"])
    return document, spans, fenced


def default_summary():
    return ("# 一、流程摘要\n\n## （一）沟通目标\n\n待根据公开记录整理。\n\n"
            "## （二）流程演进\n\n待根据公开记录整理。\n\n"
            "## （三）关键决策\n\n原话由程序写入，摘要不得替代原始记录。\n\n"
            "## （四）主要产出\n\n本地 Markdown、公开记录与核对报告。\n")


def run(source, session, title, output, rules, through_id=None, summary=None):
    if not re.fullmatch(r"[\w\u4e00-\u9fff ()（）.-]+", title) or title in {".", ".."}:
        raise ValueError("Title must be a safe local filename")
    rules_bytes = rules.read_bytes()
    if "#### 推理与操作记录" not in rules_bytes.decode("utf-8-sig"):
        raise ValueError("Rules do not contain the supported H4 operation layout")
    data = source.read_bytes()
    events, exclusions, warnings = extract(data, session, through_id)
    output.mkdir(parents=True, exist_ok=True)
    pointer = output / "current.json"
    previous = None
    if pointer.exists():
        previous = read_json(pointer)
        version_name = previous["version"]
        if not re.fullmatch(r"[a-f0-9]{64}", version_name):
            raise ValueError("Invalid archive version path")
        old_dir = output / "versions" / version_name
        for name, sha in previous["files"].items():
            if Path(name).name != name or digest((old_dir / name).read_bytes()) != sha:
                raise ValueError("Previously generated artifact changed; preserve manual edits")
        old = read_json(old_dir / "archive.json")
        if old["session_id"] != session:
            raise ValueError("Output directory belongs to another session")
        added = check_increment(old["events"], events)
    else:
        added = len(events)
    summary_text = summary.read_text(encoding="utf-8-sig") if summary else default_summary()
    document, spans, fenced = render(events, summary_text, session, title)
    archive = {"session_id": session, "events": events}
    archive_bytes = encode(archive)
    version = digest(archive_bytes + document.encode("utf-8") + rules_bytes + title.encode("utf-8"))
    target = output / "versions" / version
    filename = "AI 沟通流程 " + title + ".md"
    counts = dict(Counter(e["kind"] for e in events))
    if previous and previous["version"] == version:
        return {"added": 0, "changed": False, "counts": counts, "document": str(target / filename)}
    verification = {"session_id": session, "source_sha256": digest(data), "cutoff_id": events[-1]["id"],
                    "rules_sha256": digest(rules_bytes), "counts": counts, "added": added,
                    "previous_version": previous["version"] if previous else None,
                    "original_message_checks": len(spans), "all_original_text_exact": True,
                    "message_spans": spans, "fenced_original_messages": fenced,
                    "exclusions": exclusions, "warnings": warnings,
                    "summary_provided": bool(summary), "default_fold_in_markdown": False,
                    "limits": ["Only available source records checked; no fresh UI export comparison",
                               "Non-text attachments not copied", "Truncated source output not reconstructed",
                               "Unknown Codex record formats stop processing", "No cloud sync or scheduling"]}
    files = {"archive.json": archive_bytes, filename: document.encode("utf-8"),
             "tools.json": encode([e for e in events if e["kind"].startswith("tool_")]),
             "verification.json": encode(verification)}
    target.mkdir(parents=True, exist_ok=True)
    for name, value in list(files.items()):
        path = target / name
        if path.exists():
            existing = path.read_bytes()
            if existing != value:
                if name != "verification.json":
                    raise ValueError("Version collision or edited uncommitted artifact")
                old_report, new_report = json.loads(existing), json.loads(value)
                for field in ["source_sha256", "added", "previous_version"]:
                    old_report.pop(field, None)
                    new_report.pop(field, None)
                if old_report != new_report:
                    raise ValueError("Existing version verification changed")
            files[name] = existing
        else:
            path.write_bytes(value)
    commit = {"session_id": session, "version": version, "document": filename,
              "files": {name: digest(value) for name, value in files.items()}}
    # Immutable versions retain the previous committed archive if a write fails.
    with tempfile.NamedTemporaryFile(dir=output, delete=False) as temporary:
        temporary.write(encode(commit))
        temporary_name = temporary.name
    try:
        os.replace(temporary_name, pointer)
    finally:
        Path(temporary_name).unlink(missing_ok=True)
    return {"added": added, "changed": True, "counts": counts, "document": str(target / filename)}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    for argument in ["source", "session", "title", "output"]:
        parser.add_argument("--" + argument, required=True, type=Path if argument in {"source", "output"} else str)
    parser.add_argument("--rules", type=Path,
                        default=Path(__file__).resolve().parents[1] / "references" / "archive-standard.md",
                        help="Workspace standard; defaults to the bundled archive standard")
    parser.add_argument("--through-id")
    parser.add_argument("--summary", type=Path)
    args = parser.parse_args()
    print(json.dumps(run(**vars(args)), ensure_ascii=True))


if __name__ == "__main__":
    main()
