# Python — Phase 1: Programming Foundations

Hands-on, heavily-commented Python lessons for **Phase 1** of the
[AI Engineer Roadmap](../AI_Engineer_Roadmap.md). Every file is runnable and
self-contained: read the docstring at the top, then run it and read the output
next to the code.

```bash
# From inside the Python/ folder, run any lesson directly, e.g.:
python 01_basics/01_variables_and_types.py
python OOP/Polymorphism/polymorphism.py
```

> Note: run `02_logic/03_modules_and_imports.py` **from inside `02_logic/`** so
> it can find its local `geometry.py` helper module.

### 🟢 Start here if you're new

Almost every folder has a **`beginner_examples.py`** file with lots of tiny,
everyday examples (ages, prices, pets, snacks) and minimal jargon. Run that one
**first** to get the idea, then open the deeper numbered lessons in the same
folder for the full picture.

```bash
python 01_basics/beginner_examples.py          # easy warm-up
python 01_basics/01_variables_and_types.py     # then the deeper lesson
```

---

## Learning order

| # | Folder / File | Topic |
|---|---|---|
| **Basics** | `01_basics/01_variables_and_types.py` | Variables, types, casting |
| | `01_basics/02_conditionals.py` | if/elif/else, logic, truthiness |
| | `01_basics/03_loops.py` | for, while, break/continue, for-else |
| **Logic** | `02_logic/01_functions.py` | Params, *args/**kwargs, pure functions |
| | `02_logic/02_scope.py` | LEGB, global/nonlocal, closures |
| | `02_logic/03_modules_and_imports.py` | Imports, `__name__`, using `geometry.py` |
| **Data Handling** | `03_data_handling/01_lists.py` | Ordered, mutable sequences |
| | `03_data_handling/02_dicts.py` | Key→value mappings |
| | `03_data_handling/03_sets.py` | Uniqueness & set algebra |
| | `03_data_handling/04_tuples.py` | Immutable sequences, unpacking |
| | `03_data_handling/05_collections_comparison.py` | **When to use which** (guide) |
| | `03_data_handling/06_strings.py` | Text, methods, f-strings |
| | `03_data_handling/07_file_io.py` | Reading/writing files with `with` |
| **Reliability** | `04_reliability/01_error_handling.py` | try/except/else/finally, custom errors |
| | `04_reliability/02_debugging.py` | Tracebacks, assert, breakpoint, logging |
| **OOP** | `OOP/Foundations/01_classes_and_objects.py` | Classes, objects, methods |
| | `OOP/Foundations/02_constructors.py` | Default vs. parameterized, alt constructors |
| | `OOP/Foundations/03_introspection_and_mutability.py` | `__dict__`, `dir()`, mutability |
| | `OOP/Foundations/04_methods_static_class_factory.py` | static/class methods, overloading, factory |
| | `OOP/Encapsulation/encapsulation.py` | Private/public, getters/setters, `@property` |
| | `OOP/Inheritance/inheritance.py` | single/multi-level/multiple, `super()`, MRO |
| | `OOP/Polymorphism/polymorphism.py` | Overriding, duck typing, operator overloading |
| | `OOP/Composition/composition.py` | has-a relationships, delegation |
| | `OOP/Abstraction/abstraction.py` | ABCs, abstract methods, contracts |
| **Pythonic** | `05_pythonic/01_comprehensions.py` | list/dict/set comprehensions |
| | `05_pythonic/02_iterators.py` | Iterator protocol |
| | `05_pythonic/03_generators.py` | `yield`, lazy/infinite streams |
| **Environment** | `06_environment/01_standard_library.py` | math, random, json, collections, pathlib |
| | `06_environment/02_pip_and_virtualenvs.md` | pip, venv, requirements.txt |
| **Best Practices** | `07_best_practices/clean_code_and_type_hints.py` | PEP 8 naming, type hints, dataclasses |

---

## How to study each file

1. Read the module docstring — it states the topic and *why it matters*.
2. Run it and read the printed output alongside the code.
3. Change something and re-run — break it on purpose and observe the error.
4. Move to the next file. The order above is deliberate; later files assume earlier ones.
