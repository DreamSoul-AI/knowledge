# Daily Meeting Summary

English | [简体中文](README_zh.md)

Archive source records and prepare summaries for ended meetings, reusing existing artifacts and delivering them within the confirmed scope. Extracted from an existing daily meeting summary task and maintained as a reusable first version. Actual validation coverage is documented below.

## Files

- [Prompt](prompt.md) defines the objective, dependencies, sequence and reporting requirements for one run
- [Example configuration](config.example.yaml) exposes scheduling, scanning, rule sources, destinations, artifacts and execution scope

The configuration is read by an agent. There is currently no configuration parser or installer. Its fields are conventions for this task, which the agent resolves into actual skill inputs. Review placeholders and required empty fields before deployment.

## Dependencies

1. [Calendar Meeting Archive](../../skills/calendar-meeting-archive/SKILL.md) coordinates sources, responsibility, existing drafts, grouping and incremental recovery
2. [Meeting Minutes](../../skills/meeting-minutes/SKILL.md) receives original and supplementary material, applicable standards and existing drafts when content work is needed
3. [Document Sync](../../skills/document-sync/SKILL.md) receives explicit artifacts and per-artifact destinations for authorized uploads

The deployment supplies installed skill paths and versions. Calendar, meeting and document access also require platform tools and permissions for the actual user. Follow each skill's runtime requirements.

## Configuration and deployment

The reference schedule is daily at `00:00` in `Asia/Shanghai`, following the source task. Copying these files leaves the deployed schedule unchanged. The example has deployment enabled set to `false` and cloud writes set to `false`; the operator supplies the confirmed scope before deployment.

Paths resolve against `project_root`. The operator selects the project root, actual configuration file and rule sources. An unreadable explicitly selected rule leaves its affected stage pending. Match specialized standards by meeting type, including regular meetings and weekly reviews.

The source task requires both a source record and a summary for each eligible meeting with usable original material. Advice follows applicable standards and value screening. The example retains this artifact scope; each cloud artifact requires a verified destination and audience. Authorized text transcripts can be uploaded as source records. Audio, video and other attachments need their own scope.

When adapting an existing deployment, check overlap and preserve its state, known canonical artifacts, mappings and successful baselines. Personal project paths, identities, calendar identifiers, cloud routes, old automation and chat identifiers are omitted. The actual project supplies aliases and series mappings.

Confirm the project, hosting chat, timezone and permitted actions through the scheduler when deploying or changing scheduling. Scheduler notification preferences remain in the platform; the prompt defines report content.

## Connecting a Codex scheduled task

Save a short entry prompt in the scheduler that names the local `prompt.md` and the actual project configuration. Each run reads both files, then resolves project rules and installed skills. The repository maintains the workflow while the platform maintains its entry and schedule.

```text
Run this task in <actual project root>. On every run, first read
<local knowledge checkout>/automations/daily-meeting-summary/prompt.md
and <actual project configuration>, then follow the current files
within the existing authorization. If a source is unavailable, report
the missing input and preserve existing artifacts and progress.
Return results to this hosting chat.
```

Actual entry paths belong in the user's deployed task. When adapting an existing task, preserve its schedule, timezone, hosting chat and notification settings, update the prompt, then read back the result. Existing project configuration can remain the source of truth; the prompt resolves its rule, routing, state and artifact fields. The example documents specialized rules, supporting material, per-artifact cloud destinations and naming rules.

This integration explicitly reads files on each run. Local desktop tasks require the computer and application to be running and the directory to remain accessible. Web-only tasks need uploaded or connected context, with task definitions, configuration and sources prepared for that environment. [Official scheduled task documentation](https://learn.chatgpt.com/docs/automations?surface=app)

## Local review and validation

Local checks on 2026-11-15 confirmed that the deployed entry points to this package and the actual project configuration, its paths resolve, and the three installed skills and selected standards are readable. One existing meeting's transcript, source record, summary, advice and receipts were examined. Source and local artifact fingerprints match the historical receipts. Using historical remote baselines, the Document Sync decision helper returned unchanged content; additional cases returned conflict for two-sided edits and pending confirmation for a missing tracked side.

No live cloud read was performed, so the historical remote baseline is not an observation of current cloud state. Some applicable standards and configuration have changed and require impact review before reuse. Unchanged content fingerprints do not bypass that review. The example remains disabled with cloud writes prohibited.

Those local checks alone do not establish end-to-end execution. A subsequent complete manual run through the extracted entry used Calendar Meeting Archive for live sources and pending work, Meeting Minutes for existing-manuscript and specialized-result reuse checks, and Document Sync for live cloud-content and location comparisons. Of 49 artifacts checked, 47 were reused; one two-sided conflict and one missing standalone local summary were preserved. No cloud documents were created or overwritten.

All 23 text exports matched existing sources; one contained only header information and is not a complete transcript. No usable material required new generation, so new content and upload writes were not exercised and no duplicates were manufactured. Actual scheduled triggering, other deployment platforms and unexercised write branches still require corresponding validation. The manual run saved review state and existing pairings without advancing the scheduled scan cursor or changing scheduling. Business receipts remain in the operator's environment; distributed documentation contains only a sanitized summary. See the [run record](<../../docs/运行记录 Run Record/2026-11-15 定时任务与共享资源验证.md>).

Review one existing meeting's material, rules, responsibility, routing and artifacts before an authorized trial. Preserve existing outputs and receipts. Uncertain ownership, destinations, audience or concurrent changes leave affected artifacts local and pending.
