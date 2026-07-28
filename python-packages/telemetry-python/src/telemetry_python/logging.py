"""Structured JSON logging helpers for Python services."""

from __future__ import annotations

import json
import logging
from collections.abc import Mapping
from datetime import UTC, datetime
from typing import TextIO

_LOG_RECORD_FIELDS = frozenset(
    {
        "args",
        "asctime",
        "created",
        "exc_info",
        "exc_text",
        "filename",
        "funcName",
        "levelname",
        "levelno",
        "lineno",
        "module",
        "msecs",
        "message",
        "msg",
        "name",
        "pathname",
        "process",
        "processName",
        "relativeCreated",
        "stack_info",
        "thread",
        "threadName",
    }
)
_TOP_LEVEL_FIELDS = frozenset(
    {
        "environment",
        "event",
        "request_id",
        "service",
        "span_id",
        "tenant_id",
        "trace_id",
    }
)
_REDACTION_TOKENS = (
    "api_key",
    "authorization",
    "client_secret",
    "password",
    "private_key",
    "refresh_token",
    "secret",
    "token",
)
_REDACTION_PLACEHOLDER = "[REDACTED]"


def _utc_now() -> str:
    return datetime.now(UTC).isoformat(timespec="milliseconds").replace("+00:00", "Z")


def _is_sensitive_key(key: str) -> bool:
    lower_key = key.lower()
    return any(token in lower_key for token in _REDACTION_TOKENS)


def _sanitize_value(key: str, value: object) -> object:
    if _is_sensitive_key(key):
        return _REDACTION_PLACEHOLDER

    if value is None or isinstance(value, (bool, int, float, str)):
        return value

    if isinstance(value, Mapping):
        return {
            str(child_key): _sanitize_value(str(child_key), child_value)
            for child_key, child_value in value.items()
        }

    if isinstance(value, tuple):
        return [_sanitize_value(key, item) for item in value]

    if isinstance(value, list):
        return [_sanitize_value(key, item) for item in value]

    if isinstance(value, set):
        return [_sanitize_value(key, item) for item in sorted(value, key=str)]

    return str(value)


def _collect_extra_fields(record: logging.LogRecord) -> dict[str, object]:
    return {
        key: value
        for key, value in record.__dict__.items()
        if key not in _LOG_RECORD_FIELDS
        and key not in _TOP_LEVEL_FIELDS
        and not key.startswith("_")
    }


class JsonFormatter(logging.Formatter):
    """Render log records as compact JSON documents."""

    def format(self, record: logging.LogRecord) -> str:
        payload: dict[str, object] = {
            "timestamp": _utc_now(),
            "level": record.levelname,
            "logger": record.name,
            "message": record.getMessage(),
        }

        for field in sorted(_TOP_LEVEL_FIELDS):
            value = getattr(record, field, None)
            if value is not None:
                payload[field] = _sanitize_value(field, value)

        extra_fields = _collect_extra_fields(record)
        if extra_fields:
            payload["extra"] = _sanitize_value("extra", extra_fields)

        if record.exc_info is not None:
            payload["exception"] = self.formatException(record.exc_info)

        return json.dumps(payload, ensure_ascii=False, separators=(",", ":"), sort_keys=True)


def configure_json_logging(
    *,
    level: int = logging.INFO,
    stream: TextIO | None = None,
) -> None:
    """Configure application and Uvicorn loggers to emit one JSON object per line."""

    handler = logging.StreamHandler(stream)
    handler.setFormatter(JsonFormatter())

    root_logger = logging.getLogger()
    root_logger.handlers.clear()
    root_logger.setLevel(level)
    root_logger.addHandler(handler)

    for logger_name in ("uvicorn", "uvicorn.error", "uvicorn.access"):
        logger = logging.getLogger(logger_name)
        logger.handlers.clear()
        logger.setLevel(level)
        logger.propagate = True
