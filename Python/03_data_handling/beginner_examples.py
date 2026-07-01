"""
beginner_examples.py  (03_data_handling)
========================================

EXTRA easy examples for: lists, dicts, sets, tuples, and strings.
Think of these as different kinds of containers for your data.
"""

# ===========================================================================
# LISTS — an ordered container you can change (like a to-do list)
# ===========================================================================
print("========== LISTS ==========")

fruits = ["apple", "banana", "cherry"]
print("My fruits:", fruits)
print("First fruit:", fruits[0])      # counting starts at 0!
print("Last fruit:", fruits[-1])      # -1 means "last"

fruits.append("mango")                # add to the end
print("After adding mango:", fruits)

fruits.remove("banana")               # take one out
print("After removing banana:", fruits)

print("How many fruits?", len(fruits))
print("Is apple in the list?", "apple" in fruits)


# ===========================================================================
# DICTIONARIES — labeled data (like a contact card)
# ===========================================================================
print("\n========== DICTIONARIES ==========")

person = {
    "name": "Rafi",
    "age": 27,
    "city": "Dhaka",
}
print("Name:", person["name"])       # look up by its label ("key")
print("City:", person["city"])

person["job"] = "student"            # add a new label
person["age"] = 28                   # change an existing one
print("Updated card:", person)

# Go through every label and value
for key, value in person.items():
    print(f"{key} -> {value}")


# ===========================================================================
# SETS — a bag of UNIQUE things (duplicates disappear)
# ===========================================================================
print("\n========== SETS ==========")

colors = {"red", "blue", "red", "green"}   # "red" appears once
print("Unique colors:", colors)

colors.add("yellow")
print("After adding yellow:", colors)
print("Do we have blue?", "blue" in colors)

# Handy trick: remove duplicates from a list
numbers = [1, 2, 2, 3, 3, 3]
print("Without duplicates:", set(numbers))


# ===========================================================================
# TUPLES — a fixed container that cannot change (like coordinates)
# ===========================================================================
print("\n========== TUPLES ==========")

point = (4, 5)                        # an (x, y) pair
print("x is", point[0], "and y is", point[1])

# You can "unpack" a tuple into separate variables
x, y = point
print("Unpacked -> x:", x, "y:", y)

# Tuples can't be changed — this keeps important data safe
birthday = (1998, 5, 20)              # year, month, day
print("Birth year:", birthday[0])


# ===========================================================================
# STRINGS — text, with handy built-in tools
# ===========================================================================
print("\n========== STRINGS ==========")

message = "Hello World"
print("Uppercase:", message.upper())
print("Lowercase:", message.lower())
print("Length:", len(message))
print("Replace:", message.replace("World", "Rafi"))

# f-strings: drop variables straight into text with { }
name = "Sara"
age = 25
print(f"{name} is {age} years old.")

# Split text into a list, and join a list into text
sentence = "I love python"
words = sentence.split()              # -> ['I', 'love', 'python']
print("Words:", words)
print("Joined with dashes:", "-".join(words))


if __name__ == "__main__":
    print("\nPick the container that fits your data: list, dict, set, or tuple.")
