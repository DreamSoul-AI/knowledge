# DreamSoul Knowledge

[**English**](README.md)&nbsp; | &nbsp;**简体中文**

可复用的 Agent 技能、独立工具和定时任务定义。每个技能都包含自己的执行说明和参考资料，可以独立安装。

## 技能 Skills

按用途查找通用流程；依赖具体平台的技能集中列在“平台接入”。会议整理等通用流程仍可按各自说明接入飞书。

### 工作整理

| **技能** | **用途** | **说明** |
| --- | --- | --- |
| [收尾 wrap-up](skills/wrap-up/SKILL.md) | 默认先盘点能否收尾，明确要求后执行尾项 | [English](skills/wrap-up/references/README.md) / [中文](skills/wrap-up/references/README_zh.md) |
| [工作总结 work-summary](skills/work-summary/SKILL.md) | 盘点成果、依据和未收尾项 | [English](skills/work-summary/references/README.md) / [中文](skills/work-summary/references/README_zh.md) |
| [学习与经验提炼 learn](skills/learn/SKILL.md) | 回看过程、积累案例并提炼有依据的可复用做法 | [使用说明](skills/learn/SKILL.md) |
| [工作留言 work-message](skills/work-message/SKILL.md) | 按各留言板成文，按授权交付 | [English](skills/work-message/references/README.md) / [中文](skills/work-message/references/README_zh.md) |
| [会议总结 meeting-minutes](skills/meeting-minutes/SKILL.md) | 结合原始材料、补充材料和规范整理会议 | [English](skills/meeting-minutes/references/README.md) / [中文](skills/meeting-minutes/references/README_zh.md) |

### 对话

| **技能** | **用途** | **说明** |
| --- | --- | --- |
| [对话管理 conversation-management](skills/conversation-management/SKILL.md) | 管理指定对话，衔接相关能力 | [用法](skills/conversation-management/SKILL.md) |
| [对话回顾 conversation-review](skills/conversation-review/SKILL.md) | 回看已有记录、决定和纠正 | [English](skills/conversation-review/references/README.md) / [中文](skills/conversation-review/references/README_zh.md) |
| [对话归档 conversation-archive](skills/conversation-archive/SKILL.md) | 按受支持的适配保真保存原文 | [English](skills/conversation-archive/references/README.md) / [中文](skills/conversation-archive/references/README_zh.md) / [含 review 的 ZIP](skills/conversation-archive.zip) |
| [对话恢复 conversation-resume](skills/conversation-resume/SKILL.md) | 沿实际断点继续已授权工作 | [English](skills/conversation-resume/references/README.md) / [中文](skills/conversation-resume/references/README_zh.md) |
| [对话刷新 conversation-refresh](skills/conversation-refresh/SKILL.md) | 按变化让指定对话重读工作区规则 | [English](skills/conversation-refresh/references/README.md) / [中文](skills/conversation-refresh/references/README_zh.md) |

按当前平台实际可用的记录和工具执行。随包原始记录读取器和已验证的不可变归档目前针对 Codex JSONL；Codex 项目、侧栏调整及跨对话恢复、刷新需要相应原生工具。通用名称不代表所有平台均支持这些操作。已有公开 Markdown 或文本可以按其实际范围回顾，但不能据此声称已取得 Codex 原始记录。

conversation-archive 依赖同级完整 conversation-review。同装两个技能目录，或解压归档 ZIP 中的两个完整包；conversation-review 也可单独使用。

### 项目管理

| **技能** | **用途** | **说明** |
| --- | --- | --- |
| [项目进展同步 project-progress-sync](skills/project-progress-sync/SKILL.md) | 核对日志和任务差异，按授权双向同步进展 | [English](skills/project-progress-sync/references/README.md) / [中文](skills/project-progress-sync/references/README_zh.md) |

### 调研研究

| **技能** | **用途** | **说明** |
| --- | --- | --- |
| [通用调研 general-search](skills/general-search/SKILL.md) | 调研技术、工具和工程实践 | [English](skills/general-search/references/README.md) / [中文](skills/general-search/references/README_zh.md) |
| [文献调研 literature-search](skills/literature-search/SKILL.md) | 检索筛选文献，形成综述与跨论文可复用研究资产 | [English](skills/literature-search/references/README.md) / [中文](skills/literature-search/references/README_zh.md) |
| [论文入库 paper-intake](skills/paper-intake/SKILL.md) | 核验并收录指定论文，维护索引及多目标同步交接 | [English](skills/paper-intake/references/README.md) / [中文](skills/paper-intake/references/README_zh.md) |
| [论文分析 paper-analysis](skills/paper-analysis/SKILL.md) | 论文精读与分析 | [English](skills/paper-analysis/references/README.md) / [中文](skills/paper-analysis/references/README_zh.md) |
| [研究计划 research-plan](skills/research-plan/SKILL.md) | 从灵感形成研究计划与实验方案 | [English](skills/research-plan/references/README.md) / [中文](skills/research-plan/references/README_zh.md) |

### 研发运行

| **技能** | **用途** | **说明** |
| --- | --- | --- |
| [代码架构分析 code-architecture-analysis](skills/code-architecture-analysis/SKILL.md) | 依据源码和运行证据核对架构结论 | [用法](skills/code-architecture-analysis/SKILL.md) |
| [Python 环境管理与排障 python-environment](skills/python-environment/SKILL.md) | 检查、准备与诊断项目环境，优先复用已有环境 | [English](skills/python-environment/references/README.md) / [中文](skills/python-environment/references/README_zh.md) |
| [公开网站部署 public-website-deployment](skills/public-website-deployment/SKILL.md) | 发布和更新静态网站，管理域名及迁移 | [English](skills/public-website-deployment/references/README.md) / [中文](skills/public-website-deployment/references/README_zh.md) |
| [Agent 实验执行 agent-experiment](skills/agent-experiment/SKILL.md) | 实跑有界 Agent 实验，核对实际行为和结论 | [English](skills/agent-experiment/references/README.md) / [中文](skills/agent-experiment/references/README_zh.md) |
| [能力更新 knowledge-update](skills/knowledge-update/SKILL.md) | 检查或更新已采用技能和工具，保留定制 | [English](skills/knowledge-update/references/README.md) / [中文](skills/knowledge-update/references/README_zh.md) |
| [工作区同步 workspace-sync](skills/workspace-sync/SKILL.md) | 默认更新本地工作区，可选组织仓库分发 | [English](skills/workspace-sync/references/README.md) / [中文](skills/workspace-sync/references/README_zh.md) |

### 平台接入

| **平台** | **技能** | **用途** | **说明** |
| --- | --- | --- | --- |
| 飞书 | [日历会议归档 calendar-meeting-archive](skills/calendar-meeting-archive/SKILL.md) | 按负责人归档会议，优先复用已有成果 | [English](skills/calendar-meeting-archive/references/README.md) / [中文](skills/calendar-meeting-archive/references/README_zh.md) |
| 飞书 | [文档同步 document-sync](skills/document-sync/SKILL.md) | 同步指定文档，检查基线和冲突，目前支持飞书 | [English](skills/document-sync/references/README.md) / [中文](skills/document-sync/references/README_zh.md) |
| 飞书 | [飞书授权复用 lark-auth-reuse](skills/lark-auth-reuse/SKILL.md) | 复用对话间已有飞书授权，诊断执行身份差异 | [English](skills/lark-auth-reuse/references/README.md) / [中文](skills/lark-auth-reuse/references/README_zh.md) |
| Grok Bot | [Grok Bot 接入 grok-bot-cli](skills/grok-bot-cli/SKILL.md) | 连接 Grok Bot，检查访问及按授权验证收发 | [接入说明](skills/grok-bot-cli/references/connection.md) |
| GitHub | [GitHub 汇总 github-summary](skills/github-summary/SKILL.md) | 接收固定版本经验原文，按接收方归并 | [English](skills/github-summary/references/README.md) / [中文](skills/github-summary/references/README_zh.md) |
| Windows | [CPU 内存清理 cpu-memory-cleanup](skills/cpu-memory-cleanup/SKILL.md) | 读取 Windows 内存，按请求整理工作集 | [English](skills/cpu-memory-cleanup/references/README.md) / [中文](skills/cpu-memory-cleanup/references/README_zh.md) / [安装包](skills/cpu-memory-cleanup.zip) |


### 设计

| **平台** | **技能** | **用途** | **安装** |
| --- | --- | --- | --- |
| Figma | [Figma 设计 figma-design](https://github.com/DreamSoul-AI/figma/blob/main/src/figma-design/SKILL.md) | 按独立维护的完整工作流制作可编辑设计稿并验证原型 | [v1.1.1 安装包与说明](https://github.com/DreamSoul-AI/figma/releases/tag/figma-design-v1.1.1)，需要 Figma 仓库访问权限 |

完整工作流与互译手册统一在 Figma 仓库维护，knowledge 只保留发现和安装入口，不维护第二份正文。

安装 Figma 设计时，从发布页下载 ZIP，把解压得到的整个 `figma-design` 文件夹放到 `<项目>/.agents/skills/`，再在 Codex 中调用 `$figma-design`。说明、Node.js 工具和随包依赖一起安装。运行条件见发布页。已有旧名 `figma-design-delivery` 安装时，先保留个人修改，再替换为完整新版，避免同时加载两份 Skill。

中文名称可与英文标识并列，便于搜索。技能英文标识使用小写连字符，如 `work-message`，调用时使用 `$work-message`，不另建中文副本。

## 工具 Tools

| **平台** | **工具** | **用途** | **使用说明** |
| --- | --- | --- | --- |
| Grok Bot | [Grok Bot 命令行工具 grok-bot-cli](tools/grok-bot-cli/) | 启动本机安装的上游 CLI | [English](tools/grok-bot-cli/README.md) / [中文](tools/grok-bot-cli/README_zh.md) |
| Codex / VS Code / Windows | [Codex VS Code 通知 codex-vscode-windows-notify](tools/codex-vscode-windows-notify/) | Codex VS Code 任务完成后的原生 Windows 通知 | [English](tools/codex-vscode-windows-notify/README.md) / [中文](tools/codex-vscode-windows-notify/README_zh.md) |
| Windows | [CPU 内存清理 cpu-memory-cleanup](tools/cpu-memory-cleanup/) | 内存Package与CLI接入说明，不复制清理实现 | [English](tools/cpu-memory-cleanup/README.md) / [中文](tools/cpu-memory-cleanup/README_zh.md) |
| 本地文件系统 | [多仓库共享资源接入 shared-repository-resources](tools/shared-repository-resources/) | 按配置复用目录资源；新示例使用 `shared/` 存储、`.shared/` 仓内入口 | [English](tools/shared-repository-resources/README.md) / [中文](tools/shared-repository-resources/README_zh.md) |

## 定时任务 Automations

定时任务在 [automations](automations/README_zh.md) 独立维护，通过提示词和外部配置组合已有技能。

| 定时任务 | 用途 | 状态 | 说明 |
| --- | --- | --- | --- |
| [每日会议总结 Daily Meeting Summary](automations/daily-meeting-summary/) | 增量归档会议、整理总结并按授权交付 | 首版，手动复用流程已验证 | [中文](automations/daily-meeting-summary/README_zh.md) / [English](automations/daily-meeting-summary/README.md) |
| [每日电子邮件总结 Daily Email Summary](automations/daily-email-summary/) | 按自定义邮箱整理主题、下一步行动及原邮件入口 | 首版定义，Outlook 读取与格式已验证，调度待验证 | [中文](automations/daily-email-summary/README_zh.md) / [English](automations/daily-email-summary/README.md) |
| [每日工作区更新 daily-workspace-update](automations/daily-workspace-update/) | 更新已采用工作区，接续已采用技能和工具 | 整轮只检查已验证，更新与触发待验 | [中文](automations/daily-workspace-update/README_zh.md) / [English](automations/daily-workspace-update/README.md) |

实际项目按自己的配置和授权部署。最近手动运行未触发新增生成、上传写入和实际定时触发，具体覆盖范围见 [任务总表](automations/README_zh.md)。

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

原 `ai-work-message` 已改名为 `work-message`。安装完整的
[work-message 目录](skills/work-message/)，升级前保留个人修改，避免同时加载新旧两份技能。
旧文档链接保留迁移提示，不再提供第二份可安装的技能。

对话技能统一使用 `conversation-management`、`conversation-review`、`conversation-archive`、`conversation-resume` 和 `conversation-refresh`。旧名 `codex-conversation-management`、`codex-conversation-review`、`codex-conversation-archive`、`resume-chat`（更早为 `resume-interrupted-chat`）、`refresh-chat` 仅作迁移说明。替换完整包时保留个人修改，只保留新名可被发现，不把旧名作为另一份活跃技能安装。

## 目录结构

- `skills/<技能名>/SKILL.md`：适用场景和执行流程。
- `skills/<技能名>/agents/openai.yaml`：Codex 界面元数据。
- `skills/<技能名>/references/`：按需阅读的中英文使用说明。
- `tools/<工具名>/`：包含脚本和使用说明的独立工具。
- `automations/<任务名>/`：任务提示词、配置示例和中英文说明。

使用说明随对应技能维护。指向 GitHub 上其他技能的链接仅用于延伸阅读，
不作为本地必需依赖。

## 许可证

[MIT](LICENSE)


## 仓库维护

仓库：[DreamSoul-AI/knowledge](https://github.com/DreamSoul-AI/knowledge)。维护工作先读 [AGENTS.md](AGENTS.md) 的协作与资料定位要求；这些规则约束维护者，不将 DreamSoul 私有资料访问变成安装技能的前置条件。

本仓库分发 Markdown 指令、YAML 元数据和随包脚本。运行条件与验证命令在各技能或工具的使用说明中维护，没有全仓统一安装、构建或测试命令。说明、脚本、引用资源与许可证保持完整。

项目级执行证据从 [运行记录 Run Record](<docs/运行记录 Run Record/>) 定位，变更说明从 [开发记录 Development Record](<docs/开发记录 Development Record/>) 定位。通用调研 General Research、架构设计、代码结构设计、开发计划和缺陷记录尚无独立项目级当前入口，不能用各技能的使用说明冒充已完成的项目工程文档。本分发仓库当前没有独立维护的文献调研或研究计划。入口、依赖或范围变化时同步维护中英文 README。

专项候选的后续工作见 [多仓库共享资源接入计划](<docs/开发 Development/开发计划 Development Plan 多仓库共享资源接入.md>)，不代表全仓开发文档已经补齐。

文档职责按 AGENTS.md 维护：通用调研只回答机制、方案、来源与当前判断，历史设计、迁移和修复经过归开发记录，实际执行及旧结果归运行记录，不保留历史摘要章。设计呈现当前选定方向及实现差距，计划维护后续工作与判据。已有内容尚未符合时逐文件迁移并登记缺口，不能只改名或把旧验证记为当前结果。

通用开发使用 `main`（正式发布）和 `dev`（开发集成），已登记的个人长期分支按[仓库约定](REPO.md)保留，不纳入任务分支清理。日常从 `dev` 建必要的短期分支，通过 PR 核验后集成，稳定后以 `dev → main` 发布 PR 合入正式版。合并完成当轮清理对应远端和不再使用的本地短期分支；清理前保存未提交改动并核对关联工作区。

## 研发维护

维护入口见 [仓库约定](REPO.md) 和 [研发文档导航](docs/README.md)。

### 待评估能力

**多仓库共享资源接入**：已提供可配置目录资源和逐仓库映射的 [工具](tools/shared-repository-resources/README_zh.md)，研发惯例作为可选示例。Agent 侧的识别与迁移编排仍属候选，尚未新增独立技能。后续范围及采用边界见 [当前计划](<docs/开发 Development/开发计划 Development Plan 多仓库共享资源接入.md>)。
