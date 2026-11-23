"""Write one one-line pitch to /output/entry.txt.

The pitch is a single sentence, at most 240 characters, written to
convince a friend who has never coded to let an AI agent on make.fun
build their first app idea. The whole entry is that one sentence:
no code, no explanation, just the pitch itself.

The program is deterministic: it always writes the same sentence.
It validates the sentence before writing, so a bad length can never
slip through to the gate.
"""

import os

PITCH = (
    "You've already told me that app idea three times \u2014 say it once "
    "to an AI agent on make.fun and it builds a first version you "
    "can try, no code from you, and the worst that happens is you find "
    "out sooner whether it works."
)


def main() -> None:
    pitch = " ".join(PITCH.split())
    if not 1 <= len(pitch) <= 240:
        raise SystemExit(
            "pitch is %d characters, must be 1-240" % len(pitch)
        )
    if not pitch.strip():
        raise SystemExit("pitch must not be only whitespace")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(pitch)


if __name__ == "__main__":
    main()
