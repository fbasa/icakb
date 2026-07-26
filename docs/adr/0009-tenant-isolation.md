# Use layered tenant isolation

- Status: Accepted
- Date: 2026-07-26

## Context

Application-only tenant checks are insufficient for private company knowledge.

## Decision

Enforce tenant scope in authentication, policy, PostgreSQL RLS, storage, retrieval-store selection, metadata filters, caches, queues, logs, and tests.

## Consequences

Security is defense in depth, but every new data path must preserve tenant context.
