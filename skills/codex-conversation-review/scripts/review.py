"""Read a bounded page of traceable public Codex records without creating an archive."""

import argparse
import json
from pathlib import Path

from records import locate_source, prepare


def page(prepared, offset=0, limit=40, view="messages", expect_prefix_sha256=None):
    if offset < 0 or not 1 <= limit <= 200:
        raise ValueError("Use a nonnegative offset and a limit from 1 to 200")
    if view not in {"messages", "records"}:
        raise ValueError("Unknown record view")
    prefix = prepared["timing"]["source_prefix_sha256"]
    if expect_prefix_sha256 and prefix != expect_prefix_sha256:
        raise ValueError("Source prefix changed; retain the previous read and reconcile before continuing")
    events = prepared["events"]
    items = events if view == "records" else [e for e in events if e["kind"] in {
        "user", "final_answer", "commentary", "relay", "attachment_context"}]
    end = min(offset + limit, len(items))
    return {"session_id": prepared["session_id"], "through_id": prepared["through_id"],
            "source_sha256": prepared["source_sha256"], "source_prefix_sha256": prefix,
            "view": view, "total_public_records": len(events), "total_items": len(items),
            "offset": offset, "next_offset": end if end < len(items) else None,
            "warnings": prepared["warnings"], "exclusions": prepared["exclusions"],
            "items": items[offset:end]}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source", type=Path)
    parser.add_argument("--sessions-root", type=Path, help="Known sessions directory; only the requested ID is matched")
    parser.add_argument("--session", required=True)
    parser.add_argument("--through-id")
    parser.add_argument("--utc-offset", default="+08:00")
    parser.add_argument("--offset", type=int, default=0)
    parser.add_argument("--limit", type=int, default=40)
    parser.add_argument("--view", choices=["messages", "records"], default="messages")
    parser.add_argument("--expect-prefix-sha256")
    args = parser.parse_args()
    source = locate_source(args.session, args.source, args.sessions_root)
    prepared = prepare(source, args.session, args.through_id, args.utc_offset)
    print(json.dumps(page(prepared, args.offset, args.limit, args.view,
                          args.expect_prefix_sha256), ensure_ascii=True))


if __name__ == "__main__":
    main()
