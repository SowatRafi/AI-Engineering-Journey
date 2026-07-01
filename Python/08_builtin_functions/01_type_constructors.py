"""
01_type_constructors.py
=======================

Built-in functions that BUILD or CONVERT values.

Covers: bool, int, float, complex, str, list, tuple, dict, set, frozenset,
        bytes, bytearray, memoryview, object

WHY THIS MATTERS
----------------
Data often arrives in the wrong type (for example, text from a keyboard or a
file). These built-ins turn one type into another, and build containers.
Run this file to see each result printed next to the code.
"""

# ---------------------------------------------------------------------------
# int(), float(), str() — switch between numbers and text
# ---------------------------------------------------------------------------
print("--- numbers and text ---")
print(int("42"))            # text "42" -> the number 42
print(int(3.9))             # 3   (int() drops the decimals, it does NOT round)
print(float("3.5"))         # 3.5 (text -> decimal number)
print(str(100))             # "100" (number -> text, so you can join it to words)

# int() can also read text written in another base (base 2 = binary):
print(int("1010", 2))       # 10


# ---------------------------------------------------------------------------
# bool() — is this value True or False?
# ---------------------------------------------------------------------------
print("\n--- bool ---")
# "Empty" values are False: 0, "", [], None. Everything else is True.
print(bool(0), bool(""), bool([]))      # False False False
print(bool(5), bool("hi"), bool([1]))   # True True True


# ---------------------------------------------------------------------------
# complex() — a number with a real and an imaginary part (used in math/science)
# ---------------------------------------------------------------------------
print("\n--- complex ---")
number = complex(3, 4)      # means 3 + 4i
print(number)               # (3+4j)
print(abs(number))          # 5.0  (its length/size)


# ---------------------------------------------------------------------------
# list(), tuple(), set(), dict(), frozenset() — build containers
# ---------------------------------------------------------------------------
print("\n--- containers ---")
print(list("abc"))          # ['a', 'b', 'c']  (split text into a list)
print(tuple([1, 2, 3]))     # (1, 2, 3)        (a list that cannot change)
print(set([1, 2, 2, 3]))    # {1, 2, 3}        (duplicates are removed)
print(dict(name="Rafi", age=27))    # {'name': 'Rafi', 'age': 27}

# frozenset is a set that cannot be changed after you make it.
print(frozenset([1, 2, 2]))         # frozenset({1, 2})


# ---------------------------------------------------------------------------
# bytes(), bytearray(), memoryview() — raw binary data (files, networks)
# ---------------------------------------------------------------------------
print("\n--- binary data ---")
raw = bytes([72, 105])      # build bytes from number codes -> b'Hi'
print(raw, "->", raw.decode())      # b'Hi' -> Hi

editable = bytearray(b"cat")        # like bytes, but you CAN change it
editable[0] = ord("h")              # change the first byte 'c' to 'h'
print(editable)                     # bytearray(b'hat')

view = memoryview(b"hello")         # look at bytes without copying them
print(bytes(view[1:3]))             # b'el'


# ---------------------------------------------------------------------------
# object() — the simplest possible object
# ---------------------------------------------------------------------------
print("\n--- object ---")
# 'object' is the base that everything else is built on. Every value is one.
print(isinstance("hello", object))  # True
print(isinstance(123, object))      # True


if __name__ == "__main__":
    print("\nDone: use these to convert values and build containers.")
