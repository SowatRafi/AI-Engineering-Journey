"""
05_object_inspection.py
======================

Built-ins that let your program ask questions ABOUT a value while it runs:
what type is it? does it have that attribute? can I call it?

Covers: type, isinstance, issubclass, callable, dir, vars, id, hash,
        hasattr, getattr, setattr, delattr, repr

WHY THIS MATTERS
----------------
Sometimes you need to check what you're dealing with before using it. These
tools help you inspect objects safely, which is also great for debugging.
"""


# A tiny class we can inspect throughout the file.
class Dog:
    species = "canine"          # shared by every dog

    def __init__(self, name):
        self.name = name        # unique to each dog

    def bark(self):
        return "Woof"


rex = Dog("Rex")


# ---------------------------------------------------------------------------
# type() — what kind of value is this?
# ---------------------------------------------------------------------------
print("--- type ---")
print(type(5))              # <class 'int'>
print(type("hi"))           # <class 'str'>
print(type(rex).__name__)   # Dog


# ---------------------------------------------------------------------------
# isinstance() — is this value of a certain type?
# ---------------------------------------------------------------------------
print("\n--- isinstance ---")
print(isinstance(5, int))           # True
print(isinstance("hi", int))        # False
print(isinstance(rex, Dog))         # True
# You can check several types at once by passing a tuple:
print(isinstance(5, (int, str)))    # True (it's an int OR a str)


# ---------------------------------------------------------------------------
# issubclass() — is one class based on another?
# ---------------------------------------------------------------------------
print("\n--- issubclass ---")
print(issubclass(bool, int))    # True  (in Python, True/False are special ints)
print(issubclass(str, int))     # False


# ---------------------------------------------------------------------------
# callable() — can I use () to call this?
# ---------------------------------------------------------------------------
print("\n--- callable ---")
print(callable(print))      # True  (print is a function)
print(callable(rex.bark))   # True  (a method)
print(callable(rex))        # False (a plain object)
print(callable(5))          # False


# ---------------------------------------------------------------------------
# dir() and vars() — what's inside an object?
# ---------------------------------------------------------------------------
print("\n--- dir / vars ---")
# vars() shows the object's own data as a dictionary.
print(vars(rex))            # {'name': 'Rex'}
# dir() lists the names you can use with a dot (methods and attributes).
print([name for name in dir(rex) if not name.startswith("_")])
# -> ['bark', 'name', 'species']


# ---------------------------------------------------------------------------
# hasattr / getattr / setattr / delattr — work with attributes by NAME
# ---------------------------------------------------------------------------
print("\n--- attributes by name ---")
print(hasattr(rex, "name"))         # True  -> does it have a 'name'?
print(getattr(rex, "name"))         # Rex   -> read it
print(getattr(rex, "age", 0))       # 0     -> a default when it's missing
setattr(rex, "age", 3)              # add a new attribute called 'age'
print(rex.age)                      # 3
delattr(rex, "age")                 # remove it again
print(hasattr(rex, "age"))          # False


# ---------------------------------------------------------------------------
# id() and hash() — an object's identity and its hash number
# ---------------------------------------------------------------------------
print("\n--- id / hash ---")
a = [1, 2]
b = a                       # b points to the SAME list as a
c = [1, 2]                  # c is a different list with equal values
print(id(a) == id(b))       # True  (same object)
print(id(a) == id(c))       # False (different objects)
print(hash("hello") == hash("hello"))   # True (same text -> same hash)


# ---------------------------------------------------------------------------
# repr() — the exact, detailed view of a value (great for debugging)
# ---------------------------------------------------------------------------
print("\n--- repr ---")
text = "line1\nline2"
print(str(text))            # shows a real line break
print(repr(text))           # 'line1\nline2'  -> reveals the hidden newline


if __name__ == "__main__":
    print("\nDone: inspect any object's type, contents, and attributes.")
