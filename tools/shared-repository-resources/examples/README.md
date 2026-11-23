# Research resource sharing example

Research and engineering repositories often use the same datasets and models, or reuse another project's experiment outputs, checkpoints and figures. Directory symlinks keep resources in explicit target directories while preserving each repository's access path and reducing duplicate storage.

The [research configuration](research.config.example.json) shares data and models between two repositories and keeps artifacts separate by project. To share a specific output, define its directory as a resource and map the relevant repository entries to it. Configuration determines which outputs are shared; the tool does not mix all results by default.

Actual resources in this example live under `shared/data/`, `shared/models/` and `shared/artifacts/<project-name>/`. Repository entry points are `.shared/data`, `.shared/models` and `.shared/artifacts`. `.shared/` itself is an ordinary directory; its resource entries are symlinks. Organize data by dataset and models by model name, without a research-topic grouping layer.

Paths and names are an optional convention. Supply actual local paths, keep personal configuration local, and document adopted entries and consumers in the project's REPO.md. Other directory resource types use the same mapping mechanism. See the [tool guide](../README.md).

The tool creates path relationships. It does not synchronize devices, move existing data or modify application input settings. Preview first, verify resources, permissions and consumers, then apply within the intended scope.

Legacy configurations remain supported. To adopt the new naming, the project or workspace maintenance process renames the relevant shared entries from `.local/` to `.shared/` and updates configuration, consumers and Git ignore rules. Resource targets and unrelated uses of `.local/` stay unchanged. See [Existing entries](../README.md#existing-entries).
