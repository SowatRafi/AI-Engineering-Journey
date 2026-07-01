"""
03_generators.py
================

Topic: Generators — lazy iterators written as functions with `yield`.

WHY THIS MATTERS
----------------
Generators produce values ON DEMAND instead of building a whole list in memory.
This makes them ideal for large or infinite streams — exactly the kind of data
(logs, tokens, dataset rows) you handle in AI engineering.
"""

import sys


# ---------------------------------------------------------------------------
# 1. A generator function: uses `yield` instead of `return`
# ---------------------------------------------------------------------------
# Each `yield` produces a value and PAUSES the function, remembering its state.
# Execution resumes right after the yield on the next next()/loop step.
def count_up_to(limit: int):
    """Yield numbers 1..limit one at a time (lazily)."""
    n = 1
    while n <= limit:
        yield n                  # hand back n, then pause here
        n += 1


print("--- Generator function ---")
gen = count_up_to(5)
print("Type:", type(gen).__name__)          # 'generator'
print("Values:", list(gen))                 # [1, 2, 3, 4, 5]


# ---------------------------------------------------------------------------
# 2. The killer feature: memory efficiency
# ---------------------------------------------------------------------------
# A list comprehension builds ALL items now; a generator expression builds none
# until asked. Compare their memory footprint.
print("\n--- Memory: list vs. generator ---")
big_list = [n for n in range(1_000_000)]           # allocates a million ints
big_gen = (n for n in range(1_000_000))            # allocates almost nothing yet
print("list bytes:", sys.getsizeof(big_list))
print("generator bytes:", sys.getsizeof(big_gen))  # tiny and constant


# ---------------------------------------------------------------------------
# 3. Generator EXPRESSION — like a comprehension with () instead of []
# ---------------------------------------------------------------------------
print("\n--- Generator expression ---")
# Great for feeding aggregate functions without materialising a list.
total = sum(n ** 2 for n in range(1, 6))    # no intermediate list created
print("Sum of squares 1..5:", total)


# ---------------------------------------------------------------------------
# 4. Infinite streams (impossible with a list)
# ---------------------------------------------------------------------------
def fibonacci():
    """An INFINITE generator — safe because values are produced lazily."""
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b          # tuple-unpacking swap


print("\n--- Infinite generator (take first 8) ---")
fib = fibonacci()
first_eight = [next(fib) for _ in range(8)]
print(first_eight)               # [0, 1, 1, 2, 3, 5, 8, 13]


# ---------------------------------------------------------------------------
# 5. Pipelining generators (each stage is lazy)
# ---------------------------------------------------------------------------
def read_lines(text: str):
    """Pretend to stream lines from a large source."""
    for line in text.splitlines():
        yield line


def only_errors(lines):
    """Filter stage — consumes one generator, yields a narrower stream."""
    for line in lines:
        if "ERROR" in line:
            yield line.strip()


if __name__ == "__main__":
    log = "INFO ok\nERROR disk full\nINFO ok\nERROR timeout\n"
    print("\n--- Generator pipeline ---")
    # Data flows lazily through the pipeline, one line at a time.
    for error_line in only_errors(read_lines(log)):
        print("found:", error_line)
    print("\nDone: generators give you lazy, memory-friendly data streams.")
