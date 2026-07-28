# Phase 1 — Identity and Tenant Foundation

Create the authentication, authorization, tenancy, session, audit, and database-isolation layer.

## Tasks

- [ ] `P1-001` — Define the tenant domain model
- [ ] `P1-002` — Define the user domain model
- [ ] `P1-003` — Define roles, groups and memberships
- [ ] `P1-004` — Create tenant database tables
- [ ] `P1-005` — Create user database tables
- [ ] `P1-006` — Create role and group tables
- [ ] `P1-007` — Add typed tenant identifiers
- [ ] `P1-008` — Add typed user identifiers
- [ ] `P1-009` — Define identity-provider configuration schema
- [ ] `P1-010` — Implement OIDC discovery loading
- [ ] `P1-011` — Implement JWT signature validation
- [ ] `P1-012` — Implement issuer and audience validation
- [ ] `P1-013` — Implement token-expiry validation
- [ ] `P1-014` — Implement authenticated-request middleware
- [ ] `P1-015` — Map external subject to internal user
- [ ] `P1-016` — Implement just-in-time user provisioning
- [ ] `P1-017` — Implement disabled-user handling
- [ ] `P1-018` — Implement tenant resolution
- [ ] `P1-019` — Prevent request-supplied tenant override
- [ ] `P1-020` — Define authorization-policy interface
- [ ] `P1-021` — Implement role-based authorization checks
- [ ] `P1-022` — Implement group-based authorization context
- [ ] `P1-023` — Implement PostgreSQL tenant context
- [ ] `P1-024` — Create initial Row-Level Security policies
- [ ] `P1-025` — Add RLS negative tests
- [ ] `P1-026` — Define short-lived assistant session-token schema
- [ ] `P1-027` — Implement session-token issuance
- [ ] `P1-028` — Implement session-token validation
- [ ] `P1-029` — Add session revocation versioning
- [ ] `P1-030` — Define audit-event schema
- [ ] `P1-031` — Create audit-event storage
- [ ] `P1-032` — Record authentication events
- [ ] `P1-033` — Record authorization denials
- [ ] `P1-034` — Add tenant-management API contracts
- [ ] `P1-035` — Implement tenant creation
- [ ] `P1-036` — Implement tenant disablement
- [ ] `P1-037` — Implement user-status administration
- [ ] `P1-038` — Add tenant and user metrics
- [ ] `P1-039` — Document identity flow
- [ ] `P1-040` — Document tenant-isolation design
- [ ] `P1-041` — Create tenant-isolation test suite

## Exit gate

- [ ] Users resolve to one verified tenant.
- [ ] Short-lived assistant sessions can be issued and validated.
- [ ] Disabled users and tenants are rejected.
- [ ] PostgreSQL RLS prevents cross-tenant access.
- [ ] Authentication and authorization events are auditable.
- [ ] Tenant-isolation tests pass in CI.
