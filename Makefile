.PHONY: help bootstrap dev format lint typecheck test security check

help:
	@printf '%s
' 'bootstrap dev format lint typecheck test security check'

bootstrap:
	@echo 'Phase 0 task: implement deterministic bootstrap.'

dev:
	@echo 'Phase 0 task: start local development stack.'

format:
	@echo 'Phase 0 task: run repository formatters.'

lint:
	@echo 'Phase 0 task: run repository linters.'

typecheck:
	@echo 'Phase 0 task: run Python and TypeScript type checks.'

test:
	@echo 'Phase 0 task: run automated tests.'

security:
	@echo 'Phase 0 task: run secret and vulnerability scans.'

check: format lint typecheck test security
