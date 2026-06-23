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

The Pre-Commit POC framework improves code quality by catching formatting, linting, and validation issues early in the development lifecycle.
