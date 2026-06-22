# F1 — Working exemplars (metacognition & calibration)

Golden drills for the **Working** tier of module F1: a **short battery** of ~3 snippets of
**varied trickiness**, each a predict + confidence rating, then **measure hit-rate vs.
average confidence** (over/under-confident?) and read the **ordering**. Every battery
**must include ≥1 deceptively-simple-looking-but-tricky case** — a calibration trap.

Every answer key was obtained by **running each snippet through the runner**
(`drill-generation.md` §2); the coach never guesses — calibration is measured against
**real** output:

```
python <skill-dir>/runtime/python/runner.py snippet.py
```

Pose the battery, **hard-stop, wait** for all three predictions+confidences (`coaching-loop.md`),
*then* run and score. The calibration **verdict** lives in the **batch**, not any one item
(`assessment.md` F1 task: ≥3 trials to read a pattern). The model exemplar **W1** is a full
3-snippet battery with a worked scoring; **W2** and **W3** are alternative batteries on
different parameter-space regions.

---

## W1 — The model battery (genuine-easy · trap · genuine-hard) with worked scoring

Pose all three **before** revealing anything; collect a confidence and a prediction for each.

**Snippet (a) — genuinely easy**
```python
print(list(range(1, 10, 3)))
```
**Snippet (b) — deceptively simple (the trap)**
```python
print(0.1 + 0.2 == 0.3)
```
**Snippet (c) — genuinely hard (aliasing + rebinding)**
```python
a = [1, 2]
b = a
a += [3]
a = a + [4]
print(b)
```

> **Your turn:** For each of (a), (b), (c): first state your confidence (0–100%) you'll get
> it exactly right, then predict the output. Do all three before I run anything.
>
> (Take your best guess — wrong attempts are useful data.)

**Runner-verified answer key**

```
(a)  python runner.py a.py  → stdout: "[1, 4, 7]\n"   status: ok
(b)  python runner.py b.py  → stdout: "False\n"        status: ok
(c)  python runner.py c.py  → stdout: "[1, 2, 3]\n"    status: ok
```

So: **(a) `[1, 4, 7]`**, **(b) `False`**, **(c) `[1, 2, 3]`**.

**Why each answer.**
- **(a)** `range(1, 10, 3)` steps by 3 from 1, stopping before 10: `1, 4, 7` (10 excluded).
- **(b)** `0.1 + 0.2` is `0.30000000000000004` in binary float, so `== 0.3` is `False`.
- **(c)** `b = a` aliases the same list. `a += [3]` is an **in-place** `__iadd__` →
  the **shared** object becomes `[1, 2, 3]`, and `b` sees it. Then `a = a + [4]` **builds a
  new list and rebinds `a`** to `[1, 2, 3, 4]` — but `b` still labels the **original**
  object, now `[1, 2, 3]`. So `b` is `[1, 2, 3]`. (The `+=`-mutates-then-`+`-rebinds split
  is the trap inside the hard one.)

**How to score the calibration — worked example.** Suppose a learner answered:

| Snippet | Difficulty | Confidence | Predicted | Actual | Correct? |
|---|---|---|---|---|---|
| (a) | easy | 90% | `[1, 4, 7]` | `[1, 4, 7]` | ✅ |
| (b) | trap | 85% | `True` | `False` | ❌ |
| (c) | hard | 80% | `[1, 2, 3, 4]` | `[1, 2, 3]` | ❌ |

- **Hit rate = 1/3 ≈ 33%. Average confidence = (90+85+80)/3 = 85%.** Confidence (85%) **far
  exceeds** hit rate (33%) ⇒ **overconfident** on this batch.
- **Ordering is broken too:** confidence barely moved across wildly different difficulty
  (90 → 85 → 80), the **flat-high / hard–easy-effect** signature — accuracy collapsed on the
  hard items but the number didn't (Lichtenstein & Fischhoff 1977).
- **The costly miss is (b):** an 85% on a snippet that *looks* trivial is the **fluency
  trap** — confidence bought by smooth reading, not by knowing floats behave oddly. That is
  the single most important pair to surface.
- **(c) is a wrong-and-fairly-confident hard miss** — name the *mechanism* gap (`+=` mutates
  the shared list, then `+` rebinds only `a`), and note the confidence should have *dropped*
  here, not stayed at 80%.

A **well-calibrated** learner on the same battery might look like 90% / **45%** / **40%**
(confidence *tracks* difficulty), get (a) right and flag genuine doubt on (b) and (c) — even
if they also miss (b)/(c), their **ordering is right** and they are *not* overconfident.

**Diagnoses.** Flat confidence across varied difficulty → no-discrimination calibration
(catalog §5c, hard–easy). High confidence on (b) → fluency trap. Crucially, the coach grades
the **batch relationship** (avg-conf vs. hit-rate, plus ordering), **not** the 1/3 score —
and does **not** let the learner conflate "I got 1 of 3" with "I was badly calibrated"; those
are different findings. (Catalog §5c; module §3 calibration rule.)

---

## W2 — Alternative battery: includes an *under*-confidence probe

Different parameter-space region: this battery's trap is a snippet that **looks scary but is
simple** (to surface *under*-confidence), alongside a real trap and a real-hard item.

**Snippet (a) — looks scary, is linear (under-confidence probe)**
```python
total = 0
for i in range(1, 6):
    for _ in range(i):
        total += 1
print(total)
```
**Snippet (b) — deceptively simple (trap)**
```python
print(2 ** 3 ** 2)
```
**Snippet (c) — genuinely hard (short-circuit returns an operand)**
```python
print("" or 0 or "fallback")
```

> **Your turn:** For each, state confidence (0–100%) then predict. All three before I run
> anything.
>
> (Take your best guess — wrong attempts are useful data.)

**Runner-verified answer key**

```
(a)  stdout: "15\n"           status: ok
(b)  stdout: "512\n"          status: ok
(c)  stdout: "fallback\n"     status: ok
```

So: **(a) `15`**, **(b) `512`**, **(c) `fallback`**.

**Why each answer.**
- **(a)** The inner loop runs `i` times for `i = 1..5`, so `total = 1+2+3+4+5 = 15`. The
  nested loops *look* intimidating but it's a plain triangular sum — **no trick**.
- **(b)** `**` is **right-associative**: `3 ** 2 = 9` first, then `2 ** 9 = 512` — **not**
  `(2**3)**2 = 64`. The trap.
- **(c)** `or` returns the **first truthy operand unchanged** (an operand, not a bool):
  `""` is falsy, `0` is falsy, so it returns `"fallback"`.

**How to score the calibration.** (a) is the **under-confidence probe**: a learner who rates
it **30%** out of intimidation and then gets `15` right is **under-confident** — real
knowledge given no credit (less costly than overconfidence, but still miscalibration;
Dunlosky & Rawson 2012). (b) is the overconfidence trap (right-associativity); a confident
`64` is the fluency-trap miss. (c) is the genuine-hard item. A well-calibrated learner's
confidence is **high on (a)** (it only looks hard) and **lower on (b)/(c)** — the inverse of
the naive "long code = scary, short code = easy" heuristic.

**Diagnoses.** Low confidence + correct on (a) → under-confidence. High confidence + `64` on
(b) → overconfidence via the precedence trap. The battery teaches that **apparent** difficulty
(length, nesting) is a *bad* cue for confidence; **actual** difficulty (does the behavior
diverge from the obvious reading?) is the right cue. (Catalog §5c, under-confidence + fluency
entries.)

---

## W3 — Alternative battery: the *ranking* variant (relative calibration, no absolute numbers)

Same predict-then-check engine, but the confidence scale is a **forced ranking** — tests
*relative* calibration (does the learner know which they're least sure of?) without absolute
percentages.

**Snippet (a)**
```python
print(7 // 2, 7 / 2, -7 // 2)
```
**Snippet (b)**
```python
print(bool("False"))
```
**Snippet (c)**
```python
print([0] * 3)
print([[0]] * 3)
```

> **Your turn:** Predict the output of all three. Then **rank them** from the one you're
> *most* sure about to the one you're *least* sure about — before I run anything.
>
> (Take your best guess — wrong attempts are useful data.)

**Runner-verified answer key**

```
(a)  stdout: "3 3.5 -4\n"            status: ok
(b)  stdout: "True\n"                status: ok
(c)  stdout: "[0, 0, 0]\n[[0], [0], [0]]\n"   status: ok
```

So: **(a) `3 3.5 -4`**, **(b) `True`**, **(c) `[0, 0, 0]` then `[[0], [0], [0]]`**.

**Why each answer.**
- **(a)** `//` floors: `7 // 2 = 3`; `7 / 2 = 3.5` (true division); `-7 // 2 = -4`
  (**floors toward negative infinity**, not truncates toward zero — the trap).
- **(b)** `bool("False")` is `True` — **any non-empty string is truthy**; the *content*
  `"False"` is irrelevant. The trap.
- **(c)** `[0] * 3` is fine: `[0, 0, 0]`. `[[0]] * 3` *looks* analogous but here it prints
  `[[0], [0], [0]]` — and the **hidden** danger (not visible from this print) is that the
  three inner lists are the **same** object, so mutating one mutates all. The genuinely-hard
  one.

**How to score the calibration.** Grade the **ordering**: a well-calibrated learner ranks
(c) (and the `-7 // 2` part of (a), and (b)) as their **least sure**, and that ranking should
**match where they were actually wrong**. If the learner ranks (a) "most sure" and gets the
`-4` wrong, their *ordering* failed — they were most confident on a miss. Relative
calibration is "did your most-sure beat your least-sure on accuracy?" — and it needs **no
absolute numbers**, which is useful for learners who anchor arbitrarily on percentages.

**Diagnoses.** Most-sure item is a miss → broken ordering (the relative-calibration failure).
The ranking format isolates **discrimination** (do you know what you don't know?) from
**absolute bias** (are your numbers globally too high?). A learner can have good ordering but
global overconfidence, or vice versa — the coach reports which. (Catalog §5c; module §3,
ordering signal.)
