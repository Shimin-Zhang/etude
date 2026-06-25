# F2 — Working exemplars (designing your own practice)

Golden drills for the **Working** tier of module F2. Each is a **mixed** routine: **2–4
anti-patterns** plus **one genuinely-good element that must NOT be "fixed."** The skill is
**triage + redesign** — critique against all five levers, **prioritize the highest-leverage
fix**, redesign, **catch the hours/comfort framing**, and **leave the good element alone**.

F2 is **rubric-graded** (`drill-generation.md` §3) — a judgment with no single correct plan; the
coach says so. Where a redesign turns a passive element into **predict-then-check**, the embedded
snippet is **run** to show the redesign now has external ground truth (`drill-generation.md` §2):

```
python <skill-dir>/runtime/python/runner.py snippet.py
```

Coverage spans three distinct routine shapes (learning-a-library · problem-grinding ·
AI-assisted) with three distinct **good-element decoys** (good targeting · good generation ·
good source-selection). Pose one, **hard-stop, wait** (`coaching-loop.md`). **How to grade**
against module §7: **D1** = caught the material anti-patterns (not the good element); **D2** =
prioritized the biggest fix and redesigned across the levers (not "more hours"); **D3** = can say
*why* (felt-ease anti-signal / hours ≠ learning). **A critique that "fixes" the good element, or
buries the big miss under a small one, is a partial pass — flag the inversion.**

---

## W1 — Learning a new library by marathon-reading the docs

> *"When I pick up a new library I **read the whole docs front to back, highlighting** as I go,
> in **one marathon sitting**. I don't build anything until I've read all of it — I want the full
> picture first. I only ever do this for **libraries that are actually relevant to my current
> project**, so I'm not wasting time."*

> **Your turn:** Critique this routine against the five levers. What's the **most important** fix,
> and how would you redesign it? Is there anything you'd **leave alone**?
>
> (Take your best guess — wrong attempts are useful data.)

**Diagnosis (lever by lever).**

| Lever | Verdict |
|---|---|
| **QUALITY** | ❌ Highlighting-while-reading is **passive** — no generation. Highlighting *feels* active but is re-reading with a marker. |
| **FEEDBACK** | ❌ "Don't build anything until I've read all of it" = **no external check** at all until the end. |
| **TARGETING** | ✅ **"Libraries relevant to my current project"** is *good targeting* — relevant, edge-adjacent. **Leave it alone.** |
| **DESIRABLE DIFFICULTY** | ❌ Reading-for-the-full-picture is maximally comfortable; no struggle, no retrieval. |
| **SPACING** | ❌ **One marathon sitting** — massed, not distributed. |

**Prioritize + redesign.** The highest-leverage fix is **QUALITY + FEEDBACK together**: stop
reading the docs cover-to-cover and instead **learn by building tiny things and checking them**.

> - **Generate + get feedback:** for each function you need, **read just its signature, predict
>   what it returns on a concrete input, then run it** to check. Build a 5-line spike, not a
>   highlight.
> - **Space it:** learn the library **as you hit each need over days**, not in one marathon;
>   revisit the parts you used.
> - **Keep:** the targeting (relevant libraries) — that part is already right.

**Runner-verified evidence** (what "read the signature, predict, run" checks against):

```python
print(sorted([3, 1, 2], reverse=True))   # predict before running...
print("a,b,,c".split(","))                # what does an empty field do?
print("  hi  ".strip())
```

```
stdout: "[3, 2, 1]\n['a', 'b', '', 'c']\nhi\n"
status: ok
```

So the redesigned practice has the learner **predict `[3, 2, 1]`, then the surprising
`['a', 'b', '', 'c']`** (the empty field becomes `''`, not dropped), then `hi` — each checked
against real output. That is the feedback the marathon-read never provided.

**Why.** Reading documentation feels like the responsible thing, but front-to-back highlighting
is the re-reading anti-pattern wearing a productive costume. You learn an API by *using* it
against ground truth, not by absorbing it.

**Diagnoses.** A learner who "fixes" the **targeting** ("don't restrict to your project, read
broadly") has **inverted** a good element into a bad one (§5c, over-correction) — mark D1 down.
A learner who catches the marathon (spacing) but misses that highlighting is passive has found
the smaller fish (D2 partial). Strong critique: leads with generate-and-check, spaces it, and
**explicitly keeps the targeting**.

---

## W2 — Blank-page grind where "it ran" counts as done

> *"I do **20 unseen, hard problems a day from a blank page** — no looking at solutions. If my
> code **runs without crashing, I count it solved** and move to the next. I never go back to old
> problems; there's always a fresh batch."*

> **Your turn:** Critique this routine against the five levers. What's the **most important** fix,
> and how would you redesign it? Is there anything you'd **leave alone**?
>
> (Take your best guess — wrong attempts are useful data.)

**Diagnosis (lever by lever).**

| Lever | Verdict |
|---|---|
| **QUALITY** | ✅ **Blank-page, unseen problems** is *excellent generation*. **Leave it alone.** |
| **DESIRABLE DIFFICULTY** | ✅ **Hard, unseen** is genuine desirable difficulty. **Leave it alone.** |
| **FEEDBACK** | ❌ **"Runs without crashing = solved"** is the broken lever — *running* is not *correctness*. No edge cases, no expected-output check. |
| **TARGETING** | ⚠️ "Always a fresh batch" risks never targeting a *specific* recurring weakness, but the bigger miss is feedback. |
| **SPACING** | ❌ **"Never go back"** — no spaced revisit, no consolidation. |

**Prioritize + redesign.** The single highest-leverage fix is **FEEDBACK**: this learner has the
*hard* part right (generation + difficulty) and is wasting it by never checking correctness.

> - **Close the feedback loop:** for each problem, write a **small test battery including edge
>   cases** (empty, single, duplicate, boundary) and assert the **expected output** — "it ran" is
>   not "it's right."
> - **Space it:** **revisit** a sample of old problems on a schedule; a fresh batch every day with
>   no return means nothing consolidates.
> - **Keep:** the blank-page, unseen, hard generation — that's the engine; don't dilute it.

**Runner-verified evidence** (why "it ran" ≠ "it's correct"):

```python
def second_largest(xs):
    return sorted(xs)[-2]

print(second_largest([5, 1, 4, 2]))   # the input the learner happened to try
print(second_largest([5, 5]))          # duplicates — is 5 really the "second largest"?
print(second_largest([3]))             # a single element
```

```
second_largest([5, 1, 4, 2]) -> 4         # ran, looks solved
second_largest([5, 5])        -> 5         # ran, but silently never decided the duplicate spec
second_largest([3])           -> IndexError: list index out of range   # only "ran" on the inputs tried
status: error   (on the [3] line)
```

So "it runs" was only ever true for the **one input the learner tried**: `second_largest([3])`
**crashes**, and `[5, 5]` returns `5` without anyone deciding whether duplicates should count.
The edge-case battery — the feedback lever — is exactly what "if it runs, it's done" skips.

**Why.** This is the most *deceptive* Working routine because it gets the celebrated parts right
(blank-page, hard, unseen) — so a careless critic praises it wholesale. The whole value leaks out
of the one open lever: difficulty and generation **without feedback** is unguided struggle.

**Diagnoses.** A learner who praises the routine as "great, just do more" missed the open
feedback loop entirely (D1 fail). A learner who "fixes" the **generation** ("blank-page is too
hard, look at solutions first") inverted a good element (§5c over-correction). A learner who flags
"never go back" (spacing) but not "runs ≠ correct" found the smaller miss (D2 partial). Strong
critique: leads with the feedback loop (edge-case battery + expected output), adds spaced revisit,
**keeps** the blank-page difficulty.

---

## W3 — Learning by having the AI explain code (AI-era)

> *"My practice is efficient: the AI **writes a function and explains it to me**, I **read the
> explanation and nod along**, and I move to the next one. I get through **a lot** this way — 30
> functions a session. I always feed it **real code from my own codebase**, so it's relevant."*

> **Your turn:** Critique this routine against the five levers. What's the **most important** fix,
> and how would you redesign it? Is there anything you'd **leave alone**?
>
> (Take your best guess — wrong attempts are useful data.)

**Diagnosis (lever by lever).**

| Lever | Verdict |
|---|---|
| **QUALITY** | ❌ "Read the explanation and nod along" is **pure passive consumption** — the AI generates, the learner receives. Zero retrieval. |
| **FEEDBACK** | ❌ The AI's *explanation* feels like feedback but isn't — it's **more text to read smoothly**, never checked against what the code *does*. |
| **TARGETING** | ✅ **Real code from your own codebase** is good, relevant targeting. **Leave it alone.** |
| **DESIRABLE DIFFICULTY** | ❌ Nodding along is frictionless; "30 a session" is **volume mistaken for learning**. |
| **SPACING** | ❌ A conveyor belt of 30, none revisited. |

**Prioritize + redesign.** The highest-leverage fix is **flip consumption into generation +
verification**: the AI explaining *to* you is the re-reading anti-pattern in AI clothing.

> - **Generate first:** before reading the AI's explanation, **predict what the function returns**
>   on a tricky input and **explain it yourself**; *then* compare to the AI's account.
> - **Verify, don't trust:** **run** the function on edge cases — does its behavior match the
>   AI's confident explanation?
> - **Keep:** feeding it your own real code (good targeting). Drop the "30 a session" volume
>   metric — that's hour-dosing by another name.

**Runner-verified evidence** (the AI's fluent explanation vs. what the code does):

```python
# The AI "explains": "This checks if n is prime by testing every divisor from 2 to n-1;
#                      if none divide n, it's prime."  (sounds right...)
def is_prime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

print(is_prime(7))    # predict, then run...
print(is_prime(2))
print(is_prime(1))    # is 1 prime?
print(is_prime(0))    # is 0 prime?
```

```
stdout: "True\nTrue\nTrue\nTrue\n"
status: ok
```

The AI's explanation **reads as correct and is correct for `n ≥ 2`** — but `is_prime(1)` and
`is_prime(0)` both return **`True`**, and neither 1 nor 0 is prime (`range(2, 1)` and `range(2,
0)` are empty, so the loop never runs). The smooth explanation bought confidence the *behavior*
didn't earn — the exact gap a "predict then run the edge case" redesign closes.

**Why.** AI-assisted study is the highest-stakes Working routine because it's *so* fluent: the
code looks idiomatic and the explanation reads authoritatively, so it maximally triggers the
fluency illusion — and unaided comprehension measurably atrophies under it (`evidence-base.md` →
AI-era impact, ~17% lower unaided comprehension). The fix is to make the learner *generate and
verify* before the AI's fluency does the thinking for them.

**Diagnoses.** A learner who calls this "great use of AI, very efficient" was sold by the fluency
(D1 fail — the keystone AI-era miss, §5c). A learner who "fixes" the **targeting** ("don't use
your own code, use harder examples") inverted a good element. A learner who says "read the
explanations more carefully" proposed a **non-fix** — more careful re-reading is still re-reading
(reject it). Strong critique: predict-and-explain *before* the AI, **run the edge cases to verify**,
keep the real-code targeting, drop the volume metric.
</content>
