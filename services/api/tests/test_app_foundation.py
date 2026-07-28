from __future__ import annotations

import logging
import os
import subprocess
import sys
from http import HTTPStatus
from typing import Protocol, cast

import pytest
from fastapi import FastAPI
from fastapi.testclient import TestClient
from icakb_api.app import RuntimeConfigurationError, create_app
from icakb_api.configuration import RuntimeConfiguration
from icakb_api.health import ReadinessCheck
from icakb_api.problem_details import register_problem_handlers
from icakb_api.request_context import (
    REQUEST_ID_HEADER,
    RequestContextFilter,
    normalize_request_id,
    reset_request_id,
    set_request_id,
)
from icakb_api.telemetry import bootstrap_telemetry
from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider

BASE_ENVIRONMENT = {
    "APP_ENV": "local",
    "APP_VERSION": "1.2.3",
    "LOG_LEVEL": "INFO",
    "DATABASE_URL": "postgresql://app:app@localhost:5432/knowledge_assistant",
    "OBJECT_STORAGE_ENDPOINT": "http://localhost:9090",
    "OBJECT_STORAGE_BUCKET": "knowledge-assistant-local",
    "QUEUE_URL": "http://localhost:4566/000000000000/ingestion",
    "OPENAI_API_KEY": "replace-with-sandbox-key-only",
    "OPENAI_PROJECT_ID": "replace-with-non-production-project",
    "OIDC_ISSUER_URL": "https://example.invalid",
    "OIDC_AUDIENCE": "knowledge-assistant",
    "OPERATIONAL_DIAGNOSTICS_TOKEN": "replace-with-local-diagnostics-token",
}

SENSITIVE_VALUES = (
    "sk-proj-test-secret-value",
    "database-password-value",
    "postgresql://app:database-password-value@localhost:5432/knowledge_assistant",
    "session-cookie-value",
    "bearer-token-value",
)


class RequestLogRecord(Protocol):
    request_id: str


class PassingDependencyProbe:
    def readiness_checks(self, configuration: RuntimeConfiguration) -> list[ReadinessCheck]:
        return [
            ReadinessCheck(name="database", status="pass", detail="Test database probe passed."),
            ReadinessCheck(
                name="migrations", status="pass", detail="Test migrations probe passed."
            ),
            ReadinessCheck(
                name="object_storage",
                status="pass",
                detail="Test object-storage probe passed.",
            ),
        ]

    def diagnostic_checks(self, configuration: RuntimeConfiguration) -> list[ReadinessCheck]:
        return [
            *self.readiness_checks(configuration),
            ReadinessCheck(name="queue", status="pass", detail="Test queue probe passed."),
            ReadinessCheck(name="openai", status="pass", detail="Test OpenAI probe passed."),
        ]


class FailingDependencyProbe:
    def readiness_checks(self, configuration: RuntimeConfiguration) -> list[ReadinessCheck]:
        return [ReadinessCheck(name="database", status="fail", detail="Test failure.")]

    def diagnostic_checks(self, configuration: RuntimeConfiguration) -> list[ReadinessCheck]:
        return self.readiness_checks(configuration)


def test_request_correlation_middleware_preserves_or_normalizes_request_ids() -> None:
    app = create_app(BASE_ENVIRONMENT, dependency_probe=PassingDependencyProbe())
    client = TestClient(app)

    request_id = "123e4567-e89b-12d3-a456-426614174000"
    response = client.get("/version", headers={REQUEST_ID_HEADER: request_id})

    assert response.status_code == HTTPStatus.OK
    assert response.headers[REQUEST_ID_HEADER] == request_id

    generated = client.get("/version", headers={REQUEST_ID_HEADER: "not-a-uuid"})
    assert generated.status_code == HTTPStatus.OK
    assert generated.headers[REQUEST_ID_HEADER] != "not-a-uuid"
    assert (
        normalize_request_id(generated.headers[REQUEST_ID_HEADER])
        == generated.headers[REQUEST_ID_HEADER]
    )


def test_health_endpoints_report_liveness_and_readiness() -> None:
    app = create_app(BASE_ENVIRONMENT, dependency_probe=PassingDependencyProbe())
    client = TestClient(app)

    live_response = client.get("/health/live")
    assert live_response.status_code == HTTPStatus.OK
    assert live_response.json() == {"service": "api", "status": "ok"}

    startup_response = client.get("/health/startup")
    assert startup_response.status_code == HTTPStatus.OK
    assert startup_response.json()["status"] == "ready"

    ready_response = client.get("/health/ready")
    assert ready_response.status_code == HTTPStatus.OK
    ready_body = ready_response.json()
    assert ready_body["service"] == "api"
    assert ready_body["status"] == "ready"
    assert [check["name"] for check in ready_body["checks"]] == [
        "startup",
        "configuration",
        "telemetry",
        "database",
        "migrations",
        "object_storage",
    ]
    assert {check["status"] for check in ready_body["checks"]} == {"pass"}

    unauthenticated_diagnostics = client.get("/health/dependencies")
    assert unauthenticated_diagnostics.status_code == HTTPStatus.UNAUTHORIZED

    diagnostics_response = client.get(
        "/health/dependencies",
        headers={"X-Operations-Token": "replace-with-local-diagnostics-token"},
    )
    assert diagnostics_response.status_code == HTTPStatus.OK
    assert diagnostics_response.json()["status"] == "ready"


def test_readiness_fails_when_required_dependencies_fail() -> None:
    app = create_app(BASE_ENVIRONMENT, dependency_probe=FailingDependencyProbe())
    client = TestClient(app)

    response = client.get("/health/ready")

    assert response.status_code == HTTPStatus.SERVICE_UNAVAILABLE
    assert response.json()["status"] == "not_ready"


def test_startup_configuration_failures_are_sanitized(caplog: pytest.LogCaptureFixture) -> None:
    invalid_environment = dict(BASE_ENVIRONMENT)
    invalid_environment.update(
        {
            "DATABASE_URL": (
                "postgresql://app:database-password-value@localhost:5432/knowledge_assistant"
            ),
            "OPENAI_API_KEY": "sk-proj-test-secret-value",
            "QUEUE_URL": "not-a-url?token=bearer-token-value",
            "OIDC_AUDIENCE": "session-cookie-value",
        }
    )

    with caplog.at_level(logging.ERROR), pytest.raises(RuntimeConfigurationError) as exc_info:
        create_app(invalid_environment)

    rendered_error = str(exc_info.value)
    rendered_logs = "\n".join(record.getMessage() for record in caplog.records)
    assert rendered_error == (
        "Runtime configuration validation failed. Review required environment variables."
    )
    for sensitive_value in SENSITIVE_VALUES:
        assert sensitive_value not in rendered_error
        assert sensitive_value not in rendered_logs


def test_import_time_startup_configuration_failure_hides_sensitive_values() -> None:
    invalid_environment = dict(os.environ)
    invalid_environment.update(
        {
            "APP_ENV": "local",
            "APP_VERSION": "1.2.3",
            "LOG_LEVEL": "INFO",
            "DATABASE_URL": (
                "postgresql://app:database-password-value@localhost:5432/knowledge_assistant"
            ),
            "OBJECT_STORAGE_ENDPOINT": "http://localhost:9090",
            "OBJECT_STORAGE_BUCKET": "knowledge-assistant-local",
            "QUEUE_URL": "not-a-url?token=bearer-token-value",
            "OPENAI_API_KEY": "sk-proj-test-secret-value",
            "OPENAI_PROJECT_ID": "replace-with-non-production-project",
            "OIDC_ISSUER_URL": "https://example.invalid",
            "OIDC_AUDIENCE": "session-cookie-value",
            "OPERATIONAL_DIAGNOSTICS_TOKEN": "bearer-token-value",
        }
    )

    completed = subprocess.run(
        [sys.executable, "-c", "import icakb_api.app"],
        check=False,
        env=invalid_environment,
        text=True,
        capture_output=True,
    )

    rendered_process_output = completed.stdout + completed.stderr
    assert completed.returncode != 0
    assert (
        "Runtime configuration validation failed. Review required environment variables."
        in rendered_process_output
    )
    for sensitive_value in SENSITIVE_VALUES:
        assert sensitive_value not in rendered_process_output


def test_problem_details_cover_http_validation_and_unexpected_errors() -> None:
    app = FastAPI()
    register_problem_handlers(app)

    @app.get("/items/{item_id}")
    def get_item(item_id: int) -> dict[str, int]:
        return {"item_id": item_id}

    @app.get("/boom")
    def boom() -> None:
        raise RuntimeError("boom")

    client = TestClient(app, raise_server_exceptions=False)

    not_found = client.get("/missing")
    assert not_found.status_code == HTTPStatus.NOT_FOUND
    assert not_found.headers["content-type"] == "application/problem+json"
    assert not_found.json() == {
        "type": "about:blank",
        "title": "Not Found",
        "status": 404,
        "detail": "Not Found",
        "instance": "/missing",
    }

    validation_error = client.get("/items/not-an-int")
    assert validation_error.status_code == HTTPStatus.UNPROCESSABLE_ENTITY
    assert validation_error.headers["content-type"] == "application/problem+json"
    assert validation_error.json()["title"] == HTTPStatus.UNPROCESSABLE_ENTITY.phrase
    assert validation_error.json()["detail"] == "One or more request parameters were invalid."

    unexpected_error = client.get("/boom")
    assert unexpected_error.status_code == HTTPStatus.INTERNAL_SERVER_ERROR
    assert unexpected_error.headers["content-type"] == "application/problem+json"
    assert unexpected_error.json()["title"] == "Internal Server Error"
    assert unexpected_error.json()["detail"] == "An unexpected server error occurred."


def test_request_context_filter_injects_request_id_into_log_records() -> None:
    token = set_request_id("123e4567-e89b-12d3-a456-426614174000")
    try:
        record = logging.LogRecord("icakb", logging.INFO, __file__, 1, "message", (), None)
        assert RequestContextFilter().filter(record) is True
        enriched_record = cast("RequestLogRecord", record)
        assert enriched_record.request_id == "123e4567-e89b-12d3-a456-426614174000"
    finally:
        reset_request_id(token)


def test_bootstrap_telemetry_installs_a_tracer_provider() -> None:
    app = create_app(BASE_ENVIRONMENT)
    assert app.state.telemetry_bootstrapped is True
    assert isinstance(trace.get_tracer_provider(), TracerProvider)
    state = bootstrap_telemetry(service_name="api", service_version="1.2.3")
    assert state.tracer_provider_installed is True
