# Codex Windows Notify

Show a native Windows toast when a Codex turn completes. Clicking the toast opens the turn's working directory in VS Code.

No dependencies beyond Windows PowerShell and VS Code.

## Configure

Add this user-level setting to `~/.codex/config.toml`:

```toml
notify = [
  "powershell.exe",
  "-NoProfile",
  "-ExecutionPolicy",
  "Bypass",
  "-File",
  "D:\\GitHub\\DreamSoul\\codex-windows-notify\\notify-windows.ps1"
]
```

Reload VS Code and start a new Codex session after changing the configuration.

## Behavior

- Handles `agent-turn-complete` events.
- Uses the event's `cwd` and `last-assistant-message` fields.
- Shows the notification as Visual Studio Code.
- Opens `vscode://file/<cwd>` when clicked.
