param([string]$Json)

$event = $Json | ConvertFrom-Json
if ($event.type -ne 'agent-turn-complete') {
    exit 0
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
