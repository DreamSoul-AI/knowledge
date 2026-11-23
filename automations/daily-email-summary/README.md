# Daily Email Summary

English | [简体中文](README_zh.md)

Summarize actionable mail, follow-ups and important updates with original message links. The [prompt](prompt.md) coordinates the run; [external configuration](config.example.yaml) supplies providers, connections, accounts, folders, interests, formatting rules and destinations. No account or schedule is enabled by the example.

## Setup and manual trial

1. Copy the example into the actual project's local configuration area. Fill in project root, mailbox connections, expected identities, explicit folder scopes, timezone, output and state paths. Keep credentials in the connection provider
2. Use a working, authorized read adapter. Outlook can use get_profile and list_messages/search_messages, with detail retrieval when needed. Feishu can use lark-mail profile, +triage and +messages. Another provider needs equivalent read capabilities; a configured provider name alone does not implement an adapter
3. Ask the agent to follow the prompt and actual configuration for an explicit date range in manual_preview mode. Review coverage, pagination, grouping, links and rerun behavior before enabling any schedule

Accounts and scan progress remain separate across mailboxes. Include read messages when scanning by time. Report the actual folder scope rather than treating a whole-mailbox query as Inbox-only. Summaries do not authorize mailbox changes, replies, forwarding or external publication.

## Summary style

Use short bullets beginning with **Topic or sender | Your next action or current status.** Follow with a short paragraph explaining the concrete request or change, what has already been handled, who is expected to act, any stated deadline and the original mail link. A reply already sent is not an outstanding reply; waiting items identify the other party. Informational items name the actual change. Three to six highlights are a guide, not a quota.

For research discussions, retain the substantive question, new evidence, stated score decision or unresolved concern and distinguish the recipient's role. Grouping must explain how the discussion progressed, rather than merely reporting paper IDs or notification counts. If details needed for the action are missing, read the relevant body or disclose the gap. Put shared coverage and verification limits briefly at the end.

## Configuration fields

Supply the actual project root, connection, verified account, explicit folder scope, timezone and output destination. Each mailbox has its own connection and progress. Interests, important senders and exclusions are user-defined. Account and schedule fields are deliberately unset in the example.

- **Identity:** compare the adapter's signed-in account with expected_account. A provider name does not establish access or switch accounts
- **Folders:** resolve actual folder IDs before a folder-specific query. An unscoped Outlook list_messages request is not Inbox-only. all_visible declares scope; it is not a Graph folder ID. Sent Items must also be included in the allowed scope before reading it
- **Time:** fill both scan.start and scan.end_exclusive for a fixed trial. Incremental scans resume from the previous successful cutoff with overlap. Execution time does not restrict catch-up to one calendar day
- **Preview:** keep deployment.enabled and execution.advance_checkpoint false for manual trials. Choose a schedule only after validating the output
- **Retention:** raw_messages and source_index default to false. Do not save raw responses, bodies, attachments or temporary filtered lists. Explicit local retention is optional; private data never enters distributed examples
- **Deployment:** inspect an existing task and its progress read-only before migration. A scheduled prompt can reference prompt.md and the actual configuration by absolute path only if that environment can read both and access the connector. A repository URL does not mount an automation. Manual trials do not change production progress

Example request:

```text
Read <daily-email-summary>/prompt.md and <actual configuration>.
Check account, folders and timezone, then summarize the fixed window.
Return key items and original links, with actual coverage and gaps.
Do not change the scheduled task or advance its checkpoint.
```

## Validation status

First reusable task definition; configuration and activation are operator-managed. The same full Outlook date window was read online twice to check identity, pagination, boundaries and grouping. The second run disabled raw-message retention and checkpoint writes; the same material was then used to validate the topic-and-next-action/status format. Other providers, account switching, live scheduling and actual interruption recovery remain unverified. The existing personal schedule is unchanged; its success does not establish deployment of this new definition. See the [run record](<../../docs/运行记录 Run Record/2026-11-20 每日电子邮件总结验证.md>).
