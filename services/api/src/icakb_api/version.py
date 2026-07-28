"""Version endpoint payload helpers."""

from __future__ import annotations

import os
import platform
from collections.abc import Callable, Mapping
from dataclasses import asdict, dataclass
from datetime import UTC, datetime


def _utc_now() -> str:
    return datetime.now(UTC).isoformat(timespec="milliseconds").replace("+00:00", "Z")


@dataclass(frozen=True, slots=True)
class VersionMetadata:
    """Version payload fields returned by the demo endpoint."""

    service: str
    version: str
    commit_sha: str
    build_time: str
    python_version: str


def resolve_version_metadata(
    environment: Mapping[str, str] | None = None,
    *,
    now: Callable[[], str] = _utc_now,
) -> VersionMetadata:
    """Resolve version metadata from the provided environment mapping."""

    env = os.environ if environment is None else environment
    app_env = env.get("APP_ENV", "local")
    commit_sha = env.get("APP_COMMIT_SHA", "unknown")
    build_time = env.get("APP_BUILD_TIME", now())
    if app_env not in {"local", "development", "test"} and (
        commit_sha == "unknown" or not build_time
    ):
        raise RuntimeError("Release builds require APP_COMMIT_SHA and APP_BUILD_TIME.")

    return VersionMetadata(
        service=env.get("APP_NAME", "api"),
        version=env.get("APP_VERSION", "0.0.0-dev"),
        commit_sha=commit_sha,
        build_time=build_time,
        python_version=platform.python_version(),
    )


def build_version_response(
    environment: Mapping[str, str] | None = None,
    *,
    now: Callable[[], str] = _utc_now,
) -> dict[str, str]:
    """Render the version metadata as a JSON-serializable payload."""

    return asdict(resolve_version_metadata(environment, now=now))
