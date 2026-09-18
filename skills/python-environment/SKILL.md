---
name: python-environment
description: Inspect, create, configure, and troubleshoot isolated Python development environments. Use for interpreter selection, dependency installation, IDE integration, or environment conflicts; do not impose Conda or a specific IDE when the project already defines another workflow.
---

# Python Environment

Treat existing project files as authoritative. Inspect Python version markers,
lockfiles, dependency manifests, environment directories, and repository
instructions before selecting an environment manager.

## Workflow

1. Identify the operating system, available interpreters, and the project's required version.
2. Reuse a healthy project environment; otherwise choose the project's declared manager.
3. Keep dependencies isolated and avoid global installation unless explicitly requested.
4. Install from the lockfile or project metadata when available.
5. Verify interpreter identity, package import, and the requested command or tests.
6. Diagnose PATH, shell activation, IDE interpreter, and package-manager mismatches separately.

Ask before downloading large distributions or replacing an existing environment.
Never expose private index credentials in commands or logs. Consult the
[Python guide](references/README.md) for optional PyCharm and Conda
background, not as a universal setup requirement.
