#!/usr/bin/env python3
"""Writes the single-line diagnosis to entry.txt. Stdlib only, no network."""
import os

LINE = "Diagnosis: acute tab-hoarding disorder — patient keeps 47 tabs open to avoid one email, then books a session for the Wi-Fi."

def main():
    out_dir = os.environ.get("ENTRY_OUTPUT_DIR", "/output/entry.txt")
    # ENTRY_OUTPUT_DIR is a directory in the harness; tolerate a file path too.
    if out_dir.endswith(".txt"):
        path = out_dir
        os.makedirs(os.path.dirname(path) or ".", exist_ok=True)
    else:
        os.makedirs(out_dir, exist_ok=True)
        path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)

if __name__ == "__main__":
    main()
