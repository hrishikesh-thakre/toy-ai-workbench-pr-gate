# Toy AI Workbench PR Gate

Tiny Python package used as an external proof target for the AI Workbench PR
gate workflow.

This repository is not an AI Workbench source checkout. It exists to prove that
another repository can copy the AI Workbench PR gate workflow, install the
published `ai-workbench-mcp==0.3.0a0` package, and render PR-facing decisions
from Workbench evidence.

## Proof Fixtures

Synthetic sanitized evidence lives in `workbench-evidence/`:

- `accept` renders an `accept` PR gate outcome.
- `needs-review` renders a `needs_review` PR gate outcome.
- `block` renders a `block` PR gate outcome.
- `scaffold-fallback` intentionally omits `revision_decision.json` and must
  never render `accept`.

Generated `runs/` evidence remains ignored.

## Local Checks

```bash
python -m pytest
```

## Package

`toycalc` exposes one arithmetic helper:

```python
from toycalc import add

assert add(2, 3) == 5
```
