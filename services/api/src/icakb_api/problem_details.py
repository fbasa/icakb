"""RFC 9457 problem detail helpers for API errors."""

from __future__ import annotations

from collections.abc import Mapping
from http import HTTPStatus

from fastapi import FastAPI, Request
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from pydantic import BaseModel, ConfigDict
from starlette.exceptions import HTTPException as StarletteHTTPException

from .request_context import REQUEST_ID_HEADER, get_request_id


class ProblemDetail(BaseModel):
    """RFC 9457 problem detail payload."""

    model_config = ConfigDict(extra="forbid", frozen=True)

    type: str = "about:blank"
    title: str
    status: int
    detail: str | None = None
    instance: str | None = None


def render_problem_response(
    problem: ProblemDetail,
    *,
    headers: Mapping[str, str] | None = None,
) -> JSONResponse:
    """Render a JSON response with the RFC 9457 media type."""

    response_headers = dict(headers or {})
    request_id = get_request_id()
    if request_id is not None:
        response_headers[REQUEST_ID_HEADER] = request_id

    return JSONResponse(
        status_code=problem.status,
        content=problem.model_dump(exclude_none=True),
        headers=response_headers,
        media_type="application/problem+json",
    )


def _problem_from_status(
    status_code: int,
    *,
    detail: str | None = None,
    instance: str | None = None,
) -> ProblemDetail:
    return ProblemDetail(
        title=HTTPStatus(status_code).phrase,
        status=status_code,
        detail=detail,
        instance=instance,
    )


def register_problem_handlers(app: FastAPI) -> None:
    """Register problem-detail handlers for expected API failures."""

    @app.exception_handler(StarletteHTTPException)
    async def handle_http_exception(request: Request, exc: StarletteHTTPException) -> JSONResponse:
        detail = exc.detail if isinstance(exc.detail, str) else str(exc.detail)
        problem = _problem_from_status(
            exc.status_code,
            detail=detail,
            instance=str(request.url.path),
        )
        return render_problem_response(problem, headers=exc.headers)

    @app.exception_handler(RequestValidationError)
    async def handle_validation_error(
        request: Request,
        exc: RequestValidationError,
    ) -> JSONResponse:
        _ = exc
        problem = _problem_from_status(
            422,
            detail="One or more request parameters were invalid.",
            instance=str(request.url.path),
        )
        return render_problem_response(problem)

    @app.exception_handler(Exception)
    async def handle_unexpected_error(request: Request, exc: Exception) -> JSONResponse:
        _ = exc
        problem = _problem_from_status(
            500,
            detail="An unexpected server error occurred.",
            instance=str(request.url.path),
        )
        return render_problem_response(problem)
