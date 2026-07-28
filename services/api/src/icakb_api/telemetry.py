"""OpenTelemetry bootstrap helpers for the API service."""

from __future__ import annotations

from dataclasses import dataclass
from threading import Lock

from opentelemetry import trace
from opentelemetry.sdk.resources import Resource
from opentelemetry.sdk.trace import TracerProvider

_BOOTSTRAP_LOCK = Lock()
_TRACER_PROVIDER_INSTALLED = False


@dataclass(frozen=True, slots=True)
class TelemetryBootstrapState:
    """Describe the local OpenTelemetry bootstrap state."""

    tracer_provider_installed: bool
    service_name: str
    service_version: str


def bootstrap_telemetry(*, service_name: str, service_version: str) -> TelemetryBootstrapState:
    """Install an SDK tracer provider if one has not been configured yet."""

    global _TRACER_PROVIDER_INSTALLED

    with _BOOTSTRAP_LOCK:
        if not _TRACER_PROVIDER_INSTALLED:
            resource = Resource.create(
                {
                    "service.name": service_name,
                    "service.version": service_version,
                }
            )
            trace.set_tracer_provider(TracerProvider(resource=resource))
            _TRACER_PROVIDER_INSTALLED = True

    return TelemetryBootstrapState(
        tracer_provider_installed=True,
        service_name=service_name,
        service_version=service_version,
    )
