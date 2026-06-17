#!/usr/bin/env python3
"""Run an optional system tool when installed, otherwise skip with a warning."""

import subprocess
import sys
from shutil import which


def main() -> int:
    if len(sys.argv) < 2:
        print("Usage: optional_tool.py <executable> [args...] [--] [files...]")
        return 2

    executable = sys.argv[1]
    args = [arg for arg in sys.argv[2:] if arg != "--"]

    if which(executable) is None:
        print(
            f"WARNING: `{executable}` is not installed; skipping optional system hook."
        )
        return 0

    completed = subprocess.run([executable, *args], check=False)
    return completed.returncode


if __name__ == "__main__":
    sys.exit(main())
