"""
04_sequences_and_iterables.py
=============================

Built-ins for working with lists and other things you can loop over.

Covers: len, range, slice, sorted, reversed, enumerate, zip, iter, next,
        all, any, map, filter   (aiter, anext are mentioned at the end)

WHY THIS MATTERS
----------------
Most programs work with collections of things. These built-ins let you count,
sort, pair up, filter, and check them without writing long loops.
"""

# ---------------------------------------------------------------------------
# len() — how many items?
# ---------------------------------------------------------------------------
print("--- len ---")
print(len("hello"))         # 5
print(len([1, 2, 3]))       # 3


# ---------------------------------------------------------------------------
# range() — make a sequence of numbers
# ---------------------------------------------------------------------------
print("\n--- range ---")
print(list(range(5)))           # [0, 1, 2, 3, 4]
print(list(range(2, 11, 2)))    # [2, 4, 6, 8, 10]  (start at 2, step by 2)


# ---------------------------------------------------------------------------
# sorted() — return a new list in order (the original stays the same)
# ---------------------------------------------------------------------------
print("\n--- sorted ---")
print(sorted([3, 1, 2]))                    # [1, 2, 3]
print(sorted([3, 1, 2], reverse=True))      # [3, 2, 1]
# Sort words by length using 'key':
print(sorted(["bb", "a", "ccc"], key=len))  # ['a', 'bb', 'ccc']


# ---------------------------------------------------------------------------
# reversed() — go through items backwards
# ---------------------------------------------------------------------------
print("\n--- reversed ---")
print(list(reversed([1, 2, 3])))    # [3, 2, 1]


# ---------------------------------------------------------------------------
# enumerate() — get a position number for each item
# ---------------------------------------------------------------------------
print("\n--- enumerate ---")
for position, colour in enumerate(["red", "green", "blue"], start=1):
    print(position, colour)         # 1 red / 2 green / 3 blue


# ---------------------------------------------------------------------------
# zip() — walk through two lists side by side
# ---------------------------------------------------------------------------
print("\n--- zip ---")
names = ["Ana", "Ben"]
scores = [90, 82]
for name, score in zip(names, scores):
    print(name, "scored", score)    # Ana scored 90 / Ben scored 82


# ---------------------------------------------------------------------------
# slice() — save a "cut" you can reuse
# ---------------------------------------------------------------------------
print("\n--- slice ---")
numbers = [10, 20, 30, 40, 50]
first_two = slice(0, 2)             # this is the same as [0:2]
print(numbers[first_two])           # [10, 20]


# ---------------------------------------------------------------------------
# all() and any() — check a whole list in one line
# ---------------------------------------------------------------------------
print("\n--- all / any ---")
grades = [88, 72, 95]
print(all(g >= 50 for g in grades))     # True  -> did EVERYONE pass 50?
print(any(g < 65 for g in grades))      # False -> did ANYONE score below 65?


# ---------------------------------------------------------------------------
# map() — do the same thing to every item
# ---------------------------------------------------------------------------
print("\n--- map ---")
def double(n):
    return n * 2

# map() runs 'double' on each number. Wrap it in list() to see the results.
print(list(map(double, [1, 2, 3])))     # [2, 4, 6]


# ---------------------------------------------------------------------------
# filter() — keep only the items that pass a test
# ---------------------------------------------------------------------------
print("\n--- filter ---")
def is_even(n):
    return n % 2 == 0

print(list(filter(is_even, [1, 2, 3, 4, 5, 6])))    # [2, 4, 6]


# ---------------------------------------------------------------------------
# iter() and next() — get items one at a time
# ---------------------------------------------------------------------------
print("\n--- iter / next ---")
colours = iter(["red", "green"])    # turn the list into an "iterator"
print(next(colours))                # red
print(next(colours))                # green
print(next(colours, "no more"))     # no more  (a safe default when empty)


# ---------------------------------------------------------------------------
# aiter() and anext() — the async versions (ADVANCED, you can skip for now)
# ---------------------------------------------------------------------------
# These do the same job as iter()/next() but inside "async" code, which you use
# for things like waiting on the internet. You'll meet them much later; for now
# just know they exist and are the async twins of iter() and next().


if __name__ == "__main__":
    print("\nDone: count, sort, pair, filter, and step through collections.")
