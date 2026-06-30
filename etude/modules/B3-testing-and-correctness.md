# B3 — Testing & Specifying Correctness `[Practitioner-canon]`

> **Module type.** `[Canon + some empirical]` craft-and-specification module. The
> evidence here is **mixed and honestly badged**: the *test-design techniques* (edge
> cases, equivalence partitioning, boundary-value analysis, properties/invariants,
> metamorphic relations) are **practitioner canon** — durable, widely taught craft, but
> *not* replicated empirical findings. The *empirical* layer is the meta-analytic evidence
> on **Test-Driven Development**, which is genuinely **contested** (small quality effect,
> null-to-negative productivity effect, and the test-first ritual may not be the active
> ingredient). This module teaches the craft and states the evidence-status out loud — it
> does **not** sell TDD as proven.
>
> **Core idea.** A test is a **specification of correct behavior, checked by execution.**
> The skill is **not** "write a test that passes"; it is **deciding what "correct" means**
> for a function (its contract), **enumerating the inputs that could break it** (edges,
> boundaries, empty/degenerate, duplicates, overflow), and writing checks that would
> **fail on a wrong implementation**. The discipline in one line: ***a test that can't
> fail proves nothing — adversarially hunt the input that breaks your own code.***

---

## 1. Evidence basis `[Canon + some empirical]`

This module is **mixed-status by design**, and the coach must keep the two layers
distinct. **Honesty rule (from `evidence-base.md`): never present canon as verified
science.** The canon citations below are grounded in `evidence-base.md` → Module-specific
& craft sources (the B3a `[Practitioner-canon]` and B3b `[Some empirical] — MIXED` blocks),
where each was verified against primary sources during this module's authoring. The
TDD-evidence layer connects to the AI-era B3 priority already in `evidence-base.md`
("AI code carries defects" → B3).

### 1a. The canon layer — test design `[Practitioner-canon]`

Respected, widely taught engineering craft. Vetted against the named primary sources, but
it is **doctrine and technique, not experimentally validated science**. The coach says:
*"This is respected practice — not a verified research finding."*

- **Myers, G. J. (1979). The Art of Software Testing.** John Wiley & Sons (1st ed.;
  later eds. 2004 / 2011 with Sandler, Badgett, Thomas). The canonical source for the
  black-box test-design techniques this module drills: **equivalence partitioning**
  (divide the input domain into classes such that one representative tests the whole
  class) and **boundary-value analysis** (defects cluster at the *edges* of ranges, so
  test *at* and *just across* each boundary). Also the foundational argument that
  **exhaustive testing is generally impossible** — so the central problem of testing is
  *choosing the subset of cases most likely to find the most errors.* Craft doctrine, not
  a replicated empirical result.

- **Dijkstra, E. W. (1969/1970). Notes on Structured Programming (EWD249);** published as
  the lead essay in Dahl, Dijkstra & Hoare, *Structured Programming* (Academic Press,
  1972). Source of the load-bearing aphorism, verbatim: **"Program testing can be used to
  show the presence of bugs, but never to show their absence!"** This is a *logical*
  observation by a major figure, not data — but its provenance is exactly verifiable
  (EWD249, §"On the reliability of mechanisms"). It is the spine of this module's
  adversarial stance: passing tests ≠ correct.

### 1b. The oracle / property layer — how to test without a full answer key `[Practitioner-canon / research methods]`

- **Barr, Harman, McMinn, Shahbaz & Yoo (2015). The Oracle Problem in Software Testing:
  A Survey.** *IEEE Transactions on Software Engineering*, 41(5), 507–525.
  doi:10.1109/TSE.2014.2372785. Peer-reviewed *survey* of CS research. Defines a **test
  oracle** as "a procedure that distinguishes between the correct and incorrect behaviors
  of the System Under Test," and names the **oracle problem**: for a given input, deciding
  the correct behavior is itself hard, and is "a significant bottleneck that inhibits
  greater test automation." This is *why* asserting on exact outputs is sometimes
  impossible — and motivates properties.

- **Claessen, K., & Hughes, J. (2000). QuickCheck: A Lightweight Tool for Random Testing
  of Haskell Programs.** *ICFP '00*, 268–279. doi:10.1145/351240.351266. The origin of
  **property-based testing**: state a *universally-quantified property* (a law that must
  hold for all inputs), generate random inputs, and report a counterexample when one
  falsifies it. **Verified caveat:** the *original 2000 paper does NOT have built-in
  automatic shrinking* — it prints the first random counterexample; automatic
  minimization of failing cases came later (a user extension in the paper; standardized in
  later QuickCheck/Hedgehog/Hypothesis lineage). A tool/methods paper (won the SIGPLAN
  Most-Influential-Paper award), **not** an empirical effectiveness study.

- **Hughes, J. (2019). How to Specify It! A Guide to Writing Properties of Pure
  Functions.** *Trends in Functional Programming (TFP 2019)*, LNCS 12053, 58–83.
  doi:10.1007/978-3-030-47147-7_4. Practitioner tutorial: a taxonomy of property kinds —
  **invariants, postconditions, metamorphic/algebraic relations, model-based** — that this
  module's Advanced tier teaches. Canon/tutorial, not science.

- **Metamorphic testing.** Chen, Cheung & Yiu (1998), *Metamorphic Testing: A New Approach
  for Generating Next Test Cases* (Tech. Report HKUST-CS98-01) — origin; and **Segura,
  Fraser, Sánchez & Ruiz-Cortés (2016). A Survey on Metamorphic Testing.** *IEEE TSE*,
  42(9), 805–824. doi:10.1109/TSE.2016.2532875. The idea: check **metamorphic relations**
  between *multiple* executions that must hold *even when the exact correct output is
  unknown* (textbook example: `sin(x) == sin(π − x)`; or `sorted(xs)` and
  `sorted(shuffle(xs))` are equal). A practical answer to the oracle problem.

### 1c. The empirical layer — TDD is contested `[Some empirical — MIXED]`

This is the only part of B3 with replicated-ish empirical weight, and it is **honestly
mixed** — the coach must not inflate it.

- **Rafique, Y., & Mišić, V. B. (2013). The Effects of Test-Driven Development on External
  Quality and Productivity: A Meta-Analysis.** *IEEE TSE*, 39(6), 835–856.
  doi:10.1109/TSE.2012.28. Meta-analysis of 27 studies. Headline (verbatim): TDD has **"a
  small positive effect on quality but little to no discernible effect on productivity,"**
  with the quality gain *and* a productivity *drop* both **larger in industrial than
  academic** settings, and the productivity drop tracking how much *more* the TDD group
  tested — a **confound**, not a clean TDD effect.

- **Turhan, Layman, Diep, Erdogmus & Shull (2010). How Effective Is Test-Driven
  Development?** Ch. 12 in *Making Software* (O'Reilly, eds. Oram & Wilson), 207–217.
  Narrative systematic review of 22 reports / 32 trials. Verbatim conclusion: **"the
  evidence is not undisputedly consistent regarding TDD's effects on any of the
  measures."** The apparent external-quality benefit **"disappears after filtering out the
  less rigorous studies."**

- **Fucci, Erdogmus, Turhan, Oivo & Juristo (2017). A Dissection of the Test-Driven
  Development Process: Does It Really Matter to Test-First or to Test-Last?** *IEEE TSE*,
  43(7), 597–614. doi:10.1109/TSE.2016.2616877. (Companion replication: **Fucci et al.
  (2016)**, *An External Replication…Multi-Site Blind Analysis*, ESEM '16,
  doi:10.1145/2961111.2962592 — found TDD effects largely **not** significant.) Finding
  (verbatim): **"Sequencing, the order in which test and production code are written, had
  no important influence"**; what helped was **granularity and uniformity** — small,
  steady, fine-grained steps. *The test-first ritual that defines TDD is not the active
  ingredient.*

- **Inozemtseva, L., & Holmes, R. (2014). Coverage Is Not Strongly Correlated with Test
  Suite Effectiveness.** *ICSE '14*, 435–445. doi:10.1145/2568225.2568271 (ACM
  Distinguished Paper). Using mutation testing on five real Java projects: once you
  **control for the number of test cases**, coverage is only *low-to-moderately* correlated
  with fault-detection effectiveness, and *stronger* coverage criteria don't help much.
  **High coverage ≠ good tests.** This is the empirical backstop for the module's
  "coverage is not correctness" anti-pattern.

**What the canon vs. empirical split licenses the coach to say.** Test-*design* technique
("test the boundary, the empty case, the duplicate") is taught as **craft that works in
practice** — never "research shows." The *TDD-process* claims are taught with their real
uncertainty: ***the value is in disciplined small steps and in specifying behavior, not in
the test-first ceremony, and high coverage does not prove correctness.***

**Read through the transfer caveat** (`evidence-base.md`): even the empirical layer here is
mostly **student/academic and small-N**; its causal application to upskilling experienced
engineers is open. The transfer task (§9) — adversarially testing the learner's *own*
code — is the honest individual-level evidence.

---

## 2. Soft prerequisites

Per `assessment.md`, soft prerequisites **inform, they never gate** (the buffet rule: any
learner may open any module at any tier). B3 leans *softly* on:

- **A1 (notional machine)** — to enumerate the input that breaks a function, you must be
  able to *simulate* what the function does to that input. Edge-case hunting is applied
  execution-model reasoning.
- **A3 (tracing)** — "which single input is wrong?" is a trace under an adversarially
  chosen input; B3 is tracing pointed at the *boundaries* rather than the happy path.
- **B2 (code writing)** — writing the test itself is small-scale code composition.

If B3 is weak *and* A1/A3 are weak, the tracker notes the testing gap likely traces back
to execution-model/tracing gaps — but the coach does **not** forbid B3. A learner may
start here cold; the Foundations tier assumes only that they can read a short function.

---

## 3. The mental model

**A test is a specification of correct behavior, checked by execution. Writing tests is
not "making the code pass" — it is (1) deciding what *correct* means for this function
(its contract), (2) adversarially enumerating the inputs that could violate it, and (3)
writing checks that would *fail* on a wrong implementation.** A test that cannot fail
proves nothing.

Three pillars, and the discipline that drives them:

| Pillar | What it is |
|---|---|
| **The contract** | What the function *promises*: its **precondition** (what inputs it accepts), its **postcondition** (what must be true of the output given valid input), and its **invariants** (what stays true throughout). The contract is the *oracle* — the thing that tells you "correct" from "incorrect" (Barr et al. 2015). If you can't state the contract, you can't test it; you can only sample it. |
| **The case space** | The set of inputs partitioned by behavior. **Equivalence classes** (inputs the function should treat the same — test one representative each) and **boundaries** (the edges *between* classes, where defects cluster — test *at* and *just across* each: 0, 1, the max, the empty collection, the single element, the duplicate, the just-over-the-limit). Exhaustive testing is impossible (Myers 1979), so the skill is *choosing the cases most likely to expose a wrong implementation.* |
| **The oracle** | How you *know* the answer for a given case. Sometimes you can assert the **exact output** (`f(2) == 4`). When you can't (the oracle problem), you assert a **property** that must hold for *all* inputs — an invariant (`len(sort(xs)) == len(xs)`), a postcondition (`sort(xs)` is non-decreasing), an algebraic/**metamorphic relation** (`sort(xs) == sort(shuffle(xs))`; `reverse(reverse(xs)) == xs`), or agreement with a **simple reference model**. |

**The transition rule of testing: a test earns its keep only if some *wrong*
implementation makes it fail.** This is the operational form of Dijkstra's aphorism
(testing shows the *presence* of bugs, never their absence). A test that passes on both
the right code and an obviously-broken version is **vacuous** — it specifies nothing. So
the discipline is adversarial and *self-directed*: assume your code is wrong, and hunt the
input that proves it.

**The discipline in one line: *adversarially hunt the input that breaks your own code.***
The most common failure is the opposite reflex — confirmation testing: feeding the
function the inputs you already know it handles (the **happy path**) and reading green as
"correct." Green on the happy path is the *weakest* possible evidence. Three moves are the
usual culprits, and the module drills them:

1. **Boundaries and degenerate cases over typical cases.** The bug lives at `n == 0`, the
   empty list, the single element, the duplicate key, the off-by-one at the end — not at
   the comfortable middle of the range. (Myers' boundary-value analysis.)
2. **Behavior, not implementation.** Assert the function's *contract* (what it must do for
   the caller), not the incidental details of *how* it currently does it. A test that
   breaks when you rename a private variable or reorder two equivalent steps is testing the
   wrong thing — it will cry wolf on every refactor and still miss real bugs.
3. **Properties when there is no exact oracle.** When you can't write down the expected
   output, write down what must *always* be true regardless of input — and let many inputs
   attack it (Claessen & Hughes 2000; Hughes 2019).

---

## 4. Worked example — from a function to an adversarial case list

*(Foundations depth: every step shown. This fades by tier — see the note after.)*

The skill is to **interrogate a function for how it could be wrong**, not to confirm it is
right. Consider a function with a precise contract:

```python
def in_range(x, lo, hi):
    """True iff x lies in the CLOSED interval [lo, hi] — both ends included.
    Precondition: lo <= hi. Postcondition: returns True exactly when lo <= x <= hi."""
    return lo <= x <= hi
```

**Step 1 — State the contract (the oracle).** Precondition: `lo <= hi`. Postcondition:
returns `True` **exactly when** `lo <= x <= hi` — the interval is *closed*, so `x == lo`
and `x == hi` are both inside. That "exactly when, both ends included" is the thing that
decides correct from incorrect. (A `<` instead of `<=` at either end is the classic bug.)

**Step 2 — Partition the input space into equivalence classes.** By *behavior*, `x` falls
into three classes: **below `lo`** (→ `False`), **inside `[lo, hi]`** (→ `True`),
**above `hi`** (→ `False`). Each class needs at least one representative.

**Step 3 — Find the boundaries between the classes** (where defects cluster). The edges are
`x == lo` and `x == hi` — exactly the spots a `<` vs `<=` mistake flips the answer. So the
boundary cases are `x == lo`, `x == hi`, and one step either side: `lo - 1`, `lo + 1`,
`hi - 1`, `hi + 1`.

**Step 4 — Add the degenerate / adversarial cases the happy path skips.** `lo == hi` (the
range is a single point — only `x == lo` should be `True`); `x` far outside on both sides;
(and, as a *contract question*) what about `lo > hi` — is that the caller's bug or the
function's? Naming that the contract is silent on it is itself the skill.

**The gold case list** (what a strong learner enumerates), each tagged with the
class/boundary it attacks:

| # | Input | Class / boundary | Expected (the oracle) | Why it matters |
|---|---|---|---|---|
| 1 | `in_range(5, 0, 10)` | inside (typical) | `True` | happy path — necessary, weakest |
| 2 | `in_range(-3, 0, 10)` | below `lo` | `False` | below-range class |
| 3 | `in_range(99, 0, 10)` | above `hi` | `False` | above-range class |
| 4 | `in_range(0, 0, 10)` | **boundary** `x == lo` | `True` | `<` vs `<=` at low edge |
| 5 | `in_range(10, 0, 10)` | **boundary** `x == hi` | `True` | `<` vs `<=` at high edge |
| 6 | `in_range(11, 0, 10)` | just above `hi` | `False` | off-by-one at the top |
| 7 | `in_range(5, 5, 5)` | **degenerate** `lo == hi` | `True` | single-point range, `x` on it |
| 8 | `in_range(4, 5, 5)` | degenerate, `x` just below | `False` | single-point range, miss |

**Step 5 — Reach for a *property* (the oracle generalized).** Beyond specific cases, one
statement covers *all valid inputs*: **for every `x` and every `lo <= hi`,
`in_range(x, lo, hi)` is `True` if and only if `lo <= x` and `x <= hi`.** That single
biconditional, attacked by many random inputs, is worth more than a dozen hand-picked
cases — and it is exactly what a wrong `<`/`<=` at either end violates.

**Why this beats happy-path testing:** cases 1–3 (one per class) *all pass* on a buggy
`in_range` that uses `lo <= x < hi` (a half-open interval — the `hi` end wrongly excluded):
the interior `5`, the far-below `-3`, and the far-above `99` give the same answer under the
bug. The bug shows **only at the boundary** `x == hi` (case 5): correct says `True`, the
buggy half-open version says `False`. Confirmation testing reads green and ships the bug;
adversarial case-listing *targets the boundary where the bug lives.* That is the whole
skill. (All eight rows and this claim were runner-verified during authoring.)

> **Expertise reversal — the worked example fades by tier.** Per the worked-examples
> finding (`evidence-base.md` → instructional pillar; `coaching-loop.md` Step 2), a full
> enumeration *helps novices* (it lowers extraneous load while the schema forms) but
> becomes **redundant load for the more advanced**, who learn more by enumerating
> themselves:
>
> | Tier | Worked-example depth at B3 |
> |---|---|
> | **Foundations** | **Full** — contract stated, all classes and boundaries enumerated, the gold table above shown and explained. |
> | **Working** | **Partial** — coach states the contract and names the *classes*, then leaves the learner to find the boundaries and the degenerate cases (and to write a test that fails on a supplied buggy version). |
> | **Advanced** | **Skeleton** — coach hands only the function and asks for the contract, the case list, *and* a property; or asks "what does a naive suite here miss?" |
> | **Frontier** | **None** — straight to the problem (§6). |

---

## 5. Drill-generation spec

Instantiates the generation-spec format of `drill-generation.md` §1 for B3. Grading mode
is declared up front and is **mixed**: some drills are **executable** (run the learner's
test against implementations), some are **rubric** (enumerate-cases / specify-contract).

### 5a. Tier definitions (B3-specific)

The curriculum-wide tier names (`drill-generation.md` §1a) translated to this module:

| Tier | B3 criterion | Example shape |
|---|---|---|
| **Foundations** | One function with an *obvious* contract on a familiar surface. **Enumerate the edge cases it must handle**, or name **which single input makes it wrong**. Recognize boundary / empty / single-element cases. | "List the edge cases for `clamp` / `last_element` / `average`." / "Which one input breaks this `running_max`?" |
| **Working** | A function where the happy path *passes* but a boundary/degenerate case fails. **Write a test that catches the bug** (fails on the buggy impl, passes on the fixed one), or **state the function's contract** (pre/post/invariants) precisely. Intent and a naive suite diverge. | "Here's a buggy `dedupe` and a fixed one — write a test that distinguishes them." / "State the contract of `binary_search`." |
| **Advanced** | **Property/invariant thinking**: what must *always* hold regardless of input (invariant, postcondition, metamorphic relation, model agreement). Or **find the subtle correctness gap a naive test suite misses** — the case the obvious tests skip. | "What property must `merge(sort)` always satisfy?" / "This suite is green but the function is wrong — find the missing case." |
| **Frontier** | See §6 — a moving target one step past the learner's last comfortable success. | — |

A drill is mis-tiered if it requires more than its tier allows (e.g., a Foundations drill
that needs a metamorphic relation is really Advanced); apply the self-check
(`drill-generation.md` §4) and re-level before posing.

### 5b. Parameter space (axes the coach varies to avoid mode-collapse)

Pick a *different point on each axis* across successive drills (`drill-generation.md` §1b,
§4 check 3). The axes for B3:

- **Function shape** — pure scalar→scalar (`clamp`, `abs_diff`) · collection→scalar
  (`max`, `average`, `count`) · collection→collection (`dedupe`, `sort`, `reverse`,
  `merge`) · search/predicate (`binary_search`, `contains`) · parser/format
  (`parse_int`, `split`) · stateful/accumulating.
- **Case category targeted** — boundary (off-by-one, `<` vs `<=`) · empty input · single
  element · duplicates · all-equal · already-sorted / reverse-sorted · negative / zero ·
  overflow / very large · `None` / missing · type-edge (mixed types) · ordering
  sensitivity.
- **Oracle type** — exact expected output · invariant (length preserved, bounded) ·
  postcondition (sorted, all-present) · **metamorphic relation** (`sort∘shuffle` stable;
  `reverse∘reverse == id`; permutation-invariance) · **reference-model agreement** (test
  against a slow obvious implementation).
- **Bug class (for Debug-this / write-a-test)** — off-by-one · wrong comparison operator ·
  empty-input crash (`IndexError`/`ZeroDivisionError`) · drops/duplicates an element ·
  mutates its input · returns the *right value by luck* on typical inputs only · ignores
  ties / ordering.
- **Predicted artifact / task** — *list* the cases · *name the one* breaking input ·
  *write* a test (executable) · *state* the contract · *state* a property · *find* the
  gap in a given suite.
- **Format** (`drill-generation.md` §6) — primarily **Debug-this** (write a test that
  catches the bug; executable-graded by running it on buggy vs. fixed), **Generation →
  Comparison** (enumerate cases / state contract, then compare to the gold list),
  **Teach-it-back** (articulate the contract / why a property holds), and
  **Error-analysis** (here's a green-but-wrong suite — what's missing?).

Keep an in-session log of the `(function shape, case category, oracle type, format)`
tuples used; do not repeat a tuple until the others are exercised.

### 5c. Common-error catalog

The *specific* testing failures learners make, each with the conceptual gap it diagnoses
(`drill-generation.md` §1c format). These are grounded in the testing-design canon — Myers
1979, Dijkstra (EWD249), Barr et al. 2015, Hughes 2019, Inozemtseva & Holmes 2014 — and in
real testing-failure patterns, **not** trivia. **The root of most of them is one
misconception: "a test exists to confirm my code works." The correct model is: "a test
exists to specify what *correct* means and to *fail* when the code is wrong" — passing is
the absence of a caught bug, never proof of correctness (Dijkstra).**

```
Error: Tests only the happy path — feeds inputs the function obviously handles (a
       typical mid-range value, a normal-sized non-empty list) and reads green as
       "correct."
Diagnoses: Confirmation testing — confuses "passes my test" with "correct." Samples a
           few comfortable inputs instead of partitioning the space and attacking the
           boundaries where defects cluster. The root meta-error of the module.
           (Myers 1979 boundary-value analysis; Dijkstra — presence, not absence.)
Example trigger: give clamp/running_max with a boundary bug (`<` vs `<=`); ask "what
                 would you test?" — a happy-path-only list passes the buggy version.

Error: Asserts on the implementation, not the behavior — checks a private/internal
       detail, exact call order, or an incidental representation, so the test breaks on a
       behavior-preserving refactor (and still misses real bugs).
Diagnoses: Tests "how" instead of "what." Has no contract in mind — is mirroring the
           current code rather than specifying the promise to the caller. Produces
           brittle suites that cry wolf and erode trust in the tests. (Contract thinking;
           §3 pillar 2.)
Example trigger: a function with two equivalent implementations (loop vs comprehension);
                 ask for a test — a test that pins the loop's intermediate state is
                 implementation-coupled; one that asserts the returned value is not.

Error: Misses the empty / single-element / degenerate input — never tests [], "", n==0,
       the one-element collection, or the all-equal case; the suite is green but the
       function raises or misbehaves there.
Diagnoses: Does not enumerate degenerate equivalence classes — treats "a list" as one
           class instead of {empty, one, many}. The empty case is the single most common
           missed boundary and the most common crash. (Myers equivalence partitioning.)
Example trigger: average(xs) that ZeroDivisionErrors on []; or first(xs) that
                 IndexErrors on []. Ask "enumerate the cases" — did empty appear?

Error: Misses duplicates / ties / ordering cases — tests only distinct, already-ordered
       inputs, missing repeated keys, equal elements, or reverse-sorted input.
Diagnoses: Assumes inputs are "nice" (distinct, sorted). Does not consider that equal or
           repeated elements form their own equivalence class where dedupe/sort/max
           stability bugs live. (Equivalence partitioning on a non-obvious axis.)
Example trigger: dedupe([1,1,2]) or a "stable" sort with equal keys; max with ties.

Error: Misses overflow / very-large / out-of-range inputs — tests only small inputs,
       missing the large value, the just-over-the-limit case, or accumulation that
       overflows a fixed width / exhausts memory / times out.
Diagnoses: No notion of the *upper* boundary of the input domain. Boundary-value analysis
           applied only to the low/empty end, never the high end. (Myers BVA, high edge.)
Example trigger: a fixed-width sum, an index near a size limit, or an O(n^2) routine on a
                 large list (runner status = "timeout" is itself the finding).

Error: Writes a test that cannot fail — asserts something trivially true (assert
       f(x) == f(x)), or so loose it passes on a broken implementation; equates the test
       passing with the code being right.
Diagnoses: Vacuous test. Does not apply the transition rule "a test earns its keep only
           if some WRONG implementation fails it." Confuses green with correct — the
           operational form of Dijkstra's aphorism. (Dijkstra EWD249; §3 transition rule.)
Example trigger: ask the learner to write a test, then run THEIR test against a planted
                 buggy impl — if it still passes, the test was vacuous.

Error: Equates high code coverage with a good test suite — "100% coverage so it's tested,"
       reasons from lines-executed rather than bugs-that-would-be-caught.
Diagnoses: Coverage-as-correctness. Coverage measures what ran, not what was checked;
           once test count is controlled, coverage is only weakly correlated with fault
           detection. A line can be covered by a test that asserts nothing about it.
           (Inozemtseva & Holmes 2014.)
Example trigger: a suite that calls the function on many inputs (high coverage) but
                 asserts only that it "doesn't crash" — covers every line, catches no
                 wrong-value bug.

Error: Insists on an exact-output assertion where the correct output is unknown or
       non-deterministic, then either can't write the test or pins an arbitrary value
       (over-specifying order, floating-point exactness, hash/set ordering, timestamps).
Diagnoses: Has only one oracle (exact equality) and no property/invariant/metamorphic
           tooling — hits the oracle problem and stalls. (Barr et al. 2015 oracle problem;
           Hughes 2019 / Segura 2016 properties & metamorphic relations.)
Example trigger: test a shuffler, a float computation, or a set-returning function with
                 `==` to a hardcoded literal — brittle or impossible; a property
                 (length preserved, all elements present, bounded error) is the fix.

Error: States a property that is too weak (true of broken code) or actually false (not an
       invariant) — e.g. "sort returns a list of the same length" only, missing
       orderedness; or "sort is idempotent on the original" stated as element-equality.
Diagnoses: Property-writing without checking it against a deliberately-wrong impl and
           against a correct one. A property must REJECT wrong implementations and ACCEPT
           the right one — same falsifiability bar as a case. (Hughes 2019 "How to
           Specify It"; the §3 transition rule applied to properties.)
Example trigger: ask for "a property of sort"; if the learner's property passes on a
                 sort that drops duplicates, it is too weak — run it to show the gap.
```

### 5d. Grading mode — **mixed**

B3 drills split by task type (`drill-generation.md` §1d, §3 hybrid):

- **Executable** (run the learner's artifact via `runner.py`):
  - **"Which single input makes this wrong?"** — the coach takes the learner's named
    input, runs the function on it (and on the contract's expected value), and confirms
    via `status`/`stdout` that it really does produce the wrong result. *The coach never
    guesses which input breaks it — it runs it.*
  - **"Write a test that catches this bug."** — the coach concatenates the learner's test
    with the **buggy** implementation and runs it (must yield `status: error` — the test
    *fails*, catching the bug), then with the **fixed** implementation (must yield
    `status: ok` — the test *passes*). A test that passes on the buggy impl is **vacuous**
    and graded a fail regardless of how it reads. (See §4-style verification; protocol in
    `drill-generation.md` §2.)
  - **"Find the gap a naive suite misses"** — the coach runs the learner's added case
    against the planted-wrong impl to confirm it actually exposes the bug.

- **Rubric** (judgment, graded against the gold list + the per-tier bar in §7 and the
  catalog in §5c; `drill-generation.md` §3 — the coach says "this is a judgment call
  graded against the rubric, not a machine-verifiable answer"):
  - **"Enumerate the cases"** — graded against the module's **gold case list** for that
    function: did the learner cover the boundaries, the empty/single/many classes, the
    duplicate/tie case, the high-end/overflow case? Organized **by class/property**, not a
    flat list of arbitrary values?
  - **"State the contract"** — graded on precondition + postcondition + invariants being
    correct and complete (not the implementation restated).
  - **"State a property"** — rubric-checked for being *true* and *strong*, **then**
    optionally executable-verified: the coach encodes the property as an assertion over a
    handful of inputs and runs it against a correct and a deliberately-wrong impl to
    confirm it accepts the right one and rejects the wrong one.

**Hybrid reporting.** Many B3 drills are hybrid — e.g., "write a test AND say what
property it checks": the test is executable-graded (does it fail-on-buggy / pass-on-fixed?),
the property statement is rubric-graded. Report the two verdicts **separately**: a test
that catches the bug but a hand-wavy account of *what contract* it enforces is a **partial
pass** (it may be luck; `evidence-base.md` → illusions of fluency).

---

## 6. Frontier band

Frontier is not a fixed tier — it tracks the learner's **demonstrated ceiling** and presses
**one step** past their last comfortable success along a single parameter axis
(`drill-generation.md` §5). Escalating two steps collapses to failure; escalating none
loses the desirable-difficulty benefit.

**What "one step" means here** (per `drill-generation.md` §5):
- **Advanced** = one non-trivial specification move in isolation (one property, or finding
  one missed case in a small suite).
- **Frontier-N** = N increments beyond Advanced; each increment adds exactly one new
  interacting demand OR pushes one parameter-space dimension up one notch.
- The learner's current Frontier-N is the highest N they have passed.

Escalation directions beyond Advanced for B3, with step counts:

1. **Strengthen the oracle** (the canonical path):
   - Frontier-1: from one property to a **complete property set** that *together* pins the
     function (for `sort`: ordered **and** same-multiset — neither alone suffices; each is
     too weak on its own). One extra interacting property = one increment.
   - Frontier-2: add a **metamorphic relation** that no single input reveals
     (`sort(xs) == sort(reverse(xs))`; permutation invariance of a sum). +1.
   - Frontier-3: add a **reference-model / oracle** check — test the function against a
     slow, obviously-correct implementation over generated inputs (the property-based
     testing endgame, Claessen & Hughes 2000). +1.

2. **Harder oracle problems** (push the oracle-type dimension): non-deterministic output
   (sets, shuffles, floating-point tolerance); stateful sequences (a stack/cache whose
   correctness is a *sequence* property, not a single call); functions whose only oracle is
   a metamorphic relation. Each is one increment over the mechanism it layers on.

3. **Subtler gaps** (push the bug-class dimension): a suite that is green, high-coverage,
   *and* has a property — but the property is **too weak** to catch the planted bug;
   the learner must find why the property admits the wrong implementation and strengthen
   it. (Directly drills the Inozemtseva & Holmes "coverage ≠ effectiveness" lesson.)

4. **Test-design under realistic constraints**: choosing a *minimal* high-value case set
   from a large space (equivalence partitioning at scale); designing tests for a function
   with an *underspecified* contract (the learner must first *negotiate the contract* —
   "is `lo > hi` an error or clamped?" — then test it).

5. **Interleave with debugging/review → hand off.** Once correctness-specification is
   solid, the natural escalation is using it *in situ*: writing the failing test that
   reproduces a real bug (→ **C1 systematic debugging**) or catching a missed edge case in
   someone else's diff (→ **E3 code review**). Those are different skills and different
   modules; escalate into them rather than stretching B3.

Track the level as `B3: Frontier-N`. Reset condition: two consecutive failures at the same
level → drop to Advanced for one drill, then re-approach (`drill-generation.md` §5).

---

## 7. Mastery rubric

The observable per-tier bars, instantiating the rubric shape of `assessment.md` Part 2.
Two cross-cutting requirements apply at every tier above Foundations: **product *and*
process** (the right cases/test *and* sound contract-and-boundary reasoning — a passing
test with no account of *what contract it enforces* is a Foundations-level pass at best),
and **unaided + durable** (a same-session streak is provisional until a delayed
re-assessment or the real-code transfer task confirms it; `assessment.md` Parts 3–5).

| Tier | Observable bar for B3 |
|---|---|
| **Foundations** | For a function with an obvious contract, **enumerates the core cases** — at least the boundary, the empty/degenerate, and one typical input — **and** can name **which single input** breaks a supplied buggy version (verified by running it). Lists cases *organized*, not purely arbitrary. Allowed *with* the worked example faded to one missing case. Maps to `assessment.md` B3 "handful of cases / happy-path → Foundations." |
| **Working** | On **unseen** functions, **writes a test that catches a planted bug** — *runner-verified* to **fail on the buggy impl and pass on the fixed one** — **and** systematically covers **boundary + empty/single/many** classes **unaided**; can **state the function's contract** (precondition, postcondition) in behavior terms, not implementation terms. Recognizes and rejects a *vacuous* test. Maps to `assessment.md` "systematic boundary + empty/degenerate coverage → Working." |
| **Advanced** | **Property-level reasoning**: states an invariant/postcondition/metamorphic relation that must hold **for all inputs**, and that **rejects a wrong implementation and accepts the right one** (verified by running it against both); **identifies the function's implicit contract**; and **finds the subtle case a naive (even high-coverage) suite misses**, explaining *why* it was missed. Articulates the underlying principle on a teach-it-back — "coverage isn't correctness; a test must be able to fail" — not just the instance. Maps to `assessment.md` "property-level reasoning and identifying the implicit contract → Advanced." |
| **Frontier** | `Frontier-N`: presses one specification move past the last comfortable success per §6 / `drill-generation.md` §5 (one property → a complete property set → a metamorphic relation → a reference-model oracle; or finding why a too-weak property admits the bug). A moving target, not a fixed bar. |

Promotion is by **performance, not tenure** (`assessment.md` rule 1); the coach marks a
tier from what the learner *does* on unseen drills, never from claimed seniority. Held-out
re-assessment and real-code transfer outrank a same-session streak (`assessment.md`
Part 5). **B3-specific honesty note:** a learner who writes passing tests but cannot say
what would make them *fail* has not yet reached Working — green is not the bar; *catching a
wrong implementation* is.

---

## 8. Anti-patterns & evidence caveat

**Anti-patterns this module exists to break** (each is a catalog entry in §5c, surfaced as
a *behavior*):

- **Happy-path testing / confirmation testing.** Feeding the function the inputs you
  already know it handles and reading green as proof. The root behavior. The fix is
  adversarial: partition the input space and attack the **boundaries** and **degenerate
  cases** where defects cluster (Myers). *A test that can't fail proves nothing*
  (Dijkstra).
- **Asserting on implementation, not behavior.** Pinning private internals, call order, or
  an incidental representation, so tests break on a behavior-preserving refactor and still
  miss real bugs. The fix is to test the **contract** — the promise to the caller — not the
  *how*.
- **Missing the empty / single / duplicate / overflow case.** Treating "a collection" as
  one equivalence class instead of `{empty, one, many, all-equal, huge}`. The empty case is
  the most-missed boundary and the most common crash; the high-end/overflow boundary is the
  second.
- **Confusing "passes my test" with "correct."** The meta-error. Coverage is not
  correctness — once test count is controlled, coverage correlates only weakly with fault
  detection (Inozemtseva & Holmes 2014); a covered line can be asserted on by nothing. Green
  is the *absence of a caught bug*, never proof of its absence (Dijkstra).
- **One-oracle tunnel vision.** Only knowing exact-equality assertions, so non-deterministic
  or unknown-output functions become "untestable." The fix is properties, invariants, and
  metamorphic relations (Hughes; Segura; Barr et al.).

**Evidence caveat (this matters here — `[Canon + some empirical]`, mostly canon).** Unlike
A1's pure-`[Verified]` footing, **most of B3 is practitioner canon, not verified science**,
and the coach must say so:

- **The test-design techniques** (edge/boundary cases, equivalence partitioning, properties,
  metamorphic relations) are **craft that works in practice** — Myers, Dijkstra, Hughes,
  Barr et al. — **not** replicated empirical findings. Present them as "respected practice,"
  never "research shows." They are grounded in `evidence-base.md` → Module-specific & craft
  sources (block **B3a**) as `[Practitioner-canon]` (with the oracle/metamorphic survey sources
  as peer-reviewed *surveys*, not effectiveness experiments).
- **The TDD evidence is genuinely mixed** and must not be inflated into "TDD works." The
  strongest synthesis (Rafique & Mišić 2013) finds only a **small quality effect** and a
  **null-to-negative productivity effect**, both confounded by test-effort differences; the
  narrative review (Turhan et al. 2010) finds the quality benefit **largely evaporates under
  the most rigorous studies**; and Fucci et al. (2017) find the **test-first ordering that
  defines TDD is not the active ingredient** — disciplined, fine-grained steps are. The
  honest line: *specify behavior and work in small steady steps; the test-first ceremony is
  not what the evidence credits.*
- **The transfer caveat** (`evidence-base.md`) applies doubly: even the empirical layer is
  mostly student/academic and small-N; whether explicitly drilling correctness-specification
  *causally* improves *experienced* engineers is open. The coach leans on the transfer task
  (§9) — the skill working on the learner's *own* code — as the honest individual-level
  evidence. This module makes **no `[Verified]` claims**; its claims are `[Practitioner-canon]`
  with a clearly-bounded `[Some empirical — mixed]` TDD layer.

---

## 9. Transfer task

**The only honest test of whether the gym drill transferred to the job is applying it to
the learner's own real code** (`assessment.md` Part 4; `evidence-base.md` → transfer
caveat, consequence 2).

> **Your turn:** Find a function in **your own codebase** that you *trust* — one you wrote,
> that "works," ideally one with tests already. Pick the smallest such function with a
> non-trivial contract (it takes a collection, a range, a number that could be zero or
> negative, or an input that could be empty).
>
> Now **be the adversary.** First, **state its contract** out loud — precondition,
> postcondition, invariants — without looking at the implementation. Then **enumerate the
> cases your existing tests *don't* cover**: the empty input, the single element, the
> duplicate, the boundary value, the just-over-the-limit, the all-equal collection. For
> **at least one** uncovered case, predict what *should* happen from the contract, then
> **run the function on it** and see if it actually does. Finally, ask: **is there a
> property** — something that must hold for *every* input — that would have caught more
> than any single case? Did you find a real gap, or even a real bug?

**Grading is softer and named as such** (`assessment.md` Part 4). Real code has no clean
answer key; the coach grades against the §7 rubric and says: *"this is a judgment call on
your real code, not a machine-verifiable result."* Where the learner's function (or a
reduced version) **is runnable**, the coach still uses the runner for any executable
sub-claim — reduce the function and the suspect input to a minimal snippet and confirm the
behavior via `runner.py` before discussing it; if the learner writes a new test for the
gap, verify it **fails on the current code if the code is actually wrong**, or **passes and
documents the contract if the code is right**. **Transfer evidence is weighted heavily:** a
learner who aces generated drills but cannot find a single uncovered case (or cannot state
the contract) for a function in their own codebase has not yet transferred the skill — the
tracker notes that gap as more diagnostic than another passed synthetic drill.

---

## Cross-references

- Drill mechanics, exercise formats, executable ground-truth protocol (run the learner's
  test against impls), rubric + exemplars path, Frontier escalation:
  `references/drill-generation.md` (this module instantiates §1 and follows §2, §3, §4, §5).
- Session delivery (pause/no-spoiler hard stop, tier-faded worked example, direct feedback,
  scaffolding ladder): `references/coaching-loop.md`.
- Entry task (the B3 "what would you test? enumerate the cases — and for each, what
  property/behavior does it check?" task), per-skill routing, mastery-rubric shape,
  held-out re-assessment, transfer weighting: `references/assessment.md` (B3 entry task and
  rubric: happy-path → Foundations; systematic boundary/empty → Working; property-level +
  implicit contract → Advanced).
- Evidence grounding — the **canon** layer (Myers 1979; Dijkstra EWD249/1972; Barr et al.
  2015 oracle problem; Claessen & Hughes 2000 + Hughes 2019 properties; Chen et al. 1998 /
  Segura et al. 2016 metamorphic testing) and the **mixed-empirical** TDD layer (Rafique &
  Mišić 2013; Turhan et al. 2010; Fucci et al. 2016/2017; Inozemtseva & Holmes 2014):
  `references/evidence-base.md` → Module-specific & craft sources (these B3-specific citations
  are now in the evidence base, badged honestly as block **B3a** `[Practitioner-canon]` vs.
  block **B3b** `[Some empirical] — MIXED`). AI-era B3 priority ("AI code carries defects" → precise
  specification + verification as a durable skill): `evidence-base.md` → AI-era impact.
- Golden exemplars (~3 per tier, runner-verified where executable): `exemplars/B3/foundations.md`,
  `exemplars/B3/working.md`, `exemplars/B3/advanced.md`.
