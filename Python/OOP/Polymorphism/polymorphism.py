"""
polymorphism.py
===============

OOP Principle: POLYMORPHISM — "many forms". The same call works across different
types, each responding in its own way. Covers method overriding, duck typing,
and OPERATOR OVERLOADING via dunder (double-underscore) methods.

WHY THIS MATTERS
----------------
Polymorphism lets you write general code ("draw every shape", "print every
report") that automatically does the right thing for each concrete type. It is
what makes code extensible without giant if/elif chains.
"""


# ===========================================================================
# 1. Method overriding + polymorphic loops
# ===========================================================================
class Shape:
    def area(self) -> float:
        raise NotImplementedError

    def name(self) -> str:
        return type(self).__name__


class Circle(Shape):
    def __init__(self, radius: float) -> None:
        self.radius = radius

    def area(self) -> float:                 # each subclass overrides area()
        return 3.14159 * self.radius ** 2


class Triangle(Shape):
    def __init__(self, base: float, height: float) -> None:
        self.base, self.height = base, height

    def area(self) -> float:
        return 0.5 * self.base * self.height


print("--- Polymorphic loop ---")
# ONE loop handles ANY Shape subclass — the correct area() is chosen at runtime.
shapes: list[Shape] = [Circle(2), Triangle(3, 4)]
for shape in shapes:
    print(f"{shape.name()} area = {shape.area():.2f}")


# ===========================================================================
# 2. Duck typing: "if it walks like a duck and quacks like a duck..."
# ===========================================================================
# Python doesn't require a shared base class — it only cares that the needed
# method EXISTS. Any object with .render() works here.
class HtmlReport:
    def render(self) -> str:
        return "<h1>Report</h1>"


class MarkdownReport:
    def render(self) -> str:
        return "# Report"


def publish(document) -> None:
    """Accepts ANY object that has a .render() method — no inheritance needed."""
    print("Published:", document.render())


print("\n--- Duck typing ---")
publish(HtmlReport())
publish(MarkdownReport())


# ===========================================================================
# 3. OPERATOR OVERLOADING via dunder methods
# ===========================================================================
# Operators like +, ==, len(), and print() call special "dunder" methods behind
# the scenes. Implement them to make YOUR objects behave like built-in types.
class Vector:
    """A 2D vector supporting math operators through dunder methods."""

    def __init__(self, x: float, y: float) -> None:
        self.x, self.y = x, y

    # __repr__: unambiguous developer-facing text (used in the REPL, debuggers).
    def __repr__(self) -> str:
        return f"Vector({self.x}, {self.y})"

    # __str__: friendly text for end users (used by print() and str()).
    def __str__(self) -> str:
        return f"({self.x}, {self.y})"

    # __add__: powers the  +  operator ->  v1 + v2
    def __add__(self, other: "Vector") -> "Vector":
        return Vector(self.x + other.x, self.y + other.y)

    # __mul__: powers  *  with a scalar ->  v * 3
    def __mul__(self, scalar: float) -> "Vector":
        return Vector(self.x * scalar, self.y * scalar)

    # __eq__: powers  ==  (value equality instead of identity)
    def __eq__(self, other: object) -> bool:
        return isinstance(other, Vector) and (self.x, self.y) == (other.x, other.y)

    # __abs__: powers  abs(v)  -> magnitude/length
    def __abs__(self) -> float:
        return (self.x ** 2 + self.y ** 2) ** 0.5


print("\n--- Operator overloading (Vector) ---")
v1 = Vector(1, 2)
v2 = Vector(3, 4)
print("v1 + v2 =", v1 + v2)         # uses __add__ then __str__
print("v1 * 3  =", v1 * 3)          # uses __mul__
print("v1 == Vector(1, 2)?", v1 == Vector(1, 2))   # uses __eq__
print("abs(v2) =", abs(v2))         # uses __abs__
print("repr:", repr(v1))            # uses __repr__


# ===========================================================================
# 4. Container-like dunders: __len__, __getitem__
# ===========================================================================
class Playlist:
    """Make a custom object behave like a sequence."""

    def __init__(self, songs: list[str]) -> None:
        self._songs = songs

    def __len__(self) -> int:                 # enables len(playlist)
        return len(self._songs)

    def __getitem__(self, index: int) -> str:  # enables playlist[i] AND iteration
        return self._songs[index]


if __name__ == "__main__":
    print("\n--- Container dunders ---")
    playlist = Playlist(["Song A", "Song B", "Song C"])
    print("len(playlist):", len(playlist))     # __len__
    print("playlist[1]:", playlist[1])         # __getitem__
    for song in playlist:                      # __getitem__ makes it iterable
        print("  playing:", song)
    print("\nDone: same interface, many behaviours — that's polymorphism.")
