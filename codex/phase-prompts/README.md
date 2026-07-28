# Codex Phase Prompts

These files are reusable execution prompts for Codex. Each prompt is scoped to one approved delivery phase and references the authoritative task catalog rather than duplicating every task definition.

## Usage

1. Open the prompt for the active phase.
2. Give Codex the prompt file as context or paste its contents into the task conversation.
3. Supply a task ID such as `P2-019`. When no task ID is supplied, the prompt tells Codex to select the earliest ready task.
4. Use the same phase prompt repeatedly; by default, each run completes one atomic task and stops with a completion report.

## Prompt files

| Phase                               | Prompt                     | Atomic tasks |
| ----------------------------------- | -------------------------- | -----------: |
| 0 — Engineering Foundation          | [`phase-0.md`](phase-0.md) |           66 |
| 1 — Identity and Tenant Foundation  | [`phase-1.md`](phase-1.md) |           41 |
| 2 — Document Ingestion              | [`phase-2.md`](phase-2.md) |           67 |
| 3 — Retrieval and Answer Generation | [`phase-3.md`](phase-3.md) |           58 |
| 4 — Embeddable Widget               | [`phase-4.md`](phase-4.md) |           53 |
| 5 — Administration and Operations   | [`phase-5.md`](phase-5.md) |           56 |
| 6 — Browser Extension               | [`phase-6.md`](phase-6.md) |           40 |
| 7 — Production Hardening            | [`phase-7.md`](phase-7.md) |           82 |

The machine-readable source of truth remains `/codex/tasks/tasks.json`.

1. Read `AGENTS.md` and the mandatory documents.
2. Use `phase-0.md` to begin.
3. Execute one task or related task group at a time.
