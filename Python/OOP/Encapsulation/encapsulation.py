"""
encapsulation.py
================

OOP Principle: ENCAPSULATION — bundling data with the methods that guard it,
and controlling access to internal state.

WHY THIS MATTERS
----------------
Encapsulation protects an object's invariants (rules that must stay true, e.g.
"balance is never negative"). By exposing a controlled interface and hiding raw
internals, you can change the implementation later without breaking callers.

PYTHON'S CONVENTION
-------------------
Python has no truly `private` keyword. It uses naming conventions instead:
  - name       -> public (part of the API)
  - _name      -> "protected": internal, please don't touch (by convention)
  - __name     -> "private": triggers NAME MANGLING to _ClassName__name,
                   which discourages accidental access/override.
"""


class BankAccount:
    """Encapsulates a balance so it can only change through valid operations."""

    def __init__(self, owner: str, opening_balance: float = 0.0) -> None:
        self.owner = owner                 # public: safe to read/write freely
        self._transaction_count = 0        # protected: internal bookkeeping
        self.__balance = 0.0               # private: guarded state
        if opening_balance > 0:
            self.deposit(opening_balance)  # go through the validated path

    # ---- Controlled mutators enforce the rules --------------------------------
    def deposit(self, amount: float) -> None:
        if amount <= 0:
            raise ValueError("Deposit must be positive.")
        self.__balance += amount
        self._transaction_count += 1

    def withdraw(self, amount: float) -> None:
        if amount <= 0:
            raise ValueError("Withdrawal must be positive.")
        if amount > self.__balance:
            raise ValueError("Insufficient funds.")   # invariant protected!
        self.__balance -= amount
        self._transaction_count += 1

    # ---- A read-only VIEW of the private state --------------------------------
    def get_balance(self) -> float:
        """A getter method — read access without allowing direct assignment."""
        return self.__balance


print("--- Encapsulated BankAccount ---")
account = BankAccount("Rafi", 100)
account.deposit(50)
account.withdraw(30)
print("Balance:", account.get_balance())        # 120

# The invariant is enforced — illegal operations are rejected, not silently done.
try:
    account.withdraw(9999)
except ValueError as error:
    print("Blocked:", error)


# ---------------------------------------------------------------------------
# Name mangling demonstration
# ---------------------------------------------------------------------------
print("\n--- Name mangling ---")
# You cannot reach __balance by its written name from outside...
print("Has attribute '__balance'?", hasattr(account, "__balance"))   # False
# ...because Python mangled it to _BankAccount__balance.
print("Mangled name exists?", hasattr(account, "_BankAccount__balance"))  # True
# (You *can* still reach it if you insist — Python trusts you, but signals intent.)


# ===========================================================================
# THE PYTHONIC WAY: @property for getters/setters
# ===========================================================================
# Instead of verbose get_x()/set_x() methods, `@property` lets an attribute-style
# access run validation behind the scenes. Callers write `obj.temp = 5`, but your
# setter still guards the value. This is the preferred Python idiom.
# ---------------------------------------------------------------------------
class Thermostat:
    def __init__(self, celsius: float = 20.0) -> None:
        self._celsius = celsius            # the backing (protected) field

    @property
    def celsius(self) -> float:
        """The GETTER — accessed as `thermostat.celsius` (no parentheses)."""
        return self._celsius

    @celsius.setter
    def celsius(self, value: float) -> None:
        """The SETTER — runs validation on `thermostat.celsius = value`."""
        if value < -273.15:
            raise ValueError("Below absolute zero is impossible.")
        self._celsius = value

    @property
    def fahrenheit(self) -> float:
        """A COMPUTED, read-only property (no setter defined)."""
        return self._celsius * 9 / 5 + 32


if __name__ == "__main__":
    print("\n--- @property getters/setters ---")
    thermostat = Thermostat()
    thermostat.celsius = 25                # looks like an attribute, runs the setter
    print("Celsius:", thermostat.celsius)  # runs the getter
    print("Fahrenheit (computed):", thermostat.fahrenheit)

    try:
        thermostat.celsius = -500          # rejected by the setter's validation
    except ValueError as error:
        print("Setter blocked bad value:", error)

    print("\nDone: encapsulation guards invariants; @property is the clean way.")
