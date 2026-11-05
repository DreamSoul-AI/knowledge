# CPU Memory Cleanup tool entry

**English** | [中文](README_zh.md)

[CPU Memory Cleanup](https://github.com/DreamSoul-AI/cpu-memory-cleanup) owns the Rust CLI distributed through its [latest stable Release](https://github.com/DreamSoul-AI/cpu-memory-cleanup/releases/latest); the historical Python package is not required.

Knowledge owns the [Skill](../../skills/cpu-memory-cleanup/SKILL.md), metadata and [installation guide](../../skills/cpu-memory-cleanup/references/README.md). All executable code, including release resolution, initialization and verification under scripts/agent-skill, belongs to the product repository.

Each new task defaults to the official latest stable release, verifies the selected asset SHA256 and installs or reuses an independent runtime. Explicit versions support reproducibility; a task keeps its selected executable. Discover the actual contract through --tool-info rather than pinning versions, builds or tool counts in the Skill. The host updates the Skill; product setup updates its runtime.

Real maintenance is Windows x64 working-set trimming, not CPU scheduling or a compression algorithm. Linux/macOS product packages are readonly and do not use this Windows initializer. Setup and updates do not sample memory, perform maintenance or enable auto rules. Agents need local file and shell access.

Product setup scripts are available at the official [source commit](https://github.com/DreamSoul-AI/cpu-memory-cleanup/tree/fab1230ed0e63d5afa010b80e240e10b5bd559b0/scripts/agent-skill). Use a Knowledge development ref that contains the Skill and ZIP. This iteration reinstalls from synchronized commits for local validation, without publishing a new Release; normal use requires no source checkout.

Normal Skill calls return stdout only and create no operation-history files or Markdown. Maintenance requires native stdout_only support and --no-record; updating instructions alone cannot change an old binary. Pass --output-dir only for an explicit save request; only saved results support replay. The new behavior is currently a local build and has not been released.
