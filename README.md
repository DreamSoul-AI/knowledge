# DreamSoul Knowledge

**English**&nbsp; | &nbsp;[**简体中文**](README_zh.md)

Reusable agent skills and tools with human-readable guides. Each skill contains its own
instructions and reference material, so it can be installed independently.

## Skills and guides

| Skill | Purpose | Guide |
| --- | --- | --- |
| [ai-work-message](skills/ai-work-message/SKILL.md) | Draft a short, natural work update from an AI conversation | [English](skills/ai-work-message/references/README.md) / [中文](skills/ai-work-message/references/README_zh.md) |
| [codex-conversation-archive](skills/codex-conversation-archive/SKILL.md) | Preserve and incrementally archive local Codex conversations | [English](skills/codex-conversation-archive/references/README.md) / [中文](skills/codex-conversation-archive/references/README_zh.md) / [ZIP](skills/codex-conversation-archive.zip) |
| [meeting-minutes](skills/meeting-minutes/SKILL.md) | Retrieve original records and summarize any meeting type | [English](skills/meeting-minutes/references/README.md) / [中文](skills/meeting-minutes/references/README_zh.md) |
| [document-sync](skills/document-sync/SKILL.md) | Upload, download or sync one document using shared baselines; Feishu adapter available | [English](skills/document-sync/references/README.md) / [简体中文](skills/document-sync/references/README_zh.md) |
| [calendar-meeting-archive](skills/calendar-meeting-archive/SKILL.md) | Collect meetings from your calendar, organize minutes and upload them to a chosen folder | [English](skills/calendar-meeting-archive/references/README.md) / [中文](skills/calendar-meeting-archive/references/README_zh.md) |
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
| [cpu-memory-cleanup](tools/cpu-memory-cleanup/) | Reusable memory package and CLI entry; no duplicated cleanup implementation | [English](tools/cpu-memory-cleanup/README.md) / [中文](tools/cpu-memory-cleanup/README_zh.md) |

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


## Repository maintenance

Repository: [DreamSoul-AI/knowledge](https://github.com/DreamSoul-AI/knowledge). Read [AGENTS.md](AGENTS.md) for repository maintenance and shared-reference discovery. These rules govern maintainers; installing a skill does not require access to DreamSoul private documents.

This repository distributes Markdown instructions, YAML metadata and bundled scripts. Runtime requirements and checks belong to each skill or tool guide; there is no single repository-wide install, build or test command. Keep guides, scripts, references and licenses together.

The seven development-document roles do not yet have separate repository-wide entries: General Research, architecture, code structure, development plan, active defects, Development Record and Run Record. Track these gaps without treating per-skill user guides as completed project engineering documents. No standalone literature review or research plan is currently maintained for this distribution repository. Keep both root READMEs consistent when entries, requirements or scope change.
