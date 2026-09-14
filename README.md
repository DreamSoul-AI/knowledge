# DreamSoul Knowledge

[中文](README_zh.md)

DreamSoul Knowledge is a shared knowledge system for people and AI agents. It
keeps human-readable Wiki content, executable agent skills, and reusable
resources in one versioned repository.

## Model

| Area | Audience | Purpose |
| --- | --- | --- |
| [`wiki/`](wiki/) | People | Tutorials, concepts, references, and operating guides |
| [`skills/`](skills/) | AI agents | Executable decision rules and task workflows |
| [`templates/`](templates/) | Both | Stable structures for repeatable outputs |
| [`examples/`](examples/) | Both | Worked examples and expected-result patterns |

A tutorial is a kind of Wiki content. A skill is the executable expression of
the same domain knowledge. Templates and examples may support either side.

## Knowledge areas

- [Git](wiki/git/README.md)
- [Literature search](wiki/research/literature-search/README.md)
- [Paper reading](wiki/research/paper-reading/README.md)
- [Python environments](wiki/python/README.md)
- [PyTorch](wiki/pytorch/README.md)
- [MongoDB](wiki/mongodb/README.md)

## Agent skills

- [`git-workflow`](skills/git-workflow/SKILL.md)
- [`literature-search`](skills/literature-search/SKILL.md)
- [`paper-analysis`](skills/paper-analysis/SKILL.md)
- [`python-environment`](skills/python-environment/SKILL.md)
- [`pytorch-project`](skills/pytorch-project/SKILL.md)
- [`mongodb-development`](skills/mongodb-development/SKILL.md)

## Source of truth

The repository is the version-controlled source for skills and shared assets.
The `wiki/` tree can also be published or synchronized to a collaborative Wiki
such as Feishu. When an external Wiki is used, document which side is
authoritative before enabling two-way synchronization.

## License

[MIT](LICENSE)
