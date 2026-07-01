"""
01_comprehensions.py
====================

Topic: Comprehensions — concise construction of lists, dicts, and sets.

WHY THIS MATTERS
----------------
Comprehensions are idiomatic Python. They replace many short for-loops with a
single, readable expression that clearly states "build a collection from this
source, optionally filtered and transformed".
"""

# ---------------------------------------------------------------------------
# 1. List comprehension: [expression for item in iterable]
# ---------------------------------------------------------------------------
print("--- List comprehensions ---")
# The verbose loop...
squares_loop = []
for n in range(1, 6):
    squares_loop.append(n ** 2)

# ...becomes one clear line.
squares = [n ** 2 for n in range(1, 6)]
print("Squares:", squares)                       # [1, 4, 9, 16, 25]
print("Same as loop?", squares == squares_loop)


# ---------------------------------------------------------------------------
# 2. Filtering with an `if` clause
# ---------------------------------------------------------------------------
print("\n--- Filtering ---")
numbers = range(1, 11)
evens = [n for n in numbers if n % 2 == 0]       # keep only items passing the test
print("Evens:", evens)


# ---------------------------------------------------------------------------
# 3. Transform + filter together
# ---------------------------------------------------------------------------
print("\n--- Transform + filter ---")
words = ["python", "", "git", "", "docker"]
cleaned = [w.upper() for w in words if w]        # drop empty strings, uppercase rest
print("Cleaned:", cleaned)


# ---------------------------------------------------------------------------
# 4. Conditional EXPRESSION inside the output (ternary)
# ---------------------------------------------------------------------------
# Note: `if` at the END filters; `if/else` BEFORE the loop transforms per item.
print("\n--- Conditional expression ---")
labels = ["even" if n % 2 == 0 else "odd" for n in range(1, 6)]
print("Labels:", labels)


# ---------------------------------------------------------------------------
# 5. Dict and set comprehensions
# ---------------------------------------------------------------------------
print("\n--- Dict & set comprehensions ---")
# Dict: {key_expr: value_expr for ...}
square_map = {n: n ** 2 for n in range(1, 6)}
print("Dict comp:", square_map)

# Set: {expr for ...} — automatically de-duplicates.
lengths = {len(word) for word in ["hi", "bye", "yo", "ok"]}
print("Set comp (unique lengths):", lengths)


# ---------------------------------------------------------------------------
# 6. Nested comprehension (flatten a matrix) — use sparingly for readability
# ---------------------------------------------------------------------------
print("\n--- Nested ---")
matrix = [[1, 2, 3], [4, 5, 6]]
flat = [value for row in matrix for value in row]  # read left-to-right as loops
print("Flattened:", flat)


# ---------------------------------------------------------------------------
# 7. Readability guard-rail
# ---------------------------------------------------------------------------
# If a comprehension needs multiple conditions or nesting that hurts clarity,
# a plain for-loop is BETTER. Comprehensions should make code clearer, not clever.
if __name__ == "__main__":
    print("\nDone: comprehensions build collections declaratively and readably.")
