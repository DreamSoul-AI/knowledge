# Paper Reading

<h4 align="center">
    <p>
        <b>English</b> |
        <a href="README_zh.md">中文</a>
    </p>
</h4>

## Table of Contents
- [Optional inputs and reading record](#optional-inputs-and-reading-record)
- [Contribution and research infrastructure](#contribution-and-research-infrastructure)
- [Adapt analysis to the material](#adapt-analysis-to-the-material)
- [Scholar lookup and technical expression](#scholar-lookup-and-technical-expression)

1. [Introduction](#introduction)
2. [Understanding the Structure of a Paper](#understanding-the-structure-of-a-paper)
    - [Title and Abstract](#title-and-abstract)
    - [Introduction](#introduction-1)
    - [Related Work](#related-work)
    - [Methodology](#methodology)
    - [Experiments and Results](#experiments-and-results)
    - [Conclusion](#conclusion)
    - [References](#references)
3. [Effective Reading Strategies](#effective-reading-strategies)
    - [Skimming](#skimming)
    - [Targeted Reading](#targeted-reading)
    - [In-Depth Reading](#in-depth-reading)
4. [Taking Notes and Highlighting](#taking-notes-and-highlighting)
    - [Annotating the Paper](#annotating-the-paper)
    - [Summarizing Key Points](#summarizing-key-points)
5. [Connecting the Paper to Existing Literature](#connecting-the-paper-to-existing-literature)
    - [Commonalities and Distinctions](#commonalities-and-distinctions)
    - [Fitting into a Taxonomy](#fitting-into-a-taxonomy)
6. [Connecting the Paper to Your Work](#connecting-the-paper-to-your-work)
    - [Relating to Your Research](#relating-to-your-research)
    - [Citing the Paper](#citing-the-paper)
7. [Saving Papers](#saving-papers)
    - [Directory Structure](#directory-structure)
    - [File Naming](#file-naming)
8. [Next Steps](#next-steps)


---

## Optional inputs and reading record

A paper or source link is enough to start. Optionally supply research plans/questions, prior notes, appendices, code or an analysis standard. For example: “Analyze this paper with the attached research plan and reading standard, focusing on which baselines we should compare; save only a local note.” Use the available inputs and state assumptions without demanding a fixed form. Missing supplementary material limits the corresponding conclusions, not every independent part of the analysis.

Record paper identity, stable source, publication status/date, the actual version read, reading date and later update date/scope. A code revision matters only if code is actually examined. Record elapsed time only when measured. List the actual sections/pages/figures inspected and uncovered material. Metadata, abstract screening, targeted reading, deep reading and reproduction are different evidence depths. For an unversioned post, record visible publication/update and access dates; unknown dates stay unknown.

## Contribution and research infrastructure

Keep the original research question → claimed contribution → method → evidence → critical assessment → relationship to existing/user work structure. **Research infrastructure here means data, model, algorithm and metric**, connected to the contribution and results:

| Component | Questions to answer when applicable |
| --- | --- |
| Contribution | What is claimed as new, relative to which closest work, and what evidence supports it? |
| Data | What source, task, construction/annotation, scale, splits and preprocessing were used? What leakage or coverage limits matter? |
| Model | What architecture/base model, checkpoint or scale, component roles and trainable/frozen parts are used? |
| Algorithm | What inputs, outputs, steps, objective, assumptions and key mechanisms connect the data and model? |
| Metric and evidence | How are metrics defined/aggregated? Under which protocol, baseline settings and conditions are results, ablations and uncertainty reported? |

Tie each important result to those conditions. Hardware/runtime context belongs where needed to interpret a specific claim. Distinguish not applicable, not reported and inaccessible material. Retain code/data availability and reproducibility limitations without running training or modifying a library unless requested.

For a consequential claim, concise prose or columns **Claim / Source position and observation / Conditions / Assessment** suffice. Separate authors' claims, your inference and any checks actually performed. “Not reported” does not mean “not done.” Do not require a score, an acceptance decision, a fixed number of strengths/weaknesses or a separate evidence database.

## Adapt analysis to the material

Theory, method and application can overlap. System/infrastructure, data/benchmark, survey/review and position contributions are also supported. Keep publication/source form separate: a blog may explain a method or advocate a position; establish its actual status and evidence.

| Material | Main focus |
| --- | --- |
| Theory | Objects, assumptions, propositions, derivations, counterexamples and applicability |
| Method / Application | Mechanism, scientific components, evaluation and limits of the target setting |
| System | Design/interfaces, scientific components and workload-dependent performance claims |
| Data / Benchmark | Collection, annotation, splits, leakage, coverage/bias, task/metric protocol, baselines and license |
| Survey / Review | Scope/cutoff, inclusion basis, taxonomy, coverage gaps and supported synthesis |
| Position / Perspective | Thesis, argument chain, factual evidence, alternatives and testable implications |
| Blog / Technical post | Author/date/version and source status, then the relevant method, argument or tutorial evidence |

Expand applicable content rather than forcing every work to have experiments or fabricated metrics.

## Scholar lookup and technical expression

When useful, use authoritative sources to identify the formal publication/version or related work. An available Computer Use/browser tool can query Google Scholar by full title, replacing the previous query and verifying authors and the original link. Report citation counts with source/date, do not sum overlapping clusters, and keep unknown counts explicit. Reused observations retain their original dates. Stop on CAPTCHA/rate limit/access block and follow the tool's handoff rules without bypassing restrictions. This limited interactive route does not bundle a browser or replace original-source reading, and reference exploration stays within the current question.

Use LaTeX for formulas, define symbols/dimensions/assumptions and distinguish original equations, rewrites and your abstractions. Where helpful, pair prose with editable Mermaid and applicable formulas for the same mechanism. Check consistency and rendering when supported, disclose unverified work and never invent equations for a nonmathematical argument. The following tutorial remains optional background; follow the current task's saving, naming and output rules.

## Introduction

This tutorial will guide you through the process of reading academic papers effectively. Reading papers is a critical skill for researchers, students, and professionals in academia. By the end of this tutorial, you'll know how to approach papers systematically, extract key information, and critically analyze the content.

## Understanding the Structure of a Paper

Academic papers generally follow a structured format, which helps in navigating and understanding the content.

### Title and Abstract

- **Title**: Gives a concise indication of the paper's focus.
- **Abstract**: A summary of the entire paper, including the problem addressed, methods used, results obtained, and the conclusion. The abstract generally has three parts: 1) background, 2) a one-line summary of the work (usually beginning with "In this work, ..."), and 3) the achievements of this work, which usually include theoretical or experimental highlights. It’s essential to read this to get a quick overview of the paper.

### Introduction

- **Purpose**: Introduces the problem, why it’s important, and the scope of the research. It also usually contains a brief outline of the paper. The introduction should add motivation and the contributions of the paper before outlining its structure.
- **What to Look For**: The motivation behind the research, the research question, objectives, and contributions (often listed as bullet points).

### Related Work

- **Purpose**: Reviews existing literature and positions the paper within the current body of knowledge.
- **What to Look For**: Examine how the paper differentiates itself from previous work, including its connections and commonalities with existing literature, as well as the problems identified in prior research. The related work section is often organized chronologically. Additionally, focus on the differences between the proposed work and existing work.

### Methodology

- **Purpose**: Describes the methods and approaches used to address the research question.
- **What to Look For**: The problem formulation, method formulation (including algorithms and models), and discussions on key aspects of the method. Understanding the methodology is crucial for evaluating the validity of the research.

### Experiments and Results

- **Purpose**: Presents the data obtained from the experiments and analyzes the results.
- **What to Look For**: Key findings, data presented in figures or tables, and statistical significance. Focus on whether the experimental setup is clean and well-established (e.g., convergence, baselines). Evaluate if the results support the claims made by the authors and whether ablation studies help in understanding the contribution of each detail in the method. Look for results that justify the claims, the novelty and significance of the method, and any insights into how the author may have conceived the idea.

### Conclusion

- **Purpose**: Summarizes the findings, discusses implications, and suggests future research directions.
- **What to Look For**: The main takeaways from the paper and any recommendations for future work.

### References

- **Purpose**: Lists the scholarly work cited in the paper.
- **What to Look For**: Key papers that influenced the research and sources you might want to explore for further reading.

## Effective Reading Strategies

Reading a paper effectively involves different strategies depending on your purpose.

### Skimming

- **When to Use**: When you need to quickly decide if a paper is relevant to your work.
- **How to Do It**: 
    - Read the title, abstract, and conclusion.
    - Glance through the headings and subheadings.
    - Look at the figures and tables to get a sense of the results.
    - Pay particular attention to diagrams that illustrate the motivation and method.

### Targeted Reading

- **When to Use**: When you want a better understanding of the field or to grasp the motivation and contribution of the paper without reading it entirely.
- **How to Do It**: 
    - Read the introduction and related work sections.
    - Focus on the formulations in the methodology section.
    - Review the key results in the experimental section.

### In-Depth Reading

- **When to Use**: When you need to thoroughly understand a paper.
- **How to Do It**: 
    - Read the entire paper carefully.
    - Take notes and highlight important sections.
    - Pause after each section to summarize in your own words what you've understood.
    - Be critical and curious. Look for hidden facts and ask crucial questions that may intrigue future work.

## Taking Notes and Highlighting

Taking notes while reading helps in retaining information and makes it easier to refer back to important points.

### Annotating the Paper

- **How to Do It**: 
    - Use a PDF reader that allows you to highlight text and add comments.
    - Mark sections that are particularly important or complex.
    - Write brief notes in the margins to summarize points or raise questions.

### Summarizing Key Points

- **How to Do It**:
    - After reading each section, write a brief summary of the key points.
    - Note down any questions or thoughts that arise.
    - Summaries should include the problem, method, key results, and the significance of the research.

## Connecting the Paper to Existing Literature

Relating the paper to existing literature is essential for understanding its place within the field and its relevance to ongoing research.

### Commonalities and Distinctions

- **How to Do It**: 
    - Identify commonalities between the paper and previous works.
    - Highlight the distinctions that set the paper apart, focusing on the differences in methodology, findings, or conclusions.

### Fitting into a Taxonomy

- **How to Do It**: 
    - Try to fit the paper into a proper taxonomy of the field.
    - Determine where the paper stands in relation to other key works and how it contributes to the development of the field.

## Connecting the Paper to Your Work

Relating the paper to your research is crucial for understanding its relevance and potential impact.

### Relating to Your Research

- **How to Do It**:
    - Consider how the paper’s findings relate to your own research questions.
    - Identify any methods or approaches that could be applied to your work.
    - Think about how the paper influences or changes your understanding of the topic.

### Citing the Paper

- **How to Do It**:
    - If you plan to reference the paper in your work, make sure to record the citation in a reference manager using BibTeX format.
    - Find the citation for the original publication venue if an arXiv version exists.
    - Note down specific sections or figures you might want to cite.

## Saving Papers

Saving, renaming and indexing are separate actions governed by the current task and existing library rules. The examples below are optional for a new collection, not instructions to reorganize an existing one.

Properly organizing and saving academic papers is essential for easy retrieval and reference.

### Directory Structure

- **Project-Based Folders**: Organize papers within project-specific directories. For a single project, create a folder named after the project (e.g., `project_name/doc/paper_name.pdf`). If the project involves multiple tasks or topics, organize them further by topic name (e.g., `project_name/doc/topic_name/paper_name.pdf`).

### File Naming

- **Formatting the Filename**: The filename should be the formatted title of the paper. You can usually access the correct paper title from the arXiv or the original publication page, avoiding directly copying it from the PDF.

- **Including Publication Date**: It's helpful, though optional, to include the publication year in the filename, such as `[2020] paper_name.pdf`. This will help in organizing papers chronologically.

## Next Steps

The following are optional follow-up ideas, not automatic actions or permission to share, run experiments or broaden the search:

- **Discuss with Peers**: Share insights or questions with colleagues to deepen understanding.
- **Explore References**: Follow the cited works to expand your knowledge on the topic.
- **Apply to Your Work**: Use the insights gained to inform your research, experiments, or writing.
- **Organize into Literature Summary**: Consider organizing the paper into a literature summary with other works in the field.
