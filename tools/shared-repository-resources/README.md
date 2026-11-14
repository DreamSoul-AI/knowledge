# Shared Repository Resources

English | [简体中文](README_zh.md)

Let multiple repositories reuse selected resources through directory symlinks while keeping their own access paths. Resources remain in explicit target directories, reducing duplicate storage.

Resource names, locations, repository entry points and the adopted subset are configurable in JSON for different project layouts and directory resource types.

## Research and engineering example

Research repositories can share datasets (data), models and weights (models), and selected run outputs (artifacts). Outputs may be isolated per project or explicitly shared when reuse is intended. The [research example guide](examples/README.md) and [configuration](examples/research.config.example.json) show this convention. Other scenarios can choose different resources and mappings.

## Configuration

For research projects, start with the [research example](examples/research.config.example.json); for other layouts, see [config.example.json](config.example.json). Supply actual paths. Relative paths resolve against the configuration file's directory, independently of the script location or current working directory. Verify paths and resource availability on each device.

- `version`: currently `1`
- `resources`: user-defined keys with a directory `path` and optional boolean `create`, defaulting to `false`
- `repositories`: explicit keys with a Git repository root `path` and a `links` object mapping repository-relative entry paths to resource keys
- Link paths use forward slashes. Repositories may choose different entries and different resource subsets
- `create: true` permits creating a missing resource directory. It does not permit replacing a broken existing link or silently recreating lost linked data

Shared and per-project resources are explicit mappings; targets are not derived from repository folder names. Keep actual personal paths in local configuration. Preview does not create the sample repositories or directories.

## Usage

Requires Python 3.10+, Git and permission for the current process to create directory symlinks. Windows permission or Developer Mode must be available in the actual environment. The tool does not elevate privileges or fall back to copies or junctions.

From this directory, preview first:

```text
python link_shared.py --config <actual-config.json>
```

Review entries, targets and scope, then explicitly apply:

```text
python link_shared.py --config <actual-config.json> --apply
```

To select a subset:

```text
python link_shared.py --config <actual-config.json> --repositories app exporter --apply
```

Preview is read-only. Apply creates explicitly permitted resource directories and directory symlinks, then appends precise Git ignore entries where needed, preserving existing content. Output is UTF-8 JSON; exit code `0` means the requested operation completed, and `1` indicates a validation or execution failure.

## Reruns and conflicts

All mappings are preflighted before writes. Occupied files/directories, wrong-target or broken links, tracked content, path escapes, overlapping mounts, and redirected entry parents, including Windows junctions, are rejected with specific errors.

Correct links are reused and their actual targets and Git ignore behavior are checked. An interrupted apply may leave partial progress. `completed` reports verified entries; reruns inspect actual filesystem state and resume without deleting or replacing old entries. Keep configuration and paths stable during execution; concurrent mutation is not supported.

Only directory resources are supported. The tool does not copy, move, delete or upload content, or edit consumer settings. Verify that each project actually uses the configured entry. Symlinks do not implement cross-device transfer, runtime compatibility or multi-writer coordination.

## Research example and tests

[research.config.example.json](examples/research.config.example.json) shows shared datasets and weights with separate project outputs. Those names are an optional profile, not built-in resource types.

```text
python -B tests/test_link_shared.py
```

Tests create only temporary Git repositories and synthetic resources. Optionally set `SHARED_RESOURCES_TEST_ROOT` for scratch storage and `SHARED_RESOURCES_TEST_REPORT` for per-case JSON results. The Windows process must be able to create symlinks. Two Windows layouts, script relocation, reruns, conflicts and interrupted execution have been tested. Other operating systems remain unverified.
