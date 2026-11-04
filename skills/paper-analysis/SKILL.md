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
Use a compact, structured preface with short labeled paragraphs or small
subheadings for paper/version, reading date/scope and source/check status.
Keep detailed page inventories and tool/process logs in validation records;
do not turn the preface into a second introduction.
For an unversioned post, record its visible publication/update date and access
date; if absent, say so. Preserve existing notes and references when updating.

Choose and report actual reading depth from the purpose:

- **Triage:** relevance from available title, abstract, conclusion and key figures.
- **Targeted:** question, contribution, core method and decisive evidence.
- **Deep:** relevant assumptions, derivations, experiments, evidence and limitations.

Name the sections, pages, figures, appendices or code actually inspected and
material not covered. Extracting all PDF text does not mean reading it all;
abstract screening is not full-text assessment, and reading is not reproduction.

## Analysis structure

Keep identity, version and reading records in a brief preface. For substantive
analysis, follow the paper's reasoning in this order, scaling depth to the task:

1. **Background, motivation and research question:** establish the problem,
   why it matters and the authors' claimed contributions.
2. **Related work and research position:** distinguish the context available
   when the authors wrote the work from subsequent research available by the
   reading cutoff. Explain the closest approaches and differences. Label author
   descriptions versus your actual reading, and record first-public/version dates
   rather than treating every later submission as post-publication work.
3. **Method:** explain the core idea, workflow, mechanisms and algorithms.
   Develop formalization, assumptions, propositions and derivations here only
   when the work contains relevant theory; theory is not a mandatory chapter.
4. **Experiments and results:** connect each important claim to its design,
   source location, comparison, observations and conditions. Explain applicable
   data/model/algorithm/metric settings, baselines, tuning/selection protocols,
   ablations, uncertainty and negative results before judging the evidence.
5. **Reusable research assets:** identify what other research can take and use.
   Separate the asset analysis from the preceding explanation of this paper.
6. **Future work:** group discussion and limitations together, then combine
   future directions and open problems. For each substantive direction, connect
   the unresolved question, evidence, possible path and useful validation signal.
   Distinguish authors' stated directions from your proposals. When discussing
   current progress, align original questions with later evidence and remaining
   conditions; insufficient search proves neither universal resolution nor an
   unaddressed open problem.
7. **References:** list actual sources used, including inspected versions and
   relevant locations or links; mark indirectly known references as such.

Do not add a standalone relationship-to-current-research chapter. Optional
research context may guide the question and interpretation without becoming
an extra output section. For Chinese reports, main headings are Chinese; use
Chinese-English pairs only for the six asset subheadings below. The guides
show the default outline. Adapt method/experiment coverage to the material
instead of forcing a theory proof or empirical experiment onto every work.

## Reusable research assets

Research infrastructure starts with the scientific resources the paper actually
uses: data, models, algorithms, metrics, baselines and code. Identify the concrete
items and their role first, including upstream resources; novelty is not an
inclusion requirement. Then explain how another study could use them and the
relevant conditions. Mark a new contribution as such without using "no new
dataset/model" as a substitute for describing what was actually used.
After method and evidence, develop these categories separately when applicable:

- **数据 Data:** datasets, collection/processing recipes and splits actually used.
- **模型 Model:** architectures, base models, checkpoints, adapters and configurations used.
- **算法 Algorithm:** procedures, update rules, objectives and components used or proposed.
- **评价指标 Metrics:** metric definitions, evaluators and protocols used for the claims.
- **基线 Baselines:** comparison methods actually run or cited, their implementations and conditions.
- **代码与实现 Code and Implementation:** official/third-party source, revision,
  implementation entry points and relevant usage/configuration.

For each category explain **what the paper actually uses, its role, how to
obtain/use it, and its conditions or limits**, with source evidence and the actual verification depth.
Distinguish a new resource contributed by this work from an upstream resource
it merely uses, and a conceptual recipe from a downloadable or tested artifact.
State when a category is unused, an item is unspecified or access is unverified
rather than inventing availability. Link back to method/experiment details instead of
copying them into the asset section. A combined summary table is not a substitute
for developing the applicable categories.

For baselines, identify names/versions and their role, cited versus rerun results,
implementation, data/metric comparability, training/tuning budgets and missing
controls. An experiment proposed by the analyst is not a baseline already run
in the paper. For code, record the repository and inspected commit/release,
paper-to-code entry points, requirements, license and concrete reuse limitations
when checked. Reading a README/source does not prove installation, compatibility,
reproduction or performance. Checking code is not authorization to execute it.

## Time-aware follow-up

For targeted/deep analysis that discusses present-day position or future-work
progress, do a bounded follow-up search around the original questions. Separate
the paper's writing/first-publication context, later research dates/versions and
the reading cutoff. A work appearing between a preprint and its conference
publication needs that timing label. Verify primary sources and actual reading
depth. Citing the paper does not prove a question was answered; work addressing
the same question may be relevant without being a direct citation.

Use related work to explain the subsequent research trajectory, then use future
work to align **original question -> later evidence -> progress and conditions ->
remaining uncertainty**. Distinguish substantial support, partial progress, a
demonstrated gap and insufficient evidence where useful. Claims of resolution
must match the studied models/tasks/assumptions, not just the abstract's wording.
If current follow-up was not searched or could not be read, disclose that limit;
not finding a result does not establish that the field has not addressed it.
Do not claim exhaustive or fully current coverage from a small search.

## Evidence and interpretation

Preserve contribution, data, model, algorithm, metric and baseline detail where
needed to explain the study; reusable-asset analysis does not replace that work.
Connect results to their settings instead of listing names. Distinguish author
claims, your inference and actual checks, not applicable, not reported and
inaccessible material. Lack of reporting is not proof something was not done.
Use page/section/figure/table/code locations when available and keep applicability
limits. Include hardware/runtime details when needed to interpret a specific
claim or fair comparison, rather than making them the default analysis subject.
Do not impose scores, acceptance decisions, strength/weakness quotas, a separate
evidence database or a word limit that removes substantive conditions.

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
Use the shared narrative as a starting point; the guides give type-specific prompts.

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

Use the agreed outline and enough detail to support the requested analysis. The [English guide](references/README.md)
and [Chinese guide](references/README_zh.md) preserve the human reading tutorial
and offer optional analysis prompts. Neither overrides the current task or rules.
