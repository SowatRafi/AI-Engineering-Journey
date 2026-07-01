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


# ===========================================================================
# MORE EXAMPLES — comprehensions
# ===========================================================================
print("\n========== MORE: COMPREHENSIONS ==========")

# A dictionary comprehension: build a dict in one line
square_map = {n: n * n for n in [1, 2, 3, 4]}
print("Square map:", square_map)         # {1: 1, 2: 4, 3: 9, 4: 16}

# A set comprehension: collect the unique word lengths
lengths = {len(word) for word in ["hi", "bye", "yo"]}
print("Unique lengths:", lengths)        # {2, 3}

# Transform each item: add 10% tax to every price
prices = [100, 200, 50]
with_tax = [round(p * 1.1, 2) for p in prices]
print("With tax:", with_tax)             # [110.0, 220.0, 55.0]


# ===========================================================================
# MORE EXAMPLES — generators
# ===========================================================================
print("\n========== MORE: GENERATORS ==========")

# A generator expression (like a comprehension, but with () ) inside sum()
total = sum(n for n in range(1, 6))      # 1 + 2 + 3 + 4 + 5
print("Sum 1..5:", total)                # 15

# A generator that hands out even numbers up to a limit
def evens_up_to(limit):
    n = 0
    while n <= limit:
        yield n
        n = n + 2

print("Evens up to 8:", list(evens_up_to(8)))    # [0, 2, 4, 6, 8]


# ===========================================================================
# EVEN SIMPLER EXAMPLES
# ===========================================================================
print("\n========== EVEN SIMPLER ==========")

# Build a list of squares in one line
squares = [n * n for n in [1, 2, 3]]
print("Squares:", squares)               # [1, 4, 9]

# Keep only the short names (5 letters or fewer)
names = ["Ana", "Alexander", "Ben", "Christopher"]
short = [name for name in names if len(name) <= 5]
print("Short names:", short)             # ['Ana', 'Ben']

# A tiny generator that counts down to 1
def countdown(start):
    while start > 0:
        yield start
        start = start - 1

for number in countdown(3):
    print("Countdown:", number)          # 3, 2, 1


if __name__ == "__main__":
    print("\nComprehensions shorten loops; generators hand out values lazily.")
