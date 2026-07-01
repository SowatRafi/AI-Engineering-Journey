"""
composition.py
==============

OOP Principle: COMPOSITION — modelling "has-a" relationships by building objects
out of other objects.

WHY THIS MATTERS
----------------
Inheritance models "is-a" (a Cat IS-A Animal). Composition models "has-a"
(a Car HAS-A Engine). The widely-taught guideline "favour composition over
inheritance" applies because composition is more flexible: you can swap parts
at runtime and avoid rigid, deep class hierarchies.
"""


# ---------------------------------------------------------------------------
# 1. The parts (components) — each does one job well
# ---------------------------------------------------------------------------
class Engine:
    """A component. It knows nothing about cars."""

    def __init__(self, horsepower: int) -> None:
        self.horsepower = horsepower

    def start(self) -> str:
        return f"Engine ({self.horsepower}hp) roars to life."


class GpsUnit:
    """Another independent component."""

    def navigate(self, destination: str) -> str:
        return f"Routing to {destination}."


# ---------------------------------------------------------------------------
# 2. The whole — a Car HAS-A Engine and HAS-A GpsUnit
# ---------------------------------------------------------------------------
class Car:
    """Composed of parts. The Car delegates work to the objects it contains."""

    def __init__(self, model: str, horsepower: int) -> None:
        self.model = model
        # Composition: the Car OWNS these component objects as attributes.
        self.engine = Engine(horsepower)
        self.gps = GpsUnit()

    def start(self) -> str:
        # DELEGATION: forward the request to the relevant component.
        return f"{self.model}: {self.engine.start()}"

    def drive_to(self, place: str) -> str:
        return f"{self.model}: {self.gps.navigate(place)}"


print("--- Composition (has-a) ---")
car = Car("Model-X", 480)
print(car.start())
print(car.drive_to("Dhaka"))
print("Engine object it owns:", car.engine.horsepower, "hp")


# ---------------------------------------------------------------------------
# 3. Flexibility: inject/swap components at runtime (dependency injection)
# ---------------------------------------------------------------------------
# Because parts are separate objects, we can pass them in and swap them out —
# something rigid inheritance can't do as cleanly.
class Logger:
    def log(self, message: str) -> None:
        print(f"[LOG] {message}")


class SilentLogger:
    def log(self, message: str) -> None:
        pass                     # same interface, different behaviour


class Service:
    def __init__(self, logger) -> None:
        # The Service HAS-A logger, but doesn't care which kind — just its API.
        self.logger = logger

    def run(self) -> None:
        self.logger.log("Service started")
        self.logger.log("Service finished")


print("\n--- Swappable components ---")
print("With a real logger:")
Service(Logger()).run()
print("With a silent logger (nothing prints between the lines):")
Service(SilentLogger()).run()


# ---------------------------------------------------------------------------
# 4. Composition vs. inheritance — the mental model
# ---------------------------------------------------------------------------
# INHERITANCE  : SportsCar IS-A  Car            (specialisation of a type)
# COMPOSITION  : Car        HAS-A Engine         (assembly from parts)
#
# Rule of thumb: reach for composition first. Use inheritance only when there is
# a genuine, stable "is-a" relationship AND you want to inherit behaviour.
if __name__ == "__main__":
    print("\nDone: build complex objects by composing simple, swappable parts.")
