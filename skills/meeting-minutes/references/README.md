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

## How it works
The workflow resolves calendar instances to actual meetings, obtains original Note or Minutes transcripts, and checks any manually attached meeting notes for corrections. It retains source identifiers and raw records, then reads the full text to organize topics, decisions, reported progress, actions, and unresolved questions. See [source retrieval](sources.md).

Unknown speakers, missing owners or dates, conditional actions, and retractions remain explicit. A calendar appointment does not prove attendance, and a matching quotation does not prove a summary's meaning. Existing outputs and human edits are compared before updating.

## Scope
A normal invocation performs one scan and organization pass. Installing the skill does not schedule recurring work, join or record meetings, publish minutes, or send notifications. Cloud updates and scheduled execution follow the user's explicit task scope.

Validation covers skill structure, links, and synthetic workflow walkthroughs. A successful real-calendar, recording-permission, and transcript end-to-end run has not been established for every environment.
