from __future__ import annotations

import pytest
from icakb_api.configuration import (
    ConfigurationValidationError,
    RuntimeConfiguration,
    load_runtime_configuration,
)
from pydantic import SecretStr

BASE_ENVIRONMENT = {
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

SENSITIVE_VALUES = (
    "sk-proj-test-secret-value",
    "database-password-value",
    "postgresql://app:database-password-value@localhost:5432/knowledge_assistant",
    "session-cookie-value",
    "bearer-token-value",
)


def test_load_runtime_configuration_validates_the_committed_environment_contract() -> None:
    configuration = load_runtime_configuration(BASE_ENVIRONMENT)

    assert isinstance(configuration, RuntimeConfiguration)
    assert configuration.app_env == "local"
    assert configuration.app_version == "0.0.0-dev"
    assert configuration.log_level == "INFO"
    assert isinstance(configuration.openai_api_key, SecretStr)
    assert str(configuration.openai_api_key) == "**********"
    assert configuration.openai_api_key.get_secret_value() == "replace-with-sandbox-key-only"
    assert (
        str(configuration.database_url.get_secret_value())
        == "postgresql://app:app@localhost:5432/knowledge_assistant"
    )
    assert str(configuration.queue_url) == "http://localhost:4566/000000000000/ingestion"


def test_load_runtime_configuration_rejects_invalid_values() -> None:
    invalid_environment = dict(BASE_ENVIRONMENT)
    invalid_environment["QUEUE_URL"] = "not-a-url"

    with pytest.raises(ConfigurationValidationError):
        load_runtime_configuration(invalid_environment)


def test_runtime_configuration_validation_errors_do_not_render_sensitive_inputs() -> None:
    invalid_environment = dict(BASE_ENVIRONMENT)
    invalid_environment.update(
        {
            "DATABASE_URL": (
                "postgresql://app:database-password-value@localhost:5432/knowledge_assistant"
            ),
            "OPENAI_API_KEY": "sk-proj-test-secret-value",
            "QUEUE_URL": "not-a-url?token=bearer-token-value",
            "OIDC_AUDIENCE": "session-cookie-value",
            "OPERATIONAL_DIAGNOSTICS_TOKEN": "bearer-token-value",
        }
    )

    with pytest.raises(ConfigurationValidationError) as exc_info:
        load_runtime_configuration(invalid_environment)

    rendered_error = str(exc_info.value)
    rendered_details = str(exc_info.value.errors())
    rendered_json = exc_info.value.json()
    assert "input_value" not in rendered_error
    assert "input_type" not in rendered_error
    for rendered_value in (rendered_error, rendered_details, rendered_json):
        assert "input" not in rendered_value
        assert "ctx" not in rendered_value
        for sensitive_value in SENSITIVE_VALUES:
            assert sensitive_value not in rendered_value


def test_runtime_configuration_serialization_redacts_sensitive_values() -> None:
    sensitive_environment = dict(BASE_ENVIRONMENT)
    sensitive_environment.update(
        {
            "DATABASE_URL": (
                "postgresql://app:database-password-value@localhost:5432/knowledge_assistant"
            ),
            "OPENAI_API_KEY": "sk-proj-test-secret-value",
            "OPERATIONAL_DIAGNOSTICS_TOKEN": "bearer-token-value",
        }
    )
    configuration = load_runtime_configuration(sensitive_environment)

    rendered_model = str(configuration)
    rendered_dump = str(configuration.model_dump())
    rendered_json = configuration.model_dump_json()

    for rendered_value in (rendered_model, rendered_dump, rendered_json):
        assert "**********" in rendered_value
        for sensitive_value in SENSITIVE_VALUES:
            assert sensitive_value not in rendered_value
