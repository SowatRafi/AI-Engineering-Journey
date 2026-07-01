"""
beginner_examples.py  (02_logic)
================================

EXTRA easy examples for: functions and scope.
A function is a mini-machine: you give it something, it gives something back.
"""

# ===========================================================================
# FUNCTIONS — reusable mini-machines
# ===========================================================================
print("========== FUNCTIONS ==========")

# Example 1: a function that says hello
def say_hello():
    print("Hello there!")

say_hello()          # call it to run it
say_hello()          # call it again — no copy-paste needed


# Example 2: a function that takes an input (a "parameter")
def greet(person):
    print("Hi", person)

greet("Rafi")
greet("Sara")


# Example 3: a function that GIVES BACK a value with 'return'
def add(a, b):
    return a + b

result = add(2, 3)   # result now holds 5
print("2 + 3 =", result)
print("10 + 7 =", add(10, 7))


# Example 4: a function with a default value
def make_tea(sugar=1):
    print(f"Tea with {sugar} sugar(s)")

make_tea()           # uses the default: 1
make_tea(3)          # you chose 3


# Example 5: a small helper you can reuse
def is_even(number):
    return number % 2 == 0        # True if there is no remainder

print("Is 4 even?", is_even(4))
print("Is 7 even?", is_even(7))


# ===========================================================================
# SCOPE — where a variable "lives"
# ===========================================================================
print("\n========== SCOPE ==========")

# A variable made INSIDE a function only exists inside that function.
def make_secret():
    secret = "inside only"        # this lives only in here
    print("Inside the function:", secret)

make_secret()
# print(secret)   # <- this would ERROR: 'secret' does not exist out here

# A variable made OUTSIDE (at the top) can be READ inside a function.
shop_name = "Corner Store"        # this is a "global" variable

def show_shop():
    print("The shop is:", shop_name)   # we can read it here

show_shop()


if __name__ == "__main__":
    print("\nRemember: functions take inputs and return outputs.")
