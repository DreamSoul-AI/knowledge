# Environment operations

Use the project's declared manager. A matching tool being installed is not a reason
to migrate an existing project. The examples below describe decisions; check the
installed tool's help and the actual project before executing them.

## Choose the operation

| Project evidence | Appropriate route |
| --- | --- |
| Existing interpreter and suitable dependencies | Run the requested command with that interpreter; no installation needed |
| pip/venv project | Bind pip to the confirmed interpreter; use the project's dependency constraints |
| uv project and uv.lock | Preserve its project/workspace and lock semantics; distinguish inspection from sync |
| Conda environment declaration | Target its explicit name/prefix and channels; account for native runtime activation |
| Poetry, PDM or another declared workflow | Follow that workflow, not a generic pip/uv replacement |
| Multiple conflicting declarations | Resolve which governs the target command before changing anything |

Do not create a pyproject.toml, lockfile or new environment merely to inspect a
repository. If setup is requested and needed, create only in the agreed project or
environment location, preserve existing environments and verify the target command.

## Minimal inspection
First name the target command or infer it from the requested task and project
instructions. If competing targets would require different environments or writes,
resolve that ambiguity before changing anything. Assess only the dependencies and
groups needed for that target, without treating unrelated findings as blockers.


Replace `python` with the confirmed interpreter or project launcher. In PowerShell,
invoke a quoted executable path with `&`.

```text
python -B -c "import sys,platform; print(sys.executable); print(sys.prefix); print(sys.base_prefix); print(platform.machine()); print(sys.version)"
python -B -m pip --version
python -B -m pip check
```

Use pip checks only when pip is available and relevant; missing pip is not a reason
to install it during diagnosis. `pip check` checks installed dependency metadata.
It does not establish native DLL availability, successful imports, GPU compatibility
or application correctness. Keep unrelated base-environment conflicts separate from
the requested command's requirements.

Inspect import origins and versions for relevant packages, then test suspect native
imports separately with a timeout. Preserve the failing launch context before
changing cwd, activation or import order. A metadata pass plus a crashing import
means the environment is not fully healthy. A successful workaround supports only
the tested cause and operation; it is not a verified permanent repair.

## Commands that may change state

- `uv run` may update the lockfile and environment before running. `--locked`
  protects against lockfile updates but still permits environment sync; `--frozen`
  skips freshness checks and is not a read-only guarantee. `uv sync` removes
  extraneous packages by default. For diagnosis prefer the existing interpreter;
  use `uv run --no-sync` only after confirming the existing environment, command
  and installed version. Do not bootstrap a missing interpreter or environment
- In mixed Conda/pip environments, inspect how packages were installed before
  proposing changes. Do not repeatedly run the two solvers to repair each other's
  results. If recovery needs a new environment, keep that a separate authorized
  operation and preserve the original
- `pip freeze` is an installed-package snapshot, not proof of a portable lock or
  complete environment. Preserve the project's real lockfile and distinguish
  direct requirements, resolved packages and non-Python runtime dependencies

## Fill only a demonstrated gap

| Evidence for the target | Smallest appropriate action |
| --- | --- |
| Target already works and required constraints hold | Reuse it; no install, upgrade or cleanup |
| Wrong interpreter, cwd or declared source entry | Use the correct existing launch context; do not install the package elsewhere |
| Required dependency missing in the confirmed environment | Within setup authorization, supply it through the project's manager and constraints; leave suitable installed packages alone |
| Only an optional feature or unrelated package is inconsistent | Report its scope; do not expand the target or repair it automatically |
| Lock mismatch, conflicting declarations or native-runtime failure | Preserve evidence and the environment; do not relax constraints, reinstall broadly or treat a workaround as a verified repair |

Before a mutation, explain the demonstrated gap, proposed action and expected
impact briefly in progress, not as an extra approval ritual. Execute within existing
authorization; ask only when scope or a consequential choice is unresolved. A
diagnosis-only request permits a proposal, not repair. Keep a pre-change baseline
of the packages/files actually at risk, compare after the operation, and re-run the
target. If unexpected packages or files change, stop further mutation and report
the difference; do not assume the install was transactional.

“Only missing” does not mean ignoring a lockfile's transitive dependencies or doing
an arbitrary manual install into a manager-owned environment. Use the authoritative
dependency groups and workflow; if that entails broader synchronization or removals,
explain the actual impact and respect the authorized scope. Do not install all
extras merely because they appear in project metadata.

## Handoff

Give the caller enough to continue without reconstructing the chat. Keep this
compact and adapt its shape to the task; no required JSON schema or new service.

- **Environment**: confirmed interpreter/environment and manager
- **Target**: task/entry point, cwd and a copyable command in the applicable shell
- **Change**: what actually changed and why it was sufficient, or explicitly none;
  keep an unexecuted proposal separate
- **Evidence**: observed result, relevant import/package location or concise log
  entry; distinguish package installation, import and target execution
- **Remaining scope**: unresolved blockers or features not tested; state whether the
  target ran successfully, diagnosis stopped before repair, or execution is blocked

For example, a working target needs “reused existing environment; no changes;
command X ran with result Y,” not a reinstall recommendation. A missing-dependency
case needs its required constraint, actual added package and target rerun, without
claiming optional features were verified. A diagnosis-only case gives the evidence
and smallest proposed action, explicitly unexecuted.

For handoff/recreation, reference the existing project declarations and lockfile
when needed, including their known platform/runtime limits. Do not substitute a
dump of every base-environment package or claim a snapshot is a portable lock.
An upstream skill can supply project, interpreter, requirements and target command
and receive these results without being forced to install, repair or publish.

## Sources

- Astral, [Locking and syncing](https://docs.astral.sh/uv/concepts/projects/sync/): automatic updates and exact sync semantics
- pip maintainers, [pip check](https://pip.pypa.io/en/stable/cli/pip_check/): installed dependency compatibility check
- pip maintainers, [pip freeze](https://pip.pypa.io/en/stable/cli/pip_freeze/): snapshot rather than lockfile semantics
- Conda contributors, [Managing environments](https://docs.conda.io/projects/conda/en/stable/user-guide/tasks/manage-environments.html#using-pip-in-an-environment): mixed-manager constraints
