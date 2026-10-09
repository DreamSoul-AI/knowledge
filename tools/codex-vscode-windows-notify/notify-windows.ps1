param(
    [string]$Json,
    [string]$AllowedOriginator = 'codex_vscode'
)

$event = $Json | ConvertFrom-Json
if ($event.type -ne 'agent-turn-complete') {
    exit 0
}

$threadId = [string]$event.'thread-id'
if ($AllowedOriginator -ne '*') {
    if ([string]::IsNullOrWhiteSpace($threadId)) {
        exit 0
    }

    $codexDirectory = if ($env:CODEX_HOME) {
        $env:CODEX_HOME
    } else {
        Join-Path $env:USERPROFILE '.codex'
    }
    $sessionsDirectory = Join-Path $codexDirectory 'sessions'
    $originator = $null
    if (Test-Path -LiteralPath $sessionsDirectory) {
        $sessionFiles = Get-ChildItem -LiteralPath $sessionsDirectory -Recurse -File -Filter "*$threadId.jsonl" -ErrorAction SilentlyContinue |
            Sort-Object LastWriteTime -Descending
        foreach ($sessionFile in $sessionFiles) {
            try {
                $metadata = Get-Content -LiteralPath $sessionFile.FullName -TotalCount 1 | ConvertFrom-Json
                if ([string]$metadata.payload.session_id -eq $threadId) {
                    $originator = [string]$metadata.payload.originator
                    break
                }
            } catch {
                continue
            }
        }
    }

    # Fail closed when the session source cannot be established. This prevents
    # Codex Desktop turns from leaking into the VS Code notification channel.
    if ($originator -ne $AllowedOriginator) {
        exit 0
    }
}

# The Codex desktop app and editor integrations can forward the same completion
# through the user-level notify hook more than once. Keep the hook idempotent so
# one completed turn produces one toast, even across separate PowerShell
# processes.
$turnId = [string]$event.'turn-id'
$now = [DateTimeOffset]::UtcNow
$retention = if ([string]::IsNullOrWhiteSpace($turnId)) {
    [TimeSpan]::FromSeconds(30)
} else {
    [TimeSpan]::FromDays(7)
}
$identity = if ([string]::IsNullOrWhiteSpace($turnId)) {
    $payload = [Text.Encoding]::UTF8.GetBytes(($event | ConvertTo-Json -Compress -Depth 20))
    $hasher = [Security.Cryptography.SHA256]::Create()
    try {
        'event:' + [Convert]::ToBase64String($hasher.ComputeHash($payload))
    } finally {
        $hasher.Dispose()
    }
} else {
    "turn:$threadId`:$turnId"
}

$stateDirectory = Join-Path ([Environment]::GetFolderPath('LocalApplicationData')) 'CodexWindowsNotify'
$statePath = Join-Path $stateDirectory 'seen-events.json'
$mutex = [Threading.Mutex]::new($false, 'Local\CodexWindowsNotifySeenEvents')
$lockTaken = $false
try {
    $lockTaken = $mutex.WaitOne([TimeSpan]::FromSeconds(5))
    if ($lockTaken) {
        New-Item -ItemType Directory -Force -Path $stateDirectory | Out-Null
        $seen = @()
        if (Test-Path -LiteralPath $statePath) {
            try {
                $seen = @((Get-Content -Raw -LiteralPath $statePath | ConvertFrom-Json))
            } catch {
                $seen = @()
            }
        }

        $duplicate = $seen | Where-Object {
            $_.id -eq $identity -and ($now - [DateTimeOffset]::Parse([string]$_.seenAt)) -lt $retention
        } | Select-Object -First 1
        if ($null -ne $duplicate) {
            exit 0
        }

        $cutoff = $now.Subtract([TimeSpan]::FromDays(7))
        $seen = @($seen | Where-Object {
            try { [DateTimeOffset]::Parse([string]$_.seenAt) -ge $cutoff } catch { $false }
        })
        $seen += [pscustomobject]@{ id = $identity; seenAt = $now.ToString('O') }
        @($seen | Select-Object -Last 200) | ConvertTo-Json | Set-Content -LiteralPath $statePath -Encoding UTF8
    }
} finally {
    if ($lockTaken) {
        $mutex.ReleaseMutex()
    }
    $mutex.Dispose()
}

$cwd = [string]$event.cwd
if ([string]::IsNullOrWhiteSpace($cwd)) {
    exit 0
}

$workspace = Split-Path -Leaf $cwd
$message = [string]$event.'last-assistant-message'
if ([string]::IsNullOrWhiteSpace($message)) {
    $message = 'Task complete'
}
if ($message.Length -gt 200) {
    $message = $message.Substring(0, 200)
}

$target = 'vscode://file/' + [Uri]::EscapeUriString($cwd.Replace('\', '/'))
$title = [Security.SecurityElement]::Escape("Codex complete - $workspace")
$body = [Security.SecurityElement]::Escape($message)
$launch = [Security.SecurityElement]::Escape($target)
$xml = @"
<toast activationType="protocol" launch="$launch">
  <visual>
    <binding template="ToastGeneric">
      <text>$title</text>
      <text>$body</text>
    </binding>
  </visual>
</toast>
"@

[Windows.UI.Notifications.ToastNotificationManager, Windows.UI.Notifications, ContentType = WindowsRuntime] | Out-Null
[Windows.UI.Notifications.ToastNotification, Windows.UI.Notifications, ContentType = WindowsRuntime] | Out-Null
[Windows.Data.Xml.Dom.XmlDocument, Windows.Data.Xml.Dom.XmlDocument, ContentType = WindowsRuntime] | Out-Null
$document = New-Object Windows.Data.Xml.Dom.XmlDocument
$document.LoadXml($xml)
$toast = [Windows.UI.Notifications.ToastNotification]::new($document)
[Windows.UI.Notifications.ToastNotificationManager]::CreateToastNotifier('Microsoft.VisualStudioCode').Show($toast)
