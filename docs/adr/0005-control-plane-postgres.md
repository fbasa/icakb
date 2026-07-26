# Use PostgreSQL for the control plane

- Status: Accepted
- Date: 2026-07-26

## Context

Tenant, identity, metadata, conversation, feedback, and audit data are relational and security sensitive.

## Decision

Use PostgreSQL with typed access layers, migrations, and Row-Level Security.

## Consequences

Strong consistency and tenant enforcement are available; migrations and pool management become operational responsibilities.
