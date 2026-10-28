# Document sync

One skill handles upload, download or bidirectional synchronization of one local Markdown and one remote document. Feishu is implemented and uses existing lark-cli, lark-doc and lark-drive. Keep the complete skill folder. The optional deterministic planner uses only Python's standard library and performs no transfer.

## First version and local installation
Version 0.1.0 supports small-scale use with a single Feishu document. The executing agent reads the skill and external rules, then uses existing tools for transfers; the included script only chooses an action and is not a standalone synchronization service. Validation covers text, tables, references, one PNG, one native Mermaid component and resource-only changes. Multiple resources, component replacement with comments and concurrent editing remain unverified.

Install the complete document-sync directory into your personal Codex skills directory, retaining SKILL.md, agents, references, assets and scripts. Exclude caches, execution records and personal configuration. The skill is discoverable on the next turn; read its installed SKILL.md explicitly during the installation turn. Replace every configuration placeholder before use.

To continue an existing Meeting Minutes result, the caller can provide the existing minutes, source identity, delivery configuration, paired cloud URL and earlier archive receipt. Check for existing results first, then hand the file to document-sync with direction upload. Reuse unchanged results and verified baselines instead of regenerating minutes or creating a copy to test delivery.

## Use
```text
Use $document-sync for ./meeting-output/minutes/review.md.
Configuration: ./delivery/feishu.yaml
Use upload for this delivery. Preserve both sides if both have changed.
```

For download, identify the remote document and local destination. For bidirectional work, explicitly choose both. See the [configuration](../assets/feishu.example.yaml). Configuration paths are relative to its file; the source is located in the caller's stated context. An explicit request may override direction and must be recorded. Never infer a missing direction.

Compare each side against its own successful baseline, not Markdown bytes against XML bytes. No changes means reuse; one-sided changes follow the permitted direction; two-sided changes stop as conflict while preserving both versions and the old baseline. Missing tracked sides are not deleted or recreated automatically. Existing pairs without a baseline require confirmation.

Directory mappings match exact parent directories. Feishu exports may contain DocxXML references and extensions: preserve escapes, metadata and resources. Fingerprints must cover dependencies and native source data as well as the entry document. Keep the untouched export and materialize verified PNG images and native Mermaid components as relative local assets and fenced source. Unsupported resource preservation needs confirmation before writing.

Meeting Minutes can deliver validated local results through this same entry point using upload, without enabling download by default. Upload and download share mapping, identity, baseline and conflict handling rather than separate skill entry points.

Run `python scripts/sync_state.py snapshot.json` for a read-only decision and `python scripts/test_sync_state.py` for unit checks. Actual service and formatting behavior still require live validation. Only stop-on-conflict and no-delete policies are supported; recursive synchronization, automatic merges, other platforms and scheduling are not implemented.
