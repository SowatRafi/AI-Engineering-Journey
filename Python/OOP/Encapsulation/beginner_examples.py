"""
beginner_examples.py  (OOP / Encapsulation)
===========================================

EXTRA easy examples for: encapsulation (hiding and protecting data).

Idea: some data should not be changed directly from outside.
      We hide it and only allow safe ways to change it.
      (Like an ATM: you can't grab the cash drawer — you use buttons.)
"""

# ===========================================================================
# EXAMPLE 1: a piggy bank you can add to, but not secretly empty
# ===========================================================================
print("========== EXAMPLE 1: PiggyBank ==========")

class PiggyBank:
    def __init__(self):
        self.__coins = 0          # the two underscores mean "private/hidden"

    def add_coin(self):
        self.__coins = self.__coins + 1

    def count(self):
        return self.__coins       # a safe way to LOOK at the hidden value

bank = PiggyBank()
bank.add_coin()
bank.add_coin()
print("Coins inside:", bank.count())   # 2 — through the safe method


# ===========================================================================
# EXAMPLE 2: protecting a password
# ===========================================================================
print("\n========== EXAMPLE 2: User password ==========")

class User:
    def __init__(self, name, password):
        self.name = name              # public: fine to see
        self.__password = password    # private: hidden

    def check_password(self, guess):
        # Outsiders can't read the password, but they can TEST a guess.
        return guess == self.__password

user = User("rafi", "secret123")
print("Name:", user.name)
print("Correct guess?", user.check_password("secret123"))
print("Wrong guess?", user.check_password("abc"))


# ===========================================================================
# EXAMPLE 3: a getter and setter that VALIDATE the value
# ===========================================================================
print("\n========== EXAMPLE 3: safe age with @property ==========")

class Student:
    def __init__(self, age):
        self._age = age

    @property                 # this makes 'age' readable like: student.age
    def age(self):
        return self._age

    @age.setter               # this runs when you do: student.age = 15
    def age(self, value):
        if value < 0:
            print("Age can't be negative! Ignoring.")
        else:
            self._age = value

student = Student(20)
print("Age:", student.age)
student.age = 21              # allowed
print("New age:", student.age)
student.age = -5             # blocked by our check
print("Age after bad try:", student.age)


if __name__ == "__main__":
    print("\nHide sensitive data; expose only safe ways to use it.")
