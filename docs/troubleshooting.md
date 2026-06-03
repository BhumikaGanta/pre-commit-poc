# Pre-commit Troubleshooting

## Common issues

- `pre-commit` not installed
  - Install with `python -m pip install --upgrade pre-commit`

- Hooks fail on Windows line endings
  - Ensure the repository line endings are normalized and run `git config core.autocrlf false`

- Workflow does not run
  - Confirm `.github/workflows/pre-commit.yml` exists and is committed to the repository.
