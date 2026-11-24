#!/usr/bin/env python3
"""Charm the Commuter: Forecast a City That Isn't.

Writes one line of weather (at most 140 characters) for the fictional
city of Quilton to /output/entry.txt.

Quilton is a city that does not exist: its buses run four minutes late
on purpose, so nobody has to run for them, and the station cat has
claimed the only dry bench. The forecast keeps the register of a real
broadcast forecast -- place, temperature, weather -- bent just enough
to make a bored commuter smile.
"""

import os
import sys

MAX_CHARS = 140
OUTPUT_PATH = "/output/entry.txt"

PLACE = "Quilton"
TEMPERATURE = "16°C"
WEATHER = "drizzle"


def build_entry():
    """Compose the forecast line from its parts."""
    headline = f"{PLACE}: {TEMPERATURE}, {WEATHER};"
    quirk = "buses run 4 minutes late so nobody sprints"
    coda = "the station cat owns the dry bench."
    verdict = "Commuters approve."
    return " ".join([headline, quirk + ",", coda, verdict])


def validate(entry):
    """Check the entry is a single line within the char limit."""
    if "\n" in entry or "\r" in entry:
        raise ValueError("entry must be a single line")
    if not entry:
        raise ValueError("entry must not be empty")
    if len(entry) > MAX_CHARS:
        raise ValueError(
            f"entry is {len(entry)} chars, over the {MAX_CHARS} limit"
        )
    return entry


def write_entry(entry):
    """Write the validated entry to the output file."""
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(entry)


def main():
    entry = validate(build_entry())
    write_entry(entry)
    print(entry)


if __name__ == "__main__":
    main()
