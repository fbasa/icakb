# Data Model Domains

## Identity and tenancy

Tenant, user, role, group, membership, external identity mapping, session revocation version, and audit event.

## Sources and documents

Data source, connector credential reference, document, document version, ingestion job, provider file reference, deletion state, and reconciliation result.

## Conversations

Conversation, message, assistant response state, citation reference, feedback, prompt version, model configuration, and usage aggregation.

## Required properties

Every tenant-owned row includes a tenant identifier and is covered by Row-Level Security. External identifiers are opaque. Timestamps are UTC. Audit records are append-only under the approved retention policy.
