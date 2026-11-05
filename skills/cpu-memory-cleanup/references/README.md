# CPU Memory Cleanup Skill

## Install and initialize

Install the complete cpu-memory-cleanup folder in your host's skills location, keeping SKILL.md, agents and references. Codex supports `~/.codex/skills/`; other agents use their own loader. This package contains instructions, metadata and guides only, with no scripts or binaries.

All executable code is maintained in the [product repository](https://github.com/DreamSoul-AI/cpu-memory-cleanup). Normal users need no source checkout, Git or project docs. Obtain install-runtime.ps1 and its sibling release.ps1 from verified, published official source or release assets, and cache this installed copy under `%LOCALAPPDATA%/DreamSoul/CPU Memory Cleanup/agent-runtime/setup/`. Do not install the developer test harness. Product setup code is now on the official development branch; see the [source commit](https://github.com/DreamSoul-AI/cpu-memory-cleanup/tree/fab1230ed0e63d5afa010b80e240e10b5bd559b0/scripts/agent-skill). Install the Skill from a Knowledge ref that actually contains it. The stable Release does not yet provide the native no-record capability.

```powershell
$setup = Join-Path $env:LOCALAPPDATA 'DreamSoul/CPU Memory Cleanup/agent-runtime/setup/install-runtime.ps1'
$runtime = & $setup | ConvertFrom-Json
& $runtime.executable --tool memory_status
```

At the start of each task, setup resolves the [latest stable Release](https://github.com/DreamSoul-AI/cpu-memory-cleanup/releases/latest), selects its Windows x64 portable ZIP and verifies the asset SHA256 returned by GitHub. It installs only the Rust CLI and license materials, then queries the static tool catalog. No memory sampling, maintenance, service or auto rule runs during setup. No Rust, Python, Node, GUI or administrator installation is required. Installing a Skill has no universal executable hook; initialize during installation only if runtime preparation was requested, otherwise on first use.

## Updates and reproducibility

The default is `-Version latest`. New tasks check for the current stable release; each task keeps the executable selected at its start. Releases are installed side by side under LocalAppData, identified by their tag and archive hash prefix. Setup never replaces an older executable or terminates another task, and retains previous records.

For reproducibility, pass `-Version` with the requested stable version, with or without a v prefix. Drafts and prereleases are rejected. Offline setup accepts `-ReleaseMetadataPath` with a saved official GitHub Release API response and `-ArchivePath` with its corresponding official ZIP. Saved metadata reflects its retrieval time, not necessarily today's latest release. Use `-RuntimeRoot` for an isolated installation.

Reuse verifies the installation receipt and per-file hashes before execution. Changed files are preserved and rejected. Network errors do not silently select an older release or another download source. Use an already permitted PowerShell host: PowerShell 7 was tested; 5.1 execution remains unverified. Do not change execution policy or disable protection.

## Tool discovery and scope

Read the selected executable's `--tool-info` for its actual tools, parameters and platform capabilities; do not assume a fixed tool count. Record actual version, build and scope in results. Runtime updates belong to the product initializer; Skill updates use the host's skill-update mechanism. Update instructions when interfaces or capabilities change, rather than editing a hardcoded product version for every release.

Actual cleanup is Windows x64 working-set trimming, not CPU scheduling, process termination or a memory-compression algorithm. Linux/macOS do not use this Windows runtime. Agents need local file and command execution access; a remote cloud agent cannot control the host through this Skill. Maintenance follows the user's current scope and CLI confirmation contract. Do not run it concurrently, retry or widen its scope automatically, or enable auto rules. Installation and real readonly checks are distinct from maintenance acceptance.

## Ordinary calls do not persist operation history

Normal calls return their JSON through stdout for conversational reporting. Do not pass --output-dir, redirect JSON into a file, create report.json or timing.json, or generate Markdown. Normal reports have output_dir=null; a run ID identifies that response and does not imply a saved record. Installation integrity receipts are distinct from operation history.

Before maintenance, read --tool-info and require result_persistence.default=stdout_only and no_record_option=--no-record. Pass --no-record for normal global, process and batch maintenance. Older binaries lacking this capability must not perform this request; do not remove the flag, silently enable saving, or write and delete files to imitate no persistence.

Save only when the user explicitly requests it, using the specified --output-dir instead of --no-record. Only saved results support memory_result replay. Never enable saving merely to perform a readback. A user-specified, trusted local candidate executable may be inspected and used directly for that task; report its actual build and do not label it an official Release. The source is synchronized to a development branch, with no new Release yet. Previously published binaries retain their old behavior; identify source builds by their actual commit.

Normal users need no source repository or project docs. Do not change README, development logs, tests or Git state. Explicit product development or separate archival instructions introduce their own scoped duties.
