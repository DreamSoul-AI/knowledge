# DreamSoul Knowledge

[English](README.md)

可复用的 Agent Skills 与面向人的参考教程。每个技能都包含自己的执行说明和参考资料，可以独立安装。

## 技能与教程

| 技能 | 用途 | 教程 |
| --- | --- | --- |
| [git-workflow](skills/git-workflow/SKILL.md) | Git 操作与恢复 | [中文教程](skills/git-workflow/references/README_zh.md) |
| [literature-search](skills/literature-search/SKILL.md) | 文献检索与筛选 | [中文教程](skills/literature-search/references/README_zh.md) |
| [paper-analysis](skills/paper-analysis/SKILL.md) | 论文精读与分析 | [中文教程](skills/paper-analysis/references/README_zh.md) |
| [python-environment](skills/python-environment/SKILL.md) | Python 环境配置与排错 | [中文教程](skills/python-environment/references/README_zh.md) |
| [pytorch-project](skills/pytorch-project/SKILL.md) | PyTorch 训练与实验复现 | [中文教程](skills/pytorch-project/references/README_zh.md) |
| [mongodb-development](skills/mongodb-development/SKILL.md) | MongoDB 开发与维护 | [中文教程](skills/mongodb-development/references/README_zh.md) |

## 在 Codex 中安装

把下面这段消息发给 Codex，即可安装一个技能：

```text
$skill-installer
请安装这个目录里的技能：
https://github.com/DreamSoul-AI/knowledge/tree/main/skills/paper-analysis
```

将 paper-analysis 替换为表格中的其他技能名即可安装对应技能。
如果手动安装到某个项目，将整个技能文件夹复制到 `<项目>/.agents/skills/` 下，
保留其中的 SKILL.md、agents/ 和 references/。

安装后可以直接说：“请使用 paper-analysis 分析这篇论文。”

## 目录结构

- `skills/<技能名>/SKILL.md`：适用场景和执行流程。
- `skills/<技能名>/agents/openai.yaml`：Codex 界面元数据。
- `skills/<技能名>/references/`：按需阅读的中英文教程。

每份教程只在对应技能中维护。指向 GitHub 上其他技能的链接仅用于延伸阅读，
不作为本地必需依赖。

## 许可证

[MIT](LICENSE)
