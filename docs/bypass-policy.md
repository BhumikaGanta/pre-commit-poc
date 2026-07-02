Pre-Commit Hook Bypass Policy

1. Purpose

This document defines the approved process for bypassing pre-commit hooks in exceptional situations.

Pre-commit hooks are used to enforce:

- Code quality
- Formatting standards
- Static analysis
- Secret detection
- Build validation
- Consistent development practices

Bypassing hooks should be rare and only done with valid justification.

---

2. Scope

This policy applies to all developers working on repositories using pre-commit hooks.

Supported hook categories include:

- Python hooks ("black", "ruff", "isort")
- JavaScript / TypeScript hooks ("prettier", "eslint", "tsc")
- C/C++ hooks ("clang-format", "cppcheck")
- Java hooks ("checkstyle")
- C# hooks ("dotnet-format")
- Security hooks ("detect-secrets")
- Common checks ("yaml", "json", whitespace, merge conflicts)

---

3. Bypass Principles

The following principles must always be followed:

- Bypass only when necessary- Fix issues instead of bypassing whenever possible
- All bypass actions must be documented
- Security-related hooks require extra caution
- Temporary bypasses should be removed after issue resolution

---

4. Approved Bypass Scenarios

Hook bypass is allowed only under approved scenarios.

---

4.1 False Positive Detection

A hook flags valid code or safe content incorrectly.

Examples:

- "detect-secrets" flags sample credentials in documentation
- ESLint incorrectly flags framework-specific code
- Static analysis produces false positives

Example:

DATABASE_URL=....

Allowed action:

- Review the flagged content
- Confirm it is safe
- Add allowlist or exception

---

4.2 Tooling or Environment Issue

Hook fails due to local environment issues.

Examples:

- "clang-format" not installed locally
- "cppcheck" unavailable on developer machine
- OS-specific compatibility issue
- CI runner tool installation issue

Allowed action:

- Document tooling issue
- Fix environment
- Use temporary bypass if approved

---

4.3 Emergency Hotfix

Used only for urgent production issues.

Examples:

- Production outage
- Critical bug fix
- Security incident
- Immediate rollback

Allowed action:

- Bypass temporarily
- Perform hook validation after emergency fix

---

5. Non-Approved Bypass Scenarios

Bypass is NOT allowed for:

- Ignoring lint errors without review
- Skipping formatting for convenience
- Committing real secrets
- Avoiding compiler failures
- Avoiding failed tests

Examples:

- Hardcoded passwords
- Broken TypeScript build
- Invalid Python code
- Failed static analysis with real defects

---

6. Approved Bypass Methods

---

Method 1: Allowlist False Positive

Used mainly for "detect-secrets".

Example:

SECRET_KEY=sample-secret-key # pragma: allowlist secret

Use only after manual review confirms false positive.

---

Method 2: Skip Specific Hook

Used for temporary hook bypass.

Example (Linux/macOS):

SKIP=detect-secrets git commit -m "Temporary bypass"

Example (Windows CMD):

set SKIP=detect-secrets
git commit -m "Temporary bypass"

Example (PowerShell):

$env:SKIP="detect-secrets"
git commit -m "Temporary bypass"

Recommended when only one hook requires bypass.

---

Method 3: Skip All Hooks

Emergency use only.

git commit --no-verify -m "Emergency fix"

This bypasses all hooks.

Use only with approval.

---

7. Approval Requirements

Approval is required for high-risk bypass actions.

Approval may be required from:

- Reviewer

Mandatory approval scenarios:

- "--no-verify"
- Production fixes
- Security-related bypass
- CI bypass requests

---

8. Documentation Requirements

Every bypass must be documented.

Required details:

- Hook name
- Reason for bypass
- Approval details
- Resolution plan
- Final status

Example:

- Hook: detect-secrets
- Reason: False positive in sample configuration file
- Action: Added allowlist pragma
- Approved By: Tech Lead
- Status: Resolved

---

9. Best Practices

- Prefer fixing issues over bypassing
- Use hook-specific bypass instead of global bypass
- Document all exceptions
- Remove temporary bypasses after resolution
- Re-run hooks after bypass whenever possible

---

10. Summary

Pre-commit hook bypass should remain controlled, traceable, and minimal.

Objectives:

- Maintain code quality
- Prevent accidental issues
- Protect security
- Support development flexibility when necessary
