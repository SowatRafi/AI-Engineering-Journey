"""
beginner_examples.py  (OOP / Inheritance)
=========================================

EXTRA easy examples for: inheritance (a child class reuses a parent class).

Idea: "a Dog IS An Animal", so Dog can reuse Animal's abilities
      and add its own. This saves you from repeating code.
"""

# ===========================================================================
# EXAMPLE 1: Animals
# ===========================================================================
print("========== EXAMPLE 1: Animals ==========")

class Animal:                 # the PARENT (base) class
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(self.name, "is eating.")

class Dog(Animal):            # the CHILD inherits from Animal
    def bark(self):
        print(self.name, "says Woof!")

rex = Dog("Rex")
rex.eat()          # borrowed from Animal — no need to rewrite it
rex.bark()         # Dog's own ability


# ===========================================================================
# EXAMPLE 2: overriding — the child changes a parent's behavior
# ===========================================================================
print("\n========== EXAMPLE 2: Overriding ==========")

class Vehicle:
    def sound(self):
        print("Some vehicle sound")

class Motorbike(Vehicle):
    def sound(self):                 # same method name = replaces the parent's
        print("Vroom vroom!")

Vehicle().sound()      # Some vehicle sound
Motorbike().sound()    # Vroom vroom!


# ===========================================================================
# EXAMPLE 3: super() — reuse the parent's setup, then add more
# ===========================================================================
print("\n========== EXAMPLE 3: super() ==========")

class Person:
    def __init__(self, name):
        self.name = name

class Student(Person):
    def __init__(self, name, school):
        super().__init__(name)       # let Person handle the name
        self.school = school         # then add our own extra info

    def show(self):
        print(f"{self.name} studies at {self.school}")

Student("Sara", "MIT").show()


# ===========================================================================
# EXAMPLE 4: a family chain (grandparent -> parent -> child)
# ===========================================================================
print("\n========== EXAMPLE 4: A chain ==========")

class Grandparent:
    def family_name(self):
        print("Our family name is Rahman")

class Parent(Grandparent):
    pass                              # inherits everything, adds nothing

class Child(Parent):
    pass

Child().family_name()   # reaches all the way up the chain


if __name__ == "__main__":
    print("\nInheritance = reuse a parent's code, then add or change what you need.")
