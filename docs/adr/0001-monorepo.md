# Use a polyglot monorepo

- Status: Accepted
- Date: 2026-07-26

## Context

The product contains multiple web applications, a widget, a browser extension, Python services, shared contracts, infrastructure, prompts, and evaluations.

## Decision

Keep these components in one repository with explicit dependency boundaries and independently deployable services.

## Consequences

Atomic cross-cutting changes are easier to review, but repository tooling and ownership rules must remain disciplined.
