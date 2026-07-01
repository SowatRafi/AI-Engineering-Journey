"""
beginner_examples.py  (01_basics)
=================================

EXTRA easy examples for: variables, types, conditionals, and loops.
Everything here uses everyday things (age, snacks, money) and lots of small,
separate examples so each idea sinks in. Read top to bottom and run it.
"""

# ===========================================================================
# VARIABLES — a variable is just a labeled box that holds a value
# ===========================================================================
print("========== VARIABLES ==========")

# Example 1: your name and age
name = "Rafi"
age = 27
print("My name is", name)
print("My age is", age)

# Example 2: change a variable's value later
score = 10
print("Score at start:", score)
score = 20            # we put a new value in the same box
print("Score now:", score)

# Example 3: doing simple math with variables
apples = 3
oranges = 2
fruit_total = apples + oranges
print("Total fruit:", fruit_total)


# ===========================================================================
# TYPES — every value has a kind: text, whole number, decimal, True/False
# ===========================================================================
print("\n========== TYPES ==========")

word = "hello"        # str  -> text (always in quotes)
count = 5             # int  -> whole number
price = 9.99          # float -> decimal number
is_open = True        # bool -> True or False

print(word, "is a", type(word).__name__)
print(count, "is a", type(count).__name__)
print(price, "is a", type(price).__name__)
print(is_open, "is a", type(is_open).__name__)

# Turning text into a number so we can add it (very common!)
age_text = "30"                 # this is text, not a number
age_number = int(age_text)      # convert text -> number
print("Next year you are", age_number + 1)


# ===========================================================================
# CONDITIONALS — do different things depending on a yes/no question
# ===========================================================================
print("\n========== CONDITIONALS ==========")

# Example 1: are you old enough?
age = 18
if age >= 18:
    print("You are an adult.")
else:
    print("You are a minor.")

# Example 2: traffic light
light = "red"
if light == "green":
    print("Go!")
elif light == "yellow":
    print("Slow down.")
else:
    print("Stop.")

# Example 3: is a number positive, negative, or zero?
number = -4
if number > 0:
    print(number, "is positive")
elif number < 0:
    print(number, "is negative")
else:
    print(number, "is zero")

# Example 4: check two things at once with 'and'
money = 50
is_open = True
if money >= 20 and is_open:
    print("You can buy the ticket.")


# ===========================================================================
# LOOPS — repeat something without copy-pasting
# ===========================================================================
print("\n========== LOOPS ==========")

# Example 1: count from 1 to 5
for number in range(1, 6):
    print("Count:", number)

# Example 2: greet every friend in a list
friends = ["Ana", "Ben", "Cara"]
for friend in friends:
    print("Hi", friend)

# Example 3: add up a shopping list total
prices = [3, 5, 2]
total = 0
for p in prices:
    total = total + p            # add each price to the running total
print("You owe:", total)

# Example 4: a while-loop counts down like a rocket
seconds = 3
while seconds > 0:
    print(seconds, "...")
    seconds = seconds - 1        # get closer to 0 each time
print("Blast off!")


if __name__ == "__main__":
    print("\nGreat job — these are the four building blocks of every program.")
