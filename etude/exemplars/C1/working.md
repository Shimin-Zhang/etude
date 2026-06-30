# C1 — Working exemplars (systematic debugging)

Golden drills for the **Working** tier of module C1. Each bug lives in a **context the learner
hasn't seen**, where intent and execution diverge and the **right hypothesis must be chosen
among plausible ones** — the failure does *not* always crash; sometimes it's silently wrong on
a specific input. **W3 is a bisection drill**: a short regression history where the learner
picks **where to bisect**. The skill is *observe → hypothesize (with a discriminating test) →
predict → test the fix*, and naming the mechanism. Every **buggy output, every fixed output,
every probe, and every commit's behavior below was obtained by running it through the runner**
(`drill-generation.md` §2):

```
python <skill-dir>/runtime/python/runner.py snippet.py
```

Coverage spans three distinct points in the parameter space: **aliasing / shared mutable
reference** (a silent wrong result), an **`or`-default that swallows a legitimate falsy value**
(wrong only on one input), and a **bisection over a regression history**. Pose one,
**hard-stop, wait** (`coaching-loop.md`). **How to grade** against module §7 (executable +
hybrid, §5d): **fix is executable** (apply + re-run); **hypothesis is rubric-graded** (specific?
**discriminating** predicted observation? names the mechanism?). For the bisection drill, the
**first-bad commit is executable ground truth**; "did you bisect on a discriminating test in
`O(log n)`" is rubric-graded. A working fix via a vague hypothesis is a **partial pass** — flag
the inverted method.

---

## W1 — Aliasing: one cell write changes a whole column

**Spec.** `make_board(n)` returns a fresh `n × n` grid of zeros. Writing one cell must change
**only** that cell.

```python
def make_board(n):
    return [[0] * n] * n

board = make_board(3)
board[0][0] = 1          # intend to set ONLY the top-left cell
for row in board:
    print(row)
```

> **Your turn:** Run it and observe what gets printed. That's surprising — form a hypothesis
> for *why* setting one cell changed more than one, name a **test that would confirm your
> hypothesis**, then predict what the fix prints and give the fix.
>
> (Take your best guess — wrong attempts are useful data.)

**Runner-verified evidence** (the bug is real; the `is` check is the discriminating test)

```
buggy   board[0][0] = 1  ->  stdout:
        [1, 0, 0]
        [1, 0, 0]
        [1, 0, 0]                      <-- a whole COLUMN changed, not one cell

probe   board[0] is board[1]  ->  "row 0 is row 1? True\n"   <-- rows are the SAME object
fixed   board[0][0] = 1  ->  stdout:
        [1, 0, 0]
        [0, 0, 0]
        [0, 0, 0]                      (fix: [[0] * n for _ in range(n)])
status: ok
```

**Gold hypothesis + diagnosis.** `[[0] * n] * n` builds the inner list `[0, 0, 0]` **once** and
then makes the outer list hold **`n` references to that same inner list** — not `n` independent
rows. So `board[0]`, `board[1]`, `board[2]` are **one object**; `board[0][0] = 1` mutates it,
and every row "sees" the change. The **discriminating test** is identity, not value:
`board[0] is board[1]` returns `True` (aliases) — if they were independent rows it'd be
`False`. The fix is a comprehension `[[0] * n for _ in range(n)]`, which evaluates a **fresh**
inner list each iteration; re-running shows only `board[0][0]` changed.

**Model debugging trace (the gold).**

> *Observe:* ran it — setting `board[0][0]` turned the whole **first column** to `1`. *Hypothesis:*
> the three rows are the **same list object** (the `* n` on the outer list copies the reference,
> not the row). *Discriminating test:* `board[0] is board[1]` → `True`, confirms shared identity.
> *Predict the fix:* build each row independently with a comprehension so the rows are distinct;
> then `board[0][0] = 1` should leave rows 1 and 2 as `[0, 0, 0]`. *Test:* re-ran with
> `[[0] * n for _ in range(n)]` → exactly one cell changed. Confirmed.

**Diagnoses.** A learner who says "the list is weird" or "it's a reference thing" without the
`is` test has a **vague hypothesis** and **no discriminating test** (§5c). A learner who
"fixes" it by reassigning each cell in a loop but never identifies the shared reference got a
fix without the mechanism (§5c, partial pass). A learner who can't reproduce the surprise
before theorizing skipped *Observe*. Strong attempt: runs it, hypothesizes shared row identity,
confirms with `is`, fixes with the comprehension, re-runs. Bug class: **aliasing / shared
mutable reference** (Catalog §5c; an A1 notional-machine event seen as a failure).

---

## W2 — The `or`-default that swallows a waived `0`

**Spec.** `apply_fee(base, fee=None)` returns `base + fee`. When `fee` is **omitted**, a
standard fee of `2` applies. But a caller who passes `fee=0` (a fee-**waived** order) must get
`base + 0`.

```python
def apply_fee(base, fee=None):
    fee = fee or 2          # default fee is 2 when not specified
    return base + fee

print(apply_fee(100))       # no fee given -> 102
print(apply_fee(100, 5))    # explicit 5  -> 105
print(apply_fee(100, 0))    # fee waived  -> spec wants 100
```

> **Your turn:** Run all three calls and observe. Two look right — which one is wrong, what's
> your hypothesis for the cause, what do you predict the fix prints, and what's the fix?
>
> (Take your best guess — wrong attempts are useful data.)

**Runner-verified evidence** (the bug surfaces on exactly one input)

```
buggy  -> 102        (no fee: correct)
          105        (fee 5:  correct)
          102        <-- WRONG: fee waived (0) but charged 2; spec wants 100
fixed  -> 102
          105
          100        (fix: `if fee is None: fee = 2`)
status: ok
```

**Gold hypothesis + diagnosis.** `fee or 2` returns `2` whenever `fee` is **falsy** — and `0`
is falsy. So a caller who explicitly passes `fee=0` (waived) gets `2` substituted, and
`apply_fee(100, 0)` returns `102` instead of `100`. The `or`-default cannot tell "**not
supplied**" (`None`) from "**supplied as zero**" (`0`). The fix tests for the actual sentinel:
`if fee is None: fee = 2`, which leaves a real `0` intact. The discriminating prediction is
specific: the *waived* call goes `102 → 100`, while the other two are unchanged.

**Model debugging trace (the gold).**

> *Observe:* ran all three — `apply_fee(100, 0)` returned `102`, not `100`. *Hypothesis:*
> `fee or 2` treats `0` as "missing" because `0` is falsy, so the waived fee is overwritten by
> the default. *Predict:* replacing the `or`-default with an explicit `is None` check makes the
> waived call return `100` and leaves the other two at `102`/`105`. *Test:* re-ran with
> `if fee is None: fee = 2` → `102, 105, 100`. Confirmed; the other cases didn't regress.

**Diagnoses.** A learner who predicts only "it'll be wrong" gave a **non-discriminating
prediction** (true under many causes — §5c); the sharp version names *which* call and *why
`0` is falsy*. A learner who never runs the `fee=0` case may not see the bug at all (§5c,
fix-before-observe / did-not-trace) — it's invisible on the happy path. A learner who changes
`or 2` to `or 2` something without distinguishing `None` from `0` hasn't fixed the root — have
them re-run the waived case. Bug class: **truthiness / `or`-default swallowing a falsy value**
(Catalog §5c; A1 short-circuit semantics — `or` returns the first truthy operand).

---

## W3 — Bisection: a regression in `normalize_spaces`

**Spec.** `normalize_spaces(s)` collapses any run of whitespace (spaces, tabs, newlines) to a
single space and strips the ends. So `normalize_spaces("a\tb\nc") == "a b c"`.

**The situation.** The function used to work; now it's wrong. There are **6 commits** between
the last-known-good release (`c1`) and now (`c6`), each a small diff. A user reports:
`normalize_spaces("a\tb\nc")` returns `'a\tb\nc'` (tabs/newlines no longer collapse). Here is
the history — find the **first bad commit** by bisecting.

```
c1  (last good release):  return " ".join(s.split())
c2:  + add docstring "Collapse whitespace runs to single spaces; strip ends."  (body unchanged)
c3:  switch to regex:     return re.sub(r"\s+", " ", s).strip()
c4:  "optimize" regex:    return re.sub(r" +", " ", s).strip()
c5:  + handle None:       if s is None: return ""   (then the c4 body)
c6  (HEAD):  + lowercase: ... .strip().lower()      (then the c5 body)
```

> **Your turn:** You want to find the first commit where `normalize_spaces("a\tb\nc")` stops
> returning `'a b c'`. **(1)** What **test input** will you bisect on — and why must it be that
> one, not `"  hello   world  "`? **(2)** You can check out any commit and run it. Which commit
> do you test **first** to halve the search, and how do you proceed? **(3)** Which commit is
> the first bad one, and what's the fix?
>
> (Take your best guess — wrong attempts are useful data.)

**Runner-verified evidence** (each commit run on the discriminating test `normalize_spaces("a\tb\nc")`)

```
c1: 'a b c'      -> GOOD
c2: 'a b c'      -> GOOD
c3: 'a b c'      -> GOOD
c4: 'a\tb\nc'    -> BAD      <-- FIRST BAD COMMIT (the \s+ -> ' +' change)
c5: 'a\tb\nc'    -> BAD
c6: 'a\tb\nc'    -> BAD

# why NOT bisect on "  hello   world  ":  it returns 'hello world' in ALL six commits (only
# spaces between words), so it cannot tell good from bad -- a non-discriminating test.
#   c1 'hello world' ... c6 'hello world'   (every commit "passes" -> bisection learns nothing)
```

**Gold answer.**

1. **Bisect on `"a\tb\nc"`** (or any input containing a **tab or newline**). The reported
   regression is specifically about **non-space whitespace**; `"  hello   world  "` has only
   spaces between words, so it returns `'hello world'` in **every** commit — it can't
   distinguish good from bad. The bisection test **must reproduce the actual failure**, i.e.
   it must be one the *good* version passes and the *bad* version fails.
2. **Test the midpoint first.** With 6 commits `c1..c6`, check `c3` (or `c4`): `c3` →
   `'a b c'` (GOOD), so the regression is in the **upper half** `c4..c6`. Test the midpoint of
   that half, `c4` (or `c5`): `c4` → `'a\tb\nc'` (BAD). Since `c3` is good and `c4` is bad,
   **`c4` is the first bad commit**. That's `⌈log₂ 6⌉ = 3` checks at most, versus scanning all
   six.
3. **First bad commit: `c4`.** The diff replaced the whitespace class `\s+` (spaces, tabs,
   newlines) with `" +"` (literal spaces only), so tabs and newlines are no longer collapsed.
   **Fix:** restore the whitespace class — `re.sub(r"\s+", " ", s)`. (`c5`'s `None`-guard and
   `c6`'s `.lower()` are unrelated changes layered on top of the already-broken regex — classic
   camouflage; they're *not* the cause.)

**Model debugging trace (the gold).**

> *Observe / make it fail:* reproduced — at HEAD, `normalize_spaces("a\tb\nc")` returns
> `'a\tb\nc'`, not `'a b c'`. *Choose a discriminating test:* it must involve a tab/newline;
> `"  hello   world  "` is useless because it passes everywhere. *Divide and conquer:* `c3`
> passes, `c4` fails → first-bad is `c4`. *Diagnose:* the `\s+` → `" +"` regex change dropped
> tab/newline handling. *Fix + test:* restore `\s+`, re-run the failing input → `'a b c'`.
> Confirmed; ignored `c5`/`c6` as unrelated layers.

**Diagnoses.** A learner who picks `"  hello   world  "` (or "just run the tests") to bisect
chose a **non-discriminating test** (§5c, bisecting on a probe that passes in both good and
bad) — the central bisection error; show them it returns `'hello world'` in every commit. A
learner who **scans c1→c6 linearly** instead of halving has no divide-and-conquer (§5c). A
learner who blames `c6`'s `.lower()` or `c5`'s `None`-guard **anchored on the most recent /
most visible change** (confirmation tunnel — §5c) without testing the midpoint. Strong attempt:
discriminating test, midpoint probe, lands on `c4` in ≤3 checks, restores `\s+`, re-runs. Bug
class: **regression localized by bisection** (Catalog §5c; Zeller & Hildebrandt — halve the
search; Agans "divide and conquer").
