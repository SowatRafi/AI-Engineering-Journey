"""
02_iterators.py
===============

Topic: Iterables vs. iterators, and the iterator protocol (__iter__/__next__).

WHY THIS MATTERS
----------------
Every for-loop in Python is powered by the iterator protocol. Understanding it
demystifies loops, explains why some objects can only be looped once, and lets
you build your own iterable objects.
"""

# ---------------------------------------------------------------------------
# 1. Iterable vs. iterator — the distinction
# ---------------------------------------------------------------------------
# ITERABLE: anything you can loop over (list, str, dict...). It can produce an
#           iterator via iter().
# ITERATOR: the object that actually yields items one at a time via next(), and
#           remembers its position. It is exhausted after the last item.
print("--- iter() and next() ---")
colours = ["red", "green", "blue"]   # an iterable
iterator = iter(colours)             # get an iterator from it

print(next(iterator))                # 'red'
print(next(iterator))                # 'green'
print(next(iterator))                # 'blue'
try:
    next(iterator)                   # nothing left -> StopIteration
except StopIteration:
    print("Iterator exhausted (StopIteration).")


# ---------------------------------------------------------------------------
# 2. What a for-loop really does (the desugared version)
# ---------------------------------------------------------------------------
print("\n--- A for-loop, by hand ---")
it = iter(colours)
while True:
    try:
        colour = next(it)            # for-loops call next() until StopIteration
    except StopIteration:
        break
    print("got:", colour)


# ---------------------------------------------------------------------------
# 3. Iterators are single-use (exhaustible)
# ---------------------------------------------------------------------------
print("\n--- Single-use ---")
numbers_iter = iter([1, 2, 3])
print("First pass:", list(numbers_iter))   # [1, 2, 3]
print("Second pass:", list(numbers_iter))  # [] — already exhausted!
# A list, by contrast, can be iterated many times because each `for` calls iter().


# ---------------------------------------------------------------------------
# 4. Build your OWN iterator with the protocol
# ---------------------------------------------------------------------------
class Countdown:
    """A custom iterator counting from `start` down to 1.

    __iter__ returns the iterator object (here, self).
    __next__ returns the next value or raises StopIteration when finished.
    """

    def __init__(self, start: int) -> None:
        self.current = start

    def __iter__(self) -> "Countdown":
        return self

    def __next__(self) -> int:
        if self.current <= 0:
            raise StopIteration      # signals the loop to stop
        self.current -= 1
        return self.current + 1


if __name__ == "__main__":
    print("\n--- Custom iterator ---")
    for n in Countdown(4):           # works in a normal for-loop
        print("tick:", n)            # 4, 3, 2, 1
    print("\nDone: you understand the protocol behind every loop.")
