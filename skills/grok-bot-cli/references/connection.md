# Codex 连接 Grok Bot

本页把原飞书教程的 CLI、MCP 和故障判断整理成可离线阅读的步骤。上游是社区项目，桌面端登录仍依赖实际环境。[原接入教程](https://dreamsoul.feishu.cn/docx/Sqsdd69p7osKAqxx5UwcJeOEn1e) · [上游项目](https://github.com/ScriptedAlchemy/grok-bot-cli)

## 安装和只读验证

在运行 CLI 的设备打开 Grok Bot 桌面端，使用同一操作系统账号，并确认桌面端可见目标 Bot。Node.js 要求为 22.19.0 或更高。先检查现有安装，缺失时按本机环境安装上游包。下例固定到曾核对的版本。

```text
node --version
npm install --global grok-bot-cli@0.12.5
gbot --help
gbot doctor --json
gbot bots list --json
```

只检查安装时运行帮助即可。诊断和名单查询依赖本机桌面会话和实际资源权限。若 Windows 找不到命令，重新打开 PowerShell 后用 `Get-Command gbot` 检查。若从 knowledge 工具目录启动，将命令中的 `gbot` 替换成 `node gbot.mjs`，并按工具 README 安装依赖或指定已有包。

## 一次收发验证

只有在用户已经指定实际目标并授权发送时才运行发送。使用唯一短编号，取得回执后从同一会话查找该编号对应的回复。回执证明受理，真实回复才证明此次往返有效。

```powershell
$bot = '<已核对的完整 Bot 名>'
$marker = 'Codex 连通测试 ' + [guid]::NewGuid().ToString('N').Substring(0, 8)
gbot send $bot "请回复 $marker" --json
gbot thread $bot --json
```

暂未回复时只继续读取。发送状态不明时先查编号是否已出现。连续读取可以使用 `gbot thread --after <条目 ID>`，游标失效要按返回标识处理，不能把重新出现的历史消息当成新增。

## MCP 和 Windows 路由故障

使用已安装的 Grok Bot 插件时，先检查当前 Codex 会话加载了哪些工具。只读先使用 `gbot_thread`，需要正文时按当期工具参数打开全文。已授权发送才使用 `gbot_send`，支持时选手动回读，再用相同目标读取真实回复。插件入口和版本条件见[上游说明](https://github.com/ScriptedAlchemy/grok-bot-cli#plugins)。

如果帮助正常而 `bots list` 或 `gbot_thread` 返回旧网关路由 404，记录系统、桌面端版本和 CLI 版本，先看 `doctor` 的认证来源状态，再比较[上游问题 #168](https://github.com/ScriptedAlchemy/grok-bot-cli/issues/168)。原飞书教程保存了 Windows 隔离副本的完整步骤和脚本，建立在 0.12.5 的特定日志和环境上。知识库的启动器直接调用上游 CLI。不要从示例复制账号、设备标识、会话凭据或真实目标。

若只需排查 Windows 0.12.5 名单查询，从 knowledge 的工具目录运行 `node gbot.mjs --windows-roster-fix`。复用已安装包时在该参数前加 `--package-dir <已安装包目录>`。这条路径与飞书教程采用同一修订方法，范围只包含名单读取。

历史 Windows 试跑分别验证过从 Codex 发出消息和由 Codex 主动读回回复。Bot 主动向 Codex 回传属于单独路径，需要按目标设备与会话重新验证。逐段报告实际结果。
