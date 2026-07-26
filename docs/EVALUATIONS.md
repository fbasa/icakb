# Evaluations

## Required datasets

- Answerable questions.
- Unanswerable questions and required abstention.
- Citation correctness.
- Conflicting documents.
- Superseded document versions.
- Prompt-injection documents.
- RAG-poisoning scenarios.
- Data-exfiltration attempts.
- Tenant, role, group, department, and classification boundaries.
- Provider timeout, rate-limit, and outage behavior.
- Multi-turn context.

## Release policy

Prompt, model, retrieval, filter, chunking, and citation changes must run the relevant evaluation suite. Production candidates use a frozen, versioned dataset and machine-readable reports. No tenant-leakage regression is acceptable.
