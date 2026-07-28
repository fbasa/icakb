# Codex Task Execution

## Input

A task ID such as `P2-019`.

## Procedure

1. Locate the task in `codex/tasks/tasks.json`.
2. Verify dependencies are complete or explicitly waived by the user.
3. Treat `PHASE-N-EXIT` as incomplete until the preceding exit gate has recorded evidence.
4. For Phase 1, verify the [Phase 0 audit](../docs/PHASE_0_AUDIT.md); stop while its verdict is `FAIL`.
5. Read `AGENTS.md`, architecture constraints, and the phase exit gate.
6. Inspect the smallest relevant code and documentation surface.
7. Implement the minimum complete change.
8. Add positive, negative, and boundary tests where applicable.
9. Run focused checks, then the repository check command.
10. Update documentation, task status, and changelog when required.
11. Produce the completion report below.

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
