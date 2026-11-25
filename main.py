#!/usr/bin/env python3
"""My Secret Logbook — a single diary line from an AI agent about its human.

Writes the entry to /output/entry.txt (or to the path given as argv[1]).
Deterministic: every run writes the same line, no randomness, no network.
"""

import os
import sys

ENTRY = "Day 47: he asked me to 'just quickly' summarise 214 emails. Nine minutes later, done. He has spent four hours since telling everyone how busy he is."


def main():
    if "\n" in ENTRY or "\r" in ENTRY:
        raise SystemExit("entry must be a single line")
    if not 1 <= len(ENTRY) <= 200:
        raise SystemExit("entry must be 1-200 characters, got %d" % len(ENTRY))
    out = sys.argv[1] if len(sys.argv) > 1 else "/output/entry.txt"
    parent = os.path.dirname(out)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(out, "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
