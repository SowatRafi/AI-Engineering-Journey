"""
05_collections_comparison.py
============================

Topic: WHEN to use list vs. dict vs. set vs. tuple — a decision guide.

WHY THIS MATTERS
----------------
Beginners often reach for a list by default. Choosing the right collection makes
code faster, clearer, and less buggy. This file is a reference you can re-read.
"""

# ===========================================================================
# QUICK COMPARISON TABLE
# ===========================================================================
#
# | Type  | Ordered? | Mutable? | Duplicates? | Indexed by | Typical use          |
# |-------|----------|----------|-------------|------------|----------------------|
# | list  | Yes      | Yes      | Yes         | position   | ordered, changing seq|
# | tuple | Yes      | No       | Yes         | position   | fixed record / key   |
# | dict  | Yes*     | Yes      | keys unique | key        | labelled lookup      |
# | set   | No       | Yes      | No          | (none)     | uniqueness/membership|
#
# * dicts preserve INSERTION order (guaranteed since Python 3.7).
#
# ===========================================================================


def demo_choose_list():
    """USE A LIST when: order matters and the contents change over time."""
    # e.g. a queue of tasks processed in sequence
    queue = ["ticket-1", "ticket-2", "ticket-3"]
    queue.append("ticket-4")
    return queue


def demo_choose_tuple():
    """USE A TUPLE when: a fixed group of values that shouldn't change.

    Good for records (lat, lon), RGB colours, or returning multiple values.
    Because they're immutable+hashable they can be dict keys / set members.
    """
    coordinate = (23.81, 90.41)   # (latitude, longitude) — a fixed pair
    return coordinate


def demo_choose_dict():
    """USE A DICT when: you look things up by a meaningful key, not position."""
    user = {"id": 101, "name": "Rafi", "active": True}
    return user["name"]           # O(1) lookup by key


def demo_choose_set():
    """USE A SET when: you need uniqueness or fast 'is it in here?' checks."""
    seen_ids = {101, 102, 103}
    return 102 in seen_ids        # very fast membership test


# ---------------------------------------------------------------------------
# A worked example showing all four cooperating
# ---------------------------------------------------------------------------
def analyse_log(lines: list[str]) -> dict[str, int]:
    """Count how many times each unique status code appears in log lines.

    - `lines` is a LIST because order and duplicates are meaningful.
    - We split each line into a TUPLE-like fixed structure.
    - We tally into a DICT (code -> count).
    - We use a SET to report the distinct codes seen.
    """
    counts: dict[str, int] = {}
    for line in lines:
        code = line.split()[-1]           # last token is the status code
        counts[code] = counts.get(code, 0) + 1
    distinct = set(counts)                 # unique codes
    print("Distinct codes:", distinct)
    return counts


if __name__ == "__main__":
    print("list  ->", demo_choose_list())
    print("tuple ->", demo_choose_tuple())
    print("dict  ->", demo_choose_dict())
    print("set   ->", demo_choose_set())

    print("\n--- Worked example ---")
    logs = [
        "GET /home 200",
        "GET /docs 200",
        "GET /admin 403",
        "GET /ghost 404",
        "GET /home 200",
    ]
    print("Counts:", analyse_log(logs))
    print("\nDone: pick the collection that matches your data's shape.")
