# CPU Memory Cleanup tool entry

**English** | [中文](README_zh.md)

This directory is a documentation entry, with no cleanup implementation, installer or automatic task. The package, CLI and desktop live in [cpu-memory-cleanup](https://github.com/DreamSoul-AI/cpu-memory-cleanup).

See the pinned [integration guide](https://github.com/DreamSoul-AI/cpu-memory-cleanup/blob/a539905f9bf1d43569fb6473fa7b0ff25963223c/docs/%E5%B7%A5%E5%85%B7%E6%8E%A5%E5%85%A5%20Tool%20Integration%20CPU%20%E5%86%85%E5%AD%98%E6%B8%85%E7%90%86.md) for installation, five tools, host authorization, target identity and offline replay. The guide is pinned to a539905 and the feature installation to9c7d725 from PR #11. The published v0.2.0 does not include the new single-process tools.

Consumers are local Python programs and agent hosts able to run local subprocesses. Use the package or CLI. This is not an MCP server or an installable SKILL directory. Preparing an environment and performing an operation are explicit actions, not side effects of reading this guide.

When real sampling and cleanup are prohibited, use only the static tool catalog, offline replay or fake-interface validation. Target discovery also reads real processes and is not a default setup check. Product code and detailed tool contracts remain in the product repository.
