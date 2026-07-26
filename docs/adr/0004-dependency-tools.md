# Use pnpm and uv

- Status: Accepted
- Date: 2026-07-26

## Context

The monorepo needs reproducible dependency resolution in both ecosystems.

## Decision

Use pnpm workspaces and uv workspaces with committed lockfiles and frozen CI installs.

## Consequences

The repository supports two ecosystems but has deterministic installs.
