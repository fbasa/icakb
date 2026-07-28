from __future__ import annotations

import json
import os
from http import HTTPStatus
from time import monotonic, sleep
from urllib.error import HTTPError, URLError
from urllib.request import urlopen

import pytest

BASE_URL = os.environ.get("BASE_URL")
EXPECTED_VERSION = os.environ.get("EXPECTED_VERSION", "0.0.0-dev")


def _fetch_json(base_url: str, path: str) -> dict[str, object]:
    with urlopen(f"{base_url}{path}", timeout=5) as response:
        assert response.status == HTTPStatus.OK
        body = response.read().decode("utf-8")
        return json.loads(body)


def _fetch_json_with_retry(
    base_url: str,
    path: str,
    *,
    timeout_seconds: int = 30,
) -> dict[str, object]:
    deadline = monotonic() + timeout_seconds
    last_error: Exception | None = None

    while monotonic() < deadline:
        try:
            return _fetch_json(base_url, path)
        except (HTTPError, URLError, TimeoutError, OSError, json.JSONDecodeError) as exc:
            last_error = exc
            sleep(1)

    pytest.fail(f"Timed out waiting for {base_url}{path}: {last_error}")
    raise AssertionError("unreachable")


def test_version_endpoint_deployment_smoke() -> None:
    if BASE_URL is None:
        pytest.fail("BASE_URL is required; deployment smoke tests must target a deployed service.")

    deployment_base_url = BASE_URL.rstrip("/")
    assert deployment_base_url.startswith(("http://", "https://"))

    version_payload = _fetch_json_with_retry(deployment_base_url, "/version")
    live_payload = _fetch_json_with_retry(deployment_base_url, "/health/live")
    ready_payload = _fetch_json_with_retry(deployment_base_url, "/health/ready")

    assert version_payload["service"] == "api"
    assert version_payload["version"] == EXPECTED_VERSION
    assert "build_time" in version_payload
    assert "python_version" in version_payload

    assert live_payload == {"service": "api", "status": "ok"}
    assert ready_payload["service"] == "api"
    assert ready_payload["status"] == "ready"
    assert {check["status"] for check in ready_payload["checks"]} == {"pass"}
