# D3 — Working exemplars (refactoring judgment)

Golden drills for the **Working** tier of module D3. Each presents a candidate "refactor" that
**may or may not preserve behavior**, on a surface where intent and execution diverge (boolean
"simplification", guard-clause flatten, "extract for clarity" that drops short-circuit). The
skill is **triage + verification**: **decide refactor-vs-behavior-change, name the inputs that
decide it**, and — if it changed behavior — say **where and why**. **The central catch:** a diff
can look clean and idiomatic and *still* change behavior — that is **not a refactor**, it is a
bug (§5c, judges-by-reading-not-running).

D3 is graded **hybrid** (`drill-generation.md` §1d, §3): the coach **runs the SAME input battery
through BEFORE and AFTER and diffs** `stdout`/`status` (`drill-generation.md` §2) to settle
behavior; the judgment is rubric. Every BEFORE/candidate pair below was **run**; genuine
refactors are confirmed **identical**, fake ones **diverge** on a named input:

```
python <skill-dir>/runtime/python/runner.py snippet.py   # run BEFORE and the candidate, diff
```

Coverage spans distinct behavior-change classes (**boolean mis-simplification / lost short-
circuit / boundary**) with a genuine refactor alongside each trap. Pose one, **hard-stop, wait**
(`coaching-loop.md`). **How to grade** against module §7: **AX1** (executable) = correctly
classified refactor-vs-behavior-change and named the deciding input; **AX2** (rubric) = named the
smell the genuine move fixes and required a green test. **Crediting the clean look while missing a
behavior change is the central D3 failure — flag it** (§5c, root error).

---

## W1 — Flatten nested conditionals into guard clauses (genuine refactor)

**Smell.** A nested `if/else` ladder choosing a discount; guard clauses / a ternary read clearer.

```python
# BEFORE
def discount(customer_type, order_total):
    if customer_type == "vip":
        if order_total >= 100:
            return 0.20
        else:
            return 0.10
    else:
        if order_total >= 100:
            return 0.05
        else:
            return 0.0
```

```python
# CANDIDATE (proposed refactor)
def discount(customer_type, order_total):
    big = order_total >= 100
    if customer_type == "vip":
        return 0.20 if big else 0.10
    return 0.05 if big else 0.0
```

> **Your turn:** Is the candidate a behavior-preserving refactor? Which inputs would you run to
> **decide**, and what do BEFORE and CANDIDATE print for them?
>
> (Take your best guess — wrong attempts are useful data.)

**Runner-verified evidence** (battery hits both customer types × the `100` boundary from both
sides)

```
inputs: (vip,0) (vip,50) (vip,99) (vip,100) (vip,250)
        (regular,0) (regular,50) (regular,99) (regular,100) (regular,250)

BEFORE & CANDIDATE stdout (identical, line for line):
vip 0 0.1     vip 99 0.1     vip 250 0.2      regular 50 0.0    regular 100 0.05
vip 50 0.1    vip 100 0.2    regular 0 0.0    regular 99 0.0    regular 250 0.05

stdout identical: True   status identical: True (both ok)
VERDICT: behavior preserved  ✓  → this IS a refactor
```

**Why.** Hoisting `order_total >= 100` into `big` and collapsing each branch to a ternary changes
the *shape*, not the *decision* — every `(type, total)` lands on the same rate. The deciding
inputs are the **boundary** (`99`/`100`) for *each* customer type: those are where a flatten could
slip a `>=` into a `>`. They don't here, so it's a genuine refactor. Smell fixed: a two-level
nesting ladder replaced by guard-clause + ternary.

**Diagnoses.** A learner who says "looks fine, it's a refactor" **without naming boundary inputs**
has AX1 partial — they got lucky; the discipline is to *run the boundary*, because that's exactly
where the flatten could have changed `>=` to `>`. A learner who runs `(vip,100)` and `(regular,
100)` and confirms `0.2`/`0.05` has the right instinct. Strong: classifies genuine, names the
`99`/`100` boundary for both types as the deciding inputs, names the smell.

---

## W2 — "Simplify" a boolean with De Morgan (one version is a behavior change)

**Smell (and trap).** A guard `if not (a and b)` is "simplified." There are two tempting
rewrites; **only one is correct**. This drill hands the learner the *wrong* one and asks them to
judge it.

```python
# BEFORE — reject unless BOTH fields are present
def can_submit(has_name, has_email):
    if not (has_name and has_email):
        return "blocked"
    return "ok"
```

```python
# CANDIDATE — "I distributed the not"
def can_submit(has_name, has_email):
    if not has_name and not has_email:      # claimed equivalent to not (a and b)
        return "blocked"
    return "ok"
```

> **Your turn:** Is the candidate a behavior-preserving refactor? If not, **which input exposes
> the difference**, and what does each version return there? What would the *correct*
> simplification be?
>
> (Take your best guess — wrong attempts are useful data.)

**Runner-verified evidence** (all four truth-table rows)

```
inputs: (T,T) (T,F) (F,T) (F,F)

BEFORE stdout:          CANDIDATE stdout:
T T ok                  T T ok
T F blocked             T F ok        <-- DIFFERS
F T blocked             F T ok        <-- DIFFERS
F F blocked             F F blocked

stdout identical: False
VERDICT: BEHAVIOR CHANGED  ✗  → NOT a refactor; it is a bug

# the CORRECT De Morgan ( not a or not b ) — verified identical to BEFORE:
T T ok / T F blocked / F T blocked / F F blocked   → behavior preserved ✓
```

**Why.** De Morgan's law is `not (a and b) == (not a) or (not b)` — an **or**, not an **and**.
The candidate used `and`, so it only blocks when **both** fields are missing; the cases where
**exactly one** is missing — `(T,F)` and `(F,T)` — flip from `blocked` to `ok`. That is a real
behavior change: forms with a name but no email (or vice-versa) now wrongly submit. The deciding
inputs are precisely the **mixed** rows `(T,F)` and `(F,T)`; the all-true and all-false rows agree
and would **hide** the bug. The correct refactor, `not has_name or not has_email`, is byte-
identical to BEFORE.

**Diagnoses.** A learner who eyeballs it and says "yep, distributed the not, that's a refactor"
committed the **root D3 error** (§5c, judges-by-reading-not-running) — flag it hard: this is the
whole point of the module. A learner who senses something is off but tests only `(T,T)`/`(F,F)`
concludes "preserved" wrongly — they didn't pick the **discriminating** inputs (§5c, tests-pass-
so-safe / weak battery). Strong: classifies behavior change, names `(T,F)`/`(F,T)` as the deciding
rows, and gives the correct `or` form.

---

## W3 — "Extract the checks for clarity" (drops short-circuit — a side-effect change)

**Smell (and trap).** A combined condition `check(a) and check(b)` is "extracted into named
variables for readability." But `check` has a **side effect**, and the extraction evaluates both
eagerly — losing short-circuit. The **return value** is preserved; an **observable side effect**
is not.

```python
# BEFORE
log = []
def check(x):
    log.append(x)          # side effect: records that check ran
    return x > 0

def process(a, b):
    if check(a) and check(b):
        return "both-positive"
    return "not-both"
```

```python
# CANDIDATE — "extracted for clarity"
def process(a, b):
    a_ok = check(a)        # both now ALWAYS evaluated
    b_ok = check(b)
    if a_ok and b_ok:
        return "both-positive"
    return "not-both"
```

> **Your turn:** Is the candidate behavior-preserving? Look beyond the return value — what is the
> **observable behavior** here, and which input reveals a difference?
>
> (Take your best guess — wrong attempts are useful data.)

**Runner-verified evidence** (return value AND the side-effect log)

```
inputs: process(5,3) ; process(-1,3) ; process(5,-2)   (log printed and cleared each call)

BEFORE stdout:                       CANDIDATE stdout:
both-positive  log: [5, 3]           both-positive  log: [5, 3]
not-both       log: [-1]             not-both       log: [-1, 3]   <-- DIFFERS
not-both       log: [5, -2]          not-both       log: [5, -2]

stdout identical: False
VERDICT: BEHAVIOR CHANGED  ✗  → NOT a refactor

# a GENUINE extract — pull the whole condition into a helper that KEEPS short-circuit:
#   def _both_positive(a, b): return check(a) and check(b)
# verified identical to BEFORE, incl. log: [-1]   → behavior preserved ✓
```

**Why.** `check(a) and check(b)` **short-circuits**: if `check(a)` is falsy, `check(b)` never
runs (an A1 execution-model fact). The candidate assigns `a_ok` and `b_ok` first, so **both** run
**always**. For `process(-1, 3)` the return value is `"not-both"` either way — so a test that only
asserts the **return value** would pass and bless the "refactor" — but the side-effect log diverges:
BEFORE runs `check` once (`[-1]`), the candidate runs it twice (`[-1, 3]`). If `check` writes to a
DB, charges an API, or increments a counter, that extra call is a real behavior change. The
deciding input is one where the **first** check is falsy (`process(-1, 3)`). The genuine extract
pulls the *whole* short-circuiting condition into a helper and is identical.

**Diagnoses.** A learner who checks only the **return value**, sees it unchanged, and says
"refactor" missed that **observable behavior includes side effects**, not just the return (§5c,
judges-by-reading + confuses-improved-structure-with-preserving). This is also an **A1 short-
circuit** event seen inside a refactor (§2 soft-prereq) — a learner weak on A1 won't see why the
call count changed; name that. Strong: looks past the return value to the side effect, names
`process(-1, 3)` as the deciding input, ties it to lost short-circuit, and proposes extracting the
whole condition instead.
</content>
