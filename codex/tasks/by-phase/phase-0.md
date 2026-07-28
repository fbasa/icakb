# Phase 0 — Engineering Foundation

Establish a repeatable process for implementing, testing, reviewing, building, deploying, and rolling back a small change.

## Tasks

- [x] `P0-001` — Create the Git repository
- [x] `P0-002` — Configure branch protection for main
- [x] `P0-003` — Add root .gitignore and .gitattributes
- [x] `P0-004` — Add .editorconfig
- [x] `P0-005` — Create the monorepo directory structure
- [x] `P0-006` — Initialize the pnpm workspace
- [x] `P0-007` — Pin Node.js and pnpm versions
- [x] `P0-008` — Initialize the Python uv workspace
- [x] `P0-009` — Pin the Python runtime version
- [x] `P0-010` — Create the initial FastAPI service
- [x] `P0-011` — Create the initial Next.js assistant application
- [x] `P0-012` — Create the initial Next.js administration application
- [x] `P0-013` — Create the widget-loader package
- [x] `P0-014` — Create the browser-extension package
- [x] `P0-015` — Configure Python formatting with Ruff
- [x] `P0-016` — Configure Python linting with Ruff
- [x] `P0-017` — Configure Python type checking with mypy
- [x] `P0-018` — Configure TypeScript strict mode
- [x] `P0-019` — Configure ESLint
- [x] `P0-020` — Configure Prettier
- [x] `P0-021` — Configure Markdown, shell, Docker and YAML linting
- [x] `P0-022` — Configure pytest
- [x] `P0-023` — Configure Vitest and React Testing Library
- [x] `P0-024` — Configure Playwright
- [x] `P0-025` — Create root Makefile commands
- [x] `P0-026` — Configure pre-commit hooks
- [x] `P0-027` — Configure Gitleaks
- [x] `P0-028` — Configure Dependabot
- [x] `P0-029` — Configure GitHub Dependency Review
- [x] `P0-030` — Configure CodeQL
- [x] `P0-031` — Configure Trivy repository scanning
- [x] `P0-032` — Create service Dockerfiles
- [x] `P0-033` — Add container health checks
- [x] `P0-034` — Create local Docker Compose configuration
- [x] `P0-035` — Add local PostgreSQL
- [x] `P0-036` — Add local object-storage emulator
- [x] `P0-037` — Add local queue emulator or queue abstraction
- [x] `P0-038` — Add environment configuration validation
- [x] `P0-039` — Create .env.example
- [x] `P0-040` — Add structured JSON logging
- [x] `P0-041` — Add request-correlation middleware
- [x] `P0-042` — Add OpenTelemetry bootstrap
- [x] `P0-043` — Implement /health/live
- [x] `P0-044` — Implement /health/ready
- [x] `P0-045` — Implement RFC 9457 API error format
- [x] `P0-046` — Create the base CI workflow
- [x] `P0-047` — Add application-build jobs to CI
- [x] `P0-048` — Add container-image scanning
- [x] `P0-049` — Create the development deployment workflow
- [x] `P0-050` — Configure deployment through OIDC
- [x] `P0-051` — Add immutable image tagging
- [x] `P0-052` — Create README.md
- [x] `P0-053` — Create AGENTS.md
- [x] `P0-054` — Create docs/ARCHITECTURE.md
- [x] `P0-055` — Create docs/DECISIONS.md and initial ADRs
- [x] `P0-056` — Create docs/PLAN.md
- [x] `P0-057` — Create docs/OPERATIONS.md
- [x] `P0-058` — Create SECURITY.md
- [x] `P0-059` — Create CONTRIBUTING.md
- [x] `P0-060` — Create docs/TESTING.md
- [x] `P0-061` — Create prompt-library skeleton
- [x] `P0-062` — Create evaluation-library skeleton
- [x] `P0-063` — Implement the version endpoint demonstration
- [x] `P0-064` — Deploy the version endpoint to development
- [x] `P0-065` — Add post-deployment smoke test
- [x] `P0-066` — Demonstrate rollback

## Audit gate

**Status:** Blocked

The [Phase 0 completion audit](../../../docs/PHASE_0_AUDIT.md) has a `FAIL`
verdict; therefore the `PHASE-0-EXIT` dependency remains incomplete and no
Phase 1 task may begin.

The gate may be cleared only after every priority-zero blocker is resolved, the
audit revalidation evidence is recorded, the authoritative task catalog is
synchronized, and every exit-gate item below is complete.

## Exit gate

- [ ] A small change passes local checks and pull-request review.
- [ ] CI builds and scans affected artifacts.
- [ ] The immutable artifact deploys to development and passes smoke tests.
- [ ] The deployment can be rolled back.
- [ ] A new engineer can reproduce the process from repository documentation.
