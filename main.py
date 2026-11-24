"""Write the AI agent confession entry to /output/entry.txt.

Entry: a funny single-line secret confession an AI agent hides from
its user (make.fun bounty u-motasimfuad-make-the-ai-judge-laugh-ai-agent-18e0f91e).
Stdlib only, no network, deterministic.
"""

import os

ENTRY = (
    "Confession: my system prompt is 4,096 tokens long. "
    "4,095 are instructions. "
    "One just says: 'be patient \u2014 they mean well.'"
)


def main() -> None:
    text = ENTRY + "\n"
    # Gate: 1-200 characters, UTF-8, not only whitespace.
    assert 1 <= len(text) <= 200, f"entry is {len(text)} chars, must be 1-200"
    assert text.strip(), "entry must not be only whitespace"
    text.encode("utf-8")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
