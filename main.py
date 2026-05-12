import sys

types = ["feat", "fix", "docs", "refactor", "chore"]
scopes = ["api", "auth", "ui", "db", "core", "utils"]

if __name__ == "__main__":
    desc = " ".join(sys.argv[1:]) if len(sys.argv) > 1 else "update"
    print("suggested commits:")
    for t in types:
        import random
        scope = random.choice(scopes)
        print(f"  {t}({scope}): {desc}")
# updated
