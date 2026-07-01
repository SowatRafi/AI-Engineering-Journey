"""
beginner_examples.py  (OOP / Foundations)
=========================================

EXTRA easy examples for: classes and objects.

Idea: a CLASS is a blueprint (like a cookie cutter).
      an OBJECT is a real thing made from it (like an actual cookie).
"""

# ===========================================================================
# EXAMPLE 1: a Dog blueprint
# ===========================================================================
print("========== EXAMPLE 1: Dog ==========")

class Dog:
    # __init__ runs when we make a new dog. 'self' means "this dog".
    def __init__(self, name):
        self.name = name          # store the name on this dog

    def bark(self):
        print(self.name, "says Woof!")

# Make two real dogs from the blueprint:
dog1 = Dog("Rex")
dog2 = Dog("Luna")
dog1.bark()          # Rex says Woof!
dog2.bark()          # Luna says Woof!


# ===========================================================================
# EXAMPLE 2: a Person with more than one piece of info
# ===========================================================================
print("\n========== EXAMPLE 2: Person ==========")

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"Hi, I'm {self.name} and I'm {self.age}.")

alice = Person("Alice", 30)
alice.introduce()
print("Alice's age is:", alice.age)   # read one piece of info


# ===========================================================================
# EXAMPLE 3: a Car that can do actions (methods)
# ===========================================================================
print("\n========== EXAMPLE 3: Car ==========")

class Car:
    def __init__(self, brand):
        self.brand = brand
        self.speed = 0            # every new car starts stopped

    def accelerate(self):
        self.speed = self.speed + 10
        print(self.brand, "is now going", self.speed, "km/h")

my_car = Car("Toyota")
my_car.accelerate()
my_car.accelerate()              # speed remembers its last value


# ===========================================================================
# EXAMPLE 4: a BankAccount that keeps a running balance
# ===========================================================================
print("\n========== EXAMPLE 4: BankAccount ==========")

class BankAccount:
    def __init__(self, owner):
        self.owner = owner
        self.balance = 0

    def deposit(self, amount):
        self.balance = self.balance + amount
        print(f"{self.owner} deposited {amount}. Balance: {self.balance}")

account = BankAccount("Rafi")
account.deposit(100)
account.deposit(50)


if __name__ == "__main__":
    print("\nA class is the blueprint; each object made from it has its own data.")
