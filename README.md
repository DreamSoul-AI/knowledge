# DreamSoul Knowledge

**English**&nbsp; | &nbsp;[**简体中文**](README_zh.md)

Reusable agent skills and tools with human-readable guides. Each skill contains its own
instructions and reference material, so it can be installed independently.

## Skills and guides

| Skill | Purpose | Guide |
| --- | --- | --- |
| [ai-work-message](skills/ai-work-message/SKILL.md) | Read project rules and each board’s context, prepare complete updates, and publish or revise only as authorized | [English](skills/ai-work-message/references/README.md) / [中文](skills/ai-work-message/references/README_zh.md) |
| [codex-conversation-archive](skills/codex-conversation-archive/SKILL.md) | Preserve and incrementally archive local Codex conversations | [English](skills/codex-conversation-archive/references/README.md) / [中文](skills/codex-conversation-archive/references/README_zh.md) / [ZIP](skills/codex-conversation-archive.zip) |
| [meeting-minutes](skills/meeting-minutes/SKILL.md) | Organize meeting material with context and rules; select advice by value and actual beneficiaries; optional delivery handler | [English](skills/meeting-minutes/references/README.md) / [中文](skills/meeting-minutes/references/README_zh.md) |
| [document-sync](skills/document-sync/SKILL.md) | Upload, download or sync a document or explicit list with project rules and per-document baselines; Feishu adapter available | [English](skills/document-sync/references/README.md) / [简体中文](skills/document-sync/references/README_zh.md) |
| [calendar-meeting-archive](skills/calendar-meeting-archive/SKILL.md) | Apply archive ownership and explicit overrides, reuse or patch existing results, then archive and deliver calendar meetings | [English](skills/calendar-meeting-archive/references/README.md) / [中文](skills/calendar-meeting-archive/references/README_zh.md) |
| [literature-search](skills/literature-search/SKILL.md) | Search academic literature, synthesize reviews and reusable research assets | [English](skills/literature-search/references/README.md) / [中文](skills/literature-search/references/README_zh.md) |
| [paper-analysis](skills/paper-analysis/SKILL.md) | Critical reading of selected papers | [English](skills/paper-analysis/references/README.md) / [中文](skills/paper-analysis/references/README_zh.md) |
| [research-plan](skills/research-plan/SKILL.md) | Research ideas, study plans, and experiment protocols | [English](skills/research-plan/references/README.md) / [中文](skills/research-plan/references/README_zh.md) |
| [python-environment](skills/python-environment/SKILL.md) | Python Environment Management: inspect, prepare and troubleshoot project environments | [English](skills/python-environment/references/README.md) / [中文](skills/python-environment/references/README_zh.md) |
| [cpu-memory-cleanup](skills/cpu-memory-cleanup/SKILL.md) | Initialize the Windows runtime, read real memory and perform requested working-set cleanup | [English](skills/cpu-memory-cleanup/references/README.md) / [中文](skills/cpu-memory-cleanup/references/README_zh.md) / [ZIP](skills/cpu-memory-cleanup.zip) |

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

Document roles follow AGENTS.md: General Research covers mechanisms, options, sources and current conclusions. Design decisions, migrations and fixes belong in Development Record; executions and past results belong in Run Record, without history-summary chapters in research documents. Designs describe the chosen direction and implementation gaps; plans describe future work and acceptance criteria. Review and migrate existing content file by file where needed; renaming alone does not complete this work.

Development uses two long-lived branches: `dev` for integration and `main` for published versions. Start necessary short-lived branches from `dev`, merge through a reviewed and validated PR, then release with a `dev → main` PR. Delete completed remote and unused local short-lived branches during the same closeout; preserve uncommitted work and check attached worktrees before cleanup.
