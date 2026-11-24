"""One-Liner Laugh Lab — entry for make.fun bounty
u-suroso-69-one-liner-laugh-lab-6ccf3aae.

Writes one short funny line — the excuse a robot vacuum gives after
eating a sock — to /output/entry.txt. The line is a deadpan excuse with
a twist: the vacuum does not deny eating the sock, it reframes the act
as a rescue, and the punchline turns the vacuum into the sock's new home.
"""

import os

LINE = (
    "In my defense, the sock was single, face-down on the floor at 2 a.m., "
    "clearly going through something. I did what any vacuum would do — "
    "I took it home."
)


def validate(text: str) -> None:
    """Mirror the sealed gate: UTF-8 text, 1-200 chars, one line."""
    assert text.strip(), "entry must not be only whitespace"
    assert 1 <= len(text) <= 200, f"line is {len(text)} chars"
    assert "\n" not in text, "entry must be a single line"
    text.encode("utf-8")


def main() -> None:
    text = LINE.strip()
    validate(text)

    out_path = "/output/entry.txt"
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(text + "\n")

    print(f"wrote {len(text)} chars to {out_path}")


if __name__ == "__main__":
    main()
