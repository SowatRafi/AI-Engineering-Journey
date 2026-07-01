"""
02_scope.py
===========

Topic: Scope — where a name is visible, and the LEGB rule.

WHY THIS MATTERS
----------------
"Why can't my function see this variable?" is one of the most common beginner
confusions. Scope rules answer it precisely. Understanding scope also prevents
accidental bugs from shadowing and unwanted global state.
"""

# ---------------------------------------------------------------------------
# The LEGB rule: Python resolves a name by searching these scopes in order:
#   L - Local:     inside the current function
#   E - Enclosing: inside any enclosing (outer) function
#   G - Global:    at the top level of the module/file
#   B - Built-in:  names like len, print, range
# ---------------------------------------------------------------------------

GLOBAL_CONFIG = "production"     # a GLOBAL name (module level)


def show_local():
    """Local variables exist only inside the function call."""
    local_message = "I only exist here"   # LOCAL
    print("Inside function:", local_message)
    print("Can read global:", GLOBAL_CONFIG)  # globals are readable inside


show_local()
# print(local_message)  # <- would raise NameError: local_message is not visible here


# ---------------------------------------------------------------------------
# Reading vs. reassigning a global
# ---------------------------------------------------------------------------
counter = 0


def increment_wrong():
    """This RAISES an error: assigning to `counter` makes it local, but we read
    it before assignment. Shown here (commented) to explain the trap."""
    # counter = counter + 1   # UnboundLocalError
    pass


def increment_right():
    """Use `global` to say 'I mean the module-level counter'."""
    global counter
    counter += 1


print("\n--- global keyword ---")
increment_right()
increment_right()
print("Counter is now:", counter)   # 2
# NOTE: heavy use of `global` is a code smell. Prefer returning values instead.


# ---------------------------------------------------------------------------
# Enclosing scope and `nonlocal` (closures)
# ---------------------------------------------------------------------------
def make_counter():
    """A closure: the inner function 'remembers' the enclosing variable."""
    count = 0                    # ENCLOSING variable

    def step():
        nonlocal count           # refer to the enclosing `count`, not a new local
        count += 1
        return count

    return step                  # return the inner function itself


print("\n--- closures / nonlocal ---")
tick = make_counter()
print(tick(), tick(), tick())    # 1 2 3 — state is preserved between calls


# ---------------------------------------------------------------------------
# Shadowing a built-in (a naming pitfall)
# ---------------------------------------------------------------------------
def shadowing_demo():
    """Avoid naming variables `list`, `dict`, `str`, `id`, `sum`, etc."""
    # If you write `list = [1, 2]`, you can no longer call the built-in list().
    numbers = [3, 1, 2]          # good name — does not shadow anything
    return sorted(numbers)


if __name__ == "__main__":
    print("\n--- avoid shadowing ---")
    print(shadowing_demo())
    print("\nDone: you understand where names live (LEGB).")
