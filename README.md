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
