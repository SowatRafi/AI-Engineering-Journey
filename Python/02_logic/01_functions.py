"""
01_functions.py
================

Topic: Functions — defining reusable, named blocks of logic.

WHY THIS MATTERS
----------------
Functions are the primary tool for avoiding repetition (DRY: Don't Repeat
Yourself) and for giving a *name* to an idea. A well-named function turns a
comment into executable, testable code.
"""

# ---------------------------------------------------------------------------
# 1. Defining and calling a function
# ---------------------------------------------------------------------------
# `def` defines it; the parentheses hold parameters; a return sends a value back.
def greet(name: str) -> str:
    """Return a greeting for `name`.

    The triple-quoted string right under the def is the DOCSTRING. It documents
    what the function does and is what help(greet) displays.
    """
    return f"Hello, {name}!"


print(greet("Rafi"))           # calling the function with an argument


# ---------------------------------------------------------------------------
# 2. Parameters: positional, keyword, and defaults
# ---------------------------------------------------------------------------
def make_coffee(size: str, milk: bool = False, shots: int = 1) -> str:
    """Build a coffee order string.

    `milk` and `shots` have DEFAULT values, so they are optional.
    """
    description = f"{size} coffee, {shots} shot(s)"
    if milk:
        description += ", with milk"
    return description


print("\n--- Arguments ---")
print(make_coffee("large"))                     # uses defaults
print(make_coffee("small", True))               # positional args
print(make_coffee("medium", shots=3, milk=True))  # keyword args (order-free, clear)


# ---------------------------------------------------------------------------
# 3. *args and **kwargs: accepting any number of arguments
# ---------------------------------------------------------------------------
# *args collects extra POSITIONAL args into a tuple.
# **kwargs collects extra KEYWORD args into a dict.
def summarize(*args, **kwargs) -> None:
    """Demonstrate variable-length argument collection."""
    print("Positional args (tuple):", args)
    print("Keyword args (dict):", kwargs)


print("\n--- *args / **kwargs ---")
summarize(1, 2, 3, mode="fast", retries=2)


# ---------------------------------------------------------------------------
# 4. Returning multiple values
# ---------------------------------------------------------------------------
# Python returns a tuple, which you can unpack into several names.
def min_and_max(numbers: list[int]) -> tuple[int, int]:
    """Return the smallest and largest values as a (min, max) pair."""
    return min(numbers), max(numbers)


low, high = min_and_max([4, 9, 1, 7])
print("\n--- Multiple returns ---")
print(f"low={low}, high={high}")


# ---------------------------------------------------------------------------
# 5. Pure functions vs. side effects (a clean-code habit)
# ---------------------------------------------------------------------------
# A PURE function's output depends only on its inputs and it changes nothing
# outside itself. Pure functions are easy to test and reason about — prefer them.
def add_tax(price: float, rate: float = 0.1) -> float:
    """Pure: same inputs always give the same output, no external changes."""
    return round(price * (1 + rate), 2)


print("\n--- Pure function ---")
print("Price with tax:", add_tax(100))


# ---------------------------------------------------------------------------
# 6. A common trap: mutable default arguments
# ---------------------------------------------------------------------------
# Default values are created ONCE when the function is defined, not per call.
# Using a mutable default (like []) causes it to be SHARED across calls — a bug.
def bad_append(item, bucket=[]):     # DON'T do this
    bucket.append(item)
    return bucket


def good_append(item, bucket=None):  # DO this instead
    if bucket is None:
        bucket = []                  # a fresh list every call
    bucket.append(item)
    return bucket


if __name__ == "__main__":
    print("\n--- Mutable default trap ---")
    print("bad_append:", bad_append(1), bad_append(2))    # [1] then [1, 2]  <- leaks!
    print("good_append:", good_append(1), good_append(2)) # [1] then [2]     <- correct
    print("\nDone: functions let you name and reuse logic safely.")
