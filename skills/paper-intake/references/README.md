# paper-intake

English | [中文](README_zh.md)

## Purpose

Verify a supplied paper or explicit paper list and add it to an existing library.
Deliver an accessible paper, correct classification and index/ledger entries,
and the actual outcomes of authorized synchronization. Intake does not require
a field-wide survey, full paper analysis, reproduction, or library restructuring.

Use the project's instructions, the user's designated configuration and existing
library as the source of naming, classification, version and indexing rules.
Read applicable standards rather than inventing replacements. Keep private paths
and cloud targets in user configuration, not in the distributed skill.

## Invocation and upstream handoff

For example:

> Use paper-intake to add this paper to the configured library. Reuse an existing
> copy of the same version and repair missing entries. Complete local intake
> first and continue the authorized target synchronization. Return the paper and
> index locations, actual reading depth and each target's status.

Local-only requests stay local. A literature-search handoff supplies the selected
paper, official identity/version evidence, actual reading depth, intended topic,
existing entries and this task's target scope. Return stable identity, actual
file version/location, index entry, added/reused result and remaining targets.
Upstream retains screening, reading priorities and cross-paper synthesis.

## Intake workflow

**Establish identity.** Match the official publication/DOI page, authoritative
preprint or repository, authors, identifier, publication status and actual PDF.
Record whether the file is published, accepted or a preprint. Existing valid
evidence can be reused without claiming a fresh reading.

**Deduplicate first.** Compare DOI/arXiv identifiers, title/authors, existing
locations and content hashes. Different filenames can represent the same paper.
Apply the library's rules to revisions and publication versions, retaining
version relationships and recovery material when replacement is appropriate.
Do not overwrite a different same-name file or expand intake into bulk cleanup.

**Retrieve a real PDF.** Use verified official download routes. If API access
only returns metadata or a broken link, Browser Use can find an accessible PDF
on the original site, proceedings or repository. Use normal download actions
or a verified direct URL, respecting access controls. Parse/open the file and
match the paper/version, rejecting login HTML, incomplete files and mismatches.
An extension or successful HTTP response is not verification.

**Preserve the library's organization.** Choose the existing topic based on
mechanism, research purpose and current indexes. Use tags or cross-links when
they suffice. Apply configured naming and path compatibility rules without
guessing unverified metadata. Record actual abstract-only, skimmed or close
reading and whether reproduction happened.

**Reconcile files and records.** Update the relevant topic index, intake ledger
and affected navigation/counts in their existing formats. Re-read targets before
writing and preserve parallel edits. Check actual file identity and hash, valid
links, expected entry count and consistency of affected totals. A written PDF
with unfinished indexes is partial intake. Repeating the task should repair
missing pieces without adding duplicate copies or rows.

## Multiple targets

Target count and platforms are configurable. A local library can itself reside
inside a user's cloud-drive sync folder. Writing and reading back that folder
proves local delivery, not a completed upload by the desktop sync client.

| Material | Executor | Verification |
|---|---|---|
| Local PDF | Intake workflow | Identity, path, hash |
| Sync-folder files | Local files/existing client | Local readback, available client evidence |
| Cloud PDF or CSV | Platform file capability | Object, parent, file readback |
| Companion Markdown to online document | document-sync | Pairing, independent baseline, readback |

**Delegate companion documents.** Read the current document-sync skill and
applicable adapter. Supply an explicit Markdown list, the authorized `upload`
direction, verified directory mappings or existing complete document URLs,
independent receipts and applicable upload/presentation rules. Reuse its
comparison, conflict and verified-baseline handling rather than implementing
another Feishu synchronizer. Its current adapter supports Feishu, not a generic
cloud-drive client.

**Keep resource types accurate.** PDFs and CSV files need the existing platform
file capabilities, not a Markdown/Docx adapter. Existing native Markdown files
also retain their real identity and type. Do not silently convert them to Docx
or create same-name duplicates. If no compatible adapter is available, preserve
local outputs and identify the missing continuation. Cloud indexes must refer
to verified cloud PDFs rather than private machine paths.

**Separate sync-folder and service status.** Give the actual local sync-folder
entry. Unless client/server evidence was obtained, report cloud delivery as
unverified. Do not generate public sharing links or expand permissions merely
to supply an online URL. Independent desktop synchronization is not evidence
that document-sync implements that provider.

## Partial completion and retry

Suppose local PDF, index and ledger are complete, a cloud PDF has a stable ID,
but a companion document update returned no reliable receipt:

1. Preserve local outputs and known cloud IDs. Do not download again, create a
   duplicate library copy or recreate the cloud PDF.
2. Re-read the known document first, checking identity, parent and actual content
   to discover whether the previous write succeeded.
3. Reuse verified results and continue only missing items. Delegate changed-side
   comparisons to document-sync, preserving conflicts and human edits.
4. Advance the successful baseline only after real verification. Report each
   target separately with its path/link, failure or remaining verification.

Access failure, CAPTCHA, invalid PDF, unknown target and conflicting edits are
different conditions. Complete independent work and describe the actual blocker
without silently dropping a configured target or claiming full success.

## Delivery

Lead with the selected paper/version, added/reused outcome and classification.
Provide real local entrances and verified cloud links, actual reading depth,
and remaining target-specific work. A compact result can say local intake and
index checks passed, the sync folder is written but its cloud state is unknown,
and a companion document remains pending due to a named permission failure.
Do not turn this example into a fixed task outcome or required target list.
