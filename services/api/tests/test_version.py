from __future__ import annotations

import sys
import unittest
from pathlib import Path

PROJECT_SRC = Path(__file__).resolve().parents[1] / "src"
TELEMETRY_SRC = Path(__file__).resolve().parents[3] / "python-packages" / "telemetry-python" / "src"
for path in (str(PROJECT_SRC), str(TELEMETRY_SRC)):
    if path not in sys.path:
        sys.path.insert(0, path)

from icakb_api.version import build_version_response


class VersionEndpointTests(unittest.TestCase):
    def test_build_version_response_uses_environment_values(self) -> None:
        payload = build_version_response(
            {
                "APP_NAME": "api",
                "APP_VERSION": "1.2.3",
                "APP_COMMIT_SHA": "abc123",
                "APP_BUILD_TIME": "2026-07-26T00:00:00Z",
            },
            now=lambda: "ignored",
        )

        self.assertEqual(payload["service"], "api")
        self.assertEqual(payload["version"], "1.2.3")
        self.assertEqual(payload["commit_sha"], "abc123")
        self.assertEqual(payload["build_time"], "2026-07-26T00:00:00Z")
        self.assertRegex(payload["python_version"], r"^\d+\.\d+\.\d+$")

    def test_build_version_response_falls_back_to_safe_defaults(self) -> None:
        payload = build_version_response({}, now=lambda: "2026-07-26T00:00:00Z")

        self.assertEqual(payload["service"], "api")
        self.assertEqual(payload["version"], "0.0.0-dev")
        self.assertEqual(payload["commit_sha"], "unknown")
        self.assertEqual(payload["build_time"], "2026-07-26T00:00:00Z")


if __name__ == "__main__":
    unittest.main()
