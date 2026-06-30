# D3 — Foundations exemplars (refactoring judgment)

Golden drills for the **Foundations** tier of module D3. Each is **one clear,
behavior-preserving move** on a familiar surface — extract a duplicated sub-expression,
turn an index loop into a comprehension, replace a magic number with a named constant.
**No behavior-changing trap at this tier.** The skill is: **perform the move (or confirm a
given AFTER preserves behavior) and name the structural smell it fixes** — and *confirm*
preservation by running, never by eyeballing.

D3 is graded **hybrid** (`drill-generation.md` §1d): the **behavior-preservation** sub-claim is
**executable** — the coach runs the SAME input battery through BEFORE and AFTER and diffs
`stdout`/`status` (`drill-generation.md` §2); the **judgment** (what smell, is this the right
move) is rubric. Every BEFORE/AFTER pair below was **run** and confirmed **identical**:

```
python <skill-dir>/runtime/python/runner.py snippet.py   # run BEFORE and AFTER, diff stdout/status
```

Coverage spans distinct moves (**extract-variable / loop→comprehension / magic→constant**), each
genuinely behavior-preserving. Pose one, **hard-stop, wait** (`coaching-loop.md`). **How to
grade** against module §7: **AX1** (executable) = predicted the (unchanged) output, confirmed by
running BEFORE vs AFTER identical; **AX2** (rubric) = named the structural smell the move fixes,
and did **not** claim safety without the run. A learner who says "obviously same, no need to run"
has the right answer but the wrong *discipline* — name it: preservation is **decided by running**,
even when it looks safe (§5c, judges-by-reading-not-running).

---

## F1 — Extract a duplicated sub-expression into a variable

**Smell.** `qty * unit` is computed twice on the same line (duplicated sub-expression). The
behavior-preserving move is **extract variable**: compute `subtotal` once, use it twice.

```python
# BEFORE
def price_with_tax(items):
    out = []
    for qty, unit in items:
        out.append(qty * unit + qty * unit * 0.08)   # qty*unit computed twice
    return out
```

```python
# AFTER (proposed refactor)
def price_with_tax(items):
    out = []
    for qty, unit in items:
        subtotal = qty * unit
        out.append(subtotal + subtotal * 0.08)
    return out
```

> **Your turn:** Is the AFTER a behavior-preserving refactor? What structural smell does it fix,
> and what does `price_with_tax([(2, 10.0), (1, 5.0), (3, 2.5)])` print for **each** version?
>
> (Take your best guess — wrong attempts are useful data.)

**Runner-verified evidence** (same battery through BEFORE and AFTER)

```
inputs: [(2,10.0),(1,5.0),(3,2.5)] ; [] ; [(0,99.0)]

BEFORE stdout:                       AFTER stdout:
[21.6, 5.4, 8.1]                     [21.6, 5.4, 8.1]
[]                                   []
[0.0]                                [0.0]

stdout identical: True   status identical: True (both ok)
VERDICT: behavior preserved  ✓  → this IS a refactor
```

**Why.** Extract-variable computes the same value, so the arithmetic is unchanged — `2*10.0 +
2*10.0*0.08 = 21.6` either way. The smell it fixes is the **duplicated sub-expression**: one
place to read it, one place to change the tax base if needed. (The `0.08` is itself a magic
number — a *separate*, also-behavior-preserving move; don't bundle it in this step. One change at
a time.)

**Diagnoses.** A learner who gets the output right but says "no need to run it, it's obviously the
same" has the **answer** but is skipping the **discipline** (§5c, judges-by-reading-not-running) —
at Foundations that's fine for the verdict but flag it: the *habit* of running BEFORE vs AFTER is
what catches the Working-tier traps later. A learner who can't name the smell ("it just looks
cleaner") has AX2 partial — push for "duplicated sub-expression." Strong: confirms identical
output, names extract-variable, notes the move doesn't touch the math.

---

## F2 — Turn an index loop into a comprehension

**Smell.** `for i in range(len(names))` then `names[i]` is a C-style index loop where direct
iteration reads clearer (and `[... for ...]` replaces the manual accumulator). Both moves are
behavior-preserving.

```python
# BEFORE
def label_lengths(names):
    result = []
    for i in range(len(names)):
        result.append(len(names[i]))
    return result
```

```python
# AFTER (proposed refactor)
def label_lengths(names):
    return [len(name) for name in names]
```

> **Your turn:** Is the AFTER behavior-preserving? What does each version print for
> `label_lengths(["ada", "grace", "linus", ""])` and for `label_lengths([])`?
>
> (Take your best guess — wrong attempts are useful data.)

**Runner-verified evidence**

```
inputs: ["ada","grace","linus",""] ; []

BEFORE stdout:        AFTER stdout:
[3, 5, 5, 0]          [3, 5, 5, 0]
[]                    []

stdout identical: True   status identical: True (both ok)
VERDICT: behavior preserved  ✓
```

**Why.** `range(len(names))` visits indices `0..len-1`; direct iteration visits the same elements
in the same order; the comprehension builds the same list. The empty case is preserved too
(`range(0)` is empty; the comprehension over `[]` is `[]`). Note the empty string `""` correctly
maps to `0` in both — a small reassurance the move didn't drop the falsy element. Smell fixed:
**index indirection** replaced by direct iteration; manual append/accumulator replaced by a
comprehension.

**Diagnoses.** A learner who worries "does the comprehension handle the empty list?" and **checks
by running** is doing exactly the right thing — reward the instinct even though the answer is yes.
A learner who claims it's safe without considering the empty case has AX1 partial: the boundary
(empty input) is precisely where a loop→comprehension move *could* differ if written carelessly,
so it belongs in the battery. Strong: identical output incl. the empty case, names the move.

---

## F3 — Replace a magic number with a named constant

**Smell.** The literal `86400` is a magic number — its meaning (seconds in a day) is implicit.
The behavior-preserving move is **replace magic literal with a named constant**.

```python
# BEFORE
def days_to_seconds(days):
    return days * 86400
```

```python
# AFTER (proposed refactor)
SECONDS_PER_DAY = 86400

def days_to_seconds(days):
    return days * SECONDS_PER_DAY
```

> **Your turn:** Is the AFTER a refactor (behavior-preserving)? What does each version print for
> `days_to_seconds(1)`, `days_to_seconds(0)`, and `days_to_seconds(2.5)`?
>
> (Take your best guess — wrong attempts are useful data.)

**Runner-verified evidence**

```
inputs: 1 ; 0 ; 2.5

BEFORE stdout:    AFTER stdout:
86400             86400
0                 0
216000.0          216000.0

stdout identical: True   status identical: True (both ok)
VERDICT: behavior preserved  ✓
```

**Why.** A named constant bound to the *same value* changes nothing the program computes —
`days * 86400` and `days * SECONDS_PER_DAY` are identical, including the float case
(`2.5 * 86400 = 216000.0`, a float, in both). The smell fixed is the **magic number**: the name
documents intent and gives one place to change the value. This is the purest illustration that a
refactor can improve *readability* with provably zero behavior change.

**Diagnoses.** Almost everyone gets the verdict right; the teaching value is the *meta-point* —
name **why** this is safe (the constant holds the same value; no arithmetic changed) rather than
"it's just a rename." A learner who says "renaming can't change behavior, ever" is over-
generalizing — renaming a *variable that gets reassigned*, or shadowing a name, can change
behavior; the safety here comes from binding the **same value**, confirmed by the run. Strong:
identical output, names magic→constant, ties safety to "same value, same arithmetic."
</content>
