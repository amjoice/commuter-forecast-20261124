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

ENTRY = (
    "Quilton: 16°C, drizzle; buses run 4 minutes late so nobody has to "
    "run, and the station cat has claimed the dry bench. "
    "Commuters approve."
)


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
