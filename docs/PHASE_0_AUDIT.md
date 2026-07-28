# Phase 0 Engineering Foundation Audit

**Audit date:** 2026-07-27
**Latest remediation update:** 2026-07-28
**Verdict:** FAIL
**Repository remediation status:** PARTIAL
**Phase 1 gate:** Blocked until every item in the priority-zero section is resolved and verified.

## Scope

This audit reviewed the completed Phase 0 engineering foundation against:

- `AGENTS.md`;
- `docs/ARCHITECTURE.md`;
- `docs/ENGINEERING_FOUNDATION.md`;
- `docs/PLAN.md`;
- the Phase 0 task definitions and generated task views;
- CI and security workflows;
- Dockerfiles and Docker Compose;
- dependency manifests and lockfiles;
- lint, formatting, type-check, and test configuration;
- health checks, structured logging, and telemetry;
- development deployment, smoke-test, and rollback procedures.

The audit tested whether a small change can be implemented, checked, reviewed, built, deployed, smoke-tested, and rolled back through a repeatable process.

## Executive summary

Phase 0 does not meet its exit criterion. The most serious issue is that startup configuration validation can expose credentials in exception output. Local and CI quality gates are also incomplete or broken, the deployment workflow is not gated by successful checks, the deployed artifact is not smoke-tested, and no executable rollback exists.

Phase 1 must not begin until the priority-zero blockers below are fixed and the full Phase 0 exit gate is rerun with recorded evidence.

### 2026-07-28 remediation status

Repository-side fixes have been implemented for several blockers, but the Phase
0 exit gate is not yet complete. The verdict remains `FAIL` because credential
rotation, active remote branch protection, GitHub-hosted CI/security runs, a
successful development deployment, deployed smoke evidence, and rollback
evidence still require external verification.

Local evidence recorded on 2026-07-28:

- Configuration validation uses secret types, hides Pydantic validation inputs,
  sanitizes startup failures, and has tests for loader, logging, and import-time
  startup failure paths.
- `make check` no longer depends on mutating format commands; it delegates to
  deterministic `format-check`, lint, type, test, and security gates.
- Python workspace checks pass with `uv run --all-packages`: Ruff format check,
  Ruff lint, mypy strict checks, and pytest.
- Prettier, ESLint, TypeScript, Vitest, Playwright, pre-commit, npm audit, and
  Docker Compose config checks pass locally.
- `make check` passes locally after installing `make` through the user-scoped
  Winget `ezwinports.make` package.
- The API Docker image builds locally with immutable build metadata arguments
  using the pinned `python:3.13-alpine` digest.
- Local Trivy image scanning with vulnerability, misconfiguration, and secret
  scanners reports zero high or critical findings for
  `knowledge-assistant-api:local-test`.
- Local Docker Compose deployment starts PostgreSQL, object storage, and the API;
  the API container reports healthy.
- Deployment smoke against `BASE_URL=http://127.0.0.1:8000` passes.
- `/version` reports `commit_sha=local-test` and the supplied build timestamp in
  the local Compose deployment.
- The API container runs as user `app` and has OCI labels for version, revision,
  created time, and source.
- Raw API container logs parse as JSON.
- Deployment smoke tests now require `BASE_URL`, accept HTTPS, and cannot start a
  local Uvicorn process as a substitute for a deployed service.
- Development deployment is wired to run after successful CI, build/push one
  immutable digest, scan that digest, validate the target container name, wait
  for ECS stability, smoke-test the deployed endpoint, and verify deployed
  commit provenance.
- A rollback workflow exists for a known-good ECS task definition ARN and
  performs service-stability and smoke verification.
- Readiness now includes bounded dependency probes and returns HTTP 503 when a
  required readiness dependency fails; `/health/startup` and authenticated
  `/health/dependencies` are implemented.
- Runtime logging applies the validated `LOG_LEVEL` and configures application,
  Uvicorn error, and Uvicorn access loggers for JSON output.
- Build metadata is passed as Docker build arguments, OCI labels, Compose runtime
  environment, and deployment workflow values; release environments fail when
  provenance is absent.
- The API container uses pinned image references and a non-root application user.
- Trivy scans include secrets and do not ignore unfixed high or critical
  findings; Dependabot covers npm, uv, GitHub Actions, Docker, and Terraform
  directories.
- Dependency Review is wired with a temporary explicit exception because GitHub
  reports dependency graph is not enabled or unsupported for this repository.
  The workflow records this condition in the job summary and must have
  `continue-on-error` removed after dependency graph is enabled.
- `codex/tasks/task-index.csv` was regenerated from the authoritative
  `codex/tasks/tasks.json`.

Remaining external or environment-blocked evidence:

- Rotate the previously exposed OpenAI credential outside this repository.
- Apply and verify active remote branch protection or repository rulesets through
  the GitHub API.
- Enable GitHub dependency graph for this repository and remove the temporary
  Dependency Review workflow exception.
- Run GitHub-hosted CI, CodeQL, Dependency Review, Gitleaks, Trivy, deployment,
  and rollback workflows successfully on a reviewable pull request.
- Deploy the immutable digest to development and attach health, readiness,
  version, smoke, provenance, and rollback evidence.

## Priority-zero blockers before Phase 1

Resolve these items in order because later verification depends on the earlier controls.

1. Rotate the OpenAI credential exposed during validation-error testing and prevent all secret-bearing validation errors.
2. Replace placeholder bootstrap, build, type-check, test, security, and `make check` commands with real deterministic commands.
3. Make the clean CI sequence install all Python workspace packages and pass every configured check.
4. Resolve or formally except all critical and high dependency and container vulnerabilities.
5. Require successful CI and security checks through active branch protection.
6. Build and scan one immutable digest, then deploy that exact digest only after required checks pass.
7. Add deployment stability waiting, deployed-service smoke testing, artifact provenance verification, and executable rollback.
8. Correct readiness so it covers required dependencies and returns a failing status when the service cannot safely receive traffic.
9. Emit structured JSON for application, Uvicorn error, and access logs with request, trace, and span correlation.
10. Reconcile Phase 0 task records and complete all five exit-gate items with reviewable evidence.

## Findings

### Critical

#### P0-AUDIT-001: Configuration validation errors can disclose secrets

##### Affected files

- `services/api/src/icakb_api/configuration.py:15`
- `services/api/src/icakb_api/configuration.py:20`
- `services/api/src/icakb_api/configuration.py:24`
- `services/api/src/icakb_api/configuration.py:51`
- `services/api/src/icakb_api/app.py:62`

##### Evidence

Importing the application with incomplete configuration produced a Pydantic traceback whose rendered input contained the value of `OPENAI_API_KEY`. The credential is stored as an ordinary `str`, validation inputs are not hidden, and import-time application construction makes the failure occur during service startup. The secret could therefore enter CI, platform, or container logs.

The credential value is intentionally omitted from this report.

##### Required fix

- Rotate the exposed credential immediately.
- Use `SecretStr` or an equivalent secret type for credentials and other sensitive configuration.
- Enable `hide_input_in_errors=True`.
- Sanitize startup failures before they are logged.
- Add negative tests proving that API keys, passwords, connection strings, cookies, and tokens never appear in validation exceptions or logs.

### High

#### P0-AUDIT-002: Required local and CI checks are non-functional

##### Affected files

- `Makefile:6-33`
- `package.json:11-23`
- `.github/workflows/ci.yml:32-42`
- `pyproject.toml:20-26`
- `.pre-commit-config.yaml:1-42`

##### Evidence

- `make check` invokes targets that only print placeholder messages.
- Root `pnpm build`, `pnpm typecheck`, and `pnpm test` exit successfully after printing `Implement in Phase 0`.
- A clean `uv sync --frozen` followed by `uv run pytest` failed during collection with missing FastAPI and Pydantic modules.
- Adding `--all-packages` for audit purposes installed the workspace correctly and all 12 Python tests passed.
- Ruff found five files requiring formatting and one unused import.
- mypy is configured but is not installed.
- Pre-commit failed for script executable modes, line endings, missing final newlines, Markdown errors, and YAML errors.
- Prettier failed on 16 files.

##### Required fix

- Implement real bootstrap, format, lint, type-check, test, security, and check targets.
- Lock Ruff and mypy as development dependencies.
- Use `uv sync --frozen --all-packages` in CI.
- Run every required gate explicitly.
- Correct script executable modes and all current pre-commit, Ruff, mypy, and Prettier failures.
- Ensure no placeholder command can return a successful release-check result.

#### P0-AUDIT-003: Development deployment is not gated, verified, or reversible

##### Affected files

- `.github/workflows/deploy-development.yml:3-130`
- `.github/workflows/ci.yml:91-100`
- `.github/workflows/trivy.yml:38-57`
- `docs/OPERATIONS.md:44-68`

##### Evidence

- Deployment starts independently on every push to `main`; it does not wait for CI or security workflows.
- The workflow rebuilds an image independently from the image scanned in the Trivy workflow.
- `aws ecs update-service` is the last step. There is no `services-stable` wait, health verification, smoke test, or automatic rollback.
- No rollback input or job exists even though the operations guide claims a previous task-definition revision can be reused.
- The task-definition transformation does not fail when the configured container name matches no container.
- No successful development deployment record was available.

##### Required fix

- Trigger deployment only after all required CI and security workflows succeed.
- Publish, scan, attest, and deploy one immutable digest.
- Validate that exactly one task-definition container is updated.
- Wait for ECS service stability.
- Execute health and version smoke tests against the deployed endpoint.
- Verify that the deployed SHA or digest matches the intended artifact.
- Add an explicit rollback workflow accepting a known-good digest or task-definition ARN, followed by stability and smoke verification.

#### P0-AUDIT-004: The default smoke command bypasses the deployed service

##### Affected files

- `Makefile:15-16`
- `tests/smoke/test_version_endpoint.py:19-20`
- `tests/smoke/test_version_endpoint.py:69-114`
- `tests/smoke/test_version_endpoint.py:117-122`
- `docs/OPERATIONS.md:28-42`

##### Evidence

When `BASE_URL` is absent, the smoke test starts a separate local Uvicorn process on a free port. Consequently, running `make deploy-version-endpoint` followed by `make smoke-version-endpoint` does not verify the Compose container. The isolated test passed without a Compose deployment.

The test also rejects HTTPS endpoints with `startswith("http://")`.

##### Required fix

- Require `BASE_URL` for deployment smoke tests.
- Have the Compose smoke target explicitly use `http://127.0.0.1:8000`.
- Accept and prefer HTTPS for shared development environments.
- Move the self-managed Uvicorn test into integration testing so it cannot be mistaken for deployment verification.

#### P0-AUDIT-005: Readiness reports success without checking required dependencies

##### Affected files

- `services/api/src/icakb_api/health.py:45-78`
- `services/api/src/icakb_api/app.py:51-57`
- `docs/ENGINEERING_FOUNDATION.md:108-113`

##### Evidence

`/health/ready` checks only constant startup state, configuration parsing, and telemetry bootstrap. It does not check PostgreSQL, migrations, queue, object storage, or essential internal resources.

The deployed Compose response reported `ready` with only startup, configuration, and telemetry checks. `/health/startup` and `/health/dependencies` are not implemented.

##### Required fix

- Add bounded dependency probes with explicit timeouts.
- Return a non-success HTTP status when readiness requirements fail.
- Check database connectivity and migration state before accepting traffic.
- Implement `/health/startup`.
- Implement authenticated `/health/dependencies` diagnostics for database, queue, storage, OpenAI reachability, retrieval configuration, and telemetry.

#### P0-AUDIT-006: High and critical vulnerabilities are present and may be ignored

##### Affected files

- `pnpm-lock.yaml:1059`
- `pnpm-lock.yaml:2012`
- `pnpm-lock.yaml:2016`
- `pnpm-lock.yaml:2138`
- `services/api/Dockerfile:3`
- `.github/workflows/trivy.yml:27-36`
- `.github/workflows/trivy.yml:48-57`

##### Evidence

`pnpm audit --audit-level high` reported four high-severity and one moderate vulnerability, including Sharp/libvips, PostCSS file disclosure and path traversal, and brace-expansion denial of service.

Docker Scout reported one critical and two high vulnerabilities in the built API image. Trivy is configured with `ignore-unfixed: true`, so unfixed critical and high findings may not fail CI. No approved security exception was found.

##### Required fix

- Upgrade or override affected JavaScript dependencies.
- Use a patched minimal base image pinned by digest.
- Do not silently ignore unfixed critical or high vulnerabilities.
- Require any temporary exception to have an owner, justification, compensating control, expiry, tracking issue, and security approval.

#### P0-AUDIT-007: Branch protection does not require CI

##### Affected files

- `.github/branch-protection/main.json:2`
- `.github/branch-protection/README.md:14-18`

##### Evidence

- `required_status_checks` is `null`.
- The branch-protection guide says the policy must be updated after CI exists, but it was not updated.
- GitHub reported no status checks or workflow runs for the remote `main` HEAD reviewed during the audit.
- The Phase 0 implementation was staged locally across 95 files with no corresponding PR, CI, or review evidence.

##### Required fix

- Apply branch protection or a repository ruleset requiring all CI and security checks.
- Verify the active remote rule through the GitHub API.
- Require successful review and checks before merging or marking the Phase 0 exit gate complete.

### Medium

#### P0-AUDIT-008: Runtime logging is not structured and ignores `LOG_LEVEL`

##### Affected files

- `services/api/src/icakb_api/app.py:25-30`
- `python-packages/telemetry-python/src/telemetry_python/logging.py:100-135`
- `services/api/Dockerfile:31`

##### Evidence

- Compose emitted ordinary Uvicorn text logs rather than JSON.
- Access logs did not include request, trace, or span correlation.
- With `LOG_LEVEL=ERROR`, the configured root logger remained at `INFO`.

##### Required fix

- Configure application, Uvicorn error, and Uvicorn access loggers with the JSON formatter.
- Parse and apply the validated log level.
- Add container-level tests that parse every emitted line as JSON and verify required correlation and redaction fields.

#### P0-AUDIT-009: Build provenance cannot identify the deployed revision

##### Affected files

- `services/api/Dockerfile:1-31`
- `services/api/src/icakb_api/version.py:27-40`
- `compose.yaml:7-19`

##### Evidence

The Compose version endpoint returned:

```json
{
  "version": "0.0.0-dev",
  "commit_sha": "unknown",
  "build_time": "container process startup time"
}
```

The Dockerfile does not inject version, commit SHA, or build timestamp. Smoke testing therefore cannot prove which immutable revision is running.

##### Required fix

- Pass immutable build metadata as build arguments, OCI labels, and runtime values.
- Fail release builds when required provenance is absent.
- Verify the expected SHA or digest during post-deployment smoke testing.

#### P0-AUDIT-010: Toolchain and security automation are incomplete or mutable

##### Affected files

- `docs/ENGINEERING_FOUNDATION.md:49-58`
- `.pre-commit-config.yaml:1-42`
- `.github/workflows/ci.yml:24-42`
- `services/api/Dockerfile:11`
- `.github/dependabot.yml:1-14`
- `.github/workflows/trivy.yml:27-57`

##### Evidence

The following required controls are missing or not pinned:

- Ruff and mypy execution;
- shfmt;
- Terraform formatting and validation;
- TFLint;
- actionlint in CI;
- a pinned uv installer in CI;
- an immutable uv container reference;
- GitHub Actions pinned by commit SHA;
- Dependabot coverage for Docker images and Terraform providers;
- Trivy secret scanning.

##### Required fix

- Lock all required tools and CI actions.
- Add every required gate to the local and CI check paths.
- Add Docker and Terraform Dependabot ecosystems.
- Add Trivy secret and infrastructure scanning.
- Exclude generated lockfiles from rules that cannot produce actionable formatting changes.

#### P0-AUDIT-011: The API container runs as root and uses mutable base references

##### Affected file

- `services/api/Dockerfile:3-31`

##### Evidence

Image inspection returned an empty configured user, meaning the application runs as root. The Dockerfile also uses mutable `python:3.13-slim` and `ghcr.io/astral-sh/uv:latest` references.

##### Required fix

- Pin all base and copied images by digest.
- Create and use a non-root application user.
- Use a minimal runtime stage without build tooling.
- Restrict filesystem write access to required temporary paths.

#### P0-AUDIT-012: Phase 0 completion records contradict one another

##### Affected files

- `codex/tasks/tasks.json:536-540`
- `codex/tasks/tasks.json:1456-1506`
- `codex/tasks/task-index.csv:8-67`
- `codex/tasks/by-phase/phase-0.md:70-80`

##### Evidence

- `tasks.json`: 42 tasks done and 24 in review.
- `task-index.csv`: 38 tasks done, 27 in review, and one backlog.
- The Phase 0 Markdown checklist marks all 66 tasks complete.
- All five Phase 0 exit-gate items remain unchecked.
- `P0-064`, `P0-065`, and `P0-066` remain `in_review` in the authoritative task catalog.

##### Required fix

- Treat `tasks.json` as the single source of truth.
- Generate the CSV and phase Markdown views from the authoritative catalog.
- Do not mark a task complete until its checks, review, deployment, smoke, and rollback evidence exist.

### Low

#### P0-AUDIT-013: Local Next.js type checking is sensitive to generated artifacts

##### Affected files

- `apps/assistant-web/tsconfig.json:12-13`
- `apps/admin-web/tsconfig.json:12-13`

##### Evidence

After local development artifacts existed, assistant type checking failed with duplicate `LayoutProps` declarations from `.next/dev/types/routes.d.ts` and `.next/types/routes.d.ts`. A production build succeeded after regenerating `.next`, demonstrating a local/CI state difference.

##### Required fix

- Exclude conflicting generated development output or clean generated types deterministically before type checking.

## Missing Phase 0 requirements

- Functional one-command bootstrap and development environment.
- Real `make check` execution.
- Clean frozen CI installation for the full Python workspace.
- Ruff formatting and linting.
- Strict mypy enforcement.
- shfmt, actionlint, Terraform validation, and TFLint.
- Active required branch status checks.
- Scan-before-deploy of the exact promoted digest.
- Post-deployment stability wait and smoke verification.
- Executable rollback by digest or task-definition revision.
- Accurate immutable version and build provenance.
- Dependency-aware readiness.
- `/health/startup`.
- Authenticated `/health/dependencies`.
- Structured JSON Uvicorn access and error logs with correlation.
- Dependabot coverage for images and Terraform.
- Trivy secret scanning and explicit vulnerability-exception policy.
- Validated mock and sandbox bootstrap paths.
- Evidence of pull-request review, development deployment, promotion, and rollback.

## Commands and results

### Passed

- `uv sync --frozen --all-packages`
- `uv run --all-packages pytest -q` — 12 passed
- `pnpm install --frozen-lockfile` — passed with a local Node-version warning
- `pnpm lint`
- Widget-loader, browser-extension, and administration type checks
- `pnpm test:vitest` — 4 passed
- Assistant and administration Next.js production builds
- `pnpm test:playwright` — 1 passed
- `docker compose config --quiet`
- API Docker build
- Local Compose deployment — API, PostgreSQL, and object storage became healthy
- Smoke test against Compose with explicit `BASE_URL` — 1 passed
- Isolated smoke test without `BASE_URL` — 1 passed
- Gitleaks over filtered repository source — no leaks
- Python dependency audit over the exported lock — no known vulnerabilities
- actionlint
- Hadolint, ShellCheck, and Python compileall within pre-commit

### Failed

- Clean CI Python sequence — workspace dependencies were not installed
- Pre-commit — executable modes, line endings, final newlines, Markdown, and YAML
- Ruff format — five files
- Ruff lint — one unused import
- mypy — executable not installed
- Prettier check — 16 files
- Assistant local type check — duplicate generated Next.js declarations
- `pnpm audit --audit-level high` — four high and one moderate vulnerability
- Docker Scout image scan — one critical and two high vulnerabilities
- `make check` — `make` unavailable in the audit environment and repository targets are placeholders
- Root `pnpm build`, `pnpm typecheck`, and `pnpm test` — misleading success through placeholder commands

### Not proven

- Actual GitHub OIDC, ECR, and ECS development deployment
- GitHub-hosted CodeQL, Dependency Review, and Trivy runs
- Active remote branch-protection configuration
- Rollback to a prior immutable artifact
- Staging and production promotion of the same digest

## Phase 0 revalidation gate

After remediation, Phase 0 may be reconsidered complete only when all of the following evidence is attached to a reviewable change:

- a clean bootstrap from a new checkout;
- a successful `make check`;
- successful required PR and security checks;
- an approved pull request;
- one immutable, scanned artifact digest;
- a successful development deployment of that digest;
- post-deployment health, readiness, version, and smoke evidence;
- a successful rollback to a previous known-good digest;
- post-rollback health and smoke evidence;
- synchronized task catalog, generated task views, and completed Phase 0 exit gate.

Until that evidence exists, Phase 1 remains blocked.
