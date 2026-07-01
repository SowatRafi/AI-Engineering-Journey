"""
01_error_handling.py
====================

Topic: Handling errors with try / except / else / finally, and raising your own.

WHY THIS MATTERS
----------------
Production code deals with unreliable inputs, networks, and files. The defining
skill of an AI Engineer is "building reliable systems out of unreliable
components" — and structured error handling is the foundation of that.
"""

# ---------------------------------------------------------------------------
# 1. The basic try / except
# ---------------------------------------------------------------------------
print("--- Basic try/except ---")
try:
    result = 10 / 0              # raises ZeroDivisionError
except ZeroDivisionError:
    print("You can't divide by zero — using a safe default instead.")
    result = 0
print("result =", result)


# ---------------------------------------------------------------------------
# 2. Catch SPECIFIC exceptions, and capture the error object
# ---------------------------------------------------------------------------
# Rule: catch the narrowest exception you can handle. A bare `except:` hides bugs.
print("\n--- Specific exceptions ---")
def to_int(text: str) -> int:
    try:
        return int(text)
    except ValueError as error:            # `as error` binds the exception object
        print(f"Could not convert {text!r}: {error}")
        return 0


print(to_int("42"))     # 42
print(to_int("oops"))   # 0 (handled)


# ---------------------------------------------------------------------------
# 3. Handling multiple error types
# ---------------------------------------------------------------------------
print("\n--- Multiple except blocks ---")
def safe_lookup(data: dict, key: str, index: int):
    try:
        return data[key][index]
    except KeyError:
        return f"No such key: {key!r}"
    except IndexError:
        return f"Index {index} out of range for {key!r}"
    except (TypeError, ValueError) as error:   # group related types in a tuple
        return f"Bad data: {error}"


sample = {"scores": [90, 85]}
print(safe_lookup(sample, "scores", 0))    # 90
print(safe_lookup(sample, "grades", 0))    # KeyError handled
print(safe_lookup(sample, "scores", 9))    # IndexError handled


# ---------------------------------------------------------------------------
# 4. else and finally
# ---------------------------------------------------------------------------
# - else:    runs only if NO exception happened (keep the "success" code here).
# - finally: ALWAYS runs — cleanup that must happen no matter what.
print("\n--- else / finally ---")
def read_number(text: str):
    try:
        value = int(text)
    except ValueError:
        print("Parse failed.")
    else:
        print("Parsed successfully:", value)
    finally:
        print("(finally: this always runs — e.g. close resources here)")


read_number("7")
read_number("bad")


# ---------------------------------------------------------------------------
# 5. Raising your own exceptions (fail loudly on invalid state)
# ---------------------------------------------------------------------------
print("\n--- Raising ---")
def set_temperature(value: float) -> float:
    """Validate an LLM temperature; refuse impossible values."""
    if not 0.0 <= value <= 2.0:
        # `raise` signals a problem the caller must deal with.
        raise ValueError(f"temperature must be in [0, 2], got {value}")
    return value


try:
    set_temperature(5.0)
except ValueError as error:
    print("Rejected:", error)


# ---------------------------------------------------------------------------
# 6. Custom exception classes for your own domain
# ---------------------------------------------------------------------------
class RetryLimitExceeded(Exception):
    """Raised when an operation fails after all retries.

    Defining custom exceptions lets callers catch YOUR specific error type
    without accidentally swallowing unrelated errors.
    """


def call_flaky_api(max_attempts: int = 3):
    for attempt in range(1, max_attempts + 1):
        print(f"Attempt {attempt}...")
        # Pretend it always fails, to demonstrate the raise.
    raise RetryLimitExceeded(f"Gave up after {max_attempts} attempts")


if __name__ == "__main__":
    print("\n--- Custom exception ---")
    try:
        call_flaky_api()
    except RetryLimitExceeded as error:
        print("Caught custom error:", error)
    print("\nDone: your code can now fail safely and loudly when it should.")
