# Phase 2 — Document Ingestion

Create a reliable and reversible document lifecycle from source systems to hosted File Search.

## Tasks

- [ ] `P2-001` — Define data-source domain model
- [ ] `P2-002` — Define document domain model
- [ ] `P2-003` — Define document-version model
- [ ] `P2-004` — Define ingestion-job model
- [ ] `P2-005` — Create source database tables
- [ ] `P2-006` — Create document database tables
- [ ] `P2-007` — Create document-version tables
- [ ] `P2-008` — Create ingestion-job tables
- [ ] `P2-009` — Apply RLS to ingestion tables
- [ ] `P2-010` — Define supported-file policy
- [ ] `P2-011` — Implement upload-request API
- [ ] `P2-012` — Implement presigned object upload
- [ ] `P2-013` — Implement upload-completion callback
- [ ] `P2-014` — Validate file size and declared type
- [ ] `P2-015` — Detect actual file type
- [ ] `P2-016` — Add malware-scanning adapter
- [ ] `P2-017` — Quarantine failed or suspicious uploads
- [ ] `P2-018` — Define queue-message schema
- [ ] `P2-019` — Implement job publishing
- [ ] `P2-020` — Implement worker message consumption
- [ ] `P2-021` — Add ingestion idempotency key
- [ ] `P2-022` — Add worker lease and visibility handling
- [ ] `P2-023` — Define extraction-adapter interface
- [ ] `P2-024` — Implement PDF extraction
- [ ] `P2-025` — Implement DOCX extraction
- [ ] `P2-026` — Implement text and Markdown extraction
- [ ] `P2-027` — Implement unsupported-format failure
- [ ] `P2-028` — Normalize extracted text
- [ ] `P2-029` — Calculate source-content checksum
- [ ] `P2-030` — Implement duplicate-content detection
- [ ] `P2-031` — Define document metadata schema
- [ ] `P2-032` — Validate metadata values
- [ ] `P2-033` — Map source permissions to retrieval metadata
- [ ] `P2-034` — Define OpenAI vector-store adapter
- [ ] `P2-035` — Implement tenant vector-store creation
- [ ] `P2-036` — Implement OpenAI file upload
- [ ] `P2-037` — Apply retrieval metadata to indexed files
- [ ] `P2-038` — Poll indexing completion
- [ ] `P2-039` — Verify indexed-file association
- [ ] `P2-040` — Persist provider file references
- [ ] `P2-041` — Mark ingestion success
- [ ] `P2-042` — Implement transient-error classification
- [ ] `P2-043` — Implement bounded retries
- [ ] `P2-044` — Implement dead-letter handling
- [ ] `P2-045` — Add failed-job replay command
- [ ] `P2-046` — Implement document deletion request
- [ ] `P2-047` — Delete provider-indexed file
- [ ] `P2-048` — Delete or retain canonical object by policy
- [ ] `P2-049` — Invalidate document caches
- [ ] `P2-050` — Verify deletion completion
- [ ] `P2-051` — Implement reconciliation job
- [ ] `P2-052` — Add ingestion metrics
- [ ] `P2-053` — Add ingestion traces
- [ ] `P2-054` — Add ingestion structured logs
- [ ] `P2-055` — Add ingestion-status API
- [ ] `P2-056` — Add document-list API
- [ ] `P2-057` — Add document-version API
- [ ] `P2-058` — Define Google Drive connector interface
- [ ] `P2-059` — Implement Drive OAuth credential storage
- [ ] `P2-060` — Implement Drive folder configuration
- [ ] `P2-061` — Implement initial Drive discovery sync
- [ ] `P2-062` — Implement incremental Drive sync
- [ ] `P2-063` — Propagate Drive deletions
- [ ] `P2-064` — Add connector health status
- [ ] `P2-065` — Create synthetic ingestion fixtures
- [ ] `P2-066` — Add ingestion integration tests
- [ ] `P2-067` — Add ingestion recovery runbook

## Exit gate

- [ ] Documents can be uploaded, validated, indexed, updated, reconciled, and deleted.
- [ ] Duplicate ingestion is idempotent.
- [ ] Failed jobs are observable and recoverable.
- [ ] Drive synchronization propagates creation, modification, and deletion.
- [ ] No document is searchable before metadata and indexing verification.
