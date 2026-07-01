"""
03_loops.py
===========

Topic: Repetition with for-loops and while-loops, plus loop control.

WHY THIS MATTERS
----------------
Almost all real work is "do this for every item" or "keep going until done".
Loops express both. Choosing the right loop and the right control statement
keeps code correct and terminating (no infinite loops!).
"""

# ---------------------------------------------------------------------------
# 1. for-loop: iterate over a known collection
# ---------------------------------------------------------------------------
# Use a `for` loop when you know WHAT you are iterating over.
print("--- for over a list ---")
languages = ["Python", "SQL", "Bash"]
for language in languages:
    print(f"Learning: {language}")


# ---------------------------------------------------------------------------
# 2. range(): generate a sequence of numbers
# ---------------------------------------------------------------------------
# range(start, stop, step) — stop is EXCLUSIVE.
print("\n--- range ---")
for i in range(1, 6):          # 1, 2, 3, 4, 5
    print(f"Rep {i}")

for even in range(0, 11, 2):   # step of 2 -> 0, 2, 4, 6, 8, 10
    print("Even:", even)


# ---------------------------------------------------------------------------
# 3. enumerate(): get index AND value together
# ---------------------------------------------------------------------------
# Prefer enumerate() over manually tracking a counter — it's cleaner and safer.
print("\n--- enumerate ---")
for index, language in enumerate(languages, start=1):
    print(f"{index}. {language}")


# ---------------------------------------------------------------------------
# 4. while-loop: repeat until a condition is False
# ---------------------------------------------------------------------------
# Use a `while` loop when you DON'T know the count in advance — you loop until
# some condition changes. Always make sure the condition can become False!
print("\n--- while ---")
countdown = 3
while countdown > 0:
    print(f"T-minus {countdown}")
    countdown -= 1             # this line prevents an infinite loop
print("Liftoff!")


# ---------------------------------------------------------------------------
# 5. Loop control: break and continue
# ---------------------------------------------------------------------------
print("\n--- break / continue ---")
for number in range(1, 11):
    if number == 7:
        print("Found 7 — stopping.")
        break                  # exit the loop entirely
    if number % 2 == 0:
        continue               # skip the rest of THIS iteration
    print("Odd number:", number)


# ---------------------------------------------------------------------------
# 6. The for/else clause (a Python-specific feature)
# ---------------------------------------------------------------------------
# The `else` after a loop runs ONLY if the loop finished without hitting `break`.
# Useful for search loops.
print("\n--- for/else ---")
target = 99
for language in languages:
    if language == target:
        print("Match found.")
        break
else:
    print(f"'{target}' was not in the list (loop completed with no break).")


if __name__ == "__main__":
    print("\nDone: you can now repeat work and control the flow.")
