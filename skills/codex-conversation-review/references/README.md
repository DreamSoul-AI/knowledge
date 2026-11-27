# Codex conversation review

Read the selected Codex conversation's public records and explain its goals, turning points, decisions, corrections and unfinished work. Reply in chat by default, without creating Markdown, archive versions or uploads. A whole-conversation review covers the selected conversation through its cutoff; a topic-specific question remains within that scope, not the entire account.

## Read records

Requires Python 3.8+, with no third-party dependencies. The complete review directory works independently of archive. Obtain the selected session ID, locate its filename in the known sessions directory and verify session_meta. Resolve missing or ambiguous sources before proceeding.

Use skill-installer to install https://github.com/DreamSoul-AI/knowledge/tree/main/skills/codex-conversation-review and retain its complete directory. Install archive beside it when full original-record archiving is needed. The skill is available on the next turn; current-chat reloading is a separate check.

```text
python <review-skill>/scripts/review.py --source <session.jsonl> --session <session-id> --limit 40
```

Alternatively supply `--sessions-root <known-directory>` instead of `--source`. Only filenames matching that ID are searched. An ID mismatch or unknown record/provenance fails explicitly.

The first page returns `through_id`, `source_prefix_sha256`, `total_items` and `next_offset`. Continue with that cutoff, `--expect-prefix-sha256` and the returned `--offset` until next_offset is null. Pages contain original messages, not semantic summaries. Use `--view records` for related tool results; each view has its own item count and offsets. Stable IDs and source_line connect evidence to messages.

Each page rereads the same file; this is not byte-offset acceleration. Later appended messages stay outside the fixed cutoff. A changed prefix stops processing. Pass all events from records view or Python `records.prepare` to archive, never just message pages. See [record boundaries](record-format.md) for supported formats, missing timing, partial lines and attachments.

## Review and archive

Use [review organization](review-standard.md) to interpret the records. The script provides public evidence and timing, not an automatic decision summary or hidden reasoning.

Archive calls review for full records and a separate narrative, then owns immutable versions, original text, tools, timing and integrity checks. Install both complete directories beside each other, or use archive's `--review-skill` to specify review's location. Review does not depend on archive. Updating an older installation requires checking both complete packages and their actual loaded locations.

Public records can still contain sensitive information. Reading them does not authorize copying them into other chats, committing or uploading them.
