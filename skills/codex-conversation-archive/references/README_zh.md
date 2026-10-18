# Codex 会话归档

从指定本地 JSONL 会话生成沟通流程 Markdown，逐字符核对用户原话和正式回复。摘要单列；保留公开进度、实际工具记录和转达来源，排除隐藏推理。

## 安装与首次使用

需要 Python 3.8+，只使用标准库。下载完整技能目录或解压安装包，将整个 `codex-conversation-archive` 放入 `<项目>/.agents/skills/`。不要只复制 SKILL.md。重新打开项目会话，让 Codex 读取技能。

也可让 Codex 的 skill-installer 安装 GitHub 上的技能目录，使用实际发布分支的链接。

```text
用 $codex-conversation-archive 归档本会话到本条请求。
事项名称：首次会话归档
保存位置：本项目的归档目录
保留用户原话、正式回复、转达来源和实际工具记录，摘要单列。
先只保存本地，不同步云端，不启用定时任务。
```

指定其他会话时提供确切会话 ID 或 JSONL 路径。通常从当前用户的 Codex 数据目录 `sessions/` 按 ID 匹配文件名，必须核对 session_meta；远端或云端会话需要先取得对应原始记录。无需手动复制正文。

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

运行 `python -B <技能目录>/scripts/test_archive.py` 执行合成边界测试。发布前另以 ZIP 在干净目录、隔离 Python 下完成首次归档、原话核对、重复和增量测试。只证明已观察到的本地格式可用，不代表新用户客户端加载、其他 Codex 版本、所有操作系统或 UI 全量导出均已验证。缺失、截断和记录外的附件不能恢复，不用摘要补齐。
