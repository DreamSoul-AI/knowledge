# Codex conversation archive

Archive one explicitly selected local Codex JSONL session into Markdown. User text and final replies are copied and checked character by character. Summaries are separate. Public progress, tool records and relayed-message sources are retained; hidden reasoning is excluded.

## Install and use

Requires Python 3.8+ and only the standard library. Download the complete skill directory or extract the ZIP, then place `codex-conversation-archive` under `<project>/.agents/skills/`. Keep all bundled files together and reopen the project conversation so Codex can load it. Alternatively, ask skill-installer to install the skill directory from the actual published GitHub branch.

```text
Use $codex-conversation-archive to archive this conversation through this request.
Title: First conversation archive
Output: the archive directory in this project
Preserve user text, final replies, relay sources and available tool records. Keep the summary separate.
Save locally only. Do not sync to cloud services or enable scheduled tasks.
```

For another conversation, supply its exact session ID or JSONL path. Match filenames in the selected user's Codex `sessions/` directory and confirm session_meta. Cloud or remote sessions require access to their actual source records. Do not substitute a thread summary for raw text.

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

Run `python -B <skill>/scripts/test_archive.py` for synthetic boundary tests. The package was also exercised in a clean directory with isolated Python for first archive, exact text, repeat and increment checks. This does not establish fresh-user client loading, all operating systems, other Codex versions or full UI-export equivalence. Missing history, truncated output and external attachments cannot be reconstructed.
