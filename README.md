# DreamSoul Knowledge

**English**&nbsp; | &nbsp;[**简体中文**](README_zh.md)

Reusable Agent Skills, standalone Tools and automation definitions. Each skill contains its own
instructions and reference material, so it can be installed independently.

## Skills

### Work and documents

| Skill | Purpose | Usage |
| --- | --- | --- |
| [wrap-up](skills/wrap-up/SKILL.md) | Inspect closeout readiness first; execute remaining steps when requested | [English](skills/wrap-up/references/README.md) / [中文](skills/wrap-up/references/README_zh.md) |
| [work-summary](skills/work-summary/SKILL.md) | Consolidate results, evidence and unfinished work | [English](skills/work-summary/references/README.md) / [中文](skills/work-summary/references/README_zh.md) |
| [work-message](skills/work-message/SKILL.md) | Prepare board-specific work messages and deliver as authorized | [English](skills/work-message/references/README.md) / [中文](skills/work-message/references/README_zh.md) |
| [codex-conversation-archive](skills/codex-conversation-archive/SKILL.md) | Preserve and incrementally archive local Codex conversations | [English](skills/codex-conversation-archive/references/README.md) / [中文](skills/codex-conversation-archive/references/README_zh.md) / [ZIP](skills/codex-conversation-archive.zip) |
| [meeting-minutes](skills/meeting-minutes/SKILL.md) | Summarize meetings using supplied material and rules | [English](skills/meeting-minutes/references/README.md) / [中文](skills/meeting-minutes/references/README_zh.md) |
| [calendar-meeting-archive](skills/calendar-meeting-archive/SKILL.md) | Reuse existing results and archive calendar meetings by ownership | [English](skills/calendar-meeting-archive/references/README.md) / [中文](skills/calendar-meeting-archive/references/README_zh.md) |
| [document-sync](skills/document-sync/SKILL.md) | Sync selected documents with baseline and conflict checks; Feishu supported | [English](skills/document-sync/references/README.md) / [简体中文](skills/document-sync/references/README_zh.md) |
| [grok-bot-cli](skills/grok-bot-cli/SKILL.md) | Connect to Grok Bot and verify access or authorized messaging | [Connection guide](skills/grok-bot-cli/references/connection.md) |

### Research

| Skill | Purpose | Usage |
| --- | --- | --- |
| [general-search](skills/general-search/SKILL.md) | Research technologies, tools and engineering practices | [English](skills/general-search/references/README.md) / [中文](skills/general-search/references/README_zh.md) |
| [literature-search](skills/literature-search/SKILL.md) | Search academic literature, synthesize reviews and reusable research assets | [English](skills/literature-search/references/README.md) / [中文](skills/literature-search/references/README_zh.md) |
| [paper-analysis](skills/paper-analysis/SKILL.md) | Critical reading of selected papers | [English](skills/paper-analysis/references/README.md) / [中文](skills/paper-analysis/references/README_zh.md) |
| [research-plan](skills/research-plan/SKILL.md) | Research ideas, study plans, and experiment protocols | [English](skills/research-plan/references/README.md) / [中文](skills/research-plan/references/README_zh.md) |

### Engineering and runtime

| Skill | Purpose | Usage |
| --- | --- | --- |
| [code-architecture-analysis](skills/code-architecture-analysis/SKILL.md) | Verify architecture claims against source and runtime evidence | [Usage](skills/code-architecture-analysis/SKILL.md) |
| [python-environment](skills/python-environment/SKILL.md) | Inspect, prepare and troubleshoot Python environments | [English](skills/python-environment/references/README.md) / [中文](skills/python-environment/references/README_zh.md) |
| [cpu-memory-cleanup](skills/cpu-memory-cleanup/SKILL.md) | Read Windows memory and perform requested working-set cleanup | [English](skills/cpu-memory-cleanup/references/README.md) / [中文](skills/cpu-memory-cleanup/references/README_zh.md) / [ZIP](skills/cpu-memory-cleanup.zip) |
| [public-website-deployment](skills/public-website-deployment/SKILL.md) | ESA / Cloudflare static publishing, updates and subdomain binding; optional multi-source assembly, ESA domain migration and renewal checks; defaults to China/ESA and CLI uploads | [English](skills/public-website-deployment/references/README.md) / [中文](skills/public-website-deployment/references/README_zh.md) |
| [knowledge-update](skills/knowledge-update/SKILL.md) | Check or update adopted skills and tools, preserving local changes | [English](skills/knowledge-update/references/README.md) / [中文](skills/knowledge-update/references/README_zh.md) |
| [workspace-update](skills/workspace-update/SKILL.md) | Update Workspace templates and delegate adopted capabilities to knowledge-update | [English](skills/workspace-update/references/README.md) / [中文](skills/workspace-update/references/README_zh.md) |
| [github-summary](skills/github-summary/SKILL.md) | Receive versioned Learnings and consolidate them by recipient | [English](skills/github-summary/references/README.md) / [中文](skills/github-summary/references/README_zh.md) |
| [agent-experiment](skills/agent-experiment/SKILL.md) | Run bounded Agent experiments and assess observed behavior | [English](skills/agent-experiment/references/README.md) / [中文](skills/agent-experiment/references/README_zh.md) |

### Design

| Skill | Purpose | Installation |
| --- | --- | --- |
| [figma-design](https://github.com/DreamSoul-AI/figma/blob/main/src/figma-design/SKILL.md) | Create or revise editable designs using the independently maintained Figma workflow | [v1.1.1 release and installation](https://github.com/DreamSoul-AI/figma/releases/tag/figma-design-v1.1.1) · Figma repository access required |

The complete workflow and translation manuals are maintained in the Figma repository; knowledge provides discovery and installation links without a second maintained copy.

For Figma Design, download the ZIP from the Figma release page. Extract the entire `figma-design` folder into `<project>/.agents/skills/`, then invoke `$figma-design` in Codex. The ZIP includes the instructions, Node.js tools, and bundled dependencies. Use the install steps on the release page for runtime requirements. If upgrading an installation named `figma-design-delivery`, preserve personal changes before replacing it with the complete new package, and avoid loading both names.

## Tools

| Tool | Purpose | Usage |
| --- | --- | --- |
| [grok-bot-cli](tools/grok-bot-cli/) | Launch the locally installed upstream CLI | [English](tools/grok-bot-cli/README.md) / [中文](tools/grok-bot-cli/README_zh.md) |
| [codex-vscode-windows-notify](tools/codex-vscode-windows-notify/) | Native Windows notifications for Codex turns in VS Code | [English](tools/codex-vscode-windows-notify/README.md) / [中文](tools/codex-vscode-windows-notify/README_zh.md) |
| [cpu-memory-cleanup](tools/cpu-memory-cleanup/) | Reusable memory package and CLI entry; no duplicated cleanup implementation | [English](tools/cpu-memory-cleanup/README.md) / [中文](tools/cpu-memory-cleanup/README_zh.md) |
| [shared-repository-resources](tools/shared-repository-resources/) | Reuse configurable directory resources; new examples use `shared/` storage and `.shared/` entries | [English](tools/shared-repository-resources/README.md) / [中文](tools/shared-repository-resources/README_zh.md) |

## Automations

Automations are maintained separately in [automations](automations/README.md), composing skills through task prompts and external configuration.

| Automation | Purpose | Status | Usage |
| --- | --- | --- | --- |
| [Daily Meeting Summary](automations/daily-meeting-summary/) | Incremental meeting archiving, summaries and authorized delivery | First version; manual reuse path verified | [English](automations/daily-meeting-summary/README.md) / [中文](automations/daily-meeting-summary/README_zh.md) |
| [Daily Email Summary](automations/daily-email-summary/) | Summarize user-configured mailboxes with topics, next actions and original links | First definition; Outlook read and format verified, scheduling pending | [English](automations/daily-email-summary/README.md) / [中文](automations/daily-email-summary/README_zh.md) |

Deployment uses the actual project's configuration and confirmed scheduler scope. New generation, upload writes and scheduled triggering were not exercised in the latest manual run; see the [automation registry](automations/README.md) for validation details.

## Install in Codex

Send this message to Codex to install one skill:

```text
$skill-installer
Install the skill at:
https://github.com/DreamSoul-AI/knowledge/tree/main/skills/paper-analysis
```

Replace paper-analysis with the directory name of a skill hosted in this repository.
To install manually for a project, copy the entire skill directory into
`<project>/.agents/skills/`. Keep SKILL.md and all bundled directories, including scripts/, together.

After installation, ask Codex to use the skill, for example:
“Use paper-analysis to analyze this paper.”

The former `ai-work-message` skill is now `work-message`. Install the complete
[work-message directory](skills/work-message/). Preserve personal changes before
replacing an old installation, and keep only the new skill active. Old document
URLs remain migration notices; they are not a second installable package.

## Structure

- `skills/<name>/SKILL.md`: when to use the skill and how to perform the task.
- `skills/<name>/agents/openai.yaml`: Codex interface metadata.
- `skills/<name>/references/`: English and Chinese guides, read when relevant.
- `tools/<name>/`: standalone tools with their own scripts and guides.
- `automations/<name>/`: task prompts, example configuration and bilingual guides.

Each guide is maintained inside its skill. Links to other skills on GitHub are
optional further reading, not required local dependencies.

## License

[MIT](LICENSE)


## Repository maintenance

See [repository conventions](REPO.md) and the [engineering document index](docs/README.md) for maintenance.

Repository: [DreamSoul-AI/knowledge](https://github.com/DreamSoul-AI/knowledge). Read [AGENTS.md](AGENTS.md) for repository maintenance and shared-reference discovery. These rules govern maintainers; installing a skill does not require access to DreamSoul private documents.

This repository distributes Markdown instructions, YAML metadata and bundled scripts. Runtime requirements and checks belong to each skill or tool guide; there is no single repository-wide install, build or test command. Keep guides, scripts, references and licenses together.

Repository-wide execution evidence is available in [Run Record](<docs/运行记录 Run Record/>), and change descriptions in [Development Record](<docs/开发记录 Development Record/>). General Research, architecture, code structure, development plan and active defects do not yet have separate repository-wide entries. Track these gaps without treating per-skill user guides as completed project engineering documents. No standalone literature review or research plan is currently maintained for this distribution repository. Keep both root READMEs consistent when entries, requirements or scope change.

Candidate-specific work is tracked in the [shared-resource integration plan](<docs/开发 Development/开发计划 Development Plan 多仓库共享资源接入.md>). This does not complete repository-wide engineering documentation.

Document roles follow AGENTS.md: General Research covers mechanisms, options, sources and current conclusions. Design decisions, migrations and fixes belong in Development Record; executions and past results belong in Run Record, without history-summary chapters in research documents. Designs describe the chosen direction and implementation gaps; plans describe future work and acceptance criteria. Review and migrate existing content file by file where needed; renaming alone does not complete this work.

Development uses two long-lived branches: `dev` for integration and `main` for published versions. Start necessary short-lived branches from `dev`, merge through a reviewed and validated PR, then release with a `dev → main` PR. Delete completed remote and unused local short-lived branches during the same closeout; preserve uncommitted work and check attached worktrees before cleanup.

### Capability candidates

**Shared resources across repositories**: the [tool](tools/shared-repository-resources/README.md) now accepts arbitrary directory resource names and per-repository mappings. A research profile is an optional example. Agent-level discovery and migration orchestration remain candidates; no separate skill has been added. See the [current plan](<docs/开发 Development/开发计划 Development Plan 多仓库共享资源接入.md>) for remaining work and adoption boundaries.
