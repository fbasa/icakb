"""FastAPI application for the version, health, and error-format foundation."""

from __future__ import annotations

import logging
import os
from collections.abc import Mapping

from fastapi import FastAPI, Header, Response, status
from telemetry_python.logging import configure_json_logging

from .configuration import ConfigurationValidationError, load_runtime_configuration
from .dependencies import DependencyProbe, SocketDependencyProbe
from .health import (
    LiveHealthResponse,
    ReadinessCheck,
    ReadinessResponse,
    build_live_health_response,
    build_readiness_response,
)
from .problem_details import register_problem_handlers
from .request_context import RequestCorrelationMiddleware, install_request_context_filter
from .telemetry import bootstrap_telemetry
from .version import build_version_response, resolve_version_metadata


class RuntimeConfigurationError(RuntimeError):
    """Raised when startup configuration is invalid without exposing raw inputs."""


def create_app(
    environment: Mapping[str, str] | None = None,
    *,
    dependency_probe: DependencyProbe | None = None,
) -> FastAPI:
    """Create the API application."""

    env = dict(os.environ if environment is None else environment)
    try:
        runtime_configuration = load_runtime_configuration(env)
    except ConfigurationValidationError:
        raise RuntimeConfigurationError(
            "Runtime configuration validation failed. Review required environment variables."
        ) from None
    configure_json_logging(level=getattr(logging, runtime_configuration.log_level))
    install_request_context_filter()
    metadata = resolve_version_metadata(env)

    application = FastAPI(title="ICAKB API", version=runtime_configuration.app_version)
    telemetry_state = bootstrap_telemetry(
        service_name=metadata.service,
        service_version=metadata.version,
    )
    application.state.runtime_configuration = runtime_configuration
    application.state.dependency_probe = dependency_probe or SocketDependencyProbe()
    application.state.configuration_validated = True
    application.state.telemetry_bootstrapped = telemetry_state.tracer_provider_installed
    application.add_middleware(RequestCorrelationMiddleware)
    register_problem_handlers(application)

    @application.get("/version")
    def get_version() -> dict[str, str]:
        return build_version_response(env)

    @application.get("/health/live")
    def get_live_health() -> LiveHealthResponse:
        return build_live_health_response(service=metadata.service)

    @application.get("/health/startup")
    def get_startup_health() -> ReadinessResponse:
        return build_readiness_response(
            service=metadata.service,
            configuration_ready=bool(application.state.configuration_validated),
            telemetry_ready=bool(application.state.telemetry_bootstrapped),
            dependency_checks=[],
        )

    @application.get("/health/ready")
    def get_ready_health(response: Response) -> ReadinessResponse:
        probe = application.state.dependency_probe
        readiness = build_readiness_response(
            service=metadata.service,
            configuration_ready=bool(application.state.configuration_validated),
            telemetry_ready=bool(application.state.telemetry_bootstrapped),
            dependency_checks=probe.readiness_checks(runtime_configuration),
        )
        if readiness.status != "ready":
            response.status_code = status.HTTP_503_SERVICE_UNAVAILABLE
        return readiness

    @application.get("/health/dependencies")
    def get_dependency_health(
        response: Response,
        x_operations_token: str | None = Header(default=None, alias="X-Operations-Token"),
    ) -> ReadinessResponse:
        expected_token = runtime_configuration.operational_diagnostics_token.get_secret_value()
        if x_operations_token != expected_token:
            response.status_code = status.HTTP_401_UNAUTHORIZED
            return ReadinessResponse(
                service=metadata.service,
                status="not_ready",
                checks=[
                    ReadinessCheck(
                        name="authentication",
                        status="fail",
                        detail="Operational diagnostics require authentication.",
                    )
                ],
            )

        probe = application.state.dependency_probe
        diagnostics = build_readiness_response(
            service=metadata.service,
            configuration_ready=bool(application.state.configuration_validated),
            telemetry_ready=bool(application.state.telemetry_bootstrapped),
            dependency_checks=probe.diagnostic_checks(runtime_configuration),
        )
        if diagnostics.status != "ready":
            response.status_code = status.HTTP_503_SERVICE_UNAVAILABLE
        return diagnostics

    return application


app = create_app()
