# Grok Bot CLI

[English](README.md)

knowledge 提供本地启动入口，实际 CLI 由 [ScriptedAlchemy/grok-bot-cli](https://github.com/ScriptedAlchemy/grok-bot-cli) 提供，上游采用 MIT 许可。安装时从 npm 获取原包。桌面会话由本机 Grok Bot 管理。

在本目录执行以下命令。需要 Node.js 22.19.0 或更新版本。这里固定的是本次检查的版本。

```text
npm install --no-save --package-lock=false --ignore-scripts grok-bot-cli@0.12.5
node gbot.mjs --help
```

如果已经安装了上游包，可用 `node gbot.mjs --package-dir <已安装包目录> --help`，目录内应有 upstream 的 `package.json`。入口把其余参数交给本机 CLI。从空参数启动也只显示帮助。

业务运行时先在同一系统用户下登录桌面端，可从 `node gbot.mjs bots list --json` 验证读取。写入或发送前核对目标和授权。若遇到路由 404，按 [上游问题 #168](https://github.com/ScriptedAlchemy/grok-bot-cli/issues/168) 核对版本与症状。安装、桌面认证、实际收发分别验证。本目录交付的是上游 CLI 启动入口，Windows MCP 隔离修复另见 [接入教程](https://dreamsoul.feishu.cn/docx/Sqsdd69p7osKAqxx5UwcJeOEn1e)。

Windows 上使用 0.12.5 遇到 #168 类型的名单查询 404 时，可运行 `node gbot.mjs --windows-roster-fix`。复用全局安装时运行 `node gbot.mjs --package-dir <已安装包目录> --windows-roster-fix`。此模式复用教程中的临时隔离修订，只查 Bot 名单，使用原包的本机登录、账号绑定、域名检查和超时。它不改 npm 安装，也不用于发消息或配置 MCP。

Agent 接入和日常操作使用 [Grok Bot CLI 技能及随包教程](../../skills/grok-bot-cli/SKILL.md)。提交或分享时保留公开入口和说明，安装目录、会话、凭据及测试目标留在本机。
