Pre-Commit Hook Bypass Policy

Purpose

This document defines the approved scenarios for bypassing pre-commit hooks and ensures code quality is maintained while allowing flexibility during exceptional cases.

---

Bypass Command

Developers can bypass pre-commit hooks using:

git commit --no-verify -m "commit message"

---

Allowed Scenarios

Pre-commit hooks may be bypassed only in the following situations:

- Emergency production hotfix requiring immediate commit
- Local environment issue preventing hook execution
- Tool installation or configuration issue
- Temporary false-positive validation from hook tools

---

Restricted Scenarios

Pre-commit hooks must not be bypassed for:

- Regular feature development
- Standard bug fixes
- Intentionally ignoring lint, format, or validation issues
- Skipping checks to speed up development

---

Approval Process

- Developer should inform the tech lead or reviewer before bypassing hooks
- Reason for bypass should be clearly communicated
- Bypassed validations must be verified later through CI checks

---

Post-Bypass Validation

After bypassing hooks:

- Ensure CI pipeline validation passes
- Fix pending violations in the next commit
- Avoid repeated bypass usage without valid reason

---

Summary

Bypass should be used only in exceptional situations.

Default expectation is that all commits must pass pre-commit validation before code is pushed.
