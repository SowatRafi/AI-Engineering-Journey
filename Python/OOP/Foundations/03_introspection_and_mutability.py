"""
03_introspection_and_mutability.py
==================================

Topic: The object model — introspection (__dict__, dir, type) and
mutability/immutability behaviour (pass-by-object-reference).

WHY THIS MATTERS
----------------
Understanding how Python stores object state and passes it around explains a
huge class of "why did my variable change?" bugs. This is the model beneath
everything in the OOP module.
"""


class Robot:
    """Simple class used to inspect an object's internals."""

    species = "android"          # class attribute (shared)

    def __init__(self, name: str, battery: int = 100) -> None:
        self.name = name         # instance attributes (per object)
        self.battery = battery

    def charge(self) -> None:
        self.battery = 100


# ---------------------------------------------------------------------------
# 1. __dict__ — an object's instance attributes, as a dictionary
# ---------------------------------------------------------------------------
# An object literally stores its instance state in a dict called __dict__.
print("--- __dict__ ---")
r = Robot("R2", 60)
print("Instance __dict__:", r.__dict__)      # {'name': 'R2', 'battery': 60}
# Note: `species` is NOT here — it lives on the CLASS, not the instance.
print("Class __dict__ keys:", list(Robot.__dict__.keys()))


# ---------------------------------------------------------------------------
# 2. dir() — every attribute and method a name exposes
# ---------------------------------------------------------------------------
print("\n--- dir() ---")
# dir() lists everything you can access via the dot, including inherited dunders.
public_members = [name for name in dir(r) if not name.startswith("_")]
print("Public members of a Robot:", public_members)


# ---------------------------------------------------------------------------
# 3. type(), isinstance(), and identity
# ---------------------------------------------------------------------------
print("\n--- type / isinstance / id ---")
print("type(r):", type(r).__name__)
print("isinstance(r, Robot):", isinstance(r, Robot))
print("id(r) is a unique object identity:", id(r) == id(r))


# ---------------------------------------------------------------------------
# 4. getattr / setattr / hasattr — attributes accessed dynamically by NAME
# ---------------------------------------------------------------------------
print("\n--- dynamic attribute access ---")
print("hasattr battery?", hasattr(r, "battery"))
print("getattr battery:", getattr(r, "battery"))
setattr(r, "owner", "Rafi")      # add a brand-new attribute at runtime
print("After setattr, __dict__:", r.__dict__)


# ===========================================================================
# 5. MUTABILITY: how Python passes objects
# ===========================================================================
# Python is "pass-by-object-reference". A function receives a reference to the
# SAME object. Whether the caller sees changes depends on whether the object is
# MUTABLE (list, dict, set, most custom objects) or IMMUTABLE (int, str, tuple).
# ---------------------------------------------------------------------------

def try_to_change_number(n: int) -> None:
    """Ints are IMMUTABLE. Rebinding `n` makes a new object; caller unaffected."""
    n += 100
    print("   inside (int):", n)


def try_to_change_list(items: list) -> None:
    """Lists are MUTABLE. Mutating in place is visible to the caller."""
    items.append("mutated!")
    print("   inside (list):", items)


print("\n--- Immutable argument (int) ---")
value = 5
try_to_change_number(value)
print("   outside:", value, "  <- unchanged")

print("\n--- Mutable argument (list) ---")
data = [1, 2, 3]
try_to_change_list(data)
print("   outside:", data, "  <- CHANGED (same object)")


# ---------------------------------------------------------------------------
# 6. Consequence: comparing identity (is) vs. equality (==)
# ---------------------------------------------------------------------------
print("\n--- is vs. == ---")
a = [1, 2, 3]
b = [1, 2, 3]
c = a
print("a == b (equal values)?", a == b)   # True
print("a is b (same object)?", a is b)    # False — two distinct lists
print("a is c (alias)?", a is c)          # True — c is another name for a


if __name__ == "__main__":
    print("\nDone: you understand introspection and mutable vs. immutable behaviour.")
