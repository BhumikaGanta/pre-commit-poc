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


def has_gradle_build():
    build_files = [
        os.path.join(ROOT, "settings.gradle"),
        os.path.join(ROOT, "settings.gradle.kts"),
        os.path.join(ROOT, "settings.gradle.dcl"),
        os.path.join(ROOT, "build.gradle"),
        os.path.join(ROOT, "build.gradle.kts"),
        os.path.join(ROOT, "build.gradle.dcl"),
    ]
    return any(os.path.exists(path) for path in build_files)


def has_maven_build():
    return os.path.exists(os.path.join(ROOT, "pom.xml"))


def main():
    if not has_java_files():
        print("No Java files found — skipping Checkstyle.")
        return 0

    if not has_gradle_build() and not has_maven_build():
        warning_msg = (
            "WARNING: Java files detected but no Gradle or Maven build config found. "
            "Checkstyle was skipped. Add a build file or wrapper script to enable it."
        )
        print(warning_msg, file=sys.stderr)
        print(warning_msg)
        return 0

    # Prefer Gradle wrapper, then Gradle, then Maven
    gradlew = os.path.join(ROOT, "gradlew")
    gradlew_bat = os.path.join(ROOT, "gradlew.bat")
    if (os.path.exists(gradlew) or os.path.exists(gradlew_bat)) and has_gradle_build():
        # Use wrapper
        cmd = [gradlew if os.path.exists(gradlew) else gradlew_bat, "check"]
        rc = run(cmd)
        if rc == 127:
            # wrapper not runnable -> skip with warning
            warning_msg = (
                "WARNING: Gradle wrapper found but not runnable; skipping Checkstyle."
            )
            print(warning_msg, file=sys.stderr)
            print(warning_msg)
            return 0
        return rc

    if which("gradle") and has_gradle_build():
        rc = run(["gradle", "check"])
        if rc == 127:
            warning_msg = "WARNING: Gradle command returned 127; skipping Checkstyle."
            print(warning_msg, file=sys.stderr)
            print(warning_msg)
            return 0
        return rc

    if which("mvn") and has_maven_build():
        rc = run(["mvn", "checkstyle:check"])
        if rc == 127:
            warning_msg = "WARNING: Maven command returned 127; skipping Checkstyle."
            print(warning_msg, file=sys.stderr)
            print(warning_msg)
            return 0
        return rc

    warning_msg = (
        "WARNING: No build tool could be executed to run Checkstyle. "
        "Install Gradle/Maven or add a wrapper to the repo. Checkstyle was skipped."
    )
    print(warning_msg, file=sys.stderr)
    print(warning_msg)
    return 0


if __name__ == "__main__":
    sys.exit(main())
