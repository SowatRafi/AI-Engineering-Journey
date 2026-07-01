"""
03_numbers_and_characters.py
============================

Built-ins that show numbers in other forms, and swap characters with their
number codes.

Covers: bin, oct, hex, chr, ord, ascii, format

WHY THIS MATTERS
----------------
Computers often show numbers in binary or hex, and every character has a number
behind it. These built-ins let you move between those forms easily.
"""

# ---------------------------------------------------------------------------
# bin(), oct(), hex() — see a number in base 2, 8, or 16
# ---------------------------------------------------------------------------
print("--- number bases ---")
# The prefix tells you the base: 0b = binary, 0o = octal, 0x = hex.
print(bin(10))      # 0b1010
print(oct(64))      # 0o100
print(hex(255))     # 0xff


# ---------------------------------------------------------------------------
# ord() and chr() — a character and its number code
# ---------------------------------------------------------------------------
print("\n--- ord / chr ---")
# Every character has a number (its Unicode code).
print(ord("A"))     # 65   (letter -> number)
print(chr(65))      # A    (number -> letter)
print(ord("a"))     # 97
print(chr(97))      # a

# Example: get the next letter of the alphabet.
letter = "b"
print(chr(ord(letter) + 1))     # c


# ---------------------------------------------------------------------------
# ascii() — show a string with special characters written out
# ---------------------------------------------------------------------------
print("\n--- ascii ---")
# The é becomes an escape code, so you can see exactly what's in the text.
print(ascii("café"))    # 'caf\xe9'


# ---------------------------------------------------------------------------
# format() — turn a value into nicely formatted text
# ---------------------------------------------------------------------------
print("\n--- format ---")
print(format(1234567, ","))     # 1,234,567   (add thousands separators)
print(format(0.9137, ".1%"))    # 91.4%       (show as a percentage)
print(format(3.14159, ".2f"))   # 3.14        (2 decimal places)
print(format(255, "x"))         # ff          (as hexadecimal)
# Tip: f-strings use the same codes -> f"{0.9137:.1%}" also gives "91.4%".


if __name__ == "__main__":
    print("\nDone: change a number's base, and swap letters with their codes.")
