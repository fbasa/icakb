# API Contract Principles

- Version public APIs under `/api/v1`.
- Use validated schemas for every request, response, stream event, queue message, and widget message.
- Use RFC 9457 problem details for non-streaming errors.
- Use stable machine-readable error codes.
- Use typed terminal error events after a stream has started.
- Do not expose provider-specific objects in public or domain contracts.
- External IDs are opaque.
- Tenant identity is never selected by a client-supplied field.
