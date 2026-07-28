"""Health check payloads for the API service."""

from __future__ import annotations

from typing import Literal

from pydantic import BaseModel, ConfigDict


class LiveHealthResponse(BaseModel):
    """Liveness response payload."""

    model_config = ConfigDict(frozen=True)

    service: str
    status: Literal["ok"]


class ReadinessCheck(BaseModel):
    """Single readiness check entry."""

    model_config = ConfigDict(frozen=True)

    name: str
    status: Literal["pass", "fail"]
    detail: str


class ReadinessResponse(BaseModel):
    """Readiness response payload."""

    model_config = ConfigDict(frozen=True)

    service: str
    status: Literal["ready", "not_ready"]
    checks: list[ReadinessCheck]


def build_live_health_response(*, service: str) -> LiveHealthResponse:
    """Build the liveness payload."""

    return LiveHealthResponse(service=service, status="ok")


def build_readiness_response(
    *,
    service: str,
    configuration_ready: bool,
    telemetry_ready: bool,
    dependency_checks: list[ReadinessCheck] | None = None,
) -> ReadinessResponse:
    """Build a bounded readiness payload from local service state."""

    checks = [
        ReadinessCheck(
            name="startup",
            status="pass",
            detail="Application startup completed.",
        ),
        ReadinessCheck(
            name="configuration",
            status="pass" if configuration_ready else "fail",
            detail="Runtime configuration validated."
            if configuration_ready
            else "Runtime configuration is invalid.",
        ),
        ReadinessCheck(
            name="telemetry",
            status="pass" if telemetry_ready else "fail",
            detail="OpenTelemetry bootstrap completed."
            if telemetry_ready
            else "OpenTelemetry bootstrap is not available.",
        ),
    ]
    checks.extend(dependency_checks or [])

    overall_status: Literal["ready", "not_ready"] = (
        "ready" if all(check.status == "pass" for check in checks) else "not_ready"
    )
    return ReadinessResponse(service=service, status=overall_status, checks=checks)
