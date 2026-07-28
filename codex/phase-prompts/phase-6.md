# Codex Phase 6 Prompt — Browser Extension

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
7. `/codex/tasks/by-phase/phase-6.md` for the phase checklist.
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

Deliver a Manifest V3 browser extension that reuses the assistant API, requests least privilege, and sends page context only after explicit, reviewable user consent.

**Atomic-task range:** `P6-001 through P6-040`

## Recommended execution sequence

Use dependency readiness, not numeric order alone. Within that rule, the intended work streams are:

- **Browser scope, use cases, permissions, and manifest:** `P6-001–P6-004`
- **Service worker and side-panel shell:** `P6-005–P6-007`
- **Authentication, sessions, chat, and citations:** `P6-008–P6-013`
- **Explicit selected-text sharing and preview:** `P6-014–P6-020`
- **Active-tab, domain allowlist, and validated messaging:** `P6-021–P6-026`
- **Errors, session recovery, and privacy-safe telemetry:** `P6-027–P6-029`
- **Unit, integration, context-security, and domain tests:** `P6-030–P6-033`
- **Signing, packaging, deployment, privacy documentation, and pilot:** `P6-034–P6-040`

## Phase-specific constraints

- Use Manifest V3 and a service worker; do not introduce persistent background pages.
- Request the minimum permissions. Prefer `activeTab` and explicit user gestures over broad host access.
- Capture only user-selected text for the initial context-sharing workflow.
- Present a preview and require confirmation before transmitting page content.
- Enforce tenant-configured domain restrictions before capture and again before transmission.
- Validate senders and schemas for extension, content-script, service-worker, and side-panel messages.
- Never log, persist, or include captured page content in telemetry.
- Do not claim store publication or enterprise deployment completion without the required external account and approval evidence.

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

- [ ] The extension installs and runs under Manifest V3.
- [ ] Chat and citations use the existing assistant API.
- [ ] Page context is captured only after explicit user action, preview, and confirmation.
- [ ] Broad host permissions are not required.
- [ ] Domain restrictions and message-sender validation are enforced and tested.
- [ ] An internally deployable, traceable package is produced.
- [ ] Pilot blockers are resolved or explicitly accepted.

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
