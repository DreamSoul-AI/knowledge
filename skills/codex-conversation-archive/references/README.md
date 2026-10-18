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
Preserve user text, final replies, relay sources and original tool records. Keep the separate four-section summary to one or two sentences per section, primarily for AI readers.
Save locally only. Do not sync to cloud services or enable scheduled tasks.
```

Archive a selected conversation:

```text
Use $codex-conversation-archive to archive a selected Codex conversation.
Session: <exact session ID or JSONL path>
Title: <subject>. Output: <local archive directory>.
Fix the cutoff to the last complete public record available on the first read.
Preserve user text, final replies, relay sources and original tool records.
Keep the four-section summary to one or two sentences per section, primarily for AI readers.
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

The first run has a placeholder summary. Have the agent create a separate factual summary starting with `# 一、流程摘要` and the four sections described in the bundled standard. Rerun at the same cutoff with `--summary <summary.md>` before delivering the completed document.

`current.json` points to immutable `versions/<hash>/` containing Markdown, archive.json, tools.json and verification.json. Repeating identical input adds zero records. Reuse the output directory for increments; changed or missing history stops the update. Do not manually edit generated files.

Review generated records before sharing: original messages and tool outputs may contain sensitive data. Never commit real session archives to a public repository. Markdown does not store default heading folding; authorized Feishu sync requires separately setting and visually checking it. This skill does not install scheduled tasks or background listeners.

## Validation and limits

Validated on Windows: isolated ZIP execution, GitHub installation and Codex CLI use, plus project-scoped installation and skill recognition in a clean Codex desktop project after removing the old same-name installation. First archive, exact user/final text, real subsequent-message increments and zero-addition repeats passed. Nine synthetic regression tests passed; run `python -B <skill>/scripts/test_archive.py` to repeat them.

Tests used an existing login. Fresh OS accounts, other operating systems or client versions, the desktop UI skill picker and full UI-export equivalence were not verified. Missing history, truncated output and external attachments cannot be reconstructed.
