# Engineering Foundation

## Repository model

Use a polyglot monorepo with independently deployable applications and services:

```text
apps/                 Browser-facing applications
services/             Independently deployable Python services
packages/             Shared TypeScript packages
python-packages/      Shared Python packages
prompts/              Versioned prompt source assets
evals/                Evaluation datasets, graders, fixtures, and reports
tests/                Cross-service end-to-end, security, tenant, and performance tests
infra/                Terraform modules and environment definitions
deploy/               Environment deployment configuration
docs/                 Architecture, plan, testing, security, and operations documentation
codex/                Agent workflow and machine-readable task catalog
```

## Conventions

### TypeScript

- Files and directories: `kebab-case`.
- Variables and functions: `camelCase`.
- Components and types: `PascalCase`.
- Constants: `UPPER_SNAKE_CASE`.
- Strict TypeScript is mandatory.
- Validate external `unknown` values; avoid `any`.

### Python

- Modules, functions, and variables: `snake_case`.
- Classes and exceptions: `PascalCase`.
- Constants: `UPPER_SNAKE_CASE`.
- Complete public type annotations are mandatory.
- Use Pydantic models at system boundaries.
- Keep domain logic independent of FastAPI, database, OpenAI, and cloud implementations.

## Dependency management

- pnpm workspace with one committed lockfile and a pinned pnpm version.
- uv workspace with `pyproject.toml`, one committed `uv.lock`, and a pinned Python version.
- Frozen or locked installs in CI.
- Weekly dependency update pull requests.
- Review maintenance, license, vulnerabilities, transitive size, and runtime compatibility before adding dependencies.

## Formatting, linting, and types

- Python: Ruff formatting and linting; mypy strict mode.
- TypeScript and React: Prettier, ESLint, and `tsc --noEmit`.
- Markdown: Prettier and markdownlint.
- YAML: Prettier and yamllint.
- Shell: shfmt and ShellCheck.
- Dockerfiles: Hadolint.
- Terraform: `terraform fmt`, `terraform validate`, and TFLint.
- GitHub Actions: actionlint.

## Testing

- Python unit and integration tests: pytest, pytest-asyncio, HTTPX.
- TypeScript unit tests: Vitest and React Testing Library.
- Browser end-to-end tests: Playwright.
- Contract tests: OpenAPI, widget messages, queue messages, error schemas, retrieval contracts.
- RAG evaluations: groundedness, citations, abstention, conflicting and superseded documents, prompt injection, tenant isolation, provider failures, and multi-turn context.
- Live provider tests use a dedicated non-production OpenAI project, synthetic documents, and strict cost limits.

## Security automation

- Gitleaks locally and in CI.
- GitHub secret scanning and push protection when available.
- GitHub Dependency Review on pull requests.
- CodeQL static analysis.
- Trivy repository, image, secret, and infrastructure scans.
- Dependabot for packages, actions, images, and Terraform providers.

## Development environment

A single bootstrap path must verify pinned tools, install dependencies, install hooks, start local dependencies, apply migrations, load synthetic fixtures, and verify health endpoints. Local development must support:

- **Mock mode:** deterministic retrieval and generation fixtures; no OpenAI key required.
- **Sandbox mode:** dedicated non-production project, synthetic documents, and explicit opt-in.

## Deployment environments

- Local
- Pull-request preview
- Shared development
- Production-like staging
- Production

Each environment is isolated. CI uses workload identity or OIDC, not long-lived cloud keys. Images are immutable and promoted without rebuilding.

## CI pipeline

Pull requests run formatting, linting, types, unit tests, integration tests, contract tests, secret scanning, dependency review, static analysis, builds, container and infrastructure scans, browser smoke tests, and offline RAG evaluations. Main builds immutable artifacts and deploys to development. Staging and production promote the same digest with protected approvals and post-deployment verification.

## Logging and errors

- Structured JSON logs to stdout.
- Request, trace, and span correlation.
- No raw prompts, user messages, retrieved passages, document bodies, tokens, or cookies by default.
- RFC 9457 problem details for non-streaming API errors.
- Typed terminal error events for streams.
- Stable application error codes and bounded retries for transient idempotent operations.

## Health checks

- `/health/live`: process only; no dependencies.
- `/health/ready`: startup, configuration, database, migrations, and essential internal resources.
- `/health/startup`: slower initialization completion.
- `/health/dependencies`: authenticated operational diagnostics for database, queue, storage, OpenAI reachability, retrieval configuration, and telemetry.

## Exit criterion

A small change can be implemented, tested, reviewed, built, deployed, verified, promoted, and rolled back through a repeatable process.
