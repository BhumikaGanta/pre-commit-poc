# Feature 5: Metrics

## Objective

Metrics make the pre-commit rollout measurable instead of opinion-based. The
goal is to prove whether the quality gate improves developer experience,
reduces CI failures, and removes formatting noise from reviews.

## Implemented Metrics

<!-- prettier-ignore -->
| Metric                       | Source                                | Current Implementation                                                   |
| ---------------------------- | ------------------------------------- | ------------------------------------------------------------------------ |
| Hook pass/fail status        | Local terminal and GitHub Actions job | `pre-commit run --all-files` reports each hook result                    |
| Runtime by operating system  | GitHub Actions summary                | Workflow records elapsed seconds per runner OS                           |
| Runtime threshold compliance | GitHub Actions workflow               | Fails when elapsed runtime exceeds `PRE_COMMIT_RUNTIME_THRESHOLD_SECONDS` |
| Cross-platform health        | GitHub Actions matrix                 | Ubuntu, Windows, and macOS jobs run independently                        |
| PR formatting noise          | PR review process                     | PR template asks authors to confirm formatting was handled by automation |
| Secret scanning status       | `detect-secrets` hook                 | Fails when a new unapproved secret is detected                           |

## Developer Feedback Collection

Use a lightweight feedback loop during rollout:

<!-- prettier-ignore -->
| Feedback Area       | Question                                               | Collection Method                                            |
| ------------------- | ------------------------------------------------------ | ------------------------------------------------------------ |
| Setup friction      | How long did first-time setup take?                    | Ask developers to record setup time during onboarding        |
| False positives     | Which hooks failed but did not represent a real issue? | Track in a shared issue or sprint retrospective              |
| Auto-fix usefulness | Which hooks fixed problems automatically?              | Compare pre-commit output with `git diff` after a failed run |
| Runtime pain        | Are hooks slowing normal commits?                      | Compare local run time with CI runtime summary               |
| Missing coverage    | Which language or check is not covered yet?            | Review failed PRs and escaped defects                        |

## Suggested Feedback Template

```text
Developer:
Date:
Command run:
Total runtime:
Hook that failed:
Was the failure valid? yes/no
Did the hook auto-fix the issue? yes/no
What was confusing?
Suggested improvement:
```

## Demo Talking Points

- The workflow already captures runtime and enforces a threshold, so performance is part of the quality gate.
- The PR template turns developer feedback into a repeatable checklist.
- Local feedback and CI feedback are intentionally aligned: developers can run the same command that CI runs.
- Metrics should be reviewed after several PRs to decide whether to tighten, relax, or expand hooks.
