# C1 — Systematic / Hypothesis-Driven Debugging `[Verified]`

> **Module type.** Mixed-status by design: a **`[Verified]` model** wrapped in a
> **`[Practitioner-canon]` method**. The *model* — that program comprehension (and
> therefore debugging) is **active and hypothesis-driven**, a cycle of predicting and
> checking rather than reading until it "clicks" — rests on Finding 4 of
> `evidence-base.md` (Brooks 1983; Pennington 1987; von Mayrhauser & Vans 1995),
> `[Verified]`. The *method* — the disciplined loop **observe → hypothesize → predict →
> test → narrow**, plus bisection and input minimization — is **`[Practitioner-canon]`**
> (Zeller, *Why Programs Fail*; Zeller & Hildebrandt 2002, delta debugging; Agans, the
> nine rules). The file badge is `[Verified]` (the closest single validator token for the
> model the module is built on); the honest prose badge is **`[Verified]` model +
> `[Practitioner-canon]` method**. **Hard honesty constraint:** the curriculum does *not*
> claim systematic debugging is *causally* superior to skilled ad-hoc debugging — that
> exact claim is on the **REFUTED** list (`evidence-base.md` → Refuted: "systematic
> control/data-flow tracing causally yields better mental models and fewer errors than
> as-needed reading — refuted"). The method is taught as a **discipline that makes
> debugging tractable and falsifiable**, not as a proven optimum.
>
> **Core idea.** Debugging is **science, not staring.** A bug is a hypothesis-testing
> problem: you **observe** the actual failure (run it — don't imagine it), form a
> **specific, falsifiable hypothesis** about the cause, **predict** what you'd see if the
> hypothesis were true (and what a fix would change), **test** by running, and **narrow**
> the search — by bisecting the change history or minimizing the failing input — until one
> hypothesis survives. The runner is the oracle; your theory is on trial against it.

---

## 1. Evidence basis `[Verified]` model + `[Practitioner-canon]` method

This module is **mixed-status**, and the coach must keep the two halves apart — never
presenting the canon method as verified science (`evidence-base.md` → badge rules; and the
specific REFUTED entry below).

**(a) The model half — Finding 4, `[Verified]`.** Cite via `evidence-base.md` → Finding 4
("comprehension is active and hypothesis-driven"). Reading code — and debugging it — is
**not passive intake**. Experts run a cycle of forming hypotheses about what code does and
**checking them against the text and the running program**, combining **top-down**
(expectation-driven — Brooks) and **bottom-up** (text-driven — Pennington) strategies, and
**switching modes** opportunistically as the task demands (von Mayrhauser & Vans). The three
anchor sources, confirmed in the evidence base's fact-checking pass:

- **Brooks, R. (1983). Towards a theory of the comprehension of computer programs.**
  *International Journal of Man-Machine Studies*, 18(6), 543–554. A **top-down,
  hypothesis-driven** model of comprehension: the reader forms an expectation of what the
  program does and seeks **beacons** (recognizable cue fragments) to confirm or refute it.
  Debugging is this same loop turned on a *failure*: a working theory of the program, a
  hypothesis about where it diverges, and a search for the evidence that decides.
- **Pennington, N. (1987).** Stereotyped knowledge structures and comprehension strategies
  in programming. *Cognitive Psychology*, 19, 295–341. The **bottom-up** complement: a
  text-driven *program model* built from control-flow and procedural units. Debugging needs
  this too — when top-down expectation fails, you fall back to tracing the actual control
  flow line by line.
- **von Mayrhauser, A., & Vans, A. M. (1995). Program comprehension during software
  maintenance and evolution.** *IEEE Computer*, 28(8), 44–55. The **integrated metamodel**:
  programmers **switch** between top-down and bottom-up as the task demands. Debugging is the
  canonical mode-switching task — hypothesize from the symptom (top-down), then trace to
  confirm (bottom-up), then re-hypothesize.

The narrow verified claim these license is exactly what this module's *model* teaches:
**comprehension and debugging proceed as prediction → check, not as reading until it
clicks.** Teaching debugging as an explicit predict-then-test loop aligns the learner's
process with how skilled comprehension actually works.

**(b) The method half — the disciplined loop, `[Practitioner-canon]`.** Vetted during
authoring against the named primary sources; respected, widely taught craft — **not**
empirical effectiveness findings (see `evidence-base.md` → proposed addition: *Systematic
debugging method (module C1)*):

- **Zeller, A. (2009).** *Why Programs Fail: A Guide to Systematic Debugging* (2nd ed.).
  Morgan Kaufmann (`evidence-base.md` → reading spine). The **scientific method of
  debugging**: from a working theory of the program, **generate a hypothesis**, **design an
  experiment that could falsify it**, run the experiment, fold the result back into the
  theory, and **repeat until the theory explains the failure** — recorded in an explicit
  **debugging logbook**. This is the loop the module drills.
- **Zeller, A., & Hildebrandt, R. (2002). Simplifying and Isolating Failure-Inducing
  Input.** *IEEE Transactions on Software Engineering*, 28(2), 183–200. doi:10.1109/32.988498.
  **Delta debugging / `ddmin`** — the algorithm behind **input minimization** and
  **bisection of a change set**: systematically shrink a failing input (or a set of changes)
  to the **minimal** part that still triggers the failure. The module's bisection and
  input-minimization drills are this idea, done by hand.
- **Agans, D. J. (2002).** *Debugging: The 9 Indispensable Rules…* AMACOM. The nine rules —
  **Understand the System · Make It Fail · Quit Thinking and Look · Divide and Conquer ·
  Change One Thing at a Time · Keep an Audit Trail · Check the Plug · Get a Fresh View · If
  You Didn't Fix It, It Ain't Fixed.** Agans is **observation-first** — his "Quit Thinking
  and Look" chapter takes its epigraph from Sherlock Holmes's "it is a capital mistake to
  theorize before one has data" (Conan Doyle, *A Scandal in Bohemia*) — which is *why* "observe" precedes "hypothesize"
  in this module's loop: the hypothesis must be grounded in what the failure actually shows,
  not in what the code was *meant* to do.

**Why these license this module.** Finding 4 grounds the *stance* (`[Verified]`: debug as
prediction-and-check); Zeller and Agans ground the *procedure* (`[Practitioner-canon]`: the
explicit loop, bisection, minimization, "change one thing," "if you didn't fix it it isn't
fixed"). The combined claim taught here: **a tractable debugging process observes the real
failure, forms a falsifiable hypothesis, predicts and tests it against the runner, and
narrows the search by bisection/minimization — and that discipline keeps you honest even
when intuition fails.**

**Read through the REFUTED constraint (the central honesty rule of this module).** The
seductive overclaim — *"systematic, methodical tracing/debugging **causally** produces
better mental models and fewer errors than skilled as-needed reading"* — **did not survive
fact-checking and is on the REFUTED list** (`evidence-base.md` → Refuted under verification).
So this module **must not** be sold as "the proven-best way to debug." A fluent expert who
pattern-matches a bug in five seconds is not doing it "wrong." What the method *does* buy is
**tractability and falsifiability**: when intuition stalls — the hard, unfamiliar, or
surprising bug — a disciplined observe→hypothesize→predict→test loop turns flailing into a
finite search, and prevents the most expensive failure mode (declaring a bug fixed when it
isn't). That is the honest pitch: **a reliable method for when staring stops working**, not
a causal upgrade over expertise.

**Read through the transfer caveat too.** Finding 4's primary evidence is from
**comprehension studies of programmers, largely 1983–1995**; the canon sources are **craft
wisdom, not measured causation**. The *direction* is well grounded; that drilling synthetic
buggy snippets *causally* improves a given engineer's real-world debugging is the open
question every module here carries (`evidence-base.md` → transfer caveat). The transfer task
(§9) — debugging a **real failing test from the learner's own repo** — is the honest
individual-level test. **AI-era note:** as agents produce most first-draft code, the work
shifts from *writing* to *verifying* code one didn't write; localizing why agent-written code
fails is exactly this skill, which is why C1 sits in the verification cluster
(`evidence-base.md` → AI-era impact; spec §12) — `[Verified-adjacent]` as a *priority*, not
proof.

---

## 2. Soft prerequisites

**A1 (notional machine) and A3 (execution tracing) strongly inform this module.** Debugging
*is* the notional machine applied under adversarial conditions: most of the bugs drilled here
are A1 execution-model events seen as *failures* — aliasing (`[[0]*n]*n` shares rows),
rebinding-vs-mutation, mutating a list while iterating, a generator exhausted on its second
pass, a mutable/`or` default that swallows a legitimate value. To form a sharp hypothesis you
must be able to **trace** the actual control flow and state (A3) and reason about what the
machine *does* rather than what the author *meant* (A1). **C2 (reading stack traces)** is the
near-sibling: when the failure is an exception, the traceback is the first observation, and
C2 is the skill of reading it as a window into the execution model. **A2 (code reading &
chunking)** helps you build the whole-function model fast enough to know where to look.

Per `assessment.md`, soft prerequisites **inform, never gate** — the buffet rule holds (any
learner may open any module at any tier). If a learner flails at C1 because they cannot trace
the buggy function's state, the coach notes the gap likely traces to A1/A3 and *suggests*
shoring those up — but does not forbid C1. Conversely, C1 surfaces A1/A3 gaps *in situ*: a
learner who cannot say why setting one board cell changed a whole column has an aliasing gap
that a debugging drill just made visible.

---

## 3. The mental model

**Debugging is the scientific method run against a program. The bug is the discrepancy
between what you expected and what the machine actually did; finding it is a hypothesis
search, not a stare.** You make the failure happen on purpose, look at what it actually does
(not what the code was meant to do), form one specific falsifiable hypothesis about the
cause, predict what you'd observe if it were true and what a fix would change, test that
prediction by running, and — when several hypotheses survive — **narrow** the search space by
bisection or input minimization until exactly one remains. The runner is the oracle; your
theory is the defendant.

The loop, as five states and the rule that moves between them:

| Stage | What you do | What goes wrong without it |
|---|---|---|
| **1. Observe (make it fail; look)** | Reproduce the failure **reliably** and look at the *actual* behavior — the real output, the real traceback, the real state — not the intended behavior. Add a *targeted* observation (a print of one value, an `is`/`id` check, an instrumented loop) only where a hypothesis needs it. | You debug a failure you can't reproduce, or you "fix" code based on what you *think* it does. Agans: *"Quit thinking and look"* — and *"make it fail"* before anything else. A bug you can't reproduce is a bug you can't confirm fixed. |
| **2. Hypothesize (specific & falsifiable)** | State **one** concrete cause that **could be wrong**: "the slice on line 4 is off-by-one, so the last element is dropped." Not "something's off with the loop." A hypothesis you can't falsify isn't a hypothesis. | Vague or unfalsifiable guesses ("the logic is buggy somewhere") can't be tested, so the search never converges. Brooks/Pennington: comprehension *is* hypothesis-forming — a sharp hypothesis is the unit of progress. |
| **3. Predict (the discriminating consequence)** | Say what you'd **observe if the hypothesis holds** — and, ideally, what you'd observe if it *doesn't* (so the test **discriminates**). Predict the *fix effect*: "if I change `<` to `<=`, the count goes 2 → 4." | An untested hypothesis is folklore. Without a predicted observation, you can't tell a confirmed cause from a coincidence — the root of "I changed three things and now it works (I think)." |
| **4. Test (run; change one thing)** | Run the discriminating experiment via the runner; or apply the candidate fix and **re-run**. **Change exactly one thing** so the result is attributable. | Changing several things at once means a green result tells you nothing about *which* change mattered. Agans: *"Change one thing at a time."* And: a fix not confirmed by a re-run is a *guess wearing a fix's clothes*. |
| **5. Narrow (bisect / minimize)** | When many lines/commits/inputs could be the cause, **halve the search**: bisect the change history to the first bad commit; minimize the failing input to the smallest part that still fails (delta debugging). Each step rules out half. | A linear scan of a 40-line diff or a 900-line input is slow and error-prone. Zeller & Hildebrandt: systematic halving turns a huge search into `O(log n)` decisions. Agans: *"Divide and conquer."* |

**The discipline in one line: *observe the real failure, hypothesize a falsifiable cause,
predict and test it against the runner, and narrow until one survives.*** Three corollaries
the module drills:

1. **Reproduce before you reason; look before you theorize.** The first move is *make it
   fail reliably*, then *observe the actual behavior*. A hypothesis built on what the code
   was *meant* to do — instead of what it *did* — is debugging the wrong program. (This is
   the A1 "simulate, don't read intent" rule, now under pressure.)
2. **A hypothesis must predict a discriminating observation — and a fix must be re-tested.**
   The unit of progress is *(hypothesis → predicted observation → run)*. The most expensive
   error in debugging is **"if you didn't fix it, it isn't fixed"** (Agans): applying a
   plausible change and declaring victory without re-running. Reordering two lines can move
   the bug to a different field, not remove it — only the re-run tells you.
3. **When the search is large, halve it — don't scan it.** Bisection (over commits) and
   input minimization (over data) are the same idea: a binary search that each step
   eliminates half the candidates. They convert "somewhere in here" into a logarithmic
   number of yes/no experiments — and minimization often reveals that there were *two* bugs,
   not one.

---

## 4. Worked example — the full debugging loop on an off-by-one

*(Foundations depth: every stage shown, with runner-verified observations. This fades by
tier — see the table after.)*

The skill is to **run the loop**, not to spot the bug by eye. A teammate reports: "`count_in_range`
is returning the wrong number — it says 2 but I expected 4."

```python
def count_in_range(xs, lo, hi):
    n = 0
    for x in xs:
        if lo < x < hi:
            n += 1
    return n
```

**Spec.** `count_in_range(xs, lo, hi)` returns how many elements of `xs` fall within
`[lo, hi]` **inclusive**.

**Stage 1 — Observe (make it fail; look).** Reproduce it. Run the exact failing call — never
trust the verbal report:

```
# /tmp/C1_worked_buggy.py
print(count_in_range([1, 5, 10, 15, 20], 5, 20))
```
```
stdout: "2\n"
status: ok
```

Confirmed: it returns **2**, not 4. The failure is real and reproducible. Now *look* — which
elements got counted? Don't guess; add **one targeted observation** (Agans' "build
instrumentation in"):

```
# /tmp/C1_worked_probe.py  — instrument the predicate, change nothing else
for x in xs:
    passed = lo < x < hi
    print(f"x={x:>2}  lo<x<hi -> {passed}")
    ...
```
```
stdout:
x= 1  lo<x<hi -> False
x= 5  lo<x<hi -> False
x=10  lo<x<hi -> True
x=15  lo<x<hi -> True
x=20  lo<x<hi -> False
count = 2
```

**Stage 2 — Hypothesize (specific & falsifiable).** The observation is sharp: `5` and `20`
— the **endpoints** — evaluate `False`. The spec says `[lo, hi]` is **inclusive**, so they
should count. Hypothesis: **the predicate uses strict `<` on both sides (`lo < x < hi`), so
it excludes the boundary values `lo` and `hi`; it should be `<=`.** This is falsifiable — if
true, exactly the two boundary elements are the ones being dropped.

**Stage 3 — Predict (the discriminating consequence).** If the hypothesis holds: the dropped
elements are precisely `x == lo` (5) and `x == hi` (20), and *no interior* element is
dropped. The probe already confirms that — `10` and `15` passed. Predicted **fix effect**:
changing both comparisons to `<=` makes `5` and `20` pass too, so the count goes **2 → 4**.

**Stage 4 — Test (change one thing; re-run).** Apply exactly one change (`<` → `<=`, both
sides) and re-run the original failing call:

```
# /tmp/C1_worked_fix.py
        if lo <= x <= hi:
...
print(count_in_range([1, 5, 10, 15, 20], 5, 20))
```
```
stdout: "4\n"
status: ok
```

**Verified ground truth** (executable-ground-truth discipline, `drill-generation.md` §2 —
the coach *runs* it, never guesses):

```
buggy  count_in_range([1,5,10,15,20], 5, 20)  -> 2     (status ok)
probe  shows x==5 and x==20 evaluate lo<x<hi -> False
fixed  count_in_range([1,5,10,15,20], 5, 20)  -> 4     (status ok)
```

Prediction matched observation: **the hypothesis is confirmed and the fix is verified by a
re-run**, not by hope.

**Stage 5 — Narrow.** Not needed here — one observation localized the cause to a single
predicate. (Stage 5 earns its keep when the candidate set is large: a 40-line diff, a
six-commit regression, a 900-line input. The Working bisection drill and the Advanced
minimization drill exercise it.)

**What the loop makes visible** (and eyeballing hides): the report ("wrong number") is not the
*cause*; the **targeted observation** (`5` and `20` fail the predicate) is what turns a
symptom into a falsifiable hypothesis, and the **re-run** is what turns a plausible fix into a
verified one. A learner who jumps straight to "change `<` to `<=`" might be right — but
without the observe-and-predict steps they cannot tell a *confirmed* cause from a lucky guess,
and on a harder bug the guess will be wrong.

> **Expertise reversal — the example fades by tier.** Per the worked-examples finding
> (`evidence-base.md` → instructional pillar; `coaching-loop.md` Step 2), a fully worked
> loop *helps novices* (it shows the observe→hypothesize→predict→test move while load is
> high) but becomes **redundant load for the more advanced**, who learn more by running the
> loop themselves. So the coach fades it:
>
> | Tier | Worked-example depth at C1 |
> |---|---|
> | **Foundations** | **Full** — every stage shown above, with the instrumented observation and the verified fix. |
> | **Working** | **Partial** — coach reproduces the failure (Stage 1) and hands over the observation, then leaves the **hypothesis, prediction, and fix-test** to the learner. |
> | **Advanced** | **Skeleton** — coach gives only the failing call and the spec; the learner runs the whole loop (observe → hypothesize → predict → test → narrow) unaided and explains *why*. |
> | **Frontier** | **None** — straight to the failing system (§6). |

---

## 5. Drill-generation spec

Instantiates the generation-spec format of `drill-generation.md` §1 for C1. Grading mode is
declared up front: **executable + hybrid** (§5d) — the *fix* has executable ground truth (run
it, re-run it); the *hypothesis/diagnosis reasoning* is rubric-graded. Bisection drills add a
*choose-the-split* judgment with a runner-verified first-bad-commit.

### 5a. Tier definitions (C1-specific)

The curriculum-wide tier names (`drill-generation.md` §1a) translated to this module. **Every
drill is a buggy snippet (or a regression history / a failing input)**; the learner
**observes** the failure (runs it), forms a **hypothesis**, **predicts** the fix effect, and
**tests** by running:

| Tier | C1 criterion | Example shape |
|---|---|---|
| **Foundations** | One **clear** bug on a familiar surface (off-by-one range, accumulator reset, wrong logical operator). The failure is obvious once run; the skill is the *loop itself* — observe → hypothesize → predict → test — not hunting. Single mechanism. | A `range(1, n)` that drops the last term; predict the wrong total, then the fixed total. |
| **Working** | A bug in a **context the learner hasn't seen**, where intent and execution diverge and the **right hypothesis must be chosen among plausible ones**: aliasing (`[[0]*n]*n`), an `or`/mutable default that swallows a falsy value, a truthiness filter. **Or a bisection drill**: a short regression history where the learner picks **where to bisect**. Predict the fix effect *and* name the mechanism. | The shared-row board; the `fee or 2` that turns a waived `0` into `2`; a 6-commit regression to bisect. |
| **Advanced** | A **subtle** bug whose first hypothesis is often *wrong*, requiring a **discriminating test** to falsify it, and where the **obvious fix may not actually fix it** (re-run required): mutate-list-while-iterating, generator exhausted on second pass, a failing input that must be **minimized** (delta debugging) and turns out to hide *two* faults. Combine two mechanisms or reason about why a candidate fix fails. Explain *why*. | `xs.remove(x)` inside `for x in xs` (skips elements); `sum(gen)` twice; a config parser that crashes — minimize the input to the offending line(s). |
| **Frontier** | See §6 — one step past the learner's last comfortable success. | — |

A drill is mis-tiered if a Foundations bug needs a discriminating test to even *form* the
hypothesis (that is Advanced), or a Working drill's bug is a single obvious off-by-one (that
is Foundations), or an Advanced "subtle" bug is visible on a skim. Apply the self-check
(`drill-generation.md` §4) and re-level before posing.

### 5b. Parameter space (axes the coach varies to avoid mode-collapse)

Pick a *different point on each axis* across successive drills (`drill-generation.md` §1b, §4
check 3). The axes for C1:

- **Bug class** — off-by-one / boundary (`<` vs `<=`, `range` upper bound) · wrong logical
  operator (`and`/`or`) · accumulator init/reset · aliasing / shared mutable reference ·
  rebinding-vs-mutation · **mutation while iterating** · truthiness / `or`-default swallowing
  a falsy value · mutable default argument · **generator/iterator exhaustion** · type/precision
  (int division, `round` to int) · regex/parse over-narrowing.
- **Failure mode (the observation)** — **wrong return value** · **wrong printed output** ·
  **raises an exception** (read the traceback — ties to C2) · **silently wrong only on
  specific inputs** (passes the obvious cases, fails the interior/edge — the camouflage axis).
- **Where the bug lives** — in one line · spanning two statements (order matters) · spanning
  **calls** (state leaks between invocations) · in the **input** (the code is fine on most
  inputs; one element triggers it) · in the **change history** (a regression — bisection).
- **Hypothesis difficulty** — the obvious hypothesis is **correct** (Foundations) · several
  hypotheses are plausible and a **discriminating test** is needed (Working) · the obvious
  hypothesis is **wrong / incomplete**, and the obvious **fix doesn't actually fix it**
  (Advanced).
- **Narrowing technique exercised** — none needed · **bisection** over commits · **input
  minimization** (delta debugging) over data · targeted instrumentation (one print / `id`
  check) to discriminate.
- **Format** (`drill-generation.md` §6) — primarily **Debug-this** (observe → hypothesize →
  predict → test) and **Trace-the-path** (pause at each state to localize); also **Error
  analysis** (here is a *wrong fix someone applied* — why didn't it work?), and **Teach-it-back**
  (articulate the loop / the bisection logic after a pass).

Keep an in-session log of the `(bug class, failure mode, hypothesis difficulty, narrowing
technique, format)` tuples used; do not repeat a tuple until the others are exercised.

### 5c. Common-error catalog

The *specific* debugging-process failures, each with the conceptual gap it diagnoses
(`drill-generation.md` §1c format). These are grounded in the comprehension literature
(Finding 4) and the debugging canon (Zeller; Agans), not in trivia. **The root of most of
them is one inversion: treating debugging as *reading the code for what it should do and
guessing a fix*, instead of *running the loop — observe the real failure, form a falsifiable
hypothesis, predict, test, and re-test the fix*.** (This is the C1 face of A1's *superbug* —
attributing a "hidden mind" to the machine — now under the pressure of a failure.)

```
Error: Proposes a fix without first reproducing/observing the failure — reasons about what
       the code "should" do and edits it, never running the failing case.
Diagnoses: Skipped Observe ("make it fail" / "quit thinking and look"). Debugging the
           intended program, not the actual one; no ground-truth observation to anchor a
           hypothesis. (Agans rules 1-3: understand, make it fail, look; A1 superbug.)
Example trigger: any Foundations bug — ask for the observation FIRST; a learner who jumps to
                 "change < to <=" without running it has skipped Stage 1.

Error: States a vague, unfalsifiable hypothesis — "the loop is buggy," "something's off with
       the logic," "the indexing is wrong somewhere."
Diagnoses: No specific, testable hypothesis. Comprehension is hypothesis-forming (Finding 4);
           a hypothesis you cannot falsify cannot be tested, so the search never converges.
           (Zeller: the unit of progress is a hypothesis + an experiment that could refute it.)
Example trigger: the aliasing board drill — "the list is weird" vs. "the three rows are the
                 same object, so writing one writes all."

Error: Forms a hypothesis but proposes no discriminating test / predicted observation — or
       reads ground truth that doesn't distinguish the competing causes.
Diagnoses: Hypothesis without a prediction. Cannot tell a confirmed cause from a coincidence;
           the experiment doesn't separate the live hypotheses. (Zeller: design an experiment
           that could FALSIFY the hypothesis; the test must discriminate.)
Example trigger: the fee-or-zero drill — predicting "it'll be wrong" (true under any cause)
                 vs. predicting "apply_fee(100, 0) returns 102 not 100, because `0 or 2`==2."

Error: Applies a plausible fix and declares victory WITHOUT re-running the failing case; or
       re-runs only the cases that already passed.
Diagnoses: Violates "If you didn't fix it, it ain't fixed" (Agans rule 9). A fix unconfirmed
           by re-running the ORIGINAL failure is a guess; partial fixes that move the bug
           rather than remove it look identical to real fixes until you re-run.
Example trigger: the generator-summarize drill — "reorder the two sums" then re-run: (0, 60),
                 the bug just moved to the other field.

Error: Changes several things at once, then can't say which change fixed it (or whether the
       "fix" or an unrelated edit mattered).
Diagnoses: Violates "Change one thing at a time" (Agans rule 5). A green result after a
           multi-change edit is unattributable — and often one change fixed it while another
           silently introduced a new bug.
Example trigger: any Advanced drill where the learner rewrites the function wholesale; ask
                 them to isolate the single change that flips the observation.

Error: Scans a long diff / change history / input linearly instead of bisecting; or bisects
       using a test input that doesn't actually distinguish good from bad.
Diagnoses: No divide-and-conquer; treats an O(n) search as unavoidable, or bisects on a
           non-discriminating probe (a case that passes in BOTH the good and bad versions).
           (Zeller & Hildebrandt: halve the search; Agans rule 4. The test you bisect on MUST
           separate good from bad.)
Example trigger: the 6-commit normalize_spaces regression — bisecting with the "hello world"
                 case (passes in every commit) instead of the tab/newline case that fails.

Error: Anchors on the first hypothesis and keeps trying to confirm it after a test has
       falsified it ("confirmation tunnel") — twists the observation to fit the theory.
Diagnoses: Theory-first instead of data-first; ignores a disconfirming observation. (Sherlock
           Holmes's "a capital mistake to theorize before one has data... one begins to twist
           facts to suit theories" — Conan Doyle, *A Scandal in Bohemia*; the epigraph to Agans'
           observe-first rule. von Mayrhauser & Vans: switch modes when the current one stalls.)
Example trigger: the remove-evens drill — insisting "remove() deletes the wrong VALUE" after
                 instrumentation shows it's the iterator INDEX skipping, not a wrong value.

Error: Stops at the first reproduction of the symptom and assumes a single cause — misses
       that minimizing the input reveals a SECOND, distinct fault with the same symptom.
Diagnoses: No minimization mindset; conflates "a failing input" with "the minimal failing
           input," so a second bug masked by the first goes unseen. (Zeller & Hildebrandt:
           ddmin isolates the minimal trigger and exposes independent triggers.)
Example trigger: the config-parser drill — the no-'=' line crashes first (masking) the
                 two-'=' line, which is a separate unpack bug; minimizing finds both.

Error: "Fixes" the symptom, not the cause — special-cases the one observed failing input
       instead of correcting the underlying mechanism, so neighbors of that input still fail.
Diagnoses: Treats the example as the bug. The hypothesis named a symptom, not a root cause;
           the fix doesn't generalize. (Zeller: the theory must explain the failure, i.e.
           the class, not patch the instance.)
Example trigger: the inclusive-range bug "fixed" by `if x == hi: n += 1` bolted on, instead
                 of `<` -> `<=` (now x == lo is still dropped — re-run to expose it).
```

### 5d. Grading mode

**Executable + hybrid** (`drill-generation.md` §1d, §3). C1 drills have an executable spine —
the **fix either works or it doesn't**, decided by the runner — wrapped around a rubric-graded
reasoning process.

The coach grades a C1 drill like this (the §3 hybrid path, made concrete):

1. **Run the buggy snippet to establish ground truth (the first executable sub-claim).** The
   coach **runs** the failing case via
   `python <skill-dir>/runtime/python/runner.py snippet.py` (`drill-generation.md` §2) and
   **pastes the exact snippet and output into the reply** (`coaching-loop.md` → Surface ground
   truth). This is the *Observe* stage made honest: the learner sees the real failure, never a
   guessed one. The coach never asserts what the snippet prints.
2. **Grade the hypothesis/diagnosis reasoning against the rubric (§7), criterion by
   criterion** — *is the hypothesis specific and falsifiable? does the predicted observation
   discriminate? does it name the mechanism (tied to §5c)?* This is the rubric (softer) half.
3. **Grade the fix executably (the second executable sub-claim).** The learner's proposed fix
   is **applied and re-run**; the coach pastes the result. The fix passes **only if the
   re-run of the original failing case now succeeds** — "if you didn't fix it, it isn't fixed"
   is enforced by the runner, not by assertion. A fix that "looks right" but fails the re-run
   is a **fail**, shown with evidence.
4. **For bisection drills:** the learner names the discriminating test and the commit to
   probe; the coach has the **runner-verified first-bad-commit** (each commit's behavior on
   the discriminating input was confirmed during authoring) and grades the bisection logic
   against it. The "which commit is first-bad" answer is executable ground truth; "did you
   bisect efficiently / on a discriminating test" is rubric-graded.
5. **Name it as the hybrid it is.** Report the two verdicts **separately**: a learner who
   produces a **working fix** (executable: pass) via a **vague or wrong hypothesis** (rubric:
   poor) is a **partial pass** — the coach flags exactly that, because a fix arrived at by
   luck or trial-and-error does not show the *method* the module teaches (and won't transfer
   to the bug that *can't* be brute-forced). Conversely, a **sharp, well-tested hypothesis**
   whose fix has a small arithmetic slip is *closer to mastery* than a lucky green — say so.

---

## 6. Frontier band

Frontier is not a fixed tier — it tracks the learner's **demonstrated ceiling** and presses
**one step** past their last comfortable success along a single parameter axis
(`drill-generation.md` §5). Escalating two steps collapses to failure; escalating none loses
the desirable-difficulty benefit.

**What "one step" means here** (per `drill-generation.md` §5):
- **Advanced** = one subtle bug whose first hypothesis is often wrong, debugged through the
  full loop (observe → hypothesize → predict → test → narrow) with a working, re-verified fix
  and a correct *why*.
- **Frontier-N** = N increments beyond Advanced; each increment adds exactly one new
  dimension of difficulty OR pushes one parameter-space dimension up one notch.
- The learner's current Frontier-N is the highest N they have passed.

Escalation directions beyond Advanced for C1, with step counts:

1. **Subtler / more camouflaged bug** (push the failure-mode + hypothesis-difficulty axes):
   from a bug that fails on obvious inputs → to one that passes every obvious input and fails
   only on an **interior/edge** case (Frontier-1) → to one where the **first two hypotheses
   are both wrong** and only the third survives a discriminating test (Frontier-2) → to a bug
   whose symptom **points at the wrong function entirely** (the fault is upstream of where it
   manifests) (Frontier-3). Each is one increment.

2. **Bigger / nastier search to narrow** (push the narrowing axis): from a 6-commit bisection
   → to a **longer history with a noisy/intermittent** signal where some commits are
   build-broken and must be skipped (Frontier-1) → to **input minimization on structured
   input** (minimize a failing JSON/HTML/source to the smallest fragment) (Frontier-2) → to a
   case where minimization reveals the failure depends on the **interaction of two** input
   elements, not one (Frontier-3). Each is one increment.

3. **Compose mechanisms** (the canonical path from `drill-generation.md` §5): aliasing +
   mutation-while-iterating in one snippet (Frontier-1); + a mutable default that carries the
   corrupted state across calls (Frontier-2); + a generator that exhausts before the second
   pass over it (Frontier-3). Each additional interacting mechanism is one increment.

4. **The fix introduces a regression** (push the "if you didn't fix it" axis): the obvious
   fix removes the original bug but **breaks a previously-passing case**; the learner must
   detect the regression by re-running the *whole* set, not just the original failure — and
   iterate. One increment for "fix causes regression," another for "the regression is itself
   subtle/input-dependent."

5. **Debugging fluent AI-generated code → the AI-era frontier.** A failing function that
   *reads* as confident and idiomatic (as agent output does) but fails on a plausible-surface
   input — the spec-§12 verification skill. Localizing why code one didn't write fails,
   without the author's mental model, is the hardest debugging: one increment for "AI-plausible
   surface," another for "and the traceback points away from the real cause." (Ties to C2 for
   the traceback and F1 for not over-trusting the fluent code.)

Track the level as `C1: Frontier-N`. Reset condition: two consecutive failures at the same
level → drop to Advanced for one drill, then re-approach (`drill-generation.md` §5).

---

## 7. Mastery rubric

The observable per-tier bars, instantiating the rubric shape of `assessment.md` Part 2, scored
on **method**, not just outcome. Two cross-cutting requirements apply at every tier above
Foundations: **product *and* process** (the fix works *and* the loop that found it was sound —
a working fix reached by a vague/lucky hypothesis is a Foundations-level pass at best;
`evidence-base.md` → illusions of fluency), and **unaided + durable** (a same-session streak
is provisional until a delayed re-assessment or the real-code transfer task confirms it;
`assessment.md` Parts 3–5). This mirrors the C1 entry task, which scores the *hypotheses and
how you'd test them*, **not** whether the bug was ultimately found (`assessment.md` §1.4 → C1).

**The scored dimensions** (each graded explicitly): **Observe** (reproduced the real failure,
looked at actual behavior) · **Hypothesize** (specific, falsifiable, names the mechanism) ·
**Predict & Test** (a discriminating prediction; the fix re-verified by running) · **Narrow**
(bisects/minimizes when the search is large, on a discriminating test).

| Tier | Observable bar for C1 |
|---|---|
| **Foundations** | On a single clear bug, **runs the failing case** (doesn't guess), states a **specific** hypothesis ("`range(1, n)` stops at `n-1`, so the last term is dropped"), **predicts the fixed value** (`sum_to(5)`: 10 → 15), and **confirms the fix by re-running**. Names the mechanism in execution terms. Allowed *with* the worked loop faded to one missing stage. |
| **Working** | On a bug in an unseen context **unaided**: reproduces it, chooses the **correct hypothesis among plausible ones** with a **discriminating** predicted observation (e.g. "rows are the *same object* — I'd test `board[0] is board[1]`; it's `True`"), predicts and **re-verifies** the fix, and **names the mechanism** (aliasing; `0 or 2` swallows the waived fee). On a **bisection** drill, picks a **discriminating test input** and bisects to the first-bad commit in `O(log n)` probes, not a linear scan. On 3 of 4 such unseen drills. |
| **Advanced** | On a **subtle** bug **unaided**: when the first hypothesis is wrong, **falsifies it with a discriminating test** and re-hypothesizes (doesn't tunnel); proposes a fix and **catches that an "obvious" fix doesn't actually fix it by re-running** (e.g. reordering the two `sum`s yields `(0, 60)`); **minimizes a failing input** to the offending element(s) and notices when minimization exposes a **second** fault. Proposes a **working, re-verified** fix and **articulates the underlying principle** on a teach-it-back (`drill-generation.md` §6) — "observe before you theorize; a fix isn't fixed until the original failure re-passes" — not just the instance. |
| **Frontier** | `Frontier-N`: presses one dimension past the last comfortable success per §6 / `drill-generation.md` §5 (more camouflaged bug → nastier search to narrow → composed mechanisms → fix-causes-regression → AI-generated code). A moving target, not a fixed bar. |

Promotion is by **performance, not tenure** (`assessment.md` rule 1); the coach marks a tier
from what the learner *does* on unseen buggy snippets, never from "I debug all day." Held-out
re-assessment and **real-failing-test transfer** outrank a same-session streak
(`assessment.md` Part 5).

---

## 8. Anti-patterns & evidence caveat

**Anti-patterns this module exists to break** (each is a catalog entry in §5c, surfaced as a
*behavior*):

- **Fixing before observing ("quit thinking and look" — inverted).** Editing the code based
  on what it *should* do, without ever reproducing and looking at the actual failure. The fix
  is mechanical: *make it fail reliably first, then look* — add one targeted observation
  before forming a hypothesis. (Agans rules 1–3; the A1 superbug under pressure.)
- **Vague, unfalsifiable hypotheses.** "The logic's off somewhere." A hypothesis you can't
  test can't converge a search. The fix: state **one specific cause that could be wrong**, and
  the observation that would decide it. (Finding 4: comprehension is hypothesis-forming; Zeller.)
- **"If you didn't fix it, it isn't fixed."** Applying a plausible change and declaring victory
  without **re-running the original failure**. The single most expensive debugging error — a
  partial fix that *moves* the bug is indistinguishable from a real one until you re-run. The
  fix: **always re-run the failing case** (and the neighbors) after a change. (Agans rule 9.)
- **Changing several things at once.** A green result after a multi-edit tells you nothing
  about which change mattered, and may hide a newly-introduced bug. The fix: **change one thing
  at a time** and attribute the result. (Agans rule 5.)
- **Scanning instead of bisecting; bisecting on a non-discriminating test.** Linearly reading
  a long diff/history/input, or bisecting with an input that passes in *both* good and bad
  versions. The fix: **halve the search** with a test that actually separates good from bad.
  (Zeller & Hildebrandt; Agans rule 4.)
- **Confirmation tunnel / theory-first.** Clinging to the first hypothesis after a test has
  falsified it; twisting the observation to fit. The fix: **data-first** — let a disconfirming
  observation kill the hypothesis and switch modes. (Agans; von Mayrhauser & Vans.)

**Evidence caveat (this is a `[Verified]` model + `[Practitioner-canon]` method module — say
so).** The two halves must not be conflated, and one specific overclaim is **forbidden**:

- The **model** half — debugging as **active, hypothesis-driven prediction-and-check** — is
  `[Verified]` (Finding 4: Brooks 1983; Pennington 1987; von Mayrhauser & Vans 1995). It
  robustly establishes the *direction* (skilled comprehension is hypothesize-then-confirm, not
  passive reading), from **comprehension studies of programmers, ~1983–1995**.
- The **method** half — the explicit observe→hypothesize→predict→test→narrow loop, bisection,
  input minimization, "change one thing," "if you didn't fix it it isn't fixed" — is
  **`[Practitioner-canon]`** (Zeller, *Why Programs Fail*; Zeller & Hildebrandt 2002; Agans).
  Respected, widely taught **craft wisdom**, vetted against the named sources during authoring
  — **not** an empirical effectiveness result. The coach must never present it as verified
  science.
- **The forbidden claim (REFUTED).** Do **not** assert that systematic/methodical debugging
  is **causally superior** to skilled ad-hoc debugging — that specific claim ("systematic
  control/data-flow tracing causally yields better mental models and fewer errors than
  as-needed reading") is on the **REFUTED list** (`evidence-base.md` → Refuted under
  verification). The honest pitch is **tractability and falsifiability**, not a proven
  performance edge: the method is the reliable fallback for when intuition stalls, and the
  guard against the expensive "I think it's fixed" failure — *not* the one true way to debug.
- The **AI-era priority** that places C1 in the verification cluster (debugging code one
  didn't write rises as agents draft it; spec §12) is `[Verified-adjacent]` — **priority-steering,
  not proof**; the supporting productivity data is partly contested and vendor-sourced
  (`evidence-base.md` → AI-era honesty caveats).
- The **curriculum-wide transfer caveat** applies in full: that drilling synthetic buggy
  snippets *causally* improves a given engineer's real-world debugging is the open question.
  The coach leans on the transfer task (§9) — debugging a **real failing test** — as the
  honest individual-level evidence.

No claim in this module is dressed above its badge — and the causal-superiority overclaim is
actively refused.

---

## 9. Transfer task

**The only honest test of whether the gym drill transferred to the job is applying the loop to
a real failing test in the learner's own code** (`assessment.md` Part 4; `evidence-base.md` →
transfer caveat, consequence 2).

> **Your turn:** Find a **real bug in your own codebase** — a failing test, a recent incident,
> or a function whose behavior once surprised you (the thing that made you say "wait, why did
> it do *that*?"). Pick the smallest one you can still reproduce.
>
> Now **run the loop, out loud.** **(1) Observe:** reproduce the failure reliably and look at
> the *actual* behavior — the real output, the real traceback — not what the code was meant to
> do. Add **one** targeted observation if you need it. **(2) Hypothesize:** state **one
> specific, falsifiable** cause. **(3) Predict:** say what you'd observe if it's true (and what
> a fix would change). **(4) Test:** run the discriminating experiment, or apply the fix and
> **re-run the original failing case** — change one thing at a time. **(5) Narrow** if the
> search is large: bisect the history to the first bad commit, or minimize the failing input to
> the smallest piece that still fails.
>
> Then step back: **was your first hypothesis right, or did a test falsify it?** And: **did you
> confirm the fix by re-running the original failure, or did you just assume it worked?** If you
> reached for a fix before reproducing the bug, that's the exact trap this module targets — run
> the loop.

**Grading is softer and named as such** (`assessment.md` Part 4). Real code has no clean answer
key; the coach grades against the §7 rubric (Observe / Hypothesize / Predict & Test / Narrow)
and says: *"this is a judgment call on your real debugging, not a machine-verifiable result."*
Where any sub-claim **is** runnable — the learner suspects a cause and the code can be exercised
— the coach still uses the runner: **reduce the failure to a minimal snippet, run it through
`runner.py` to confirm the observation, apply the fix, and re-run to confirm it resolves** (the
same discipline as the §5d hybrid check, now on the learner's real bug). **Transfer evidence is
weighted heavily:** a learner who aces synthetic drills but, on a real bug, edits before
reproducing — or declares a fix done without re-running the failure — has **not** transferred
the skill, and the tracker notes that gap as more diagnostic than another passed synthetic drill.

---

## Cross-references

- Drill mechanics, the **executable + hybrid** grading path, the runner protocol, the
  Debug-this / Trace-the-path / Error-analysis formats, Frontier escalation:
  `references/drill-generation.md` (this module instantiates §1 and follows §2, §3, §4, §5;
  the fix/bug checks use §2).
- Session delivery (pause/no-spoiler hard stop, tier-faded worked example, surface-ground-truth,
  direct feedback, scaffolding ladder): `references/coaching-loop.md`.
- C1 entry task (a **failing test + the buggy function** — give your **first three hypotheses,
  ranked, and how you'd test each**; process is the primary signal, *not* whether you found the
  bug), per-skill routing, mastery-rubric shape, held-out re-assessment, **real-failing-test
  transfer** weighting: `references/assessment.md` (the C1 entry task, with the `running_max`
  example whose output lags by one).
- Evidence grounding (Finding 4 — Brooks 1983 / Pennington 1987 / von Mayrhauser & Vans 1995;
  the REFUTED causal-superiority claim that bounds the badge; the debugging-method craft
  sources — Zeller *Why Programs Fail*, Zeller & Hildebrandt 2002 delta debugging, Agans nine
  rules; the worked-examples / expertise-reversal instructional finding; the AI-era verification
  priority): `references/evidence-base.md`.
- Soft prerequisites (the execution model under pressure; tracing to localize; reading
  tracebacks): modules **A1** (notional machine), **A3** (execution tracing), **C2** (reading
  stack traces), **A2** (code reading & chunking).
- Golden exemplars (~3 per tier, each with a **runner-verified** failure, a gold hypothesis,
  and a **runner-verified** fix — plus the bisection drill's runner-verified first-bad commit):
  `exemplars/C1/foundations.md`, `exemplars/C1/working.md`, `exemplars/C1/advanced.md`.
