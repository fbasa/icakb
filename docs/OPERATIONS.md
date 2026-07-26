# Operations

## Required runbooks

The following procedures must be implemented and validated as their dependent phases complete:

- Deployment and post-deployment verification.
- Application rollback.
- Database migration and migration rollback or forward recovery.
- Prompt and model configuration rollback.
- OpenAI outage and rate-limit response.
- Queue backlog and dead-letter recovery.
- Failed ingestion replay and reconciliation.
- Document deletion verification.
- Tenant disablement and offboarding.
- Secret rotation.
- Backup, restore, and disaster recovery.
- Incident response, severity, escalation, and communication.

## Deployment principles

- Build once and promote the same immutable artifact digest.
- Require protected approvals for production.
- Apply backward-compatible database changes before application rollout.
- Verify liveness, readiness, version, authentication, retrieval, and citations after deployment.
- Stop or roll back when health thresholds fail.

## Operational telemetry

Monitor request latency, errors, streaming failures, token usage, retrieval duration and result counts, empty retrieval, citations, queue depth, oldest job age, ingestion failures, indexing duration, database-pool use, authorization denials, rate limits, and health-check failures.

## Data handling

Logs and traces must not record raw internal documents, retrieved passages, user prompts, cookies, tokens, API keys, or connection strings by default. Deletion workflows must verify all configured storage locations and caches.
