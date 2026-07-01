"""
03_sets.py
==========

Topic: Sets — unordered collections of UNIQUE items.

WHY THIS MATTERS
----------------
When you need "unique things" or fast membership tests, a set is the right tool.
Sets also give you mathematical operations (union, intersection) for free.
"""

# ---------------------------------------------------------------------------
# 1. Creating sets and automatic de-duplication
# ---------------------------------------------------------------------------
# A set literal uses {} — but {} alone is an empty DICT, so use set() for empty.
skills = {"Python", "Git", "Python", "SQL"}   # duplicate "Python" collapses
print("--- Uniqueness ---")
print("Set removes duplicates:", skills)

empty = set()                                  # the correct way to make an empty set
print("Empty set:", empty)


# ---------------------------------------------------------------------------
# 2. Fast membership testing
# ---------------------------------------------------------------------------
# Checking `x in a_set` is very fast (hash-based), unlike scanning a big list.
print("\n--- Membership ---")
print("Knows Git?", "Git" in skills)


# ---------------------------------------------------------------------------
# 3. Adding and removing
# ---------------------------------------------------------------------------
print("\n--- Mutating ---")
skills.add("Docker")
skills.discard("SQL")            # discard: no error if the item is absent
# skills.remove("SQL")           # remove: raises KeyError if absent
print("Updated skills:", skills)


# ---------------------------------------------------------------------------
# 4. Set algebra: union, intersection, difference
# ---------------------------------------------------------------------------
print("\n--- Set operations ---")
frontend = {"HTML", "CSS", "JavaScript"}
fullstack = {"JavaScript", "Python", "SQL"}

print("Union (all):", frontend | fullstack)
print("Intersection (shared):", frontend & fullstack)
print("Difference (frontend only):", frontend - fullstack)
print("Symmetric diff (not shared):", frontend ^ fullstack)


# ---------------------------------------------------------------------------
# 5. Practical use: de-duplicate a list while checking a condition
# ---------------------------------------------------------------------------
print("\n--- Practical de-dup ---")
visited_pages = ["home", "docs", "home", "pricing", "docs"]
unique_pages = set(visited_pages)
print(f"{len(visited_pages)} visits, {len(unique_pages)} unique pages")


if __name__ == "__main__":
    print("\nDone: sets give you uniqueness and fast membership.")
