# DreamSoul Knowledge

[中文](README_zh.md)

Reusable agent skills with human-readable guides. Each skill contains its own
instructions and reference material, so it can be installed independently.

## Skills and guides

| Skill | Purpose | Guide |
| --- | --- | --- |
| [git-workflow](skills/git-workflow/SKILL.md) | Git operations and recovery | [English](skills/git-workflow/references/README.md) / [中文](skills/git-workflow/references/README_zh.md) |
| [literature-search](skills/literature-search/SKILL.md) | Academic literature discovery and screening | [English](skills/literature-search/references/README.md) / [中文](skills/literature-search/references/README_zh.md) |
| [paper-analysis](skills/paper-analysis/SKILL.md) | Critical reading of selected papers | [English](skills/paper-analysis/references/README.md) / [中文](skills/paper-analysis/references/README_zh.md) |
| [python-environment](skills/python-environment/SKILL.md) | Python environments and troubleshooting | [English](skills/python-environment/references/README.md) / [中文](skills/python-environment/references/README_zh.md) |
| [pytorch-project](skills/pytorch-project/SKILL.md) | PyTorch training and reproducibility | [English](skills/pytorch-project/references/README.md) / [中文](skills/pytorch-project/references/README_zh.md) |
| [mongodb-development](skills/mongodb-development/SKILL.md) | MongoDB development workflows | [English](skills/mongodb-development/references/README.md) / [中文](skills/mongodb-development/references/README_zh.md) |

## Install in Codex

Send this message to Codex to install one skill:

```text
$skill-installer
Install the skill at:
https://github.com/DreamSoul-AI/knowledge/tree/main/skills/paper-analysis
```

Replace paper-analysis with another skill name from the table.
To install manually for a project, copy the entire skill directory into
`<project>/.agents/skills/`. Keep SKILL.md, agents/, and references/ together.

After installation, ask Codex to use the skill, for example:
“Use paper-analysis to analyze this paper.”

## Structure

- `skills/<name>/SKILL.md`: when to use the skill and how to perform the task.
- `skills/<name>/agents/openai.yaml`: Codex interface metadata.
- `skills/<name>/references/`: English and Chinese guides, read when relevant.

Each guide is maintained inside its skill. Links to other skills on GitHub are
optional further reading, not required local dependencies.

## License

[MIT](LICENSE)
