"""Runtime environment validation for the API service."""

from __future__ import annotations

import json
import os
from collections.abc import Mapping
from typing import Any, Literal

from pydantic import (
    AnyUrl,
    BaseModel,
    ConfigDict,
    Field,
    PostgresDsn,
    Secret,
    SecretStr,
    ValidationError,
)


class RuntimeConfiguration(BaseModel):
    """Validated environment variables required by the API service."""

    model_config = ConfigDict(
        extra="forbid",
        frozen=True,
        hide_input_in_errors=True,
        str_strip_whitespace=True,
    )

    app_env: str = Field(alias="APP_ENV", min_length=1)
    app_version: str = Field(alias="APP_VERSION", min_length=1)
    log_level: Literal["CRITICAL", "ERROR", "WARNING", "INFO", "DEBUG"] = Field(alias="LOG_LEVEL")
    database_url: Secret[PostgresDsn] = Field(alias="DATABASE_URL")
    object_storage_endpoint: AnyUrl = Field(alias="OBJECT_STORAGE_ENDPOINT")
    object_storage_bucket: str = Field(alias="OBJECT_STORAGE_BUCKET", min_length=1)
    queue_url: AnyUrl = Field(alias="QUEUE_URL")
    openai_api_key: SecretStr = Field(alias="OPENAI_API_KEY", min_length=1)
    openai_project_id: str = Field(alias="OPENAI_PROJECT_ID", min_length=1)
    oidc_issuer_url: AnyUrl = Field(alias="OIDC_ISSUER_URL")
    oidc_audience: str = Field(alias="OIDC_AUDIENCE", min_length=1)
    operational_diagnostics_token: SecretStr = Field(
        alias="OPERATIONAL_DIAGNOSTICS_TOKEN",
        min_length=1,
    )


_REQUIRED_ENVIRONMENT_KEYS: tuple[str, ...] = tuple(
    field.alias or name for name, field in RuntimeConfiguration.model_fields.items()
)


class ConfigurationValidationError(ValueError):
    """Sanitized configuration validation failure safe for logs and tracebacks."""

    def __init__(self, errors: tuple[dict[str, object], ...]) -> None:
        self._errors = errors
        super().__init__(
            "Runtime configuration validation failed. Review required environment variables."
        )

    def errors(self) -> tuple[dict[str, object], ...]:
        """Return validation details without raw input values or context."""

        return self._errors

    def json(self) -> str:
        """Serialize sanitized validation details."""

        return json.dumps(self._errors, separators=(",", ":"))


def _sanitize_validation_errors(error: ValidationError) -> tuple[dict[str, object], ...]:
    """Remove raw inputs and contexts from Pydantic validation details."""

    sanitized_errors: list[dict[str, object]] = []
    for validation_error in error.errors(include_context=False, include_input=False):
        sanitized_error: dict[str, object] = {
            "type": validation_error["type"],
            "loc": tuple(validation_error["loc"]),
            "msg": validation_error["msg"],
        }
        if url := validation_error.get("url"):
            sanitized_error["url"] = url
        sanitized_errors.append(sanitized_error)
    return tuple(sanitized_errors)


def _select_environment_values(environment: Mapping[str, str]) -> dict[str, Any]:
    """Select only the configuration fields this service validates."""

    return {key: environment[key] for key in _REQUIRED_ENVIRONMENT_KEYS if key in environment}


def load_runtime_configuration(
    environment: Mapping[str, str] | None = None,
) -> RuntimeConfiguration:
    """Load and validate the API runtime environment."""

    env = os.environ if environment is None else environment
    try:
        return RuntimeConfiguration.model_validate(_select_environment_values(env))
    except ValidationError as error:
        raise ConfigurationValidationError(_sanitize_validation_errors(error)) from None
