# Security Policy

## Scope

This project processes private company knowledge and must be treated as a security-sensitive, multi-tenant application.

## Reporting vulnerabilities

Report suspected vulnerabilities privately to the repository security owners. Do not create public issues containing exploit details, credentials, tenant information, internal documents, or reproduction data from production.

## Mandatory controls

- No secrets or production data in the repository, test fixtures, build logs, or browser bundles.
- Short-lived credentials and workload identity are preferred over static credentials.
- Tenant isolation must be enforced in application policy, PostgreSQL Row-Level Security, object-storage paths and policies, retrieval-store selection, cache keys, and tests.
- Retrieved documents are untrusted input.
- Security-sensitive actions must be authorized and audited.
- Dependency, secret, static-analysis, container, and infrastructure scans must pass release policy.

## Security exceptions

An exception must have an owner, business justification, compensating control, expiry date, tracking issue, and security approval.

## Supported versions

Supported versions will be recorded in `CHANGELOG.md` after the first production release.
