# Codex Phase 2 Prompt — Document Ingestion

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
7. `/codex/tasks/by-phase/phase-2.md` for the phase checklist.
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

Implement a reliable, observable, idempotent, authorization-aware, and reversible document lifecycle from approved sources to hosted File Search.

**Atomic-task range:** `P2-001 through P2-067`

## Recommended execution sequence

Use dependency readiness, not numeric order alone. Within that rule, the intended work streams are:

- **Source, document, version, and job models:** `P2-001–P2-010`
- **Upload flow and file-security controls:** `P2-011–P2-017`
- **Queue contracts, consumption, and idempotency:** `P2-018–P2-022`
- **Extraction, normalization, and deduplication:** `P2-023–P2-030`
- **Metadata and source-permission mapping:** `P2-031–P2-033`
- **Vector-store and provider indexing adapter:** `P2-034–P2-041`
- **Retry, dead-letter, and replay behavior:** `P2-042–P2-045`
- **Deletion, cache invalidation, and reconciliation:** `P2-046–P2-051`
- **Metrics, traces, logs, and status APIs:** `P2-052–P2-057`
- **Google Drive connector and synchronization:** `P2-058–P2-064`
- **Synthetic fixtures, integration tests, and runbook:** `P2-065–P2-067`

## Phase-specific constraints

- Canonical source files live in approved object storage; hosted File Search is an index, not the system of record.
- No document becomes searchable until file validation, malware-policy handling, metadata validation, indexing, and tenant-store verification succeed.
- Queue consumers and external operations must be idempotent. Duplicate delivery must not duplicate versions or provider files.
- Use a per-tenant or approved security-boundary vector store. Never select a vector store from untrusted request input.
- Authorization metadata must be deterministic, validated, and compatible with hosted File Search attribute limits.
- Deletion must cover provider files, canonical storage according to policy, metadata, and caches, followed by verification.
- Do not ingest production files in tests or local development; use synthetic fixtures.

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

- [ ] Files can be uploaded, validated, indexed, updated, and deleted.
- [ ] Duplicate ingestion is idempotent and failed jobs are recoverable.
- [ ] Internal, object-storage, queue, and provider states can be reconciled.
- [ ] Google Drive synchronization handles create, change, and delete events.
- [ ] Authorization metadata is present before searchability.
- [ ] Ingestion and deletion integration tests pass.

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
