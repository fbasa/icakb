# Codex Phase 7 Prompt — Production Hardening

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
7. `/codex/tasks/by-phase/phase-7.md` for the phase checklist.
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

Produce evidence that the system satisfies approved security, privacy, quality, performance, resilience, recovery, operational, and release-readiness gates.

**Atomic-task range:** `P7-001 through P7-082`

## Recommended execution sequence

Use dependency readiness, not numeric order alone. Within that rule, the intended work streams are:

- **Data flows, classification, trust boundaries, and threat model:** `P7-001–P7-005`
- **IAM, secrets, retention, deletion, and offboarding:** `P7-006–P7-014`
- **SLIs, SLOs, dashboards, and alerts:** `P7-015–P7-018`
- **Load models, performance tests, tuning, quotas, and edge controls:** `P7-019–P7-031`
- **Dependency failure and resilience exercises:** `P7-032–P7-040`
- **Backups, restore, RTO/RPO, and disaster recovery:** `P7-041–P7-049`
- **Adversarial RAG tests and frozen release evaluations:** `P7-050–P7-058`
- **Accessibility, compatibility, penetration testing, licenses, SBOM, and provenance:** `P7-059–P7-066`
- **Incident response, support, pilot, readiness review, deployment, and post-release review:** `P7-067–P7-082`

## Phase-specific constraints

- Hardening tasks produce verifiable evidence; do not mark controls complete based only on configuration intent.
- Do not invent retention periods, SLOs, RTOs, RPOs, risk acceptance, or compliance approval. Record unresolved decisions as blockers.
- Load, resilience, backup, restore, deletion, and disaster-recovery tests must use approved non-production environments unless explicitly authorized otherwise.
- Freeze evaluation datasets before release-candidate scoring and record exact model, prompt, configuration, and artifact versions.
- No critical security finding may remain unresolved. High findings require remediation or an explicit time-limited exception from the authorized owner.
- Production promotion must reuse the staging-tested immutable artifact and require the configured approval gates.
- Never claim penetration-test completion, pilot acceptance, production readiness, or go-live approval without the corresponding evidence and owner decision.
- Production actions must include rollback readiness and post-deployment verification.

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

- [ ] Threat modeling and independent security testing are complete with required remediation.
- [ ] Performance and SLO targets are approved and met.
- [ ] Retention, deletion, tenant offboarding, backup, restore, and disaster recovery are verified.
- [ ] Frozen model and prompt evaluations meet approved quality and leakage thresholds.
- [ ] Operational dashboards, alerts, runbooks, incident response, and support paths are active.
- [ ] Pilot acceptance and production-readiness reviews are documented.
- [ ] Production deployment, smoke tests, telemetry, and rollback readiness are verified.

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
