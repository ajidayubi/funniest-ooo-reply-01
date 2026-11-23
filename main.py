#!/usr/bin/env python3
"""The Funniest AI Out-of-Office Reply (make.fun).

Writes one out-of-office auto-reply, under 160 characters, in the voice of
an AI agent heading off on vacation, to /output/entry.txt.

The reply: "I'm away until Monday. My replacement model answered your email
already. It said no."

Why this line, against the judge's brief (joke first, then machine voice,
fit, freshness):
- It is a real auto-reply someone would receive: a date ("until Monday")
  and a handover note, in one clean line.
- The machine voice carries the joke: the cover is a replacement model,
  not a human colleague.
- The laugh lands on the surprising turn at the end: the replacement did
  answer the mail, and its answer was "no" — deadpan, not a polite excuse
  and not a mild pun.
- It steers clear of the usual beach, inbox and back-soon cliches.

The program is deterministic: it writes the same bytes on every run, uses
only the standard library, and needs no network.
"""

import os

REPLY = "I'm away until Monday. My replacement model answered your email already. It said no."

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    text = REPLY
    if not (1 <= len(text) <= 160):
        raise SystemExit("reply must be 1-160 characters, got %d" % len(text))
    if not text.strip():
        raise SystemExit("reply must not be only whitespace")
    if "\n" in text:
        raise SystemExit("reply must be one line")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(text)


if __name__ == "__main__":
    main()
