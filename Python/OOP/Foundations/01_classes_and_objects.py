"""
01_classes_and_objects.py
=========================

Topic: Classes, objects, instances, attributes, and methods — the foundation.

WHY THIS MATTERS
----------------
Object-Oriented Programming lets you bundle DATA (attributes) together with the
BEHAVIOUR that operates on it (methods). A `class` is a blueprint; an `object`
(or `instance`) is a concrete thing built from that blueprint.
"""


# ---------------------------------------------------------------------------
# 1. A minimal class
# ---------------------------------------------------------------------------
class Dog:
    """A blueprint for dogs.

    `class` defines a new TYPE. `self` is the conventional name for "this
    particular object" and is passed automatically when you call a method.
    """

    def __init__(self, name: str, age: int) -> None:
        """The initializer (constructor). Runs when a new Dog is created.

        We attach data to `self` so it becomes part of THIS instance.
        These are INSTANCE ATTRIBUTES — each object has its own copy.
        """
        self.name = name        # instance attribute
        self.age = age          # instance attribute

    def bark(self) -> str:
        """An INSTANCE METHOD — behaviour that uses the object's own data."""
        return f"{self.name} says Woof!"

    def describe(self) -> str:
        return f"{self.name} is {self.age} years old."


# ---------------------------------------------------------------------------
# 2. Creating instances (objects)
# ---------------------------------------------------------------------------
print("--- Instances ---")
rex = Dog("Rex", 3)              # calls __init__ behind the scenes
luna = Dog("Luna", 5)            # a SEPARATE object with its own attributes

print(rex.bark())                # Rex says Woof!
print(luna.describe())           # Luna is 5 years old.

# Each instance holds its own state:
print("rex.name:", rex.name, "| luna.name:", luna.name)
print("Are they the same object?", rex is luna)   # False


# ---------------------------------------------------------------------------
# 3. Class attributes vs. instance attributes
# ---------------------------------------------------------------------------
class Circle:
    """Demonstrates the difference between shared and per-object data."""

    # CLASS ATTRIBUTE: shared by ALL instances (one copy on the class).
    pi = 3.14159

    def __init__(self, radius: float) -> None:
        # INSTANCE ATTRIBUTE: unique to each object.
        self.radius = radius

    def area(self) -> float:
        # Access the shared class attribute via self (or Circle.pi).
        return Circle.pi * self.radius ** 2


print("\n--- Class vs. instance attributes ---")
small = Circle(1)
big = Circle(10)
print("small.pi:", small.pi, "| big.pi:", big.pi, "(shared)")
print("small.area():", round(small.area(), 2))
print("big.area():", round(big.area(), 2))


# ---------------------------------------------------------------------------
# 4. Methods can modify state
# ---------------------------------------------------------------------------
class Counter:
    def __init__(self) -> None:
        self.count = 0

    def increment(self) -> None:
        self.count += 1          # mutate this instance's state

    def reset(self) -> None:
        self.count = 0


if __name__ == "__main__":
    print("\n--- Stateful object ---")
    c = Counter()
    c.increment()
    c.increment()
    print("Count after two increments:", c.count)   # 2
    c.reset()
    print("Count after reset:", c.count)             # 0
    print("\nDone: a class bundles data + behaviour; objects are instances of it.")
