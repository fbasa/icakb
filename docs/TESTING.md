# Testing Guide

## Test categories

- Unit tests for domain rules and small components.
- Integration tests for PostgreSQL, queues, storage, OpenAI adapters, and FastAPI endpoints.
- Contract tests for OpenAPI, widget messages, queue messages, retrieval contracts, and RFC 9457 errors.
- Playwright tests for assistant, widget, administration, and extension workflows.
- Tenant-isolation tests across API, database, storage, retrieval, and caches.
- Security tests for authentication, authorization, origin validation, prompt injection, RAG poisoning, and data exfiltration.
- RAG evaluations for retrieval, groundedness, citations, abstention, conflicts, superseded documents, and multi-turn behavior.
- Load, resilience, backup, restore, and disaster-recovery tests before production.

## Fixture policy

Use synthetic, non-sensitive documents and identities only. Never copy production documents, prompts, conversations, credentials, or database rows into tests.

## Provider modes

- Mock mode is the default for local and most CI tests.
- Sandbox mode uses a dedicated non-production OpenAI project, strict spending limits, and synthetic documents.

## Completion rule

Run the narrowest relevant tests while developing. Before completing a task, run every available repository check and report skipped checks with the reason.

## Local checks

- `pnpm lint:markdown`
- `pnpm lint:shell`
- `pnpm lint:docker`
- `pnpm lint:yaml`
- `pnpm test:python`
- `pnpm test:playwright`
- `pnpm test:vitest`
- `make smoke-version-endpoint` after `make deploy-version-endpoint`; the target sets
  `BASE_URL=http://127.0.0.1:8000`.
- For shared environments, run
  `BASE_URL=https://... EXPECTED_VERSION=... uv run --all-packages pytest tests/smoke/test_version_endpoint.py -q`.
