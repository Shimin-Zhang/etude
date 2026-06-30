# F3 — Learning new languages & frameworks fast `[Verified-adjacent]`

> **Module type.** A judgment-heavy, **hybrid** module. The core skill — *map an
> unfamiliar construct onto the notional machine you already have; decide what is the
> same and what is genuinely different* — is **rubric-graded** (there is no executable
> ground truth for "is this a good mapping?"). But every drill carries one **executable
> sub-claim**: the learner predicts the new construct's behavior *under their analogy*,
> and the coach **runs it**, so a false-friend mapping is **convicted by the runner**,
> not argued. Mostly rubric; the run *verifies the mapping*. Honest prose badge:
> `[Verified-adjacent]` — transfer-of-learning is well-established **general** cognitive
> science, the **programming-specific causal** evidence is thin, and the mapping is fenced
> hard by the notation-dependence result (idioms are partly notation-specific, so an
> analogy can be a **false friend**).
>
> **Core idea.** You never learn a new language from zero. You already own a **notional
> machine** (A1) and a stock of **idioms** (A2) from the languages you know. The fast path
> is **transfer**: map the new language's constructs onto what you have — *this language's
> X is like that language's Y* — and sort what transfers for free from what is genuinely
> different. **Don't memorize syntax; port the execution model and the idioms.** And
> because the analogy can be a **false friend**, the discipline is to **run the construct
> and let the machine convict the mapping.**

---

## 1. Evidence basis `[Verified-adjacent]`

This module is grounded on three things, and they must be kept at three different
confidence levels. The coach must never present the general-science half as
programming-specific proof, and must never let the analogy stand in for a verified result.

**(a) What you port — the notional-machine foundation (Verified-tier; reused, not
re-derived).** F3 rests on **Finding 1** of `evidence-base.md` — *the notional machine is
the durable barrier, not syntax* — the curriculum's most strongly verified result (Sorva
2013; du Boulay 1986). The whole thesis of this module is a corollary of it: if the
durable thing is the **execution model**, then learning a *new* language is mostly
**re-using the execution model you already built** and patching the places it differs —
**not** re-memorizing syntax. A1 is the machine; F3 ports it. (Cite Finding 1 via
`evidence-base.md`; do not re-derive it here.)

**(b) Why mapping works at all — transfer of learning `[Verified-adjacent]` (general
cognitive science).** That skill acquired in one setting carries to a related setting *to
the extent the two share structure* is one of the oldest, best-established results in
cognitive psychology — but it is **general** science, established mostly **outside
programming**, so for our purposes it is `[Verified-adjacent]` — well-established in general,
**not** a verified *programming* result. Cite via `evidence-base.md` → *Learning new
languages & frameworks — transfer of learning (module F3)*:

- **Thorndike & Woodworth (1901)** — the **identical-elements** theory: in their words,
  "spread of practice occurs only where identical elements are concerned in the influencing
  and influenced function." This is the mechanism behind both halves of F3 at once:
  the parts a new language **shares** with one you know (sequencing, branching, function
  call/return, integer arithmetic) transfer for **free**; the parts it does **not** share
  do not transfer — and *look like they should*.
- **Salomon & Perkins (1989)** — **near vs. far** and **low-road vs. high-road** transfer.
  *Near* transfer (to a similar context — a new C-family language) is comparatively reliable
  and can fire **reflexively**; *far* transfer (to a paradigm-distant language) needs
  deliberate, **mindful** abstraction (the "high road"). The practical reading: the closer
  the new language, the more transfers automatically — **and the more dangerous the
  automatic transfer becomes**, because a reflexive analogy fires before you have checked it.
- **Singley & Anderson (1989), *The Transfer of Cognitive Skill*** — the **programming-
  adjacent** anchor, and the most we can honestly claim near programming. They revived
  Thorndike's identical-elements idea in a cognitive-skill framework (ACT*: transfer is
  roughly proportional to **shared productions** — shared procedural knowledge) and studied
  it on text-editing and related cognitive skills. **Honest bound:** this is **1989**, on
  **editors and small skills**, not modern frameworks — it makes the *direction* (transfer
  ∝ shared structure) credible for programming, **not** any quantitative promise about how
  fast you will pick up React.

**(c) Why the mapping is not safe — the false-friend fence (reused refutation +
honesty).** Two hard limits keep this module at `[Verified-adjacent]` and drive its whole
discipline:

- **Negative transfer / false friends are real, and idioms are notation-dependent.** The
  same surface can carry *different* behavior, and prior learning then **interferes** rather
  than helps. The rigorous programming-specific anchor is already in the evidence base: the
  **Gilmore & Green (1988)** notation-dependence result (`evidence-base.md` → Refuted; the
  A2 caveat). Pascal programmers were cued by plan structure where BASIC programmers were
  **not** — so programming **plans/idioms are partly notation-specific**, and an idiom that
  cued you in language A may simply **not hold** in language B. That is exactly a *false
  friend*. (Reuse this citation; do not re-add it.)
- **Far transfer is hard and often fails to happen on its own.** **Barnett & Ceci (2002)**
  survey a century of work and conclude that whether far transfer reliably occurs is, even
  now, **disputed** — it frequently **does not** happen spontaneously. This is not a reason
  to distrust the module; it is the *reason the module exists*: you cannot count on osmosis
  to map a new language for you. You must map **deliberately** and **verify**.

**Why these license this module.** (a) gives F3 the thing worth porting (the execution
model). (b) explains why porting it is faster than starting over (shared structure
transfers). (c) explains why porting is **not automatic and not safe** (far transfer is
unreliable; surface-matched constructs are false friends; idioms are notation-specific).
The combined, honestly-bounded claim F3 teaches: **acquire a new language fast by mapping
its constructs onto the notional machine you already have — then run each mapping to
convict the false friends, because the analogy is a hypothesis, not a result.**

**Read through the transfer caveat (twice over).** The general transfer science (b) is from
**non-programming** tasks; the programming-adjacent anchor (c-Singley & Anderson) is **1989,
on editors**; and the curriculum-wide caveat applies in full — that **explicitly** teaching
this mapping discipline *causally* makes a working engineer learn languages faster is an
**open question** (`evidence-base.md` → transfer caveat). The coach says this out loud and
leans on the transfer task (§9) — the skill on a language the learner is *actually* learning
— as the honest individual-level evidence. **AI-era note:** when you (or an agent) work in
an unfamiliar language or framework, the false-friend risk is highest and fluent-looking
output is most dangerous — verifying code in a stack you don't yet own is precisely the
"port-and-run-don't-trust-the-surface" skill (`evidence-base.md` → AI-era impact; ties to
F1 calibration and E3 review). `[Verified-adjacent]` as a **priority**, not proof.

---

## 2. Soft prerequisites

**A1 (notional machine) — the load-bearing prerequisite.** F3 is, almost exactly, "A1
applied to a language you don't know yet." The thing you port is the execution model; the
thing the runner verifies is a state-transition prediction. A learner who cannot simulate a
construct's state changes in a language they *do* know has nothing to port — the gap will
surface here as "I can read the new syntax but can't predict what it does."

**A2 (code reading & chunking) — recommended.** Idioms are A2's *plans/beacons* seen at the
language level; the *re-notation* outcome in §3 (same concept, different idiomatic surface)
is an A2 skill applied across languages. A2 is also where the **notation-dependence caveat**
lives — the reason an idiom can be a false friend.

Per `assessment.md`, soft prerequisites **inform, never gate** — the buffet rule holds (any
learner may open any module at any tier). If a learner flails at F3 because they cannot
predict a construct's behavior, the coach notes the gap likely traces to **A1** and
*suggests* shoring it up — but does not forbid F3. Conversely, F3 is itself a strong
**signal the other way**: a learner solid on A1/A2 in one language who nonetheless mis-maps
constructs into a new one is exactly who F3 is for.

---

## 3. The mental model

**You already have a notional machine. Learning a new language is porting it: re-use the
parts the new language shares, and *repair* the parts it doesn't — then verify the repair by
running.** Each construct you meet in the new language lands in exactly one of four
**mapping outcomes**, and your job is to sort it correctly:

| Outcome | What it is | Python-as-"new-language" example (vs. a known language) | Discipline |
|---|---|---|---|
| **True friend** (positive transfer) | Same surface, **same** behavior. The analogy holds; it transfers for free. | `if/else`, `+` on numbers, `7 % 2`, function call & `return`, `==` as value-equality. | Spot-check once, move on. |
| **False friend** (negative transfer) | Same/similar surface, **different** behavior. The analogy *misleads*. **This is where the bugs live.** | `7 / 2` is `3.5`, not `3`; `1 < 3 < 2` is `False` (chained, not left-associated); `def f(x, acc=[])` shares one list across calls; a mutable in a class body is a **class** attribute. | **Run it.** Predict under the analogy, then convict the analogy with the machine. |
| **Genuinely new** (no analogy) | No real counterpart in the languages you know. Forcing an analogy makes it *worse*. | generators / `yield` (lazy, one-shot, frame-suspending); context managers / `with`; decorators; the GIL. | Build the sub-model **from scratch** (A1) — *then* find the nearest partial analogy, if any. |
| **Same concept, new notation** (re-notated idiom) | The concept exists in both; the **idiomatic surface** differs. | "iterate with index" → `enumerate`; "swap" → `a, b = b, a`; "copy a list" → `a[:]` / `list(a)`; "null check" → `is None` / truthiness. | Learn the **target** idiom; do **not** transliterate the source one. |

**Two moves, in order.** First, **port the machine, not the syntax.** Do not collect syntax
trivia ("how do I write a for-loop here"); ask the A1 questions — *what are the values and
names, when does this run, what mutates, what is shared, what does this evaluate to* — and
map the answers onto the model you already have. Second, **treat every analogy as a
hypothesis and run it.** A mapping is a *prediction* about behavior; the runner (or, in a
language the runner can't execute, the language's own REPL / tests / spec) is the
**falsifier**. The false friend is the dangerous case precisely because the **surfaces
match** — the only thing that separates a true friend from a false one is *behavior under
test*, which you cannot get by reading.

**The discipline in one line: *port the machine, not the syntax — and run the analogy,
because the false friend hides exactly where the surfaces match.*** Three corollaries the
module drills:

1. **The analogy is a hypothesis, not a conclusion.** "Python's `/` is like C's `/`" is a
   *claim to test*, not a fact to use. Most fast-learning bugs are an **untested** analogy
   shipped as if confirmed. Predict under the analogy → run → keep it or repair it.
2. **A lot transfers for free — don't re-learn the true friends.** The opposite error to
   over-trusting analogies is **distrusting all of them** and re-deriving sequencing,
   branching, and arithmetic from scratch in every new language. Identical-elements says the
   shared core *does* transfer; spend your attention on the false friends and the genuinely
   new, not on the parts that already work.
3. **When there is no analogy, stop forcing one.** Generators, context managers, decorators,
   ownership, async — for genuinely-new constructs the fastest path is to **build the
   notional-machine sub-model directly** (be the machine; trace it), and only *then* reach
   for the nearest partial analogy, knowing where it stops.

---

## 4. Worked example — mapping `/`, `//`, `%` from C into Python

*(Foundations depth: every step shown, including the analogy, the prediction, the run, and
the classification of each construct. This fades by tier — see the note after.)*

The skill is to **be a disciplined porter**: name the source-language analogy out loud,
predict under it, **run**, then classify each construct as true friend / false friend /
re-notated / new — and *repair* the false friends. Suppose you know **C / Java / Go** and
you meet this Python:

```python
print(7 / 2)
print(7 // 2)
print(7 % 2)
```

**Step 1 — name the analogy (the source construct you are mapping from).** In C/Java/Go,
`/` on two integers is **integer division** that **truncates toward zero**, `%` is the
remainder, and there is no `//`. So your imported model says: *`7 / 2` is the integer
division I know.*

**Step 2 — predict the behavior *under the analogy*** (this is the hypothesis):

| Construct | Prediction under the C analogy | Reasoning you imported |
|---|---|---|
| `7 / 2` | `3` | `/` truncates int÷int |
| `7 // 2` | *(unknown — no `//` in C)* | no imported model — flag it |
| `7 % 2` | `1` | remainder, same as C |

**Step 3 — RUN it** (executable ground truth — the coach *runs* it, never guesses;
`drill-generation.md` §2):

```python
print(7 / 2)
print(7 // 2)
print(7 % 2)
```
```
stdout: "3.5\n3\n1\n"
status: ok
```

**Step 4 — locate the break and classify each construct** (the porting payoff):

| Construct | Predicted | Actual | Outcome | Repaired mapping |
|---|---|---|---|---|
| `7 / 2` | `3` | **`3.5`** | **False friend** | Python 3 `/` is **true division** (always `float`). The C `/` you wanted is `//`. |
| `7 // 2` | *(unknown)* | `3` | **True friend for C's `/`** | `//` is **floor division** — *this* is your imported integer-division operator. |
| `7 % 2` | `1` | `1` | **True friend** | `%` is the remainder, as imported (on positives). |

**Step 5 — verify the *repaired* mapping at the boundary, too.** You "fixed" the analogy to
`C's / ≈ Python's //`. But is that exact? Run the edge case before you trust it:

```python
print(-7 // 2)
print(int(-7 / 2))
```
```
stdout: "-4\n-3\n"
status: ok
```

So `-7 // 2` is **`-4`** (floor division rounds toward **−∞**) while C's `-7 / 2` is `-3`
(truncates toward **zero**, like `int(-7 / 2)` here). Even your *true-friend repair* has a
residual difference **on negatives** — which you would have shipped as a bug if you had
stopped at "`//` is C's `/`." The lesson lands twice: the surface `/` lied (false friend),
**and** the repair lied at the boundary (verify even the true friend where it matters).

**What the example makes visible** (and reading the syntax hides): you could **not** sort
true friend from false friend by looking — `7 / 2` and C's `7 / 2` are *character-identical*.
Only **running** it separated them. Porting is fast because three of the four constructs
mapped cleanly; it is *safe* only because you ran the one that didn't.

> **Expertise reversal — the example fades by tier.** Per the worked-examples finding
> (`evidence-base.md` → instructional pillar; `coaching-loop.md` Step 2), a fully worked
> mapping helps **novices** (it shows the predict→run→classify move) but is **redundant load
> for the more advanced**, who learn more by porting unaided. So the coach fades it:
>
> | Tier | Worked-example depth at F3 |
> |---|---|
> | **Foundations** | **Full** — the analogy, the prediction table, the run, and the four-way classification above, every step shown. |
> | **Working** | **Partial** — coach states the construct and the source-language analogy, runs it, and leaves the **classification + the repaired mapping** for the learner. |
> | **Advanced** | **Skeleton** — coach hands over only the construct ("here's a Python idiom; you know language X") and the rubric; learner names the analogy, predicts, asks for the run, classifies, and repairs unaided. |
> | **Frontier** | **None** — straight to the problem (§6). |

---

## 5. Drill-generation spec

Instantiates the generation-spec format of `drill-generation.md` §1 for F3. Grading mode is
declared up front: **hybrid — executable prediction + rubric mapping** (§5d). The *new*
thing in every drill is a **Python idiom the learner treats as "new"**, mapped from a
language they know; the run **verifies the mapping**, and the mapping reasoning is graded
against the rubric.

### 5a. Tier definitions (F3-specific)

The curriculum-wide tier names (`drill-generation.md` §1a) translated to this module. Every
drill: *here is a Python construct; you know language X; map it, predict it, and we'll run
it.*

| Tier | F3 criterion | Example shape |
|---|---|---|
| **Foundations** | **One construct**, a **clear** true/false-friend on a familiar surface, mapped from a close (C-family/JS) source. Predict the behavior under the analogy; name what's the same and what's different after the run. | `7 / 2` (false friend from C); `1 < 3 < 2` (chained comparison); `"3" + 4` (no implicit coercion, from JS). |
| **Working** | One construct in a context the learner hasn't seen, where the analogy is **more tempting** and **passes a shallow look** (intent and execution diverge). Predict, run, **and articulate the execution-model reason** the analogy broke. | mutable default arg shared across calls; `is` vs `==` and the small-int cache; shallow `a[:]` copy with a nested list. |
| **Advanced** | A **genuinely-new** construct (no clean analogy) **or** a false friend that **combines two mechanisms**; build/port the sub-model, predict, run, **explain why**, and name the analogy *and its limit*. | generator laziness/`yield`; `with` / `__exit__` exception suppression vs `try/finally`; a mutable **class attribute** shared across instances. |
| **Frontier** | See §6 — one step past the learner's last comfortable success (compose constructs; map from a paradigm-distant language; framework-level idioms; map *out* of Python into a target language; verify without the runner). | — |

A drill is mis-tiered if a Foundations drill hides its false friend behind two interacting
constructs, or an "Advanced" drill is a one-line true friend with no execution-model
explanation to give. Apply the self-check (`drill-generation.md` §4) and re-level before
posing.

### 5b. Parameter space (axes the coach varies to avoid mode-collapse)

Pick a *different point on each axis* across successive drills (`drill-generation.md` §1b, §4
check 3). The axes for F3:

- **Construct family** — numeric semantics (`/`, `//`, int cache) · equality/identity
  (`==` vs `is`) · binding/defaults (mutable default arg) · truthiness/`None` · slicing &
  copy depth · comprehension scope · chained comparison · operator/`++` absence · string
  immutability & concatenation · iteration & **laziness** (generators) · resource scoping
  (`with`/`__exit__`) · attribute resolution (class vs instance) · decorators.
- **Source-language analogy** (what the learner maps *from*) — C/C++ · Java · JavaScript ·
  Go · Ruby/Python-2 · SQL · math notation · a functional language. (Vary the *distance*:
  close source = near transfer = reflexive-but-dangerous; distant source = far transfer =
  needs the high road.)
- **Mapping outcome under test** — true friend (transfers) · **false friend** (negative
  transfer) · genuinely-new construct · re-notated idiom. (Don't make *every* drill a false
  friend; a true-friend or re-notation drill teaches the same/different discrimination and
  guards against corollary 2.)
- **Predicted artifact** — `stdout` value · **whether it raises** (`status`/exception type) ·
  an **identity** `True`/`False` (`is`) · the **order/count** of side effects (lazy eval) ·
  a **mutation seen through an alias / second instance**.
- **Format** (`drill-generation.md` §6) — primarily **Prediction → Observation → Reflection**
  (predict under the analogy, run, reflect on where it broke); also **Teach-it-back**
  (state the general port-and-verify principle), **Error analysis** (here is a false-friend
  *bug someone wrote mapping from language X* — what did they assume?), and
  **Concrete-to-abstract transfer** (name the mapping outcome, then "where else will this
  bite?").

Keep an in-session log of the `(construct family, source analogy, mapping outcome, format)`
tuples used; do not repeat a tuple until the others are exercised.

### 5c. Common-error catalog

The *specific* mapping failures, each with the conceptual gap it diagnoses
(`drill-generation.md` §1c format). Grounded in the transfer literature (negative transfer —
Thorndike & Woodworth 1901; Salomon & Perkins 1989; far transfer is unreliable — Barnett &
Ceci 2002) and the notation-dependence refutation (Gilmore & Green 1988), not in trivia.
**The root of most of them is one inversion: treating the surface analogy as the *answer*
(transliterate the syntax) instead of as a *hypothesis to port and verify* (port the
execution model, then run to convict the false friends).**

```
Error: Over-trusts the analogy — assumes same/similar surface ⇒ same behavior, and reports
       the source-language behavior as the Python answer without running it (predicts 7/2
       == 3; predicts 1 < 3 < 2 left-associates; predicts "3" + 4 == "34").
Diagnoses: The false-friend error. Treats the analogy as a conclusion, not a hypothesis;
           skips the executable check that the mapping invited. Negative transfer shipped
           unverified. (Thorndike & Woodworth 1901; Gilmore & Green 1988 — idioms are
           notation-specific.)
Example trigger: any false-friend Foundations drill (7/2; chained comparison; str+int).

Error: Memorizes syntax instead of porting the execution model — can recite "Python uses
       def for functions" but cannot predict what an unseen construct DOES (when it runs,
       what mutates, what is shared).
Diagnoses: Collecting surface forms without re-using/repairing the notional machine (A1).
           Syntax is the cheap, transferable-anyway part; the execution model is the part
           that needed porting and was skipped.
Example trigger: a generator or context-manager drill where syntax is obvious but the
                 behavior (laziness; exception suppression) is not.

Error: Transliterates a source idiom into Python syntax instead of using the target idiom
       (writes a C-style index loop with range(len(...)) where enumerate fits; rebuilds a
       manual swap with a temp; hand-rolls a copy loop instead of a[:] / list(a)).
Diagnoses: Ports the idiom literally, missing that idioms are notation-specific — the
           concept transfers but the idiomatic SURFACE does not. Re-notation outcome
           mishandled. (Gilmore & Green 1988; A2 plans/beacons across languages.)
Example trigger: a re-notated-idiom drill (swap; enumerate; list copy).

Error: Assumes NOTHING transfers — re-derives sequencing, branching, arithmetic, function
       call/return from scratch in the new language; slow and anxious on the parts that
       already work.
Diagnoses: The opposite failure — ignores the large shared core that transfers for free
           (identical elements). Spends attention on true friends instead of on false
           friends and genuinely-new constructs. (Thorndike & Woodworth 1901; corollary 2.)
Example trigger: a true-friend drill (== as value equality; 7 % 2) where the learner
                 over-checks the obvious and under-checks the trap.

Error: Over-generalizes ONE language's model as "how programming works" — treats a
       language-specific behavior as universal (expects ++ to increment; expects pass-by-
       value everywhere; assumes try/finally semantics for with; assumes per-instance fields
       for a class-body assignment).
Diagnoses: Egocentrism (Pea's term, cross-language flavor): the learner's first language is
           mistaken for the universal machine, so language-specific traits become invisible
           and un-checked. Far transfer fails because the abstraction was never lifted.
           (Salomon & Perkins 1989 — far transfer needs the high road.)
Example trigger: ++x as a no-op; class-attribute sharing; with/__exit__ suppression.

Error: Maps to the WRONG analogy — picks a source construct that is superficially similar
       but mechanically different (maps Python generators to "a function that returns a
       list"; maps `is` to "value equality"; maps with to "just try/finally").
Diagnoses: Surface-feature matching instead of execution-model matching. The analogy is
           chosen by how it LOOKS, not by what it DOES — so the prediction is wrong in a
           confident-sounding way.
Example trigger: generator-vs-list drill; `is` vs `==` drill; with-suppresses-exception drill.

Error: Forces an analogy onto a genuinely-NEW construct and never builds the real sub-model
       (insists a generator "is basically a list," a decorator "is just a wrapper function
       call," and so cannot predict the surprising case).
Diagnoses: No "no-counterpart → learn fresh" category; refuses to drop to building the
           notional-machine sub-model from scratch (A1) where no analogy holds. (Genuinely-
           new outcome mishandled.)
Example trigger: generator laziness/exhaustion; context-manager protocol; decorator timing.

Error: Treats a single green run as proof the mapping is fully correct ("it printed the
       right thing once, so my analogy holds") — stops verifying at the happy path.
Diagnoses: Under-tests the repaired mapping; misses the boundary where the analogy still
           leaks (// floors on negatives; the int cache makes `is` "work" for small ints
           then fail for large). A calibration gap (F1): confidence outran the evidence.
Example trigger: the //-on-negatives boundary; the 256-vs-257 `is` cache drill.
```

### 5d. Grading mode

**Hybrid — executable prediction + rubric mapping** (`drill-generation.md` §1d, §3). Report
the two verdicts **separately**:

1. **Run the construct (the executable sub-claim).** The learner predicts the behavior
   *under their analogy*; the coach **runs the snippet** via
   `python <skill-dir>/runtime/python/runner.py snippet.py`, parses the `RunResult`, and
   grades the prediction against `stdout` (strip the trailing newline) and/or `status` (for
   "does it raise?") and/or an `is`/identity print. **The run is what verifies the mapping**
   — a false-friend analogy is *convicted by the machine*, not by the coach's assertion
   (`coaching-loop.md` → Surface ground truth: paste the snippet and its real output into
   the reply). This half is **executable ground truth**: never guess it.
2. **Score the mapping against the F3 rubric (§7), criterion by criterion** — *did they name
   a sensible source analogy? did they classify the construct correctly (true friend / false
   friend / new / re-notated)? did they give the execution-model reason the analogy held or
   broke, not just "it's different"? did they propose the repaired mapping / target idiom?*
   This half is **rubric + golden exemplars** and is **explicitly softer** than the run: the
   coach says so out loud (`drill-generation.md` §3). Cite the closest exemplar in
   `exemplars/F3/<tier>.md`.

Report separately, because the central F3 partial-pass is a **right prediction with a wrong
or absent mapping**: a learner who predicts `3.5` because they *already knew* Python (not
because they ported and verified) has the *product* but not the *process* — flag it as a
Foundations-level pass at best (`evidence-base.md` → illusions of fluency), and re-probe with
a construct they *haven't* seen. The mirror case — a **good mapping with a wrong prediction**
(sound analogy, sound execution-model reasoning, arithmetic slip) — is the *stronger* signal
and routes **up**, exactly as `assessment.md` Part 1.3 prescribes.

**Honesty about the grader's reach.** The runner is **Python-only**. So F3's executable
verification is *demonstrated* on Python idioms — but the **principle** (a mapping is a
hypothesis; verify it against ground truth) generalizes to languages the runner **cannot**
execute, where "the runner" becomes the language's own **REPL / unit test / spec**. When a
drill or transfer task is in a non-Python stack, the coach grades the *reasoning and the
verification plan* and says plainly: **"I can't run this here; the verification step is yours
to do in that language's REPL/tests — and naming that step is part of the skill."**

---

## 6. Frontier band

Frontier is not a fixed tier — it tracks the learner's **demonstrated ceiling** and presses
**one step** past their last comfortable success along a single parameter axis
(`drill-generation.md` §5). Escalating two steps collapses to failure; escalating none loses
the desirable-difficulty benefit.

**What "one step" means here** (per `drill-generation.md` §5):
- **Advanced** = one genuinely-new-or-false-friend construct mapped, predicted, run, and
  explained with its analogy *and the analogy's limit*.
- **Frontier-N** = N increments beyond Advanced; each increment adds exactly one new
  interacting mechanism OR pushes one parameter-space dimension up one notch.
- The learner's current Frontier-N is the highest N they have passed.

Escalation directions beyond Advanced for F3, with step counts:

1. **Compose constructs so the false friends interact** (push the construct axis): a
   generator whose values are mutable defaults (laziness + shared mutable) → Frontier-1; add
   a context manager around it whose `__exit__` interacts with the generator's `close()` →
   Frontier-2. Each interacting construct is one increment.

2. **Map from a more distant source language** (push the *near→far* transfer axis, the
   hardest direction per Barnett & Ceci 2002): from a C-family false friend (near) → to
   mapping **Haskell laziness** onto Python generators, or **SQL set-semantics** onto Python
   `set`/comprehensions, or **Rust ownership/borrowing** onto Python's reference model
   (far). Each jump in paradigm distance is one increment — and the coach names that far
   transfer needs the *deliberate* high road, not a reflex.

3. **Framework-/idiom-level mapping, not one construct** (push the surface axis): map a
   *pattern*, not a keyword — a route **decorator** in a web framework, `async`/`await`
   scheduling, list-comprehension-as-`map`/`filter` from FP, an ORM's lazy query. The unit of
   transfer is now an idiom cluster; each level up (construct → idiom → framework pattern) is
   one increment.

4. **Reverse the direction — map *out* of Python into a target language you are learning**
   (push the source/target axis): given a Python idiom you own, predict where **your Python
   habits become false friends in Go / Rust / JS** (e.g., "Python's `for x in xs` over a dict
   gives keys — does Go's `range`? does JS's `for...in` vs `for...of`?"). Anticipating your
   *own* negative transfer is one increment harder than catching it in Python.

5. **Verify without the runner — the AI-era frontier** (push the verification axis to the
   honest limit): a construct in a language the runner **cannot execute**, where the learner
   must port-and-predict and then **name how they would verify** against that language's
   REPL/tests/spec — and state the **residual uncertainty** they cannot close from the
   armchair. This is exactly verifying agent-generated code in a stack you don't yet own:
   one increment for "no runner," another for "and the surface reads fluent, so you must not
   trust it" (ties to F1 calibration, E3 review).

Track the level as `F3: Frontier-N`. Reset condition: two consecutive failures at the same
level → drop to Advanced for one drill, then re-approach (`drill-generation.md` §5).

---

## 7. Mastery rubric

The observable per-tier bars, instantiating the rubric shape of `assessment.md` Part 2,
scored on the two F3 dimensions. Two cross-cutting requirements apply at every tier above
Foundations: **product *and* process** (right, run-verified prediction *and* a sound mapping
— a correct prediction with an absent/wrong mapping is a Foundations-level pass at best,
often "I already knew Python," not "I ported and verified"), and **unaided + durable** (a
same-session streak is provisional until a delayed re-assessment or the real-language
transfer task confirms it; `assessment.md` Parts 3–5).

**The two scored dimensions** (each 3-point: absent / partial / solid):

- **D1 — Predict (executable).** Did the learner predict the construct's behavior, and is the
  prediction right when the coach **runs** it? *(Executable sub-claim; §5d. A right prediction
  the learner couldn't have *derived* — they just knew Python — counts only as Foundations.)*
- **D2 — Map (rubric).** Did they name a sensible source analogy, **classify** the construct
  (true/false friend / new / re-notated), give the **execution-model reason** it held or
  broke, and state the **repaired mapping / target idiom** — rather than report the source
  behavior or hand-wave "it's just different"?

| Tier | Observable bar for F3 |
|---|---|
| **Foundations** | On a single, clear true/false-friend mapped from a close language, **predicts the behavior under the analogy** and, after the run, **names what is the same and what is different** (e.g., "`7 / 2` looked like C's int division but is `3.5` — true division; `//` is the one I wanted"). D1 solid; D2 at least partial (classifies it and gives the gist of why). Allowed *with* the worked example faded to one missing step. |
| **Working** | On a more-tempting false friend in an unseen context (mutable default; `is`/cache; shallow copy), **unaided**: predicts, and after the run **articulates the execution-model reason** the analogy broke (defaults evaluated once at definition time; `is` is identity not value; `[:]` copies the outer list only) and the repaired mapping. On 3 of 4 such unseen drills. A right prediction with no execution-model reason ⇒ partial pass, flagged. |
| **Advanced** | On a **genuinely-new** construct or a **two-mechanism** false friend (generator laziness; `with`/`__exit__` suppression; class-attribute sharing), **unaided**: builds/ports the sub-model, predicts (run-verified), **explains why**, and names the analogy **and its limit** ("`with` is like RAII/try-with-resources for cleanup — but `__exit__` returning truthy *suppresses* the exception, which `finally` does not"). Articulates the **general port-and-verify principle** on a teach-it-back, not just the instance. |
| **Frontier** | `Frontier-N`: presses one dimension past the last comfortable success per §6 / `drill-generation.md` §5 (compose constructs → map from a distant paradigm → framework-level idiom → map *out* of Python → verify without the runner). A moving target, not a fixed bar. |

Promotion is by **performance, not tenure** (`assessment.md` rule 1); the coach marks a tier
from what the learner *does* on unseen constructs, never from "I know five languages." Held-out
re-assessment and **real-language transfer** outrank a same-session streak (`assessment.md`
Part 5) — and because the runner is Python-only, the real-language signal (a false friend the
learner caught while actually learning a new stack) is weighted heavily.

---

## 8. Anti-patterns & evidence caveat

**Anti-patterns this module exists to break** (each is a catalog entry in §5c, surfaced as a
*behavior*):

- **Shipping the untested analogy (false-friend over-trust).** Reporting the source-language
  behavior as the Python answer because the surfaces match. The signature F3 error. The fix
  is mechanical: predict *under* the analogy, then **run** it — the analogy is a hypothesis,
  and the false friend lives exactly where the surfaces are identical.
- **Memorizing syntax instead of porting the machine.** Collecting "how do I write X here"
  trivia while never asking the A1 questions (*when does this run, what mutates, what is
  shared, what does it evaluate to*). Syntax transfers anyway; the execution model is the
  part that needed porting. The fix: port the machine first, treat syntax as the cheap layer.
- **Transliterating idioms.** Writing language-A idioms in language-B syntax
  (`range(len(...))` index loops; hand-rolled swaps and copies) instead of the target idiom.
  Idioms are notation-specific (Gilmore & Green 1988); the concept transfers, the surface
  does not. The fix: learn the target idiom; don't port the source one literally.
- **Re-deriving the true friends (assuming nothing transfers).** Slowly rebuilding
  sequencing, branching, and arithmetic in every new language. The fix: trust the shared core
  (identical elements), and spend attention on the false friends and the genuinely-new.
- **Mistaking your first language for the universal machine.** Treating `++`, pass-by-value,
  `try/finally` semantics, or per-instance fields as how *programming* works. The fix: lift
  the abstraction (the high road) so language-specific traits become visible and checkable.
- **One green run = "my mapping is correct."** Stopping at the happy path while the repaired
  analogy still leaks at the boundary (`//` on negatives; the small-int cache). The fix:
  verify the repair where it is most likely to differ — a calibration discipline (F1).

**Evidence caveat (this is a `[Verified-adjacent]` module — say so).** F3's grounding is
mixed and must not be oversold:

- **What you port is Verified-tier** — the notional-machine finding (Finding 1) is among the
  best-supported results in the curriculum. That part carries no inflated claim.
- **Why porting works is `[Verified-adjacent]` general science** — transfer-of-learning
  (Thorndike & Woodworth 1901; Salomon & Perkins 1989; Singley & Anderson 1989) is solid
  cognitive psychology, but established mostly **outside programming**; the programming-
  adjacent anchor is **1989, on editors**, not modern frameworks. State it as "well-
  established in learning science generally; the programming-specific evidence is thinner,"
  never "research proves you'll learn Python faster."
- **Why porting is unsafe is a hard, reused fence** — negative transfer / false friends are
  real and **notation-dependent** (Gilmore & Green 1988, already in the evidence base's
  Refuted list), and **far transfer is unreliable and often fails to happen spontaneously**
  (Barnett & Ceci 2002). These are *why the module's discipline exists*, not caveats bolted
  on after.
- **The curriculum-wide transfer caveat applies in full.** That **explicitly** teaching this
  mapping discipline *causally* makes a working engineer learn languages faster is the open
  question every module here carries. The coach leans on the transfer task (§9) — the skill on
  a language the learner is *actually* learning — as the honest individual-level evidence.
- **The AI-era priority** (verifying code in an unfamiliar stack rises as agents draft it;
  spec §12) is `[Verified-adjacent]` — **priority-steering, not proof**.

No claim in this module is dressed above its badge.

---

## 9. Transfer task

**The only honest test of whether the gym drill transferred is applying it to a language or
framework you are *actually* learning** (`assessment.md` Part 4; `evidence-base.md` → transfer
caveat, consequence 2). Because the runner is Python-only, this is also where the skill leaves
the sandbox and meets the real, un-runnable stacks where it matters most.

> **Your turn:** Pick a language or framework you have **recently learned or are learning**
> right now (not one you already own). Find a construct in it that **surprised you** — code you
> had to run twice, a bug that made you say "wait, that's not how it works where I come from,"
> or an idiom you wrote the long way before learning the short way.
>
> Now **port it out loud.** **(1) Name the analogy you used:** which construct in a language you
> already know did you map this onto? **(2) Classify it:** true friend, false friend, genuinely
> new, or same-concept-different-notation? **(3) Locate the break:** if it was a false friend,
> name the *exact* behavioral difference — and the execution-model reason for it (when it runs,
> what it shares, what it evaluates to), not just "it's different." **(4) Verify it:** if the
> language is runnable, reduce the surprise to the smallest snippet and **run it in that
> language's REPL / a unit test** to convict the mapping (in Python, use our runner). If it is
> *not* easily runnable here, **say how you would verify it** in that stack — and name the
> residual uncertainty you cannot close from the armchair.

**Grading is softer and named as such** (`assessment.md` Part 4). A real language has no clean
answer key, and for most non-Python stacks the coach **cannot run it here** — so the coach
grades the **mapping and the verification plan** against the §7 rubric and says: *"this is a
judgment call on your real learning, and for this language the run is yours to do — naming that
step is part of the skill."* Where the construct **is** runnable (Python, or a REPL the learner
can drive), the coach still insists on the executable check: **reduce it to a minimal snippet
and confirm the behavior before the learner trusts the mapping** (the same discipline as the
§5d run). **Transfer evidence is weighted heavily:** a learner who aces synthetic Python
false-friend drills but cannot recount, classify, and explain a single real false friend from
their own language-learning has **not** transferred the skill — the tracker notes that gap as
more diagnostic than another passed synthetic drill.

---

## Cross-references

- Drill mechanics, the **hybrid grading path** (executable prediction + rubric mapping),
  the executable check that *verifies the mapping*, exercise formats (Prediction → Observation
  → Reflection, Teach-it-back, Error analysis), Frontier escalation:
  `references/drill-generation.md` (this module instantiates §1 and follows §2, §3, §4, §5).
- Session delivery (pause/no-spoiler hard stop after posing the predict-under-the-analogy
  question, tier-faded worked example, direct feedback, **surface the run** so the learner
  sees the mapping convicted): `references/coaching-loop.md`.
- F3 entry task (map an unfamiliar idiom onto a known concept, predict, then verify by
  running — catching where the analogy breaks), per-skill routing, mastery-rubric shape,
  held-out re-assessment, **real-language transfer** weighting: `references/assessment.md`
  (Part 1.4 — proposed F3 entry task; Part 1.3 partial-knowledge boundary).
- Evidence grounding — the notional machine you **port** (**Finding 1**); the **transfer-of-
  learning** addition (Thorndike & Woodworth 1901; Salomon & Perkins 1989; Singley & Anderson
  1989; Barnett & Ceci 2002 — `evidence-base.md` → *Learning new languages & frameworks —
  transfer of learning (module F3)*); the **notation-dependence / false-friend fence**
  (Gilmore & Green 1988, reused from the Refuted list); the AI-era verification priority; the
  worked-examples / expertise-reversal instructional finding: `references/evidence-base.md`.
- Soft prerequisites — the machine you port (**A1**, notional machine) and idioms-as-plans
  across languages (**A2**, code reading & chunking); related calibration/review modules
  **F1**, **E3** (the AI-era "verify the unfamiliar stack" tie).
- Golden exemplars (~3 per tier, each with a **runner-verified** prediction key + the gold
  mapping + Diagnoses): `exemplars/F3/foundations.md`, `exemplars/F3/working.md`,
  `exemplars/F3/advanced.md`.
</content>
</invoke>
