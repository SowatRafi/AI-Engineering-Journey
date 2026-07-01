"""
abstraction.py
==============

OOP Principle: ABSTRACTION — expose WHAT an object does while hiding HOW it does
it, and define contracts that subclasses must fulfil.

WHY THIS MATTERS
----------------
Abstraction lets you program to an interface, not an implementation. Callers
depend on a stable contract (e.g. "every PaymentProcessor has pay()"), so you
can swap or add implementations without changing the calling code. In Python
this is done with the `abc` module (Abstract Base Classes).
"""

from abc import ABC, abstractmethod


# ===========================================================================
# 1. An Abstract Base Class defines a CONTRACT
# ===========================================================================
class PaymentProcessor(ABC):
    """Abstract base class. You CANNOT instantiate it directly.

    Any concrete subclass MUST implement every @abstractmethod, or it too
    remains abstract and cannot be instantiated. This enforces the contract.
    """

    @abstractmethod
    def pay(self, amount: float) -> str:
        """Subclasses define HOW payment happens; callers only need to know it does."""
        ...

    @abstractmethod
    def refund(self, amount: float) -> str:
        ...

    # An abstract class CAN also provide concrete, shared behaviour.
    def receipt(self, amount: float) -> str:
        return f"Receipt: {amount:.2f} processed via {type(self).__name__}"


# ===========================================================================
# 2. Concrete implementations fulfil the contract
# ===========================================================================
class CreditCardProcessor(PaymentProcessor):
    def pay(self, amount: float) -> str:
        # HOW is hidden from the caller — could involve a gateway, tokens, etc.
        return f"Charged {amount:.2f} to a credit card."

    def refund(self, amount: float) -> str:
        return f"Refunded {amount:.2f} to a credit card."


class PayPalProcessor(PaymentProcessor):
    def pay(self, amount: float) -> str:
        return f"Sent {amount:.2f} via PayPal."

    def refund(self, amount: float) -> str:
        return f"Returned {amount:.2f} via PayPal."


# ===========================================================================
# 3. Programming to the abstraction
# ===========================================================================
def checkout(processor: PaymentProcessor, amount: float) -> None:
    """This function depends only on the ABSTRACT contract, never on a concrete
    class. Add a new processor tomorrow and this code needs zero changes."""
    print(processor.pay(amount))
    print(processor.receipt(amount))   # inherited concrete method


print("--- Abstraction with ABCs ---")
for processor in (CreditCardProcessor(), PayPalProcessor()):
    checkout(processor, 49.99)
    print()


# ===========================================================================
# 4. The contract is ENFORCED at instantiation time
# ===========================================================================
print("--- Contract enforcement ---")

# 4a. You cannot instantiate the abstract base class itself.
try:
    PaymentProcessor()                    # raises TypeError
except TypeError as error:
    print("Cannot instantiate abstract base:", error)

# 4b. A subclass that FORGETS an abstract method stays abstract.
class BrokenProcessor(PaymentProcessor):
    def pay(self, amount: float) -> str:  # implements pay but NOT refund
        return "paid"

try:
    BrokenProcessor()                     # raises TypeError: refund not implemented
except TypeError as error:
    print("Incomplete subclass rejected:", error)


if __name__ == "__main__":
    print("\nDone: abstraction hides implementation and enforces clean contracts.")
