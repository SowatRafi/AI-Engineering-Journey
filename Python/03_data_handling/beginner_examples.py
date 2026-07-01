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


# ===========================================================================
# MORE EXAMPLES — lists
# ===========================================================================
print("\n========== MORE: LISTS ==========")

scores = [50, 90, 70, 60]
print("Sorted:", sorted(scores))         # [50, 60, 70, 90]
print("Highest:", max(scores))           # 90
print("Total:", sum(scores))             # 270
print("First two:", scores[0:2])         # [50, 90]  (slicing)


# ===========================================================================
# MORE EXAMPLES — dictionaries
# ===========================================================================
print("\n========== MORE: DICTIONARIES ==========")

prices = {"apple": 3, "banana": 2}
# .get() is safe: it returns a default instead of crashing if the key is missing.
print("Apple price:", prices.get("apple"))       # 3
print("Mango price:", prices.get("mango", 0))    # 0  (not in the dict)
print("Do we sell banana?", "banana" in prices)  # True


# ===========================================================================
# MORE EXAMPLES — sets
# ===========================================================================
print("\n========== MORE: SETS ==========")

morning = {"eggs", "milk", "bread"}
evening = {"milk", "rice"}
print("In both lists:", morning & evening)   # {'milk'}   (shared items)
print("Everything:", morning | evening)      # all items from both


# ===========================================================================
# MORE EXAMPLES — tuples
# ===========================================================================
print("\n========== MORE: TUPLES ==========")

def divide(a, b):
    return a // b, a % b             # returns a tuple: (quotient, remainder)

whole, left_over = divide(17, 5)
print("17 / 5 ->", whole, "remainder", left_over)   # 3 remainder 2


# ===========================================================================
# MORE EXAMPLES — strings
# ===========================================================================
print("\n========== MORE: STRINGS ==========")

email = "  Rafi@Example.com  "
clean = email.strip().lower()        # remove spaces, then make it lowercase
print("Cleaned email:", clean)
print("Is it a .com address?", clean.endswith(".com"))
print("How many 'a' in banana?", "banana".count("a"))   # 3

csv_line = "red,green,blue"
print("Split by comma:", csv_line.split(","))           # ['red', 'green', 'blue']


# ===========================================================================
# EVEN SIMPLER EXAMPLES
# ===========================================================================
print("\n========== EVEN SIMPLER ==========")

# Go through a list and print each item
pets = ["cat", "dog", "fish"]
for pet in pets:
    print("I have a", pet)

# Change one item in a list using its position
pets[0] = "rabbit"
print("Updated pets:", pets)             # ['rabbit', 'dog', 'fish']

# Print just the names (keys) of a dictionary
ages = {"Ana": 30, "Ben": 25}
for name in ages:
    print("Name:", name)

# Check if a word is inside a sentence
sentence = "python is fun"
print("Has 'fun'?", "fun" in sentence)   # True

# Count how many items are in a list
print("Number of pets:", len(pets))      # 3


if __name__ == "__main__":
    print("\nPick the container that fits your data: list, dict, set, or tuple.")
