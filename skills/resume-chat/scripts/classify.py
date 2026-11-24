"""Classify read-only thread snapshots. The caller supplies verified stop intent."""
import json
import sys
from pathlib import Path

def classify(thread, stop_intent="unknown"):
    turns = thread.get("turns", [])
    if not turns:
        return "review"
    status = turns[-1].get("status")
    if status in ("inProgress", "in_progress"):
        return "running"
    if status == "completed":
        return "closed_or_waiting"
    if status != "interrupted":
        return "review"
    if stop_intent in ("user_pause", "user_stop"):
        return "excluded_by_user"
    if stop_intent != "execution_interruption":
        return "review"
    return "resume_candidate"

if __name__ == "__main__":
    records = json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))
    print(json.dumps([dict(id=r["thread"]["id"], decision=classify(r["thread"], r.get("stop_intent", "unknown"))) for r in records], ensure_ascii=False, indent=2))
