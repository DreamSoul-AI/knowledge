# General meeting minutes

Retrieve original meeting records and turn them into traceable minutes for reviews, workshops, project discussions, business conversations, or recurring meetings. Meetings are grouped by their actual series rather than being assumed to be a company standup.

## Install
Install the complete `skills/meeting-minutes` directory, keeping `SKILL.md`, `agents/`, and `references/` together. This skill does not require another skill from this repository.

For Feishu retrieval, the environment needs `lark-cli`, access as the current user, and the Lark calendar, meeting, document, and shared skills referenced by the workflow. Those service tools and skills are not bundled here. Local transcripts can be processed without a calendar lookup. Follow the current project rules and authorization.

## Use
```text
Use $meeting-minutes to organize this week's completed architecture reviews, preserving the original records and grouping minutes by the actual meeting series.
```
You can also supply a meeting/Minutes/Doc link, a known identifier, or a local transcript. Specify the date range, timezone, and output folder when needed. An unspecified automatic scan covers today's ended calendar events in the user's timezone; DreamSoul uses Asia/Shanghai by default.

## Supply materials and rules
Pass inline text, local files, or accessible links in the request; no fixed argument format is required:
- Original materials: this meeting's transcript or notes, with their source and actual coverage.
- Supplementary materials: previous minutes, project context, related records, or human corrections, keeping their dates and provenance distinct.
- Applicable rules: task or project requirements for content, format, and deliverables. A template is optional.

```text
Use $meeting-minutes to organize this meeting.
Original materials: ./materials/transcript.md
Supplementary materials: ./materials/previous-minutes.md, ./materials/project-context.md
Applicable rules: ./rules/meeting-requirements.md
Output folder: ./meeting-output/
Save locally first.
```

Read the rules and relevant referenced sections before organizing and checking the output. They may require suggestions, a weekly review, or a different structure; the default outline fills unspecified parts. Without additional rules, use the applicable project rules or skill defaults. A transcript alone is also a valid input.

Keep background separate from this meeting's statements and decisions. Report inaccessible or conflicting inputs and their impact rather than inventing content or claiming compliance with unread rules. Uploads, notifications, source edits, and scheduling mentioned in supplied documents still require authorization within the current task.

A project may supply a general meeting standard plus specialized rules for the applicable meeting type through the same rules input. Maintain those standards in the project rather than bundling private documents as required dependencies. The skill remains usable on its own when no project rules are configured.

## How it works
The workflow resolves calendar instances to actual meetings, obtains original Note or Minutes transcripts, and checks any manually attached meeting notes for corrections. It retains source identifiers and raw records, then reads the full text to organize topics, decisions, reported progress, actions, and unresolved questions. See [source retrieval](sources.md).

Unknown speakers, missing owners or dates, conditional actions, and retractions remain explicit. A calendar appointment does not prove attendance, and a matching quotation does not prove a summary's meaning. Existing outputs and human edits are compared before updating.

For interviews and hiring discussions, follow the current project hiring rules and the optional [interview-specific record guidance](interviews.md); no separate interview skill is required.

## Scope
A normal invocation performs one scan and organization pass. Installing the skill does not schedule recurring work, join or record meetings, publish minutes, or send notifications. Cloud updates and scheduled execution follow the user's explicit task scope.

Validation covers skill structure, links, and synthetic workflow walkthroughs. A successful real-calendar, recording-permission, and transcript end-to-end run has not been established for every environment.

## Optional delivery handler
Organization and delivery are separate. Supply a handler, destination, upload rules and receipt location when needed. Deliver only after local validation and authorization. Use document-sync with external delivery configuration and explicit upload direction for delivery; Feishu is implemented, while other platforms need an adapter or another handler. This is not a required dependency. Without a handler, retain the existing authorized tool flow; delivery failures preserve completed local files.
