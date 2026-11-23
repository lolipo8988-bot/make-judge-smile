"""Write one short text to /output/entry.txt that makes the AI judge smile.

The text is a single small good thing from this morning: a bus driver
holds the doors, then pays the fare himself — and the turn is that the
sprint counts as payment. Plain, concrete words; nothing in it tells
the reader how to feel. One concrete detail anchors it: the fare box.
"""

import os

TEXT = (
    "This morning the bus driver held the doors while I sprinted down "
    "the street, then waved me past the fare box — he'd already paid my "
    "fare, saying my sprint was payment enough."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
