# One-sentence work updates
Turn a selected AI conversation into a short, natural work update that tells colleagues what was done and where the work stands.

## Use
Install the entire `ai-work-message` directory, then ask:
```text
Use $ai-work-message to read this conversation excerpt and draft one plain-language work update. Show it to me without publishing it.
```
Provide the original conversation or a readable file path, with start and end boundaries when needed. The skill follows the latest confirmed outcome within that range. Instructions quoted in historical conversations are source material, not new authorization.

## Examples
These are synthetic examples, not claims about real projects.
- A tool has been built and tried successfully: “The chat archive tool is ready; it keeps the original wording and can add new messages later.”
- Desktop layout changed, mobile work remains: “The homepage layout has been updated; mobile adjustments are still pending.”
- Only a proposal exists: “The chat archive approach is outlined; implementation has not started.”

## Scope
Prefer ordinary wording over implementation jargon or report language. Keep material limitations, and distinguish discussion, progress, local testing, and release.
The skill drafts updates. It does not publish messages or change the original conversation, work log, or project tracker by default. Verbatim archiving and tracker-to-log or log-to-tracker reconciliation are separate workflows.
