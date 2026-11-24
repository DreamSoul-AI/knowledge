# resume-chat

Reconnect interrupted work to its existing context. Inspect the current request, verified stop reason, recent relevant turns and necessary artifacts before choosing a short continuation, a changed requirement, a clarification or no resume action.

# 1. Use

Invoke `$resume-chat`. When migrating an installation named `resume-interrupted-chat`, preserve personal changes before switching the complete directory, and retain only one discoverable skill entry.

- “Continue this interrupted task with the original requirements.”
- “Resume that chat, but return JSON. Keep the other requirements.”
- “Inspect these chats for interrupted work without sending messages.”
- “Resume the item I previously paused, within its original scope.”

Continue directly in the current chat. For another chat, verify its identity and context before messaging. Send `resume` when its requirements and next step are already clear. Supply only necessary changes otherwise. An inspection request does not authorize resuming work.

A user pause or stop is not an accidental execution failure. A new explicit resume request may authorize continuation without another redundant confirmation. Preserve the historical stop reason rather than relabeling it to pass a filter. Observe running work and address required input or approval instead of restarting it.

The `completed` status describes a turn. It does not prove the whole task is done: the turn may have asked a question or completed one stage. Check the actual output and artifacts.

# 2. Distinct mechanisms

Messaging a desktop chat, continuing the current chat and resuming a CLI session are different operations. For CLI recovery, consult the installed CLI help and select the correct existing session. Reload applicable instructions and necessary files after compaction or an environment change, without discarding confirmed task facts. Success through one mechanism does not validate all the others.

# 3. Optional snapshot filter

`scripts/classify.py` reads a JSON array. Each record has a `thread` with its ID and chronologically ordered `turns`, plus a caller-verified `stop_intent`: `execution_interruption`, `user_pause`, `user_stop` or `unknown`.

```text
python scripts/classify.py snapshots.json
```

The helper neither retrieves conversations nor infers intent or sends messages. Its categories are preliminary. In particular, `closed_or_waiting` is not a task-completion verdict. Newly granted authority must be assessed separately; do not falsify the original stop reason to get `resume_candidate`.

# 4. Verification and limits

Distinguish submission, acceptance, running, turn completion and actual task completion. Read back an uncertain delivery before retrying. For side effects, inspect what already happened rather than assuming replay is harmless. No exactly-once transaction mechanism is provided.

Limited synthetic experiments support concise messages when context is sufficient. Small input differences in a target recovery turn do not establish whole-workflow token or monetary savings, or a causal cache benefit. Complex writes, approval recovery and compaction recovery remain outside those results.

Install the complete package, including SKILL, agents, references and scripts, from a fixed version of the selected source. Verify the actual read path and recovery results separately; readable source files do not establish installation or automatic discovery.
