# AI Workbench PR Gate: Block

Decision: Block
Why: No complete Workbench acceptance evidence found for this PR.
Required next action: Provide a complete Workbench acceptance run with validation_report.json and revision_decision.json, then regenerate the PR gate artifact.
Evidence present: validation_report yes, revision_decision no

## Details

**Run ID:** `pr-gate-demo-scaffold-fallback`
**Evidence source:** `fallback_scaffold`
**Source run dir:** `workbench-evidence/scaffold-fallback`

## Status

| Check | Status |
|---|---|
| Validation | `passed` |
| Quality gate | `unknown` |

## Evidence

| Artifact | Path | Present |
|---|---|---|
| validation_report | `validation_report.json` | yes |
| revision_decision | `revision_decision.json` | no |
| model_output | `model_output.md` | yes |
| run_log | `run_log.jsonl` | yes |

## Reason Codes

- `validation.accepted`
- `pr_gate.acceptance_evidence_missing`

This artifact is generated from Workbench evidence only. It does not embed raw model output or provider logs.
