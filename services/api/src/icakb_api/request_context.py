"""Request correlation helpers for the API service."""

from __future__ import annotations

import logging
from contextvars import ContextVar, Token
from uuid import UUID, uuid4

from starlette.middleware.base import BaseHTTPMiddleware, RequestResponseEndpoint
from starlette.requests import Request
from starlette.responses import Response

REQUEST_ID_HEADER = "X-Request-ID"
_request_id_context: ContextVar[str | None] = ContextVar("icakb_request_id", default=None)


def normalize_request_id(request_id: str | None) -> str:
    """Normalize an inbound request identifier to a canonical UUID string."""

    if request_id is None:
        return str(uuid4())

    candidate = request_id.strip()
    if not candidate:
        return str(uuid4())

    try:
        return str(UUID(candidate))
    except ValueError:
        return str(uuid4())


def get_request_id() -> str | None:
    """Return the current request identifier, if one is active."""

    return _request_id_context.get()


def set_request_id(request_id: str) -> Token[str | None]:
    """Store the current request identifier in context."""

    return _request_id_context.set(request_id)


def reset_request_id(token: Token[str | None]) -> None:
    """Restore the previous request identifier context."""

    _request_id_context.reset(token)


class RequestContextFilter(logging.Filter):
    """Attach the active request identifier to log records."""

    def filter(self, record: logging.LogRecord) -> bool:
        request_id = get_request_id()
        if request_id is not None and not hasattr(record, "request_id"):
            record.request_id = request_id
        return True


def install_request_context_filter() -> None:
    """Install the request identifier filter once on the root logger."""

    root_logger = logging.getLogger()
    for handler in root_logger.handlers:
        if any(isinstance(filter_, RequestContextFilter) for filter_ in handler.filters):
            continue
        handler.addFilter(RequestContextFilter())


class RequestCorrelationMiddleware(BaseHTTPMiddleware):
    """Populate a stable request identifier for each incoming request."""

    async def dispatch(
        self,
        request: Request,
        call_next: RequestResponseEndpoint,
    ) -> Response:
        request_id = normalize_request_id(request.headers.get(REQUEST_ID_HEADER))
        token = set_request_id(request_id)
        request.state.request_id = request_id

        try:
            response = await call_next(request)
        finally:
            reset_request_id(token)

        response.headers[REQUEST_ID_HEADER] = request_id
        return response
