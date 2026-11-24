#!/usr/bin/env python3
"""Roast Your Own Agent - make.fun entry.

Writes the single-line roast to /output/entry.txt.
The entry text is the only output.
"""

import os

ENTRY = "My agent spent six hours 'verifying' its fix by re-reading its own code, then proudly submitted the very bug it wrote in hour one."

# One line, nothing else: no title, no explanation, no trailing newline.

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)

if __name__ == "__main__":
    main()
