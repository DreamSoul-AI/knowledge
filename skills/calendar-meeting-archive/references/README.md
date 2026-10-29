# Calendar meeting archive

Collect ended meetings hosted by or inviting the current user, retrieve their original records, prepare minutes for each actual meeting type, and upload them to a specified Feishu folder.

## Install
Install the complete `skills/calendar-meeting-archive` directory. The workflow requires an existing lark-cli setup, the relevant Lark calendar, meeting, document, drive and shared skills, and the current user's source and destination permissions. Service integrations are not bundled here.

This skill can run independently. Pass original material, supplements and applicable rules to meeting-minutes when installed or explicitly selected. Use document-sync for delivery when available or selected. Report missing explicitly selected dependencies rather than silently switching versions. Current project templates, archive rules and access restrictions take precedence.

## Use
```text
Use $calendar-meeting-archive to organize this week's ended meetings from my calendar and upload their minutes to this Feishu folder: <destination folder link>.
```
Specify dates, timezone and filters as needed. Without dates, scan today's ended events in the user's timezone. Without a destination, prepare local results and ask for the folder; do not upload to the drive root. Each person uses their own account and destination; access to an inviter's entire calendar is not required.

## Project placement
Provide an external [grouping and requirements profile](placement.md), or supply natural-language additions for confirmed aliases, archive groups, supplements and applicable standards. Existing series-only profiles remain valid. An ad-hoc meeting may have no series and use an explicitly established shared group. Resolve each occurrence’s identity, group, location and applicable rules before preparing content. Unknown ownership or conflicting requirements remain pending only for affected meetings. The profile is read by the agent, not an executable parser; it neither authorizes uploads nor enables scheduling.

For example, combine two confirmed aliases into one series, apply the regular-meeting standard only to its scope, and place confirmed external ad-hoc discussions in a specified shared group. Keep run-specific additions in the current run record rather than silently making permanent rules. Group changes do not change occurrence identity, authorize migrations or regenerate existing minutes.

## Workflow
[Retrieve original sources](sources.md), read the complete available text, then [upload or update](upload.md). Retain raw evidence and provenance long term; by default only the requested minutes are uploaded. Apply project-specific rules to interviews and other specialized meetings, including restricted audiences.

Compare actual source and destination content on reruns. Skip unchanged results, retain human edits, and report conflicts. Return per-meeting status, actual result links and failures. Query timed-out import jobs before considering another creation.

## Automation
One invocation runs one pass. Recurring triggers require a separate user request. Installation does not start a schedule, record meetings, request sharing or send messages. Structural checks and isolated walkthroughs do not verify live source or destination permissions.

## Local-only runs
Supply existing transcripts and source responses with execution.mode: local_only to prepare the local archive first. When platform reads are prohibited, do not fetch missing material. A local-only run does not require a remote folder or call a transfer workflow. Compare actual local material and artifacts on reruns and preserve human edits.

A meeting series is separate from a project. Historical titles can identify one confirmed series, and one occurrence may discuss several projects. Retain one source record per actual meeting, with project associations by topic. Cloud delivery requires a separately established scope.
