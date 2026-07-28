from __future__ import annotations

import os
import sys
from pathlib import Path

PROJECT_SRC = Path(__file__).resolve().parents[1] / "src"
TELEMETRY_SRC = Path(__file__).resolve().parents[3] / "python-packages" / "telemetry-python" / "src"

DEFAULT_ENVIRONMENT = {
    "APP_ENV": "local",
    "APP_VERSION": "0.0.0-dev",
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

for path in (str(PROJECT_SRC), str(TELEMETRY_SRC)):
    if path not in sys.path:
        sys.path.insert(0, path)

for key, value in DEFAULT_ENVIRONMENT.items():
    os.environ.setdefault(key, value)
