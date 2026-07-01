"""
inheritance.py
==============

OOP Principle: INHERITANCE — modelling "is-a" relationships so a child class
reuses and extends a parent class.

WHY THIS MATTERS
----------------
Inheritance removes duplication: shared behaviour lives in a base class, and
specialised classes add or override just what differs. This file covers single,
multi-level, hierarchical, and multiple inheritance, plus super() and MRO.
"""


# ===========================================================================
# 1. SINGLE inheritance: one child, one parent
# ===========================================================================
class Animal:
    """Base class with shared behaviour."""

    def __init__(self, name: str) -> None:
        self.name = name

    def eat(self) -> str:
        return f"{self.name} is eating."

    def speak(self) -> str:
        return "Some generic sound."


class Cat(Animal):               # Cat "is-a" Animal
    """Child class: inherits eat(), overrides speak()."""

    def speak(self) -> str:      # OVERRIDE the parent's version
        return f"{self.name} says Meow."


print("--- Single inheritance ---")
cat = Cat("Luna")
print(cat.eat())                 # inherited from Animal
print(cat.speak())               # overridden in Cat
print("Is Cat an Animal?", isinstance(cat, Animal))     # True
print("Is Cat a subclass?", issubclass(Cat, Animal))    # True


# ===========================================================================
# 2. super() — extend, don't replace, the parent
# ===========================================================================
class Employee:
    def __init__(self, name: str, salary: float) -> None:
        self.name = name
        self.salary = salary

    def describe(self) -> str:
        return f"{self.name} earns {self.salary:.0f}"


class Manager(Employee):
    def __init__(self, name: str, salary: float, team_size: int) -> None:
        # super() calls the parent's __init__ so we don't rewrite that logic.
        super().__init__(name, salary)
        self.team_size = team_size          # add new state

    def describe(self) -> str:
        base = super().describe()           # reuse parent's string, then extend
        return f"{base} and manages {self.team_size} people"


print("\n--- super() ---")
print(Manager("Rafi", 90000, 5).describe())


# ===========================================================================
# 3. MULTI-LEVEL inheritance: a chain (grandparent -> parent -> child)
# ===========================================================================
class Vehicle:
    def move(self) -> str:
        return "moving"


class Car(Vehicle):              # Car is-a Vehicle
    def move(self) -> str:
        return "driving on roads"


class SportsCar(Car):            # SportsCar is-a Car is-a Vehicle
    def move(self) -> str:
        return "driving fast on roads"


print("\n--- Multi-level inheritance ---")
sc = SportsCar()
print("SportsCar move:", sc.move())
print("Still a Vehicle?", isinstance(sc, Vehicle))     # True (whole chain)


# ===========================================================================
# 4. HIERARCHICAL inheritance: several children share one parent
# ===========================================================================
class Shape:
    def area(self) -> float:
        raise NotImplementedError("Subclasses must implement area().")


class Square(Shape):
    def __init__(self, side: float) -> None:
        self.side = side

    def area(self) -> float:
        return self.side ** 2


class Rectangle(Shape):
    def __init__(self, width: float, height: float) -> None:
        self.width, self.height = width, height

    def area(self) -> float:
        return self.width * self.height


print("\n--- Hierarchical inheritance ---")
for shape in (Square(4), Rectangle(3, 5)):
    print(f"{type(shape).__name__} area:", shape.area())


# ===========================================================================
# 5. MULTIPLE inheritance and the MRO (Method Resolution Order)
# ===========================================================================
# A class can inherit from more than one parent. Python resolves which method to
# use via the MRO (a deterministic left-to-right, depth-considered order).
class Swimmer:
    def dive(self) -> str:
        return "diving"

    def action(self) -> str:
        return "swimming"


class Flyer:
    def soar(self) -> str:
        return "soaring"

    def action(self) -> str:
        return "flying"


class Duck(Swimmer, Flyer):      # inherits from BOTH
    """When both parents define action(), MRO picks the FIRST parent listed."""


print("\n--- Multiple inheritance + MRO ---")
duck = Duck()
print("Can:", duck.dive(), "&", duck.soar())
print("action() resolves to:", duck.action())   # 'swimming' (Swimmer is first)
# The MRO is the exact search order Python uses:
print("MRO:", [cls.__name__ for cls in Duck.__mro__])


if __name__ == "__main__":
    print("\nDone: you can model is-a hierarchies and reuse code with super().")
