# syntax=docker/dockerfile:1.7

FROM python:3.13-alpine@sha256:399babc8b49529dabfd9c922f2b5eea81d611e4512e3ed250d75bd2e7683f4b0 AS base

ARG APP_VERSION=0.0.0-dev
ARG APP_COMMIT_SHA=unknown
ARG APP_BUILD_TIME=1970-01-01T00:00:00Z
ARG GITHUB_REPOSITORY=unknown

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    APP_VERSION="${APP_VERSION}" \
    APP_COMMIT_SHA="${APP_COMMIT_SHA}" \
    APP_BUILD_TIME="${APP_BUILD_TIME}" \
    PATH="/app/.venv/bin:$PATH"

WORKDIR /app

LABEL org.opencontainers.image.version="${APP_VERSION}" \
      org.opencontainers.image.revision="${APP_COMMIT_SHA}" \
      org.opencontainers.image.created="${APP_BUILD_TIME}" \
      org.opencontainers.image.source="https://github.com/${GITHUB_REPOSITORY:-unknown}"

COPY --from=ghcr.io/astral-sh/uv:0.11.28@sha256:0f36cb9361a3346885ca3677e3767016687b5a170c1a6b88465ec14aefec90aa /uv /uvx /bin/

COPY pyproject.toml uv.lock ./
COPY services/api/pyproject.toml services/api/pyproject.toml
COPY python-packages/telemetry-python/pyproject.toml python-packages/telemetry-python/pyproject.toml

RUN --mount=type=cache,target=/root/.cache/uv \
    uv sync --frozen --no-install-workspace

COPY services/api/src services/api/src
COPY python-packages/telemetry-python/src python-packages/telemetry-python/src

RUN --mount=type=cache,target=/root/.cache/uv \
    uv sync --frozen --no-editable --package icakb-api

RUN addgroup -S app && adduser -S -G app -h /app app \
    && chown -R app:app /app

USER app

EXPOSE 8000

HEALTHCHECK --interval=30s --timeout=3s --start-period=15s --retries=3 \
    CMD python -c "from urllib.request import urlopen; urlopen('http://127.0.0.1:8000/health/live', timeout=2)"

CMD ["uvicorn", "icakb_api.app:app", "--host", "0.0.0.0", "--port", "8000"]
