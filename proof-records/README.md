# External PR Gate Proof Records

Status: complete
Date: 2026-05-18

This directory records the public external proof for the copied AI Workbench PR
gate workflow. The workflow installed the published
`ai-workbench-mcp==0.3.0a0` package and rendered PR-facing artifacts from
synthetic sanitized Workbench evidence committed in this toy repository.

## Public Links

- Repository: <https://github.com/hrishikesh-thakre/toy-ai-workbench-pr-gate>
- Same-repository PR: <https://github.com/hrishikesh-thakre/toy-ai-workbench-pr-gate/pull/1>
- First PR run: <https://github.com/hrishikesh-thakre/toy-ai-workbench-pr-gate/actions/runs/26039196095>
- Sticky-comment update PR run: <https://github.com/hrishikesh-thakre/toy-ai-workbench-pr-gate/actions/runs/26039299132>
- Node 24 action update smoke run: <https://github.com/hrishikesh-thakre/toy-ai-workbench-pr-gate/actions/runs/26043403995>

## Verified Outcomes

| Proof case | Run | Expected | Recorded artifact |
|---|---:|---|---|
| Same-repo PR rerun | 26039299132 | `accept` | `pr-accept-rerun/` |
| Dispatch accept | 26039415176 | `accept` | `dispatch-accept/` |
| Dispatch needs review | 26039447479 | `needs_review` | `dispatch-needs-review/` |
| Dispatch block | 26039474439 | `block` | `dispatch-block/` |
| Dispatch scaffold fallback | 26039499619 | `block` | `dispatch-scaffold-fallback/` |
| Node 24 action update smoke | 26043403995 | `accept` | `node24-action-update-smoke/` |

The same-repository PR had exactly one `<!-- ai-workbench-pr-gate -->` sticky
comment after the second PR run, and that comment contained the `Accept`
outcome.

The proof PR was closed unmerged after the durable proof records were committed,
because it was only a trigger PR. The branch was deleted.

## Local Checks

Before publishing these records:

```text
python -m pytest -q
python -m ai_workbench_mcp.tools.pr_gate for accept, needs_review, block, and scaffold fallback
git diff --check
```

The scaffold fallback proof used a missing `workbench_run_dir` and
`workbench-evidence/scaffold-fallback` as fallback evidence. It rendered
`block`, not `accept`.
