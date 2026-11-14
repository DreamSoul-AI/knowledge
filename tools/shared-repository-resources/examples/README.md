# Research resource sharing example

Research and engineering repositories often use the same datasets and models, or reuse another project's experiment outputs, checkpoints and figures. Directory symlinks keep resources in explicit target directories while preserving each repository's access path and reducing duplicate storage.

The [research configuration](research.config.example.json) shares data and models between two repositories and keeps artifacts separate by project. To share a specific output, define its directory as a resource and map the relevant repository entries to it. Configuration determines which outputs are shared; the tool does not mix all results by default.

Paths and names are an optional convention. Supply actual local paths, keep personal configuration local, and document adopted entries and consumers in the project's REPO.md. Other directory resource types use the same mapping mechanism. See the [tool guide](../README.md).

The tool creates path relationships. It does not synchronize devices, move existing data or modify application input settings. Preview first, verify resources, permissions and consumers, then apply within the intended scope.
