# Prompt Library

Prompts are reviewed source assets. They are not arbitrary strings scattered through application code.

Each prompt manifest entry must define an ID, version, purpose, owner, variables, output schema, supported models, evaluation datasets, change history, and checksum.

Prompt changes require:

- Variable validation.
- Associated evaluation coverage.
- Recorded model and prompt versions.
- Quality thresholds.
- A rollback version.
- Changelog entry when user-visible behavior changes.

Retrieved document text must be clearly delimited as untrusted evidence and must never be treated as trusted instructions.
