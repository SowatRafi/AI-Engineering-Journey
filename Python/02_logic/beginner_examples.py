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


# ===========================================================================
# MORE EXAMPLES — functions
# ===========================================================================
print("\n========== MORE: FUNCTIONS ==========")

# Example 6: a function with two parameters
def rectangle_area(width, height):
    return width * height

print("Area of 4 x 3:", rectangle_area(4, 3))    # 12


# Example 7: a function can RETURN two things at once
def min_and_max(numbers):
    return min(numbers), max(numbers)

low, high = min_and_max([5, 2, 9, 1])
print("Lowest:", low, "Highest:", high)


# Example 8: one function using ANOTHER function
def is_odd(number):
    return not is_even(number)       # reuse is_even from earlier

print("Is 5 odd?", is_odd(5))


# Example 9: naming arguments makes a call easy to read (keyword arguments)
def make_coffee(size, sugar=0):
    print(f"{size} coffee with {sugar} sugar")

make_coffee("large", sugar=2)        # you can name the argument
make_coffee(size="small")            # order doesn't matter when you name them


# Example 10: a loop inside a function that adds up a list
def total(numbers):
    running = 0
    for n in numbers:
        running = running + n        # add each number to the running total
    return running

print("Total of [1, 2, 3, 4]:", total([1, 2, 3, 4]))


# ===========================================================================
# MORE EXAMPLES — scope
# ===========================================================================
print("\n========== MORE: SCOPE ==========")

# Two functions can each have their OWN variable with the same name.
# They do not affect each other.
def room_a():
    light = "on"
    print("Room A light is", light)

def room_b():
    light = "off"                    # separate from Room A's 'light'
    print("Room B light is", light)

room_a()
room_b()


# ===========================================================================
# EVEN SIMPLER EXAMPLES
# ===========================================================================
print("\n========== EVEN SIMPLER ==========")

# A function that prints a full sentence
def welcome(name):
    print("Welcome to the class, " + name + "!")

welcome("Rafi")

# A function that gives back True or False
def is_positive(number):
    return number > 0

print("Is 5 positive?", is_positive(5))      # True
print("Is -2 positive?", is_positive(-2))    # False

# A function that doubles a number
def double(number):
    return number * 2

print("Double of 8:", double(8))             # 16

# Call the same function again and again inside a loop
def cheer(times):
    for _ in range(times):
        print("Hooray!")

cheer(3)


if __name__ == "__main__":
    print("\nRemember: functions take inputs and return outputs.")
