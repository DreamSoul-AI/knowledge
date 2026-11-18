# Codex Experiment

Turn a short question about Codex behavior into an executed, observable experiment. Use for mechanism probes, prompt or configuration effects, tool behavior and working methods. The agent chooses and runs the experiment without requiring the user to supply a protocol.

## Use

Install the entire `codex-experiment` directory, keeping `SKILL.md`, `agents/` and `references/` together. The actual environment must provide authentication and relevant tools.

```text
Use $codex-experiment to test whether CLI structured output also constrains files written by tools. Run it and explain the evidence and conclusion.
```

Optional inputs include existing material, the target surface, permitted operations and budget. Ask only for consequential missing information. Choose direct probes, before-and-after checks or grouped comparisons as appropriate; use isolated test sessions when independent context matters.

## Results

For a simple question, deliver the conclusion, observations and applicable conditions directly. Save a short record, necessary evidence and scripts in the project's existing location when review or reproduction warrants it. Distinguish mechanism, permission and configuration failures from model performance. Collect CLI and desktop evidence separately.

Use synthetic or permitted inputs and preserve business data and persistent configuration by default. External writes, cleanup and publication remain subject to the current authorization. A limited sample does not establish behavior across every model or setting.

See the [execution reference](execution.md) for conditional technical guidance. Use the applicable research workflow for a full scientific study and the development workflow for maintaining skill implementations.
