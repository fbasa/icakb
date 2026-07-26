# Phase 5 — Administration and Operations

Provide controlled management, visibility, recovery, quotas, feedback, and operational tooling.

## Tasks

- [ ] `P5-001` — Define administration-role matrix
- [ ] `P5-002` — Enforce administration-route authorization
- [ ] `P5-003` — Implement administration application shell
- [ ] `P5-004` — Implement tenant-settings read API
- [ ] `P5-005` — Implement tenant-settings update API
- [ ] `P5-006` — Build tenant-settings page
- [ ] `P5-007` — Build allowed-origin management UI
- [ ] `P5-008` — Add source-list API
- [ ] `P5-009` — Build source-list page
- [ ] `P5-010` — Build manual-upload interface
- [ ] `P5-011` — Build Drive-connector setup flow
- [ ] `P5-012` — Build connector-health display
- [ ] `P5-013` — Implement manual synchronization action
- [ ] `P5-014` — Implement source-disable action
- [ ] `P5-015` — Build document-list page
- [ ] `P5-016` — Add document search and filters
- [ ] `P5-017` — Build document-detail page
- [ ] `P5-018` — Implement document reindex action
- [ ] `P5-019` — Implement document-delete action
- [ ] `P5-020` — Require destructive-action confirmation
- [ ] `P5-021` — Build ingestion-job list
- [ ] `P5-022` — Build ingestion-job detail view
- [ ] `P5-023` — Implement failed-job replay action
- [ ] `P5-024` — Implement dead-letter queue summary
- [ ] `P5-025` — Implement audit-event query API
- [ ] `P5-026` — Build audit-log viewer
- [ ] `P5-027` — Protect audit events from modification
- [ ] `P5-028` — Define usage-event aggregation
- [ ] `P5-029` — Implement tenant-usage API
- [ ] `P5-030` — Build usage dashboard
- [ ] `P5-031` — Add tenant quota configuration
- [ ] `P5-032` — Enforce request quotas
- [ ] `P5-033` — Define user-feedback schema
- [ ] `P5-034` — Implement feedback submission API
- [ ] `P5-035` — Add widget feedback controls
- [ ] `P5-036` — Build feedback review page
- [ ] `P5-037` — Link feedback to traces and prompt versions
- [ ] `P5-038` — Implement evaluation-report storage
- [ ] `P5-039` — Build evaluation-results page
- [ ] `P5-040` — Implement prompt-version read API
- [ ] `P5-041` — Build prompt-version display
- [ ] `P5-042` — Add system-status page
- [ ] `P5-043` — Define alert thresholds
- [ ] `P5-044` — Configure ingestion-failure alerts
- [ ] `P5-045` — Configure query-error alerts
- [ ] `P5-046` — Configure authorization-denial anomaly alerts
- [ ] `P5-047` — Configure queue-backlog alerts
- [ ] `P5-048` — Create deployment runbook
- [ ] `P5-049` — Create rollback runbook
- [ ] `P5-050` — Create OpenAI outage runbook
- [ ] `P5-051` — Create failed-ingestion runbook
- [ ] `P5-052` — Create tenant-offboarding runbook
- [ ] `P5-053` — Create secret-rotation runbook
- [ ] `P5-054` — Create prompt-rollback runbook
- [ ] `P5-055` — Add administrative end-to-end tests
- [ ] `P5-056` — Add administration audit tests

## Exit gate

- [ ] Administrators can manage sources, documents, and origins.
- [ ] Operators can identify and recover ingestion failures.
- [ ] Usage, feedback, audit, and evaluation results are visible.
- [ ] Sensitive actions are authorized and audited.
- [ ] Required alerts and runbooks exist.