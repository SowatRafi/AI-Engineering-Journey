"""
beginner_examples.py  (OOP / Polymorphism)
==========================================

EXTRA easy examples for: polymorphism ("many forms").

Idea: the SAME action word works on different things,
      and each thing responds in its own way.
      Example: everyone can "speak", but a dog and a cat speak differently.
"""

# ===========================================================================
# EXAMPLE 1: same method name, different results
# ===========================================================================
print("========== EXAMPLE 1: Animal sounds ==========")

class Dog:
    def speak(self):
        return "Woof"

class Cat:
    def speak(self):
        return "Meow"

class Cow:
    def speak(self):
        return "Moo"

# One loop handles all of them — each speaks in its own way.
for animal in [Dog(), Cat(), Cow()]:
    print(animal.speak())


# ===========================================================================
# EXAMPLE 2: the same '+' behaves differently by type (built-in example)
# ===========================================================================
print("\n========== EXAMPLE 2: '+' has many forms ==========")

print(2 + 3)                 # numbers -> adds -> 5
print("cat" + "dog")         # text    -> joins -> catdog
print([1, 2] + [3, 4])       # lists   -> combines -> [1, 2, 3, 4]


# ===========================================================================
# EXAMPLE 3: making '+' work on YOUR own object (operator overloading)
# ===========================================================================
print("\n========== EXAMPLE 3: adding money ==========")

class Money:
    def __init__(self, amount):
        self.amount = amount

    # __add__ is called when you write:  wallet1 + wallet2
    def __add__(self, other):
        return Money(self.amount + other.amount)

    # __str__ decides what print() shows
    def __str__(self):
        return f"${self.amount}"

wallet1 = Money(10)
wallet2 = Money(5)
total = wallet1 + wallet2    # uses our __add__
print("Total money:", total) # uses our __str__ -> $15


# ===========================================================================
# EXAMPLE 4: one function, many shapes
# ===========================================================================
print("\n========== EXAMPLE 4: describe anything ==========")

class Circle:
    def area(self):
        return 3.14 * 2 * 2

class Square:
    def area(self):
        return 4 * 4

def print_area(shape):       # works for ANY shape that has .area()
    print("Area is", shape.area())

print_area(Circle())
print_area(Square())


if __name__ == "__main__":
    print("\nSame action, different behavior depending on the object.")
