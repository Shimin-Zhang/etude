# D2 — Advanced exemplars (naming)

Golden drills for the **Advanced** tier of module D2. Each turns on **two interacting issues** or
a **codebase-level** fault: a lying name *plus* hidden cross-call state, an inverted predicate
buried in otherwise-correct code, or a **consistency** violation across two functions whose
different return types **crash a caller**. The skill is **find it, prove it with a run, explain the
impact precisely, and propose the consistent/honest fix — and say *why*** (teach-back). D2 is
**hybrid**: the mismatch/crash is **executable** (behavior wins), the rename quality is **rubric**
— report the two verdicts separately (module §5d). Every fault below was **confirmed by running
it** (`drill-generation.md` §2):

```
python <skill-dir>/runtime/python/runner.py snippet.py
```

Coverage spans **distinct Advanced shapes**: a **lie + persisted state across calls**
(`get_config`), an **inverted polarity** (`filter_active`), and a **cross-function consistency
fault that raises** (`fetch_user`/`get_user`). Pose one, **hard-stop, wait** (`coaching-loop.md`).
**How to grade (module §7):** **D1** = caught it and the run proves it (for A3, shows the
`TypeError`); **D2/D3** = precise + consistent fix + the principle articulated; do not over-report
correct code.

---

## A1 — `get_config` that persists the first default across calls (lie + hidden cross-call state)

**Spec / promise in the name+signature.** `get_config(key, default)` reads a config value; the
`default` is just a **fallback** if the key is absent. The name `get_` and the `default` parameter
both imply **a pure read** — calling it shouldn't *change* what later calls return.

```python
_cache = {}

def get_config(key, default):
    if key not in _cache:
        _cache[key] = default      # silently PERSISTS the fallback as if it were configured
    return _cache[key]
```

> **Your turn:** Caller 1 does `get_config("timeout", 30)`. Later, caller 2 does
> `get_config("timeout", 99)`, expecting *their* default. Predict what each call returns and what
> `_cache` holds. Does the name match the behavior — and what's the impact?
>
> (Take your best guess — wrong attempts are useful data.)

**Runner-verified evidence** (the name lies; behavior wins)

```
$ python3 runtime/python/runner.py /tmp/D2_a1.py
{"status": "ok", "stdout": "30\n30\ncache: {'timeout': 30}\n", ...}

get_config("timeout", 30)  ->  30
get_config("timeout", 99)  ->  30        # NOT 99 — caller 1's "default" stuck
_cache                     ->  {'timeout': 30}
```

**Two verdicts.**
- **D1 — Honest? (executable):** **No — the name lies twice.** `get_` is not a pure read: the
  *first* call **writes** `default` into `_cache`, so a *later* call with a different `default`
  silently gets the **first** one (`99` → returns `30`). The run convicts it: caller 2's default is
  ignored.
- **D2/D3 — Precise/Consistent? (rubric):** the fix must stop the hidden write and make the name
  honest about caching.

**Model answer (the gold).**

> **The name lies — `get_config` isn't a pure "get," and `default` isn't a per-call fallback.** The
> first call writes its `default` into `_cache`; every later call for that key returns the **stored
> first value**, ignoring the new `default`. So `get_config("timeout", 99)` after
> `get_config("timeout", 30)` returns `30`, not `99` — a config value silently frozen by whoever
> called first. Two problems, one root: a `get_` that **mutates**, and a `default` that **persists**
> (an A1 "side effect under a pure name" event across calls). Honest fix — make the fallback truly
> per-call and don't write on read:
> ```python
> def get_config(key, default=None):
>     return _cache.get(key, default)      # pure read; default is a real fallback
> ```
> If caching *is* intended, name it so (`get_or_cache_config`) and make the cross-call behavior part
> of the contract — but don't hide a write behind `get_`.

**Diagnoses.** §5c **lying name + hidden state across calls** (the Frontier-adjacent "lie only
manifests across two calls" shape, here at Advanced because the second mechanism — persisted
default — is explicit). A learner who predicts `99` for the second call modeled `get_` as pure;
run it to show `30`. Catching "it caches" but not that **caller 2's default is silently dropped**
is a **partial D1** — the impact (a config value frozen by call order) is the consequential part.

---

## A2 — `filter_active` that returns the inactive users (inverted polarity in correct-looking code)

**Spec / promise in the name.** `filter_active(users)` should return the **active** users' names.

```python
def filter_active(users):
    out = []
    for u in users:
        if not u["active"]:        # keeps the INACTIVE ones (inverted predicate)
            out.append(u["name"])
    return out

users = [
    {"name": "ada", "active": True},
    {"name": "bob", "active": False},
    {"name": "cleo", "active": True},
]
```

> **Your turn:** The loop, the append, the structure all look fine. Predict what
> `filter_active(users)` returns for the data above. Does the name match what it returns?
>
> (Take your best guess — wrong attempts are useful data.)

**Runner-verified evidence** (the name lies; behavior wins)

```
$ python3 runtime/python/runner.py /tmp/D2_a2.py
{"status": "ok", "stdout": "filter_active -> ['bob']\n", ...}

filter_active(users)  ->  ['bob']      # bob is the INACTIVE one; ada & cleo (active) are dropped
```

**Two verdicts.**
- **D1 — Honest? (executable):** **No — the name lies (inverted polarity).** `filter_active`
  returns `['bob']`, the **inactive** user, and omits the active `ada` and `cleo`. The code is
  structurally clean; only the **predicate is inverted** (`if not u["active"]`). The run convicts
  it.
- **D2/D3 — Precise/Consistent? (rubric):** one-character behavior fix, or an honest rename.

**Model answer (the gold).**

> **The name lies — `filter_active` returns the *inactive* users.** For the sample data it returns
> `['bob']` (active is `False`) and drops `ada` and `cleo` (active). Everything but the predicate is
> correct; the `if not u["active"]` is inverted. This is the nastiest kind of naming bug because the
> code *reads* right — a reviewer skimming the loop sees a clean filter and trusts the name (the A2
> lying-name trap; running it is what exposes it). Honest fix: drop the `not` —
> `if u["active"]:` — so the name tells the truth; **or**, if returning inactive users is what's
> wanted, rename to `filter_inactive`. Don't ship "active" code that yields the inactive set.

**Diagnoses.** §5c **inverted polarity** (`is_X`/`filter_X` returns `not X`). A learner who predicts
`['ada', 'cleo']` reasoned from the **name**, not the code — exactly the trap; the run's `['bob']`
is the correction. Strong answers note *why* it's dangerous (clean structure + lying name → a
reviewer rubber-stamps it) and tie it to "behavior wins, so run it." Over-reporting (flagging the
clean loop as also buggy) costs D2.

---

## A3 — `fetch_user` vs `get_user`: inconsistent names for one concept that crash a caller

**Spec / context.** Two functions in the codebase deal with "the user for an id." Their names use
**different verbs** for what a reader assumes is the **same operation** — and they return
**different shapes**. A caller who learned one and assumes the other does the rest.

```python
_users = {1: {"id": 1, "name": "ada"}, 2: {"id": 2, "name": "bob"}}

def fetch_user(uid):           # "fetch" -> returns the user RECORD (dict)
    return _users.get(uid)

def get_user(uid):             # same concept, different verb; returns just the NAME (str)
    rec = _users.get(uid)
    return rec["name"] if rec else None

a = fetch_user(1)
b = get_user(2)
print("fetch_user(1):", a)       # a dict (record)
print("get_user(2):", b)         # a str (name only)
print("a['name']:", a["name"])   # works (a is a dict)
print("b['name']:", b["name"])   # a reader assumes get_user is like fetch_user -> CRASH
```

> **Your turn:** A teammate sees `fetch_user(1)["name"]` work, then writes `get_user(2)["name"]`,
> assuming `get_user` returns the same kind of thing. Predict what happens. What's the naming
> problem, and how would you fix it across the codebase?
>
> (Take your best guess — wrong attempts are useful data.)

**Runner-verified evidence** (the inconsistency causes a real crash; behavior wins)

```
$ python3 runtime/python/runner.py /tmp/D2_a3.py
{"status": "error", "stdout": "fetch_user(1): {'id': 1, 'name': 'ada'}\nget_user(2): bob\na['name']: ada\n", "stderr": "Traceback (most recent call last):\n  ...\n    print(\"b['name']:\", b[\"name\"])\nTypeError: string indices must be integers, not 'str'\n", "returncode": 1, ...}

fetch_user(1)   ->  {'id': 1, 'name': 'ada'}     # a dict (record)
get_user(2)     ->  'bob'                          # a str (name only)
a["name"]       ->  'ada'                          # works (a is a dict)
b["name"]       ->  TypeError: string indices must be integers, not 'str'   # CRASH (status: error)
```

**Two verdicts.**
- **D1 — Honest? (executable):** the **inconsistency is the fault, and it's machine-proven.** Two
  verbs (`fetch_`/`get_`) for one concept, returning a **dict** vs a **str**; a caller who
  generalizes from one **crashes** (`b["name"]` raises `TypeError`). The run shows both the
  divergent shapes and the exception.
- **D3 — Consistent? (rubric):** the fix is a codebase-level rename + shape decision.

**Model answer (the gold).**

> **Inconsistent naming for one concept — and the inconsistency crashes callers.** `fetch_user`
> returns the **record** (dict); `get_user` returns just the **name** (str). The two verbs imply
> the same operation, so a reader who learned `fetch_user(uid)["name"]` reasonably writes
> `get_user(uid)["name"]` — and it raises `TypeError: string indices must be integers` (indexing a
> str with `"name"`). Two failures: **different verbs for the same concept** (`fetch_`/`get_`) and
> **different return shapes** under near-synonymous names. Fix at the codebase level: pick **one
> verb** for "look up a user" and **one return shape**. e.g. `get_user(uid) -> dict | None` (the
> record), and if a name-only helper is genuinely needed, name it for *that*:
> `get_user_name(uid) -> str | None`. The principle (teach-back): **one concept → one name,
> everywhere; one name → one concept** (Ousterhout's consistency rule — and its third clause,
> "same name ⇒ same behavior," is exactly what's violated here, the same shape as his `block` bug).

**Diagnoses.** §5c **inconsistent names for one concept** (and its dangerous twin — near-synonyms
with different contracts). The instructive part: the bug is **not in any one line** — both functions
are individually correct — it's in the **relationship between two names**, invisible without a
whole-codebase view (the A2 whole-change-model gap, authored-side). A learner who "fixes" only
`get_user`'s body without standardizing the **verb and shape** has patched the symptom, not the
inconsistency — a **partial D3**. Strong answers run it to show the `TypeError` is *caused by the
naming*, and articulate the one-concept-one-name principle.
</content>
