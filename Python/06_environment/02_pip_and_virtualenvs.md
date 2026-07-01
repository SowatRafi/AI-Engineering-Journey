# Environments: `pip`, Virtual Environments, and Dependencies

**Why this matters:** Every serious Python project uses an *isolated* environment
so its dependencies don't collide with other projects or your system Python.
This is a non-negotiable professional habit — and Phase 2 of the roadmap assumes
you already do it.

---

## 1. The problem virtual environments solve

Without isolation, `pip install` puts packages into one global location shared by
every project. Project A needs `numpy==1.26`, Project B needs `numpy==2.1` — they
now conflict. A **virtual environment** (venv) is a private, per-project folder
holding its own Python and its own installed packages.

---

## 2. Creating and activating a venv (`venv` ships with Python)

```bash
# Create a virtual environment in a folder named .venv (run once per project)
python -m venv .venv
```

Activate it (you must activate it in each new terminal session):

```powershell
# Windows PowerShell
.\.venv\Scripts\Activate.ps1
```

```bash
# macOS / Linux (bash/zsh)
source .venv/bin/activate
```

```bash
# Windows Git Bash
source .venv/Scripts/activate
```

When active, your prompt shows `(.venv)`. Deactivate with:

```bash
deactivate
```

> **Tip:** `.venv/` should be **git-ignored** (it already is in this repo's
> `.gitignore`). You never commit the environment itself — only the list of
> dependencies.

---

## 3. Installing packages with `pip`

```bash
pip install requests            # install the latest version
pip install "numpy>=1.26,<2.0"  # install within a version range
pip install requests==2.32.0    # pin an exact version
pip uninstall requests          # remove a package
pip list                        # show what's installed
pip show requests               # details about one package
```

---

## 4. Reproducibility: `requirements.txt`

Capture your exact dependencies so anyone (including future-you and CI) can
recreate the environment.

```bash
# Freeze the currently installed packages into a file
pip freeze > requirements.txt

# On another machine / fresh venv, install them all
pip install -r requirements.txt
```

A `requirements.txt` looks like:

```
requests==2.32.0
numpy==1.26.4
```

---

## 5. The standard workflow (memorize this)

```bash
python -m venv .venv                 # 1. create
source .venv/Scripts/activate        # 2. activate (Git Bash on Windows)
pip install -r requirements.txt      # 3. install deps (or pip install X)
python your_script.py                # 4. work
pip freeze > requirements.txt        # 5. record new deps when they change
deactivate                           # 6. leave when done
```

---

## 6. Modern tooling (good to know)

- **`uv`** — an extremely fast drop-in replacement for pip/venv, increasingly the
  2026 default (`uv venv`, `uv pip install`).
- **Poetry / PDM** — manage dependencies and packaging via `pyproject.toml`.

Start with `venv` + `pip` (built in, universal). Graduate to `uv` once the basic
workflow is second nature.

---

**Gate check:** You can create a venv, activate it, install a package, freeze
`requirements.txt`, and recreate the environment on a clean machine — unaided.
