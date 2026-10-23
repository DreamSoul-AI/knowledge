# DreamSoul Knowledge

**English**&nbsp; | &nbsp;[**简体中文**](https://github.com/DreamSoul-AI/knowledge/blob/main/README_zh.md)

Reusable agent skills and tools with human-readable guides. Each skill contains its own
instructions and reference material, so it can be installed independently.

## Skills and guides

| Skill | Purpose | Guide |
| --- | --- | --- |
| [ai-work-message](skills/ai-work-message/SKILL.md) | Draft a short, natural work update from an AI conversation | [English](skills/ai-work-message/references/README.md) / [中文](skills/ai-work-message/references/README_zh.md) |
| [table-log-sync](skills/table-log-sync/SKILL.md) | Reconcile a project tracker and work log in their existing structure, preview changes, then apply confirmed edits | [English](skills/table-log-sync/references/README.md) / [中文](skills/table-log-sync/references/README_zh.md) |
| [codex-conversation-archive](skills/codex-conversation-archive/SKILL.md) | Preserve and incrementally archive local Codex conversations | [English](skills/codex-conversation-archive/references/README.md) / [中文](skills/codex-conversation-archive/references/README_zh.md) / [ZIP](skills/codex-conversation-archive.zip) |
| [meeting-minutes](skills/meeting-minutes/SKILL.md) | Retrieve original records and summarize any meeting type | [English](skills/meeting-minutes/references/README.md) / [中文](skills/meeting-minutes/references/README_zh.md) |
| [interview-records](skills/interview-records/SKILL.md) | Find interviews in calendars and organize their original records | [English](skills/interview-records/references/README.md) / [中文](skills/interview-records/references/README_zh.md) |
| [git-workflow](skills/git-workflow/SKILL.md) | Git operations and recovery | [English](skills/git-workflow/references/README.md) / [中文](skills/git-workflow/references/README_zh.md) |
| [literature-search](skills/literature-search/SKILL.md) | Academic literature discovery and screening | [English](skills/literature-search/references/README.md) / [中文](skills/literature-search/references/README_zh.md) |
| [paper-analysis](skills/paper-analysis/SKILL.md) | Critical reading of selected papers | [English](skills/paper-analysis/references/README.md) / [中文](skills/paper-analysis/references/README_zh.md) |
| [research-plan](skills/research-plan/SKILL.md) | Research ideas, study plans, and experiment protocols | [English](skills/research-plan/references/README.md) / [中文](skills/research-plan/references/README_zh.md) |
| [python-environment](skills/python-environment/SKILL.md) | Python environments and troubleshooting | [English](skills/python-environment/references/README.md) / [中文](skills/python-environment/references/README_zh.md) |
| [pytorch-project](skills/pytorch-project/SKILL.md) | PyTorch training and reproducibility | [English](skills/pytorch-project/references/README.md) / [中文](skills/pytorch-project/references/README_zh.md) |
| [mongodb-development](skills/mongodb-development/SKILL.md) | MongoDB development workflows | [English](skills/mongodb-development/references/README.md) / [中文](skills/mongodb-development/references/README_zh.md) |

## Tools

| Tool | Purpose | Guide |
| --- | --- | --- |
| [codex-vscode-windows-notify](tools/codex-vscode-windows-notify/) | Native Windows notifications for Codex turns in VS Code | [English](tools/codex-vscode-windows-notify/README.md) / [中文](tools/codex-vscode-windows-notify/README_zh.md) |

## Install in Codex

Send this message to Codex to install one skill:

```text
$skill-installer
Install the skill at:
https://github.com/DreamSoul-AI/knowledge/tree/main/skills/paper-analysis
```

Replace paper-analysis with another skill name from the table.
To install manually for a project, copy the entire skill directory into
`<project>/.agents/skills/`. Keep SKILL.md and all bundled directories, including scripts/, together.

After installation, ask Codex to use the skill, for example:
“Use paper-analysis to analyze this paper.”

## Structure

- `skills/<name>/SKILL.md`: when to use the skill and how to perform the task.
- `skills/<name>/agents/openai.yaml`: Codex interface metadata.
- `skills/<name>/references/`: English and Chinese guides, read when relevant.
- `tools/<name>/`: standalone tools with their own scripts and guides.

Each guide is maintained inside its skill. Links to other skills on GitHub are
optional further reading, not required local dependencies.

## License

[MIT](LICENSE)

