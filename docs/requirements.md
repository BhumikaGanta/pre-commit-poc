# Requirements Document

## Purpose

This repository is a proof of concept for a reusable pre-commit quality gate
that can be adopted across multi-language engineering teams. The implementation
focuses on shifting quality checks left, reducing pull request review noise, and
making local developer feedback consistent with CI feedback.

## Scope

The POC covers repository hygiene, formatting, linting, static analysis, secret
scanning, CI enforcement, runtime measurement, and developer enablement
documentation.

## Functional Requirements

<!-- prettier-ignore -->
| ID    | Requirement                                        | Implementation                                                                                     |
| ----- | -------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| FR-01 | Run common repository hygiene checks before commit | `trailing-whitespace`, `end-of-file-fixer`, `check-merge-conflict`, `check-yaml`, and `check-json` |
| FR-02 | Format and validate Python code                    | `black`, `ruff`, and `isort`                                                                       |
| FR-03 | Format and validate JavaScript and TypeScript code | `prettier`, `eslint`, and `tsc --noEmit`                                                           |
| FR-04 | Scan for committed secrets                         | `detect-secrets` with `.secrets.baseline`                                                          |
| FR-05 | Validate Java files                                | Local Checkstyle wrapper through Maven or Gradle when a supported build file is available          |
| FR-06 | Validate C and C++ formatting and static analysis  | `clang-format --dry-run --Werror` and `cppcheck`                                                   |
| FR-07 | Validate C# formatting                             | `dotnet format --verify-no-changes`                                                                |
| FR-08 | Enforce the same checks in CI                      | GitHub Actions workflow runs `pre-commit run --all-files`                                          |
| FR-09 | Support cross-platform validation                  | CI matrix covers Ubuntu, Windows, and macOS                                                        |
| FR-10 | Capture quality gate runtime metrics               | CI writes elapsed runtime and threshold data to the GitHub Actions summary                         |
| FR-11 | Reduce formatting-only PR comments                 | PR template asks authors to confirm local or CI pre-commit execution                               |
| FR-12 | Keep Windows line endings deterministic            | `.gitattributes` pins normalized repository line endings                                           |

## Non-Functional Requirements

<!-- prettier-ignore -->
| ID     | Requirement              | Implementation                                                                  |
| ------ | ------------------------ | ------------------------------------------------------------------------------- |
| NFR-01 | Fast local feedback      | Hooks run locally before commit and on demand with `pre-commit run --all-files` |
| NFR-02 | Reproducible CI behavior | CI installs explicit Python, Node.js, .NET, `clang-format`, and `cppcheck`      |
| NFR-03 | Maintainability          | Hook definitions are centralized in `.pre-commit-config.yaml`                   |
| NFR-04 | Developer usability      | Setup, troubleshooting, quality gates, metrics, and guides live in `docs/`      |
| NFR-05 | Safe failure behavior    | CI fails on hook failure or runtime threshold breach                            |

## Assumptions

- Developers have Python, Git, Node.js, and language-specific SDKs available for the checks they run locally.
- CI is the source of truth for cross-platform validation.
- Optional system tools may need local installation for full parity with CI, especially `clang-format`, `cppcheck`, Maven, Gradle, and the .NET SDK.

## Current Limitations

- The Java Checkstyle hook is best-effort unless the Java project exposes a supported Maven or Gradle check target.
- Windows CI skips `cppcheck` because hosted runner packages can install a broken `std.cfg` lookup path; Linux and macOS still enforce it.
- Secret detection uses a baseline file; teams must review and update the baseline intentionally when known findings change.
