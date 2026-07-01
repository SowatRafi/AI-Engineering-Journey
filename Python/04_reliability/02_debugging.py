"""
02_debugging.py
===============

Topic: Debugging techniques — finding out WHY code misbehaves.

WHY THIS MATTERS
----------------
You will spend more time reading and fixing code than writing it. Systematic
debugging beats random guessing. This file shows the core tools, from quick
prints to the built-in debugger and logging.
"""

import logging
import pdb  # noqa: F401  (imported to show usage; breakpoint() is preferred)


# ---------------------------------------------------------------------------
# 1. print debugging — fast, but noisy. Use f-string '=' for clarity.
# ---------------------------------------------------------------------------
def average(numbers: list[float]) -> float:
    """Buggy-looking function used to demonstrate inspection."""
    total = sum(numbers)
    count = len(numbers)
    # The {var=} form prints both the name and value — perfect for tracing.
    print(f"[trace] {total=} {count=}")
    return total / count


print("--- print debugging ---")
print("avg:", average([10, 20, 30]))


# ---------------------------------------------------------------------------
# 2. Reading a traceback (the most important debugging skill)
# ---------------------------------------------------------------------------
# When an unhandled error occurs, Python prints a TRACEBACK. Read it BOTTOM-UP:
#   - the LAST line is the exception type and message (what went wrong)
#   - the lines above show the call stack (where it happened)
print("\n--- reading a traceback ---")
try:
    average([])                 # division by zero: count == 0
except ZeroDivisionError as error:
    print("Bottom line of a traceback would say:", type(error).__name__, "-", error)
    print("Fix: guard against an empty list before dividing.")


# ---------------------------------------------------------------------------
# 3. assert — check assumptions during development
# ---------------------------------------------------------------------------
# An assert documents and verifies an assumption. If it's False, it raises
# AssertionError immediately, close to the source of the bug.
def apply_discount(price: float, percent: float) -> float:
    assert 0 <= percent <= 100, f"percent must be 0-100, got {percent}"
    return price * (1 - percent / 100)


print("\n--- assert ---")
print("Discounted:", apply_discount(100, 20))
# apply_discount(100, 250)  # would raise AssertionError with a helpful message


# ---------------------------------------------------------------------------
# 4. The built-in debugger: breakpoint()
# ---------------------------------------------------------------------------
# Uncomment the breakpoint() line and run this file to drop into an interactive
# debugger AT THAT LINE. Handy commands once inside:
#   n (next line)  s (step into)  c (continue)  p expr (print)  q (quit)  l (list)
def buggy_sum(items):
    total = 0
    for item in items:
        # breakpoint()          # <- uncomment to inspect `item` and `total` live
        total += item
    return total


print("\n--- breakpoint() ---")
print("Sum:", buggy_sum([1, 2, 3]))
print("(Uncomment breakpoint() above and re-run to step through interactively.)")


# ---------------------------------------------------------------------------
# 5. logging — the production-grade replacement for print
# ---------------------------------------------------------------------------
# Unlike print, logging has severity levels, timestamps, and can be turned off
# or redirected without deleting lines. Prefer it in real applications.
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%H:%M:%S",
)
logger = logging.getLogger("demo")


def process(order_id: int) -> None:
    logger.debug("Starting to process order %s", order_id)   # detailed trace
    logger.info("Order %s processed", order_id)              # normal event
    if order_id < 0:
        logger.error("Invalid order id: %s", order_id)       # something wrong


if __name__ == "__main__":
    print("\n--- logging ---")
    process(101)
    process(-5)
    print("\nDone: you have a systematic toolkit for finding and fixing bugs.")
