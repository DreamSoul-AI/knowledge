---
name: git-workflow
description: Inspect and operate Git repositories for branching, commits, synchronization, merges, remotes, and recovery. Use when a task requires changing or diagnosing repository state; do not trigger for general Git explanations alone.
---

# Git Workflow

Inspect the repository before choosing a command. Determine the current branch,
working-tree changes, remotes, and relevant history. Preserve unrelated user
changes and follow repository-local instructions.

## Workflow

1. Translate the requested outcome into the smallest Git operation that achieves it.
2. Check status and the exact refs or paths involved before changing state.
3. Prefer non-interactive commands and recoverable operations.
4. Verify the resulting branch, worktree, or history after the operation.
5. Report what changed and identify anything intentionally left uncommitted or unpushed.

Do not discard changes, rewrite shared history, force-push, delete branches, or
remove untracked files without explicit authorization. Do not treat permission
to commit as permission to push. Consult the human-oriented [Git Wiki guide](../../wiki/git/README.md)
only when background explanation is useful.
