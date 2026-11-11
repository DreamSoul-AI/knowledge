# Research Planning

**English** | [中文](README_zh.md)

Use this guide to turn an initial idea into a scientific study plan, including
literature-only, theoretical, reproduction, method, benchmark, and system studies.
The sections are prompts to adapt, combine, or shorten. Keep sources authentic,
describe what was actually done, and support conclusions with traceable evidence.
AI checks should identify consequential gaps, not block progress because fields
remain empty. Choose the detail and precision for the research question.

## From inspiration to research outputs

### Where to start

**Inspiration can strike at any moment in everyday life.** A conversation, a
small frustration, or a surprise can be a starting point. Note what happened,
what caught your attention, and what you want to understand. An idea that comes
up later can enter at the step where it matters.

An agent should also look for leads while browsing, listening to people describe
their experiences, or examining research evidence. When an observation, conflict,
or connection stands out, propose an initial question, explain where it came
from, and suggest a first check.

### How research progresses

![Research flow from an initial question to an output. Thought experiments and empirical experiments both feed into analysis. A research gap can prompt a rephrased question. From the conclusion, revisit the literature, revise the question or hypothesis, or add experiments.](research-flow-en.png)

[Open the diagram](research-flow-en.png) · [View the SVG source](research-flow-en.svg)

1. **Review existing evidence and define the research question.** Check the
   literature and previous experiments. If the evidence answers the initial
   question, state the answer and where it applies. If a worthwhile gap remains,
   narrow it into a research question you can investigate.
2. **Plan the test and draw a conclusion.** State what would support or challenge
   the hypothesis. Choose a thought experiment or an empirical experiment, or
   use both in parallel or in sequence. An exploratory study can gather evidence
   before forming a hypothesis. Explain what the evidence supports and what
   remains uncertain.
3. **Turn the conclusion into an output.** Put the conclusion and its evidence
   in a paper, a research report, or code with a record of how it was verified.
   If you pause the study, keep its results and open questions.

### When to go back

- **Reframe the question.** If the current question reveals no worthwhile gap
  but the observation still calls for an explanation, try a different angle.
- **Revisit the literature.** Go back when you find overlooked work or when a
  result conflicts with prior findings.
- **Revise the question.** Refine the scope when it is too broad or when the
  evidence points to a more specific question.
- **Revise the hypothesis.** Reconsider the explanation when you find a
  counterexample or a better explanation.
- **Add experiments.** Return to the design when the evidence cannot distinguish
  competing explanations or the measurements need improvement.

When you go back, note what prompted the change and what to check next. Steps can
be combined or expanded, and several lines of inquiry can run in parallel or in
sequence.

For an existing study, start with its current plan and applicable standards. The
user may also supply literature reviews, paper analyses, prior results, and resource
constraints. Trace decisive claims back to the paper, configuration, or run record.
Focus additional reading on gaps that affect the decision. Preserve confirmed
priorities and distinguish completed work, remaining work, and proposed changes.

## Connect the six aspects

| Aspect | Planning decision |
| --- | --- |
| Literature | What is known, disputed, or missing? Extract source locations and each core work's data, model, algorithm, metrics, experimental conditions, and limitations. |
| Data | What is observed, from where, under what permissions and distribution? Define preprocessing, labels, splits, versions, and leakage checks. |
| Model | What represents the object? Define assumptions, interfaces, parameters/state, initialization, versions, and baselines. |
| Algorithm | What procedure changes the result? Define steps, objective, change from baseline, hyperparameters, randomness, stopping, and cost. |
| Metrics | What would count as improvement? Define primary outcomes, constraints, units, aggregation, measurement conditions, uncertainty, and thresholds with their basis. |
| Experiments | Which comparison addresses which hypothesis? Define treatments, controls, confounders, repetitions, analysis, costs, and interpretation. |

Literature supports all five technical choices; experiments must measure the
claimed improvement within the stated data and model conditions. Design choices
can change conclusions, as reviewed by Gundersen et al. [4]. Do not rank results
from different protocols as if they were controlled comparisons.

For literature-only work, compare evidence and identify missing validation. For
theory, specify problem instances, mathematical assumptions, proofs,
counterexamples, or complexity/error bounds. Omit details that do not apply.

## Select experiments and allocate resources

Start with a small correctness check and necessary baseline verification before
costly runs. Select main comparisons, ablations, robustness checks, and failure
analysis for the actual claim; not every study needs every type.

Prefer the authors' official implementation and configuration. Record its source,
version or commit, license, and meaningful adaptations. If unavailable, summarize
where you looked and label the alternative implementation. A representative
reproduction of the main results or trends is usually sufficient to establish a
baseline; exact agreement and rerunning the entire paper are not universal gates.
Investigate gaps that could change the conclusion. State whether you evaluated
released weights or also ran training or the method's generation procedure.
Choose key ablations, starting simply where useful, and explain differences in
coverage, intervention location, or protocol. Preserve the sources of key numbers.

- **DOE:** use randomization, blocking, and full or fractional factorial designs
  as appropriate to estimate factor effects and interactions; record confounding.
- **OR:** formulate experiment choice, resource allocation, or scheduling with
  decision variables, objectives, and constraints. Simulation optimization
  includes ranking and selection and evaluation-budget allocation [5].
- **BO:** for expensive black-box evaluations, use observed trials to choose the
  next configuration. Specify the search space, initial trials, surrogate,
  acquisition, noise/cost handling, budget, and stopping [6].
- **Bayesian experimental design:** choose designs by expected utility, which
  can express information or decision value. State prior assumptions, the
  observation model, utility, and constraints [7].

Optimization seeks good configurations; a scientific comparison tests a claim.
Document adaptive trials and budget fairness, and independently evaluate chosen
settings. Specify statistical handling when adaptive sampling, repeated looks,
or multiple comparisons affect inference. Preserve failed and negative runs.

## Copyable plan template

Fill consequential unknowns explicitly. Select a format appropriate to the
project; combine or skip sections as useful, retaining the relevant connections.

```markdown
# Inspiration
Idea or observation, source, trigger conditions, preliminary question, value.

# Literature
Search scope/date/criteria; core sources and reading depth.
For each core work: question, data/model, algorithm, metrics/controls, result,
limitations, source location, and relevance. Route and baseline rationale.
Decision on the initial idea: continue, revise, already addressed, or defer.

# Research question and hypothesis
Object, conditions, gap, nearest work, contribution and scope.
Mechanism or exploratory question; supporting and contrary predictions.
How the six aspects jointly answer the question.

# Data
Provenance, use rights, version, observation unit, size/distribution, labels.
Preprocessing, exclusion rules, splits/isolation, quality and leakage checks.

# Model
Representation/assumptions, inputs/outputs, parameters/state, initialization.
Version and baselines; fixed and varied components.

# Algorithm
Steps or equations, baseline change, objective, hyperparameters and search.
Randomness, state updates, cost, stopping and failure conditions.
Prefer official code; note source/version, adaptations, and implementation type.

# Metrics
Primary outcome and constraints: definition, unit/direction, aggregation,
measurement implementation/conditions, uncertainty and decision criteria.

# Experimental design
For each experiment: question, treatment/control, varied/fixed conditions,
data, metrics, repetition/analysis, budget, and interpretation.
For decisive comparisons, state which results would support the hypothesis,
count against it, or leave it unresolved.
Small checks, baseline readiness, tuning/test separation, confounders.
Representative reproduction: main target/trend, source, key conditions,
observed gap and next step. Numerical tolerances only where the claim needs them.
If useful: DOE factors; OR variables/objective/constraints; BO space/surrogate/
acquisition/initial trials/noise/budget; Bayesian design prior/model/utility.
Adaptive search history, independent validation, execution and stopping rules.
Owner, time/resource constraints, and unresolved dependencies.

# Execution and conclusions
Actual run IDs and versioned configurations, environment, commands, artifacts.
Results/variation, failures, hypothesis assessment and generalization limits.
New questions; dated protocol amendments and affected evidence.
```

## Use in GitHub projects

Save the plan at an existing documentation location, for example
`docs/research-plan.md`, and link it from the README. Inspiration can start in an
exploration issue. After literature review, link implementation and experiment
issues to the plan's question and validation. PRs link actual checks and results.
Preserve the repository's layers, configuration, and artifact tools.

Retain enough version, configuration, environment, command, and result information
to revisit important runs. Scale the recording detail to the study and separate
plans from actual results. Do not commit private data or internal document links
into a public plan.

## Methodological sources

These sources support the component practices; the six-aspect organization is a
planning convention. Clinical-specific requirements in [1] are not universal AI
requirements. Sources were checked on 2026-10-14 at relevant sections or abstracts.

1. Ackermann and the AGA Research Committee (2024). [From the idea to the research question and hypothesis](https://doi.org/10.1007/s00142-024-00682-x). *Arthroskopie*, 37, 232–237. Idea, literature, question, and hypothesis sections.
2. Cohen and Howe (1988). [How Evaluation Guides AI Research: The Message Still Counts More than the Medium](https://paulrcohen.github.io/papers/952-949-1-PB.pdf). *AI Magazine*, 9(4). Research stages and evaluation feedback.
3. Forde and Paganini (2019). [The Scientific Method in the Science of Machine Learning](https://arxiv.org/abs/1904.10922). arXiv position paper. Hypothesis testing and uncertainty.
4. Gundersen, Coakley, Kirkpatrick, and Gil (2022). [Sources of Irreproducibility in Machine Learning: A Review](https://arxiv.org/html/2204.07610v2). arXiv review, sections 4–9. Design, algorithms, observations, evaluation, and documentation.
5. Amaran, Sahinidis, Sharda, and Bury (2016). [Simulation optimization: a review of algorithms and applications](https://doi.org/10.1007/s10479-015-2019-x). *Annals of Operations Research*, 240, 351–380. Simulation optimization, ranking/selection, and budget allocation.
6. Frazier (2018). [A Tutorial on Bayesian Optimization](https://arxiv.org/abs/1807.02811). arXiv tutorial. Surrogate models, acquisition functions, and expensive evaluations.
7. Chaloner and Verdinelli (1995). [Bayesian Experimental Design: A Review](https://doi.org/10.1214/ss/1177009939). *Statistical Science*, 10(3), 273–304. Decision theory and expected utility.
