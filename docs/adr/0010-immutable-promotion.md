# Build once and promote immutable artifacts

- Status: Accepted
- Date: 2026-07-26

## Context

Rebuilding in each environment can produce untested differences.

## Decision

Build signed, scanned artifacts once and promote the same digest through development, staging, and production.

## Consequences

Release provenance and rollback improve; runtime configuration must be environment specific.
