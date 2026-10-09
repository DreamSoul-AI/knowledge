# Codex VS Code Windows Notify

[**English**](https://github.com/DreamSoul-AI/codex-vscode-windows-notify/blob/main/README.md)&nbsp; | &nbsp;**简体中文**

Codex VS Code 扩展完成一轮任务后显示原生 Windows 通知。点击通知会用 Visual
Studio Code 打开该轮任务的工作目录。

脚本会忽略 Codex Desktop 会话，让桌面应用继续使用自己的原生通知，避免同一轮任务
同时出现 Codex 和 VS Code 两条通知。

本项目使用 Codex 官方的 `notify` 配置，无第三方依赖，不访问网络，也不上传任何数据。

## 环境要求

- Windows 10/11
- Windows PowerShell 5.1 或更高版本
- Visual Studio Code
- 本地运行的 Codex VS Code 扩展

## 安装

在 PowerShell 中克隆本仓库并执行安装器：

```powershell
git clone https://github.com/DreamSoul-AI/codex-vscode-windows-notify.git
cd codex-vscode-windows-notify
powershell.exe -NoProfile -ExecutionPolicy Bypass -File .\install.ps1
```

安装器会：

1. 将通知脚本复制到 `~/.codex/scripts/codex-windows-notify.ps1`；
2. 在用户级 `~/.codex/config.toml` 中写入 `notify`；
3. 立即发送一条测试通知。

安装后重启 VS Code，或新建一个 Codex 会话。之后 VS Code 扩展中的每轮任务完成时
都会通知；点击通知会回到对应项目。

如果已经配置了其他 `notify`，安装器不会擅自覆盖。确认要替换时运行：

```powershell
powershell.exe -NoProfile -ExecutionPolicy Bypass -File .\install.ps1 -Force
```

替换前的配置会备份为 `~/.codex/config.toml.codex-windows-notify.bak`。

## 卸载

在仓库目录运行：

```powershell
powershell.exe -NoProfile -ExecutionPolicy Bypass -File .\install.ps1 -Uninstall
```

卸载器只会移除由本安装器写入的通知配置和脚本，并保留配置备份。

## 手动安装

将 `notify-windows.ps1` 放到固定位置，并把下面配置加入用户级配置。Windows 路径中的
反斜杠要在 TOML 中写成 `\\`：

```toml
notify = ["powershell.exe", "-NoProfile", "-ExecutionPolicy", "Bypass", "-File", "C:\\path\\to\\notify-windows.ps1"]
```

`notify` 不能放在项目内的 `.codex/config.toml`，Codex 会忽略项目级通知配置。

## 工作方式

- 只处理 `agent-turn-complete` 事件；
- 默认读取本地会话元数据，只接受 `originator = codex_vscode` 的事件；
- Codex Desktop 会话继续使用桌面应用自己的原生通知；
- 同一 `turn-id` 只通知一次，包括被多次转发的完成事件；
- 使用事件中的 `cwd` 和 `last-assistant-message`；
- 通过 Windows 原生 WinRT API 显示通知；
- 点击后打开 `vscode://file/<cwd>`；
- 不访问网络，不保存会话内容。

如需对所有 Codex 客户端启用此外部通知，可在命令末尾添加
`-AllowedOriginator *`。启用后，同一轮 Codex Desktop 任务可能同时出现 Codex 原生
通知和 VS Code 外部通知。

## 官方参考

- [OpenAI Codex 高级配置：通知](https://developers.openai.com/zh-Hans/docs/config-file/config-advanced#%E9%80%9A%E7%9F%A5)

官方文档说明了用户级 `notify` 配置、`agent-turn-complete` 事件，以及传给通知脚本的
JSON 字段。
