"""
beginner_examples.py  (OOP / Composition)
=========================================

EXTRA easy examples for: composition ("has-a").

Idea: build a bigger thing out of smaller things.
      A Car HAS-A Engine. A House HAS rooms. A Computer HAS parts.
"""

# ===========================================================================
# EXAMPLE 1: a Car HAS-A Engine
# ===========================================================================
print("========== EXAMPLE 1: Car has an Engine ==========")

class Engine:
    def start(self):
        print("Engine starts: vroom!")

class Car:
    def __init__(self):
        self.engine = Engine()    # the car OWNS an engine object

    def drive(self):
        self.engine.start()       # the car asks its engine to do the work
        print("Car is driving.")

my_car = Car()
my_car.drive()


# ===========================================================================
# EXAMPLE 2: a Person HAS-A Pet
# ===========================================================================
print("\n========== EXAMPLE 2: Person has a Pet ==========")

class Pet:
    def __init__(self, name):
        self.name = name

    def play(self):
        print(self.name, "runs around happily!")

class Person:
    def __init__(self, person_name, pet):
        self.person_name = person_name
        self.pet = pet            # the person HAS a pet

    def play_with_pet(self):
        print(self.person_name, "plays with", self.pet.name)
        self.pet.play()

buddy = Pet("Buddy")
rafi = Person("Rafi", buddy)
rafi.play_with_pet()


# ===========================================================================
# EXAMPLE 3: a Computer is BUILT FROM parts
# ===========================================================================
print("\n========== EXAMPLE 3: Computer made of parts ==========")

class CPU:
    def run(self):
        print("CPU is calculating...")

class Screen:
    def show(self):
        print("Screen displays a picture.")

class Computer:
    def __init__(self):
        self.cpu = CPU()          # has a CPU
        self.screen = Screen()    # has a Screen

    def turn_on(self):
        self.cpu.run()
        self.screen.show()
        print("Computer is ready!")

Computer().turn_on()


if __name__ == "__main__":
    print("\nComposition = build big objects out of smaller helper objects.")
