# Project Progress Sync

English | [简体中文](README_zh.md)

The optional [input example](inputs.example.yaml) accepts project sources, standards, aliases and a previous report. Compare only fields actually read in both snapshots. A field not read is distinct from a blank or zero. On a follow-up run, verify versions and changes across the original scope, reuse unchanged snapshots, reassess new evidence and do not treat old recommendations as accepted decisions.

Review work logs against a project task table before updating it. Supply log and table links, or local log files and table exports. Copy the entire `project-progress-sync` folder into the project's `.agents/skills/` or ask an agent to follow the [skill instructions](../SKILL.md) for a trial.

```text
Use $project-progress-sync to compare my work logs from the start of this
quarter through today with the project and task tables. Check the logs day by
day and cover all tasks I own in scope. Return read-only recommendations
for additions and progress changes with evidence and decisions to review.
```

The default range is the current quarter through the review date. You can specify a different range. If the base has several views, identify the underlying project and task tables or the scope available to you. You can provide task IDs, confirmed aliases, project mappings or a prior report. For an export, identify when it was saved and whether it includes a filtered view. Online access uses the current account and its existing permissions.

Suppose two log entries mention report export and diagnosing a slow export. If the project and deliverable identify the existing report export task, combine both entries into one progress suggestion with both sources. If another project has a plausible task with the same name, present both candidates when the evidence is ambiguous. A checked log item alone cannot establish that a deliverable is complete.

Check whether an existing project can host a proposed task. For a proposed project, state its independent objective, expected outcome and likely parent. For a field change, show the current and proposed values with evidence. If progress is clear and the percentage still needs judgment, describe the confirmed milestone and remaining work for the owner to review. Group decisions for discussion after delivering the initial read-only report. A rerun uses the current task table.

## Reviewable changes

For manual review, organize by workstream and connect the log item to its exact table record, reason for the change and remaining question. Distinguish previous values, proposed values and values actually written and read back. Keep already-applied updates separate from unchanged and unresolved items. State snapshot read times rather than implying a new live query. Log keywords are location hints, not delivery evidence; retain direct supporting references in the details.

Start with a short overview table ordered by the most useful next updates. Then show each record and field as current value → proposed wording or value → reason and source. Separate table changes from log follow-ups, and map earlier candidates to their existing records, consolidated candidates or unresolved questions. Put detailed explanations outside the overview table.

For example, an existing export-optimization task says that the slow stage has been identified. Later logs record a repair and a limited check. Propose appending the verified repair and remaining full-scale acceptance, rather than creating a duplicate task or setting progress to 100%. The quarterly log can retain full-scale acceptance as the next step while keeping the checked daily repair entry.

If an owner has already added that milestone and a new plan, preserve the human edit and mark the suggestion as already reflected. Return only the remaining difference. Append genuinely new evidence where needed and isolate conflicts for review; do not replace the whole description with an older draft. Check mode does not write. When synchronization is explicitly authorized, apply the confirmed changes against fresh targets and read back the result.

For a complete quarterly reconciliation, check every date from the first day of the selected quarter through the agreed cutoff. The current quarter can be reviewed through today. Report missing days and use quarter goals, meeting context and delivery evidence across the workstreams in scope. For a closed quarter, use stable record IDs and the pre-close snapshot to distinguish closeout values from delivered work and trace carryovers. Preserve both historical and current values, including the distinction between blank and explicit zero. When recommending a percentage, label the milestone-based estimate and state the remaining acceptance conditions.

## Check and synchronize

Ask to check a scope without writing, or explicitly authorize synchronization of confirmed changes to the corresponding tasks and logs. Reuse that scope and authorization; do not ask again for each accepted item. Isolate unresolved structural changes while continuing independent confirmed updates.

Read current sources and targets before writing. Locate records by stable identity and log positions, apply field or text-fragment changes, preserve unrelated human edits, and skip values already applied. If a field changed against the baseline, investigate or calibrate the conflict rather than overwriting it. Recheck before creating a task, query unknown write outcomes before retrying, then read back actual results and retain mappings for continuation.

For example, a confirmed 30% to 60% proposal must not replace a later human update to 80% and an acceptance plan. Investigate that conflict and preserve the plan. A completed onboarding task may add an onboarding result to a mixed recruiting/onboarding log item without checking off all recruiting work. Standards, personal formatting and platform permissions remain external inputs.

Local fixture writes do not prove live platform synchronization or atomic transactions. This skill is not tied to Feishu, a company or personal paths. It replaces the local log-table-reconciliation candidate; historical reports retain their original identity, without a duplicate discoverable skill.
