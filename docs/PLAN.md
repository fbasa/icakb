# Delivery Plan

This plan contains the approved delivery phases and the atomic task catalog. The machine-readable source is `codex/tasks/tasks.json`.

## Phase 0 — Engineering Foundation

**Objective:** Establish a repeatable process for implementing, testing, reviewing, building, deploying, and rolling back a small change.

| ID     | Atomic task                                           |
| ------ | ----------------------------------------------------- |
| P0-001 | Create the Git repository                             |
| P0-002 | Configure branch protection for main                  |
| P0-003 | Add root .gitignore and .gitattributes                |
| P0-004 | Add .editorconfig                                     |
| P0-005 | Create the monorepo directory structure               |
| P0-006 | Initialize the pnpm workspace                         |
| P0-007 | Pin Node.js and pnpm versions                         |
| P0-008 | Initialize the Python uv workspace                    |
| P0-009 | Pin the Python runtime version                        |
| P0-010 | Create the initial FastAPI service                    |
| P0-011 | Create the initial Next.js assistant application      |
| P0-012 | Create the initial Next.js administration application |
| P0-013 | Create the widget-loader package                      |
| P0-014 | Create the browser-extension package                  |
| P0-015 | Configure Python formatting with Ruff                 |
| P0-016 | Configure Python linting with Ruff                    |
| P0-017 | Configure Python type checking with mypy              |
| P0-018 | Configure TypeScript strict mode                      |
| P0-019 | Configure ESLint                                      |
| P0-020 | Configure Prettier                                    |
| P0-021 | Configure Markdown, shell, Docker and YAML linting    |
| P0-022 | Configure pytest                                      |
| P0-023 | Configure Vitest and React Testing Library            |
| P0-024 | Configure Playwright                                  |
| P0-025 | Create root Makefile commands                         |
| P0-026 | Configure pre-commit hooks                            |
| P0-027 | Configure Gitleaks                                    |
| P0-028 | Configure Dependabot                                  |
| P0-029 | Configure GitHub Dependency Review                    |
| P0-030 | Configure CodeQL                                      |
| P0-031 | Configure Trivy repository scanning                   |
| P0-032 | Create service Dockerfiles                            |
| P0-033 | Add container health checks                           |
| P0-034 | Create local Docker Compose configuration             |
| P0-035 | Add local PostgreSQL                                  |
| P0-036 | Add local object-storage emulator                     |
| P0-037 | Add local queue emulator or queue abstraction         |
| P0-038 | Add environment configuration validation              |
| P0-039 | Create .env.example                                   |
| P0-040 | Add structured JSON logging                           |
| P0-041 | Add request-correlation middleware                    |
| P0-042 | Add OpenTelemetry bootstrap                           |
| P0-043 | Implement /health/live                                |
| P0-044 | Implement /health/ready                               |
| P0-045 | Implement RFC 9457 API error format                   |
| P0-046 | Create the base CI workflow                           |
| P0-047 | Add application-build jobs to CI                      |
| P0-048 | Add container-image scanning                          |
| P0-049 | Create the development deployment workflow            |
| P0-050 | Configure deployment through OIDC                     |
| P0-051 | Add immutable image tagging                           |
| P0-052 | Create README.md                                      |
| P0-053 | Create AGENTS.md                                      |
| P0-054 | Create docs/ARCHITECTURE.md                           |
| P0-055 | Create docs/DECISIONS.md and initial ADRs             |
| P0-056 | Create docs/PLAN.md                                   |
| P0-057 | Create docs/OPERATIONS.md                             |
| P0-058 | Create SECURITY.md                                    |
| P0-059 | Create CONTRIBUTING.md                                |
| P0-060 | Create docs/TESTING.md                                |
| P0-061 | Create prompt-library skeleton                        |
| P0-062 | Create evaluation-library skeleton                    |
| P0-063 | Implement the version endpoint demonstration          |
| P0-064 | Deploy the version endpoint to development            |
| P0-065 | Add post-deployment smoke test                        |
| P0-066 | Demonstrate rollback                                  |

### Exit gate

- Current gate status: **Blocked** by the findings and revalidation requirements
  in the [Phase 0 audit](PHASE_0_AUDIT.md).
- A small change passes local checks and pull-request review.
- CI builds and scans affected artifacts.
- The immutable artifact deploys to development and passes smoke tests.
- The deployment can be rolled back.
- A new engineer can reproduce the process from repository documentation.

## Phase 1 — Identity and Tenant Foundation

### Entry gate

`PHASE-0-EXIT` is not satisfied while the verdict in the
[Phase 0 audit](PHASE_0_AUDIT.md) is `FAIL`. Do not begin a Phase 1 task until:

- every priority-zero blocker in the audit is resolved;
- the audit revalidation gate has recorded evidence;
- every Phase 0 task prerequisite is complete in `codex/tasks/tasks.json`; and
- every Phase 0 exit-gate item above is complete.

**Objective:** Create the authentication, authorization, tenancy, session, audit, and database-isolation layer.

| ID     | Atomic task                                       |
| ------ | ------------------------------------------------- |
| P1-001 | Define the tenant domain model                    |
| P1-002 | Define the user domain model                      |
| P1-003 | Define roles, groups and memberships              |
| P1-004 | Create tenant database tables                     |
| P1-005 | Create user database tables                       |
| P1-006 | Create role and group tables                      |
| P1-007 | Add typed tenant identifiers                      |
| P1-008 | Add typed user identifiers                        |
| P1-009 | Define identity-provider configuration schema     |
| P1-010 | Implement OIDC discovery loading                  |
| P1-011 | Implement JWT signature validation                |
| P1-012 | Implement issuer and audience validation          |
| P1-013 | Implement token-expiry validation                 |
| P1-014 | Implement authenticated-request middleware        |
| P1-015 | Map external subject to internal user             |
| P1-016 | Implement just-in-time user provisioning          |
| P1-017 | Implement disabled-user handling                  |
| P1-018 | Implement tenant resolution                       |
| P1-019 | Prevent request-supplied tenant override          |
| P1-020 | Define authorization-policy interface             |
| P1-021 | Implement role-based authorization checks         |
| P1-022 | Implement group-based authorization context       |
| P1-023 | Implement PostgreSQL tenant context               |
| P1-024 | Create initial Row-Level Security policies        |
| P1-025 | Add RLS negative tests                            |
| P1-026 | Define short-lived assistant session-token schema |
| P1-027 | Implement session-token issuance                  |
| P1-028 | Implement session-token validation                |
| P1-029 | Add session revocation versioning                 |
| P1-030 | Define audit-event schema                         |
| P1-031 | Create audit-event storage                        |
| P1-032 | Record authentication events                      |
| P1-033 | Record authorization denials                      |
| P1-034 | Add tenant-management API contracts               |
| P1-035 | Implement tenant creation                         |
| P1-036 | Implement tenant disablement                      |
| P1-037 | Implement user-status administration              |
| P1-038 | Add tenant and user metrics                       |
| P1-039 | Document identity flow                            |
| P1-040 | Document tenant-isolation design                  |
| P1-041 | Create tenant-isolation test suite                |

### Exit gate

- Users resolve to one verified tenant.
- Short-lived assistant sessions can be issued and validated.
- Disabled users and tenants are rejected.
- PostgreSQL RLS prevents cross-tenant access.
- Authentication and authorization events are auditable.
- Tenant-isolation tests pass in CI.

## Phase 2 — Document Ingestion

**Objective:** Create a reliable and reversible document lifecycle from source systems to hosted File Search.

| ID     | Atomic task                                  |
| ------ | -------------------------------------------- |
| P2-001 | Define data-source domain model              |
| P2-002 | Define document domain model                 |
| P2-003 | Define document-version model                |
| P2-004 | Define ingestion-job model                   |
| P2-005 | Create source database tables                |
| P2-006 | Create document database tables              |
| P2-007 | Create document-version tables               |
| P2-008 | Create ingestion-job tables                  |
| P2-009 | Apply RLS to ingestion tables                |
| P2-010 | Define supported-file policy                 |
| P2-011 | Implement upload-request API                 |
| P2-012 | Implement presigned object upload            |
| P2-013 | Implement upload-completion callback         |
| P2-014 | Validate file size and declared type         |
| P2-015 | Detect actual file type                      |
| P2-016 | Add malware-scanning adapter                 |
| P2-017 | Quarantine failed or suspicious uploads      |
| P2-018 | Define queue-message schema                  |
| P2-019 | Implement job publishing                     |
| P2-020 | Implement worker message consumption         |
| P2-021 | Add ingestion idempotency key                |
| P2-022 | Add worker lease and visibility handling     |
| P2-023 | Define extraction-adapter interface          |
| P2-024 | Implement PDF extraction                     |
| P2-025 | Implement DOCX extraction                    |
| P2-026 | Implement text and Markdown extraction       |
| P2-027 | Implement unsupported-format failure         |
| P2-028 | Normalize extracted text                     |
| P2-029 | Calculate source-content checksum            |
| P2-030 | Implement duplicate-content detection        |
| P2-031 | Define document metadata schema              |
| P2-032 | Validate metadata values                     |
| P2-033 | Map source permissions to retrieval metadata |
| P2-034 | Define OpenAI vector-store adapter           |
| P2-035 | Implement tenant vector-store creation       |
| P2-036 | Implement OpenAI file upload                 |
| P2-037 | Apply retrieval metadata to indexed files    |
| P2-038 | Poll indexing completion                     |
| P2-039 | Verify indexed-file association              |
| P2-040 | Persist provider file references             |
| P2-041 | Mark ingestion success                       |
| P2-042 | Implement transient-error classification     |
| P2-043 | Implement bounded retries                    |
| P2-044 | Implement dead-letter handling               |
| P2-045 | Add failed-job replay command                |
| P2-046 | Implement document deletion request          |
| P2-047 | Delete provider-indexed file                 |
| P2-048 | Delete or retain canonical object by policy  |
| P2-049 | Invalidate document caches                   |
| P2-050 | Verify deletion completion                   |
| P2-051 | Implement reconciliation job                 |
| P2-052 | Add ingestion metrics                        |
| P2-053 | Add ingestion traces                         |
| P2-054 | Add ingestion structured logs                |
| P2-055 | Add ingestion-status API                     |
| P2-056 | Add document-list API                        |
| P2-057 | Add document-version API                     |
| P2-058 | Define Google Drive connector interface      |
| P2-059 | Implement Drive OAuth credential storage     |
| P2-060 | Implement Drive folder configuration         |
| P2-061 | Implement initial Drive discovery sync       |
| P2-062 | Implement incremental Drive sync             |
| P2-063 | Propagate Drive deletions                    |
| P2-064 | Add connector health status                  |
| P2-065 | Create synthetic ingestion fixtures          |
| P2-066 | Add ingestion integration tests              |
| P2-067 | Add ingestion recovery runbook               |

### Exit gate

- Documents can be uploaded, validated, indexed, updated, reconciled, and deleted.
- Duplicate ingestion is idempotent.
- Failed jobs are observable and recoverable.
- Drive synchronization propagates creation, modification, and deletion.
- No document is searchable before metadata and indexing verification.

## Phase 3 — Retrieval and Answer Generation

**Objective:** Provide grounded, cited, permission-filtered answers through one stable API.

| ID     | Atomic task                                          |
| ------ | ---------------------------------------------------- |
| P3-001 | Define retrieval request contract                    |
| P3-002 | Define retrieval result contract                     |
| P3-003 | Define retrieval-adapter interface                   |
| P3-004 | Implement File Search retrieval adapter              |
| P3-005 | Implement mandatory tenant-store selection           |
| P3-006 | Implement metadata-filter builder                    |
| P3-007 | Reject unsupported filter combinations               |
| P3-008 | Add retrieval-filter unit tests                      |
| P3-009 | Add cross-tenant retrieval tests                     |
| P3-010 | Define conversation domain model                     |
| P3-011 | Create conversation database tables                  |
| P3-012 | Create message database tables                       |
| P3-013 | Apply RLS to conversation tables                     |
| P3-014 | Define query API contract                            |
| P3-015 | Implement conversation creation                      |
| P3-016 | Implement user-message validation                    |
| P3-017 | Implement conversation ownership check               |
| P3-018 | Create base system prompt                            |
| P3-019 | Create citation-policy prompt fragment               |
| P3-020 | Create insufficient-evidence prompt                  |
| P3-021 | Create retrieved-content delimiter                   |
| P3-022 | Add prompt manifest entries                          |
| P3-023 | Implement prompt-variable validation                 |
| P3-024 | Implement retrieval orchestration                    |
| P3-025 | Limit retrieval result count                         |
| P3-026 | Implement evidence normalization                     |
| P3-027 | Implement citation identifier mapping                |
| P3-028 | Implement Responses API adapter                      |
| P3-029 | Build grounded-generation request                    |
| P3-030 | Implement server-sent event streaming                |
| P3-031 | Implement streaming cancellation                     |
| P3-032 | Parse provider citations                             |
| P3-033 | Validate citation references                         |
| P3-034 | Persist completed assistant response                 |
| P3-035 | Persist failed-response state                        |
| P3-036 | Implement insufficient-evidence decision             |
| P3-037 | Implement no-document-access response                |
| P3-038 | Implement bounded conversation history               |
| P3-039 | Implement token-budget calculation                   |
| P3-040 | Implement provider timeout handling                  |
| P3-041 | Implement provider rate-limit handling               |
| P3-042 | Implement provider-unavailable circuit breaker       |
| P3-043 | Add request and provider traces                      |
| P3-044 | Add retrieval metrics                                |
| P3-045 | Add generation metrics                               |
| P3-046 | Redact prompt and evidence content from default logs |
| P3-047 | Create answerable-question evaluation dataset        |
| P3-048 | Create unanswerable-question dataset                 |
| P3-049 | Create citation-correctness dataset                  |
| P3-050 | Create conflicting-document dataset                  |
| P3-051 | Create superseded-document dataset                   |
| P3-052 | Create prompt-injection document dataset             |
| P3-053 | Create tenant-isolation evaluation dataset           |
| P3-054 | Implement offline evaluation runner                  |
| P3-055 | Define initial quality thresholds                    |
| P3-056 | Add evaluation checks to CI                          |
| P3-057 | Document query architecture                          |
| P3-058 | Document model and prompt rollback                   |

### Exit gate

- Every query is tenant- and permission-filtered.
- Answers stream through a stable API.
- Citations map only to authorized evidence.
- Unsupported questions produce evidence-aware abstention.
- Provider failures have stable behavior.
- RAG and tenant-isolation evaluations pass approved thresholds.

## Phase 4 — Embeddable Widget

**Objective:** Provide a secure framework-independent assistant widget for existing web applications.

| ID     | Atomic task                                  |
| ------ | -------------------------------------------- |
| P4-001 | Define public widget configuration schema    |
| P4-002 | Define widget versioning policy              |
| P4-003 | Implement loader script entry point          |
| P4-004 | Implement duplicate-loader protection        |
| P4-005 | Implement launcher Web Component             |
| P4-006 | Implement Shadow DOM styles                  |
| P4-007 | Implement iframe creation                    |
| P4-008 | Configure iframe sandbox attributes          |
| P4-009 | Define host-to-iframe message schemas        |
| P4-010 | Define iframe-to-host message schemas        |
| P4-011 | Implement message origin validation          |
| P4-012 | Implement message schema validation          |
| P4-013 | Implement tenant embed-origin configuration  |
| P4-014 | Enforce embed-origin allowlist               |
| P4-015 | Implement host session-exchange client       |
| P4-016 | Implement secure token handoff to iframe     |
| P4-017 | Prevent token persistence in browser storage |
| P4-018 | Implement assistant iframe application shell |
| P4-019 | Implement authenticated API client           |
| P4-020 | Implement conversation creation UI           |
| P4-021 | Implement message composer                   |
| P4-022 | Implement streaming message renderer         |
| P4-023 | Implement streaming cancellation UI          |
| P4-024 | Implement citation presentation              |
| P4-025 | Implement source-detail view                 |
| P4-026 | Implement insufficient-evidence state        |
| P4-027 | Implement authentication-expired state       |
| P4-028 | Implement service-unavailable state          |
| P4-029 | Implement retry control                      |
| P4-030 | Implement widget open and close behavior     |
| P4-031 | Implement responsive sizing                  |
| P4-032 | Implement configurable placement             |
| P4-033 | Implement controlled theming                 |
| P4-034 | Implement focus management                   |
| P4-035 | Implement keyboard navigation                |
| P4-036 | Add screen-reader labels and announcements   |
| P4-037 | Add color-contrast checks                    |
| P4-038 | Configure CSP for assistant origin           |
| P4-039 | Configure frame-ancestors policy             |
| P4-040 | Add clickjacking and framing tests           |
| P4-041 | Add postMessage security tests               |
| P4-042 | Add widget unit tests                        |
| P4-043 | Add widget end-to-end test host              |
| P4-044 | Test widget in Next.js host                  |
| P4-045 | Test widget in plain HTML host               |
| P4-046 | Test widget in another SPA framework         |
| P4-047 | Add widget bundle-size budget                |
| P4-048 | Add widget release build                     |
| P4-049 | Publish widget assets to development CDN     |
| P4-050 | Add asset-integrity metadata                 |
| P4-051 | Document embedding procedure                 |
| P4-052 | Document widget events API                   |
| P4-053 | Document CSP requirements                    |

### Exit gate

- The widget embeds in multiple host frameworks.
- Only approved origins can initialize sessions.
- Session tokens are short-lived and memory-only.
- Streaming, citations, accessibility, and responsive behavior pass tests.
- Widget assets are versioned and deployable through a CDN.

## Phase 5 — Administration and Operations

**Objective:** Provide controlled management, visibility, recovery, quotas, feedback, and operational tooling.

| ID     | Atomic task                                   |
| ------ | --------------------------------------------- |
| P5-001 | Define administration-role matrix             |
| P5-002 | Enforce administration-route authorization    |
| P5-003 | Implement administration application shell    |
| P5-004 | Implement tenant-settings read API            |
| P5-005 | Implement tenant-settings update API          |
| P5-006 | Build tenant-settings page                    |
| P5-007 | Build allowed-origin management UI            |
| P5-008 | Add source-list API                           |
| P5-009 | Build source-list page                        |
| P5-010 | Build manual-upload interface                 |
| P5-011 | Build Drive-connector setup flow              |
| P5-012 | Build connector-health display                |
| P5-013 | Implement manual synchronization action       |
| P5-014 | Implement source-disable action               |
| P5-015 | Build document-list page                      |
| P5-016 | Add document search and filters               |
| P5-017 | Build document-detail page                    |
| P5-018 | Implement document reindex action             |
| P5-019 | Implement document-delete action              |
| P5-020 | Require destructive-action confirmation       |
| P5-021 | Build ingestion-job list                      |
| P5-022 | Build ingestion-job detail view               |
| P5-023 | Implement failed-job replay action            |
| P5-024 | Implement dead-letter queue summary           |
| P5-025 | Implement audit-event query API               |
| P5-026 | Build audit-log viewer                        |
| P5-027 | Protect audit events from modification        |
| P5-028 | Define usage-event aggregation                |
| P5-029 | Implement tenant-usage API                    |
| P5-030 | Build usage dashboard                         |
| P5-031 | Add tenant quota configuration                |
| P5-032 | Enforce request quotas                        |
| P5-033 | Define user-feedback schema                   |
| P5-034 | Implement feedback submission API             |
| P5-035 | Add widget feedback controls                  |
| P5-036 | Build feedback review page                    |
| P5-037 | Link feedback to traces and prompt versions   |
| P5-038 | Implement evaluation-report storage           |
| P5-039 | Build evaluation-results page                 |
| P5-040 | Implement prompt-version read API             |
| P5-041 | Build prompt-version display                  |
| P5-042 | Add system-status page                        |
| P5-043 | Define alert thresholds                       |
| P5-044 | Configure ingestion-failure alerts            |
| P5-045 | Configure query-error alerts                  |
| P5-046 | Configure authorization-denial anomaly alerts |
| P5-047 | Configure queue-backlog alerts                |
| P5-048 | Create deployment runbook                     |
| P5-049 | Create rollback runbook                       |
| P5-050 | Create OpenAI outage runbook                  |
| P5-051 | Create failed-ingestion runbook               |
| P5-052 | Create tenant-offboarding runbook             |
| P5-053 | Create secret-rotation runbook                |
| P5-054 | Create prompt-rollback runbook                |
| P5-055 | Add administrative end-to-end tests           |
| P5-056 | Add administration audit tests                |

### Exit gate

- Administrators can manage sources, documents, and origins.
- Operators can identify and recover ingestion failures.
- Usage, feedback, audit, and evaluation results are visible.
- Sensitive actions are authorized and audited.
- Required alerts and runbooks exist.

## Phase 6 — Browser Extension

**Objective:** Deliver a least-privilege Manifest V3 extension using the same assistant backend.

| ID     | Atomic task                                    |
| ------ | ---------------------------------------------- |
| P6-001 | Define supported browser versions              |
| P6-002 | Define extension use cases                     |
| P6-003 | Define minimum permission set                  |
| P6-004 | Create Manifest V3 configuration               |
| P6-005 | Implement extension service worker             |
| P6-006 | Implement side-panel shell                     |
| P6-007 | Reuse assistant design-system components       |
| P6-008 | Implement extension authentication entry point |
| P6-009 | Implement extension session-token exchange     |
| P6-010 | Prevent permanent token storage                |
| P6-011 | Implement conversation creation                |
| P6-012 | Implement streaming chat                       |
| P6-013 | Implement citations in extension UI            |
| P6-014 | Define page-context request schema             |
| P6-015 | Implement explicit share-selection action      |
| P6-016 | Implement selected-text extraction             |
| P6-017 | Implement context preview                      |
| P6-018 | Implement context confirmation                 |
| P6-019 | Add context-size limit                         |
| P6-020 | Add sensitive-field warning                    |
| P6-021 | Implement active-tab access                    |
| P6-022 | Avoid broad host permissions                   |
| P6-023 | Implement tenant domain allowlist              |
| P6-024 | Enforce domain allowlist                       |
| P6-025 | Implement content-script messaging             |
| P6-026 | Validate extension message senders             |
| P6-027 | Implement extension error states               |
| P6-028 | Implement session-expiry recovery              |
| P6-029 | Add extension event telemetry                  |
| P6-030 | Add extension unit tests                       |
| P6-031 | Add extension integration tests                |
| P6-032 | Add page-context security tests                |
| P6-033 | Add domain-restriction tests                   |
| P6-034 | Add extension build signing process            |
| P6-035 | Generate internal release package              |
| P6-036 | Document enterprise deployment options         |
| P6-037 | Document extension permissions                 |
| P6-038 | Document user privacy behavior                 |
| P6-039 | Pilot extension with internal test group       |
| P6-040 | Resolve pilot defects                          |

### Exit gate

- The Manifest V3 extension reuses the assistant API.
- Page context is captured only after explicit user action and preview.
- Broad host permissions are avoided.
- Domain restrictions and sender validation are tested.
- An internally deployable signed package is available.

## Phase 7 — Production Hardening

**Objective:** Validate security, resilience, performance, recovery, compliance, and operational readiness.

| ID     | Atomic task                                                |
| ------ | ---------------------------------------------------------- |
| P7-001 | Finalize system data-flow diagram                          |
| P7-002 | Classify stored and transmitted data                       |
| P7-003 | Finalize trust-boundary diagram                            |
| P7-004 | Complete threat model                                      |
| P7-005 | Review tenant-isolation controls                           |
| P7-006 | Review least-privilege IAM policies                        |
| P7-007 | Review secret inventory                                    |
| P7-008 | Test secret rotation                                       |
| P7-009 | Define retention policy by data type                       |
| P7-010 | Implement conversation-retention jobs                      |
| P7-011 | Implement audit-retention behavior                         |
| P7-012 | Configure vector-store expiration policy where appropriate |
| P7-013 | Test document-deletion completeness                        |
| P7-014 | Test tenant-offboarding                                    |
| P7-015 | Define service-level indicators                            |
| P7-016 | Define service-level objectives                            |
| P7-017 | Configure SLO dashboards                                   |
| P7-018 | Configure SLO alerts                                       |
| P7-019 | Create representative load model                           |
| P7-020 | Implement API load test                                    |
| P7-021 | Implement widget load test                                 |
| P7-022 | Implement ingestion throughput test                        |
| P7-023 | Establish performance baseline                             |
| P7-024 | Tune API worker configuration                              |
| P7-025 | Tune database connection pools                             |
| P7-026 | Tune ingestion concurrency                                 |
| P7-027 | Set retrieval result limits                                |
| P7-028 | Set tenant request-rate limits                             |
| P7-029 | Set tenant usage quotas                                    |
| P7-030 | Configure edge rate limiting                               |
| P7-031 | Configure CDN and WAF policies                             |
| P7-032 | Test OpenAI timeout behavior                               |
| P7-033 | Test OpenAI rate-limit behavior                            |
| P7-034 | Test OpenAI outage behavior                                |
| P7-035 | Test database unavailability                               |
| P7-036 | Test queue unavailability                                  |
| P7-037 | Test object-storage unavailability                         |
| P7-038 | Test worker termination during processing                  |
| P7-039 | Test network interruption during streaming                 |
| P7-040 | Verify circuit-breaker recovery                            |
| P7-041 | Define backup scope and schedule                           |
| P7-042 | Configure database backups                                 |
| P7-043 | Configure infrastructure-state backups                     |
| P7-044 | Execute database restore test                              |
| P7-045 | Execute configuration restore test                         |
| P7-046 | Define recovery-time objective                             |
| P7-047 | Define recovery-point objective                            |
| P7-048 | Create disaster-recovery runbook                           |
| P7-049 | Execute disaster-recovery exercise                         |
| P7-050 | Expand prompt-injection test suite                         |
| P7-051 | Add RAG-poisoning scenarios                                |
| P7-052 | Add data-exfiltration scenarios                            |
| P7-053 | Add conflicting-policy scenarios                           |
| P7-054 | Add authorization-boundary fuzz tests                      |
| P7-055 | Freeze production evaluation dataset version               |
| P7-056 | Run candidate model evaluation                             |
| P7-057 | Run candidate prompt evaluation                            |
| P7-058 | Approve production model and prompt configuration          |
| P7-059 | Conduct accessibility audit                                |
| P7-060 | Conduct browser compatibility test                         |
| P7-061 | Conduct external or independent penetration test           |
| P7-062 | Remediate critical penetration-test findings               |
| P7-063 | Remediate required high-severity findings                  |
| P7-064 | Review software licenses                                   |
| P7-065 | Generate production SBOM                                   |
| P7-066 | Verify artifact provenance                                 |
| P7-067 | Finalize incident-response plan                            |
| P7-068 | Run incident-response tabletop exercise                    |
| P7-069 | Define support escalation path                             |
| P7-070 | Define pilot tenant criteria                               |
| P7-071 | Provision pilot tenant                                     |
| P7-072 | Ingest pilot synthetic or approved documents               |
| P7-073 | Execute pilot acceptance tests                             |
| P7-074 | Monitor pilot quality and operations                       |
| P7-075 | Resolve pilot release blockers                             |
| P7-076 | Conduct production-readiness review                        |
| P7-077 | Record go-live decision                                    |
| P7-078 | Deploy approved production release                         |
| P7-079 | Execute production smoke tests                             |
| P7-080 | Verify production alerts and dashboards                    |
| P7-081 | Verify production rollback readiness                       |
| P7-082 | Conduct post-release review                                |

### Exit gate

- Threat modeling and penetration testing are complete.
- No unapproved critical security findings remain.
- Performance and resilience targets are met.
- Retention, deletion, backup, restore, and disaster recovery are verified.
- Frozen evaluations approve production model and prompt versions.
- Pilot and production-readiness gates are approved.

## Cross-phase sequence

```text
Phase 0 → Phase 1 → Phase 2 → Phase 3 → Phase 4 → Phase 5 → Phase 6 → Phase 7
```

Parallel work is allowed only after the relevant contracts and security foundations are stable.
