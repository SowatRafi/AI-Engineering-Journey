"""
beginner_examples.py  (04_reliability)
======================================

EXTRA easy examples for: error handling (try/except) and simple debugging.
Errors are normal! The goal is to handle them calmly instead of crashing.
"""

# ===========================================================================
# TRY / EXCEPT — try something risky, and have a backup plan if it fails
# ===========================================================================
print("========== TRY / EXCEPT ==========")

# Example 1: dividing by zero would crash — so we catch it
try:
    answer = 10 / 0
except ZeroDivisionError:
    print("Oops, you can't divide by zero. Using 0 instead.")
    answer = 0
print("Answer:", answer)


# Example 2: turning text into a number might fail
def to_number(text):
    try:
        return int(text)
    except ValueError:
        print(f"'{text}' is not a number. Using 0.")
        return 0

print(to_number("42"))     # works -> 42
print(to_number("cat"))    # fails safely -> 0


# Example 3: a missing dictionary key
menu = {"tea": 2, "coffee": 3}
try:
    print("Juice costs:", menu["juice"])
except KeyError:
    print("Sorry, we don't sell juice.")


# Example 4: keep asking-style logic without crashing
def safe_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "cannot divide by zero"

print("10 / 2 =", safe_divide(10, 2))
print("10 / 0 =", safe_divide(10, 0))


# ===========================================================================
# FINALLY — code that ALWAYS runs (good for "cleanup")
# ===========================================================================
print("\n========== FINALLY ==========")

def open_box(has_key):
    try:
        if not has_key:
            raise ValueError("No key!")
        print("Box opened!")
    except ValueError as problem:
        print("Could not open:", problem)
    finally:
        print("(You walked away from the box either way.)")

open_box(True)
open_box(False)


# ===========================================================================
# SIMPLE DEBUGGING — print things to see what's happening
# ===========================================================================
print("\n========== SIMPLE DEBUGGING ==========")

def total_price(prices):
    # When something looks wrong, print the values to inspect them.
    print("  [debug] prices received:", prices)
    total = sum(prices)
    print("  [debug] total is:", total)
    return total

print("Final total:", total_price([2, 3, 5]))


if __name__ == "__main__":
    print("\nHandling errors keeps your program running instead of crashing.")
