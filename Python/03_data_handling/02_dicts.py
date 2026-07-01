"""
02_dicts.py
===========

Topic: Dictionaries — key -> value mappings.

WHY THIS MATTERS
----------------
Dictionaries store labelled data and give near-instant lookup by key. They are
everywhere in AI engineering: JSON payloads, API responses, config, and model
parameters are all dict-shaped.
"""

# ---------------------------------------------------------------------------
# 1. Creating and accessing
# ---------------------------------------------------------------------------
engineer = {
    "name": "Rafi",
    "phase": 1,
    "skills": ["Python", "Git"],
}

print("--- Access ---")
print("Name:", engineer["name"])       # direct access — KeyError if missing
print("Phase:", engineer.get("phase"))  # .get() returns None if missing (safe)
print("Salary:", engineer.get("salary", "unknown"))  # supply a default


# ---------------------------------------------------------------------------
# 2. Adding, updating, removing
# ---------------------------------------------------------------------------
print("\n--- Mutating ---")
engineer["location"] = "Dhaka"          # add a new key
engineer["phase"] = 2                    # update an existing key
engineer.update({"level": "junior"})     # merge in another dict
removed = engineer.pop("location")        # remove & return a value
print("After edits:", engineer)
print("Removed:", removed)


# ---------------------------------------------------------------------------
# 3. Iterating: keys, values, items
# ---------------------------------------------------------------------------
print("\n--- Iterating ---")
for key in engineer:                     # iterating a dict yields its KEYS
    print("key:", key)

for key, value in engineer.items():      # .items() yields (key, value) pairs
    print(f"{key} = {value}")


# ---------------------------------------------------------------------------
# 4. Safe key checks and counting pattern
# ---------------------------------------------------------------------------
print("\n--- Membership & counting ---")
print("Has 'name'?", "name" in engineer)   # checks KEYS

# A classic use: tallying occurrences.
text = "banana"
counts: dict[str, int] = {}
for char in text:
    counts[char] = counts.get(char, 0) + 1  # default 0, then increment
print("Letter counts:", counts)              # {'b': 1, 'a': 3, 'n': 2}


# ---------------------------------------------------------------------------
# 5. Nested dictionaries (JSON-like data)
# ---------------------------------------------------------------------------
print("\n--- Nested ---")
config = {
    "model": {"name": "claude", "temperature": 0.2},
    "retries": 3,
}
print("Nested access:", config["model"]["temperature"])


if __name__ == "__main__":
    print("\nDone: dicts map keys to values with fast lookup.")
