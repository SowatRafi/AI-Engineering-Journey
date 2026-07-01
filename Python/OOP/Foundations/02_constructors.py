"""
02_constructors.py
==================

Topic: Constructors — __init__, default vs. parameterized, and __new__ (briefly).

WHY THIS MATTERS
----------------
The constructor decides how an object starts life. Understanding default vs.
parameterized construction — and how Python simulates "overloaded" constructors
with default arguments and class methods — is core to designing clean classes.
"""


# ---------------------------------------------------------------------------
# 1. The default (implicit) constructor
# ---------------------------------------------------------------------------
class Empty:
    """If you write NO __init__, Python provides a default one that takes no
    arguments beyond self. You can still create the object."""


e = Empty()                      # works fine — nothing to initialise
print("--- Default constructor ---")
print("Created:", e)


# ---------------------------------------------------------------------------
# 2. A parameterized constructor
# ---------------------------------------------------------------------------
class Book:
    """A parameterized constructor REQUIRES arguments to build the object."""

    def __init__(self, title: str, author: str, pages: int) -> None:
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self) -> str:    # nicer print output (see Polymorphism module)
        return f"'{self.title}' by {self.author} ({self.pages}p)"


print("\n--- Parameterized constructor ---")
book = Book("Deep Learning", "Goodfellow", 775)
print(book)


# ---------------------------------------------------------------------------
# 3. Default parameter values = optional arguments
# ---------------------------------------------------------------------------
# Python has NO true constructor overloading (unlike Java/C++). Instead, DEFAULT
# VALUES let one constructor handle many call shapes.
class Server:
    def __init__(self, host: str, port: int = 8000, secure: bool = False) -> None:
        self.host = host
        self.port = port
        self.secure = secure

    def url(self) -> str:
        scheme = "https" if self.secure else "http"
        return f"{scheme}://{self.host}:{self.port}"


print("\n--- Defaults simulate optional args ---")
print(Server("localhost").url())                       # uses defaults
print(Server("api.site.com", 443, secure=True).url())  # all provided


# ---------------------------------------------------------------------------
# 4. Multiple ways to construct: alternative constructors via @classmethod
# ---------------------------------------------------------------------------
# This is the Pythonic answer to "constructor overloading": provide named
# class methods that build the object different ways. (More in the methods file.)
class Date:
    def __init__(self, year: int, month: int, day: int) -> None:
        self.year, self.month, self.day = year, month, day

    @classmethod
    def from_string(cls, text: str) -> "Date":
        """Alternative constructor: build a Date from 'YYYY-MM-DD'."""
        year, month, day = (int(part) for part in text.split("-"))
        return cls(year, month, day)   # cls is the class itself -> Date(...)

    def __str__(self) -> str:
        return f"{self.year:04d}-{self.month:02d}-{self.day:02d}"


print("\n--- Alternative constructor ---")
print("Normal:", Date(2026, 7, 1))
print("From string:", Date.from_string("2026-12-25"))


# ---------------------------------------------------------------------------
# 5. __new__ vs __init__ (advanced, awareness only)
# ---------------------------------------------------------------------------
# __new__ actually CREATES the object; __init__ INITIALISES the already-created
# object. You almost always customise __init__, not __new__. Shown for context.
class Widget:
    def __new__(cls, *args, **kwargs):
        print("[__new__] object is being allocated")
        return super().__new__(cls)

    def __init__(self, label: str) -> None:
        print("[__init__] object is being initialised")
        self.label = label


if __name__ == "__main__":
    print("\n--- __new__ then __init__ ---")
    w = Widget("save")
    print("Widget label:", w.label)
    print("\nDone: you can design flexible, well-initialised constructors.")
