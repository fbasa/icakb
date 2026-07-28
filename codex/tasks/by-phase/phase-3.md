# Phase 3 — Retrieval and Answer Generation

Provide grounded, cited, permission-filtered answers through one stable API.

## Tasks

- [ ] `P3-001` — Define retrieval request contract
- [ ] `P3-002` — Define retrieval result contract
- [ ] `P3-003` — Define retrieval-adapter interface
- [ ] `P3-004` — Implement File Search retrieval adapter
- [ ] `P3-005` — Implement mandatory tenant-store selection
- [ ] `P3-006` — Implement metadata-filter builder
- [ ] `P3-007` — Reject unsupported filter combinations
- [ ] `P3-008` — Add retrieval-filter unit tests
- [ ] `P3-009` — Add cross-tenant retrieval tests
- [ ] `P3-010` — Define conversation domain model
- [ ] `P3-011` — Create conversation database tables
- [ ] `P3-012` — Create message database tables
- [ ] `P3-013` — Apply RLS to conversation tables
- [ ] `P3-014` — Define query API contract
- [ ] `P3-015` — Implement conversation creation
- [ ] `P3-016` — Implement user-message validation
- [ ] `P3-017` — Implement conversation ownership check
- [ ] `P3-018` — Create base system prompt
- [ ] `P3-019` — Create citation-policy prompt fragment
- [ ] `P3-020` — Create insufficient-evidence prompt
- [ ] `P3-021` — Create retrieved-content delimiter
- [ ] `P3-022` — Add prompt manifest entries
- [ ] `P3-023` — Implement prompt-variable validation
- [ ] `P3-024` — Implement retrieval orchestration
- [ ] `P3-025` — Limit retrieval result count
- [ ] `P3-026` — Implement evidence normalization
- [ ] `P3-027` — Implement citation identifier mapping
- [ ] `P3-028` — Implement Responses API adapter
- [ ] `P3-029` — Build grounded-generation request
- [ ] `P3-030` — Implement server-sent event streaming
- [ ] `P3-031` — Implement streaming cancellation
- [ ] `P3-032` — Parse provider citations
- [ ] `P3-033` — Validate citation references
- [ ] `P3-034` — Persist completed assistant response
- [ ] `P3-035` — Persist failed-response state
- [ ] `P3-036` — Implement insufficient-evidence decision
- [ ] `P3-037` — Implement no-document-access response
- [ ] `P3-038` — Implement bounded conversation history
- [ ] `P3-039` — Implement token-budget calculation
- [ ] `P3-040` — Implement provider timeout handling
- [ ] `P3-041` — Implement provider rate-limit handling
- [ ] `P3-042` — Implement provider-unavailable circuit breaker
- [ ] `P3-043` — Add request and provider traces
- [ ] `P3-044` — Add retrieval metrics
- [ ] `P3-045` — Add generation metrics
- [ ] `P3-046` — Redact prompt and evidence content from default logs
- [ ] `P3-047` — Create answerable-question evaluation dataset
- [ ] `P3-048` — Create unanswerable-question dataset
- [ ] `P3-049` — Create citation-correctness dataset
- [ ] `P3-050` — Create conflicting-document dataset
- [ ] `P3-051` — Create superseded-document dataset
- [ ] `P3-052` — Create prompt-injection document dataset
- [ ] `P3-053` — Create tenant-isolation evaluation dataset
- [ ] `P3-054` — Implement offline evaluation runner
- [ ] `P3-055` — Define initial quality thresholds
- [ ] `P3-056` — Add evaluation checks to CI
- [ ] `P3-057` — Document query architecture
- [ ] `P3-058` — Document model and prompt rollback

## Exit gate

- [ ] Every query is tenant- and permission-filtered.
- [ ] Answers stream through a stable API.
- [ ] Citations map only to authorized evidence.
- [ ] Unsupported questions produce evidence-aware abstention.
- [ ] Provider failures have stable behavior.
- [ ] RAG and tenant-isolation evaluations pass approved thresholds.
