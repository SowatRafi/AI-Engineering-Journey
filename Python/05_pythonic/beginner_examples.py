"""
beginner_examples.py  (05_pythonic)
===================================

EXTRA easy examples for: comprehensions, iterators, and generators.
These are shortcuts that make Python code shorter and cleaner.
"""

# ===========================================================================
# LIST COMPREHENSIONS — build a list in one short line
# ===========================================================================
print("========== LIST COMPREHENSIONS ==========")

# The long way (a loop):
squares_long = []
for n in [1, 2, 3, 4]:
    squares_long.append(n * n)
print("Long way:", squares_long)

# The short way (a comprehension) — read it as "n*n for each n":
squares_short = [n * n for n in [1, 2, 3, 4]]
print("Short way:", squares_short)

# Example: double every number
numbers = [1, 2, 3]
doubled = [n * 2 for n in numbers]
print("Doubled:", doubled)

# Example: keep only the even numbers (the 'if' filters)
all_numbers = [1, 2, 3, 4, 5, 6]
evens = [n for n in all_numbers if n % 2 == 0]
print("Evens only:", evens)

# Example: make each word UPPERCASE
words = ["cat", "dog", "fish"]
loud = [w.upper() for w in words]
print("Loud words:", loud)


# ===========================================================================
# ITERATORS — going through items one at a time
# ===========================================================================
print("\n========== ITERATORS ==========")

# A for-loop already does this for you, one item at a time:
for animal in ["cat", "dog", "cow"]:
    print("Animal:", animal)

# You can also ask for the "next" item by hand using iter() and next():
colors = iter(["red", "green", "blue"])
print("First:", next(colors))
print("Second:", next(colors))
print("Third:", next(colors))


# ===========================================================================
# GENERATORS — make values one at a time using 'yield' (saves memory)
# ===========================================================================
print("\n========== GENERATORS ==========")

# A generator gives you values only when you ask for them.
def count_to(limit):
    number = 1
    while number <= limit:
        yield number          # hand back one value, then pause
        number = number + 1

for value in count_to(5):
    print("Value:", value)

# Example: yield only the happy words
def only_happy(words):
    for word in words:
        if word in ("yay", "great", "nice"):
            yield word

for word in only_happy(["yay", "meh", "great", "boo", "nice"]):
    print("Happy word:", word)


if __name__ == "__main__":
    print("\nComprehensions shorten loops; generators hand out values lazily.")
