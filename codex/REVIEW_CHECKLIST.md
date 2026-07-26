# Review Checklist

- [ ] The change implements one atomic task.
- [ ] Architecture boundaries are preserved.
- [ ] Tenant identity is derived from validated context.
- [ ] No secrets or production data are present.
- [ ] External inputs are validated.
- [ ] Tests cover success, failure, and security boundaries.
- [ ] Prompt or retrieval changes include evaluations and rollback information.
- [ ] Database changes include migrations and tenant isolation.
- [ ] Logs and traces do not expose sensitive content.
- [ ] Documentation is updated.
- [ ] CI and security checks pass.
