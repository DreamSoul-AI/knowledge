---
name: literature-search
description: Plan and conduct academic literature searches using supplied material and applicable rules, emphasize citation impact, screen and deduplicate results, and produce traceable reading lists or evidence maps. Use for research discovery and review-scoping, not deep analysis of one already-selected paper.
---

# Literature Search

## Inputs and scope

Accept the research question, purpose, existing paper lists or other material,
supplements, applicable standards, date range, output requirements and location
in natural language or an external file. Read the supplied material, current
project instructions and applicable standards before searching; use existing
lists as seeds and a deduplication baseline. Report which inputs were used.
Project-specific rules stay external, without requiring a company account or
private path. If a requested input is inaccessible, state the affected scope and
continue independent work; do not claim compliance with unread rules. State
reasonable assumptions for unspecified details rather than requiring a form.

Keep discovery, deep reading, library maintenance and reproduction distinct.
Searching does not itself authorize reorganizing existing papers, running
experiments, uploading documents or sending messages. Reuse existing outputs
where appropriate and follow the requested read/write boundaries.

## Search and selection

1. Decompose the question into concepts, synonyms, abbreviations and exclusions.
2. Build complementary query families and choose appropriate scholarly sources.
   Use seed references and citing work to fill important gaps, not an unbounded
   citation crawl. Record access failures and actual search coverage.
3. Screen by research relevance, citation impact, evidence quality, venue,
   recency and role in the field. Open the original paper or authoritative
   metadata page for included works; snippets and curated lists are discovery
   aids, not evidence of full-text reading.
4. Deduplicate by DOI/arXiv ID, title and authors. Link preprint and publication
   records, recording the version actually read; substantive extensions may be
   separate works. Do not merge different works by similar titles alone.
5. Separate surveys, foundational work, representative methods and recent
   advances. Explain inclusion and reading priority for the current purpose.
6. Stop when the scoped questions have useful coverage and further searches no
   longer change the main picture, or report the remaining gaps and limits.
   Do not claim exhaustive or systematic coverage without supporting records.

## Citation impact is a prominent selection signal

Actively seek influential, highly cited work and make citation counts prominent
in the reading list. For foundational work and established methods, citation
impact should carry substantial weight in selection and reading priority.
Combine it with direct
relevance and what the paper contributes. Recent research has had less time to
accumulate citations, so explain that context rather than treating a low count
as automatic exclusion or a high count as proof that every claim is sound.

Retrieve counts from an identifiable bibliographic source when accessible.
Report the count, source link and observation date; a shared source/date note
can cover a whole table. Keep sources consistent where possible, or label
differences rather than treating cross-platform counts as directly comparable.
Confirm the count belongs to the correct paper/version group; do not sum
overlapping preprint/publication counts, substitute GitHub stars or infer a
number from a search snippet. If lookup fails, write “unavailable” and the
reason, not zero or an invented estimate, and continue the literature search.
Counts order exploration and reading; no automatic paper score is required.

## Inclusion value tiers

Give included papers an explicit task-relative tier and a short reason, rather
than only free-text priority. Use the supplied tier rubric if present; otherwise
use **A Core**, **B Important**, **C Supplementary**:

- **A Core:** directly answers the central question or provides an essential
  foundation; prioritize for core reading and synthesis.
- **B Important:** fills a key comparison dimension, implementation condition or
  directly relevant candidate route; retain for the corresponding research branch.
- **C Supplementary:** contributes useful peripheral detail; revisit when that
  subquestion becomes relevant.

Keep the tier separate from relationship to existing material (e.g. existing
seed or new candidate), the reason, actual reading depth and citation count with
source/date. Citation impact remains a substantial signal for mature work;
combine it with relevance and knowledge dependencies without converting counts
into fixed thresholds or a numerical score. Tiers describe value for this task,
not universal paper quality, venue rank or verification status. Abstract-only
judgments are provisional and can change after deeper reading. If the available
material cannot support a tier, mark it pending with the reason; do not force C.
Do not impose a quota of papers in each tier. Show these fields in the existing
list or compact table, without requiring a separate grading document.

## Google Scholar through Computer Use

For a small citation lookup, use Google Scholar's visible website through an
available browser/Computer Use tool when requested or when API counts are
unavailable. Follow that tool's current instructions; the skill does not bundle
a browser or promise that every host can access Scholar. Replace the search
field with the full title, verify the actual query, then match the result's
title, authors and original paper link before reading that row's “Cited by”.
Record its count, source/result link and observation date. Use the displayed
count, not the overall search-result estimate, and do not infer zero from a
missing citation link. Separate clusters or citation-only entries may overlap:
record the selected matching entry and note ambiguity rather than adding counts.
This is a limited interactive lookup, not a bulk scraping interface. Stop on a
CAPTCHA, access block or rate limit; leave affected counts pending or request
user handoff according to the tool's rules, without bypassing the restriction.

## Lightweight evidence and delivery

For a small task, keep the evidence inside the result: a short note with the
date, sources, key queries, time window and access/coverage limits, followed by
paper entries with title/authors, stable ID or original link, publication or
version date, relationship to existing material, inclusion value tier and reason,
reading status and citation count provenance.
Distinguish metadata/abstract screening from full-text assessment. Explain
important exclusions or uncertain matches when they affect the conclusion.
Do not require separate logs, a database, fixed paper counts or a file tree.
Larger or continuing reviews can reuse their existing search records.

Return a cited synthesis of the scoped question, prioritized reading list and
unresolved gaps. Keep source claims and your interpretation distinct. If the
task requests a full literature review, apply its supplied reporting standard
and state the actual synthesis and reading coverage. Rendering and derivation
checks are separate from text checks. The [English guide](references/README.md)
and [Chinese guide](references/README_zh.md) are optional human tutorials, not
permission to execute all their follow-up suggestions.

## Diagrams and mathematical abstraction

Write all mathematical formulas in LaTeX, including inline and display equations.

When the requested output explains method families or mechanisms, keep a clear
text explanation and aim to accompany it with Mermaid diagrams and applicable
LaTeX abstractions. Show the same concept from complementary perspectives:
meaning and conditions in prose, structure and relationships in diagrams, and
objects, constraints, or quantitative relationships in mathematics. Explain how
these representations correspond and plan them together in any outline.
A search list alone does not need formulas or diagrams. Do not invent formulas
or imply deeper reading than was actually completed.

Explain nodes, arrows, symbols, dimensions, and assumptions. Cite the supporting
source locations and distinguish source content from your own abstraction.
Keep editable diagram source, check consistency with the text, and verify
rendering where supported; disclose unverified rendering. Follow the destination's
math and diagram conventions rather than forcing a diagram or formula quota.
