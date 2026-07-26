# Use TypeScript and Python by layer

- Status: Accepted
- Date: 2026-07-26

## Context

Browser clients benefit from the TypeScript ecosystem; orchestration and ingestion benefit from Python and FastAPI.

## Decision

Use TypeScript for browser-facing applications and Python for APIs, workers, retrieval, and ingestion.

## Consequences

Contracts and generation must be managed centrally to prevent drift.
