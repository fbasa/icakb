# Threat Model

## Assets

Internal documents, identities, tenant configuration, permissions, conversations, audit events, prompts, model configuration, provider credentials, source-system credentials, and deployment artifacts.

## Primary threats

- Cross-tenant document or metadata leakage.
- Broken object-level authorization.
- Prompt injection from users or retrieved documents.
- RAG poisoning through malicious indexed content.
- Data exfiltration through answers, logs, traces, browser context, or extensions.
- Session-token theft or origin confusion.
- Iframe and postMessage abuse.
- Browser-extension permission abuse.
- Supply-chain compromise.
- Administrative privilege abuse.
- Incomplete deletion and retention violations.

## Mandatory mitigations

Layered tenant isolation, short-lived sessions, least privilege, schema validation, origin allowlists, sandboxed iframe, explicit extension user actions, retrieval-time authorization, RLS, audit events, content-redacted telemetry, secret and dependency scanning, adversarial evaluations, deletion reconciliation, and independent security review.
