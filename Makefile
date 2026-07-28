.PHONY: help bootstrap dev deploy-version-endpoint smoke-version-endpoint format format-check lint typecheck test security check

help:
	@printf '%s\n' 'bootstrap dev deploy-version-endpoint smoke-version-endpoint format format-check lint typecheck test security check'

bootstrap:
	uv sync --frozen --all-packages
	pnpm install --frozen-lockfile
	uv run pre-commit install

dev:
	docker compose up -d postgres object-storage api

deploy-version-endpoint:
	docker compose up -d --build postgres object-storage api

smoke-version-endpoint:
	BASE_URL=http://127.0.0.1:8000 uv run --all-packages pytest tests/smoke/test_version_endpoint.py -q

format:
	uv run --all-packages ruff format python-packages services
	pnpm format

format-check:
	uv run --all-packages ruff format --check python-packages services tests
	pnpm format:check

lint:
	uv run --all-packages ruff check python-packages services tests
	pnpm lint
	uv run pre-commit run --all-files

typecheck:
	uv run --all-packages mypy python-packages services
	pnpm typecheck

test:
	uv run --all-packages pytest
	pnpm test:vitest
	pnpm test:playwright

security:
	uv run pre-commit run check-added-large-files --all-files
	pnpm audit --audit-level high

check: format-check lint typecheck test security
