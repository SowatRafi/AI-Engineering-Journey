"""
06_oop_helpers.py
================

Built-ins you use when writing CLASSES (object-oriented programming).

Covers: super, property, classmethod, staticmethod
(The built-in 'object' is covered in 01_type_constructors.py.)

WHY THIS MATTERS
----------------
When you build your own classes, these four helpers keep them clean: reuse a
parent's code, make smart attributes, and add helper methods.
"""


# ---------------------------------------------------------------------------
# super() — use the parent class's version of a method
# ---------------------------------------------------------------------------
print("--- super ---")

class Animal:
    def __init__(self, name):
        self.name = name

    def describe(self):
        return f"{self.name} is an animal"


class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)      # let Animal set up 'name' (don't repeat it)
        self.breed = breed

    def describe(self):
        # reuse the parent's sentence, then add to it
        return super().describe() + f" (a {self.breed})"


print(Dog("Rex", "Labrador").describe())    # Rex is an animal (a Labrador)


# ---------------------------------------------------------------------------
# property() — make a method that you use like a simple attribute
# ---------------------------------------------------------------------------
print("\n--- property ---")

class Circle:
    def __init__(self, radius):
        self.radius = radius

    @property
    def area(self):                 # note: used as circle.area, WITHOUT ()
        return round(3.14159 * self.radius ** 2, 2)


circle = Circle(5)
print(circle.area)                  # 78.54  (looks like an attribute, runs code)


# ---------------------------------------------------------------------------
# classmethod() — a method that gets the CLASS, handy for extra "constructors"
# ---------------------------------------------------------------------------
print("\n--- classmethod ---")

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def baby(cls, name):            # 'cls' is the class itself (Person)
        return cls(name, 0)         # build a Person aged 0


baby = Person.baby("Sam")
print(baby.name, baby.age)          # Sam 0


# ---------------------------------------------------------------------------
# staticmethod() — a plain helper function kept inside a class
# ---------------------------------------------------------------------------
print("\n--- staticmethod ---")

class Calculator:
    @staticmethod
    def add(a, b):                  # no 'self' — it doesn't use the object
        return a + b


print(Calculator.add(3, 4))         # 7


if __name__ == "__main__":
    print("\nDone: these four helpers make your own classes cleaner.")
