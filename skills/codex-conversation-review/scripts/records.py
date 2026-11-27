"""Public Codex record preparation, shared by review and lossless archiving."""

from collections import Counter
from datetime import datetime, timedelta, timezone
import hashlib
import json
from pathlib import Path
import re
from xml.etree import ElementTree

CONTEXT_KINDS = {
    "agents_md.instructions", "environments.environment_context",
    "additional_content.codex_apps_open_page",
    "skills.selected_skill_instructions",
}
TOOL_TYPES = {"custom_tool_call", "custom_tool_call_output", "function_call", "function_call_output"}


def public_output(value):
    if isinstance(value, str):
        return [{"type": "input_text", "text": value}]
    if not isinstance(value, list):
        raise ValueError("Unsupported tool output shape")
    return [part if part.get("type") in {"input_text", "output_text"}
            else {"type": part.get("type"), "omitted": "non-text content"} for part in value]


def known_goal_context(payload, meta, kinds):
    """Recognize harness-origin goal context without discarding unknown user records."""
    wrappers = {"goal.internal_context": "goal", "user.goal": "user_goal"}
    if len(kinds) != 1 or not kinds <= wrappers.keys():
        return None
    provenance = meta.get("content_item_metadata", [])
    if not provenance or any(item.get("provenance", {}).get("type") != "harness"
                             for item in provenance):
        return None
    content = payload.get("content", [])
    if not content or any(part.get("type") != "input_text" for part in content):
        return None
    text = "".join(part.get("text", "") for part in content).strip()
    source_kind = next(iter(kinds))
    if not (text.startswith('<codex_internal_context source="' + wrappers[source_kind] + '">')
            and text.endswith("</codex_internal_context>")):
        return None
    return "injected_context" if source_kind == "goal.internal_context" else "goal_lifecycle_context"


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
        elif kind == "configuration_update" and set(p) <= {"type", "reasoning"} and isinstance(p.get("reasoning"), dict):
            excluded[kind] += 1
        elif kind == "agent_message":
            meta = p.get("internal_chat_message_metadata_passthrough") or {}
            provenance = meta.get("content_item_metadata", [])
            if (not provenance or not p.get("author", "").startswith("/root")
                    or not p.get("recipient", "").startswith("/root")
                    or any(item.get("provenance") != {"type": "tool", "namespace": "collaboration"}
                           for item in provenance)):
                raise ValueError(f"Unknown internal agent-message provenance at line {number}")
            excluded[kind] += 1
        elif kind == "message":
            role, phase = p.get("role"), p.get("phase")
            meta = p.get("internal_chat_message_metadata_passthrough") or {}
            if role == "user":
                kinds = set(meta.get("content_item_kinds", []))
                if "user.text" in kinds:
                    selected = "user"
                elif known_goal_context(p, meta, kinds):
                    excluded[known_goal_context(p, meta, kinds)] += 1
                    selected = None
                elif kinds and all(k in CONTEXT_KINDS or re.fullmatch(
                        r"additional_content\.codex_apps_selected_page_part_[1-9]\d*_of_[1-9]\d*", k)
                        for k in kinds):
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


def display_timezone(offset):
    if not re.fullmatch(r"[+-]\d{2}:\d{2}", offset):
        raise ValueError("UTC offset must use +HH:MM or -HH:MM")
    hours, minutes = map(int, offset[1:].split(":"))
    if hours > 23 or minutes > 59:
        raise ValueError("Invalid UTC offset")
    delta = timedelta(hours=hours, minutes=minutes)
    return timezone(delta if offset[0] == "+" else -delta)


def message_time(stamp, zone):
    if not isinstance(stamp, str):
        return None
    try:
        value = datetime.fromisoformat(stamp.replace("Z", "+00:00"))
        if value.tzinfo is None:
            return None
        return value.astimezone(zone).strftime("%Y-%m-%d %H:%M:%S")
    except (ValueError, OverflowError):
        return None


def duration_text(milliseconds):
    seconds = (milliseconds + 500) // 1000
    hours, remaining = divmod(seconds, 3600)
    minutes, seconds = divmod(remaining, 60)
    if hours:
        return f"{hours} 小时 {minutes:02d} 分 {seconds:02d} 秒"
    if minutes:
        return f"{minutes} 分 {seconds:02d} 秒"
    return f"{seconds} 秒"


def collect_timing(data, events, utc_offset):
    """Read lifecycle metadata only through the same public-record cutoff."""
    zone = display_timezone(utc_offset)
    needed = {e["source_line"]: e for e in events if e["kind"] in {"user", "final_answer"}}
    messages, tasks, warnings = {}, {}, []
    active = None
    prefix = hashlib.sha256()
    cutoff_line = events[-1]["source_line"]
    for number, line in enumerate(data.splitlines(keepends=True), 1):
        if number > cutoff_line:
            break
        prefix.update(line)
        row = json.loads(line)
        payload = row.get("payload") or {}
        kind = payload.get("type")
        if row.get("type") == "event_msg" and kind == "task_started":
            active = payload.get("turn_id")
            if active:
                if active in tasks:
                    raise ValueError("Repeated task_started for the same turn")
                tasks[active] = {"started": row.get("timestamp"), "started_epoch": payload.get("started_at")}
        elif row.get("type") == "event_msg" and kind in {"task_complete", "turn_aborted"}:
            turn_id = payload.get("turn_id")
            task = tasks.get(turn_id)
            duration = payload.get("duration_ms")
            if task is not None:
                if ("ended" in task or task["started_epoch"] != payload.get("started_at")
                        or type(duration) is not int or duration < 0):
                    raise ValueError("Inconsistent native turn timing")
                task.update(ended=row.get("timestamp"), duration_ms=duration,
                            status="complete" if kind == "task_complete" else "aborted")
            if turn_id == active:
                active = None
        if number in needed:
            event = needed[number]
            if payload.get("id") != event["id"] or row.get("timestamp") != event["recorded_timestamp"]:
                raise ValueError("Timeline does not match archived message")
            messages[event["id"]] = {"turn_id": active, "source_line": number,
                                      "recorded_timestamp": event["recorded_timestamp"], "kind": event["kind"]}
    finals = Counter(m["turn_id"] for m in messages.values() if m["kind"] == "final_answer")
    last_users = {m["turn_id"]: identifier for identifier, m in messages.items() if m["kind"] == "user"}
    for identifier, entry in messages.items():
        stamp = message_time(entry["recorded_timestamp"], zone)
        entry["display"] = stamp or "时间未记录"
        if stamp is None:
            warnings.append(f"{identifier}: 原始时间缺失、无时区或无效，未推测")
        turn_id = entry["turn_id"]
        task = tasks.get(turn_id, {})
        if entry["kind"] == "final_answer":
            if turn_id and task.get("status") == "complete" and finals[turn_id] == 1:
                entry.update(turn_status="complete", duration_ms=task["duration_ms"])
                entry["display"] += " · 本轮耗时 " + duration_text(task["duration_ms"])
            else:
                entry["display"] += " · 本轮耗时未记录"
        elif task.get("status") == "aborted" and last_users[turn_id] == identifier:
            entry.update(turn_status="aborted", duration_ms=task["duration_ms"])
            ended = message_time(task.get("ended"), zone) or "时间未记录"
            entry["display"] += f" · 本轮中断于 {ended}，耗时 {duration_text(task['duration_ms'])}"
    note = ("消息时间均为北京时间（UTC+08:00）。" if utc_offset == "+08:00"
            else f"消息时间均为 UTC{utc_offset}。")
    note += "整轮耗时取 Codex 记录的任务耗时，包含执行和等待，缺失时不推算。"
    return {"utc_offset": utc_offset, "cutoff_id": events[-1]["id"],
            "source_prefix_sha256": prefix.hexdigest(), "note": note,
            "messages": messages,
            "tasks": {k: v for k, v in tasks.items() if k in finals or k in last_users}}, warnings


def archive_summary_template():
    return ("# 一、流程摘要\n\n待根据公开记录整理沟通目标、主线、结果与未完事项，本占位内容不能作为正式交付。\n\n"
            "## （一）流程演进\n\n待绘制基于实际记录的流程图，并解释关键转折。\n\n"
            "## （二）关键决策\n\n待整理已确认选择、依据与边界。\n\n"
            "## （三）主要产出\n\n待核对成果入口、完成状态与未完事项。\n\n"
            "## （四）反思与经验\n\n待从记录提炼有依据的问题、有效做法与适用条件。\n")


def locate_source(session, source=None, sessions_root=None):
    """Locate only the requested session; never search other conversations' text."""
    if source is not None:
        path = Path(source)
        if not path.is_file():
            raise FileNotFoundError("Session source not found: " + str(path))
        return path
    if sessions_root is None:
        raise ValueError("Supply --source or the known --sessions-root for this session")
    if not re.fullmatch(r"[A-Za-z0-9-]+", session):
        raise ValueError("Session ID must not contain path or glob characters")
    root = Path(sessions_root)
    if not root.is_dir():
        raise FileNotFoundError("Sessions root not found: " + str(root))
    matches = sorted(p for p in root.rglob("*" + session + "*.jsonl") if p.is_file())
    if len(matches) != 1:
        raise ValueError(f"Expected one source for session {session}; found {len(matches)}. Supply --source.")
    return matches[0]


def prepare(source, session, through_id=None, utc_offset="+08:00"):
    """Return full traceable public records, never a replacement summary."""
    data = Path(source).read_bytes()
    events, exclusions, warnings = extract(data, session, through_id)
    timing, timing_warnings = collect_timing(data, events, utc_offset)
    return {"session_id": session, "source_sha256": hashlib.sha256(data).hexdigest(),
            "through_id": events[-1]["id"], "events": events,
            "exclusions": exclusions, "warnings": warnings + timing_warnings,
            "timing": timing}
