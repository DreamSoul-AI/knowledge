# GitHub Summary

Collect experience from selected GitHub repositories, branches and explicitly supplied local Learnings. Preserve complete sources, merge overlapping lessons by their intended recipient, and distinguish pending candidates from adopted work.

## Use

Install the complete `skills/github-summary` directory from knowledge, or explicitly provide this skill's [SKILL.md](../SKILL.md). Keep the instructions, metadata, references, scripts, tests and license together.

~~~text
$skill-installer
Install https://github.com/DreamSoul-AI/knowledge/tree/main/skills/github-summary
~~~

```text
Use $github-summary to inspect main/dev in repository A and main in repository B,
plus the local Learnings I provide. Receive complete originals into this local
workspace, consolidate them by intended recipient, and list adopted, pending
and cleanup candidates. Read remote sources only; do not modify or publish them.
```

Replace A/B with actual repositories and name the receiving location. Existing intake records, confirmed recipients, fixed revisions and permitted cleanup actions are optional inputs. Reuse applicable project configuration rather than requiring a new service or configuration format.

## Deliverables

- Actual repository and branch coverage, fixed revisions and gaps
- Complete received originals and content verification
- Consolidated lessons with conditions, evidence, intended recipients and status
- Verified adoption references and unresolved questions
- Actual mutations and a resumable record, including when no cleanup occurred

The substantive [curation standard](curation.md) covers source identity, deduplication, recipient routing and cleanup. Workspace template adoption remains with the existing workspace-update or project workflow.

Read access does not authorize changes. Before an authorized cleanup, verify complete intake, recovery material, project-specific prerequisites and the current source. Preserve concurrent changes and distinguish a proposed cleanup from one that was merged and read back.

## Repeatable intake and recovery

With an existing local Git checkout, run from the skill directory:

The helper requires Python 3.10+ and existing Git. It uses the standard library and does not install dependencies or clone repositories. For remote-only access, use the available connector to obtain originals before ingesting them.

~~~text
python scripts/github_summary.py collect --repo <checkout> --name owner/project --ref main --ref dev --out <receipt-directory>
~~~

Read project conventions first. Supply custom sources with --source-path, exclusions with --exclude, and additional navigation pages with --nav. Registered worktrees and ignored experience files are checked by default. Do not place receipts inside a learning source in any scanned worktree.

Reruns reuse unchanged source identities. Review changes, errors, exclusions and navigation in last-run.json before making item-level judgments. objects/ preserves complete original bytes; index.json preserves repository, branch, fixed commit, worktree identity and history. These receipts can contain private originals and are not distributed with the skill.

A remote manifest that has not covered a complete source scope returns coverage_complete=false. Limited intake can succeed without establishing branch-wide coverage. Ambiguous path migrations remain independent sources for Agent review.

For remote-only inputs, use the available connector/API to resolve fixed commits and save complete originals, then ingest their verified manifest. restore rehydrates original bytes to a new directory, refusing distinct existing content and redirected destinations. check-cleanup never deletes anything: unchanged bytes alone do not establish adoption, durable recovery or authorization. Detailed arguments and the manifest shape are in [the curation standard](curation.md#六脚本与接续).

The helper does not summarize, choose recipients or evaluate the meaning of lessons. The Agent reviews each problem, practice, condition and supporting evidence against existing intake. A navigation finding is not automatic permission to open a repair task.

## Validation and limits

tests/test_intake.py exercises real temporary Git repositories: component-based discovery, explicit source paths, ignored and other-worktree originals, byte-exact restoration, stable reruns, isolated content changes, path migration, branch identity, navigation findings and changed-source cleanup protection. It also checks no-write rejection of Windows Junction restore escapes and receipts placed inside another scanned worktree's sources.

~~~text
python -B tests/test_intake.py -v
~~~

After installation, compare all distributed files against the adopted fixed commit and run the checks from the installed directory. Explicit use of the skill does not establish automatic discovery or selection by the desktop app. These tests do not establish production cleanup, concurrent writers, other devices or untested platform behavior.
