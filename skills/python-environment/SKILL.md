---
name: python-environment
description: Inspect, prepare and troubleshoot Python project environments, including interpreter identity, dependency consistency and native-runtime failures. Use for environment setup or diagnosis; respect the project's manager and existing environment, and keep diagnosis separate from repair.
---

# Python 环境管理与排障 Python Environment Management

Inspect, prepare or diagnose the environment needed for a concrete project command.
The outcome is a verified interpreter and dependency context, or an evidence-based
diagnosis within the requested scope; diagnosis does not authorize repair. Read
repository instructions, Python version markers, dependency metadata, lockfiles
and existing environment declarations before choosing tools. Accept an optional
project path, interpreter/environment, applicable requirements and target command;
otherwise use the current project's actual declarations. Do not invent a lockfile
or adopt an optional tutorial's tooling as the project default.

## Workflow

1. Inspect the OS, available and declared interpreters, required version and task.
   Check `sys.executable`, `sys.prefix`, `sys.base_prefix` and relevant import
   locations. Matching version numbers or an activation prompt do not prove identity.
2. Reuse an existing environment that meets the target's requirements without
   reinstalling suitable dependencies. Keep a shared/base environment read-only unless
   changing it is explicitly requested. If a new environment is needed, follow the
   project's declared manager; use an isolated environment when no manager is declared.
   Identify the environment behind the actual shell, IDE, notebook or job command,
   not just the current terminal. Its working directory and activation may differ.
   Judge readiness against the target command and requested dependency groups.
   Separate blocking gaps from optional extras and unrelated environment findings;
   a working target does not require cleanup of every installed package.
3. Bind package operations to that interpreter with its full path and `-m pip`, or
   use the project's declared manager targeting the confirmed environment. Inspect
   requirements before executing them: they may invoke builds, editable installs,
   remote sources or indexes. Respect pinned versions, lock semantics and hashes;
   do not upgrade, relax a pin, disable hash checks or switch to global installation
   merely to bypass failure. A requirements file is not necessarily a complete lock.
   Check command side effects: `uv run` can lock and sync automatically, and
   `uv sync` can remove extraneous packages. A diagnosis-only task must not trigger
   these writes. Do not alternate Conda and pip repairs in a shared environment.
   Before a needed change, identify the blocking evidence, smallest sufficient
   action, affected environment/files and verification command. Carry it out when
   already authorized; otherwise report that concrete proposal without executing it.
   Leave suitable packages and optional extras alone. Preserve the project's full
   lock/sync contract rather than cherry-picking packages to bypass its constraints.
4. If an environment is missing or broken, distinguish interpreter failure from
   missing dependencies, native-library/runtime setup, project import paths and
   IDE/kernel selection. An explicit Python path selects the interpreter but may
   not supply a Conda/native library's runtime context. Preserve
   the existing directory and any user files; use a separate recovery location
   within the authorized scope, or ask before replacement. Do not clear or uninstall
   existing environments as routine diagnosis.
5. Run the requested import, command or relevant existing tests with that interpreter.
   Check dependency metadata when relevant (for example `python -m pip check`),
   but distinguish it from import and runtime validation. Probe suspect native
   imports in separate bounded processes so a crash or earlier import cannot hide
   the failure. Compare launch contexts only when needed to test a specific cause.
   Use project-declared source-layout/test entry points instead of installing a
   package just because an unconfigured shell cannot import it. Keep validation
   outputs separate from business data. On failure, report the actual layer and
   preserve existing files; installation is not transactional, so check what changed
   rather than assuming a failed install left the environment untouched.
6. Return a usable handoff: selected environment/manager, target and working
   directory, actual change (including none), copyable run command, observed result
   and remaining blockers or limits. Distinguish a successful run, diagnosis only
   and work blocked before execution. Keep proposed changes separate from actual
   changes; a small successful test does not establish every workflow or backend.

Do not change system Python, global PATH, execution policy, IDE defaults or download
large distributions without the corresponding scope. Never expose private index
credentials in commands or logs. Direct invocation can avoid shell activation for
supported commands; native extensions may still need the manager's runtime setup.
For manager-specific decisions and read-only checks, use the focused
[environment operations reference](references/environment-operations.md).
Consult the [English guide](references/README.md) or
[中文教程](references/README_zh.md) for examples and optional IDE/Conda background,
not as a universal setup requirement. Do not make project-specific paths or a single
environment manager prerequisites for other users.
