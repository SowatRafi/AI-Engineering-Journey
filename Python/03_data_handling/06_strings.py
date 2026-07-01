"""
06_strings.py
=============

Topic: Strings — text as an immutable sequence of characters.

WHY THIS MATTERS
----------------
Text is the primary interface of AI engineering: prompts, model outputs, JSON,
logs, and file contents are all strings. Fluent string handling is non-optional.
"""

# ---------------------------------------------------------------------------
# 1. Creating strings and quoting
# ---------------------------------------------------------------------------
single = 'single quotes'
double = "double quotes"
triple = """A triple-quoted string
spans multiple lines."""          # great for multi-line text and docstrings
print("--- Multi-line ---")
print(triple)


# ---------------------------------------------------------------------------
# 2. Strings are immutable but indexable/sliceable (like tuples of characters)
# ---------------------------------------------------------------------------
word = "Python"
print("\n--- Indexing/slicing ---")
print("First char:", word[0])     # 'P'
print("Last char:", word[-1])     # 'n'
print("Slice [0:3]:", word[0:3])  # 'Pyt'
print("Reversed:", word[::-1])    # 'nohtyP'
# word[0] = "J"  # TypeError — strings cannot be mutated in place


# ---------------------------------------------------------------------------
# 3. Common, high-value methods (each returns a NEW string)
# ---------------------------------------------------------------------------
messy = "   Hello, World!   "
print("\n--- Methods ---")
print("strip:", repr(messy.strip()))        # remove surrounding whitespace
print("lower:", messy.strip().lower())
print("replace:", "cat".replace("c", "b"))  # 'bat'
print("startswith:", "report.pdf".endswith(".pdf"))
print("find:", "hello".find("l"))           # index of first match (or -1)


# ---------------------------------------------------------------------------
# 4. split and join — converting between strings and lists
# ---------------------------------------------------------------------------
print("\n--- split / join ---")
csv_row = "name,phase,city"
fields = csv_row.split(",")       # str -> list
print("split:", fields)

rejoined = " | ".join(fields)     # list -> str, glued by the separator
print("join:", rejoined)


# ---------------------------------------------------------------------------
# 5. f-strings: formatting and alignment
# ---------------------------------------------------------------------------
print("\n--- f-strings ---")
name, score = "Rafi", 0.9137
print(f"Plain: {name} scored {score}")
print(f"Percent, 1 dp: {score:.1%}")        # 91.4%
print(f"Fixed, 2 dp:  {score:.2f}")         # 0.91
print(f"Padded:      |{name:>10}|")         # right-align in a width of 10
print(f"Debug (=):   {score=}")             # prints 'score=0.9137'


# ---------------------------------------------------------------------------
# 6. Escape sequences and raw strings
# ---------------------------------------------------------------------------
print("\n--- Escapes ---")
print("Tab\tseparated\tvalues")
print("Line one\nLine two")
print(r"Raw string keeps backslashes: C:\Users\name")  # r"" disables escapes


if __name__ == "__main__":
    print("\nDone: you can slice, transform, and format text confidently.")
