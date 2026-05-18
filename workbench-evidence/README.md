# Workbench Evidence Fixtures

This directory contains sanitized synthetic Workbench evidence for the toy PR
gate proof repository.

Folders:

- `accept`: complete evidence expected to render a PR gate `accept` outcome.
- `needs-review`: complete evidence expected to render a `needs_review`
  outcome.
- `block`: complete evidence expected to render a `block` outcome.
- `scaffold-fallback`: validation-only fallback evidence. It intentionally
  omits `revision_decision.json`, so it must block with
  `pr_gate.acceptance_evidence_missing` when used as fallback evidence.

Hygiene boundary:

- no raw provider transcripts
- no provider credentials or tokens
- no local absolute paths
- no private source repository paths
- no private run history
