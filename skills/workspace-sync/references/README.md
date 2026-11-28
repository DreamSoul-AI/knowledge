# workspace-sync

Install the complete `skills/workspace-sync/` folder into your runner's skill directory, including metadata and references. Compare an existing installation and preserve local customizations.

Ask: `Use $workspace-sync to update my workspace.` By default, update the identified local workspace's rules, templates and adopted capabilities, preserve project and personal settings, and read back the result. Inspection requests produce a preview without target writes.

Optionally ask to also update organization repositories, or select `github_distribution.enabled: true` in runtime configuration. Resolve organization, repositories, target branches and exclusions from existing configuration and adoption records without asking the user to repeat a known list. A list of repositories alone does not select remote distribution. Reading a GitHub source is distinct from writing to GitHub; this is a configuration field, not a CLI flag.

The optional remote path retains the existing commit, PR, checks, merge and readback workflow. Cloud destinations and download packages enter only when separately included in this round's delivery scope. Briefly surface the option when the maintainer's role and current goal make it relevant; continue the default local work without a mandatory approval question.

This skill owns Workspace templates and delegates adopted skills and tools to [knowledge-update](../../knowledge-update/SKILL.md) once per round, sharing scope, pinned sources and authorization. Provide the complete knowledge-update directory or its readable entry point when installing this skill; this does not install every Knowledge skill. Both skills keep targets unchanged in check mode. Update mode reuses adoption records and results for targets already handled in the same round. No weekly schedule is created by this workflow.

[Skill](../SKILL.md) · [中文](README_zh.md)

## Optional private Git

The default pulls and merges local templates/rules and calls knowledge-update once. Private Git is off unless explicitly selected with private_git.enabled, repo, branch, allowlist and required dependencies. See [private Git](private-git.md) and [configuration](config.example.yaml). Organization distribution remains independently selected by github_distribution.enabled. Check mode writes to neither remote path.

knowledge-update retains its name and does not call back.
