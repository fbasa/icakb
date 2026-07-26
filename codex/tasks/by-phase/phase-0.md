# Phase 0 — Engineering Foundation

Establish a repeatable process for implementing, testing, reviewing, building, deploying, and rolling back a small change.

## Tasks

- [ ] `P0-001` — Create the Git repository
- [ ] `P0-002` — Configure branch protection for main
- [ ] `P0-003` — Add root .gitignore and .gitattributes
- [ ] `P0-004` — Add .editorconfig
- [ ] `P0-005` — Create the monorepo directory structure
- [ ] `P0-006` — Initialize the pnpm workspace
- [ ] `P0-007` — Pin Node.js and pnpm versions
- [ ] `P0-008` — Initialize the Python uv workspace
- [ ] `P0-009` — Pin the Python runtime version
- [ ] `P0-010` — Create the initial FastAPI service
- [ ] `P0-011` — Create the initial Next.js assistant application
- [ ] `P0-012` — Create the initial Next.js administration application
- [ ] `P0-013` — Create the widget-loader package
- [ ] `P0-014` — Create the browser-extension package
- [ ] `P0-015` — Configure Python formatting with Ruff
- [ ] `P0-016` — Configure Python linting with Ruff
- [ ] `P0-017` — Configure Python type checking with mypy
- [ ] `P0-018` — Configure TypeScript strict mode
- [ ] `P0-019` — Configure ESLint
- [ ] `P0-020` — Configure Prettier
- [ ] `P0-021` — Configure Markdown, shell, Docker and YAML linting
- [ ] `P0-022` — Configure pytest
- [ ] `P0-023` — Configure Vitest and React Testing Library
- [ ] `P0-024` — Configure Playwright
- [ ] `P0-025` — Create root Makefile commands
- [ ] `P0-026` — Configure pre-commit hooks
- [ ] `P0-027` — Configure Gitleaks
- [ ] `P0-028` — Configure Dependabot
- [ ] `P0-029` — Configure GitHub Dependency Review
- [ ] `P0-030` — Configure CodeQL
- [ ] `P0-031` — Configure Trivy repository scanning
- [ ] `P0-032` — Create service Dockerfiles
- [ ] `P0-033` — Add container health checks
- [ ] `P0-034` — Create local Docker Compose configuration
- [ ] `P0-035` — Add local PostgreSQL
- [ ] `P0-036` — Add local object-storage emulator
- [ ] `P0-037` — Add local queue emulator or queue abstraction
- [ ] `P0-038` — Add environment configuration validation
- [ ] `P0-039` — Create .env.example
- [ ] `P0-040` — Add structured JSON logging
- [ ] `P0-041` — Add request-correlation middleware
- [ ] `P0-042` — Add OpenTelemetry bootstrap
- [ ] `P0-043` — Implement /health/live
- [ ] `P0-044` — Implement /health/ready
- [ ] `P0-045` — Implement RFC 9457 API error format
- [ ] `P0-046` — Create the base CI workflow
- [ ] `P0-047` — Add application-build jobs to CI
- [ ] `P0-048` — Add container-image scanning
- [ ] `P0-049` — Create the development deployment workflow
- [ ] `P0-050` — Configure deployment through OIDC
- [ ] `P0-051` — Add immutable image tagging
- [ ] `P0-052` — Create README.md
- [ ] `P0-053` — Create AGENTS.md
- [ ] `P0-054` — Create docs/ARCHITECTURE.md
- [ ] `P0-055` — Create docs/DECISIONS.md and initial ADRs
- [ ] `P0-056` — Create docs/PLAN.md
- [ ] `P0-057` — Create docs/OPERATIONS.md
- [ ] `P0-058` — Create SECURITY.md
- [ ] `P0-059` — Create CONTRIBUTING.md
- [ ] `P0-060` — Create docs/TESTING.md
- [ ] `P0-061` — Create prompt-library skeleton
- [ ] `P0-062` — Create evaluation-library skeleton
- [ ] `P0-063` — Implement the version endpoint demonstration
- [ ] `P0-064` — Deploy the version endpoint to development
- [ ] `P0-065` — Add post-deployment smoke test
- [ ] `P0-066` — Demonstrate rollback

## Exit gate

- [ ] A small change passes local checks and pull-request review.
- [ ] CI builds and scans affected artifacts.
- [ ] The immutable artifact deploys to development and passes smoke tests.
- [ ] The deployment can be rolled back.
- [ ] A new engineer can reproduce the process from repository documentation.