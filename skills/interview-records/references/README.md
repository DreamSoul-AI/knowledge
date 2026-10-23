# Calendar-driven interview records

Find completed interviews in a Feishu calendar, retrieve their actual records, and organize evidence by the correct role and interview round. Candidate statements, interviewer observations, artifacts, judgments, corrections, and unknowns remain distinct.

## Install
Install the complete `skills/interview-records` directory. The source-retrieval reference is bundled, so `meeting-minutes` is not a required local dependency.

Feishu access needs `lark-cli`, the relevant Lark calendar/meeting/document/shared skills, and the current user's permissions. Those service integrations are not bundled in this repository. Local records can be supplied directly. Project hiring rules and role-specific templates take precedence over a generic evaluation scheme.

## Use
```text
Use $interview-records to find today's completed interviews in my calendar, retrieve their original records, and organize each under the actual role and round.
```
A date range, candidate, role, calendar event, or source link can narrow the request. A scan without a date range starts with today's ended events in the user's timezone; DreamSoul defaults to Asia/Shanghai.

## Retrieval and matching
Calendar event instance → actual meeting → Note transcript, Minutes transcript, or explicitly attached interview notes. See [source retrieval](sources.md) and [record structure](record.md).

Cancelled interviews and training meetings are excluded. A direct source link can be used without inventing a meeting identifier. Ambiguous same-name sessions remain pending instead of being merged or matched to the nearest meeting. A missing transcript, an artifact still being generated, and a permission failure are reported separately.

## Output
Preserve raw sources and provenance, then prepare a role-appropriate record of the discussion, personal contribution, evidence, corrections, conflicting conditions, and follow-up questions. Missing information does not automatically become a low score. The default output does not assign a total score, rank candidates, or decide hiring.

Review privacy throughout summaries, tables, and derived lists. Keep only task-relevant candidate information in shared outputs and retain internal originals within their existing access scope.

## Limits
One invocation runs one retrieval and organization pass. It does not schedule recurring work, contact candidates, update rankings, publish records, or record interviews. Real-calendar and transcript retrieval have not been verified end to end in every target environment; structural validation and synthetic walkthroughs do not establish that result.
