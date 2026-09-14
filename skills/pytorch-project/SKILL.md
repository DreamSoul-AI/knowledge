---
name: pytorch-project
description: Build, train, evaluate, and troubleshoot reproducible PyTorch projects. Use for tensor/device problems, data pipelines, model training, checkpoints, evaluation, or experiment reproducibility; not for framework-neutral machine-learning questions.
---

# PyTorch Project

Inspect the existing project and runtime before changing code. Confirm tensor
shape, dtype, device, and batch semantics at component boundaries.

## Workflow

1. Detect the available backend and use CPU fallback unless hardware is a requirement.
2. Keep data loading, model definition, training, validation, and evaluation separable.
3. Make randomness, preprocessing, splits, metrics, and configuration reproducible.
4. Use training/evaluation modes and gradient contexts correctly.
5. Save enough checkpoint state to resume the requested workflow reliably.
6. Verify with a small batch or short run before launching expensive training.

For failures, isolate environment compatibility, data, shape/device, numerical
stability, memory, and optimization causes instead of changing several variables
at once. Record experiment assumptions with the shared
[experiment template](../../templates/experiment-record.md). The
[PyTorch Wiki guide](../../wiki/pytorch/README.md) provides introductory context.
