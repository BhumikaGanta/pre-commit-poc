# Demo Guide

## Executive Summary

This POC demonstrates a centralized pre-commit quality framework that works
locally and in CI. It protects the repository from common hygiene issues,
formatting drift, lint errors, type errors, static-analysis findings, and
accidental secrets before code reaches review.

## What Is Implemented

<!-- prettier-ignore -->
| Area                 | Implementation                                                                                       |
| -------------------- | ---------------------------------------------------------------------------------------------------- |
| Common hygiene       | Whitespace cleanup, EOF normalization, merge-conflict detection, YAML validation, and JSON validation |
| Python               | Black formatting, Ruff linting, and isort import ordering                                            |
| JavaScript           | Prettier formatting and ESLint validation                                                            |
| TypeScript           | Prettier formatting and `tsc --noEmit` compiler validation                                           |
| Secrets              | `detect-secrets` scanning with a baseline file                                                       |
| Java                 | Local Checkstyle wrapper that uses Maven or Gradle when available                                    |
| C/C++                | `clang-format` check and `cppcheck` static analysis                                                  |
| C#                   | `dotnet format --verify-no-changes`                                                                  |
| CI                   | GitHub Actions workflow for push and pull request validation                                         |
| Cross-platform       | CI matrix runs on Ubuntu, Windows, and macOS                                                         |
| Runtime metrics      | CI records elapsed seconds and enforces a runtime threshold                                          |
| Developer enablement | Setup, troubleshooting, quality gates, metrics, requirements, and developer guide documentation      |

## Demo Flow

1. Show the centralized hook configuration.

   ```bash
   cat .pre-commit-config.yaml
   ```

2. Show the local quality gate passing.

   ```bash
   pre-commit run --all-files
   ```

3. Show that the working tree stays clean after the run.

   ```bash
   git status --short
   ```

4. Show CI parity.

   ```text
   .github/workflows/pre-commit.yml runs the same pre-commit command on push and pull requests.
   ```

5. Show runtime metrics.

   ```text
   The workflow writes elapsed seconds and threshold seconds to the GitHub Actions job summary.
   ```

6. Show developer enablement material.

   ```text
   docs/developer-guide.md
   docs/requirements.md
   docs/metrics.md
   docs/quality-gates.md
   docs/troubleshooting.md
   ```

## Scenario Matrix

<!-- prettier-ignore -->
| Scenario              | Example Issue                | Hook Response                                      | Auto-Fix             |
| --------------------- | ---------------------------- | -------------------------------------------------- | -------------------- |
| Trailing spaces       | Extra spaces at line end     | `trailing-whitespace` fails and rewrites file      | Yes                  |
| Missing final newline | File ends without newline    | `end-of-file-fixer` fails and rewrites file        | Yes                  |
| Invalid YAML          | Broken indentation or syntax | `check-yaml` fails                                 | No                   |
| Invalid JSON          | Missing comma or bad syntax  | `check-json` fails                                 | No                   |
| Python formatting     | Non-Black style              | `black` fails and rewrites file                    | Yes                  |
| Python import order   | Imports out of order         | `isort` fails and rewrites file                    | Yes                  |
| Python lint           | Ruff rule violation          | `ruff` fails                                       | No by current config |
| JS/TS formatting      | Non-Prettier style           | `prettier` fails and rewrites file                 | Yes                  |
| JS lint               | Undefined variable           | `eslint` fails                                     | No by current config |
| TS type error         | Type mismatch                | `tsc` fails                                        | No                   |
| Secret committed      | Token-like value             | `detect-secrets` fails                             | No                   |
| C/C++ style           | Non-clang-format style       | `clang-format` fails                               | No by current config |
| C/C++ static issue    | Cppcheck finding             | `cppcheck` fails                                   | No                   |
| C# formatting drift   | `dotnet format` changes file | `dotnet format --verify-no-changes` fails          | No by current config |
| Merge conflict marker | `<<<<<<< HEAD` remains       | `check-merge-conflict` fails                       | No                   |

## Local vs CI Explanation

The same pre-commit suite is used locally and in CI. The difference is how
auto-fixes are handled:

- Locally, auto-fix hooks modify files so developers can review and commit the fixes.
- In CI, auto-fix hooks may still attempt to modify files, but the job fails because CI does not commit generated changes.
- Therefore, developers should run `pre-commit run --all-files` before pushing to avoid CI failures.

## Current Health

Latest local validation:

```text
pre-commit run --all-files
All configured hooks passed.
```

The previous repeated modified-file issue was caused by Windows line-ending
conversion. The repo now includes `.gitattributes`, and the local clone has
`core.autocrlf=false` to keep pre-commit output stable.
