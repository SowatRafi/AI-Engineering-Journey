"""
04_methods_static_class_factory.py
==================================

Topic: The kinds of methods — instance, static, class — plus method/constructor
overloading (the Pythonic way) and the factory pattern.

WHY THIS MATTERS
----------------
Not all methods need an instance. Knowing when to use @staticmethod vs.
@classmethod vs. a normal method, and how Python handles "overloading",
keeps your class APIs clean and expressive.
"""


class Temperature:
    """Demonstrates all three method types working together."""

    # Class attribute used by a class method below.
    ABSOLUTE_ZERO_C = -273.15

    def __init__(self, celsius: float) -> None:
        self.celsius = celsius

    # ---- INSTANCE METHOD: needs `self`, uses the object's data --------------
    def to_fahrenheit(self) -> float:
        return self.celsius * 9 / 5 + 32

    # ---- STATIC METHOD: no self, no cls — a plain function grouped in the
    #      class because it's logically related. Use for helpers/validators. --
    @staticmethod
    def is_valid_celsius(value: float) -> bool:
        """Doesn't touch instance or class state — purely a utility check."""
        return value >= Temperature.ABSOLUTE_ZERO_C

    # ---- CLASS METHOD: receives `cls` (the class). Ideal for ALTERNATIVE
    #      CONSTRUCTORS / factories that build and return instances. ----------
    @classmethod
    def from_fahrenheit(cls, fahrenheit: float) -> "Temperature":
        celsius = (fahrenheit - 32) * 5 / 9
        return cls(celsius)      # cls() == Temperature() (and works for subclasses)


print("--- Instance / static / class methods ---")
t = Temperature(25)
print("25C in F:", t.to_fahrenheit())                 # instance method
print("Is -300C valid?", Temperature.is_valid_celsius(-300))  # static method
print("From 212F:", Temperature.from_fahrenheit(212).celsius, "C")  # class method


# ===========================================================================
# METHOD OVERLOADING (the Pythonic way)
# ===========================================================================
# Python does NOT support multiple methods with the same name and different
# signatures (unlike Java/C++). If you define two, the second REPLACES the first.
# Instead, achieve "overloading" with default values or *args.
# ---------------------------------------------------------------------------
class Greeter:
    def greet(self, name: str = "there", *, formal: bool = False) -> str:
        """One flexible method handles several call shapes."""
        if formal:
            return f"Good day, {name}."
        return f"Hi, {name}!"


print("\n--- Method overloading via defaults/kwargs ---")
g = Greeter()
print(g.greet())                       # Hi, there!
print(g.greet("Rafi"))                 # Hi, Rafi!
print(g.greet("Dr. Rafi", formal=True))  # Good day, Dr. Rafi.


# For true type-based dispatch, functools.singledispatchmethod exists:
from functools import singledispatchmethod


class Formatter:
    @singledispatchmethod
    def format(self, value) -> str:
        return f"generic: {value}"

    @format.register
    def _(self, value: int) -> str:        # specialised for int
        return f"int in hex: {value:#x}"

    @format.register
    def _(self, value: list) -> str:       # specialised for list
        return f"list of {len(value)} items"


print("\n--- singledispatch (type-based overloading) ---")
f = Formatter()
print(f.format(255))            # int in hex: 0xff
print(f.format([1, 2, 3]))      # list of 3 items
print(f.format("hello"))        # generic: hello


# ===========================================================================
# THE FACTORY PATTERN
# ===========================================================================
# A factory is a function/method that decides WHICH object to build and returns
# it, hiding the construction details from the caller.
# ---------------------------------------------------------------------------
class Notification:
    def send(self, message: str) -> str:
        raise NotImplementedError


class EmailNotification(Notification):
    def send(self, message: str) -> str:
        return f"[EMAIL] {message}"


class SmsNotification(Notification):
    def send(self, message: str) -> str:
        return f"[SMS] {message}"


def notification_factory(channel: str) -> Notification:
    """Factory: pick and build the right Notification subclass by name."""
    channels = {"email": EmailNotification, "sms": SmsNotification}
    try:
        return channels[channel]()      # look up the class, then instantiate
    except KeyError:
        raise ValueError(f"Unknown channel: {channel!r}")


if __name__ == "__main__":
    print("\n--- Factory pattern ---")
    for kind in ("email", "sms"):
        notifier = notification_factory(kind)
        print(notifier.send("Deployment finished"))
    print("\nDone: you can choose the right method type and build via factories.")
