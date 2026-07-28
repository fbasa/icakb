# Codex Phase 4 Prompt — Embeddable Widget

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
7. `/codex/tasks/by-phase/phase-4.md` for the phase checklist.
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

Deliver a framework-independent, accessible, origin-restricted assistant widget using a small loader and a separately hosted sandboxed iframe.

**Atomic-task range:** `P4-001 through P4-053`

## Recommended execution sequence

Use dependency readiness, not numeric order alone. Within that rule, the intended work streams are:

- **Public configuration, loader, and launcher isolation:** `P4-001–P4-006`
- **Iframe creation and typed cross-window messaging:** `P4-007–P4-012`
- **Embed-origin policy and secure session handoff:** `P4-013–P4-017`
- **Assistant UI, chat, streaming, citations, and errors:** `P4-018–P4-029`
- **Open/close behavior, responsive layout, and theming:** `P4-030–P4-033`
- **Accessibility foundations:** `P4-034–P4-037`
- **CSP, framing, and postMessage security:** `P4-038–P4-041`
- **Unit, host-framework, and end-to-end tests:** `P4-042–P4-046`
- **Bundle budget, CDN release, integrity, and documentation:** `P4-047–P4-053`

## Phase-specific constraints

- Keep the loader small and framework-independent; host applications must not need React or Next.js.
- Host the assistant iframe on a separate approved origin with the minimum sandbox capabilities.
- Validate both `postMessage` origin and schema on every message. Never use wildcard target origins for sensitive messages.
- Embed eligibility is enforced server-side through the tenant origin allowlist and CSP `frame-ancestors`.
- Short-lived assistant tokens remain memory-only and are transferred only to the expected iframe origin.
- Host CSS and JavaScript must not control the iframe application; launcher styles remain isolated with Shadow DOM.
- Accessibility, keyboard navigation, focus management, responsive behavior, and browser compatibility are release requirements.
- Do not expose source content the user is not authorized to view in citation or detail interfaces.

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

- [ ] The widget embeds in plain HTML and supported application frameworks.
- [ ] Host and widget styles remain isolated.
- [ ] Only approved origins can initialize sessions or frame the assistant.
- [ ] Session tokens are short-lived and not persisted.
- [ ] Streaming, citations, error states, and cancellation work.
- [ ] Accessibility and security tests pass.
- [ ] Versioned assets are deployable through the CDN.

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
