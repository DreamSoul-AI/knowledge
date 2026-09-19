# Codex Windows Notify

Codex 完成一轮任务后显示原生 Windows 通知。点击通知会用 VS Code 打开该轮任务的工作目录。

它使用 Codex 官方的 `notify` 配置，无第三方依赖，不上传任何数据。

## 环境要求

- Windows 10/11
- Windows PowerShell 5.1 或更高版本
- Visual Studio Code
- 本地运行的 Codex（CLI 或 VS Code 扩展）

## 安装

在 PowerShell 中克隆本仓库并执行安装器：

```powershell
git clone <本仓库的 GitHub URL>
cd codex-windows-notify
powershell.exe -NoProfile -ExecutionPolicy Bypass -File .\install.ps1
```

安装器会：

1. 将通知脚本复制到 `~/.codex/scripts/codex-windows-notify.ps1`；
2. 在用户级 `~/.codex/config.toml` 中写入 `notify`；
3. 立即发送一条测试通知。

安装后重启 VS Code，或新建一个 Codex 会话。之后 Codex 每轮完成时都会通知；点击通知会回到对应项目。

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

将 `notify-windows.ps1` 放到固定位置，并把下面配置加入用户级 `~/.codex/config.toml`。Windows 路径中的反斜杠要写成 `\\`：

```toml
notify = ["powershell.exe", "-NoProfile", "-ExecutionPolicy", "Bypass", "-File", "C:\\path\\to\\notify-windows.ps1"]
```

`notify` 不能放在项目内的 `.codex/config.toml`，Codex 会忽略项目级通知配置。

## 工作方式

- 只处理 `agent-turn-complete` 事件；
- 使用事件中的 `cwd` 和 `last-assistant-message`；
- 通过 Windows 原生 WinRT API 显示通知；
- 点击后打开 `vscode://file/<cwd>`；
- 不访问网络，不保存会话内容。

## 官方参考

- [OpenAI Codex 高级配置：通知](https://developers.openai.com/zh-Hans/docs/config-file/config-advanced#%E9%80%9A%E7%9F%A5)

官方文档说明了 `notify` 的用户级配置位置、`agent-turn-complete` 事件，以及传给脚本的 JSON 字段。
