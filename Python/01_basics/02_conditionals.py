"""
02_conditionals.py
===================

Topic: Making decisions with if / elif / else, comparison and logical operators.

WHY THIS MATTERS
----------------
Programs need to react to data. Conditionals are how a program chooses one path
over another. Clear conditions are the difference between readable logic and
bug-prone spaghetti.
"""

# ---------------------------------------------------------------------------
# 1. Comparison operators produce booleans
# ---------------------------------------------------------------------------
print("--- Comparisons ---")
print(10 > 5)      # True
print(10 == 10)    # True  (== compares values; = assigns)
print(10 != 3)     # True  (not equal)
print(2 <= 2)      # True


# ---------------------------------------------------------------------------
# 2. if / elif / else
# ---------------------------------------------------------------------------
# Python checks branches top-to-bottom and runs the FIRST one that is True.
# Indentation (4 spaces) defines the block — it is syntactically required.
def grade_for(score: int) -> str:
    """Return a letter grade for a numeric score (0-100)."""
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    else:
        # The catch-all branch when nothing above matched.
        return "F"


print("\n--- if / elif / else ---")
for s in (95, 83, 71, 40):
    print(f"Score {s} -> Grade {grade_for(s)}")


# ---------------------------------------------------------------------------
# 3. Logical operators: and, or, not
# ---------------------------------------------------------------------------
print("\n--- Logical operators ---")
age = 25
has_ticket = True

# `and` -> both sides must be True.  `or` -> at least one.  `not` -> flips it.
if age >= 18 and has_ticket:
    print("Entry allowed.")

if not has_ticket:
    print("This won't print.")
else:
    print("Ticket present.")


# ---------------------------------------------------------------------------
# 4. Truthiness — what counts as True/False
# ---------------------------------------------------------------------------
# Empty containers, 0, None, and "" are "falsy". Everything else is "truthy".
# This lets you write clean checks without comparing to len() or None explicitly.
print("\n--- Truthiness ---")
items = []
if items:                     # cleaner than: if len(items) > 0
    print("Cart has items.")
else:
    print("Cart is empty (empty list is falsy).")

name = ""
print("Name provided." if name else "Name is missing (empty string is falsy).")


# ---------------------------------------------------------------------------
# 5. The ternary (conditional) expression
# ---------------------------------------------------------------------------
# A compact one-line if/else that RETURNS a value.
temperature = 30
label = "hot" if temperature > 25 else "cool"
print(f"\nIt is {label} today.")


if __name__ == "__main__":
    print("\nDone: you can now branch logic based on data.")
