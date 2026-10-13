---
name: research-plan
description: Create or review scientific research plans from an initial idea through literature, research questions, hypotheses, and coordinated data, model, algorithm, metric, and experiment choices. Use for study planning and experiment protocols, not solely for paper discovery, paper analysis, or implementing an already-defined experiment.
---

# Research Plan

Turn an idea into a plan whose evidence and experiments can support, refute, or
leave its hypotheses unresolved. Read the existing plan, relevant project
constraints, and implementation before changing them. Preserve the user's scope:
planning alone does not authorize training, data collection, publishing, or
external repository changes.

## Workflow

1. Record the inspiration: an observation, practical difficulty, conjecture, or
   disagreement with an explanation. Capture its source and a preliminary
   question without assuming novelty or feasibility.
2. Review relevant literature and competing explanations. Extract the data,
   models, algorithms, metrics, and validation conditions of decisive work.
   State the search scope, actual reading depth, and unresolved evidence gaps.
3. Refine the research question, scope, contribution, and mechanism hypothesis.
   Identify observations that would count against it. Exploratory studies may
   start with questions; distinguish hypothesis discovery from later testing.
4. Coordinate the six aspects below. They are planning dimensions, not an
   irreversible sequence. Revisit earlier choices when evidence changes them.
5. Define the smallest informative validation plan, resource needs, decision
   criteria, and execution order. Leave consequential unknowns explicit rather
   than inventing budgets, owners, dates, thresholds, or results.
6. Deliver or update the plan in the requested format. For execution follow-up,
   compare actual runs with the protocol, retain failures and negative results,
   and record amendments, conclusion boundaries, and new questions.

## Six connected aspects

| Aspect | Required connection to the research question |
| --- | --- |
| Literature | Evidence for the gap, candidate route, nearest work, baselines, and alternative explanations; preserve source locations and comparison conditions. |
| Data | Observation unit, provenance, version, permitted use, preprocessing, labels, split isolation, leakage risks, and the population to which conclusions apply. |
| Model | Representation, assumptions, inputs/outputs, parameters or state, initialization/version, fixed parts, and model baselines. |
| Algorithm | Training, inference, or solution steps; the specific change from baseline, objective, search settings, randomness, stopping rule, and cost. |
| Metrics | Primary outcome and necessary quality/resource constraints, definitions, units, direction, aggregation, implementation, uncertainty, and decision criteria. |
| Experiments | Which comparison tests which claim; interventions, controls, confounders, data, repetitions, analysis, budget, and possible interpretations. |

Literature informs all five technical choices. Data bounds the object of study,
models represent it, algorithms operate on it, metrics operationalize the goal,
and experiments connect observations to the question. Record model, data, and
algorithm changes separately so their effects are not silently conflated.

Require an explicit response to each aspect, allowing justified adaptations:
literature-only work compares reported evidence and proposes validation without
claiming it ran; theory can use assumptions, proofs, counterexamples, and bounds
instead of training data or experiments.

## Experiment choices

Choose methods for the scientific objective, not to fill a checklist:

- Use statistical design of experiments (DOE) for factor effects and interactions
  when appropriate; specify randomization/blocking and confounding limits.
- Use operations research (OR) when experiment selection, budget allocation,
  ranking and selection, or scheduling is itself a decision problem. State
  decision variables, objectives, constraints, and the proposed solver.
- Use Bayesian optimization (BO) when evaluations are expensive and the target
  is a suitable black box. Record the search space, initial evaluations,
  surrogate, acquisition rule, noise/cost treatment, budget, and stopping rule.
- Use Bayesian experimental design when selecting experiments by expected
  information or decision utility; state the prior, observation model, and utility.

Separate searching for good settings from testing a mechanism. Keep model
selection on development data and reserve independent evaluation for the chosen
protocol. Retain adaptive search histories, specify comparable tuning/resource
budgets, and account for repeated looks or comparisons when they affect inference.
Do not interpret the best search observation as independent confirmation.

Select repetitions and statistical analysis from effect size, variability,
independent observation units, and available resources, not a universal run count.
Distinguish author-reported results, implementation inspection, and actual runs.

## Repository use and references

Follow the repository's existing structure. A plan can live in
`docs/research-plan.md`, linked from the README. Connect inspiration notes to
study questions, implementation/experiment issues, configurations, and PR
evidence only when those actions are requested. For each formal run record code
and uncommitted differences, data/split and model versions, configuration,
environment, randomness, command, status, and raw artifact locations.

Read the [English guide and template](references/README.md) or
[Chinese guide and template](references/README_zh.md) when drafting a full plan,
reviewing method choices, or needing the methodological sources. These are
self-contained; adjacent skills are optional, not installation dependencies.
