# Calendar meeting archive

Collect ended meetings hosted by or inviting the current user, retrieve their original records, prepare minutes for each actual meeting type, and upload them to a specified Feishu folder.

## Install
Install the complete `skills/calendar-meeting-archive` directory. The workflow requires an existing lark-cli setup, the relevant Lark calendar, meeting, document, drive and shared skills, and the current user's source and destination permissions. Service integrations are not bundled here.

This skill can run independently. When meeting-minutes is installed, reuse its content-organization workflow. Current project templates, archive rules and access restrictions take precedence.

## Use
```text
Use $calendar-meeting-archive to organize this week's ended meetings from my calendar and upload their minutes to this Feishu folder: <destination folder link>.
```
Specify dates, timezone and filters as needed. Without dates, scan today's ended events in the user's timezone. Without a destination, prepare local results and ask for the folder; do not upload to the drive root. Each person uses their own account and destination; access to an inviter's entire calendar is not required.

## Workflow
[Retrieve original sources](sources.md), read the complete available text, then [upload or update](upload.md). Retain raw evidence and provenance long term; by default only the requested minutes are uploaded. Apply project-specific rules to interviews and other specialized meetings, including restricted audiences.

Compare actual source and destination content on reruns. Skip unchanged results, retain human edits, and report conflicts. Return per-meeting status, actual result links and failures. Query timed-out import jobs before considering another creation.

## Automation
One invocation runs one pass. Recurring triggers require a separate user request. Installation does not start a schedule, record meetings, request sharing or send messages. Structural checks and isolated walkthroughs do not verify live source or destination permissions.
