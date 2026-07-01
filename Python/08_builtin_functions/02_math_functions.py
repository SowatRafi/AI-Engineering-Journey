"""
02_math_functions.py
====================

Built-in functions for everyday math (no 'import math' needed).

Covers: abs, divmod, pow, round, sum, min, max

WHY THIS MATTERS
----------------
These handle common number tasks in one short, clear call — adding up a list,
finding the smallest/largest, rounding money, and more.
"""

# ---------------------------------------------------------------------------
# abs() — the distance from zero (always positive)
# ---------------------------------------------------------------------------
print("--- abs ---")
print(abs(-7))          # 7
print(abs(7))           # 7
# Example: how far apart are two temperatures, no matter which is bigger?
print(abs(18 - 25))     # 7


# ---------------------------------------------------------------------------
# round() — round a decimal number
# ---------------------------------------------------------------------------
print("\n--- round ---")
print(round(3.14159, 2))    # 3.14  (keep 2 decimal places)
print(round(7.8))           # 8     (round to a whole number)
# Example: a shopping total rounded to cents.
print(round(19.99 + 5.5, 2))    # 25.49


# ---------------------------------------------------------------------------
# pow() — raise a number to a power
# ---------------------------------------------------------------------------
print("\n--- pow ---")
print(pow(2, 3))        # 8   (2 * 2 * 2, the same as 2 ** 3)
print(pow(5, 2))        # 25


# ---------------------------------------------------------------------------
# divmod() — get the quotient AND the remainder at once
# ---------------------------------------------------------------------------
print("\n--- divmod ---")
print(divmod(17, 5))    # (3, 2)  because 17 = 3*5 + 2

# Example: turn 130 seconds into minutes and seconds.
minutes, seconds = divmod(130, 60)
print(minutes, "min", seconds, "sec")   # 2 min 10 sec


# ---------------------------------------------------------------------------
# sum(), min(), max() — work on a whole list at once
# ---------------------------------------------------------------------------
print("\n--- sum / min / max ---")
prices = [4.99, 12.50, 3.25]
print("Total:", round(sum(prices), 2))  # 20.74
print("Cheapest:", min(prices))         # 3.25
print("Most expensive:", max(prices))   # 12.5

# min() and max() also work on separate values:
print(min(9, 2, 7))     # 2
print(max(9, 2, 7))     # 9


# ---------------------------------------------------------------------------
# min()/max() with 'key' — find the "best" by a rule
# ---------------------------------------------------------------------------
print("\n--- max with a rule ---")
words = ["cat", "elephant", "dog"]
# 'key=len' means: compare the words by their length. So this finds the longest.
print(max(words, key=len))      # elephant


if __name__ == "__main__":
    print("\nDone: these replace many small math loops with one clear call.")
