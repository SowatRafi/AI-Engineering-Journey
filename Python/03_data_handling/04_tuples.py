"""
04_tuples.py
============

Topic: Tuples — ordered, IMMUTABLE sequences.

WHY THIS MATTERS
----------------
A tuple is like a list that cannot change. Immutability signals intent ("these
values belong together and won't change") and makes tuples usable as dict keys
and set members, which lists cannot be.
"""

# ---------------------------------------------------------------------------
# 1. Creating tuples
# ---------------------------------------------------------------------------
point = (3, 4)                   # parentheses are conventional
rgb = 255, 128, 0                # they are optional — the commas make the tuple
single = (42,)                   # a one-element tuple NEEDS the trailing comma
not_a_tuple = (42)               # this is just the int 42!

print("--- Creation ---")
print("point:", point, "| rgb:", rgb)
print("single is tuple:", isinstance(single, tuple))
print("not_a_tuple is int:", isinstance(not_a_tuple, int))


# ---------------------------------------------------------------------------
# 2. Immutability — you cannot change a tuple in place
# ---------------------------------------------------------------------------
print("\n--- Immutability ---")
try:
    point[0] = 99                # attempting to mutate raises TypeError
except TypeError as error:
    print("Cannot mutate tuple:", error)


# ---------------------------------------------------------------------------
# 3. Unpacking — a favourite Python idiom
# ---------------------------------------------------------------------------
print("\n--- Unpacking ---")
x, y = point                     # assign each element to a name
print(f"x={x}, y={y}")

# Swap two variables with no temp variable — powered by tuple packing/unpacking.
a, b = 1, 2
a, b = b, a
print("Swapped:", a, b)

# The star target captures "the rest".
first, *middle, last = (10, 20, 30, 40, 50)
print("first:", first, "| middle:", middle, "| last:", last)


# ---------------------------------------------------------------------------
# 4. Why immutability is useful: tuples as dict keys
# ---------------------------------------------------------------------------
print("\n--- Tuple as key ---")
# A grid/coordinate lookup — a list could NOT be used as a key here.
grid = {(0, 0): "start", (1, 2): "treasure"}
print("At (1, 2):", grid[(1, 2)])


# ---------------------------------------------------------------------------
# 5. Returning multiple values is really returning a tuple
# ---------------------------------------------------------------------------
def divide(a: int, b: int) -> tuple[int, int]:
    """Return (quotient, remainder) — a tuple."""
    return a // b, a % b


if __name__ == "__main__":
    q, r = divide(17, 5)
    print("\n17 / 5 ->", f"quotient={q}, remainder={r}")
    print("Done: tuples are fixed, safe, hashable sequences.")
