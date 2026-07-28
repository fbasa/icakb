"""Bounded operational dependency probes for health endpoints."""

from __future__ import annotations

import socket
from typing import Protocol
from urllib.parse import urlparse

from .configuration import RuntimeConfiguration
from .health import ReadinessCheck


class DependencyProbe(Protocol):
    """Probe runtime dependencies without exposing provider-specific SDK objects."""

    def readiness_checks(self, configuration: RuntimeConfiguration) -> list[ReadinessCheck]:
        """Return dependency checks required before the service receives traffic."""

    def diagnostic_checks(self, configuration: RuntimeConfiguration) -> list[ReadinessCheck]:
        """Return operational diagnostics for all configured external dependencies."""


class SocketDependencyProbe:
    """Dependency probe using bounded TCP connections."""

    def __init__(self, *, timeout_seconds: float = 1.0) -> None:
        self._timeout_seconds = timeout_seconds

    def readiness_checks(self, configuration: RuntimeConfiguration) -> list[ReadinessCheck]:
        return [
            _tcp_check(
                "database",
                str(configuration.database_url.get_secret_value()),
                timeout_seconds=self._timeout_seconds,
            ),
            ReadinessCheck(
                name="migrations",
                status="pass",
                detail="No migrations are configured in the Phase 0 foundation.",
            ),
            _tcp_check(
                "object_storage",
                str(configuration.object_storage_endpoint),
                timeout_seconds=self._timeout_seconds,
            ),
        ]

    def diagnostic_checks(self, configuration: RuntimeConfiguration) -> list[ReadinessCheck]:
        return [
            *self.readiness_checks(configuration),
            _tcp_check(
                "queue", str(configuration.queue_url), timeout_seconds=self._timeout_seconds
            ),
            ReadinessCheck(
                name="openai",
                status="pass",
                detail="OpenAI project and API key are configured; live reachability is deferred.",
            ),
            ReadinessCheck(
                name="telemetry",
                status="pass",
                detail="OpenTelemetry bootstrap state is reported by readiness.",
            ),
        ]


def _tcp_check(name: str, raw_url: str, *, timeout_seconds: float) -> ReadinessCheck:
    parsed = urlparse(raw_url)
    host = parsed.hostname
    port = parsed.port
    if host is None or port is None:
        return ReadinessCheck(
            name=name,
            status="fail",
            detail="Dependency URL does not include a host and port.",
        )

    try:
        with socket.create_connection((host, port), timeout=timeout_seconds):
            pass
    except OSError:
        return ReadinessCheck(
            name=name,
            status="fail",
            detail="Dependency TCP probe failed.",
        )

    return ReadinessCheck(
        name=name,
        status="pass",
        detail="Dependency TCP probe succeeded.",
    )
