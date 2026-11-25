# refresh-chat

Use `$refresh-chat` after workspace rules or source locations change. It checks the actual working directory, applicable AGENTS/override files, REPO, relevant USER configuration and explicitly available memory or reference entries, then explains changes affecting the current task and its continuation point.

The core `SKILL.md` is sufficient for a normal refresh. Open this guide for first-time preparation, an exception, or missing operational detail. There is no need to routinely load both language versions. Keep the complete rules rather than shortening required content to reduce reads.

For several chats, specify the targets and relevant changes. First compare changed files/versions with each chat's actual workspace, linked sources and last reliable read receipt. Mark chats as needing refresh, already current, unaffected, deferred until use, or unresolved. A hash or modification time does not establish that an Agent loaded the rules. Do not scan every chat's full history to make this selection.

First use, a changed working directory/source entry, or an unreliable baseline requires the necessary complete entry files. With a reliable baseline, read only relevant changes and affected references. Send short requests with concrete change locations. Targets return compact receipts with actual paths, versions, application and gaps; verify necessary tool evidence and reuse sound receipts rather than rewriting them.

Once the necessary file paths and relationships are known, combine independent reads when the tool supports it, retaining file identities and individual errors. Locate unknown entries first, and keep dependent discovery steps sequential. Batching does not omit required text or relax complete-entry reading when the baseline is unreliable.

An explicit request to refresh a paused or unused chat now still applies, while its business work stays paused. Otherwise deferring until continuation may avoid unnecessary calls. Each target reads its own workspace; inspecting status does not send requests. Submission, reading and demonstrated application are separate states. First check that necessary refreshes are identified and unnecessary requests are not sent. Then check that dispatch contains only the skill entry, the current change and necessary exceptions. Reading required files such as AGENTS.md is normal; do not omit their content to shorten a request.

Example: “Use $refresh-chat; changes: <file/version>. Refresh rules only, preserve business state and report briefly.” If the skill is not installed, replace the invocation with a readable full SKILL.md path. Do not repeat the skill procedure. Preserve necessary information without imposing a fixed character limit.

Refreshing does not resume business, clear context, restart the host or change tool permissions. Preserve confirmed task facts, pauses, authorization and uncommitted work. Report missing paths, unavailable tools and access failures precisely. No hooks or new memory service are required. Keep the full package together; a local candidate is not a published or automatically discovered installation.
