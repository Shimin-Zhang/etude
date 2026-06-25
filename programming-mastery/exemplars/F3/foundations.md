# F3 — Foundations exemplars (learning new languages & frameworks fast)

Golden drills for the **Foundations** tier of module F3: **one construct**, a clear
true/false-friend mapped from a **close** source language (C-family / JavaScript). The
learner names the source-language analogy, **predicts the behavior under it**, and the
coach **runs it** to convict (or confirm) the mapping — then they name what is the *same*
and what is *different*. Grading is **hybrid** (`drill-generation.md` §3): the prediction is
**executable** (run it, never guess); the *mapping* is **rubric-graded** against the gold
below and is explicitly softer. Every prediction key was obtained by **running the snippet
through the runner**:

```
python <skill-dir>/runtime/python/runner.py snippet.py
```

Coverage spans three distinct construct families (chained comparison / string-int
concatenation / `++`), three source analogies (C · JavaScript · universal), and three
predicted artifacts (a bool · *whether it raises* · a value) — no repeated gotcha. The
**worked example in the module (`/`, `//`, `%`) is not reused here.** Pose one,
**hard-stop, wait** (`coaching-loop.md`).

---

## Fnd-1 — Chained comparison `1 < 3 < 2` (false friend from C / Java)

> You know **C / Java**. There, `a < b < c` evaluates **left to right**: `(a < b) < c`,
> where `a < b` becomes `1` or `0` and then gets compared to `c`.

```python
print(1 < 3 < 2)
print(3 < 2 < 1)
```

> **Your turn:** Map `1 < 3 < 2` onto the C analogy and predict each line. Then: is `<`
> a true friend or a false friend here, and why?
>
> (Take your best guess — wrong attempts are useful data.)

**Runner-verified prediction key**

```
stdout: "False\nFalse\n"
status: ok
```

So both lines print `False`. Under the C analogy you would have predicted **`True`** for
`1 < 3 < 2` (`(1<3)<2` → `True<2` → `1<2` → `True`) and **`True`** for `3 < 2 < 1`
(`(3<2)<1` → `False<1` → `0<1` → `True`). Both predictions are wrong — the construct is a
false friend.

**Gold mapping.** *Analogy:* C/Java `a < b < c` = `(a < b) < c`, left-associated.
*Classify:* **false friend** — same surface, different behavior. *Why:* Python does **not**
left-associate comparisons; `a < b < c` is **chained**, meaning `(a < b) and (b < c)` with
`b` evaluated once. So `1 < 3 < 2` is `(1 < 3) and (3 < 2)` = `True and False` = `False`.
*Repaired mapping:* in Python, a chain is a conjunction of neighbouring comparisons, not a
fold of booleans — the very feature that makes `0 <= i < len(xs)` read naturally is the one
that breaks the imported C reading.

**Why.** The danger is that the surface `1 < 3 < 2` is **character-identical** across the
two languages; only running it separates them. A learner who "reads" the line in C cannot
see the difference — they have to execute it.

**Diagnoses.** Predicting `True` reveals **false-friend over-trust**: the analogy
(left-associated comparison) was reported as the answer without testing it, and the
construct's genuinely-different Python semantics (chaining) were invisible. (Catalog §5c,
entries 1 & "wrong analogy"; the root inversion — surface analogy as conclusion.)

---

## Fnd-2 — `"3" + 4` (false friend from JavaScript)

> You know **JavaScript**. There, `"3" + 4` **coerces** the number to a string and
> concatenates → `"34"`. `+` is happy to mix a string and a number.

```python
print("3" + 4)
```

> **Your turn:** Map `+` onto the JS analogy and predict what this prints. Then: true
> friend or false friend, and why?
>
> (Take your best guess — wrong attempts are useful data.)

**Runner-verified prediction key**

```
status: error   (returncode 1)
stderr (tail):
    print("3" + 4)
          ~~~~^~~
TypeError: can only concatenate str (not "int") to str
```

So it does **not** print `"34"` — it **raises `TypeError`**. Under the JS analogy you would
have predicted the string `34`; the construct is a false friend.

**Gold mapping.** *Analogy:* JS `+` does implicit string/number coercion (`"3" + 4 === "34"`).
*Classify:* **false friend** — same operator surface, different behavior. *Why:* Python's
`+` does **no** implicit string↔number coercion; `str + int` has no defined behavior, so it
raises `TypeError` rather than guessing your intent. *Repaired mapping:* to concatenate you
must convert explicitly — `"3" + str(4)` → `"34"`, or `f"{3}{4}"`; to add, `int("3") + 4` →
`7`. The concept "combine a string and a number" exists in both, but Python forces you to
say *which* combination you mean.

**Why.** This is the false friend that fails **loudly** (a `TypeError`), which is the *kind*
case — contrast Fnd-1, which fails *silently* with a wrong `False`. The teaching is the same:
predict under the analogy, run, and let the machine — here, the traceback — convict it. (The
coach reads `status`/`stderr`, not a guess; `drill-generation.md` §2.)

**Diagnoses.** Predicting `"34"` reveals **mistaking one language's model for universal**
(JS's implicit coercion assumed to hold everywhere) — a far-transfer failure where the
abstraction "`+` coerces" was never checked against Python's stricter model. (Catalog §5c,
"over-generalizes one language's model"; false-friend over-trust.)

---

## Fnd-3 — `++x` does not increment (absent construct from C / Java / JS)

> You know **C / Java / JavaScript**. All of them have `++` — `++x` (or `x++`) **increments
> `x` by one**.

```python
x = 5
print(++x)
print(x)
```

> **Your turn:** Map `++x` onto the increment operator you know and predict both lines.
> Then: does Python have a `++` operator?
>
> (Take your best guess — wrong attempts are useful data.)

**Runner-verified prediction key**

```
stdout: "5\n5\n"
status: ok
```

So it prints `5`, then `5` — `x` is **not** incremented. Under the `++` analogy you would
have predicted `6` (and `x` left at `6`). The construct does not exist; the surface lies.

**Gold mapping.** *Analogy:* C/Java/JS `++x` increments. *Classify:* **genuinely-absent
construct that silently parses as something else** — the most dangerous false friend,
because it neither errors nor does what you meant. *Why:* Python has **no `++` operator**.
`++x` parses as `+(+x)` — **two unary-plus operations** — which for an `int` is just `x`. So
`++x` is `5`, and nothing is rebound, so `x` stays `5`. (Its sibling `x++` is worse: it is a
`SyntaxError`.) *Repaired mapping:* the increment idiom in Python is `x += 1`.

**Why.** `++x` is *valid Python* that runs cleanly and produces a plausible-looking number —
so a learner mapping from C gets **no signal at all** that their model is wrong unless they
check the value. This is why "it ran and printed a number" is not "my mapping is correct"
(§5c, last entry; corollary 1).

**Diagnoses.** Predicting `6` reveals **mistaking your first language for the universal
machine** — `++` assumed to be a feature of "programming," not of C specifically — combined
with **false-friend over-trust** (the surface `++x` was read as the increment, untested).
(Catalog §5c, "over-generalizes one language's model"; the absent-construct case.)
</content>
