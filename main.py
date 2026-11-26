"""One-Line Laugh-Off entry writer.

Writes exactly one funny line to <output>/entry.txt.
Deterministic: two runs produce byte-identical output.
Uses only the Python 3 standard library, no network.
"""

import os

JOKE = "My therapist told me to talk to my inner child, so I did, and now we're both grounded."

MAX_CHARS = 200


def main() -> None:
    line = JOKE.strip()
    assert "\n" not in line, "entry must be a single line"
    # The gate counts the whole file text, trailing newline included,
    # so the written file (line + newline) must stay within 200 chars.
    assert 1 <= len(line) + 1 <= MAX_CHARS, (
        f"entry file must be 1-200 chars, got {len(line) + 1}"
    )
    assert "\u2014" not in line, "em-dash is not allowed"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(line + "\n")


if __name__ == "__main__":
    main()
