# Pre-commit Setup

This repository uses `pre-commit` to enforce a common set of quality checks
before committing code.

## Install

```bash
python -m pip install --upgrade pre-commit
```

## Enable Git hook

```bash
pre-commit install
```

## Run locally

```bash
pre-commit run --all-files
```
