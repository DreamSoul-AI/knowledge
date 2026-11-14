# DreamSoul Knowledge

[**English**](README.md)&nbsp; | &nbsp;**简体中文**

可复用的 Agent Skills、工具、定时任务定义与面向人的参考教程。每个技能都包含自己的执行说明和参考资料，可以独立安装。

## 技能与教程

| 技能 | 用途 | 教程 |
| --- | --- | --- |
| [工作留言 AI Work Message](skills/ai-work-message/SKILL.md) | 先读规范与各板语境，完整成文，按授权发送或更新并回读 | [English](skills/ai-work-message/references/README.md) / [中文](skills/ai-work-message/references/README_zh.md) |
| [Codex 对话归档 Codex Conversation Archive](skills/codex-conversation-archive/SKILL.md) | 保留原话并增量归档 Codex 本地会话 | [English](skills/codex-conversation-archive/references/README.md) / [中文](skills/codex-conversation-archive/references/README_zh.md) / [安装包](skills/codex-conversation-archive.zip) |
| [会议总结 Meeting Minutes](skills/meeting-minutes/SKILL.md) | 结合材料和规范整理会议，建议按实际价值与受益人筛选，可按授权外接交付 | [English](skills/meeting-minutes/references/README.md) / [中文](skills/meeting-minutes/references/README_zh.md) |
| [文档同步 Document Sync](skills/document-sync/SKILL.md) | 按项目规范同步单文档或明确清单，逐份核对基线并保留冲突，目前支持飞书 | [English](skills/document-sync/references/README.md) / [中文](skills/document-sync/references/README_zh.md) |
| [日历会议归档 Calendar Meeting Archive](skills/calendar-meeting-archive/SKILL.md) | 按负责人及明确例外处理，先判断已有稿复用与局部补齐，再归档交付 | [English](skills/calendar-meeting-archive/references/README.md) / [中文](skills/calendar-meeting-archive/references/README_zh.md) |
| [文献调研 Literature Search](skills/literature-search/SKILL.md) | 检索筛选文献，形成综述与跨论文可复用研究资产 | [English](skills/literature-search/references/README.md) / [中文](skills/literature-search/references/README_zh.md) |
| [论文分析 Paper Analysis](skills/paper-analysis/SKILL.md) | 论文精读与分析 | [English](skills/paper-analysis/references/README.md) / [中文](skills/paper-analysis/references/README_zh.md) |
| [研究计划 Research Plan](skills/research-plan/SKILL.md) | 从灵感形成研究计划与实验方案 | [English](skills/research-plan/references/README.md) / [中文](skills/research-plan/references/README_zh.md) |
| [Python 环境管理与排障 Python Environment Management](skills/python-environment/SKILL.md) | 检查、准备与诊断项目环境，优先复用已有环境 | [English](skills/python-environment/references/README.md) / [中文](skills/python-environment/references/README_zh.md) |
| [CPU 内存清理 CPU Memory Cleanup](skills/cpu-memory-cleanup/SKILL.md) | 首次初始化 Windows 内存工具，读取真实状态并按请求整理工作集 | [English](skills/cpu-memory-cleanup/references/README.md) / [中文](skills/cpu-memory-cleanup/references/README_zh.md) / [安装包](skills/cpu-memory-cleanup.zip) |

技能显示名统一采用“中文名 English Name”，调用标识仍沿用目录中的英文形式，例如“文献调研 Literature Search”使用 `$literature-search`。中英文名称指向同一技能，不另建中文副本。

## 由其他仓库维护的技能

| 技能 | 用途 | 安装 |
| --- | --- | --- |
| Figma 设计交付 Figma Design Delivery | 新建或改版可编辑设计稿，按规格和运行前端核对原型 | [Figma 仓库发布页](https://github.com/DreamSoul-AI/figma/releases)，需要 DreamSoul Figma 仓库访问权限 |

安装 Figma 设计交付时，从发布页下载 ZIP，把解压得到的整个 `figma-design-delivery` 文件夹放到 `<项目>/.agents/skills/`，再在 Codex 中调用 `$figma-design-delivery`。说明、Node.js 工具和随包依赖一起安装。运行条件见发布页。

## 工具

| 工具 | 用途 | 教程 |
| --- | --- | --- |
| [codex-vscode-windows-notify](tools/codex-vscode-windows-notify/) | Codex VS Code 任务完成后的原生 Windows 通知 | [English](tools/codex-vscode-windows-notify/README.md) / [中文](tools/codex-vscode-windows-notify/README_zh.md) |
| [cpu-memory-cleanup](tools/cpu-memory-cleanup/) | 内存Package与CLI接入说明，不复制清理实现 | [English](tools/cpu-memory-cleanup/README.md) / [中文](tools/cpu-memory-cleanup/README_zh.md) |

## 定时任务

任务定义和配置示例维护在 [automations](automations/README_zh.md)。当前提供 [每日会议总结](automations/daily-meeting-summary/README_zh.md) 的本地审阅稿，复用日历会议归档、会议总结和文档同步三个技能。实际项目填写配置后，另按确认范围部署到调度平台。

## 在 Codex 中安装

把下面这段消息发给 Codex，即可安装一个技能：

```text
$skill-installer
请安装这个目录里的技能：
https://github.com/DreamSoul-AI/knowledge/tree/main/skills/paper-analysis
```

将 paper-analysis 替换为本仓维护的技能目录名即可安装对应技能。
如果手动安装到某个项目，将整个技能文件夹复制到 `<项目>/.agents/skills/` 下，
保留 SKILL.md 和所有随包目录，包括 scripts/。

安装后可以直接说：“请使用 paper-analysis 分析这篇论文。”

## 目录结构

- `skills/<技能名>/SKILL.md`：适用场景和执行流程。
- `skills/<技能名>/agents/openai.yaml`：Codex 界面元数据。
- `skills/<技能名>/references/`：按需阅读的中英文教程。
- `tools/<工具名>/`：包含脚本和使用教程的独立工具。
- `automations/<任务名>/`：任务提示词、配置示例和中英文说明。

每份教程只在对应技能中维护。指向 GitHub 上其他技能的链接仅用于延伸阅读，
不作为本地必需依赖。

## 许可证

[MIT](LICENSE)


## 仓库维护

仓库：[DreamSoul-AI/knowledge](https://github.com/DreamSoul-AI/knowledge)。维护工作先读 [AGENTS.md](AGENTS.md) 的协作与资料定位要求；这些规则约束维护者，不将 DreamSoul 私有资料访问变成安装技能的前置条件。

本仓库分发 Markdown 指令、YAML 元数据和随包脚本。运行条件与验证命令在各技能或工具教程中维护，没有全仓统一安装、构建或测试命令。指南、脚本、引用资源与许可证保持完整。

项目级执行证据从 [运行记录 Run Record](<docs/运行记录 Run Record/>) 定位，变更说明从 [开发记录 Development Record](<docs/开发记录 Development Record/>) 定位。通用调研 General Research、架构设计、代码结构设计、开发计划和缺陷记录尚无独立项目级当前入口，不能用各技能的使用教程冒充已完成的项目工程文档。本分发仓库当前没有独立维护的文献调研或研究计划。入口、依赖或范围变化时同步维护中英文 README。

专项候选的后续工作见 [多仓库共享资源接入计划](<docs/开发 Development/开发计划 Development Plan 多仓库共享资源接入.md>)，不代表全仓开发文档已经补齐。

文档职责按 AGENTS.md 维护：通用调研只回答机制、方案、来源与当前判断，历史设计、迁移和修复经过归开发记录，实际执行及旧结果归运行记录，不保留历史摘要章。设计呈现当前选定方向及实现差距，计划维护后续工作与判据。已有内容尚未符合时逐文件迁移并登记缺口，不能只改名或把旧验证记为当前结果。

长期分支仅保留 `main`（正式发布）和 `dev`（开发集成）。日常从 `dev` 建必要的短期分支，通过 PR 核验后集成，稳定后以 `dev → main` 发布 PR 合入正式版。合并完成当轮清理对应远端和不再使用的本地短期分支；清理前保存未提交改动并核对关联工作区。

## 研发维护

维护入口见 [仓库约定](REPO.md) 和 [研发文档导航](docs/README.md)。

### 待评估能力

**多仓库共享资源接入**：候选，待后续评估是否值得独立技能化。先复用 workspace 的共享目录工具，区分 Agent 的判断与编排、工具的文件操作。评估用户配置、资源及消费者识别、映射和迁移预览、实体目录与 Git 跟踪冲突、在用文件、旧路径保留、完整性及链接目标核验、重复执行和中断接续。评估结论明确独立 Skill、沿用工具或接入已有能力的理由，再确定实现和发布范围。

2026年11月15日已对现有工具完成隔离预览、真实建链、重跑、实体目录冲突、Git 跟踪拦截和注入中断后的接续验证，详见 [运行记录](<docs/运行记录 Run Record/2026-11-15 定时任务与共享资源验证.md>)。下一步评估重点为可移植的配置与判断流程，以及现有初始化工具未提供的实体迁移边界，尚未创建或发布独立技能。

交接来源为关联 workspace 仓库中的 `docs/经验 Learnings/多仓库共享目录与符号链接.md`、`工具/本机共享目录/README.md`、同目录 `link_shared.py` 与 `初始化共享目录.cmd`，以及 `USER.template.md` 的共享根配置和 `使用教程.md` 的“共享数据与产物”。这些材料交接时尚未提交发布，后续按实际关联目录读取最新来源，不视为本仓库已分发的依赖。

当前脚本负责预览和建立共享入口，实体数据迁移仍需另行处理。个人路径和业务数据保留在运行环境，符号链接权限按实际进程核验。既有迁移结果作为来源记录，本候选登记不触发再次迁移或真实数据操作。
