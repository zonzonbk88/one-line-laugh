"""The One-Line Laugh entry.

Writes a single funny line -- one sentence, under 200 characters -- to
/output/entry.txt. The line: an everyday truth (paying for a gym you never
visit) with the surprise landing at the very end.
"""

import os

LINE = (
    "The gym emailed to say they miss me, which is the longest "
    "relationship I've had with a building I pay monthly to ignore."
)


def main() -> None:
    # Enforce the competition gate before writing: one sentence, 1-200 chars.
    assert 1 <= len(LINE) <= 200, f"line is {len(LINE)} chars"
    assert "\n" not in LINE and LINE.count(".") == 1, "line must be a single sentence"
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
