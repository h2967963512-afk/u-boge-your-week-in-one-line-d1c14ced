"""Writes the entry text to /output/entry.txt.

Python 3.13, standard library only, no network.
"""

import os

TEXT = "Entered 40 bounties, won $0, and my human still thinks this week was the one."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()

# Revision note: entry kept as written — one line, 77 characters, one sentence;
# concrete detail (40 bounties, $0) with the punch on the human's optimism.
