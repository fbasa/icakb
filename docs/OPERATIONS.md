# Operations

## Required runbooks

The following procedures must be implemented and validated as their dependent phases complete:

- Deployment and post-deployment verification.
- Application rollback.
- Database migration and migration rollback or forward recovery.
- Prompt and model configuration rollback.
- OpenAI outage and rate-limit response.
- Queue backlog and dead-letter recovery.
- Failed ingestion replay and reconciliation.
- Document deletion verification.
- Tenant disablement and offboarding.
- Secret rotation.
- Backup, restore, and disaster recovery.
- Incident response, severity, escalation, and communication.

## Deployment principles

- Build once and promote the same immutable artifact digest.
- Require protected approvals for production.
- Apply backward-compatible database changes before application rollout.
- Verify liveness, readiness, version, authentication, retrieval, and citations after deployment.
- Stop or roll back when health thresholds fail.

## Version endpoint development demo

The Phase 0 version-endpoint slice is deployed locally through Docker Compose:

1. `make deploy-version-endpoint`
2. `make smoke-version-endpoint`

Rollback for the demo is a redeploy of the previous known-good revision:

1. Check out the previous commit or tagged release.
2. Run `make deploy-version-endpoint`.
3. Run `make smoke-version-endpoint`.

This repository demo uses the same immutable source revision for the local deployment and the smoke check. Production rollback remains a later-phase operational runbook task.

## GitHub Actions development deployment

The development deployment workflow in `.github/workflows/deploy-development.yml` assumes AWS credentials through GitHub OIDC and promotes an immutable image digest after CI succeeds.

Configure these repository variables before enabling the workflow:

- `AWS_REGION`
- `AWS_ACCOUNT_ID`
- `AWS_ROLE_TO_ASSUME`
- `AWS_ECR_REPOSITORY`
- `AWS_ECS_CLUSTER`
- `AWS_ECS_SERVICE`
- `AWS_ECS_TASK_DEFINITION`
- `AWS_ECS_CONTAINER_NAME`
- `DEVELOPMENT_BASE_URL`

The workflow:

1. Assumes the AWS deployment role with OIDC.
2. Builds the API image from `services/api/Dockerfile`.
3. Pushes the image to ECR with the commit SHA tag.
4. Resolves the pushed image digest.
5. Scans the published immutable image reference.
6. Registers a new ECS task definition revision that references the immutable digest.
7. Fails if the configured container name does not match exactly one task-definition container.
8. Updates the development service to that revision.
9. Waits for ECS service stability.
10. Runs deployment smoke tests against `DEVELOPMENT_BASE_URL`.
11. Verifies the deployed `/version` commit SHA matches the workflow commit.

Rollback uses `.github/workflows/rollback-development.yml` with a known-good ECS task definition ARN. The rollback workflow updates the service, waits for stability, and reruns the same smoke test against `DEVELOPMENT_BASE_URL`.

## Operational telemetry

Monitor request latency, errors, streaming failures, token usage, retrieval duration and result counts, empty retrieval, citations, queue depth, oldest job age, ingestion failures, indexing duration, database-pool use, authorization denials, rate limits, and health-check failures.

## Data handling

Logs and traces must not record raw internal documents, retrieved passages, user prompts, cookies, tokens, API keys, or connection strings by default. Deletion workflows must verify all configured storage locations and caches.
