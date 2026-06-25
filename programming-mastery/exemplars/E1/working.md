# E1 — Working exemplars (large-codebase comprehension)

Golden drills for the **Working** tier of module E1. Each presents an **unseen ~8–15-file
repo AS TEXT** (file tree + key files) and asks for the **full four-part map unaided** —
entry point · core module · **where to change feature X** · the one file to open first — where
**feature X takes one trace-hop** (the behavior lives one import away from where the feature is
*named*). Coverage spans three distinct shapes and three feature-location traps: a **web
service** (rule in the service, not the route), a **CLI** (filter in commands, not the parser),
and a **data pipeline** (core found by churn/imports, not by the orchestrator).

Orienting is **rubric-graded**; the executable sub-claim *"what does module M do?"* is
confirmed by running the module + its test (`drill-generation.md` §2–§3):

```
python <skill-dir>/runtime/python/runner.py snippet.py
```

Pose one, **hard-stop, wait** (`coaching-loop.md`). **How to grade** against module §7:
**P1** entry · **P2** core · **P3** feature-X location (must be **traced**, not the first
keyword hit) · **P4** first file + why. **Answering the feature-X question with the file that
merely *names* the feature (the route path / CLI word) instead of the module that *owns* the
behavior is the central Working failure — flag it** (§5c, locates-by-surface-string).

---

## W1 — Web service: change the discount rule (it's in the service, not the route)

```
shop/
├── README.md            #  "Checkout service."  flask --app shop.app run
├── shop/
│   ├── __init__.py
│   ├── app.py           #  create_app(); registers the blueprint
│   ├── routes.py        #  @bp.route("/checkout")  -> calls pricing
│   ├── pricing.py       #  apply_discount(subtotal, code)   <- the RULE + the 50% cap
│   ├── models.py        #  Cart, LineItem
│   └── db.py            #  session / persistence
└── tests/
    ├── test_pricing.py  #  asserts the discount behavior
    └── test_routes.py
```

```python
# shop/routes.py  (only wires HTTP -> the rule)
from shop.pricing import apply_discount
@bp.route("/checkout", methods=["POST"])
def checkout():
    body = request.get_json()
    return {"total": apply_discount(body["subtotal"], body["code"])}

# shop/pricing.py  (the discount RULE + the cap live here)
def apply_discount(subtotal, code):
    rules = {"SAVE10": 0.10, "HALF": 0.50, "VIP": 0.20}
    rate = min(rules.get(code, 0.0), 0.50)     # business rule: never discount > 50%
    return round(subtotal * (1 - rate), 2)
```

> **Your turn:** Orient. Give the **four-part map**. In particular: a PM asks you to **add a
> new `BLACKFRIDAY` discount code**. Which file do you change — `routes.py` or `pricing.py`?
> Which file would you open *first*?
>
> (Take your best guess — wrong attempts are useful data.)

**Runner-verified — `apply_discount` (the test-as-spec)**

```
SAVE10: 90.0
HALF: 50.0
unknown: 100.0
route(VIP): {'total': 80.0}
test_pricing.py: 3 passed
status: ok
```

**Gold orientation map**

- **Entry point (P1):** `shop/app.py` (`create_app` + blueprint registration); the README's
  `flask --app shop.app run` confirms it. `routes.py` is the request *surface*.
- **Core module (P2):** `shop/pricing.py` — owns the discount rules and the 50% cap; imported
  by `routes.py`. (The churn hot-spot in a pricing service is almost always the pricing rules.)
- **Feature X — add `BLACKFRIDAY` (P3):** **`pricing.py`**, in the `rules` table — **not**
  `routes.py`. Trace: `POST /checkout` (routes) → `apply_discount` (pricing). The route only
  passes the code through; the *rule* is one hop down. Runner confirms `apply_discount` owns
  the codes and the cap (`HALF` → 50.0, unknown → 100.0).
- **First file (P4):** `README.md` to confirm how it runs, then `pricing.py` (the rule you're
  changing) — or `test_pricing.py`, which *shows* the discount contract you must not break.

**Why.** The endpoint path `/checkout` is a **beacon for the request surface**, and it's a
tempting wrong answer because the word "checkout"/"discount" appears in `routes.py`. The
Working skill is to **trace one hop** from the route to the service that owns the rule, and to
read the test as the contract.

**Diagnoses.** A learner who says "change `routes.py`" located the feature by the **endpoint
name** (§5c, locates-by-surface-string) — the route owns *no* discount logic. A learner who
never opens `test_pricing.py` may not see the **50% cap** (so they'd "add a 70% code" and
silently hit the cap). Strong map: entry `app.py`, core `pricing.py`, `BLACKFRIDAY` → the
`rules` table in `pricing.py` (traced from the route), test read for the cap.

---

## W2 — CLI: add a `--pending` filter (it's in commands, not the arg parser)

```
todo/
├── README.md            #  python -m todo list [--pending]
├── todo/
│   ├── __init__.py
│   ├── __main__.py      #  entry
│   ├── cli.py           #  dispatch(argv): matches "list", reads flags  <- PARSER
│   ├── commands.py      #  list_tasks(tasks, pending_only=...)          <- BEHAVIOR
│   ├── models.py        #  Task(text, done)
│   └── store.py         #  load/save
└── tests/
    └── test_commands.py
```

```python
# todo/cli.py  (only parses argv and routes)
from todo import commands, store
def dispatch(argv):
    tasks = store.load("todo.json")
    if argv and argv[0] == "list":
        return commands.list_tasks(tasks, pending_only=("--pending" in argv))
    # add / done elided

# todo/commands.py  (the `list` behavior — the filter lives here)
def list_tasks(tasks, pending_only=False):
    items = [t for t in tasks if not t.done] if pending_only else list(tasks)
    return [t.text for t in items]
```

> **Your turn:** Orient. Give the **four-part map**. Feature X: **the `--pending` filter is
> dropping nothing** — every task still shows. Which file owns the filtering behavior you'd
> debug — `cli.py` or `commands.py`?
>
> (Take your best guess — wrong attempts are useful data.)

**Runner-verified — `dispatch` + `list_tasks` (the test-as-spec)**

```
list: ['a', 'b', 'c']
list --pending: ['a', 'c']
test_commands.py: 2 passed
status: ok
```

**Gold orientation map**

- **Entry point (P1):** `todo/__main__.py` → `cli.dispatch` (README: `python -m todo`).
- **Core module (P2):** `todo/models.py` is the domain type, but the **behavior core** for
  this feature is `commands.py` (and `store.py` is the persistence core). For "where does the
  *list* behavior live," it's `commands.py`.
- **Feature X — the `--pending` filter (P3):** **`commands.list_tasks`** owns the filter
  (`[t for t in tasks if not t.done]`); `cli.py` only **detects the flag** (`"--pending" in
  argv`) and passes `pending_only`. Trace: `__main__` → `cli.dispatch` (parses `--pending`) →
  `commands.list_tasks` (applies it). The bug ("drops nothing") is in `commands` if the
  comprehension is wrong, or in `cli` if the flag isn't passed — but the **filtering** is in
  `commands`. Runner confirms `list --pending` → `['a', 'c']` (drops the done `'b'`), so the
  behavior is correct here — the learner should trace which side actually fails.
- **First file (P4):** `test_commands.py` (it *shows* that `--pending` should drop done
  tasks), then `commands.py`.

**Why.** `cli.py` is where the *word* `list` and the *flag* `--pending` are parsed — a magnet
for the wrong answer. The behavior is one hop away in `commands.py`. The Working skill is
tracing the flag from parse-site to behavior-site, and reading the test as the spec for what
`--pending` *should* do.

**Diagnoses.** A learner who answers "debug `cli.py`" stopped at the **flag's parse site**
(§5c, locates-by-surface-string). A learner who can't say whether the bug is "flag not passed"
(cli) vs "filter wrong" (commands) hasn't **traced the value** across the hop (§5c, the trace
step). Strong map: entry `__main__`/`cli`, behavior core `commands.py`, filter owned by
`list_tasks`, confirmed by the test (which here *passes* — so the real bug is elsewhere, e.g.
the flag spelled `--pending` vs `--Pending`).

---

## W3 — Data pipeline: find the core by churn + imports, not by the orchestrator

```
etl/
├── README.md            #  "Nightly customer-data ETL."
├── etl/
│   ├── __init__.py
│   ├── pipeline.py      #  run(): extract -> transform -> load   <- orchestrator (entry)
│   ├── extract.py       #  read rows from source
│   ├── transform.py     #  normalize(row): email + amount rules  <- CORE (churn hot-spot)
│   ├── load.py          #  write rows to the warehouse
│   └── config.py
└── tests/
    └── test_transform.py
```

```
# git churn (last 90 days, given):
#   42  etl/transform.py        <- changes most often
#    6  etl/pipeline.py
#    3  etl/load.py
#    1  etl/extract.py
```

```python
# etl/pipeline.py  (orchestrator — the entry; almost never changes)
from etl import extract, transform, load
def run(rows):
    return load.load(transform.transform(extract.extract(rows)))

# etl/transform.py  (the CORE — the normalization rules; changes constantly)
def normalize(row):
    return {
        "email": row["email"].strip().lower(),
        "amount_cents": round(float(row["amount"]) * 100),
    }
def transform(rows):
    return [normalize(r) for r in rows]
```

> **Your turn:** Orient. Give the **four-part map**. The **entry point looks like
> `pipeline.run`** — but where is the **core**, the file you'd actually spend your time in?
> Use the churn list. Feature X: "trim whitespace from phone numbers too" — which file?
>
> (Take your best guess — wrong attempts are useful data.)

**Runner-verified — `transform` (the test-as-spec)**

```
transform: [{'email': 'alice@x.com', 'amount_cents': 1250}, {'email': 'bob@y.com', 'amount_cents': 300}]
pipeline.run count: 2
test_transform.py: passed
status: ok
```

**Gold orientation map**

- **Entry point (P1):** `etl/pipeline.py` → `run()` (the orchestrator that wires
  extract→transform→load). Beacon: it imports all three stages and is what a scheduler calls.
- **Core module (P2):** `etl/transform.py` — **the churn hot-spot (42 changes) and the most
  semantically dense module.** The orchestrator barely changes; the *rules* in `transform`
  change constantly. **This is the git-churn-as-core-finder beacon** — the core is where the
  work concentrates over time, not the top-level `run()`.
- **Feature X — trim phone whitespace (P3):** **`transform.py`** (`normalize`) — the per-row
  normalization rules. Not `pipeline.py` (just orchestration), not `extract`/`load` (I/O).
  Runner confirms `transform` owns the email-lowercasing + amount→cents rules.
- **First file (P4):** `README.md` (what the pipeline is for), then `transform.py` (the core
  you'll live in) — or `test_transform.py` (the rules' contract).

**Why.** The *orchestrator* (`pipeline.run`) is the entry, but it is **not** the core — a
classic trap. The Working skill is to use **churn** (and import counts) to find the file where
behavior actually concentrates, and to put the normalization feature there.

**Diagnoses.** A learner who names `pipeline.py` as both entry **and** core conflated "where it
starts" with "where the work is" (§5c, ignores-churn). A learner who reads the churn list as
"`transform.py` changes a lot, so it's buggy — avoid it" **inverted** the signal (§5c, high
churn = the heart, not a warning). Strong map: entry `pipeline.run`, core `transform.py` (by
churn + imports), phone-trim → `transform.normalize`, confirmed by the test.
