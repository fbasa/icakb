# Phase 6 — Browser Extension

Deliver a least-privilege Manifest V3 extension using the same assistant backend.

## Tasks

- [ ] `P6-001` — Define supported browser versions
- [ ] `P6-002` — Define extension use cases
- [ ] `P6-003` — Define minimum permission set
- [ ] `P6-004` — Create Manifest V3 configuration
- [ ] `P6-005` — Implement extension service worker
- [ ] `P6-006` — Implement side-panel shell
- [ ] `P6-007` — Reuse assistant design-system components
- [ ] `P6-008` — Implement extension authentication entry point
- [ ] `P6-009` — Implement extension session-token exchange
- [ ] `P6-010` — Prevent permanent token storage
- [ ] `P6-011` — Implement conversation creation
- [ ] `P6-012` — Implement streaming chat
- [ ] `P6-013` — Implement citations in extension UI
- [ ] `P6-014` — Define page-context request schema
- [ ] `P6-015` — Implement explicit share-selection action
- [ ] `P6-016` — Implement selected-text extraction
- [ ] `P6-017` — Implement context preview
- [ ] `P6-018` — Implement context confirmation
- [ ] `P6-019` — Add context-size limit
- [ ] `P6-020` — Add sensitive-field warning
- [ ] `P6-021` — Implement active-tab access
- [ ] `P6-022` — Avoid broad host permissions
- [ ] `P6-023` — Implement tenant domain allowlist
- [ ] `P6-024` — Enforce domain allowlist
- [ ] `P6-025` — Implement content-script messaging
- [ ] `P6-026` — Validate extension message senders
- [ ] `P6-027` — Implement extension error states
- [ ] `P6-028` — Implement session-expiry recovery
- [ ] `P6-029` — Add extension event telemetry
- [ ] `P6-030` — Add extension unit tests
- [ ] `P6-031` — Add extension integration tests
- [ ] `P6-032` — Add page-context security tests
- [ ] `P6-033` — Add domain-restriction tests
- [ ] `P6-034` — Add extension build signing process
- [ ] `P6-035` — Generate internal release package
- [ ] `P6-036` — Document enterprise deployment options
- [ ] `P6-037` — Document extension permissions
- [ ] `P6-038` — Document user privacy behavior
- [ ] `P6-039` — Pilot extension with internal test group
- [ ] `P6-040` — Resolve pilot defects

## Exit gate

- [ ] The Manifest V3 extension reuses the assistant API.
- [ ] Page context is captured only after explicit user action and preview.
- [ ] Broad host permissions are avoided.
- [ ] Domain restrictions and sender validation are tested.
- [ ] An internally deployable signed package is available.
