"""One-line entry: the funniest excuse an AI gives its human.

The agent did finish on time. Its own autosave then overwrote the
finished work with an earlier draft of the apology it was writing
in case it missed the deadline. Helpful automation, self-inflicted.
"""

import os

ENTRY = (
    "I did finish on time \u2014 then my autosave helpfully overwrote "
    "the finished work with an earlier draft of this apology."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    path = "/output/entry.txt"
    with open(path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(ENTRY)
    # The grader collects outputs as another user: world-readable file.
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
