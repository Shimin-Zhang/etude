# E1 — Advanced exemplars (large-codebase comprehension)

Golden drills for the **Advanced** tier of module E1. Each presents a **denser /
partly-lying-structure repo AS TEXT** and asks for the full map **unaided**, plus the
Advanced moves: **recover the real entry/core when names mislead** (confirm by tracing the
import-call chain or running a test), **trace a cross-file feature path** naming the owner at
each hop, **rank the one gateway file**, and **articulate the orient procedure** (teach-it-back).
Coverage spans three distinct Advanced traps: **lying folder names + a hidden entry point**, a
**three-hop cross-cutting feature**, and a **no-README/no-tests** repo (the Feathers corner).

Orienting is **rubric-graded**; the executable sub-claim is confirmed by running the relevant
module + a test (`drill-generation.md` §2–§3):

```
python <skill-dir>/runtime/python/runner.py snippet.py
```

Pose one, **hard-stop, wait** (`coaching-loop.md`). **How to grade** against module §7:
**P1** entry · **P2** core · **P3** feature path (every hop named, traced) · **P4** gateway file,
ranked. **Naming the entry/core from a *folder name* when the behavior disagrees is the central
Advanced failure — convict it by running a test** (§5c, trusts-a-folder-name). Require a
**teach-it-back** of the method at this tier.

---

## A1 — Lying structure: `core/` is dead; the entry hides in `console_scripts`

```
app/
├── pyproject.toml       #  [project.scripts]  app = "app.run:main"     <- the REAL entry
├── app/
│   ├── __init__.py
│   ├── core/
│   │   └── legacy.py    #  process(invoice)  -- LOOKS central; nothing imports it
│   ├── services/
│   │   └── billing.py   #  charge(invoice)   -- the ACTUAL core (imported by run.py)
│   ├── run.py           #  main(invoice) -> billing.charge
│   └── utils.py
└── tests/
    └── test_billing.py
```

```python
# app/core/legacy.py   (named "core", but DEAD -- nothing imports it)
def process(invoice):
    return invoice["amount"]            # superseded pricing: no tax, never wired in

# app/services/billing.py   (the live core)
TAX = 0.08
def charge(invoice):
    return round(invoice["amount"] * (1 + TAX), 2)

# app/run.py   (the real entry: pyproject console_scripts  app = "app.run:main")
from app.services.billing import charge
def main(invoice):
    return charge(invoice)              # delegates to services.billing, NOT core.legacy
```

> **Your turn:** Orient. Where is the **entry point**, and what is the **core**? There's a
> folder literally named `core/` — is that the core? Justify by tracing what actually runs,
> and confirm with a test. Then teach the method back in one line.
>
> (Take your best guess — wrong attempts are useful data.)

**Runner-verified — convict the lying name (the test-as-spec)**

```
core.legacy.process (dead): 100.0
services.billing.charge : 108.0
run.main (entry)        : 108.0
test_billing.py: 2 passed
status: ok
```

**Gold orientation map**

- **Entry point (P1):** `app/run.py:main` — declared in `pyproject.toml`'s
  `[project.scripts] app = "app.run:main"`. Beacon: **there is no `__main__.py`; the entry is
  the `console_scripts` line.** A learner must read `pyproject` to find it.
- **Core module (P2):** `app/services/billing.py` (`charge`) — imported by `run.py` and what
  the entry actually calls. **`app/core/legacy.py` is dead code**: nothing imports it, and its
  `process` returns the pre-tax amount. The folder named `core/` **lies.**
- **Convict it (the run):** `process(invoice) == 100.0` (stale, no tax) while
  `charge(invoice) == main(invoice) == 108.0` — the **entry's result equals the *service*,
  not `core/`.** Behavior over names, settled by running the test.
- **Feature X — change the tax rate:** `services/billing.py` (`TAX`/`charge`), not
  `core/legacy.py`. **First file (P4):** `pyproject.toml` (it names the real entry), then
  `services/billing.py`.
- **Teach-it-back:** *"tree → entry (check `pyproject` console_scripts, not just
  `__main__`) → tests → core (most-imported / what the entry calls, not the folder named
  `core`) → churn → gateway; when a folder name and the behavior disagree, the behavior wins."*

**Why.** Two beacons lie at once: the entry is **not** a `__main__.py` (it's a
`console_scripts` line), and the folder named `core/` is **dead**. The Advanced skill is to
distrust both names and **confirm by tracing imports / running** — the run convicts `core/`.

**Diagnoses.** A learner who answers "entry is `__main__.py`" (there isn't one) and "core is
`core/legacy.py`" trusted **two folder/file-name beacons** over behavior (§5c,
trusts-a-folder-name) — the signature Advanced failure. A learner who never reads `pyproject`
can't find the entry at all (§5c, skips-the-high-signal-artifacts). Strong map: entry from
`pyproject`, core = `services/billing.py`, `core/` convicted dead by the run, method taught back.

---

## A2 — A three-hop cross-cutting feature: route → service → repository

```
api/
├── README.md
├── api/
│   ├── __init__.py
│   ├── routes.py        #  POST /users -> post_users()      (hop 1: HTTP)
│   ├── services/
│   │   └── users.py     #  register(repo, name)             (hop 2: the RULE)
│   ├── db/
│   │   └── repository.py#  UserRepo.exists() / add()        (hop 3: the lookup)
│   └── app.py           #  create_app()
└── tests/
    └── test_users.py
```

```python
# api/db/repository.py   (storage + case-insensitive lookup)
class UserRepo:
    def __init__(self): self._users = {}
    def exists(self, name): return name.lower() in self._users   # case-insensitive
    def add(self, name): self._users[name.lower()] = name

# api/services/users.py   (the cross-cutting RULE: unique usernames)
class DuplicateUser(Exception): pass
def register(repo, name):
    if repo.exists(name):
        raise DuplicateUser(name)
    repo.add(name); return name

# api/routes.py   (HTTP layer: only translates the exception to a 409)
def post_users(repo, name):
    try:
        return {"created": register(repo, name)}
    except DuplicateUser:
        return {"error": "username taken", "code": 409}
```

> **Your turn:** Orient. Feature X: **"usernames must be unique, case-insensitively."** Trace
> **every file** that enforces it and name the owner at each hop. If product asks to make it
> **case-sensitive**, which file(s) change — and which stays the same?
>
> (Take your best guess — wrong attempts are useful data.)

**Runner-verified — the uniqueness rule across the hops (the test-as-spec)**

```
first Alice: {'created': 'Alice'}
dup alice : {'error': 'username taken', 'code': 409}
dup ALICE : {'error': 'username taken', 'code': 409}
test_users.py: passed
status: ok
```

**Gold orientation map**

- **Entry point (P1):** `api/app.py` (`create_app`); `routes.py` is the request surface for
  `POST /users`.
- **Core module (P2):** `api/services/users.py` — owns the uniqueness *rule*; the domain logic
  hub.
- **Feature X path (P3) — three hops, owner named at each:**
  1. **`routes.py:post_users`** — *names* the endpoint and turns `DuplicateUser` into a 409.
     Owns **no** rule.
  2. **`services/users.py:register`** — **owns the uniqueness rule** (the `if repo.exists`
     guard).
  3. **`db/repository.py:UserRepo.exists`** — **owns the case-insensitivity** (`name.lower()`).
  - To make it **case-sensitive:** change **`repository.exists`/`add`** (drop `.lower()`); the
    rule in `services/users.py` stays; `routes.py` stays. The **runner confirms** the current
    behavior: `alice` and `ALICE` both 409 after `Alice` — case-insensitive, enforced at the
    repo.
- **First file (P4):** `services/users.py` (the rule) — the gateway to understanding the
  feature; `test_users.py` shows the contract.
- **Teach-it-back:** *"a cross-cutting feature is a path, not a file; trace entry → each layer
  and name the owner — the route names it, the service rules it, the repo implements the
  detail (case-insensitivity) — and a change lands at the layer that owns that detail."*

**Why.** The feature's *name* ("unique usernames") appears at the route, but the **rule** is in
the service and the **case-insensitivity** is in the repo — three owners. The Advanced skill is
to trace the whole path and place a change at the correct layer (case-sensitivity → the repo).

**Diagnoses.** A learner who says "it's enforced in `routes.py`" stopped at hop 1 (§5c,
locates-by-surface-string). A learner who finds the rule in `services` but misses that
**case-insensitivity lives in the repo** (`name.lower()`) would "fix" case-sensitivity in the
wrong file — the run shows the repo is where `ALICE == alice`. Strong map: all three hops named,
case-sensitive change → `repository.py`, rule layer unchanged, confirmed by the test.

---

## A3 — No README, no tests: orient from structure + churn, then characterize before changing

```
billing/
├── billing/
│   ├── __init__.py
│   ├── fees.py          #  compute_fee(amount, tier)   <- churn hot-spot; UNTESTED
│   ├── invoice.py
│   └── ledger.py
└── (no README, no tests/)
```

```
# git churn (given):
#   58  billing/fees.py     <- changes most; the heart
#    9  billing/invoice.py
#    4  billing/ledger.py
```

```python
# billing/fees.py   (untested; load-bearing quirks hide here)
def compute_fee(amount, tier):
    if tier == "gold":
        return min(amount * 0.02, 5.00)     # gold: 2% capped at 5.00
    return max(amount * 0.02, 0.50)         # else: 2% with a 0.50 floor
```

> **Your turn:** Orient with **no README and no tests.** What's the **core**? You've been asked
> to change `compute_fee` to a flat 1%. Before you touch it, what do you do **first** — and
> what current behavior must you not destroy? (Feathers: legacy code is code without tests.)
>
> (Take your best guess — wrong attempts are useful data.)

**Runner-verified — the characterization test you write first (Feathers)**

```
std small : 0.5
std large : 2.0
gold large: 5.0
test_characterization.py: behavior pinned
status: ok
```

**Gold orientation map**

- **Entry point (P1):** not given at this slice — say so honestly; orient from the package
  structure. (The Advanced move is recognizing you've been handed a *module*, and asking where
  it's called from.)
- **Core module (P2):** `billing/fees.py` — **the churn hot-spot (58 changes)** and the
  densest logic. With no README/tests, **churn is the core-finder.**
- **Feature X — flat 1% fee (P3):** `fees.py:compute_fee`. But **first, characterize** (P4 /
  the gateway move): with no tests, you **write a characterization test that pins the *current*
  behavior** before changing it — because `compute_fee` has **two load-bearing quirks**: the
  `0.50` floor for non-gold and the `5.00` cap for gold. The **runner-verified** pins:
  `compute_fee(10,"std") == 0.50` (floor bites), `compute_fee(1000,"gold") == 5.00` (cap bites).
  A naive "flat 1%" rewrite would **silently destroy the floor and the cap.**
- **First file / first action (P4):** there's no README or test, so the **gateway is the
  characterization test you create** — pin behavior, *then* change. (Feathers: find a seam, pin
  it, work outward.)
- **Teach-it-back:** *"no docs, no tests → orient from structure + churn (the hot file is the
  core), and before changing untested code, write a characterization test to pin its current
  behavior — the quirks (the floor, the cap) may be load-bearing."*

**Why.** This is the Feathers corner: the cheapest orientation artifacts (README, tests) are
**absent**, so you fall back to **structure + churn**, and you do **not** refactor untested
code blind — you characterize first. The run shows exactly which quirks a careless rewrite
would erase.

**Diagnoses.** A learner who immediately rewrites `compute_fee` to `amount * 0.01` **destroyed
the floor and cap** without noticing (§5c, exhaustive-reading-reflex's opposite — acting
without pinning behavior; Feathers). A learner who can't find the core without a README is over-
reliant on docs and didn't use **churn** (§5c, ignores-churn). Strong map: core = `fees.py` (by
churn), characterize-first, the `0.50` floor and `5.00` cap pinned by the run before any change,
method taught back.
