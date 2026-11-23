# knowledge-update

Check or update adopted Knowledge skills and tools while preserving local customizations. It does not install every available skill or upgrade the whole environment.

```text
Use $knowledge-update to inspect this project's adopted skills and tools. Show differences without changing installations.
Use $knowledge-update to update adopted capabilities from their recorded sources, preserve customizations and verify the results.
```

Reuse the current mode, workspace, adoption records, pinned sources, exclusions and local changes. Ordinary text and existing records are sufficient; no mandatory configuration schema is required. Check mode leaves targets unchanged. Update mode follows the actual authorization.

Install the entire knowledge-update directory. It works independently and is also called by workspace-update by default. Reuse one round's scope and results; do not update the same real target twice. An unchanged adopted source needs no repeated copy or record rewrite.

Report source and installed versions, preserved changes, exclusions, conflicts/failures, verification and reload requirements. File updates, runner discovery and actual invocation are separate observations.

For a directory already selected and pinned, the optional [helper](../scripts/update_package.py) accepts `--current`, `--base`, `--incoming` and an external `--work-dir`. It previews by default; add `--apply` to update. It preserves extra local files and cleanly mergeable text changes, and reports overlaps without changing that package. Source selection, semantic decisions and runtime verification remain the Agent's responsibility.

Personal skills may use a confirmed username branch while common skills retain their own release sources. Pin each adopted item's commit: inherited common files on a personal branch are not a reason to downgrade them. Do not merge personal skills into common branches by default. A personal branch retains the repository's visibility, and a review-only draft is not an installed or released skill.

[Skill](../SKILL.md) · [Comparison helper](updating.md) · [中文](README_zh.md)
