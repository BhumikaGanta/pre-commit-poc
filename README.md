
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
