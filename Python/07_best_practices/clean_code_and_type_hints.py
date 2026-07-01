"""
clean_code_and_type_hints.py
============================

Topic: Clean-code habits — naming (PEP 8), type hints, small functions, and
self-documenting code.

WHY THIS MATTERS
----------------
Code is read far more often than it is written. The roadmap's whole thesis is
"production-first thinking": readable, well-named, type-hinted code is what makes
a system maintainable, reviewable, and hireable. These habits start now.
"""

from dataclasses import dataclass


# ===========================================================================
# 1. NAMING CONVENTIONS (PEP 8 — Python's style guide)
# ===========================================================================
# - variables & functions : snake_case
# - constants             : UPPER_SNAKE_CASE
# - classes               : PascalCase (a.k.a. CapWords)
# - "internal" helpers    : _leading_underscore
#
# Names should reveal INTENT. Prefer clarity over brevity.

MAX_RETRIES = 3                  # constant: UPPER_SNAKE_CASE


def calculate_average_score(scores: list[float]) -> float:   # snake_case, clear
    """Good: the name says exactly what it returns."""
    if not scores:
        return 0.0
    return sum(scores) / len(scores)


# Compare — same logic, unclear names (DON'T do this):
def calc(x):                     # what is x? what does calc do?
    return sum(x) / len(x)


# ===========================================================================
# 2. TYPE HINTS — document and check the shapes of your data
# ===========================================================================
# Type hints don't change runtime behaviour, but they:
#   - document expected inputs/outputs,
#   - power editor autocomplete and error highlighting,
#   - let tools like `mypy` catch bugs before you run the code.
def send_prompt(prompt: str, temperature: float = 0.7, retries: int = 3) -> str:
    """Every parameter and the return value is annotated."""
    return f"sent {prompt!r} at temp={temperature} (up to {retries} retries)"


# Container and optional types:
from typing import Optional


def find_user(user_id: int, users: dict[int, str]) -> Optional[str]:
    """Return the user's name, or None if not found.

    `Optional[str]` == `str | None` — signals the caller MUST handle None.
    """
    return users.get(user_id)


# ===========================================================================
# 3. FUNCTIONS SHOULD DO ONE THING
# ===========================================================================
# A function that does one thing is easy to name, test, and reuse.
# BAD: one function fetches, validates, transforms, saves, and emails.
# GOOD: small functions, each with a single responsibility, composed together.
def normalize(text: str) -> str:
    """One job: clean up a string."""
    return text.strip().lower()


def is_valid_email(text: str) -> bool:
    """One job: a simple validity check."""
    return "@" in text and "." in text.split("@")[-1]


def register(email: str) -> str:
    """Compose the small helpers — reads like a sentence."""
    email = normalize(email)
    if not is_valid_email(email):
        raise ValueError(f"Invalid email: {email!r}")
    return f"Registered {email}"


# ===========================================================================
# 4. dataclasses — clean, boilerplate-free data holders
# ===========================================================================
# @dataclass auto-generates __init__, __repr__, and __eq__ from the annotations.
# Perfect for simple "record" objects; expresses intent with minimal code.
@dataclass
class ModelConfig:
    name: str
    temperature: float = 0.7
    max_tokens: int = 1024


# ===========================================================================
# 5. GUARD CLAUSES over deep nesting; comments explain WHY, not WHAT
# ===========================================================================
def apply_discount(price: float, is_member: bool) -> float:
    # Guard clause: handle the edge case first and return early, keeping the
    # main logic un-indented and easy to follow.
    if price < 0:
        raise ValueError("price cannot be negative")

    # WHY comment: members get a loyalty discount per the 2026 pricing policy.
    if is_member:
        return round(price * 0.9, 2)
    return price


if __name__ == "__main__":
    print("--- Clean code in action ---")
    print("Average:", calculate_average_score([90, 80, 100]))
    print(send_prompt("Explain attention", temperature=0.2))
    print("Find user 1:", find_user(1, {1: "Rafi"}))
    print("Find user 9:", find_user(9, {1: "Rafi"}))   # None, handled by caller
    print(register("  Rafi@Example.com "))
    print("Config:", ModelConfig("claude", max_tokens=2048))   # auto __repr__
    print("Member price:", apply_discount(100, is_member=True))
    print("\nDone: readable, typed, single-purpose code is professional code.")
