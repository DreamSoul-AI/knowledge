# General Research Standard

[简体中文](README_zh.md) · [General Search Skill](../SKILL.md)

In Codex, invoke `$general-search` with the topic, the questions to answer, and any existing material. For formal research, prepare an outline first and write the report against it.

## 1. Scope and principles

Established September 14, 2026. This standard covers technical research, source collection, analysis, and report writing for engineering and related practical work.

Before drafting the outline, locate and read the applicable document standard from the project's documentation entry point, such as its Feishu Document Standard. Apply the relevant naming, heading, layout, table, and figure rules to the outline, report, and source index even when drafting in local Markdown first. Check the deliverables against that same standard. Use this guide when the project has no applicable standard. When uploading or converting the documents, also check how they render on the destination platform.

Use the standard to explain what a technology or tool is, what problem it solves, how it works, where its implementation or use is limited, and how it might be used in a given setting. Topics include software and tooling, frameworks and platforms, system internals, protocols and interfaces, engineering workflows, technical ecosystems, hardware and software options, and related materials.

The emphasis is on practical technical and engineering questions. Sources may include official documentation, source code, standards, technical articles, product information, discussions, internal records, or papers. Assess each source by what it establishes for the question at hand.

A report may simply explain the subject reliably. Procurement advice, a plan to implement, and experimental results are only needed when the task calls for them. Academic questions, paper contributions, and research trajectories follow the project's Literature Search Standard. In mixed topics, allocate questions to the appropriate report and cross-reference them.

Create both a general research report and a literature review under the same topic when requested or when both sets of questions need independent treatment. General research covers use, organization, platform differences, operating procedures, and maintenance. Literature review covers the research trajectory, methods, and paper evidence. Keep shared source metadata in one place and give the practical analysis its own prose.

- **Questions first.** Define what to answer before choosing where and how deeply to search
- **Explain mechanisms.** Describe how the parts relate, the conditions, and the trade-offs
- **Keep evidence close.** Cite the actual support alongside important facts
- **Distinguish evidence from judgment.** Identify source claims, code inspection, tests, inferences, and recommendations
- **Keep applicable conditions.** Versions, platforms, configuration, dates, and use cases are part of the conclusion
- **Keep uncertainty visible.** Report what was found, what remains unverified, and where sources disagree
- **Scale the deliverables.** Make an outline before the formal report. A small topic can use a compact outline. Add indexes and attachments as needed
- **Enable review and reuse.** Let readers trace the evidence, understand the analysis, and identify the remaining questions

Treat mandatory requirements as the minimum. Scale recommendations to the task and use conditional steps where applicable. Keep the scope, source traceability, and factual accuracy at every size.

If supplied material or an applicable standard cannot be read, record the actual cause, such as an invalid path, a missing tool, authentication, resource permissions, or incomplete content. State what was read and which conclusions are affected. Try known alternative entry points to the same material and continue work that can proceed independently. Keep judgments with missing critical evidence unresolved and list the material needed to complete them.

## 2. Define the question, scope, and depth

### Minimum task definition

Record the following at the start of the outline or report. Reuse established task and project facts and flag uncertain details that affect the conclusion.

| Item | What to specify |
| --- | --- |
| Purpose and audience | Who will use the report and what it should explain or help decide |
| Core questions | Questions that can be answered individually |
| Subjects and boundaries | Included and excluded systems, technologies, and scenarios |
| Constraints | Relevant platforms, architecture, equipment, budget, people, or compatibility |
| Dates | Information cutoff and, for changing sources, the actual access date |
| Depth and deliverables | Overview, mechanism analysis, comparison, or verification, and the files required |

For example, narrow an operating system survey to the components, state, completion paths, and differences involved in reading a file on three systems. Break CI/CD research into integration checks, builds, releases, and traceability.

### Choose the main focus

| Focus | Main question | Suitable result |
| --- | --- | --- |
| Overview | What are the concepts, objects, and sources, and how do they relate? | Map, explanations, reading path |
| Mechanism and implementation | Who performs the work, where is state kept, and why does it work this way? | Architecture and execution paths, source locations, limits |
| Comparison | How do capabilities and trade-offs differ for the same need? | Comparison and applicable conditions, with advice if requested |
| Engineering practice | How does the workflow solve the problem and what does it require? | Practical mechanism, project mapping, questions to verify |
| Diagnosis and verification | Which explanation fits the observation and what would rule out alternatives? | Evidence chain, verification record, conclusion limits |

A report may combine multiple focuses while keeping one main question or organizing axis. Include timelines, rankings, code snippets, and deployment steps where they serve that question.

### Scale the outline and deliverables

Determine scale from the user's purpose, breadth of questions, range of objects or approaches, and the mechanisms and evidence needed for coverage. Do not default to a small topic or ask the user to choose a size by default. For formal studies of systems, architectures, or technical approaches, establish coverage of the major categories and representative real implementations before developing the mechanisms and comparisons. Staging changes the research order, not the overall scope; an earlier small experiment does not automatically limit a later formal study. Use a lightweight treatment only for explicitly local or genuinely bounded questions. Length, heading counts, and citation counts do not establish coverage, and not every query needs a long report.

- **Small topic.** Prepare a short outline and a report with scope, answers, limits, and References. Keep source details at the end. If explicitly asked for one short file, put the outline in that file
- **Comprehensive topic.** Prepare a standalone outline and its corresponding report. Add a source index when material is extensive or frequently reused
- **Long-running topic.** Add a search log, attachments, and structured records where they help ongoing updates or handover

In the outline, give actual section titles, the questions they answer, expected evidence, and unresolved points. Plan which concepts benefit from prose, an editable Mermaid diagram, or a justified LaTeX expression. Include a separate plan for References that connects source groups, representative systems or protocols, and priority readings to specific questions.

For a comprehensive topic, show the real hierarchy of headings and subheadings. Use consecutive levels, starting with H1 for first-level sections where the delivery format follows that convention. Brief, single-purpose sections can remain at the top level. For each substantive section, state its question, representative evidence, and relationship to adjacent sections. Organize task metadata, the heading tree, and the reference plan separately. Revise the outline when evidence changes the classification and reconcile it with the final report.

### Classification and axes

Choose one consistent axis for parallel sections, such as mechanism, component, or problem. For example, caching and scheduling can be categories, while vendor, date, or reading status can be comparison fields.

Use separate sections, table columns, or tags for platform, version, context, and evidence type when helpful. Cross-reference objects that appear in several themes. Keep shared background in one place. If the report is organized by product, use common questions to compare products and explain differences in coverage.

State the classification axis, representative systems or sources, and division of topics in each section of the outline. Identify the classification as an analytical choice unless a source establishes it as official.

## 3. Find, screen, and record sources

### Search workflow

1. Read earlier research, project constraints, and applicable standards. Identify which findings can be reused and which facts need rechecking.
2. Plan first-draft coverage around the core questions. List the main approaches, common scenarios, important comparisons, conditions, and counterexamples that could change the conclusion. Carry sound earlier evidence and methods into the outline.
3. Establish primary sources using official documentation, specifications, public repositories, or original release records. Follow supporting details as required.
4. Search for alternative implementations, restrictions, failure cases, compatibility notes, and opposing evidence.
5. Trace secondary material through to interface documentation, source code, design discussions, or change records where the conclusion requires it.
6. Check evidence for core questions and branches before drafting. Update the outline and report when a new line of evidence changes the analysis.

Search snippets, aggregators, tutorials, and generated summaries can surface leads. Open the actual supporting material before citing a key fact. Record whether you accessed an abstract, a section, or a secondary quotation.

### Evaluate sources by what they can establish

| Source | Useful evidence | Check |
| --- | --- | --- |
| Official technical docs, API docs, standards | Definitions, public contracts, capabilities, compatibility | Version, maturity, implementation differences |
| Official code, tests, releases, changelogs | Implementation, fixes, evolution at a specified version | Tag or commit, whether the code path actually runs |
| Product pages, pricing pages, licenses | Vendor claims, plans, pricing, licensing | Region, plan, version, date, limits of the claim |
| Author posts, design docs, engineering talks | Rationale, experience, trade-offs | The setting and assumptions behind the account |
| Issues, discussions, Q&A, user reports | Failures, edge cases, practical experiences | Reproduction conditions, maintainer response, resolution |
| Third-party tutorials, evaluations, reviews | Onboarding, comparisons, independent observations | Method, conflicts of interest, original source |
| Internal docs, logs, local measurements | Project constraints and observed behavior | Environment, date, traceable records |
| Papers and technical reports | Principles, history, methods, experimental evidence | Applicability to the shipped system |

Assess directness, specificity, version match, reproducibility, and potential bias for each claim. A single universal quality ranking cannot represent all these uses.

### Include, exclude, and stop

- Use material that supports or explains the central questions in the report or source index. Put background-only sources under Further Reading. Prefer the original over repeated copies
- Exclude unrelated material, material for incompatible versions, and unsupported key figures. Note exclusions that affect the conclusion
- Look for independent evidence for consequential disputed claims. Several rewrites of one release note share an origin. Documentation and code from one vendor can complement each other
- Complete search, analysis, drafting, and self-check in one formal research task. Explain representative mechanisms, implementation differences, conditions, costs, and failure cases. Keep tables scannable and explain reasoning and important counterexamples in prose
- Before delivery, investigate gaps that could change the conclusion or choice. Update the summary, comparisons, and conclusion together. Report remaining gaps, actual coverage, and the effect on the conclusion
- Judge completion by the questions and evidence. Claims of exhaustive search require supporting methods and records

For broad or long-running work, keep a search log with dates, questions or queries, major sources, inclusion or exclusion reasons, and outstanding issues. Record the research path in a useful form.

### Depth and research value

Give central, disputed, and implementation-sensitive sources the reading depth they need.

| Reading status | Actual work |
| --- | --- |
| To read | Entry located, content unchecked |
| Skimmed | Overview, contents, or selected passages checked for relevance |
| Targeted reading | Relevant sections, interfaces, or code paths inspected and recorded |
| Deep reading | Surrounding context, conditions, branches, and related evidence checked |

Summarized can be tracked as a separate state. Record the sections or paths actually read. Full-text extraction and reading are distinct activities.

In a standalone source index, give each included item a one-sentence account of its unique value for the topic. Optional roles include introduction, design rationale, implementation, interface constraint, evaluation method, counterexample, and practical experience. Mark unread candidates as pending judgment.

Write standalone reading entries for material that supports central definitions, mechanisms, comparisons, or findings. A reader should be able to identify the source, understand its substance, evaluate its usefulness, and continue reading. A short primary source can have a compact entry. A supporting source can have a full reference and a short description of its role.

```text
Source and reading scope: title, location, version, actual sections or code paths
Question: what this source answers
Content and mechanism: key objects, states, or execution steps
Analysis and comparison: reusable ideas, differences, and contradictions
Evidence and limits: reported claims, inspected implementation, measurements, conditions, and counterexamples
Value for this topic: the question or section it supports and why it matters
Open questions: missing evidence and what to check next
```

Order reading by dependencies and the current question, for example concepts, mechanisms, implementation, then limitations.

## 4. References and evidence management

### Put citations next to claims

Cite important definitions, implementation details, version support, limits, figures, comparisons, and quotations near the claims they support. Use concise, recognizable source names as links in the text. End with a standalone References section that identifies the main sources by full title, publisher or author, and a direct entry. A source index can carry the detailed reading entries.

Use a recognizable form such as “Python asyncio documentation” or a short name based on the publisher and topic. Differentiate sources with similar names by topic, date, or version. Keep names consistent throughout the report and index. Avoid bare citation numbers, internal record IDs, rendered numeric footnotes, and generic labels as source names.

For several facts from different sources in a paragraph, cite each source where it applies. In tables with different sources by row, add evidence at the appropriate row. Link to the actual document, section, pinned source revision, or verification record. Keep the body and References aligned by short name and link, and list suggested reading separately.

When a link includes a section fragment, verify that the corresponding location exists on the page. A successful page load establishes page access. If the original page has no stable fragment, link to the page and name the relevant section.

### Minimum source entry

| Field | Requirement |
| --- | --- |
| Short name | Recognizable and consistent with the body |
| Full title and responsible party | Actual title and author or institution. Record unknowns |
| Source type | Documentation, code, standard, product page, article, discussion, observation, or another applicable type |
| Location | Original URL or relative local path, with section, page, function, or line as needed |
| Version and date | Applicable version and publication or update date. Mark rolling updates |
| Access date | Actual visit date, distinct from publication |
| Support and limits | Claim supported, key conditions, and unverified details |

Use the order responsible party, full title, source type, version or year, and original location. An institution or project name can stand in for an uncredited individual. Retain fields meaningful to the source type rather than requiring academic bibliographic fields for engineering sources.

A short report can combine the entry and reading note in References. For many sources, maintain full metadata and reading entries in the index and list principal sources in the report. Keep detailed versions, locations, and reading records in one place.

A standalone index includes classification, suggested reading order, formal references, core reading entries, and outstanding checks. Give core sources individual entries with metadata, substantive content, research value, and limits. Several code files can form a reading entry for one bounded call path if their locations remain traceable. Keep source type, verification state, reading depth, and research value distinct. Academic venue rank is unnecessary for general materials. Papers placed in a paper library follow that library's applicable rules.

Illustrative format only:

```markdown
Feature X works under condition Y. See [Publisher, Feature X limits](<original URL and section>).

## References
- Publisher, [Full document title](<original URL and section>), official technical documentation, vX.Y, YYYY-MM-DD

### Full document title
- Responsible party and type: publisher, official technical documentation
- Version and dates: vX.Y, updated YYYY-MM-DD, accessed YYYY-MM-DD
- Original and reading scope: [Full document title](<original URL and section>), Feature X limits section, targeted reading
- Content and mechanism: inputs, state changes, and how condition Y constrains execution
- Analysis and topic value: how related approaches handle Y and what this means for the current choice
- Evidence and limits: actual stated conditions and evidence still missing
```

### Version and timeliness

- Match capabilities, APIs, and system requirements to the target version. Label historical implementations
- For migrations, repository moves, or multiple clients, check which product and version each source describes
- Prefer permanent links pinned to a commit for source claims and record paths and symbols. Note when only a rolling branch or release link exists
- Distinguish publication, update, access, and report cutoff dates. Update the stated scope explicitly if using later changes
- Recheck prices, licenses, quotas, and support windows before using them for an actual decision
- Where versions differ, separate shared conclusions from version-specific ones

### Evidence states and conflicts

Use natural language to indicate the basis of important claims.

| State | Example wording |
| --- | --- |
| Source claim | “The documentation specifies…” or “The vendor states…” |
| Implementation analysis | “Function X at commit Y shows…” |
| Local test | “We observed this with the following environment and input…” |
| Inference | “This mechanism suggests… The remaining check is…” |
| Engineering advice | “Given these conditions, we recommend…” |
| Unverified | “The available sources do not establish…” |

For conflicts, check versions, platforms, terminology, defaults, and methods. Explain the scope of each source and the impact of unresolved differences. A newer statement may describe a different version.

An API description establishes its documented contract. An issue report establishes a reported case. A passing test establishes the outcome under its stated conditions. Scope conclusions to the actual evidence.

Mark quotations and translations, and preserve relevant context. Keep excerpts and screenshots to what the analysis needs, and redact sensitive material before sharing. Generated synthesis or inference needs traceable evidence for factual claims.

## 5. Analysis and report writing

### Report structure

For formal studies of objects or mechanisms, first identify the subjects, scope and easily confused terms, then give a short overview of the overall relationships and main judgments. Address common questions for each object: what it is, how it works, a representative scenario and its capability limits. Compare the objects under the same scenario, then synthesize common ground, key differences and applicable choices to answer the opening questions. Keep evidence, examples and figures beside the explanation they support, and put limits and unknowns where they affect a judgment. Merge or expand sections as the actual questions require rather than filling a fixed set of headings. A knowledge overview may simply answer the questions; add next steps when action advice is needed. Keep References as a separate entry with full entries for major sources, links to the categorized source index and core reading notes, and a separate further-reading list.

Make the reasoning understandable before readers open the links. Synthesize findings across sources. Start the introduction with the short conclusion readers need to judge the subject, keeping conditions and limits close by; put experimental steps, raw numbers and detailed methods in their corresponding body sections. Use tables for quick comparisons on a common basis, with phrases or short sentences in cells; move paragraph-length explanations to nearby prose or lists. Develop the explanation, evidence and necessary qualifications around the central question, and close a long section with its judgment and limits when useful.

### Explain mechanisms

For existing tools, frameworks, and systems, show how the representative implementation works for the question. Identify the entry point, participating objects, where state lives, and how state is updated. Establish the mechanism before developing comparisons and recommendations. Distinguish documentation, source inspection, and tests.

**Question and scenario → components → objects and state → execution or data path → failures and completion → design trade-offs → operating limits.**

As relevant, explain who creates and owns state, who calls whom, how synchronous or asynchronous work completes, how failures propagate, what process or permission boundaries are crossed, and who bears the cost. For code, identify the actual entry, branches, and configuration. Distinguish the public contract, internal implementation, and analyst's model. Leave closed-source details open where evidence is insufficient.

### Compare options

- Define the common task and mandatory conditions before choosing candidates and dimensions
- Use consistent meanings such as native support, plugin support, custom development, unknown, and not applicable
- Choose relevant dimensions from capabilities, API, deployment, compatibility, maintenance, migration, costs, performance, and licensing
- Attach versions, hardware, load, configuration, metrics, and test sources to performance figures. Present results separately where conditions differ
- For scoring, explain scales and weights. Keep unknowns visible and explain changes in recommendation when weights change
- Tie recommendations to scenarios and preconditions. Consider keeping the existing approach when it meets the need

### Explain evolution where it affects the mechanism

For each useful stage, explain the earlier constraint, the change, and its remaining cost, with date evidence. Separate proposal, first release, stable support, and local adoption. Show coexisting approaches where the evidence supports coexistence.

### Mermaid diagrams and LaTeX

Use prose to explain meaning, mechanism, and conditions. Add diagrams for structures, relationships, and processes, and equations for relations that can be formalized. Plan these in the outline and place them together near the relevant discussion in the report. Use consistent names and symbols and explain how the representations correspond.

#### Mermaid diagrams

Use editable `mermaid` fences in Markdown. Use native text diagrams for Feishu delivery where required and retain the editable source. Use diagrams for architecture, dependencies, execution paths, interaction sequences, states, or method relationships. Tables can show parallel attributes and comparisons, and plotting tools are suitable for measured curves.

State in the outline what each important diagram explains. Label objects, arrows, and boundaries. Mark original, adapted, or analytical figures and cite the actual basis. Check syntax, labels, edges, and agreement with the text. Check rendering when the delivery environment supports it and report the actual verification scope.

Determine what each edge actually means before choosing the layout. Flow and relationship diagrams default to top-to-bottom; a true sequence may form one column, while ownership, containment, parallel attributes, optional relationships and branches follow their actual meaning. Do not invent causality or hierarchy to force a vertical layout. Keep node labels to short terms or actions and put fields and parameters in adjacent prose. Split a complex diagram or pair it with a table when useful; use a horizontal comparison when the reading width supports it. Check every edge's meaning and the actual display; if only source is available, state that rendering is unverified.

Distinguish logical layers from process boundaries, and data flow from control flow. Explain uneven evidence coverage instead of implying equivalent coverage through layout.

#### LaTeX expressions

Use LaTeX for inline and display math. Where appropriate, formalize inputs and outputs, state updates, constraints, complexity, error, probability, or cost. Distinguish a cited equation, an equivalent rewrite, and an analytical model. Identify assumptions and source locations.

Explain each symbol on first use and include its domain and units as needed. Use consistent notation across methods and describe differences in assumptions. Explain the math in prose and substantiate its quantities and weights.

Use `$...$` and `$$...$$` in local Markdown. For Feishu, keep a display equation on one physical Markdown line and use `aligned` for multi-line derivations. Render readable equations in the document and use code formatting when discussing the LaTeX syntax itself. Check symbols, scripts, and rendering according to the destination's document standard.

#### Examples and checks

Label commands, configs, and snippets as conceptual, taken from a source, or tested in a specified environment. Before delivery, check whether prose, diagrams, and applicable math explain the core concepts clearly and consistently with the evidence and conditions.

## 6. Verification and implementation boundaries

Document and source reading can establish a mechanism within a stated scope. When practical verification is requested, run the smallest check directly relevant to the question. Treat installation, project changes, testing, and deployment as separate work.

| Item | Record |
| --- | --- |
| Question and hypothesis | What the check should confirm or rule out |
| Environment | Hardware, software, versions, dependencies, configuration, and date |
| Method | Inputs, steps or script, control, and metric |
| Result | Actual outputs, logs, or measurements, including failures |
| Interpretation and boundary | What the result establishes and which settings remain unverified |

For performance or random effects, record repetitions, variation, and aggregation. Distinguish loading, warm-up, and steady state as relevant. Mark checks that were not run and use measured numbers only. Report completion, verification, and implementation as separate states. Follow the project's existing engineering collaboration and approval rules for implementation work.

## 7. Organization and maintenance

### Organize files as needed

Reuse the existing topic location and naming conventions. With bilingual topic names in DreamSoul, carry the same complete prefix into `[Chinese topic] [English topic] 通用调研 General Search.md` and `[Chinese topic] [English topic] 通用调研大纲 General Search Outline.md`. For example, a topic directory called `技能 Skills` uses `技能 Skills 通用调研 General Search.md`. Honor the user's topic naming and the actual scope of any migration.

```text
[Topic]/
├─ [Topic] General Search.md
├─ [Topic] General Search Outline.md  # outline goes in the report when a single short file is requested
├─ Source Index.md                   # many sources
├─ Search Log.md                     # long or complex research or handover
├─ Sources/                          # source files retained for a concrete purpose
└─ Validation/                       # actual verification output
```

Reuse existing index or log names. Add folders, PDF copies, or CSV files when the task needs them.

### Archive sources

- Cite original online locations. Save permitted copies where evidence needs to be fixed, read offline, or protected against important changes
- Keep recognizable attachment titles. Use institution, version, or date when useful and preserve the exact title and origin in the index
- Keep one main copy per content version by default and link it across topics
- Store source material apart from analysis. Label redrawn figures, translations, and excerpts
- Record hashes for fixed evidence or verification outputs where they matter
- Prefer relative links within the collection. Use angle brackets for Markdown destinations with spaces and recheck links when moving or renaming files

Check saved files for type, readability, and agreement with the entry. Preserve the full title in the index when shortening the filename. In the source project, ordinary material paths should generally fit within 240 characters, with actual tooling checked for longer paths. Paper-library PDFs follow the applicable library rules.

### Batch work on existing material

Inventory files, indexes, and broken links. Prepare a mapping of old paths, target paths, and reasons, then check conflicts before acting. Keep existing names and record uncertainty when the title or version cannot be established.

Preserve stable parent directories and useful copies across topics. Identical hashes establish identical bytes. Keep meaningful versions and document their relationship. Check counts, readability, mappings, and links afterward. A repeated run should leave names that are already correct alone.

Evaluate organization and research separately. A usable index and complete files are evidence of organization. Verify technical conclusions separately. Scope new searches and downloads to the actual task. Use the project's paper-library governance for library-wide work.

### Update findings

Revisit affected conclusions after version upgrades, primary-source revisions, changes in project constraints, discoveries of mistakes, or adoption. Set a review schedule appropriate to the source's rate of change.

Record the date, reason, affected sections, and revised findings. Preserve historical conclusions with their valid version. Mark findings for review when central evidence goes unavailable and no replacement exists.

## 8. Delivery checks

Verify that the report answers its core questions, explains mechanisms and conclusions, and gives traceable evidence and applicable conditions. Keep the outline, report, source index, and attachments aligned. Inspect the actual heading tree, required subtopics, and question and evidence notes against the report. Check nearby citations, full References, and core reading entries separately. Verify that the reader can understand the source content, relationships, and reason for using each core source from the report and notes.

Give the first draft enough depth to cover the main branches. Run the evidence and coverage checks in Section 3 and deliver the complete report.

## 9. Reusable task prompt

> Use the General Research Standard to research [topic] for [audience or purpose]. Answer [core questions] within [subjects, scenarios, versions, and constraints] as of [cutoff date]. Read the existing research first and save the deliverables to [location].
>
> Read the applicable project document standard before drafting the outline. Apply the same naming, heading, and layout rules from the outline onward, even when drafting in local Markdown first. Prepare the outline before the report. For a broad topic, show the actual hierarchy and state each section's question, representative evidence, and key unknowns. Use consistent categories and keep subtopics within their parent theme.
>
> Use direct evidence suited to each claim, such as official docs, code, and standards. Explain mechanisms, differences, conditions, and costs. Distinguish source claims, inspected code, inference, and tests. Link recognizable source names near the relevant statements. In References give the responsible party, full title, and direct location. Record the core readings' contents and mechanisms, comparison, research value, limits, version, actual reading scope, and access date. For many sources, keep detailed entries in the index and main references in the report.
>
> Explain concepts in prose, and use editable Mermaid diagrams and justified LaTeX where helpful. Explain how the representations correspond, including symbols, conditions, and evidence. Before delivery, check questions, evidence gaps, heading hierarchy, citations, full references, core reading entries, and required rendering. Include logs and attachments as needed. Ranking papers, downloading PDFs, implementing a solution, and running experiments depend on the task.

## First-draft explanatory depth

A formal mechanism or comparison report should let readers explain relationships, choose an entry point and recognize limits. Align core terms, relevant bilingual names, fields and diagram nodes; explain whether edges mean actions or relationships. Follow one representative scenario through inputs, state changes, observable results and completion criteria. Compare the main routes under the same assumptions and explain limits that change the choice. Place diagrams beside the relevant prose and choose layouts by the actual relationships, without inventing causality or hierarchy to force a vertical path. Split complex diagrams when useful and check the reading width for side-by-side comparisons. Expand key outline questions that remain mere index entries with direct evidence and explanation, rather than padding length or counting figures. Small, explicit queries may remain lightweight.
