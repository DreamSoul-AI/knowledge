# work-summary

Consolidate work from one or multiple conversations into completed deliverables, unfinished work, uncertainties and next steps. Use it independently for wrap-up, review or handoff, or as input to work-message.

## Usage

Keep the entire `work-summary` folder and its references together when installing.

```text
Use $work-summary to summarize the work and remaining issues. Propose the exact cross-conversation time window for confirmation first. Do not publish anything.
```

For each new global review, confirm start, end, time zone and source scope. Reuse that scope during the same review. Optional inputs include conversations, source material, supplementary context and applicable standards. Preserve the full factual picture, including work unsuitable for public sharing.

For sufficiently independent sources, use bounded parallel collection as described in [source collection](collecting.md). The main Agent checks coverage, corrections and evidence, then consolidates by deliverable. Reuse that inventory downstream rather than scanning again for each board; claim speed improvements only when overall elapsed time has been compared.

## Archive location

Save `工作总结 <date>.md` directly under `工作总结/<author's real name>/`, without a date subfolder. Use the corresponding document title `工作总结 <date>` in Feishu. Resolve the real name from the applicable `USER.md` or explicit instructions, rather than a GitHub handle, device account or message signature. Locate the local and cloud roots separately from existing configuration. A missing cloud destination does not block the local summary. See the [archive reference](archiving.md) for root selection, continuation and relative links.

```text
Use $work-summary to summarize these materials. Save under the real author name and local work-summary root in USER.md. Reuse this round's archive date, link the coverage evidence and message candidates, and do not upload yet.
```

Use the explicitly assigned work date for the filename; otherwise apply the user's confirmed date convention and task context rather than the generation date. Continue the same round in its existing file, including after midnight. Distinguish the assigned work date, actual coverage window and time zone, and latest update time. Preserve necessary cutoff context instead of presenting later results as already known then. The naming convention does not authorize moving historical material or creating cloud folders; check current objects and repair references before an authorized move or sync.

## Handoff to work-message

Before delivery, check the summary against the sources actually obtained. Preserve independently completed deliverables even when their project is unfinished. If the user identifies one omission, check comparable items while organizing the report by the task rather than the order of examples.

```text
Use $work-summary to prepare the complete summary, then use $work-message to calibrate what to share and prepare every selected board's text. Do not send it yet.
```

Pass ordinary text, a Markdown file or a readable link, retaining scope, cutoff, evidence and material links. The downstream skill reuses those facts without repeating collection. Summarizing alone does not authorize publishing, transcript uploads or edits to logs and trackers. work-message is optional and only needed for that downstream task.

Organize the full summary by the reader’s work structure: department → project when applicable, with completed results, unfinished work and uncertainty inside each project. Do not filter facts by downstream sharing choices. If message feedback changes a factual result or status, verify and update the corresponding summary fact; recipient wording, priority and sharing choices remain the message workflow’s responsibility.

When log updates are also requested, first locate the intended user’s actual log. Prefer the explicitly specified target; otherwise use that user’s USER entry and existing index, verify authorship, then read recent structure, state and writing conventions. Apply only authorized differences while preserving human content. Ordinary summaries do not require log scanning, and the Agent’s current user log is not an implicit target. Use project-progress-sync when task-table reconciliation or writeback is involved.
