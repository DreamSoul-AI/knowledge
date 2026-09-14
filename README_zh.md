# DreamSoul Knowledge

[English](README.md)

DreamSoul Knowledge 是面向人类和 AI Agent 的共享知识体系，将可阅读的
Wiki 内容、可执行的 Agent Skills，以及可复用资源统一放在同一个版本化仓库中。

## 知识模型

| 区域 | 面向对象 | 作用 |
| --- | --- | --- |
| [`wiki/`](wiki/) | 人 | 教程、概念、参考资料与操作指南 |
| [`skills/`](skills/) | AI Agent | 可执行的决策规则与任务工作流 |
| [`templates/`](templates/) | 人与 Agent | 稳定、可复用的产出结构 |
| [`examples/`](examples/) | 人与 Agent | 完整案例与预期结果示范 |

Tutorial 是 Wiki 的一种内容；Skill 是同一领域知识的可执行表达；Template 和
Example 可以同时服务于 Wiki 与 Skill。

## 知识领域

- [Git](wiki/git/README_zh.md)
- [文献检索](wiki/research/literature-search/README_zh.md)
- [论文阅读](wiki/research/paper-reading/README_zh.md)
- [Python 环境](wiki/python/README_zh.md)
- [PyTorch](wiki/pytorch/README_zh.md)
- [MongoDB](wiki/mongodb/README_zh.md)

## Agent Skills

- [`git-workflow`](skills/git-workflow/SKILL.md)
- [`literature-search`](skills/literature-search/SKILL.md)
- [`paper-analysis`](skills/paper-analysis/SKILL.md)
- [`python-environment`](skills/python-environment/SKILL.md)
- [`pytorch-project`](skills/pytorch-project/SKILL.md)
- [`mongodb-development`](skills/mongodb-development/SKILL.md)

## 内容源约定

本仓库是 Skills 与共享资源的版本控制源。`wiki/` 中的内容也可以发布或同步到
飞书知识库等协作平台。启用双向同步前，应先明确 GitHub 与外部 Wiki 中哪一侧是
权威内容源，避免产生两个相互冲突的版本。

## 许可证

[MIT](LICENSE)
