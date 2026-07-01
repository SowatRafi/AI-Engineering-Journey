"""
07_file_io.py
=============

Topic: File input/output — reading and writing files safely.

WHY THIS MATTERS
----------------
Data lives in files: datasets, configs, logs, prompts. Reading and writing them
correctly — with encodings and proper closing — is a daily task. The `with`
statement is the safe, idiomatic way to do it.

This script writes to (and reads back) files in its OWN folder, then cleans up.
"""

from pathlib import Path

# `pathlib` is the modern way to handle paths. `__file__` is this script's path;
# `.parent` is the folder it lives in. This keeps the demo self-contained and
# OS-independent (no hard-coded slashes).
HERE = Path(__file__).parent
demo_file = HERE / "sample_output.txt"    # `/` joins paths cross-platform


# ---------------------------------------------------------------------------
# 1. Writing with `with` (context manager) — auto-closes the file
# ---------------------------------------------------------------------------
# Mode "w" = write (creates or OVERWRITES). Always pass encoding="utf-8".
# The `with` block guarantees the file is closed even if an error occurs.
print("--- Writing ---")
lines = ["Phase 1: Foundations\n", "Phase 2: Software Engineering\n"]
with open(demo_file, "w", encoding="utf-8") as f:
    f.write("AI Engineering Journey\n")
    f.writelines(lines)           # write a list of strings (no newlines added)
print(f"Wrote to {demo_file.name}")


# ---------------------------------------------------------------------------
# 2. Appending — mode "a" adds to the end without erasing
# ---------------------------------------------------------------------------
with open(demo_file, "a", encoding="utf-8") as f:
    f.write("Phase 3: Data & ML\n")
print("Appended one line.")


# ---------------------------------------------------------------------------
# 3. Reading — three common patterns
# ---------------------------------------------------------------------------
print("\n--- Reading (whole file) ---")
with open(demo_file, "r", encoding="utf-8") as f:
    content = f.read()            # entire file as one string
print(content, end="")

print("\n--- Reading (line by line, memory-friendly) ---")
with open(demo_file, "r", encoding="utf-8") as f:
    # Iterating the file object reads ONE line at a time — ideal for big files.
    for number, line in enumerate(f, start=1):
        print(f"{number}: {line.rstrip()}")   # rstrip removes the trailing \n


# ---------------------------------------------------------------------------
# 4. The convenient pathlib shortcuts for small files
# ---------------------------------------------------------------------------
print("\n--- pathlib shortcuts ---")
quick_file = HERE / "quick.txt"
quick_file.write_text("one-liner via pathlib\n", encoding="utf-8")
print("Read back:", quick_file.read_text(encoding="utf-8").strip())


# ---------------------------------------------------------------------------
# 5. Safe reading — handle a missing file gracefully
# ---------------------------------------------------------------------------
print("\n--- Missing file handling ---")
try:
    with open(HERE / "does_not_exist.txt", "r", encoding="utf-8") as f:
        f.read()
except FileNotFoundError as error:
    print("Handled gracefully:", error)


# ---------------------------------------------------------------------------
# 6. Clean up the demo files so the folder stays tidy
# ---------------------------------------------------------------------------
if __name__ == "__main__":
    demo_file.unlink(missing_ok=True)   # delete if it exists
    quick_file.unlink(missing_ok=True)
    print("\nCleaned up demo files. Done: you can read and write files safely.")
