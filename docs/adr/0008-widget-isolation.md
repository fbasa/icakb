# Use a sandboxed iframe widget

- Status: Accepted
- Date: 2026-07-26

## Context

The assistant must embed into unknown host frameworks without style or script interference.

## Decision

Use a small Web Component launcher that creates a sandboxed iframe on a separate assistant origin and communicates through validated postMessage schemas.

## Consequences

Isolation and compatibility improve, while origin, CSP, and session exchange require strict configuration.
