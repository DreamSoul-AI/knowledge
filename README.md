# Codex VS Code Windows Notify

**English**&nbsp; | &nbsp;[**简体中文**](https://github.com/DreamSoul-AI/codex-vscode-windows-notify/blob/main/README_zh.md)

Show a native Windows notification when a Codex turn finishes in the VS Code
extension. Clicking the notification opens that turn's working directory in
Visual Studio Code.

Codex Desktop sessions are ignored so they can use the desktop app's native
notifications without producing a second VS Code notification.

The project uses Codex's official `notify` configuration. It has no third-party
dependencies, does not access the network, and does not upload any data.

## Requirements

- Windows 10 or 11
- Windows PowerShell 5.1 or later
- Visual Studio Code
- The Codex VS Code extension running locally

## Install

Clone the repository and run the installer in PowerShell:

```powershell
git clone https://github.com/DreamSoul-AI/codex-vscode-windows-notify.git
cd codex-vscode-windows-notify
powershell.exe -NoProfile -ExecutionPolicy Bypass -File .\install.ps1
```

The installer:

1. Copies the notification script to
   `~/.codex/scripts/codex-windows-notify.ps1`.
2. Adds `notify` to the user-level `~/.codex/config.toml`.
3. Sends one test notification.

Restart VS Code or start a new Codex session after installation. Each completed
turn in the VS Code extension will then produce one notification; clicking it
opens the corresponding project.

If another `notify` command is already configured, the installer will not
overwrite it automatically. To confirm replacement, run:

```powershell
powershell.exe -NoProfile -ExecutionPolicy Bypass -File .\install.ps1 -Force
```

The previous configuration is backed up to
`~/.codex/config.toml.codex-windows-notify.bak`.

## Uninstall

Run this command from the repository directory:

```powershell
powershell.exe -NoProfile -ExecutionPolicy Bypass -File .\install.ps1 -Uninstall
```

The uninstaller removes only the notification configuration and script created
by this installer. It keeps a configuration backup.

## Manual setup

Place `notify-windows.ps1` at a stable path and add the following user-level
configuration. Backslashes in Windows paths must be doubled in TOML:

```toml
notify = ["powershell.exe", "-NoProfile", "-ExecutionPolicy", "Bypass", "-File", "C:\\path\\to\\notify-windows.ps1"]
```

Codex ignores `notify` in a project-local `.codex/config.toml`, so this setting
must be placed in the user-level configuration.

## How it works

- Handles only `agent-turn-complete` events.
- Reads local session metadata and accepts only
  `originator = codex_vscode` by default.
- Leaves Codex Desktop sessions to the desktop app's native notification path.
- Deduplicates each `turn-id`, including events forwarded more than once.
- Uses the event's `cwd` and `last-assistant-message` fields.
- Displays the notification through the native Windows WinRT API.
- Opens `vscode://file/<cwd>` when the notification is clicked.
- Does not access the network or save session content.

To enable this external notification for every Codex client, append
`-AllowedOriginator *` to the command. Doing so can produce both a Codex Desktop
notification and an external VS Code notification for the same turn.

## Official reference

- [OpenAI Codex advanced configuration: notifications](https://developers.openai.com/docs/config-file/config-advanced#notifications)

The official documentation describes the user-level `notify` setting, the
`agent-turn-complete` event, and the JSON fields passed to notification scripts.
