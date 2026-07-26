# Use OpenTelemetry-compatible telemetry

- Status: Accepted
- Date: 2026-07-26

## Context

Requests cross browsers, APIs, queues, workers, databases, storage, and OpenAI.

## Decision

Use structured logs, metrics, and distributed traces with content recording disabled by default.

## Consequences

Operations gain end-to-end visibility without making sensitive content the default telemetry payload.
