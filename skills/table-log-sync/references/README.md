# Tracker and work-log reconciliation

Compare a project tracker and a work log while keeping their existing organization. Preview precise changes first, then write only the items the user confirms. Either direction can be used independently.

## Use

Install the entire `table-log-sync` directory, including `agents/` and `references/`, then ask:

```text
Use $table-log-sync to compare this tracker and work log. Start with a few records, keep the existing categories and hierarchy, and show the exact location, current value, proposed value, and source links. Do not write yet.
```

Provide links or readable local paths and the relevant people, dates, or records. The skill first uses resources already available in the conversation or project. Historical snapshots are labeled with their date rather than presented as current data.

## What a preview contains

Every item has a number, direction, exact log path or tracker record and field, current text, complete proposed text, original evidence with links, and the scope of the change. Existing matching content is left alone; ambiguous matches remain pending.

These examples are synthetic:

- **Tracker to log:** A tracker description includes a skill installation guide. At the existing path “Stage plan → Administration → Office → Tool guide,” propose changing “Tool guide” to “Tool guide (including skill installation),” retaining its position and checkbox.
- **Log to tracker:** An original log describes equipment inventory work and uniquely matches “Office equipment maintenance.” Show its record ID, existing description, proposed additional scope, and log link. Preserve progress unless there is independent evidence supporting a change.
- **Needs verification:** An expected date has passed without a confirmed outcome. Propose a verification note at the existing log entry; do not infer completion or invent a new date.

Ideas, current tasks, stage plans, future work, alignment notes, and daily history keep their existing roles. Repeated mentions across days are not automatically duplicates. Stage plans are not automatically scheduled for today.

## Confirmed writes

After reviewing the preview, say, for example:

```text
Apply items 1 and 3 from that preview. Leave the others pending.
```

Approving edits does not supply missing factual evidence of completion or dates. The skill re-reads the affected targets and evidence before making narrow edits. A relevant concurrent change requires an updated preview and confirmation for that item; unrelated new content is retained. Partial success and uncertain results are reported separately. Previously successful edits are not appended again.

Generated log text, copies, and readbacks are not independent evidence for updating the tracker. Daily checkmarks do not directly determine tracker percentages or actual completion dates. Unknown values and manually maintained parent progress are preserved.

Installing or publishing the skill does not authorize business-data writes. The skill does not create scheduled automation, publish messages, or archive conversation transcripts.
