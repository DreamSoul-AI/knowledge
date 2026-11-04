## Literature Search
<h4 align="center">
    <p>
        <b>English</b> |
        <a href="README_zh.md">中文</a>
    </p>
</h4>

### Table of Contents

1. [Introduction](#introduction)
2. [Using Google Scholar](#using-google-scholar)
   1. [Search with Keywords](#search-with-keywords)
   2. [Filter Papers](#filter-papers)
3. [Understanding Publication Venues](#understanding-publication-venues)
   1. [Types of Venues](#types-of-venues)
4. [Types of Papers](#types-of-papers)
   1. [Survey Papers](#survey-papers)
   2. [Novelty Papers](#novelty-papers)
5. [Downloading Papers](#downloading-papers)
6. [Organizing Papers](#organizing-papers)
7. [Reproducing Results](#reproducing-results)
8. [Additional Resources](#additional-resources)

---

## Using material, standards and light evidence

For example: “Start from this existing LoRA list, use the supplied literature-review standard, cover 2021–2024, emphasize influential work and show citation counts with their source/date. Return missing candidates and a reading order without renaming existing PDFs.” Read the provided inputs first and state which were available. Domain and output rules remain external; this tutorial does not override the task or project rules.

A short result can use one search note (date, sources, key queries, window and limits) plus a table of paper identity, inclusion value, reading status and citation provenance. No separate log is required. Use original metadata or papers to verify identity; finding a DOI does not establish that the cited claim is supported. Preserve unknown counts and version differences explicitly. Saving, renaming, indexing and reproduction follow the task's scope and the project's current rules.

## Introduction

Conducting a thorough literature search is a fundamental step in academic and professional research. It helps in understanding the existing body of knowledge, identifying gaps, and building on previous work. This tutorial will guide you through the process of finding relevant papers, organizing them effectively, and reproducing key results to deepen your understanding of the field.

---

## Using Google Scholar

### Search with Keywords
- Start with a broad keyword related to your topic of interest.
- Use additional keywords to narrow down the search if necessary.
- Use Ctrl + F to search within an article to find the papers cited by this paper.
- Use "Cited by" and "Search within citing articles" to find follow-up papers.

You can access Google Scholar [here](https://scholar.google.com).

### Citation lookup with Computer Use

For a small number of papers, an available browser/Computer Use tool can search Google Scholar by full title and read “Cited by” from the matching result. Clear the previous query and verify the new one, title, authors and original paper link. Record the observed count, Scholar source link and date in the existing table. Do not use total search hits or add potentially overlapping clusters/citation-only entries. Missing counts stay unknown. A CAPTCHA, rate limit or access block stops the affected lookup; follow the tool's handoff rules rather than bypassing it. This is an optional interactive route when requested or APIs are unavailable, not a bundled browser or a bulk API.

### Filter Papers
- **Number of Citations:** Citation impact is an important signal of influence, especially for foundational work and established methods. Actively seek highly cited papers and show counts prominently with their source and observation date. Assess relevance and contribution alongside impact; account for publication age and field when judging recent work. Unavailable counts are not zero, and overlapping preprint/publication counts must not be added together.
- **Publication Venue:** Prefer papers published in prestigious venues. You can determine the ranking of these venues using [Google Scholar metrics](https://scholar.google.com/citations?view_op=top_venues&hl=en).
- **Publication Time:** Match the time window to the question. New work matters for recent advances, while older highly cited work remains central to foundations and historical context.

---

## Understanding Publication Venues

### Types of Venues

#### Conferences
- Have specific deadlines.
- Papers are peer-reviewed by other authors.
- Notification of acceptance is usually given after about 3 months.
- Accepted papers are presented at a conference, providing networking opportunities.

#### Journals
- Do not have specific deadlines but often have special topics. Journals may periodically issue calls for papers on specific emerging trends.
- Papers undergo an editor's desk review, followed by peer review.
- The review process can take from 6 months to over a year and may involve several rounds of revision.
- In the AI domain, top conferences are preferred over top journals, while in other fields, the reverse is often true.

---

## Types of Papers

### Survey Papers
- Summarize and organize previous research.
- These are ideal starting points to understand a field.
- **Selection emphasis:** Scope and taxonomy quality first; recency, citation impact and venue provide important context. A newer date alone does not make a survey more useful.

### Novelty Papers
- Present new discoveries and can be categorized into theory, method, and application papers. Some papers may touch on two or three factors.
- Some of these papers are often cornerstones of a field, highly cited, and published in prestigious venues.
- **Selection emphasis:** Citation impact carries substantial weight for established contributions, together with relevance, contribution and evidence. Do not impose one fixed ranking across every research purpose.
- For state-of-the-art advancements, the publication date is crucial.

---

## Downloading Papers

- If access to the original source is restricted, search for the paper title and look for alternative sources like [arXiv](https://arxiv.org/).

---

## Organizing Papers

- **Create a Spreadsheet:** A tool to systematically organize and manage your literature collection. To enhance readability and emphasize key concepts, it is recommended to **bold important keywords** throughout the spreadsheet. This can include critical concepts, methods, datasets, evaluation metrics, or any novel contributions. Bolding keywords helps highlight essential information at a glance and makes it easier to quickly reference specific details when revisiting the literature.
  
- **Suggested Columns (sorted by Date):** 

  - **Title:** The title of the paper, which usually reflects the core research question or contribution.

  - **Citation Count:** Display prominently with a source link and observation date. Use an explicit unavailable status when lookup fails, not zero. Do not add overlapping counts for versions of the same work.
  
  - **Authors and optional Institution:** Preserve author identity with title and DOI/arXiv ID. Institutions can add context but do not replace authors or serve as a quality ranking.
  
  - **Venue:** The conference or journal where the paper was published. This can indicate the paper's credibility and impact, as some venues are more prestigious than others.
  
  - **Date:** The publication date of the paper. Sorting by date helps in tracking the chronological evolution of the research topic.
  
  - **Objective:** A summary of the primary goal of the research, detailing the problem the paper addresses.
  
  - **Method:** A brief description of the methodology used in the paper, including any algorithms, models, or theoretical approaches. The method can often be extracted from the abstract.

  - **Novelty:** A summary of what makes the paper unique or innovative compared to previous work. This could be a new approach, a novel application, or a significant improvement on existing methods.
  
  - **Result:** The main contributions of the paper, often highlighting how well the method performed according to the chosen metrics. The contributions can be extracted from the abstract, introduction, and conclusion sections.
  
  - **Dataset:** The dataset used in the research, which is crucial for establishing a standard benchmark to compare against baselines.

  - **Metric:** The evaluation metrics used to assess the performance of the proposed method, such as Accuracy and F1 score.
  
  - **Link:** A URL to access the paper online, whether through the publisher's website, arXiv, or other repositories.
  
  - **Code:** A link to any code repository (e.g., GitHub) associated with the paper. Having access to the code can be invaluable for reproducing results or building on the work.

---

## Reproducing Results

The following are optional follow-up ideas for a separately requested reproduction task, not automatic steps of a literature search.

- Select a foundational paper to reproduce its results, preferably one with available implementation.
- Try to find benchmark code bases that include old baseline papers.
- Use this process to deepen your understanding of the field and brainstorm new ideas.

---

## Additional Resources

- **Conference Deadlines:** Use websites like [AI Deadlines](https://aideadlin.es/) to track important dates.
- **GitHub Repositories:** Look for "Awesome [Topic name]" repositories for curated lists of important papers. There are also benchmark repositories for a particular field.
- **Papers with Code:** A website that gathers leaderboards, data, code, and papers for various topics. Access it [here](https://paperswithcode.com/).
- **Paper Reading Tutorial:** For guidance on how to effectively read and analyze academic papers, refer to this [Paper Reading Tutorial](https://github.com/DreamSoul-AI/knowledge/blob/main/skills/paper-analysis/references/README.md).
