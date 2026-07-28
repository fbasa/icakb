from __future__ import annotations

import json
import logging
import sys
import unittest
from pathlib import Path

PROJECT_SRC = Path(__file__).resolve().parents[1] / "src"
if str(PROJECT_SRC) not in sys.path:
    sys.path.insert(0, str(PROJECT_SRC))

from telemetry_python.logging import JsonFormatter, configure_json_logging


class JsonLoggingTests(unittest.TestCase):
    def test_formatter_redacts_sensitive_values_and_keeps_context_structured(self) -> None:
        formatter = JsonFormatter()
        record = logging.LogRecord(
            name="icakb.telemetry",
            level=logging.INFO,
            pathname=__file__,
            lineno=42,
            msg="User %s signed in",
            args=("alice",),
            exc_info=None,
        )
        record.service = "api"
        record.environment = "local"
        record.request_id = "req-123"
        record.trace_id = "trace-456"
        record.event = "auth.login"
        record.password = "super-secret"
        record.audit_context = {
            "api_key": "abc123",
            "nested": [{"token": "def456"}, "plain"],
        }

        payload = json.loads(formatter.format(record))

        self.assertEqual(payload["level"], "INFO")
        self.assertEqual(payload["logger"], "icakb.telemetry")
        self.assertEqual(payload["message"], "User alice signed in")
        self.assertEqual(payload["service"], "api")
        self.assertEqual(payload["environment"], "local")
        self.assertEqual(payload["request_id"], "req-123")
        self.assertEqual(payload["trace_id"], "trace-456")
        self.assertEqual(payload["event"], "auth.login")
        self.assertEqual(payload["extra"]["password"], "[REDACTED]")
        self.assertEqual(payload["extra"]["audit_context"]["api_key"], "[REDACTED]")
        self.assertEqual(payload["extra"]["audit_context"]["nested"][0]["token"], "[REDACTED]")
        self.assertEqual(payload["extra"]["audit_context"]["nested"][1], "plain")

    def test_configure_json_logging_writes_compact_json_lines(self) -> None:
        import io

        output = io.StringIO()
        configure_json_logging(level=logging.ERROR, stream=output)

        logger = logging.getLogger("icakb.telemetry.test")
        logger.info("hidden")
        logger.info("ready", extra={"tenant_id": "tenant-1"})
        logger.error("ready", extra={"tenant_id": "tenant-1"})

        rendered = output.getvalue().strip()
        payload = json.loads(rendered)

        self.assertEqual(payload["logger"], "icakb.telemetry.test")
        self.assertEqual(payload["message"], "ready")
        self.assertEqual(payload["tenant_id"], "tenant-1")
        self.assertNotIn("\n", rendered)

        self.assertEqual(logging.getLogger().level, logging.ERROR)
        self.assertEqual(logging.getLogger("uvicorn.error").level, logging.ERROR)
        self.assertEqual(logging.getLogger("uvicorn.access").level, logging.ERROR)


if __name__ == "__main__":
    unittest.main()
