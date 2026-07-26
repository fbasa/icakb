# Use hosted File Search behind a retrieval adapter

- Status: Accepted
- Date: 2026-07-26

## Context

The MVP needs rapid semantic and keyword retrieval without operating a search cluster.

## Decision

Use OpenAI File Search initially, isolated per tenant or security boundary, behind internal retrieval contracts.

## Consequences

Delivery is faster, while retention, ACL complexity, metadata limits, and provider dependency require explicit monitoring and a migration path.
