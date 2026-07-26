# Contributing

## Workflow

1. Select one ready task from `codex/tasks/tasks.json`.
2. Create a short-lived branch named `<task-id>-<short-description>`.
3. Implement only the selected task.
4. Add or update tests and documentation.
5. Run `make check` or every currently available equivalent.
6. Open a pull request using `.github/pull_request_template.md`.
7. Resolve review comments and required checks before merge.

## Pull-request expectations

- One atomic outcome.
- Clear acceptance criteria.
- No unrelated refactoring.
- Security and tenant-isolation impacts identified.
- Prompt and retrieval changes include evaluation evidence.
- Database changes include migrations and rollback considerations.
