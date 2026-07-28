# Main branch protection

`main.json` is the reviewable baseline for the classic GitHub branch-protection
rule on `main`.

The baseline:

- requires pull requests and one approving review;
- dismisses approvals after new commits;
- applies protections to repository administrators;
- requires successful CI and security status checks before merge;
- requires review conversations to be resolved; and
- prevents force-pushes and branch deletion.

Code-owner reviews are intentionally unset because the current `CODEOWNERS`
handles require repository teams that have not yet been provisioned.

## Apply

An administrator authenticated by GitHub CLI with repository Administration
write permission can apply the policy:

```bash
gh api \
  --method PUT \
  -H "X-GitHub-Api-Version: 2026-03-10" \
  "repos/OWNER/REPOSITORY/branches/main/protection" \
  --input .github/branch-protection/main.json
```

Replace `OWNER/REPOSITORY` with the repository's actual GitHub identifier. Do
not commit or pass a token on the command line; use `gh auth login`.

## Verify

```bash
gh api \
  -H "X-GitHub-Api-Version: 2026-03-10" \
  "repos/OWNER/REPOSITORY/branches/main/protection"
```

Verify that pull-request review protection and administrator enforcement are
enabled, required status checks match `main.json`, force-pushes and deletion are
disabled, and conversation resolution is required.
