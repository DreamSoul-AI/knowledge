[CmdletBinding()]
param(
    [switch]$Force,
    [switch]$Uninstall,
    [switch]$SkipTest
)

$ErrorActionPreference = 'Stop'

$codexHome = if ($env:CODEX_HOME) {
    $env:CODEX_HOME
} else {
    Join-Path $env:USERPROFILE '.codex'
}
$configPath = Join-Path $codexHome 'config.toml'
$scriptDirectory = Join-Path $codexHome 'scripts'
$installedScript = Join-Path $scriptDirectory 'codex-windows-notify.ps1'
$sourceScript = Join-Path $PSScriptRoot 'notify-windows.ps1'
$tomlPath = $installedScript.Replace('\', '\\').Replace('"', '\"')
$notifySetting = 'notify = ["powershell.exe", "-NoProfile", "-ExecutionPolicy", "Bypass", "-File", "' + $tomlPath + '"]'
$notifyPattern = '(?ms)^notify[ \t]*=[ \t]*\[(?:[^\]"'']|"(?:\\.|[^"\\])*"|''(?:''''|[^''])*'')*\][ \t]*(?:#.*)?\r?$'

New-Item -ItemType Directory -Force -Path $codexHome | Out-Null
$config = if (Test-Path -LiteralPath $configPath) {
    Get-Content -Raw -LiteralPath $configPath
} else {
    ''
}
$match = [regex]::Match($config, $notifyPattern)

if ($Uninstall) {
    if (-not $match.Success -or -not $match.Value.Contains($tomlPath)) {
        Write-Host 'Codex Windows Notify is not installed by this script.'
        exit 0
    }

    $backupPath = "$configPath.codex-windows-notify.bak"
    Copy-Item -LiteralPath $configPath -Destination $backupPath -Force
    $updated = ($config.Remove($match.Index, $match.Length)).TrimEnd() + [Environment]::NewLine
    Set-Content -LiteralPath $configPath -Value $updated -Encoding UTF8
    Remove-Item -LiteralPath $installedScript -Force -ErrorAction SilentlyContinue
    Write-Host "Uninstalled. Config backup: $backupPath"
    exit 0
}

if (-not (Test-Path -LiteralPath $sourceScript)) {
    throw "Missing source script: $sourceScript"
}

if ($match.Success -and $match.Value.Trim() -ne $notifySetting) {
    if (-not $Force) {
        throw "A different Codex notify command already exists in $configPath. Re-run with -Force to back it up and replace it."
    }
    $backupPath = "$configPath.codex-windows-notify.bak"
    if (Test-Path -LiteralPath $configPath) {
        Copy-Item -LiteralPath $configPath -Destination $backupPath -Force
    }
    $config = $config.Remove($match.Index, $match.Length).Insert($match.Index, $notifySetting)
} elseif (-not $match.Success) {
    if ($config -match '(?m)^notify[ \t]*=') {
        throw "The existing notify setting in $configPath could not be edited safely. Update it manually using the README."
    }
    if ($config.Length -gt 0 -and -not $config.EndsWith("`n")) {
        $config += [Environment]::NewLine
    }
    if ($config.Length -gt 0) {
        $config += [Environment]::NewLine
    }
    $config += $notifySetting + [Environment]::NewLine
}

New-Item -ItemType Directory -Force -Path $scriptDirectory | Out-Null
Copy-Item -LiteralPath $sourceScript -Destination $installedScript -Force
Set-Content -LiteralPath $configPath -Value $config.TrimEnd() -Encoding UTF8

Write-Host "Installed: $installedScript"
Write-Host "Configured: $configPath"
Write-Host 'Restart VS Code or start a new Codex session before relying on the hook.'

if (-not $SkipTest) {
    $testEvent = @{
        type = 'agent-turn-complete'
        cwd = $PSScriptRoot
        'last-assistant-message' = 'Installation succeeded. Click to open this repository in VS Code.'
    } | ConvertTo-Json -Compress
    & $installedScript $testEvent
}
