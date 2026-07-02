Developer Guide

Overview

This guide helps developers set up and use the Pre-Commit POC framework for local code validation and CI validation.

The framework ensures code quality by automatically running validation checks before commits and during GitHub Actions workflow execution.

---

Supported Hooks

The framework currently supports:

- Common validation hooks
- Python hooks (Black, Ruff, Isort)
- JavaScript hooks (ESLint, Prettier)
- TypeScript hooks (TypeScript Compiler Check)
- Java hooks (Checkstyle)
- C/C++ hooks (Clang Format, Cppcheck)
- C# hooks (.NET Format)

---

Prerequisites

Ensure the following tools are installed:

- Git
- Python 3.12+
- Node.js 20+
- .NET SDK 8.0
- Cppcheck
- Clang-format

---

Installation

Clone repository:

git clone <repository-url>
cd pre-commit-poc

Install pre-commit:

pip install pre-commit

Install hooks:

pre-commit install

Install Node dependencies:

npm install

---

Usage

Pre-commit hooks run automatically during commit.

Example:

git add .
git commit -m "sample commit"

Hooks validate files before allowing commit.

---

Bypass Hooks

In exceptional cases, hooks may be skipped using:

git commit --no-verify -m "commit message"

Refer to "bypass-policy.md" for approved scenarios.

---

CI Validation

All hooks also run in GitHub Actions during:

- Push to main/master
- Pull Request creation

Invalid code changes will fail CI checks.

---

Common Commands

Run all hooks manually:

pre-commit run --all-files

Run specific hook:

pre-commit run <hook-id>

Update hooks:

pre-commit autoupdate

---

Troubleshooting

Common fixes:

- Reinstall hooks

pre-commit install

- Clear cache

pre-commit clean

- Re-run hooks

pre-commit run --all-files

---

Summary

# The Pre-Commit POC framework improves code quality by catching formatting, linting, and validation issues early in the development lifecycle.

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
