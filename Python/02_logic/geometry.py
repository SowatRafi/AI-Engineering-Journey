"""
geometry.py
===========

A small HELPER MODULE, imported by 03_modules_and_imports.py to demonstrate
how importing works. A "module" is simply a .py file whose names (functions,
classes, constants) can be reused elsewhere via `import`.

WHY THIS MATTERS
----------------
Real projects are split across many files. Modules let you organise code by
responsibility and reuse it without copy-pasting.
"""

PI = 3.141592653589793      # a module-level constant


def circle_area(radius: float) -> float:
    """Return the area of a circle with the given radius."""
    return PI * radius ** 2


def rectangle_area(width: float, height: float) -> float:
    """Return the area of a rectangle."""
    return width * height


# This guard means: only run the demo when the file is executed DIRECTLY,
# not when it is imported by another module. See 03_modules_and_imports.py.
if __name__ == "__main__":
    print("Self-test of geometry module:")
    print("circle_area(2) =", circle_area(2))
    print("rectangle_area(3, 4) =", rectangle_area(3, 4))
