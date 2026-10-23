# DreamSoul Knowledge

[**English**](https://github.com/DreamSoul-AI/knowledge/blob/main/README.md)&nbsp; | &nbsp;**简体中文**

可复用的 Agent Skills、工具与面向人的参考教程。每个技能都包含自己的执行说明和参考资料，可以独立安装。

## 技能与教程

| 技能 | 用途 | 教程 |
| --- | --- | --- |
| [ai-work-message](skills/ai-work-message/SKILL.md) | 把一段 AI 沟通整理成一句自然简短的工作留言 | [English](skills/ai-work-message/references/README.md) / [中文](skills/ai-work-message/references/README_zh.md) |
| [table-log-sync](skills/table-log-sync/SKILL.md) | 按现有分类和层级双向整理总表与日志，先预览、确认后写入 | [English](skills/table-log-sync/references/README.md) / [中文](skills/table-log-sync/references/README_zh.md) |
| [codex-conversation-archive](skills/codex-conversation-archive/SKILL.md) | 保留原话并增量归档 Codex 本地会话 | [English](skills/codex-conversation-archive/references/README.md) / [中文](skills/codex-conversation-archive/references/README_zh.md) / [安装包](skills/codex-conversation-archive.zip) |
| [meeting-minutes](skills/meeting-minutes/SKILL.md) | 获取原始记录并整理各类会议纪要 | [English](skills/meeting-minutes/references/README.md) / [中文](skills/meeting-minutes/references/README_zh.md) |
| [interview-records](skills/interview-records/SKILL.md) | 从日历定位面试并获取、整理原始记录 | [English](skills/interview-records/references/README.md) / [中文](skills/interview-records/references/README_zh.md) |
| [git-workflow](skills/git-workflow/SKILL.md) | Git 操作与恢复 | [English](skills/git-workflow/references/README.md) / [中文](skills/git-workflow/references/README_zh.md) |
| [literature-search](skills/literature-search/SKILL.md) | 文献检索与筛选 | [English](skills/literature-search/references/README.md) / [中文](skills/literature-search/references/README_zh.md) |
| [paper-analysis](skills/paper-analysis/SKILL.md) | 论文精读与分析 | [English](skills/paper-analysis/references/README.md) / [中文](skills/paper-analysis/references/README_zh.md) |
| [research-plan](skills/research-plan/SKILL.md) | 从灵感形成研究计划与实验方案 | [English](skills/research-plan/references/README.md) / [中文](skills/research-plan/references/README_zh.md) |
| [python-environment](skills/python-environment/SKILL.md) | Python 环境配置与排错 | [English](skills/python-environment/references/README.md) / [中文](skills/python-environment/references/README_zh.md) |
| [pytorch-project](skills/pytorch-project/SKILL.md) | PyTorch 训练与实验复现 | [English](skills/pytorch-project/references/README.md) / [中文](skills/pytorch-project/references/README_zh.md) |
| [mongodb-development](skills/mongodb-development/SKILL.md) | MongoDB 开发与维护 | [English](skills/mongodb-development/references/README.md) / [中文](skills/mongodb-development/references/README_zh.md) |

## 工具

| 工具 | 用途 | 教程 |
| --- | --- | --- |
| [codex-vscode-windows-notify](tools/codex-vscode-windows-notify/) | Codex VS Code 任务完成后的原生 Windows 通知 | [English](tools/codex-vscode-windows-notify/README.md) / [中文](tools/codex-vscode-windows-notify/README_zh.md) |

## 在 Codex 中安装

把下面这段消息发给 Codex，即可安装一个技能：

```text
$skill-installer
请安装这个目录里的技能：
https://github.com/DreamSoul-AI/knowledge/tree/main/skills/paper-analysis
```

将 paper-analysis 替换为表格中的其他技能名即可安装对应技能。
如果手动安装到某个项目，将整个技能文件夹复制到 `<项目>/.agents/skills/` 下，
保留 SKILL.md 和所有随包目录，包括 scripts/。

安装后可以直接说：“请使用 paper-analysis 分析这篇论文。”

## 目录结构

- `skills/<技能名>/SKILL.md`：适用场景和执行流程。
- `skills/<技能名>/agents/openai.yaml`：Codex 界面元数据。
- `skills/<技能名>/references/`：按需阅读的中英文教程。
- `tools/<工具名>/`：包含脚本和使用教程的独立工具。

每份教程只在对应技能中维护。指向 GitHub 上其他技能的链接仅用于延伸阅读，
不作为本地必需依赖。

## 许可证

[MIT](LICENSE)

