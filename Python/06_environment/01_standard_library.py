"""
01_standard_library.py
=====================

Topic: The standard library — Python's "batteries included" toolbox.

WHY THIS MATTERS
----------------
Before reaching for a third-party package, check the standard library — it ships
with Python and covers an enormous amount: math, dates, randomness, JSON, files,
counting, and more. Using it well means less code to write and maintain.
"""

# Modules are imported at the TOP of a file by convention.
import math
import random
import json
import datetime as dt
from collections import Counter, defaultdict
from pathlib import Path


# ---------------------------------------------------------------------------
# 1. math — numeric helpers
# ---------------------------------------------------------------------------
print("--- math ---")
print("sqrt(81):", math.sqrt(81))
print("factorial(5):", math.factorial(5))
print("ceil/floor of 4.3:", math.ceil(4.3), math.floor(4.3))
print("pi:", round(math.pi, 4))


# ---------------------------------------------------------------------------
# 2. random — randomness (seed it for reproducible results)
# ---------------------------------------------------------------------------
print("\n--- random ---")
random.seed(42)                  # fixed seed => same "random" output every run
print("randint(1, 6):", random.randint(1, 6))
print("choice:", random.choice(["rock", "paper", "scissors"]))
print("sample 3 of 10:", random.sample(range(10), 3))


# ---------------------------------------------------------------------------
# 3. datetime — dates and times
# ---------------------------------------------------------------------------
print("\n--- datetime ---")
today = dt.date.today()
print("Today:", today)
print("In 30 days:", today + dt.timedelta(days=30))
now = dt.datetime.now()
print("Formatted:", now.strftime("%Y-%m-%d %H:%M"))


# ---------------------------------------------------------------------------
# 4. json — serialize/deserialize (the language of web APIs)
# ---------------------------------------------------------------------------
print("\n--- json ---")
payload = {"model": "claude", "temperature": 0.2, "tools": ["search"]}
text = json.dumps(payload)                 # Python dict -> JSON string
print("dumps:", text)
restored = json.loads(text)                # JSON string -> Python dict
print("loads keeps type:", type(restored).__name__, restored["temperature"])


# ---------------------------------------------------------------------------
# 5. collections — specialised containers
# ---------------------------------------------------------------------------
print("\n--- collections ---")
# Counter: tally occurrences in one line.
votes = ["yes", "no", "yes", "yes", "no"]
print("Counter:", Counter(votes))
print("Most common:", Counter(votes).most_common(1))

# defaultdict: supplies a default value for missing keys (no KeyError).
groups = defaultdict(list)                  # missing key -> a new empty list
for name in ["Ann", "Bob", "Amy"]:
    groups[name[0]].append(name)            # group by first letter
print("defaultdict grouping:", dict(groups))


# ---------------------------------------------------------------------------
# 6. pathlib — filesystem paths done right (already used in file I/O)
# ---------------------------------------------------------------------------
print("\n--- pathlib ---")
here = Path(__file__)
print("This file name:", here.name)
print("Its folder:", here.parent.name)
print("Suffix:", here.suffix)


if __name__ == "__main__":
    print("\nDone: check the standard library first — it's already installed.")
