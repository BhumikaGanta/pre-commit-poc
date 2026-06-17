# Universal Pre-Commit POC

## Overview

This repository demonstrates a reusable, multi-language pre-commit framework
to enforce code quality checks before code is committed.

## Goals

- Shift-left code quality checks
- Reduce PR review effort
- Minimize CI failures
- Provide reusable configuration

## Supported Languages

- Python
- JavaScript / TypeScript
- Java
- C / C++
- C#

## How It Works

Pre-commit hooks run automatically before each git commit and the same checks
are enforced in CI using GitHub Actions.

## Getting Started

1. Install `pre-commit` in your environment:
   ```bash
   python -m pip install --upgrade pre-commit
   ```
2. Install the Git hook for this repository:
   ```bash
   pre-commit install
   ```
3. Run all checks once locally:
   ```bash
   pre-commit run --all-files
   ```

## CI Integration

A GitHub Actions workflow is configured at
`.github/workflows/pre-commit.yml` to run the same checks on push and pull requests.

## Quality Gates

- CI runs the pre-commit suite on Linux, Windows, and macOS.
- CI records hook execution time in the GitHub Actions job summary.
- CI fails when hook execution exceeds `PRE_COMMIT_RUNTIME_THRESHOLD_SECONDS`.
- PR authors use `.github/pull_request_template.md` to confirm formatting noise was handled by automation.

See `docs/quality-gates.md` for acceptance criteria and operating guidance.
