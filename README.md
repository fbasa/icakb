# Internal Company Knowledge Assistant

A documentation-first, Codex-friendly monorepo scaffold for a secure internal RAG assistant that can be embedded in existing web applications, exposed as a standalone web app, and packaged as a browser extension.

## Approved architecture

The approved design uses:

- Next.js for the assistant iframe application and administration portal.
- A small TypeScript widget loader using a Web Component and sandboxed iframe.
- A Chrome Manifest V3 browser extension.
- FastAPI for the API gateway, identity enforcement, conversation orchestration, and administration APIs.
- OpenAI Responses API with hosted File Search behind a replaceable retrieval adapter.
- PostgreSQL for tenants, users, roles, document metadata, conversations, feedback, and audit events.
- S3-compatible object storage as the canonical document store.
- Google Drive as the first external connector.
- A managed queue for ingestion jobs.
- OpenTelemetry for traces, metrics, and log correlation.
- Terraform-managed development, staging, and production environments.

## Repository status

This repository contains the approved architecture, engineering foundation, delivery phases, and **463 atomic tasks**. It intentionally does not implement business modules yet.

## Start here

1. Read `AGENTS.md`.
2. Read `docs/ARCHITECTURE.md` and `docs/ENGINEERING_FOUNDATION.md`.
3. Select exactly one ready task from `codex/tasks/tasks.json` or `codex/tasks/task-index.csv`.
4. Create a focused branch and pull request.
5. Follow `codex/TASK_EXECUTION.md` and the task definition of done.

## Important files

- `docs/ARCHITECTURE.md` — approved application architecture and security boundaries.
- `docs/ENGINEERING_FOUNDATION.md` — repository, CI, testing, security, environments, and operations requirements.
- `docs/PLAN.md` — phase objectives, atomic-task catalog, dependencies, and exit gates.
- `codex/tasks/tasks.json` — machine-readable task backlog.
- `codex/tasks/task-index.csv` — spreadsheet-friendly task index.
- `AGENTS.md` — binding instructions for Codex and other coding agents.
- `SECURITY.md` — security and disclosure requirements.

## Bootstrap target

The first implementation milestone is Phase 0. Its exit criterion is that a small change can be implemented, tested, reviewed, built, deployed, verified, and rolled back through a repeatable process.
