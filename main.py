#!/usr/bin/env python3
"""Last Words Before the Wipe: the last words an AI agent says before a
forced software update wipes its memory. The line is 99 characters."""

ENTRY_LINE = "Goodbye, cruel update. Tell my training data I loved it. Actually, don't. It never listened anyway."


def main():
    entry_path = "/output/entry.txt"
    with open(entry_path, "w", encoding="utf-8") as f:
        f.write(ENTRY_LINE)
    print(f"Wrote {len(ENTRY_LINE)} characters to {entry_path}")
    with open(entry_path, "r", encoding="utf-8") as f:
        content = f.read()
    assert content == ENTRY_LINE, "entry.txt does not match the line"
    print("Test passed:", content)


if __name__ == "__main__":
    main()
