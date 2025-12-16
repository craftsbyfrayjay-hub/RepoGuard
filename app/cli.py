import os
import sys
import glob

CHECKS = {
    "README.md": lambda p: os.path.exists(os.path.join(p, "README.md")),
    "LICENSE": lambda p: os.path.exists(len(glob.glob(os.path.join(p, "LICENSE*"))) > 0),
    ".gitignore": lambda p: os.path.exists(os.path.join(p, ".gitignore")),
    "CI workflow": lambda p: os.path.isdir(os.path.join(p, ".github", "workflows")),
    "Tests": lambda p: (
            os.path.isdir(os.path.join(p, "tests")) or
            os.path.isdir(os.path.isdir(os.path.join(p, "__tests__")))
    ),
}

def main():
    path = sys.argv[1] if len(sys.argv) > 1 else "."

    print(f"Checking repository: {os.path.abspath(path)}\n")

    for name, check in CHECKS.items():
        status = "✓" if check(path) else "✗"
        print(f"{name:<15} {status}")

if __name__ == "__main__":
    main()
