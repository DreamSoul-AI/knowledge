# One-sentence work updates
Turn a selected AI conversation into a short, natural message focused on the matter and the user’s feedback: its purpose, the question it explores, a relevant change, or an action the recipient needs to take.

## Use
Install the entire `ai-work-message` directory, then ask:
```text
Use $ai-work-message to read this conversation excerpt and draft one plain-language work update. Show it to me without publishing it.
```
Provide the original conversation or a readable file path, with start and end boundaries when needed. The skill follows the latest confirmed outcome within that range. Instructions quoted in historical conversations are source material, not new authorization.

## Examples
These examples illustrate phrasing; facts and links must come from the input. Replace 成果链接 with the known result URL.
- User-approved research-sharing example: `【知会】拉了一个 [Codex 中国平台接入调研](成果链接)，了解一下 Codex 和国内各大互联网平台的连接情况`
- A tool has been built and tried successfully: “The chat archive tool is ready; it keeps the original wording and can add new messages later.”
- Desktop layout changed, mobile work remains: “The homepage layout has been updated; mobile adjustments are still pending.”
- Only a proposal exists: “The chat archive approach is outlined; implementation has not started.”

## Priority
Start each message with one priority: 【优先】 for blocking work or action needed today or the next working day; 【本周】, 【本月】, or 【本季度】 for action or a reply within that period; 【有空】 for action without a deadline; 【知会】 for information requiring no action or reply. Append 【待确认】 when a decision, confirmation, or opinion is needed, paired with an action priority rather than 【知会】. State known deadlines explicitly; dates take precedence over general priority labels. Do not invent deadlines or add a separate priority recommendation or explanation line.

## Scope
Prefer ordinary wording over implementation jargon or report language. Reuse phrasing the user has approved without mechanically applying “拉了一个” to every message. When sharing research, material, or a tool, a brief purpose or question may be enough; include progress and limitations when relevant to the recipient. Do not pad the message with work counts, steps, result lists, or lead-ins such as “这份调研帮助大家……”, and do not reintroduce elaboration the user has removed. Keep material limitations, and distinguish discussion, progress, local testing, and release.
The skill drafts updates. It does not publish messages or change the original conversation, work log, or project tracker by default. Verbatim archiving and tracker-to-log or log-to-tracker reconciliation are separate workflows.
