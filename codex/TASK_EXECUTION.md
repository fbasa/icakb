# Codex Task Execution

## Input

A task ID such as `P2-019`.

## Procedure

1. Locate the task in `codex/tasks/tasks.json`.
2. Verify dependencies are complete or explicitly waived by the user.
3. Read `AGENTS.md`, architecture constraints, and the phase exit gate.
4. Inspect the smallest relevant code and documentation surface.
5. Implement the minimum complete change.
6. Add positive, negative, and boundary tests where applicable.
7. Run focused checks, then the repository check command.
8. Update documentation, task status, and changelog when required.
9. Produce the completion report below.

## Completion report

```text
Task:
Outcome:
Files changed:
Tests and checks:
Security and tenancy:
Observability and operations:
Documentation:
Known limitations:
Follow-up tasks:
```

## Stop conditions

Stop and report rather than guessing when a task requires an unavailable secret, an unapproved production-data operation, a destructive external action, or a decision that contradicts an accepted ADR.
