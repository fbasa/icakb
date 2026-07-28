# Phase 4 — Embeddable Widget

Provide a secure framework-independent assistant widget for existing web applications.

## Tasks

- [ ] `P4-001` — Define public widget configuration schema
- [ ] `P4-002` — Define widget versioning policy
- [ ] `P4-003` — Implement loader script entry point
- [ ] `P4-004` — Implement duplicate-loader protection
- [ ] `P4-005` — Implement launcher Web Component
- [ ] `P4-006` — Implement Shadow DOM styles
- [ ] `P4-007` — Implement iframe creation
- [ ] `P4-008` — Configure iframe sandbox attributes
- [ ] `P4-009` — Define host-to-iframe message schemas
- [ ] `P4-010` — Define iframe-to-host message schemas
- [ ] `P4-011` — Implement message origin validation
- [ ] `P4-012` — Implement message schema validation
- [ ] `P4-013` — Implement tenant embed-origin configuration
- [ ] `P4-014` — Enforce embed-origin allowlist
- [ ] `P4-015` — Implement host session-exchange client
- [ ] `P4-016` — Implement secure token handoff to iframe
- [ ] `P4-017` — Prevent token persistence in browser storage
- [ ] `P4-018` — Implement assistant iframe application shell
- [ ] `P4-019` — Implement authenticated API client
- [ ] `P4-020` — Implement conversation creation UI
- [ ] `P4-021` — Implement message composer
- [ ] `P4-022` — Implement streaming message renderer
- [ ] `P4-023` — Implement streaming cancellation UI
- [ ] `P4-024` — Implement citation presentation
- [ ] `P4-025` — Implement source-detail view
- [ ] `P4-026` — Implement insufficient-evidence state
- [ ] `P4-027` — Implement authentication-expired state
- [ ] `P4-028` — Implement service-unavailable state
- [ ] `P4-029` — Implement retry control
- [ ] `P4-030` — Implement widget open and close behavior
- [ ] `P4-031` — Implement responsive sizing
- [ ] `P4-032` — Implement configurable placement
- [ ] `P4-033` — Implement controlled theming
- [ ] `P4-034` — Implement focus management
- [ ] `P4-035` — Implement keyboard navigation
- [ ] `P4-036` — Add screen-reader labels and announcements
- [ ] `P4-037` — Add color-contrast checks
- [ ] `P4-038` — Configure CSP for assistant origin
- [ ] `P4-039` — Configure frame-ancestors policy
- [ ] `P4-040` — Add clickjacking and framing tests
- [ ] `P4-041` — Add postMessage security tests
- [ ] `P4-042` — Add widget unit tests
- [ ] `P4-043` — Add widget end-to-end test host
- [ ] `P4-044` — Test widget in Next.js host
- [ ] `P4-045` — Test widget in plain HTML host
- [ ] `P4-046` — Test widget in another SPA framework
- [ ] `P4-047` — Add widget bundle-size budget
- [ ] `P4-048` — Add widget release build
- [ ] `P4-049` — Publish widget assets to development CDN
- [ ] `P4-050` — Add asset-integrity metadata
- [ ] `P4-051` — Document embedding procedure
- [ ] `P4-052` — Document widget events API
- [ ] `P4-053` — Document CSP requirements

## Exit gate

- [ ] The widget embeds in multiple host frameworks.
- [ ] Only approved origins can initialize sessions.
- [ ] Session tokens are short-lived and memory-only.
- [ ] Streaming, citations, accessibility, and responsive behavior pass tests.
- [ ] Widget assets are versioned and deployable through a CDN.
