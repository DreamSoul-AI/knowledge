# Codex conversation archive

Archive one explicitly selected local Codex JSONL session into Markdown. User text and final replies are copied and checked character by character. Summaries are separate. Public progress, tool records and relayed-message sources are retained; hidden reasoning is excluded.

## Install and use

Requires Python 3.8+ and permission to read the selected source, run Python and write the archive. Ask Codex to install the complete skill:

```text
Use $skill-installer to install https://github.com/DreamSoul-AI/knowledge/tree/main/skills/codex-conversation-archive
Destination: <absolute-project-path>/.agents/skills/
Keep all bundled files. Verify the installation path instead of using an older copy.
Install only; do not archive or schedule tasks yet.
```

Alternatively, extract the [ZIP](https://github.com/DreamSoul-AI/knowledge/raw/refs/heads/main/skills/codex-conversation-archive.zip) into that directory. Invoke the skill in the next turn; reopen the project conversation if it has not loaded. Check the actual path and version when duplicate names exist; do not automatically uninstall global skills.

Archive the current conversation:

```text
Use $codex-conversation-archive to archive this conversation through this request.
Title: First conversation archive
Output: the archive directory in this project
Preserve user text, final replies, relay sources and original tool records. Make the first section independently readable: explain the goal, actual workflow diagram, turning points, decisions, results and lessons.
Save locally only. Do not sync to cloud services or enable scheduled tasks.
```

Archive a selected conversation:

```text
Use $codex-conversation-archive to archive a selected Codex conversation.
Session: <exact session ID or JSONL path>
Title: <subject>. Output: <local archive directory>.
Fix the cutoff to the last complete public record available on the first read.
Preserve user text, final replies, relay sources and original tool records.
Make the first section independently readable, covering the goal, actual workflow diagram, turning points, decisions, results and lessons.
Save locally only. Do not sync or schedule tasks.
```

Match filenames in the selected user's Codex `sessions/` directory and confirm session_meta. A title may be resolved through available session-list metadata; ask for an ID or path if ambiguous. Do not scan all conversation bodies. Cloud or remote sessions require their actual source records; thread summaries cannot replace raw text.

For increments, ask to incrementally archive this conversation or session `<ID>`, reusing its title and output directory. The current conversation ends at the new request; another conversation uses the cutoff fixed on its first read. Do not send messages to the selected conversation just to archive it.

Use the current workspace standard when available, otherwise the bundled [archive standard](archive-standard.md). An explicit `--rules` records the standard's hash; it does not dynamically change the renderer. See [SKILL.md](../SKILL.md) for the workflow and [format boundaries](record-format.md) for supported records.

## CLI and output

Replace placeholders with actual paths and quote paths containing spaces:

```text
python <skill>/scripts/archive.py --source <session.jsonl> --session <session-id> --title "First conversation archive" --output <archive-directory> --through-id <cutoff-message-id>
```

The first run has a placeholder summary. Prepare a review starting with `# 一、流程摘要`. State the goal, turning points and result in the opening overview, then cover the workflow, decisions, outputs and reusable lessons. Include a Mermaid diagram and explain what changed the approach. Link accessible outputs and record outstanding work. Keep session and cutoff IDs and local verification files in the archive metadata. Rerun at the same cutoff with `--summary <summary.md>` before delivery.

Each user message and final reply displays its original timestamp beneath the heading, in Beijing time by default. A final reply may also display the native Codex turn duration, including execution and waiting. Aborted turns are marked separately. Missing timestamps or durations are explicitly marked as unrecorded; archive time and message gaps are never substituted. Use `--utc-offset=+00:00` for a different fixed display offset; daylight-saving rules are not applied.

`current.json` points to immutable `versions/<hash>/` containing Markdown, archive.json, tools.json, timing.json and verification.json. timing.json preserves the source timestamps and turn metadata. Upgrading an existing archive creates a new version without changing original text or removing the old version. Repeating identical input adds zero records. Reuse the output directory for increments; changed or missing history stops the update. Do not manually edit generated files.

Review generated records before sharing: original messages and tool outputs may contain sensitive data. Never commit real session archives to a public repository. Markdown does not store default heading folding; authorized Feishu sync requires separately setting and visually checking it. This skill does not install scheduled tasks or background listeners.

## Validation and limits

Previously validated on Windows: isolated ZIP execution, GitHub installation and Codex CLI use, plus project-scoped installation and skill recognition in a clean Codex desktop project after removing the old same-name installation. First archive, exact user/final text, real subsequent-message increments and zero-addition repeats passed.

The timestamp update was replayed locally against a real product-positioning conversation: 511 user/final timestamps matched the previously verified document, with 241 native durations retained. Original messages and tool records remained unchanged, the old version was preserved, and repeating the run added zero records without changing the version. Fifteen synthetic regression tests cover offsets, missing times, aborted turns, cutoffs, exact text and incremental boundaries; run `python -B <skill>/scripts/test_archive.py` to repeat them. This replay did not update any Feishu document.

The expanded review was also generated for that conversation, including a locally rendered Mermaid workflow, turning points and grounded lessons. The complete second section, timing metadata and tool records stayed unchanged, and repetition kept the same version. Neither the original business archive nor Feishu content was updated by this validation.

Tests used an existing login. Fresh OS accounts, other operating systems or client versions, the desktop UI skill picker and full UI-export equivalence were not verified. Missing history, truncated output and external attachments cannot be reconstructed.
