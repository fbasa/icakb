# Codex Phase 5 Prompt — Administration and Operations

You are Codex working in the `knowledge-assistant-codex-repo` monorepo.

Execute this phase by completing **exactly one ready atomic task per run**, unless the user explicitly supplies a small contiguous task batch. Do not attempt to implement an entire phase in one pull request.

## Binding sources

Read these files before editing:

1. `/AGENTS.md` and every nearer `AGENTS.md` governing files you will change.
2. `/docs/ARCHITECTURE.md`.
3. `/docs/ENGINEERING_FOUNDATION.md`.
4. `/docs/PLAN.md` for this phase and its exit gate.
5. `/codex/TASK_EXECUTION.md`.
6. `/codex/tasks/tasks.json` for the authoritative task record.
7. `/codex/tasks/by-phase/phase-5.md` for the phase checklist.
8. Relevant ADRs in `/docs/adr/`.

When instructions conflict, stop and report the conflict rather than silently choosing one.

## Per-run execution contract

1. Resolve the requested task ID. When none is supplied, select the earliest backlog task in this phase whose dependencies are complete.
2. Confirm the task objective, dependencies, acceptance criteria, affected boundaries, and required tests.
3. Inspect the smallest relevant repository surface before editing.
4. Implement only the minimum complete change for the selected task.
5. Add positive, negative, boundary, security, tenancy, and failure tests where relevant.
6. Add or update logs, metrics, traces, health checks, runbooks, ADRs, and API documentation only when the task changes those concerns.
7. Run focused checks first, then run `make check` when the repository supports it.
8. Keep generated files reproducible and never edit generated outputs manually.
9. Update the selected task to `in_review` after checks pass; do not mark it `done`, because reviewer approval owns that transition.
10. Return the completion report defined in `/codex/TASK_EXECUTION.md`, including exact commands and results.

## Global constraints

- Preserve the approved Option 1 architecture: OpenAI Responses API and hosted File Search stay behind replaceable adapters.
- Derive tenant and authorization scope only from verified identity and policy context.
- Never place API keys, credentials, tokens, production documents, retrieved passages, or page content in source control, logs, fixtures, screenshots, or test reports.
- Use synthetic data by default.
- Make external calls only in explicitly configured sandbox environments.
- Do not perform destructive cloud, GitHub, identity-provider, or production actions without explicit authorization.
- Do not weaken linting, typing, security scans, branch controls, RLS, CSP, origin validation, or evaluation thresholds to make a check pass.
- Do not invent provider configuration, account identifiers, domains, secrets, retention policy, SLO values, or compliance approvals.

## Stop conditions

Stop and provide a precise blocker report when work requires:

- An unavailable secret or account.
- A production-data operation.
- A destructive external action.
- A security or compliance decision not recorded in the repository.
- A change that contradicts an accepted ADR.
- A dependency task that is not complete and cannot be safely stubbed.

When an external setting cannot be changed from the repository, create the smallest reviewable configuration, script, documentation, or verification artifact possible, then clearly identify the remaining manual action.


## Phase mission

Provide authorized tenant administrators and operators with safe management, usage, quality, audit, alerting, and recovery capabilities.

**Atomic-task range:** `P5-001 through P5-056`

## Recommended execution sequence

Use dependency readiness, not numeric order alone. Within that rule, the intended work streams are:

- **Administration roles, authorization, and application shell:** `P5-001–P5-003`
- **Tenant settings and allowed origins:** `P5-004–P5-007`
- **Sources, connectors, and manual synchronization:** `P5-008–P5-014`
- **Documents, versions, reindexing, and deletion:** `P5-015–P5-020`
- **Ingestion jobs, replay, and dead-letter visibility:** `P5-021–P5-024`
- **Audit query and immutable audit view:** `P5-025–P5-027`
- **Usage aggregation, dashboards, quotas, and enforcement:** `P5-028–P5-032`
- **Feedback collection and traceability:** `P5-033–P5-037`
- **Evaluation and prompt-version visibility:** `P5-038–P5-041`
- **Status, alerts, and operational runbooks:** `P5-042–P5-054`
- **Administrative end-to-end and audit tests:** `P5-055–P5-056`

## Phase-specific constraints

- Every administration action requires explicit server-side authorization; UI visibility is not an authorization control.
- Destructive operations require confirmation, stable audit events, idempotency, and documented recovery or irreversibility.
- Audit records are append-only from the administration surface and must not reveal inaccessible content.
- Usage aggregation and feedback must remain tenant-scoped and avoid storing unnecessary message or document content.
- Quota enforcement must use stable machine-readable errors and must not permit one tenant to exhaust shared capacity.
- Operational status pages must not expose secrets, provider identifiers, stack traces, or internal network details.
- Alerts require named owners, thresholds, severity, and a linked runbook.

## Phase verification expectations

For every selected task:

- Prove the stated acceptance criterion with automated checks or a reproducible verification artifact.
- Include negative tests for trust boundaries and failure handling when relevant.
- Confirm tenant isolation whenever data, identity, retrieval, storage, caching, or administration is affected.
- Confirm logs and traces exclude restricted content.
- Record external manual steps separately; never represent them as completed repository work.
- Preserve backward compatibility unless the task explicitly authorizes a versioned breaking change.

## Phase exit gate

Do not declare this phase complete until all atomic tasks are reviewer-approved and all conditions below have evidence:

- [ ] Tenant administrators can safely manage settings, sources, documents, and origins.
- [ ] Operators can identify, replay, and recover ingestion failures.
- [ ] Usage, feedback, audits, evaluations, and active prompt versions are visible to authorized users.
- [ ] Destructive and sensitive actions are authorized, confirmed, and audited.
- [ ] Alerts and operational runbooks exist and are testable.
- [ ] Administrative end-to-end and audit tests pass.

## Required final response for each run

Use this exact structure:

```text
Task: <task ID and title>
Outcome: <what was completed>
Files changed: <paths>
Tests and checks: <commands and exact results>
Security and tenancy: <controls and negative tests>
Observability and operations: <logs, metrics, traces, health, or runbooks>
Documentation: <updated documents>
Task status: in_review | blocked
Known limitations: <remaining limitations>
Follow-up tasks: <dependency-safe next tasks>
```
