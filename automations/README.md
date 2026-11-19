# Automations

English | [简体中文](README_zh.md)

Reusable prompts and configuration examples for recurring tasks. Automations compose installed skills and platform tools. The user's environment maintains scheduling, authorization and runtime state.

## Automation registry

| **Automation** | **Reference schedule** | **Definition status** | **Validation** | **Entry points** |
| --- | --- | --- | --- | --- |
| Daily Meeting Summary | Daily 00:00, Asia/Shanghai | First version | Manual checks passed; new writes and triggering pending | [Guide](daily-meeting-summary/README.md) / [Prompt](daily-meeting-summary/prompt.md) / [Configuration](daily-meeting-summary/config.example.yaml) |
| Daily Email Summary | User-configured | First definition | Outlook read and summary format verified; other providers and scheduling pending | [Guide](daily-email-summary/README.md) / [Prompt](daily-email-summary/prompt.md) / [Configuration](daily-email-summary/config.example.yaml) |

Register task definitions that actually exist in this repository. Add a row and maintain its directory and validation status when adding a task. A reference schedule does not mean a task is enabled. Accounts, hosting chats, scheduler identifiers and deployment status remain in each operator's environment.

The current task composes Calendar Meeting Archive, Meeting Minutes and Document Sync to incrementally process ended meetings. A manual run through the extracted entry on 2026-11-15 performed live source scanning, existing-manuscript review and cloud comparisons, reusing artifacts and preserving conflicts and missing inputs. No material required new generation; the trial did not create duplicates to exercise writes. Generation, writes and actual scheduled triggering remain explicitly outside this run's coverage. Prior deployment success does not replace evidence for this revision. See the [run record](<../docs/运行记录 Run Record/2026-11-15 定时任务与共享资源验证.md>).

Each directory maintains English and Chinese guides, a `prompt.md` and a `config.example.yaml`. Prompts coordinate skills. Content standards, deduplication and transfer behavior remain in the referenced skills and project rules.

Copy the example configuration into the actual project's local configuration area and supply identity checks, rule sources, destinations and persistent state paths. Personal configuration, credentials, task and chat identifiers, locks, receipts and meeting material stay in the runtime environment. Check distribution contents before publication.

Before enabling, replacing or changing a deployed task, confirm its existing scheduler entry, destination, timezone, scope and authorized actions. Preserve known artifacts and progress, and validate each deployment. Scheduler changes are performed separately through the scheduling platform.
