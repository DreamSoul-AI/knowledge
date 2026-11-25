# meeting-background

Prepare an author's recurring meeting background from their personal work log. Produce an opening summary, previous-week progress and the coming week's plan. This is meeting preparation, not meeting minutes, log cleanup or project-table reconciliation.

# 1. Configuration

Read the author's real name and confirmed section aliases, personal-log entry, timezone, requested reporting period, meeting-series or current-document entry, naming preferences and document standard from `USER.md` or the current request. Existing prose or project configuration is sufficient. A new schema is not required.

Historical links and dates are examples, never permanent targets. Verify the current meeting document's date and author section before any write. If a period crosses a month boundary, read both months. When an essential target remains ambiguous, deliver the useful draft and ask only about that ambiguity.

# 2. Use

- Draft: “Use $meeting-background to prepare my background for the specified meeting. Read the previous week's daily entries and latest TODO list. Show the complete draft without uploading it.”
- Update: “Update the confirmed current document's author section, preserve the other sections, read it back and report the real link.”
- Continue: “Continue the same week's background with these additional results.” Read the current target, merge the change and avoid appending another copy. For a new week, locate that week's document again.

Daily checkmarks show work done or advanced that day. They do not establish completion of the entire project. Continuing work can remain in a weekly plan even after a daily checkbox was checked. Merge repeated work while retaining concrete independent results and the author's established terminology.

# 3. Output and update boundary

Use an H1 for the author's name, followed by H2 headings for the summary, previous week (date range), and current week (plan start). Give each actual department or category one summary paragraph, starting with a bold category name and punctuation outside the emphasis. Use inline `1)`, `2)` points with plain-text labels, without italics or separate numbered lists. Put internal research under R&D. Omit external collaboration from all three sections unless requested for this run. The weekly sections use compact nested bullet lists without blank lines between parent and child items or adjacent items. Preserve paragraph boundaries without creating empty Feishu text blocks.

Use plans valid at the meeting-preparation point. Do not backfill later TODO entries into a Monday replay. Keep source checks, trial notes and unresolved evidence outside the author's meeting prose, without appending historical paused-work lists.

Before an authorized update, read the entire author section through the next same-level or higher-level heading, including trailing lists. Compare with the current draft and preserve meaningful manual edits and resources. Replace only the authorized author range. Read back the entire range to detect old summaries or plans left behind, and verify neighboring sections remain unchanged.

Use the available `lark-doc` workflow for Feishu operations and consult its current CLI documentation. Drafting does not imply upload permission. A failed or unknown write is not success: inspect the target before retrying.

Maintain personal editions in the owner's registered personal branch. Install the complete skill package from the selected recorded source when separately authorized. Pushing the skill neither installs it nor updates a real meeting document. Check the actual reporting period and materials when using it; no schedule is created automatically.
