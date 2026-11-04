---
name: paper-analysis
description: Read and critically analyze academic papers, extracting claims, methods, evidence, limitations, and research relevance into structured notes. Use when one or more papers have been selected for close reading or comparison.
---

# Paper Analysis

## Optional context and scope

Start from a selected paper, link or supplied text. Supplementary material,
research questions/plans, existing notes, applicable standards, preferred depth
and output requirements are optional inputs in natural language or files, not
a required form. Read the supplied context and applicable project instructions;
state what was used. Without extra context, analyze the selected work on its
own and state a reasonable focus. Keep project-specific rules external.
If material is inaccessible, identify the missing part and continue only the
analysis supported by available sources. Do not claim compliance with unread
rules. Paper analysis does not authorize library reorganization, renaming,
training/reproduction, uploads or messages; suggested follow-ups are not actions.

## Identity, version and reading record

Record title, authors, stable ID or source URL, publication status/date and the
actual version read. Keep preprint, publication, supplement and any inspected
code revision identifiable; do not silently mix their results. Include the
actual reading date and, for an updated note, its update date and changed scope.
Record elapsed reading time only if actually measured, never inferred.
For an unversioned post, record its visible publication/update date and access
date; if absent, say so. Preserve existing notes and references when updating.

Choose and report actual reading depth from the purpose:

- **Triage:** relevance from available title, abstract, conclusion and key figures.
- **Targeted:** question, contribution, core method and decisive evidence.
- **Deep:** relevant assumptions, derivations, experiments, evidence and limitations.

Name the sections, pages, figures, appendices or code actually inspected and
material not covered. Extracting all PDF text does not mean reading it all;
abstract screening is not full-text assessment, and reading is not reproduction.

## Analysis framework

Preserve the original question, contribution, method, evidence, critical
assessment and relationship-to-prior/user-work framework. Make the applicable
scientific components explicit. Here **research infrastructure** groups
**data, model, algorithm and metric** and their relationships:

- **Contribution:** identify the problem, claimed novelty and difference from
  the closest work. Distinguish author claims from your assessment of support.
- **Data:** source, construction, task, scale, splits and preprocessing; assess
  leakage, representativeness or bias where relevant and supported.
- **Model:** architecture/base model, scale or checkpoint, component roles,
  trainable/frozen parts and relevant training/inference settings.
- **Algorithm:** inputs/outputs, mechanism, steps, objective and assumptions;
  explain how it operates on the data and model.
- **Metric and evidence:** definition and aggregation, evaluation protocol,
  baselines and settings, decisive results, ablations/uncertainty and boundaries.

Connect results to their data, model, algorithm and metric conditions instead
of listing names alone. Include hardware or deployment details when needed to
interpret a particular claim, without replacing these scientific components
with an operations checklist. Distinguish not applicable, not reported and
unavailable material; do not invent values or fill every field mechanically.

For important claims, connect the source position, evidence, conditions and
your judgment in concise prose or a small table. Use section/page/figure/table
locations when available. Separate author statements, your inference and any
actual checks. Lack of reporting is not proof the authors did not do something.
Discuss limitations, reproducibility information, unanswered questions and
concrete relevance to the requested purpose. Do not impose numerical scores,
acceptance recommendations, strength/weakness quotas or a separate evidence log.

## Adapt to the material

Allow overlapping theory, method and application contributions; also recognize
system, data/benchmark, survey/review and position work. Record
source form/status separately: a blog post can contain a method or a position,
and is not automatically peer reviewed. Use applicable evidence rather than
forcing empirical datasets and metrics onto every material type.

For theory inspect assumptions, statements and derivations; for methods and
applications inspect mechanisms and evaluation; for systems inspect design and
workload-dependent claims; for data/benchmarks inspect construction and evaluation
protocols; for surveys inspect scope, taxonomy and synthesis; for positions/posts
inspect arguments, factual sources, alternatives and testable implications.
The guides provide type-specific prompts, not mandatory output templates.

## Scholar and source lookup when needed

When identity, publication/version, citation impact or a relevant reference
needs checking, use authoritative paper/venue/author sources. For small Google
Scholar lookups, use an available browser/Computer Use tool and follow its
current instructions. Replace the query with the full title; check the actual
query, matching title, authors and original link. If reporting citations, retain
the displayed count, source link and observation date. Do not sum overlapping
version clusters, use search-result totals or treat unavailable counts as zero.
Label reused observations with their original dates instead of claiming a new
lookup. Stop the affected lookup on a CAPTCHA, access block or rate limit and
follow the tool's handoff rules without bypassing restrictions. State when the
tool/source is unavailable and continue supported reading. This is optional
interactive discovery, not a bulk API or evidence for technical claims; retrieve
the original source before assessing a discovered claim. Keep reference follow-up
bounded to the analysis question; a broader search is a separate task.

## Diagrams and mathematical abstraction

Write mathematical formulas in LaTeX, including inline and display equations.
For targeted/deep analysis, explain mechanisms in text and use Mermaid diagrams
and applicable LaTeX to show the same concept's structure and transformations.
Define symbols, dimensions and assumptions and explain how representations
correspond. Distinguish source equations, equivalent rewrites and your own models,
with source positions and applicability limits. Do not invent formulas or impose
a diagram quota; triage or nonmathematical arguments may need neither.
Keep editable diagram source, check arrows and formulas against the text, and
verify derivations/rendering where supported. State what was not checked; a
numerical spot check is not a general proof. Follow destination conventions.

Use a compact note or the requested format. The [English guide](references/README.md)
and [Chinese guide](references/README_zh.md) preserve the human reading tutorial
and offer optional analysis prompts. Neither overrides the current task or rules.
