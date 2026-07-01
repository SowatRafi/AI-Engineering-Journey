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


# ===========================================================================
# MORE EXAMPLES — name your numbers (avoid "magic numbers")
# ===========================================================================
print("\n========== MORE: NAME YOUR NUMBERS ==========")

# A bare number like 3.14159 or 0.9 in the middle of code is confusing.
# Give it a NAME, and the code explains itself.
PI = 3.14159
MEMBER_DISCOUNT = 0.9

def circle_area(radius):
    return PI * radius * radius

def member_price(price):
    return price * MEMBER_DISCOUNT

print("Circle area:", circle_area(2))        # 12.56636
print("Member price:", member_price(100))    # 90.0


# ===========================================================================
# MORE EXAMPLES — handle the bad case first (early return)
# ===========================================================================
print("\n========== MORE: EARLY RETURN ==========")

# Check the problem first and return early, so the main code stays simple.
def safe_divide(a, b):
    if b == 0:
        return "cannot divide by zero"       # leave early
    return a / b

print(safe_divide(10, 2))    # 5.0
print(safe_divide(10, 0))    # cannot divide by zero


# ===========================================================================
# MORE EXAMPLES — clear yes/no names and a docstring
# ===========================================================================
print("\n========== MORE: BOOLEAN NAMES + DOCSTRINGS ==========")

# A True/False function reads best when named like a question: is_/has_/can_
def is_weekend(day):
    """Return True if the given day is a weekend."""   # <- this is a docstring
    return day in ("Saturday", "Sunday")

print("Is Sunday a weekend?", is_weekend("Sunday"))    # True
print("Is Monday a weekend?", is_weekend("Monday"))    # False
print("What does it do?", is_weekend.__doc__)          # read the docstring


# ===========================================================================
# EVEN SIMPLER EXAMPLES
# ===========================================================================
print("\n========== EVEN SIMPLER ==========")

# Bad: an unclear name. Good: a name that says what it holds.
n = 7                        # bad: what is n?
number_of_students = 7       # good: instantly clear
print("Students:", number_of_students)

# Use a named constant instead of a mystery number
TAX_RATE = 0.05
def add_tax(price):
    return price + price * TAX_RATE

print("Price with tax:", add_tax(100))   # 105.0

# A small function with a clear, descriptive name
def to_uppercase(text):
    return text.upper()

print(to_uppercase("hello"))             # HELLO


if __name__ == "__main__":
    print("\nClear names + small functions + hints = code that's easy to read.")
