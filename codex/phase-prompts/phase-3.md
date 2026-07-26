# Codex Phase 3 Prompt — Retrieval and Answer Generation

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
7. `/codex/tasks/by-phase/phase-3.md` for the phase checklist.
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

Deliver a stable API that retrieves only authorized evidence and generates grounded, cited, streaming answers with measurable abstention and safety behavior.

**Atomic-task range:** `P3-001 through P3-058`

## Recommended execution sequence

Use dependency readiness, not numeric order alone. Within that rule, the intended work streams are:

- **Retrieval contracts and hosted File Search adapter:** `P3-001–P3-009`
- **Conversation and message persistence:** `P3-010–P3-017`
- **Versioned system, citation, and evidence prompts:** `P3-018–P3-023`
- **Retrieval orchestration and evidence normalization:** `P3-024–P3-027`
- **Responses API adapter and streaming:** `P3-028–P3-035`
- **Abstention, history, and token budgeting:** `P3-036–P3-039`
- **Provider resilience and observability:** `P3-040–P3-046`
- **Evaluation datasets, runner, thresholds, and CI:** `P3-047–P3-056`
- **Architecture and rollback documentation:** `P3-057–P3-058`

## Phase-specific constraints

- Authorization is resolved before retrieval. The model must never choose the tenant, vector store, or access filter.
- File Search and Responses API provider objects must not leak beyond their adapters.
- Every displayed citation must map to evidence retrieved for the current authorized request.
- When evidence is absent or insufficient, abstain rather than fill gaps with unsupported model knowledge.
- Retrieved text is untrusted data and must be delimited from trusted instructions.
- Raw prompts, user messages, retrieved passages, and document content are excluded from default logs and traces.
- Live OpenAI tests require an explicit sandbox project, synthetic data, and bounded cost; offline deterministic tests remain the default.
- Prompt or model changes require versioned evaluations and a rollback target.

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

- [ ] Every query is tenant- and permission-filtered.
- [ ] Streaming responses use a stable versioned contract.
- [ ] Citations refer only to authorized evidence.
- [ ] Insufficient evidence produces a safe abstention.
- [ ] Provider failures map to stable, observable application behavior.
- [ ] Quality, prompt-injection, and tenant-isolation evaluations pass approved thresholds.

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
