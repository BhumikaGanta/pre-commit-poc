# Feature 6: Developer Enablement Guide

## What This Repository Provides

This repository provides a multi-language pre-commit framework for Python,
JavaScript, TypeScript, Java, C/C++, and C#. It is designed to catch formatting,
linting, static-analysis, merge-conflict, YAML, JSON, and secret issues before
code reaches pull request review.

## One-Time Setup

1. Install Python and pre-commit.

   ```bash
   python -m pip install --upgrade pre-commit
   ```

2. Install repository dependencies.

   ```bash
   npm ci
   ```

3. Install the Git hook.

   ```bash
   pre-commit install
   ```

4. Run the full suite once.

   ```bash
   pre-commit run --all-files
   ```

## Recommended Windows Setup

This repo normalizes text files with LF endings through `.gitattributes`.
For the cleanest local experience on Windows, use repo-local Git settings:

```bash
git config core.autocrlf false
git config core.eol lf
```

This prevents repeated "modified" files after tools such as Prettier, Black,
and end-of-file-fixer rewrite files with LF endings.

## Daily Developer Workflow

<!-- prettier-ignore -->
| Scenario                         | Command                            | Expected Result                              |
| -------------------------------- | ---------------------------------- | -------------------------------------------- |
| Check staged files before commit | `git commit`                       | Pre-commit runs automatically                |
| Check the full repository        | `pre-commit run --all-files`       | All hooks pass or report actionable failures |
| Run one hook only                | `pre-commit run black --all-files` | Only Python formatting is checked            |
| See hook-created changes         | `git diff`                         | Shows files auto-fixed by formatting hooks   |
| Retry after fixes                | `pre-commit run --all-files`       | Previously fixed hooks should pass           |

## Auto-Fix Behavior

<!-- prettier-ignore -->
| Hook                        | Auto-Fixes Locally   | Auto-Fixes in CI | Notes                                                    |
| --------------------------- | -------------------- | ---------------- | -------------------------------------------------------- |
| `trailing-whitespace`       | Yes                  | Check-only result | Removes trailing spaces                                  |
| `end-of-file-fixer`         | Yes                  | Check-only result | Ensures final newline                                    |
| `black`                     | Yes                  | Check-only result | Formats Python                                           |
| `isort`                     | Yes                  | Check-only result | Sorts Python imports                                     |
| `prettier`                  | Yes                  | Check-only result | Formats JS, TS, JSON, YAML, and Markdown                 |
| `ruff`                      | No by current config | No               | Reports lint issues; `--fix` is not enabled              |
| `eslint`                    | No by current config | No               | Reports JS/TS lint issues                                |
| `detect-secrets`            | No                   | No               | Reports potential secrets                                |
| `check-yaml` / `check-json` | No                   | No               | Validates syntax                                         |
| `check-merge-conflict`      | No                   | No               | Detects unresolved conflict markers                      |
| `clang-format`              | No by current config | No               | Uses `--dry-run --Werror` as a check-only gate            |
| `cppcheck`                  | No                   | No               | Static analysis only                                     |
| `dotnet format`             | No by current config | No               | Uses `--verify-no-changes` as a check-only gate           |
| `tsc`                       | No                   | No               | Type-check only                                          |
| `checkstyle`                | No                   | No               | Build-tool-backed Java validation when configured        |

## Local vs CI Behavior

- Local runs are developer-friendly: auto-fix hooks can rewrite files so the developer can review and commit the changes.
- CI runs the same pre-commit command, but CI should not commit changes back automatically.
- If an auto-fix hook changes files in CI, the job fails and the developer must run the hook locally, commit the generated changes, and push again.
- CI adds additional confidence by running on Ubuntu, Windows, and macOS.

## Why Files Appeared Modified After Every Run

The repeated modified-file list was caused by Windows line-ending conversion.
Git was configured with `core.autocrlf=true`, while pre-commit tools rewrote
some files using LF endings. The repository now includes `.gitattributes`, and
this local clone has `core.autocrlf=false`, which stops the repeated noise.

## Troubleshooting

<!-- prettier-ignore -->
| Symptom                                       | Likely Cause                 | Fix                                                                |
| --------------------------------------------- | ---------------------------- | ------------------------------------------------------------------ |
| Many files show modified but `git diff` empty | Line-ending/index noise      | Run `git config core.autocrlf false`, then restore or refresh files |
| `pre-commit` cannot write cache database      | User cache permission issue  | Clear or fix permissions for `~/.cache/pre-commit`                 |
| SSH fetch fails on port 22                    | Network blocks SSH to GitHub | Use HTTPS remote URL                                               |
| `cppcheck` missing locally                    | System package not installed | Install `cppcheck` or rely on CI for that gate                     |
| C# hook fails locally                         | .NET SDK missing             | Install .NET 8 SDK                                                 |
