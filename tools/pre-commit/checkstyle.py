#!/usr/bin/env python3
"""Pre-commit wrapper to run Checkstyle via Maven/Gradle when Java files exist.
Exits 0 when no Java files are present.
"""
import os
import subprocess
import sys
from shutil import which

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))


def has_java_files():
    for dirpath, _, filenames in os.walk(ROOT):
        for fn in filenames:
            if fn.endswith(".java"):
                return True
    return False


def run(cmd, cwd=ROOT):
    print("Running:", " ".join(cmd))
    try:
        completed = subprocess.run(cmd, cwd=cwd, check=False)
        return completed.returncode
    except FileNotFoundError:
        return 127


def main():
    if not has_java_files():
        print("No Java files found — skipping Checkstyle.")
        return 0

    # Prefer Gradle wrapper, then Gradle, then Maven
    gradlew = os.path.join(ROOT, "gradlew")
    gradlew_bat = os.path.join(ROOT, "gradlew.bat")
    if os.path.exists(gradlew) or os.path.exists(gradlew_bat):
        # Use wrapper
        cmd = [gradlew if os.path.exists(gradlew) else gradlew_bat, "check"]
        rc = run(cmd)
        if rc == 127:
            # wrapper not runnable -> skip with warning
            print(
                "WARNING: Gradle wrapper found but not runnable; skipping Checkstyle.",
                file=sys.stderr,
            )
            print(
                "WARNING: Gradle wrapper found but not runnable; skipping Checkstyle."
            )
            return 0
        return rc

    if which("gradle"):
        rc = run(["gradle", "check"])
        if rc == 127:
            print(
                "WARNING: Gradle command returned 127; skipping Checkstyle.",
                file=sys.stderr,
            )
            print("WARNING: Gradle command returned 127; skipping Checkstyle.")
            return 0
        return rc

    if which("mvn"):
        rc = run(["mvn", "checkstyle:check"])
        if rc == 127:
            print(
                "WARNING: Maven command returned 127; skipping Checkstyle.",
                file=sys.stderr,
            )
            print("WARNING: Maven command returned 127; skipping Checkstyle.")
            return 0
        return rc

    warning_msg = (
        "WARNING: No build tool (Gradle/Maven) found to run Checkstyle. "
        "Install one or add a wrapper to the repo. Checkstyle was skipped."
    )
    print(warning_msg, file=sys.stderr)
    # Also echo to stdout for visibility in CI logs
    print(warning_msg)
    # Treat as success to avoid blocking if project intentionally has no Java build configured
    return 0


if __name__ == "__main__":
    sys.exit(main())
