"""
07_io_and_dynamic.py
===================

Built-ins that talk to the outside world (screen, keyboard, files), plus a few
"dynamic" ones that run code stored in text.

Covers: print, input, open, eval, exec, compile, globals, locals,
        help, breakpoint, __import__

WHY THIS MATTERS
----------------
Programs need to show output, read input, and use files. A few of these
(eval/exec) are powerful but risky, so we explain when NOT to use them.
"""

from pathlib import Path


# ---------------------------------------------------------------------------
# print() — show text, with some handy options
# ---------------------------------------------------------------------------
print("--- print ---")
print("a", "b", "c")            # words separated by spaces (the default)
print("a", "b", sep="-")        # choose your own separator -> a-b
print("no newline", end=" ")    # stay on the same line...
print("same line")              # ...this continues it


# ---------------------------------------------------------------------------
# input() — read what the user types (SHOWN, not run here)
# ---------------------------------------------------------------------------
print("\n--- input ---")
# input() pauses and waits for the user to type, so we don't call it here
# (it would freeze an automatic run). In your own program you'd write:
#
#     name = input("Your name: ")     # always gives back text
#     age = int(input("Your age: "))  # convert if you need a number
#
print("(input() is shown in comments so this file runs without pausing.)")


# ---------------------------------------------------------------------------
# open() — write to and read from a file
# ---------------------------------------------------------------------------
print("\n--- open ---")
demo = Path(__file__).parent / "_demo.txt"

# "w" means write. The 'with' block closes the file automatically when done.
with open(demo, "w", encoding="utf-8") as f:
    f.write("hello from a file\n")

# "r" means read.
with open(demo, "r", encoding="utf-8") as f:
    print(f.read().strip())     # hello from a file

demo.unlink()                   # delete the demo file to tidy up


# ---------------------------------------------------------------------------
# eval() and exec() — run code stored in text (POWERFUL BUT RISKY)
# ---------------------------------------------------------------------------
print("\n--- eval / exec ---")
print(eval("2 + 3 * 4"))        # 14  -> eval works out ONE expression

box = {}
exec("total = 1 + 2 + 3", box)  # exec runs statements; we catch results in a dict
print(box["total"])             # 6

# WARNING: never run eval()/exec() on text from a user or the internet — it
# could run harmful code. To safely read a simple value (list, number, dict),
# use ast.literal_eval instead, which reads data but never runs commands:
import ast
print(ast.literal_eval("[1, 2, 3]"))    # [1, 2, 3]  (safe)


# ---------------------------------------------------------------------------
# compile() — turn text into code you can run with eval/exec
# ---------------------------------------------------------------------------
print("\n--- compile ---")
code = compile("x + 1", "<demo>", "eval")   # prepare the code once
print(eval(code, {"x": 10}))                # 11


# ---------------------------------------------------------------------------
# globals() and locals() — the names Python currently knows
# ---------------------------------------------------------------------------
print("\n--- globals / locals ---")
message = "hi"
print("message" in globals())   # True  (it's a top-level name)

def show_locals():
    inside = 5
    print(locals())             # {'inside': 5}  (names inside this function)

show_locals()


# ---------------------------------------------------------------------------
# help() — read an object's built-in documentation
# ---------------------------------------------------------------------------
print("\n--- help ---")
# In the Python prompt, type help(str) to read full docs. Here we just peek at
# the first line so the output stays short.
print(abs.__doc__.splitlines()[0])
# Try typing  help(len)  yourself in the Python prompt!


# ---------------------------------------------------------------------------
# breakpoint() — pause the program to debug it (SHOWN, not run here)
# ---------------------------------------------------------------------------
print("\n--- breakpoint ---")
# Calling breakpoint() drops you into a debugger where you can look at your
# variables step by step. We don't call it (it would pause the program):
#
#     breakpoint()   # then type: n (next line), p x (print x), c (continue)
#
print("(breakpoint() is a debugging pause — shown in comments only.)")


# ---------------------------------------------------------------------------
# __import__() — import a module using its name as text
# ---------------------------------------------------------------------------
print("\n--- __import__ ---")
# Normal code uses the 'import' statement. __import__ is the function behind it,
# useful when the module name is decided while the program runs.
math_module = __import__("math")
print(math_module.sqrt(49))     # 7.0


if __name__ == "__main__":
    print("\nDone: show output, use files, and avoid eval/exec on untrusted text.")
