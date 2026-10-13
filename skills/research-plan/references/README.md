# Research Planning

**English** | [中文](README_zh.md)

Use this guide to turn an initial idea into a scientific study plan, including
literature-only, theoretical, reproduction, method, benchmark, and system studies.

## From inspiration to evidence

**Inspiration → literature review → research question and hypothesis → coordinated
data, model, algorithm, metric, and experiment choices → execution and analysis →
conclusions and new ideas.**

An inspiration may be an anomaly, practical difficulty, conjecture, or question
about an existing explanation. Record its origin and use a preliminary question
to search. Literature then helps refine the question, assess novelty, identify
alternatives, and decide whether to continue, revise, or set the idea aside.
Ideas can also emerge from reading and experiments. This is an iterative working
convention rather than a universal fixed order. Ackermann et al. [1] discuss the
idea-to-question transition; Cohen and Howe [2] discuss evaluation throughout AI
research; Forde and Paganini [3] emphasize hypothesis testing and uncertainty.

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
counterexamples, or complexity/error bounds. Justify adaptations to each aspect.

## Select experiments and allocate resources

Start with a small correctness check and necessary baseline verification before
costly runs. Select main comparisons, ablations, robustness checks, and failure
analysis for the actual claim; not every study needs every type.

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
project; retain the logical connections if sections are combined.

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

# Metrics
Primary outcome and constraints: definition, unit/direction, aggregation,
measurement implementation/conditions, uncertainty and decision criteria.

# Experimental design
For each experiment: question, treatment/control, varied/fixed conditions,
data, metrics, repetition/analysis, budget, and interpretation.
Small checks, baseline readiness, tuning/test separation, confounders.
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

For formal runs retain code commit and uncommitted differences, data/split and
model versions, configuration, dependencies/hardware, randomness, command,
status, raw results, and artifact locations. Record plan changes separately from
execution state. Do not commit private data or internal document links into a
public plan.

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
