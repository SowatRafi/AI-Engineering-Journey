"""
beginner_examples.py  (OOP / Abstraction)
=========================================

EXTRA easy examples for: abstraction (hide the messy details, show a simple button).

Idea: you press "play" on a remote without knowing the electronics inside.
      Abstraction lets you say WHAT should happen and hide HOW it happens.
      In Python we use 'abstract base classes' to say "every child MUST have this".
"""

from abc import ABC, abstractmethod


# ===========================================================================
# EXAMPLE 1: every Animal MUST be able to speak (but we don't say how here)
# ===========================================================================
print("========== EXAMPLE 1: Animal must speak ==========")

class Animal(ABC):                 # ABC = Abstract Base Class (a template)
    @abstractmethod
    def speak(self):
        ...                        # no code here — children must fill it in

class Dog(Animal):
    def speak(self):               # child provides the real behavior
        print("Woof!")

class Cat(Animal):
    def speak(self):
        print("Meow!")

Dog().speak()
Cat().speak()

# You cannot create the template itself — it's only a plan:
try:
    Animal()
except TypeError:
    print("(You can't create a plain Animal — it's just a template.)")


# ===========================================================================
# EXAMPLE 2: a simple 'button' idea — same button, different machines
# ===========================================================================
print("\n========== EXAMPLE 2: everything has a start() ==========")

class Machine(ABC):
    @abstractmethod
    def start(self):
        ...

class WashingMachine(Machine):
    def start(self):
        print("Washing your clothes...")

class Microwave(Machine):
    def start(self):
        print("Heating your food...")

# We can press "start" on any machine without knowing its inner details.
for machine in [WashingMachine(), Microwave()]:
    machine.start()


# ===========================================================================
# EXAMPLE 3: a payment template
# ===========================================================================
print("\n========== EXAMPLE 3: pay() must exist ==========")

class Payment(ABC):
    @abstractmethod
    def pay(self, amount):
        ...

class Cash(Payment):
    def pay(self, amount):
        print(f"Paid {amount} in cash.")

class Card(Payment):
    def pay(self, amount):
        print(f"Paid {amount} by card.")

Cash().pay(20)
Card().pay(50)


if __name__ == "__main__":
    print("\nAbstraction = agree on WHAT to do; each class decides HOW.")
