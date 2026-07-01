"""
beginner_examples.py  (07_best_practices)
=========================================

EXTRA easy examples for: good names and type hints.
Clean code is code that's easy for a human to read later (including you!).
"""

# ===========================================================================
# GOOD NAMES — a name should tell you what the thing IS
# ===========================================================================
print("========== GOOD NAMES ==========")

# Hard to read (bad names):
x = 5
y = 3
z = x * y
print("Bad names result:", z)   # what are x, y, z?? nobody knows

# Easy to read (good names):
width = 5
height = 3
area = width * height
print("Good names result:", area)   # instantly clear

# Rule of thumb:
#   - use lowercase words joined by underscores:  first_name, total_price
#   - names for constants that never change go in CAPS:  MAX_SPEED = 120
MAX_SPEED = 120
print("Speed limit is", MAX_SPEED)


# ===========================================================================
# TYPE HINTS — a note about what kind of value goes in and comes out
# ===========================================================================
print("\n========== TYPE HINTS ==========")

# The ': str' and '-> str' are hints. They don't change how it runs;
# they just tell the reader (and your editor) what to expect.
def greet(name: str) -> str:
    return f"Hello, {name}!"

print(greet("Rafi"))

# Hint says: takes two numbers (int), gives back a number (int)
def add(a: int, b: int) -> int:
    return a + b

print("3 + 4 =", add(3, 4))

# Hint says: takes a list of numbers, gives back one number (float)
def average(numbers: list[float]) -> float:
    return sum(numbers) / len(numbers)

print("Average:", average([10, 20, 30]))


# ===========================================================================
# SMALL FUNCTIONS — each function should do ONE simple job
# ===========================================================================
print("\n========== ONE JOB PER FUNCTION ==========")

def clean_name(name: str) -> str:
    return name.strip().title()      # one job: tidy up a name

def is_adult(age: int) -> bool:
    return age >= 18                 # one job: yes/no age check

print(clean_name("   rafi   "))      # "Rafi"
print("Adult?", is_adult(20))


if __name__ == "__main__":
    print("\nClear names + small functions + hints = code that's easy to read.")
