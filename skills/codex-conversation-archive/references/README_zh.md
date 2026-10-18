# Codex 会话归档

从指定本地 JSONL 会话生成沟通流程 Markdown，逐字符核对用户原话和正式回复。摘要单列；保留公开进度、实际工具记录和转达来源，排除隐藏推理。

## 安装与首次使用

需要 Python 3.8+，以及读取目标原始记录、运行 Python 和写入归档目录的权限。先向 Codex 发送安装请求，把项目路径替换为实际值：

```text
用 $skill-installer 安装 https://github.com/DreamSoul-AI/knowledge/tree/main/skills/codex-conversation-archive
安装到 <项目绝对路径>/.agents/skills/，保留完整技能目录，不使用旧的同名安装。
只安装，不归档，不启用定时任务。
```

也可解压[安装包](https://github.com/DreamSoul-AI/knowledge/raw/refs/heads/main/skills/codex-conversation-archive.zip)，把完整目录放到上述位置，不能只复制 SKILL.md。安装后在下一轮请求调用；若未加载，重新打开项目会话。已有同名技能时先核对实际加载路径和版本，不默认卸载全局技能。

归档当前会话：

```text
用 $codex-conversation-archive 归档本会话到本条请求。
事项名称：首次会话归档
保存位置：本项目的归档目录
保留用户原话、正式回复、转达来源和工具原件，摘要四节各一两句，主要供 AI 读取。
先只保存本地，不同步云端，不启用定时任务。
```

归档指定会话：

```text
用 $codex-conversation-archive 归档指定 Codex 会话。
会话：<确切会话 ID 或 JSONL 路径>
事项名称：填写事项。保存位置：填写本地归档目录。
固定到本次首次读取时可取得的最后一条完整公开记录。
保留用户原话、正式回复、转达来源和工具原件，摘要四节各一两句，主要供 AI 读取。
只保存本地，不同步云端，不启用定时任务。
```

通常从当前用户的 Codex 数据目录 `sessions/` 按 ID 匹配文件名，必须核对 session_meta。只有标题时，可通过会话列表元数据定位；不能唯一确定时询问 ID 或路径。远端或云端会话需要先取得对应原始记录。不扫描全部聊天正文，不需要手动复制，不用会话摘要补原文。

继续归档时说“用此技能增量归档本会话”或“增量归档会话 <ID>”，沿用该会话的输出目录和事项名称。当前会话截止到本次请求；其他会话固定首次读取的截止点。不会向目标会话发消息。

优先用工作区最新规范；没有独立规范时使用随包 [归档规则](archive-standard.md)。`--rules` 记录规范哈希，不会自动适配任意新结构。详细操作见 [SKILL.md](../SKILL.md)，适配限制见 [记录格式](record-format.md)。

## 命令与结果

从实际安装目录调用脚本，下例路径和 ID 均替换为实际值：

```text
python <技能目录>/scripts/archive.py --source <会话.jsonl> --session <会话ID> --title 首次会话归档 --output <归档目录> --through-id <截止消息ID>
```

路径含空格时加引号。首次运行的摘要是占位内容；让 Agent 依据公开原文整理四节摘要文件，再加 `--summary <摘要.md>` 以相同截止点重跑，才作为完成文档交付。摘要文件以 `# 一、流程摘要` 开头。

`current.json` 指向不可变 `versions/<哈希>/`，内含 Markdown、archive.json、tools.json、verification.json。重复同一输入应新增 0 条；后续增量沿用同一输出目录，历史变化时停止，不覆盖旧版。不要手改生成文件。

本地原文和工具输出可能含敏感内容，生成后先审阅再分享；不要把实际会话记录提交到公开仓库。Markdown 不保存默认折叠，飞书同步须另行授权并设置、实际验证折叠。本技能不安装定时任务或后台监听。

## 验证范围

已验证 Windows 上 ZIP 隔离运行、从 GitHub 安装后的 Codex CLI 调用，以及 Codex 桌面端干净项目的项目级安装、技能识别、首次归档、真实新消息增量和重复新增 0 条；桌面测试移除了旧同名安装，并逐字符核对原话与正式回复。9 项合成回归测试通过，可用 `python -B <技能目录>/scripts/test_archive.py` 复核。

测试沿用已有登录账号，未验证全新系统账号、其他操作系统或版本、桌面 UI 技能选择器及 UI 导出的全量等价性。缺失、截断和记录外的附件不能恢复，不用摘要补齐。
