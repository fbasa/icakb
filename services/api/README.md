# services/api

FastAPI service scaffold for the repository's version-endpoint demonstration and future API work.

Current foundation endpoints:

- `GET /version`
- `GET /health/live`
- `GET /health/ready`

The service also emits structured JSON logs, propagates `X-Request-ID`, and returns RFC 9457
problem details for API errors.

Startup validates the committed runtime environment contract before the app begins serving
requests. The package also includes a minimal in-memory queue port for later ingestion work.
