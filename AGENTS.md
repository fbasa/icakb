# AGENTS.md

These instructions apply to Codex and all automated or human coding agents working in this repository.

## Required reading

Before changing files, read:

1. `docs/ARCHITECTURE.md`
2. `docs/ENGINEERING_FOUNDATION.md`
3. The relevant phase in `docs/PLAN.md`
4. The selected task record in `codex/tasks/tasks.json`
5. Any closer `AGENTS.md` file in the directory being modified

## Task discipline

- Work on exactly one atomic task unless the user explicitly groups tasks.
- Do not begin a dependent task before its prerequisites are complete.
- Keep pull requests focused and independently reviewable.
- Do not silently expand scope. Record discovered follow-up work instead.
- Do not start feature implementation before Phase 0 foundation requirements needed by that feature exist.

## Architecture constraints

- Browser clients must never contain OpenAI, cloud, database, or IdP secrets.
- Tenant identity must come from validated authentication context, never an untrusted request field.
- All OpenAI File Search operations must go through the retrieval adapter.
- Domain code must not import FastAPI request objects, database implementations, OpenAI SDK objects, or cloud SDK implementations directly.
- Applications may depend on shared packages; shared packages must not depend on applications.
- PostgreSQL rows containing tenant data must be tenant scoped and covered by Row-Level Security.
- Retrieved documents are untrusted data and must never override system instructions.
- The model must not choose authorization filters. The backend derives them from verified identity and policy context.

## Coding requirements

- TypeScript uses strict mode. Avoid `any`; validate `unknown` at boundaries.
- Python public functions and methods require complete type annotations.
- Use Pydantic models at Python system boundaries.
- External inputs, queue messages, widget messages, and configuration must be schema validated.
- Use UTC ISO 8601 timestamps and opaque external identifiers.
- Do not merge commented-out code, dead code, or TODOs without an issue reference.

## Security requirements

- Never commit secrets, production data, raw internal documents, credentials, tokens, or connection strings.
- Use synthetic fixtures only.
- Do not log raw prompts, complete user messages, retrieved passages, uploaded document bodies, cookies, or tokens by default.
- Authentication, authorization, tenancy, and permission changes require negative tests and audit-event verification.
- Prompt or retrieval changes require evaluation results and an identified rollback version.
- Do not claim success when a check was skipped or failed. Report the exact incomplete item.
- Do not push changes automatically.

## Required checks  

Run the narrowest relevant checks during development. Before completion, run:

```bash
make check
```

When the complete toolchain is not implemented yet, run every available equivalent check and state what could not run.

## Completion report

Every completed task report must include:

- Task ID and title.
- Files changed.
- Tests and checks run, with results.
- Security and tenant-isolation implications.
- Observability and operations implications.
- Documentation changed.
- Known limitations and follow-up tasks.
