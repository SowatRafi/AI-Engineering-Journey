"""
01_lists.py
===========

Topic: Lists — ordered, mutable sequences.

WHY THIS MATTERS
----------------
The list is the workhorse collection: an ordered, changeable sequence that can
grow and shrink. You'll use it constantly for "a bunch of things in order".
"""

# ---------------------------------------------------------------------------
# 1. Creating and indexing
# ---------------------------------------------------------------------------
tasks = ["design", "build", "test", "deploy"]

print("--- Indexing ---")
print("First:", tasks[0])       # 0-based: first element
print("Last:", tasks[-1])       # negative indexes count from the end
print("Length:", len(tasks))


# ---------------------------------------------------------------------------
# 2. Slicing  ->  list[start:stop:step]  (stop is exclusive)
# ---------------------------------------------------------------------------
print("\n--- Slicing ---")
print("First two:", tasks[:2])   # ['design', 'build']
print("From index 1:", tasks[1:])  # ['build', 'test', 'deploy']
print("Reversed:", tasks[::-1])    # step of -1 reverses the list


# ---------------------------------------------------------------------------
# 3. Mutating: lists can change in place (they are MUTABLE)
# ---------------------------------------------------------------------------
print("\n--- Mutating ---")
tasks.append("monitor")          # add to the end
tasks.insert(0, "plan")          # insert at a position
tasks.remove("test")             # remove by value
popped = tasks.pop()             # remove & return the last item
tasks[1] = "architect"           # replace by index
print("After edits:", tasks)
print("Popped off:", popped)


# ---------------------------------------------------------------------------
# 4. Searching and counting
# ---------------------------------------------------------------------------
print("\n--- Searching ---")
print("'build' present?", "build" in tasks)   # membership test -> bool
print("Index of 'build':", tasks.index("build"))
print("Count of 'plan':", tasks.count("plan"))


# ---------------------------------------------------------------------------
# 5. Sorting
# ---------------------------------------------------------------------------
print("\n--- Sorting ---")
numbers = [5, 2, 9, 1]
numbers.sort()                   # sorts IN PLACE (mutates `numbers`)
print("Sorted in place:", numbers)

words = ["banana", "apple", "cherry"]
print("sorted() copy:", sorted(words, reverse=True))  # returns a NEW list
print("Original unchanged:", words)


# ---------------------------------------------------------------------------
# 6. Copying — the aliasing trap
# ---------------------------------------------------------------------------
# `b = a` does NOT copy the list; both names point to the SAME list object.
print("\n--- Copy vs. alias ---")
original = [1, 2, 3]
alias = original                 # same object!
alias.append(999)
print("Aliasing changed original:", original)   # [1, 2, 3, 999]

real_copy = original.copy()      # or list(original) or original[:]
real_copy.append(0)
print("Copy is independent:", original, "vs", real_copy)


if __name__ == "__main__":
    print("\nDone: lists are your ordered, mutable go-to collection.")
