"""
03_modules_and_imports.py
=========================

Topic: Modules, imports, and the `if __name__ == "__main__"` idiom.

WHY THIS MATTERS
----------------
Code lives in many files. `import` is how one file uses another's functions and
classes. Knowing the different import styles — and the __name__ guard — is
essential to structuring any project beyond a single script.

Run from THIS folder so the local `geometry.py` is found:

    python 03_modules_and_imports.py
"""

# ---------------------------------------------------------------------------
# 1. Importing our own local module (geometry.py sits next to this file)
# ---------------------------------------------------------------------------
# Style A: import the whole module, then use `module.name`. Most readable —
# the reader always sees where a function came from.
import geometry

print("--- import geometry ---")
print("Circle area:", geometry.circle_area(5))
print("PI constant:", geometry.PI)


# Style B: import specific names directly into this file's namespace.
from geometry import rectangle_area

print("\n--- from geometry import rectangle_area ---")
print("Rectangle area:", rectangle_area(4, 6))


# Style C: import with an alias (common for long/standard names).
import geometry as geo

print("\n--- aliased import ---")
print("Aliased circle area:", geo.circle_area(1))


# ---------------------------------------------------------------------------
# 2. Importing from the standard library
# ---------------------------------------------------------------------------
# Python ships with a huge "standard library" — batteries included.
import math
from datetime import date

print("\n--- standard library ---")
print("math.sqrt(144):", math.sqrt(144))
print("math.pi:", math.pi)
print("Today is:", date.today())


# ---------------------------------------------------------------------------
# 3. The __name__ == "__main__" idiom, explained
# ---------------------------------------------------------------------------
# Every module has a built-in variable `__name__`.
#   - When you RUN a file directly:      __name__ == "__main__"
#   - When the file is IMPORTED:          __name__ == the module's name
#
# This lets a file act BOTH as an importable library AND as a runnable script,
# without its demo code firing on import.
print("\n--- __name__ ---")
print("This file's __name__ is:", __name__)


def main() -> None:
    """Conventional entry point. Keeping logic in main() keeps the top level
    clean and makes the code importable without side effects."""
    print("\nRunning main(): everything above imported cleanly.")


if __name__ == "__main__":
    main()
