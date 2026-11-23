# workspace-update

Install the complete `skills/workspace-update/` folder into your runner's skill directory, including metadata and references. Compare an existing installation and preserve local customizations.

Ask: `Use $workspace-update to complete this release across the adopted projects and distribution destinations, preserve project and personal settings, and verify each result.`

Resolve the scope and exclusions from adoption records and release configuration. A single-project update stays scoped to that project; a release-wide update follows through on listed repositories, local copies, cloud documents and download packages using available tools and existing authorization. Inspection requests produce a preview.

This skill owns Workspace templates and delegates adopted skills and tools to [knowledge-update](../../knowledge-update/SKILL.md) once per round, sharing scope, pinned sources and authorization. Provide the complete knowledge-update directory or its readable entry point when installing this skill; this does not install every Knowledge skill. Both skills keep targets unchanged in check mode. Update mode reuses adoption records and results for targets already handled in the same round. No weekly schedule is created by this workflow.

[Skill](../SKILL.md) · [中文](README_zh.md)
