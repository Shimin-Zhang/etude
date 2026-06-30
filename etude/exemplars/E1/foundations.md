# E1 — Foundations exemplars (large-codebase comprehension)

Golden drills for the **Foundations** tier of module E1. Each presents a **small repo
(≤ ~6 files, helpful names, a feature owned by one file) AS TEXT** — a file tree + the key
files — and asks for the **entry point** and **core module** (each justified by a beacon),
plus *"what does module M do?"* for a module with a test. Coverage spans **three distinct
repo shapes** — a **library**, a **web service**, and a **CLI** — with three distinct
entry-point kinds (`__init__` public API · `app.py` route table · `__main__`).

Orienting is **rubric-graded** (`drill-generation.md` §3); the **one executable sub-claim**
is *"what does module M do?"*, confirmed by collapsing the module + its test into one file
and **running it** (`drill-generation.md` §2):

```
python <skill-dir>/runtime/python/runner.py snippet.py
```

Pose one, **hard-stop, wait** (`coaching-loop.md`). **How to grade** against module §7:
**P1** = entry point named + beacon-justified; **P2** = core module named + beacon-justified;
plus the test-as-spec confirms the module's behavior. **An entry/core named from a *folder
name* rather than a *beacon/trace/import* is a partial pass — flag it as a possible lucky
name-match, not orientation** (§5c, trusts-a-folder-name).

---

## F1 — A library: where is the "entry point" when there's no `main`?

```
textslug/
├── README.md            #  "Turn any string into a URL slug."  pip install textslug
├── pyproject.toml       #  name = "textslug"
├── textslug/
│   ├── __init__.py      #  from .core import slugify        <- the public API
│   └── core.py          #  def slugify(text): ...
└── tests/
    └── test_core.py     #  asserts slugify on several inputs
```

```python
# textslug/__init__.py
from .core import slugify          # re-exports the one public name

# textslug/core.py
import re
def slugify(text):
    text = text.lower().strip()
    text = re.sub(r"[^a-z0-9]+", "-", text)
    return text.strip("-")
```

> **Your turn:** Orient. What is the **entry point** of this package, what is the **core
> module**, and *what does `slugify` actually do* on `"Cafe del Mar #2"`? Justify each from a
> beacon, not a guess.
>
> (Take your best guess — wrong attempts are useful data.)

**Runner-verified — `slugify` (the test-as-spec)**

```
slugify('Hello, World!') -> 'hello-world'
slugify('  Multiple   Spaces  ') -> 'multiple-spaces'
slugify('Cafe del Mar #2') -> 'cafe-del-mar-2'
test_core.py: 3 passed
status: ok
```

**Gold orientation map**

- **Entry point (P1):** for a *library* there is no `main` — the **entry point is the public
  API**, `textslug/__init__.py`, which re-exports `slugify` (`from .core import slugify`).
  Beacon: the `__init__.py` re-export *is* the door users come through.
- **Core module (P2):** `textslug/core.py` — the single function that does the work; imported
  by `__init__`. Beacon: it's the only non-trivial module, and `__init__` imports *from* it.
- **What `slugify` does:** lowercases, replaces every run of non-`[a-z0-9]` characters with
  `-`, and strips leading/trailing `-`. Note the **runner-confirmed** edge: `"Cafe del Mar
  #2"` → `"cafe-del-mar-2"` (the `#` and spaces collapse). **Feature X** ("handle accented
  characters") lives in `core.py`'s regex — one file.

**Why.** The Foundations move for a *library* is recognizing that the public `__init__.py`
is the entry — not a missing `main`. The core is found by following the one import. And you
**read the test** (or run it) to confirm what `slugify` is *for*, rather than guessing the
regex's behavior.

**Diagnoses.** A learner who says "there's no entry point, it's just functions" hasn't mapped
a *library*'s public API to the entry concept (P1 partial; §5c root — a repo isn't a script).
A learner who **predicts** `slugify` strips accents to `café`→`cafe` without running it is
guessing the regex (§5c, never-opens-tests) — run it; `é` is non-`[a-z0-9]`, so it becomes a
`-`. Strong map: `__init__` is the entry, `core.py` is the core, behavior confirmed by the test.

---

## F2 — A web service: the route names the endpoint; the core does the work

```
webhello/
├── README.md            #  "A tiny greeting service."  run: flask --app webhello.app run
├── webhello/
│   ├── __init__.py
│   ├── app.py           #  create_app(); @app.route("/hello/<name>")   <- entry
│   └── greeting.py      #  def greet(name, formal=False): ...          <- core logic
└── tests/
    └── test_greeting.py
```

```python
# webhello/app.py  (entry point — the route table; delegates to greeting)
from webhello.greeting import greet
def create_app():
    app = Flask(__name__)
    @app.route("/hello/<name>")
    def hello(name):
        return greet(name)                  # <- delegates to the core
    return app

# webhello/greeting.py  (the core — pure logic, no framework)
def greet(name, formal=False):
    name = name.strip() or "there"
    return f"Good day, {name}." if formal else f"Hi {name}!"
```

> **Your turn:** Orient. **Entry point? Core module?** If you had to change the **wording of
> the greeting**, which file would you edit — `app.py` or `greeting.py`? Justify from a beacon.
>
> (Take your best guess — wrong attempts are useful data.)

**Runner-verified — `greet` + the route table (the test-as-spec)**

```
greet('Sam'): Hi Sam!
greet('   '): Hi there!
greet('Sam', formal=True): Good day, Sam.
routes: ['/hello/<name>']
test_greeting.py: passed
status: ok
```

**Gold orientation map**

- **Entry point (P1):** `webhello/app.py` — `create_app()` + the `@app.route("/hello/<name>")`
  table. Beacon: `@app.route` / `create_app` is the framework's entry convention, and the
  README's `flask --app webhello.app run` confirms it.
- **Core module (P2):** `webhello/greeting.py` — the pure `greet` logic, imported by `app.py`.
  Beacon: `app.py` imports `greet` *from* it and just delegates.
- **Change the greeting wording → `greeting.py`** (`greet`), **not** `app.py`. The route only
  maps the URL to the function; the *wording* is owned by the core. Runner confirms `greet`
  owns the blank→`"there"` and formal/informal behavior.

**Why.** The route is a **beacon for the request surface**, not the place behavior lives. The
Foundations skill is to separate "where the endpoint is named" (`app.py`) from "where the
logic lives" (`greeting.py`) — the same name-vs-owner split the Working tier pushes to a
trace-hop.

**Diagnoses.** A learner who answers "edit `app.py`" because that's where `/hello` appears has
located the feature by its **surface** (the route path), not its owner (§5c,
locates-by-surface-string). A learner who never opens `test_greeting.py` misses that
`greet("")` returns `"Hi there!"` (the blank fallback). Strong map: `app.py` entry,
`greeting.py` core, wording change → `greeting.py`, confirmed by the test.

---

## F3 — A CLI: find the persistence core by following the imports

```
notekeeper/
├── README.md            #  "Keep tiny notes from the terminal."  python -m notekeeper add ...
├── notekeeper/
│   ├── __init__.py
│   ├── __main__.py      #  entry: python -m notekeeper        <- entry
│   ├── cli.py           #  parse argv -> commands
│   ├── models.py        #  Task dataclass
│   └── store.py         #  load/save notes to JSON            <- imported by cli + commands
└── tests/
    └── test_store.py    #  asserts the JSON round-trip
```

```python
# notekeeper/store.py  (the persistence core)
import json, os
from notekeeper.models import Task
def save(path, tasks):
    with open(path, "w") as f:
        json.dump([t.__dict__ for t in tasks], f)
def load(path):
    if not os.path.exists(path):
        return []                       # missing file -> empty, no crash
    with open(path) as f:
        return [Task(**d) for d in json.load(f)]
```

> **Your turn:** Orient. **Entry point? Core module?** And *what does `store.load` do when the
> file doesn't exist yet* — crash, or something else? Justify from a beacon.
>
> (Take your best guess — wrong attempts are useful data.)

**Runner-verified — `store` round-trip (the test-as-spec)**

```
load(missing): []
roundtrip: [Task(text='a', priority=2, done=False), Task(text='b', priority=1, done=True)]
test_store.py: 2 passed
status: ok
```

**Gold orientation map**

- **Entry point (P1):** `notekeeper/__main__.py` (`python -m notekeeper`). Beacon: the README
  run line + the `__main__.py` convention.
- **Core module (P2):** `notekeeper/store.py` — the persistence center, **imported by both
  `cli.py` and the commands**. Beacon: it's the **most-imported** module (and would be the
  churn hot-spot). `models.py` is the domain *type*; `store.py` is what everything calls to
  persist.
- **What `store.load` does:** returns `[]` for a missing file (no crash), and round-trips
  saved notes — **runner-confirmed**. **Feature X** ("store as YAML instead of JSON") lives in
  `store.py` — one file.

**Why.** Two modules could plausibly be "the core" — `models.py` (the type) and `store.py`
(the persistence). The Foundations skill is to pick by **what's most depended-on / where the
work concentrates** (imports + churn), and to **confirm the missing-file behavior by running
the test** rather than assuming `load` crashes.

**Diagnoses.** A learner who **predicts `load` crashes** on a missing file is guessing (§5c,
never-opens-tests) — the test pins `[]`. A learner who names `models.py` as the core *only*
because it's "the data" — without noting `store.py` is more imported — has a thin P2
justification (process partial). Strong map: `__main__` entry, `store.py` core (most-imported),
missing-file → `[]` confirmed by the test.
