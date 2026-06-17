# Quality Gates

This POC treats pre-commit as both a local developer guardrail and a CI quality
gate. The workflow is intentionally measurable so CI runtime, hook performance,
cross-platform behavior, CI failures, and PR formatting noise can be reviewed
without guessing.

## Acceptance criteria

| Work item              | Validation                                                                       | Done when                                                             |
| ---------------------- | -------------------------------------------------------------------------------- | --------------------------------------------------------------------- |
| Optimize CI runtime    | CI caches pre-commit, pip, and npm dependencies and enforces a runtime threshold | Pre-commit job finishes within `PRE_COMMIT_RUNTIME_THRESHOLD_SECONDS` |
| Performance testing    | CI measures `pre-commit run --all-files` elapsed time                            | GitHub Actions summary shows elapsed seconds for each runner OS       |
| Cross-platform testing | CI runs the same hook suite on Ubuntu, Windows, and macOS                        | The matrix passes on all three operating systems                      |
| Track CI failures      | GitHub Actions keeps pass/fail history for push and PR runs                      | Failure rate can be compared before and after pre-commit adoption     |
| PR quality assessment  | PR template asks authors to confirm automated formatting/linting was used        | Review comments about formatting-only issues trend down               |

## Runtime threshold

The default threshold is configured in `.github/workflows/pre-commit.yml`:

```yaml
PRE_COMMIT_RUNTIME_THRESHOLD_SECONDS: "300"
```

Tune this value only after reviewing at least a few successful runs across all
matrix operating systems. Keep the threshold high enough to avoid noisy failures
but low enough to catch dependency or hook regressions.

## CI failure tracking

Use the GitHub Actions history for the `Pre-commit` workflow to compare:

- total runs
- failed runs
- most common failing hook
- elapsed runtime by operating system

For a lightweight before/after view, capture these numbers before enabling the
workflow and again after several PRs have used it.

## PR noise tracking

During review, count comments that only request formatting, import ordering,
lint cleanup, or whitespace changes. These comments should decrease because the
same checks run locally and in CI before human review.
