"""
01_variables_and_types.py
==========================

Topic: Variables and Python's core built-in types.

WHY THIS MATTERS
----------------
A variable is just a *name* that points to an object in memory. Understanding
that names are labels (not boxes) explains almost every "surprising" behaviour
in Python later on (especially mutability, covered in the OOP module).

Run this file directly to see the output:

    python 01_variables_and_types.py
"""

# ---------------------------------------------------------------------------
# 1. Variables are names bound to objects
# ---------------------------------------------------------------------------
# No type declaration is needed. The type belongs to the *object*, not the name.
message = "Hello, AI Engineer"   # `message` now points to a str object
year = 2026                      # `year` points to an int object
pi = 3.14159                     # a float
is_learning = True               # a bool

# You can rebind a name to a completely different type at any time.
# This is why Python is called "dynamically typed".
value = 10          # int
value = "ten"       # now the same name points to a str — perfectly legal


# ---------------------------------------------------------------------------
# 2. The core built-in types
# ---------------------------------------------------------------------------
# type() tells you what kind of object a name currently points to.
print("--- Core types ---")
print(type(message))   # <class 'str'>
print(type(year))      # <class 'int'>
print(type(pi))        # <class 'float'>
print(type(is_learning))  # <class 'bool'>
print(type(None))      # <class 'NoneType'> — represents "no value"


# ---------------------------------------------------------------------------
# 3. Numbers: int, float, and basic arithmetic
# ---------------------------------------------------------------------------
print("\n--- Numbers ---")
a, b = 17, 5                 # multiple assignment in one line
print("Addition:", a + b)        # 22
print("Subtraction:", a - b)     # 12
print("Multiplication:", a * b)  # 85
print("True division:", a / b)   # 3.4  -> always returns a float
print("Floor division:", a // b) # 3    -> discards the remainder
print("Modulo:", a % b)          # 2    -> the remainder
print("Power:", a ** 2)          # 289


# ---------------------------------------------------------------------------
# 4. Strings: text data
# ---------------------------------------------------------------------------
print("\n--- Strings ---")
first = "Sowat"
last = "Rafi"
full = first + " " + last        # concatenation with +
print("Concatenation:", full)

# f-strings (formatted string literals) are the modern, readable way to build
# strings. The expression inside {} is evaluated and inserted.
print(f"f-string: {first} is learning AI in {year}.")

# Strings are immutable — you cannot change a character in place. Instead you
# create a *new* string. (More on immutability in the OOP module.)
print("Upper:", full.upper())
print("Length:", len(full))


# ---------------------------------------------------------------------------
# 5. Type conversion (casting)
# ---------------------------------------------------------------------------
# User input and file data usually arrive as strings; convert explicitly.
print("\n--- Type conversion ---")
age_text = "30"                  # a string
age_number = int(age_text)       # convert to int so we can do math
print("Next year you'll be:", age_number + 1)

print("Float to int truncates:", int(3.99))   # 3 (not rounded!)
print("Int to string:", "Level " + str(7))    # must cast before concatenating


# ---------------------------------------------------------------------------
# 6. Dynamic typing pitfall to remember
# ---------------------------------------------------------------------------
# Because types are flexible, mixing them by accident raises a TypeError.
try:
    result = "5" + 5             # str + int is NOT allowed
except TypeError as error:
    print("\nCaught a TypeError:", error)
    # Fix: decide what you meant — "55" (str) or 10 (int) — and cast.
    print("Fixed as numbers:", int("5") + 5)


if __name__ == "__main__":
    # This block only runs when the file is executed directly (not imported).
    # It's a Python convention explained in detail in 02_logic/03_modules_and_imports.py
    print("\nDone: you now understand variables, types, and casting.")
