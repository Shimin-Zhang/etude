# D3 — Advanced exemplars (refactoring judgment)

Golden drills for the **Advanced** tier of module D3. Each is **untested legacy with a quirk**,
or a refactor whose behavior change **survives shallow testing** (passes the obvious inputs,
fails interior/edge ones), combining **≥2 mechanisms**. The skill, **unaided**: **write a
characterization battery FIRST** that pins current behavior (including quirks), perform the
refactor, and **prove preservation** by running BEFORE vs AFTER — **or catch the planted behavior
change** the obvious inputs miss — and **articulate the judgment** (characterize before you
change; a clean look doesn't make it a refactor; the quirk may be load-bearing).

D3 is graded **hybrid** (`drill-generation.md` §1d, §3): behavior is settled by **running the
SAME battery through BEFORE and AFTER and diffing** `stdout`/`status` (`drill-generation.md` §2);
the judgment is rubric. Every pair below was **run** — true refactors confirmed **identical**,
behavior changes shown to **diverge** on inputs the naive battery omits:

```
python <skill-dir>/runtime/python/runner.py snippet.py   # run BEFORE and the candidate, diff
```

Coverage spans **characterize-the-quirk-first / cross-call shared-state aliasing / integer re-
association**. Pose one, **hard-stop, wait** (`coaching-loop.md`). **How to grade** against module
§7: **AX1** (executable) = wrote a battery that *could* falsify preservation (hits the quirk /
the second call / the interior input), and correctly proved-preserved or caught-the-change; **AX2**
(rubric, solid required at Advanced) = characterized **before** changing, articulated the
underlying discipline on a teach-back, kept one hat on. A learner who proves a *weak* battery
identical and declares "refactor" has the **central Advanced trap** — they never ran the input that
distinguishes the versions (§5c, tests-pass-so-safe).

---

## A1 — Untested legacy parser: characterize the quirk before you touch it

**Setup.** This CSV-row parser has **no tests** and a **quirk**: it silently **drops empty
fields**. A teammate says "this drops fields, that looks like a bug — clean it up."

```python
# BEFORE (legacy, no tests)
def parse_csv_row(row):
    parts = row.split(",")
    out = []
    for p in parts:
        p = p.strip()
        if p:                       # quirk: empty fields silently dropped
            out.append(p)
    return out
```

> **Your turn:** You're about to refactor this for readability. **Before** you change anything,
> what characterization battery pins its *current* behavior — including the quirk? Then: is the
> "clean it up" rewrite below a **refactor**, and what does each version produce for `"a,,c"` and
> `""`?
>
> ```python
> # "CLEAN IT UP" rewrite a teammate proposes
> def parse_csv_row(row):
>     return [p.strip() for p in row.split(",")]
> ```
>
> (Take your best guess — wrong attempts are useful data.)

**Runner-verified evidence** (characterization battery: includes empty fields, all-empty, single)

```
inputs: "a, b ,c" ; "a,,c" ; " , ,x" ; "" ; "one"

BEFORE stdout (the behavior to PIN):
'a, b ,c' -> ['a', 'b', 'c']      'a,,c' -> ['a', 'c']      ' , ,x' -> ['x']
''        -> []                   'one'  -> ['one']

"CLEAN IT UP" rewrite stdout:
'a, b ,c' -> ['a', 'b', 'c']      'a,,c' -> ['a', '', 'c']  <-- DIFFERS
''        -> ['']                 <-- DIFFERS               ' , ,x' -> ['', '', 'x']  <-- DIFFERS

stdout identical: False
VERDICT: BEHAVIOR CHANGED  ✗  → the "clean it up" rewrite is NOT a refactor (it keeps empties)

# a TRUE refactor — same drop-empties behavior, expressed as one comprehension:
#   return [p.strip() for p in row.split(",") if p.strip()]
# verified identical to BEFORE incl. 'a,,c' -> ['a', 'c'] and '' -> []   → preserved ✓
```

**Why.** The right first move is **characterization**, not cleanup (Feathers: untested code is
legacy code; pin its behavior before changing it). The battery *must* include `"a,,c"` and `""` —
the inputs that exercise the quirk — or it won't catch the change. The teammate's rewrite drops
the `if p`, so empty fields are now **kept**: `"a,,c"` → `['a', '', 'c']` (was `['a', 'c']`), `""`
→ `['']` (was `[]`). That may be what *should* happen — but it is a **behavior change**, not a
refactor, and a downstream caller may depend on the drop-empties quirk. The honest path: pin the
quirk, then either do a **true refactor** (the `if p.strip()` comprehension, identical behavior)
**or** make the behavior change *deliberately*, with its own justification and tests — wearing the
**feature hat**, not the refactoring hat.

**Diagnoses.** A learner who **refactors before characterizing** ("it's a bug, I'll just fix the
structure") committed the signature Advanced error (§5c, refactors-untested-legacy-without-
characterizing) — the quirk may be load-bearing; flag it. A learner whose battery omits `"a,,c"`/
`""` "proves" the rewrite identical on `"a, b ,c"`/`"one"` and wrongly blesses it (§5c, tests-pass-
so-safe / weak battery). A learner who **conflates** "cleaner" with "refactor" credits the nicer
comprehension and misses that it changed behavior (§5c, confuses-structure-with-preserving).
Strong: writes a battery hitting the quirk first, classifies the rewrite as a behavior change,
offers the true `if p.strip()` refactor, and says the empties-change needs the feature hat.

---

## A2 — "Hoist the defaults to a constant" — aliasing changes behavior across calls

**Setup.** `build_config` rebuilds a defaults dict each call. A teammate proposes "hoist the
defaults to a module constant to avoid rebuilding it" — a plausible micro-optimization. It
**survives a single-call test** and breaks on the **second** call.

```python
# BEFORE
def build_config(overrides):
    config = {"retries": 3, "timeout": 30}   # fresh dict literal each call
    for k, v in overrides.items():
        config[k] = v
    return config
```

```python
# CANDIDATE — "hoisted the defaults to avoid rebuilding"
DEFAULTS = {"retries": 3, "timeout": 30}     # one shared dict

def build_config(overrides):
    config = DEFAULTS                          # alias, not copy
    for k, v in overrides.items():
        config[k] = v
    return config
```

> **Your turn:** Is the candidate a behavior-preserving refactor? A single call looks fine —
> what **sequence** of calls would you run to be sure, and what does each version produce?
>
> (Take your best guess — wrong attempts are useful data.)

**Runner-verified evidence** (the battery must be a **sequence**, not one call)

```
inputs:  build_config({"timeout": 60})   then   build_config({"retries": 5})

BEFORE stdout:                          CANDIDATE stdout:
{'retries': 3, 'timeout': 60}           {'retries': 3, 'timeout': 60}   (1st call: identical)
{'retries': 5, 'timeout': 30}           {'retries': 5, 'timeout': 60}   <-- DIFFERS (2nd call)

stdout identical: False
VERDICT: BEHAVIOR CHANGED  ✗  → NOT a refactor (state leaks between calls)

# a TRUE refactor — hoist the constant but COPY it per call:
#   config = dict(DEFAULTS); config.update(overrides)
# verified identical to BEFORE incl. 2nd call {'retries': 5, 'timeout': 30}   → preserved ✓
```

**Why.** `config = DEFAULTS` makes `config` an **alias** of the one shared module dict (an A1
aliasing event), and the loop **mutates that shared object in place**. The **first** call looks
right — `{'retries': 3, 'timeout': 60}` — so a single-call test passes and blesses the change.
The **second** call exposes it: the mutation from call one persists, so `build_config({"retries":
5})` returns `{'retries': 5, 'timeout': 60}` instead of `{'retries': 5, 'timeout': 30}` — the
`timeout: 60` leaked across calls. The deciding battery is a **call sequence**; one call cannot
reveal it. The true refactor hoists the constant but **copies** it per call (`dict(DEFAULTS)`),
preserving per-call independence.

**Diagnoses.** A learner who tests **one call**, sees it identical, and says "refactor" fell into
the central Advanced trap (§5c, tests-pass-so-safe) — the battery never exercised the cross-call
state. A learner who can't explain *why* the second call leaks is showing an **A1 aliasing/shared-
mutable gap** inside a refactor (§2 soft-prereq) — name it. Strong: runs a **sequence**,
classifies behavior change, names the second call as the deciding input, ties it to aliasing-the-
shared-dict, and gives the copy-per-call true refactor.

---

## A3 — "Factor out the division" — integer re-association survives shallow testing

**Setup.** `scaled` computes `(a * b) // c` with **integer** floor division. A teammate "factors
out the division" to `a * (b // c)` — algebraically equal over the reals, **not** over integers.
It passes on inputs that happen to divide evenly and fails on others.

```python
# BEFORE
def scaled(a, b, c):
    return (a * b) // c
```

```python
# CANDIDATE — "factored the division out"
def scaled(a, b, c):
    return a * (b // c)
```

> **Your turn:** Is the candidate behavior-preserving? Some inputs agree — which inputs would you
> deliberately choose to try to **break** it, and what does each version return?
>
> (Take your best guess — wrong attempts are useful data.)

**Runner-verified evidence** (note which inputs agree — those would hide the bug)

```
inputs: (10,3,2) (10,2,5) (7,6,4) (100,1,1) (3,5,5)

BEFORE stdout:        CANDIDATE stdout:
(10, 3, 2) -> 15      (10, 3, 2) -> 10      <-- DIFFERS
(10, 2, 5) -> 4       (10, 2, 5) -> 0       <-- DIFFERS
(7, 6, 4) -> 10       (7, 6, 4) -> 7        <-- DIFFERS
(100, 1, 1) -> 100    (100, 1, 1) -> 100    (agree — would hide the bug)
(3, 5, 5) -> 3        (3, 5, 5) -> 3        (agree — would hide the bug)

stdout identical: False
VERDICT: BEHAVIOR CHANGED  ✗  → NOT a refactor
```

**Why.** Floor division doesn't distribute over multiplication: `(a*b)//c` floors **after**
multiplying; `a*(b//c)` floors `b//c` **first**, throwing away the remainder, then multiplies the
error by `a`. For `(10,3,2)`: `(30)//2 = 15` vs `10*(3//2) = 10*1 = 10`. The danger is that inputs
where `c` divides `b` evenly (`(100,1,1)`, `(3,5,5)`) **agree** — so a battery built from
"convenient" inputs passes and **blesses the bug**. To *decide* this you must deliberately choose
inputs where `b//c` has a **remainder** (`3//2`, `2//5`, `6//4`). This is the B3 skill —
adversarial case selection — in service of D3: the battery must include the inputs that *could*
falsify equivalence, not the ones that happen to agree.

**Diagnoses.** A learner who tries `(100,1,1)` and `(3,5,5)`, sees them agree, and concludes
"refactor" committed the central Advanced trap (§5c, tests-pass-so-safe) — they sampled the
inputs that *hide* the change. A learner who says "multiplication and division commute, so it's
fine" is applying a **real-number** identity to **integer** arithmetic — name the floor-division
remainder as the gap. Strong: *deliberately* picks remainder-producing inputs, classifies behavior
change, identifies `(10,3,2)`/`(10,2,5)`/`(7,6,4)` as deciding (and notes the agreeing ones would
hide it), and explains floor-division non-distribution. A teach-back: "algebraic identities over
the reals are not behavior-preserving over ints — verify by running, don't trust the algebra."
</content>
