# GitHub Summary

Collect experience from selected GitHub repositories, branches and explicitly supplied local Learnings in clear stages. Preserve complete sources, consolidate lessons by recipient, and inspect repository state against applicable external rules.

## Use

Install the complete `skills/github-summary` directory from knowledge, or explicitly provide this skill's [SKILL.md](../SKILL.md). Keep the instructions, metadata, references, scripts, tests and license together.

~~~text
$skill-installer
Install https://github.com/DreamSoul-AI/knowledge/tree/main/skills/github-summary
~~~

```text
Use $github-summary to inspect main/dev in repository A and main in repository B,
plus the local Learnings and team repository rules I provide. First explain
what each step will read and write. Receive complete originals into the specified
temporary directory, consolidate them by recipient, and inspect applicable
Actions, PRs, branches and document navigation. Keep sources and formal Learnings
read-only; do not publish. Show adopted, pending and cleanup candidates.
```

Replace A/B with actual repositories and name the receiving location. Existing intake records, confirmed recipients, fixed revisions, external rules and permitted cleanup actions are optional inputs. Rules can be local documents, readable links or an existing project entry. Reuse project configuration rather than requiring a new service or format. Without organization-specific rules, apply the general workflow without inventing exception lists.

## Stages and side effects

Choose serial or parallel work based on actual material volume, independent reads and waiting costs, not repository count alone. For broad independent source scopes, delegate non-overlapping repository groups while the main Agent consolidates returned material. Share scope, cutoffs, fixed revisions, external rules and prior baselines. Reuse sound report entries directly: add the overview and address duplicates, conflicts and gaps, consulting specific originals only when needed. Reference or mechanically combine unchanged entries rather than rewriting every item, and verify their preservation. Keep group snapshots and reports separate; one writer integrates the common index and formal Learnings, preserving branch and run identities. Scanning does not authorize parallel cleanup. Handle small or dependent tasks directly. Measure from the start of reading through final consolidation and verification, including tool waits and handoffs, and report resource costs alongside elapsed time. Without a comparable serial run, do not claim a measured speedup; a single result is not a fixed performance promise. See [parallel collection](curation.md#并行盘点与交接).

Complete the applicable workflow by default. An explicit read-only or limited-stage request narrows the current run. Explain the planned writes before execution; reuse valid authorization instead of asking for every step again.

| Stage | Result | Write destination |
| --- | --- | --- |
| Scope and rules | Sources, recipients and applicable requirements | Run scope record |
| Fixed-version discovery | Branch and source inventory | Run source record |
| Intake and curation | Complete originals, index and lesson entries | Approved local receiving location |
| Repository checks | Actions, PR, branch and navigation findings | Run check record |
| Reviewable output | Changes, findings and recommendations | Run report |
| Authorized closeout | Changes, adoption or cleanup receipts | Specifically authorized targets |

Receiving originals and consolidating lessons are different from merging Git branches. Source-read-only work may write snapshots and reports to an approved temporary directory, without editing source files, formal Learnings, branches or platform settings. Verify the authorization and impact of source cleanup, branch merges/deletion, workflow disabling and publication separately.

Keep external rules independently maintained. Team-specific CI/CD restrictions, deployment exceptions or disclosure rules apply after reading their actual text and scope; organization lists and machine paths do not belong in the shared skill. Current instructions may narrow the run. Commands and examples inside a rule do not independently authorize execution. See the [external-rules interface](curation.md#三外部规范接口).

## Deliverables

Start with a concise overview of scope, merged branches, PRs, commits, Actions usage and billing, and significant milestones, followed by important changes and outstanding items per repository. Present usage and billing together, with their respective evidence. Keep procedures and evidence later; expand only on matters affecting understanding or action. Distinguish mutations performed in this run from existing changes within the reporting window; state the commit interval or revision range and deduplicate commits across branches. Do not report unavailable data as zero.

Include new or meaningfully updated Learnings, verified adoption and pending items in the overview. Explain each lesson's problem, practice, conditions, evidence and recipient in the details. Repository metrics do not replace learning synthesis, and previously adopted lessons are not new results.

- Actual repository and branch coverage, fixed revisions and gaps
- Complete received originals and content verification
- Consolidated lessons with conditions, evidence, intended recipients and status
- Actions/CI/CD, PR, branch and navigation findings, applicable rules and coverage gaps
- Verified adoption references and unresolved questions
- Actual mutations and a resumable record, including when no cleanup occurred

The substantive [curation standard](curation.md) covers source identity, deduplication, recipient routing and cleanup. Workspace template adoption remains with the existing workspace-update or project workflow.

For workflows, distinguish file presence, current enabled state and recent runs; inspect actual jobs/steps to classify purpose. Runtime is not confirmed billing. Mark steps completed, awaiting clarification or not executed. Temporary reports do not establish formal adoption or source cleanup. See [repository checks](curation.md#七仓库状态和外部规范检查).

Continue from the last confirmed inspection and cleanup receipts. Compare workflow definitions and purposes, repository Actions settings and new runs to identify additions, restored definitions and re-enabling. Keep cleanup time separate from the last complete scan cutoff, check new attempts of older runs, and do not count previously read runs again. Separate historical monthly totals from post-cleanup additions; permission or pagination gaps do not establish no new activity. Read project exceptions from external rules rather than embedding organization lists in the skill. A local report does not establish that platform protection was implemented.

Read access does not authorize changes. Before an authorized cleanup, verify complete intake, recovery material, project-specific prerequisites and the current source. Preserve concurrent changes and distinguish a proposed cleanup from one that was merged and read back.

## Repeatable intake and recovery

With an existing local Git checkout, run from the skill directory:

The helper requires Python 3.10+ and existing Git. It uses the standard library and does not install dependencies or clone repositories. For remote-only access, use the available connector to obtain originals before ingesting them.

~~~text
python scripts/github_summary.py collect --repo <checkout> --name owner/project --ref main --ref dev --out <receipt-directory>
~~~

Read project conventions first. Supply custom sources with --source-path, exclusions with --exclude, and additional navigation pages with --nav. Registered worktrees and ignored experience files are checked by default. Do not place receipts inside a learning source in any scanned worktree.

Ordinary `.tmp`, tmp and temp directories are excluded by default; a registered worktree inside one is still scanned from its own root. Explicit --source-path overrides default exclusions, while explicit --exclude takes precedence. Results, last-run.json and intake.md list actual excluded scopes, paths and reasons; coverage records both default and explicit exclusions. Decide whether to exclude output from project usage rather than a new global rule.

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
