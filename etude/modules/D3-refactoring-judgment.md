# D3 — Refactoring Judgment `[Practitioner-canon]`

> **Module type.** `[Practitioner-canon]` (the prescriptions) **with a strong EXECUTABLE
> anchor** (the definition). This is a **judgment module** about *when* and *whether* to
> refactor — but it is bolted to the one part of refactoring that is **not** a matter of
> opinion: **behavior preservation**. A refactor, by Fowler's definition, changes internal
> structure *without changing observable behavior*. So "did behavior change?" is a
> **computation**: run the same inputs through the code BEFORE and AFTER and compare
> `stdout`/`status` — identical means behavior was preserved, the literal definition. The
> coach **runs** this and grades it like an A1 drill. The *judgment* half — should you
> refactor here? is this the right move? are you under a green test first? when should you
> **not**? — is rubric + exemplars, and is named as softer.
>
> **Core idea.** Refactoring is a **behavior-preserving** change that improves internal
> structure, made in **small steps under a green test**, with the test re-run after each
> step. The skill is two things at once: (1) **never silently change behavior** while
> claiming to "clean up" — a "refactor" that changes output is a **bug**, however clean it
> looks; and (2) **judge well** — refactor the code you are about to touch, follow the Rule
> of Three, never wear the refactoring hat and the new-feature hat at the same time, and
> *don't* refactor untested code until you have pinned its behavior with a characterization
> test first.

---

## 1. Evidence basis `[Practitioner-canon]` (with an executable definition-anchor)

This module is **practitioner canon** — respected, widely-taught craft from two landmark
books — **plus** one genuinely non-negotiable piece that the runner enforces directly. The
coach must keep these apart and must never present the craft prescriptions as empirical
findings (`evidence-base.md` → badge rules).

**(a) The executable anchor — behavior preservation is a *definition*, not a finding.**
Refactoring's defining property is that observable behavior does not change. Fowler's own
definitions (verbatim, from martinfowler.com → *DefinitionOfRefactoring*; mirrored in
*Refactoring*, 2nd ed., 2018, ch. 2):

> **Refactoring** *(noun)*: "a change made to the internal structure of software to make it
> easier to understand and cheaper to modify **without changing its observable behavior**."
>
> **Refactoring** *(verb)*: "to restructure software by applying a series of refactorings
> **without changing its observable behavior**."

Because "observable behavior" is exactly what a program *prints and returns*, the coach can
**verify** it: run a fixed battery of inputs through the BEFORE code and the AFTER code and
compare. Identical `stdout` and `status` ⇒ behavior preserved (for the inputs tested). A
divergence ⇒ behavior changed ⇒ **by definition not a refactor** — it is a behavior change
masquerading as one, i.e. a bug. This is the same executable-ground-truth discipline as A1
(`drill-generation.md` §2), and it is what makes "is this a refactor?" decidable rather than
a matter of taste. **Honest scope:** the runner proves preservation **only for the inputs
you run** — it is a *falsifier* (one differing input disproves "refactor"), not a *proof of
total equivalence* (see §8). That caveat is the analogue of Dijkstra's point that testing shows
the presence of bugs, not their absence (`evidence-base.md` → B3a, where the verbatim aphorism lives).

**(b) The craft half — the discipline and the judgment `[Practitioner-canon]`.** Vetted
during authoring against the named primary sources; respected, widely-taught **craft
wisdom**, not measured causation:

- **Fowler, *Refactoring* (2nd ed., 2018)** — the reading spine's D3 anchor
  (`evidence-base.md` → reading spine). Source of: the **definition** above; the discipline
  of **small steps under tests** — make a tiny change, **run the tests**, and if they go red
  you know the last small step did it (Fowler's recurring point in ch. 1: small steps make a
  mistake cheap to find — paraphrased, not a pinned quote); the **Two Hats** metaphor — when you code you are
  either *adding function* (new behavior + its tests; existing code untouched) **or**
  *refactoring* (restructuring; **adding no new behavior, not even new tests**) — and you
  **swap hats consciously, never wear both at once**; and the **Rule of Three** (Fowler,
  ch. 2, attributed to **Don Roberts**) — in its standard published form: *the first time you
  do something you just do it; the second time you wince at the duplication but do it anyway;
  the third time, you refactor.* Don't abstract on the *first* whiff of duplication — wait
  until the third (two look-alikes are often coincidental; the wrong abstraction is harder to
  undo than the duplication).
- **Kent Beck — "make the change easy, then make the easy change"** (verbatim, from Beck's
  own post, 25 Sep 2012): *"for each desired change, make the change easy (warning: this may
  be hard), then make the easy change."* This is **preparatory refactoring**: when a feature
  is awkward to add, first refactor (behavior-preserving) so the new shape *fits*, then add
  the feature. It is the operational form of "refactor the code you are about to touch."
- **Feathers, *Working Effectively with Legacy Code* (2004)** — the staff anchor
  (`evidence-base.md` → reading spine; itemized in the proposed D3 craft-source block). Source
  of: **"legacy code is code without tests"** (the provocative operational definition — *old*
  isn't the problem; *untested* is, because you cannot change it safely); and the
  **characterization test** — "a test that characterizes the actual behavior of a piece of
  code." When code has no tests, you do **not** start by cleaning it up: you first **pin its
  current behavior** (even its weird behavior) with characterization tests, *then* refactor
  under that green net. This is the discipline that makes the **"no tests yet → write the
  test first"** judgment concrete, and the **seam**/dependency-breaking techniques are how you
  get untestable code into a test harness in the first place.

**Why these license this module.** The *definition* (a) licenses the executable check the
runner performs. The *craft* (b) licenses the judgment the module drills — **when** to
refactor (Rule of Three; preparatory refactoring; refactor the code you're about to touch),
**how** (two hats; small steps under a green test), and **when not** (no tests → characterize
first; deadline-critical throwaway; gold-plating). The combined skill: **preserve behavior
provably, and exercise good judgment about when the restructuring is worth doing at all.**

**Read through the honesty caveat — this is the load-bearing one for D3.** Refactoring is
**respected craft, not a verified intervention.** Its *causal* effect on defect rate and
long-term maintainability has only **mixed and limited empirical support** — the studies
genuinely **contradict** each other (some report fewer defects after refactoring, others
report *more* bug reports following heavy refactoring, and at least one large study found **no
clear effect** on maintainability/modifiability; `evidence-base.md` → proposed D3 craft-source
note). So the coach must **never** say "refactoring reduces bugs" or "improves
maintainability" as if proven. The one part that *feels* verified — behavior preservation — is
a **definition enforced by the runner**, not an empirical finding about outcomes. And the
**curriculum-wide transfer caveat** (`evidence-base.md`) applies in full: that drilling
refactoring judgment on synthetic snippets *causally* improves a given engineer's real-world
restructuring is the open question every module here carries; the transfer task (§9) is the
honest individual-level test.

---

## 2. Soft prerequisites

**B3 (testing & specifying correctness) recommended.** Refactoring's whole safety story is
"small steps **under a green test**." B3 is the skill of writing the test that makes the step
safe — the characterization test that pins legacy behavior (Feathers), and the boundary/edge
cases that catch a behavior change the happy path hides. A learner who refactors with no test
is doing the thing this module most warns against; the gap traces to B3.

**D1 (deep modules / `[Practitioner-canon]`, Ousterhout) recommended.** D1 supplies the
*target* — what "improves internal structure" *means* (deeper modules, narrower interfaces,
less complexity). D3 supplies the *safe motion* toward that target. You refactor *toward* a D1
design; you judge a candidate refactor by whether it makes the module deeper, not merely
different. The two are companion skills: D1 is the destination, D3 is the disciplined way to
get there without breaking anything en route.

**A1 (notional machine) helps.** Several behavior-preservation traps in this module are A1
execution-model events seen inside a "cleanup": a shared mutable default created once at
definition time (the config-hoist trap, §6 / Advanced A2), short-circuit evaluation lost when
a condition is "extracted for clarity" (Working W3), aliasing the caller's object. If a
learner cannot see *why* the refactor changed behavior, the gap is often A1.

Per `assessment.md`, soft prerequisites **inform, never gate** — the buffet rule holds (any
learner may open any module at any tier). If a learner flails at D3 because they can't tell a
behavior change from a refactor, the coach notes the gap likely traces to A1/B3 and *suggests*
shoring those up — but does not forbid D3.

---

## 3. The mental model

**A refactor is a change that improves internal structure while keeping observable behavior
exactly the same — verified by running the same inputs before and after — and the discipline
is to do it in small steps under a green test, one hat at a time.** Two halves, and you need
both: a **provable invariant** (behavior unchanged) and a **judgment** (is this restructuring
worth doing, here, now?).

| Component | What it is | What goes wrong without it |
|---|---|---|
| **The invariant: behavior preserved** | Observable behavior — what the code prints/returns/raises for given inputs — is **identical** before and after. This is the *definition*. Verify it: run a fixed input battery through both versions and diff `stdout`/`status`. | You call a behavior **change** a "refactor." The output silently differs on some input; the diff ships as a bug under a safe-sounding name. (`<= 500` where it was `< 500`; a dropped short-circuit; a shared mutable default.) |
| **The motion: small steps under a green test** | Make one tiny structural change, **run the tests**, see green, commit; repeat. The test net is what makes the small step safe and the mistake **cheap to find** — if the test goes red, the *last small step* caused it. | A big-bang rewrite with no green checkpoint. When behavior breaks you can't localize *which* change did it, and you can't tell a refactor from a feature change because both happened at once. |
| **The two hats** | At any moment you are **either** adding behavior (new feature + its tests) **or** refactoring (restructuring; **no new behavior**). You **swap hats deliberately and never wear both at once**. | You "refactor while you're in there" and slip a behavior change in alongside the cleanup. Now the diff is unreviewable — reviewer can't separate "moved code" from "changed what it does." |
| **The judgment: when, and whether** | Refactor the code you are **about to touch** ("make the change easy, then make the easy change"); abstract on the **third** duplication (Rule of Three), not the first; and when there are **no tests**, write a **characterization test first**. Sometimes the right call is **don't** (throwaway code on a deadline; gold-plating). | You refactor for its own sake (gold-plating), abstract too early on a coincidental duplication (the wrong abstraction is worse than duplication), or restructure untested legacy with nothing pinning its behavior — and silently change a quirk a caller depended on. |

**The discipline in one line: *change the structure, never the behavior — in small steps,
under a green test, with one hat on.*** Three corollaries the module drills:

1. **Behavior preservation is decidable — so decide it by running, not by eyeballing.** "It
   looks equivalent" is exactly the trap. `not (a and b)` "simplified" to `not a and not b` is
   *wrong*; `(a*b)//c` "factored" to `a*(b//c)` is *wrong* for integers; both read fine. The
   only way to know is to run the inputs through both and compare. A clean-looking diff that
   changes one input's output is **not a refactor**.
2. **No tests? Characterize first; don't "fix" the quirk.** Untested code is legacy code
   (Feathers). Before you touch it, pin its *current* behavior — including its odd corners —
   with a characterization test. The quirk may be load-bearing. Refactoring is not a license
   to change behavior you happen to dislike; that's a separate, behavior-changing edit that
   needs its own justification and its own tests.
3. **Refactor with purpose, on a clock you can justify.** Refactor the code you're **about to
   change**, to make that change easy (Beck) — not the whole codebase on a whim. Wait for the
   **third** duplication before abstracting (Rule of Three). And know when **not** to: a
   throwaway spike under a hard deadline, or polishing code no change is coming to, is
   gold-plating. *Better*, not *perfect*; and only where a change is actually landing.

---

## 4. Worked example — a refactor, verified behavior-preserving (and a fake one caught)

*(Foundations depth: the full refactor shown — the structural improvement, the input battery,
and the runner-verified BEFORE/AFTER comparison. Then a "refactor" that looks just as clean but
silently changes behavior — caught by the same check. This fades by tier; see the note after.)*

The skill is to **restructure like a disciplined engineer**: improve the shape, then **prove**
behavior didn't change by running a fixed battery through both versions. Consider this shipping
cost function — deeply nested, with an early-return special case:

```python
# BEFORE
def shipping_cost(weight_kg, distance_km, express):
    if weight_kg <= 0:
        return 0.0
    else:
        if distance_km < 100:
            base = 5.0
        else:
            if distance_km < 500:
                base = 10.0
            else:
                base = 20.0
        cost = base + weight_kg * 0.5
        if express:
            cost = cost * 1.5
        return round(cost, 2)
```

**Step 1 — Put the refactoring hat on (no new behavior).** The structural smells: a nested
`if/else` ladder for `base`, and an `else` wrapping the whole body after an early-return case.
Two behavior-preserving moves: **guard clause** for the `weight_kg <= 0` case (drop the big
`else`), and **extract** the `base` selection into a small helper, flattened to a `return`
chain.

```python
# AFTER (genuine refactor — structure improved, behavior intended unchanged)
def _base_rate(distance_km):
    if distance_km < 100:
        return 5.0
    if distance_km < 500:
        return 10.0
    return 20.0

def shipping_cost(weight_kg, distance_km, express):
    if weight_kg <= 0:
        return 0.0
    cost = _base_rate(distance_km) + weight_kg * 0.5
    if express:
        cost *= 1.5
    return round(cost, 2)
```

**Step 2 — Prove behavior is preserved.** Pick an input battery that **hits every branch and
every boundary** (this is the B3 skill in service of D3): the special case, the two distance
boundaries (`100`, `500`) from *both* sides, express on/off. Run the *same* battery through
BEFORE and AFTER and diff.

**Verified ground truth** (executable-ground-truth discipline, `drill-generation.md` §2 — the
coach *runs* both, never guesses, and surfaces the run; `coaching-loop.md` → Surface ground
truth):

```
inputs: (0,50,F) (-2,600,T) (3,50,F) (3,50,T) (3,250,F) (3,250,T)
        (10,800,F) (10,800,T) (1,99,F) (1,100,F) (1,499,F) (1,500,F)

BEFORE stdout:
(0, 50, False) -> 0.0          (3, 250, False) -> 11.5        (1, 99, False) -> 5.5
(-2, 600, True) -> 0.0         (3, 250, True) -> 17.25        (1, 100, False) -> 10.5
(3, 50, False) -> 6.5          (10, 800, False) -> 25.0       (1, 499, False) -> 10.5
(3, 50, True) -> 9.75          (10, 800, True) -> 37.5        (1, 500, False) -> 20.5

AFTER stdout:  (identical, line for line)
(1, 500, False) -> 20.5   ...  (1, 100, False) -> 10.5   ...  (3, 50, True) -> 9.75   ...

stdout identical: True     status identical: True (both ok)
VERDICT: behavior preserved  ✓  → this IS a refactor (for the inputs tested)
```

The output is **byte-for-byte identical** across all twelve inputs. The structure is better
(no nesting ladder, no wrapping `else`, the rate table isolated and independently testable) and
behavior is provably unchanged for the battery. That is a refactor.

**Step 3 — Now watch a fake one get caught.** Here is a "refactor" that looks *just as clean* —
same flatten/extract — but one boundary slipped from `< 500` to `<= 500`:

```python
def _base_rate(distance_km):
    if distance_km < 100:
        return 5.0
    if distance_km <= 500:          # <-- silently changed from `< 500`
        return 10.0
    return 20.0
# (shipping_cost body identical to the genuine AFTER)
```

Same input battery, diffed against BEFORE:

```
BEFORE: (1, 500, False) -> 20.5
FAKE  : (1, 500, False) -> 10.5     <-- DIFFERS
stdout identical: False
VERDICT: BEHAVIOR CHANGED  ✗  → this is NOT a refactor; it is a bug wearing a refactor's clothes
```

The input `distance_km == 500` now takes the `10.0` rate instead of `20.0` — output drops from
`20.5` to `10.5`. **Nothing in the structure looks wrong.** The only way anyone catches this is
by running the boundary input through both versions. That is the entire point of the executable
check: *clean ≠ behavior-preserving*, and the runner is the arbiter.

**What the example makes visible** (and a structure-only review hides): a refactor has **two**
obligations, and they are graded **separately**. The *structure* improved (a rubric judgment).
The *behavior* did or did not change (an executable fact). A beautiful restructuring that flips
one boundary **fails outright** on the executable axis — it does not matter how clean it looks.
And the boundary inputs (`100`, `500` from both sides) are not decoration: they are exactly
where a "looks equivalent" change hides, which is why the battery must include them.

> **Expertise reversal — the example fades by tier.** Per the worked-examples finding
> (`evidence-base.md` → instructional pillar; `coaching-loop.md` Step 2), a fully worked
> refactor-plus-proof helps **novices** (it shows the motion and the check) but is **redundant
> load for the more advanced**, who learn more by doing the restructuring and designing the
> battery themselves. So the coach fades it:
>
> | Tier | Worked-example depth at D3 |
> |---|---|
> | **Foundations** | **Full** — the complete BEFORE/AFTER, the input battery, and the runner-verified identical-output proof above, every step shown. |
> | **Working** | **Partial** — coach shows the BEFORE and the proposed AFTER but leaves the learner to **name the inputs that would prove (or break) preservation** and predict the diff; coach then runs it. |
> | **Advanced** | **Skeleton** — coach hands over only the BEFORE (often untested/legacy) and the goal; the learner writes the characterization battery, performs the refactor, and proves preservation unaided. |
> | **Frontier** | **None** — straight to the design/diff (§6). |

---

## 5. Drill-generation spec

Instantiates the generation-spec format of `drill-generation.md` §1 for D3. Grading mode is
declared up front: **hybrid** (§5d) — the **behavior-preservation** sub-claim is
**executable** (run BEFORE vs AFTER, diff `stdout`/`status`); the **judgment** sub-claims
(should you refactor here? right move? under test first? when not?) are **rubric + golden
exemplars**. Report the two verdicts **separately**.

### 5a. Tier definitions (D3-specific)

The curriculum-wide tier names (`drill-generation.md` §1a) translated to this module. **Most
drills present a BEFORE snippet and either a candidate AFTER to judge, or a goal to refactor
toward**; the behavior question is always settled by **running both** against a fixed battery.

| Tier | D3 criterion | Example shape |
|---|---|---|
| **Foundations** | One **clear, behavior-preserving** move on a familiar surface — extract a duplicated sub-expression into a variable, replace a magic number with a named constant, turn an index loop into a comprehension. **Perform the move (or confirm the given AFTER is behavior-preserving) and say what structural smell it fixes.** No behavior-changing trap. | Extract `qty*unit` into `subtotal`; predict the (unchanged) output and name the smell (duplicated expression). |
| **Working** | A candidate "refactor" that **may or may not** preserve behavior, on a surface where intent and execution diverge — a boolean "simplification" (De Morgan), a guard-clause flatten, an "extract for clarity" that drops short-circuit. **Decide: refactor or behavior change? Name the inputs that decide it. If it changed behavior, where and why.** | `if not (a and b)` "simplified" to `not a and not b` — decide; the inputs `(T,F)`/`(F,T)` expose it. |
| **Advanced** | **Untested legacy** with a quirk, or a refactor whose behavior change **survives shallow testing** (passes on obvious inputs, fails on interior/edge ones), combining ≥2 mechanisms (e.g. aliasing + cross-call state; integer-division re-association). **Write the characterization battery FIRST, then refactor and prove preservation — or catch the planted behavior change. Articulate the judgment** (characterize before changing; the quirk may be load-bearing). | A CSV parser that drops empty fields; "clean it up" silently keeps them — pin the drop-empties behavior first. |
| **Frontier** | See §6 — one step past the learner's last comfortable success. | — |

A drill is mis-tiered if a Foundations drill hides a behavior-changing trap (that's Working+),
or a Working drill's behavior change is obvious on the first input the learner would try (too
easy), or an Advanced drill needs no characterization step and combines only one mechanism.
Apply the self-check (`drill-generation.md` §4) and re-level before posing.

### 5b. Parameter space (axes the coach varies to avoid mode-collapse)

Pick a *different point on each axis* across successive drills (`drill-generation.md` §1b, §4
check 3). The axes for D3:

- **Refactoring move** — extract variable/method · inline · guard clause / flatten nesting ·
  replace magic literal with constant · loop → comprehension/`sum` · consolidate duplicate
  conditional · replace temp with query · split/rename for clarity · hoist a constant ·
  introduce a parameter object. (The *named catalog* lives in Fowler; the coach varies which
  move is exercised, it does not drill the catalog as the deep structure.)
- **Preservation status** (the executable axis) — **genuinely behavior-preserving** · **silent
  behavior change** (the trap). Vary which: a Working/Advanced drill is *much* stronger when the
  learner cannot assume the AFTER is safe.
- **Behavior-change class** (when there *is* a trap) — boundary slip (`<`↔`<=`, off-by-one) ·
  boolean mis-simplification (De Morgan, swapped `and`/`or`) · lost short-circuit / changed
  side-effect count · integer-vs-float / re-association · aliasing or shared-mutable-default
  introduced · changed iteration order / sort stability · early-return reordered.
- **Test status** (the judgment axis) — already under a green test · **no tests (legacy →
  characterize first)** · a test exists but is too weak to catch the planted change (the
  "green but inadequate" case).
- **What the drill must produce** — *perform the move + name the smell* (Foundations) ·
  *classify refactor-vs-behavior-change + name the deciding inputs* (Working) · *characterize
  first, then refactor and prove preservation, or catch the hidden change + articulate the
  judgment* (Advanced) · *teach-back the discipline* (Advanced/Frontier).
- **The "when/whether" judgment stressed** — is this the right move toward a deeper design
  (ties D1)? · is the Rule of Three satisfied or is this premature abstraction? · is this
  *preparatory* (about-to-touch) or gold-plating? · two-hats violation (behavior + refactor in
  one diff)? Vary which judgment the drill foregrounds.
- **Format** (`drill-generation.md` §6) — primarily **Debug-this** (here is a candidate
  refactor; is it one?) and **Generation → Comparison** (refactor this; coach reveals the gold +
  runs preservation); also **Error analysis** (here is a "refactor" someone shipped — what did it
  change?) and **Teach-it-back** (articulate why behavior preservation is a definition, not a
  feeling).

Keep an in-session log of the `(move, preservation status, behavior-change class, test status,
format)` tuples used; do not repeat a tuple until the others are exercised.

### 5c. Common-error catalog

The *specific* refactoring failures, each with the conceptual gap it diagnoses
(`drill-generation.md` §1c format). These are grounded in the named craft sources (Fowler;
Feathers; Beck) and in the recurring A1 execution-model events that make "looks equivalent"
false, not in trivia. **The root of most of them is one inversion: trusting that a
clean-looking structural change *must* preserve behavior — judging the refactor by how it
*reads* instead of by what it *does* when you run it.** The secondary root is treating
refactoring as a license to change behavior you happen to dislike (skipping the characterization
step).

```
Error: Calls a behavior-changing edit a "refactor" because the structure looks cleaner —
       ships a diff where some input's output silently differs, under a safe-sounding name.
Diagnoses: Judges preservation by reading, not running. Has not internalized that "refactor"
           is DEFINED by unchanged observable behavior, which is decidable by execution.
           (Fowler's definition; the executable anchor, §1a.) THE root D3 error.
Example trigger: any Working/Advanced drill with a planted boundary slip, De Morgan
                 mis-simplification, or dropped short-circuit (W2, W3, the worked-example fake).

Error: Refactors untested legacy code by "cleaning it up" first — changes a quirk before any
       test pins the current behavior.
Diagnoses: Skipped the characterization test. Untested code is legacy code; you cannot refactor
           safely without first pinning behavior, and the quirk may be load-bearing for a
           caller. (Feathers: "legacy code is code without tests"; characterization tests.)
Example trigger: the CSV-parser drill (drops empty fields) where the learner "fixes" the drop
                 before writing a test that pins it.

Error: "Tests pass, so it's a refactor" — relies on an existing test suite that is too weak to
       exercise the changed path, and concludes behavior is preserved.
Diagnoses: Mistakes a green (but inadequate) suite for proof of equivalence. Preservation holds
           only for inputs actually run; the boundary/edge case that the change breaks isn't in
           the suite. (Dijkstra: testing shows presence, not absence of bugs; B3 coverage≠
           correctness.) The honest limit of the executable check (§1a, §8).
Example trigger: an Advanced drill whose planted change passes the obvious inputs and fails an
                 interior one (the integer re-association A3: passes (100,1,1), fails (10,3,2)).

Error: Wears both hats at once — bundles a behavior change in with the restructuring in a single
       diff ("while I was refactoring I also fixed/added...").
Diagnoses: Two-hats violation. The diff is now unreviewable: nobody can separate "moved code"
           from "changed what it does," and the behavior change rides in unscrutinized.
           (Fowler, the Two Hats.)
Example trigger: a learner who, asked to extract a method, also "tidies" a condition and changes
                 an edge case in the same step.

Error: Abstracts on the first or second duplication — extracts a shared helper the moment two
       pieces of code look alike.
Diagnoses: Premature abstraction; ignores the Rule of Three. Two look-alikes are often
           coincidental duplication; the wrong abstraction is harder to undo than the
           duplication. (Fowler/Roberts, Rule of Three.)
Example trigger: a drill with two superficially-similar blocks that diverge on the next
                 requirement — extracting now couples two things that should stay separate.

Error: Refactors code no change is coming to / polishes for its own sake — gold-plating, or a
       codebase-wide "cleanup" with no feature behind it.
Diagnoses: Refactoring without purpose. Refactor the code you are ABOUT TO TOUCH ("make the
           change easy, then make the easy change"); restructuring untouched, working code on a
           deadline is cost with no payoff. (Beck, preparatory refactoring; the "when not to.")
Example trigger: a learner who, on a deadline-critical throwaway script, proposes a full
                 architecture refactor instead of shipping.

Error: Big-bang refactor — restructures a large chunk in one leap, no intermediate green
       checkpoint, then can't tell what broke.
Diagnoses: Abandoned small-steps-under-test. The value of small steps is localization: if the
           test goes red, the LAST small step did it. One giant step destroys that. (Fowler,
           small steps; "find the bug quickly.")
Example trigger: an Advanced drill where the learner rewrites the whole function at once and a
                 behavior change appears with no way to bisect which sub-change caused it.

Error: Confuses "improved structure" with "behavior-preserving" — assumes that because the new
       version is genuinely cleaner/deeper, it must also be a refactor.
Diagnoses: Conflates the two SEPARATE obligations (better structure = rubric; same behavior =
           executable). A change can improve design AND change behavior; then it is a redesign,
           not a refactor, and needs behavior justification + tests. (§5d report-separately.)
Example trigger: any drill where the AFTER is both cleaner and subtly behavior-changing — the
                 learner credits the cleanliness and misses the change.
```

### 5d. Grading mode

**Hybrid** (`drill-generation.md` §1d, §3) — a genuinely strong executable half plus a
judgment half, graded and reported **separately**. The coach grades a D3 attempt like this:

1. **Settle behavior preservation by running (the executable sub-claim).** Write BOTH versions
   to unique snippet files, append the **same fixed input battery** (chosen to hit branches and
   boundaries), run each via `python <skill-dir>/runtime/python/runner.py snippet.py`
   (`drill-generation.md` §2), and **diff `stdout` and `status`**. Identical ⇒ behavior
   preserved *for the battery*; any divergence ⇒ behavior changed ⇒ **not a refactor**. **Paste
   the BEFORE output, the AFTER output, and the verdict into the reply** (`coaching-loop.md` →
   Surface ground truth) — never leave it in a collapsed tool call; an unseen run reads as a
   guessed key. If the learner *disputes* whether behavior changed, the coach **runs the
   deciding input** and shows the two outputs side by side. This sub-claim is graded **like
   A1** — pass/fail on the executable fact. **A "refactor" that changes the battery's output
   FAILS the executable check outright, regardless of how clean it looks.**
2. **Score the judgment against the D3 rubric (§7), criterion by criterion** — *was this the
   right move toward a better/deeper structure (ties D1)? was a green test (or a characterization
   test) in place first? did they keep one hat on? is the timing right (about-to-touch / Rule of
   Three satisfied / not gold-plating)?* Each is a 3-point criterion (§7), graded explicitly.
3. **Cite the closest golden exemplar.** Compare to the tier's golds in
   `exemplars/D3/<tier>.md` — "your move is close to the **fake-refactor** exemplar: clean, but
   it changed the boundary output" vs. "close to the **gold**: structure improved, battery
   identical, characterization test written first." The golds are the calibration anchor.
4. **Name the judgment half as soft.** The coach says out loud: "**behavior preservation I
   verified by running it; whether this was the right refactor to make, and your test-first
   discipline, is a judgment call graded against the module's rubric + exemplars, not a
   machine-verifiable answer**" (`drill-generation.md` §3; `assessment.md` §1.2).

**Report the verdicts separately.** A learner who **preserves behavior** (executable: pass) but
**refactored untested code without characterizing first**, or **bundled a behavior change in a
later step**, or **abstracted prematurely** (rubric: poor judgment) is a **partial pass**, and
the coach flags exactly which. Conversely, a learner with **excellent judgment** whose diff
**changed the output** (executable: fail) has not refactored at all — the executable failure
dominates, because behavior preservation is the *definition*, not a nice-to-have. The two
axes are independent and both are reported.

---

## 6. Frontier band

Frontier is not a fixed tier — it tracks the learner's **demonstrated ceiling** and presses
**one step** past their last comfortable success along a single parameter axis
(`drill-generation.md` §5). Escalating two steps collapses to failure; escalating none loses
the desirable-difficulty benefit.

**What "one step" means here** (per `drill-generation.md` §5):
- **Advanced** = untested legacy with a quirk (characterize first, then refactor and prove
  preservation), or a behavior change that survives shallow testing — one such, ≥2 mechanisms.
- **Frontier-N** = N increments beyond Advanced; each increment adds exactly one new dimension
  of difficulty OR pushes one parameter-space dimension up one notch.
- The learner's current Frontier-N is the highest N they have passed.

Escalation directions beyond Advanced for D3, with step counts:

1. **Subtler / better-camouflaged behavior change** (push the behavior-change axis): from a
   boundary slip → to a change that only manifests on a **specific data shape** (empty / single
   / duplicate / very large) the obvious battery omits (Frontier-1) → to one that manifests only
   under a **specific call sequence** (cross-call shared state; the second call leaks state
   from the first) (Frontier-2) → to a change in a **non-`stdout` observable** the learner must
   think to instrument (mutation of a caller's argument; an exception type that changed)
   (Frontier-3). Each is one increment, and each raises the bar on *what battery proves
   preservation*.

2. **Weaker safety net** (push the test-status axis): from "a green suite exists" → to "**no
   tests**, write the characterization battery yourself" (Frontier-1) → to "a **green-but-
   inadequate** suite exists and you must notice it doesn't cover the changed path before
   trusting it" (Frontier-2). Recognizing that a passing suite is *insufficient* is one
   increment over writing one from scratch.

3. **Bigger surface / harder judgment** (push the move and when/whether axes): from a single
   function → to a **multi-function** refactor where the right move is a sequence of small steps
   (and the learner must keep each step green) → to a case where the *right* judgment is
   **"don't refactor this now"** (throwaway under deadline; coincidental duplication that fails
   the Rule of Three) and the learner must **resist** an inviting-but-wrong refactor. Choosing
   *not* to refactor, correctly, is a Frontier-level judgment.

4. **Refactoring AI-generated code → the AI-era frontier.** A diff where an **agent "refactored"
   a function** and it reads fluent and idiomatic — but silently changed an edge case (the
   spec-§12 verification load). The learner must **not** trust the fluency: write the
   characterization battery, run BEFORE vs AFTER, and catch the behavior change the confident
   prose hides. One increment for "AI-plausible surface," another for "and you must verify, not
   rubber-stamp, that it preserved behavior." (Ties to F1 calibration — over-trusting fluent
   output is the documented AI-era miss — and to E3 — reviewing AI code.)

Track the level as `D3: Frontier-N`. Reset condition: two consecutive failures at the same level
→ drop to Advanced for one drill, then re-approach (`drill-generation.md` §5).

---

## 7. Mastery rubric

The observable per-tier bars, instantiating the rubric shape of `assessment.md` Part 2, scored
against the two D3 axes (executable + judgment). Two cross-cutting requirements apply at every
tier above Foundations: **product *and* process** (behavior preserved *and* sound judgment about
whether/how — a behavior-preserving change made with bad judgment, or excellent judgment that
changed behavior, is not a clean pass), and **unaided + durable** (a same-session streak is
provisional until a delayed re-assessment or the real-code transfer task confirms it;
`assessment.md` Parts 3–5).

**The two scored axes:**

- **AX1 — Preserve (executable).** Does behavior stay identical across a battery that hits the
  branches and boundaries? *(Settled by the runner; §5d. A "refactor" that changes the battery's
  output fails this outright.)*
- **AX2 — Judge (rubric).** Right move toward a better/deeper structure (D1)? Green/
  characterization test in place **first**? One hat on (no behavior change bundled in)? Timing
  right (about-to-touch / Rule of Three / not gold-plating)? Did they design a battery that
  actually *could* falsify preservation?

| Tier | Observable bar for D3 |
|---|---|
| **Foundations** | On a clear, behavior-preserving move (extract variable, magic→constant, loop→comprehension), **performs the move (or correctly confirms a given AFTER is behavior-preserving) and names the structural smell it fixes** — and predicts the (unchanged) output, confirmed by running BEFORE vs AFTER. AX1 solid; AX2 at least partial (names the smell; doesn't claim it's safe without the run). Allowed *with* the worked example faded to one missing step. |
| **Working** | On a candidate "refactor" that **may or may not** preserve behavior, **unaided**: correctly **classifies it refactor-vs-behavior-change**, **names the inputs that decide it**, and — if it changed behavior — says **where and why** (AX1). Articulates the judgment for the genuine case (what smell it fixes; that it needs a green test). Calls a clean-but-behavior-changing diff what it is: **not a refactor** (the central D3 catch). On 3 of 4 such unseen drills. Crediting cleanliness while missing a behavior change ⇒ partial pass, flagged. |
| **Advanced** | On **untested legacy** (or a change that survives shallow testing), **unaided**: **writes a characterization battery FIRST** that pins current behavior (including its quirks), performs the refactor, and **proves preservation** by running BEFORE vs AFTER (verified by the coach re-running) — **or** catches the planted behavior change that the obvious inputs miss (AX1). Combines ≥2 mechanisms. **Articulates the underlying judgment** on a teach-it-back (`drill-generation.md` §6) — "characterize before you change; a clean look doesn't make it a refactor; the quirk may be load-bearing; one hat at a time" — not just the instance (AX2 solid). |
| **Frontier** | `Frontier-N`: presses one dimension past the last comfortable success per §6 / `drill-generation.md` §5 (subtler/cross-call behavior change → weaker safety net → multi-step surface or a correct *don't-refactor* call → AI-generated-code verification). A moving target, not a fixed bar. |

Promotion is by **performance, not tenure** (`assessment.md` rule 1); the coach marks a tier
from what the learner *does* on unseen drills, never from claimed seniority or "I refactor all
day." Held-out re-assessment and **real-code transfer** outrank a same-session streak
(`assessment.md` Part 5) — and for a judgment module especially, the real-code signal is weighted
heavily (a clean synthetic-snippet streak that doesn't show up when the learner refactors their
own code under their own tests is not yet mastery).

---

## 8. Anti-patterns & evidence caveat

**Anti-patterns this module exists to break** (each is a catalog entry in §5c, surfaced as a
*behavior*):

- **Calling a behavior change a "refactor."** Shipping a clean-looking diff that silently
  changes some input's output. The signature D3 failure. The fix is mechanical and
  non-negotiable: **run the same inputs through BEFORE and AFTER and diff** — "looks equivalent"
  is not equivalent (`<`↔`<=`, bad De Morgan, lost short-circuit, integer re-association all
  read fine and aren't).
- **Refactoring untested legacy without characterizing first.** "Cleaning up" code with no test
  net and changing a quirk in the process. The fix: **characterization test first** (Feathers) —
  pin current behavior, including the odd corners, *then* restructure under green. A quirk you
  dislike is a *separate*, behavior-changing edit with its own justification.
- **"Tests pass, so it's safe."** Trusting a green-but-inadequate suite as proof of equivalence.
  The fix: preservation holds only for inputs *run*; make sure the battery exercises the **changed
  path and its boundaries** (B3). The runner is a falsifier, not a proof of total equivalence.
- **Wearing both hats.** Bundling a behavior change with the restructuring. The fix: **one hat at
  a time** (Fowler) — refactor *or* add behavior in a given step/diff, never both, so the diff
  stays reviewable and the behavior change can't ride in unscrutinized.
- **Premature abstraction / gold-plating / big-bang.** Extracting on the second look-alike
  (violating the Rule of Three), polishing code no change is coming to, or rewriting a big chunk
  with no green checkpoint. The fixes: **Rule of Three**; **refactor the code you're about to
  touch** ("make the change easy, then make the easy change"); **small steps under a green
  test** so a red test localizes the mistake to the last step.

**Evidence caveat (this is a `[Practitioner-canon]` module — say so, and this caveat is
load-bearing).** D3's grounding is craft plus one definitional anchor, and must not be oversold:

- The **definition-anchor** (behavior preservation, verified by the runner) is the only part
  that *feels* verified — and it is verified as a **definition enforced by execution**, **not**
  as an empirical finding about outcomes. The runner proves preservation **only for the inputs
  run** (a falsifier, not a proof of total equivalence; Dijkstra). The coach states this limit.
- The **discipline and judgment** (small steps under tests; two hats; Rule of Three;
  characterize-first; preparatory refactoring) are **`[Practitioner-canon]`** — Fowler, Feathers,
  Beck. Respected, widely-taught **craft**, vetted against the named sources during authoring —
  **not** empirical findings. The coach must never present them as verified science.
- **Do NOT claim "refactoring reduces bugs" or "improves maintainability."** This is the
  explicit honesty bound for D3. The empirical literature on refactoring's *causal* effect on
  defect rate and maintainability is **mixed, contradictory, and limited** — different studies
  report fewer defects, *more* bug reports, and *no clear effect* on maintainability depending
  on context (`evidence-base.md` → proposed D3 craft-source note). Refactoring is sold here as
  **disciplined craft that keeps behavior provably stable while you improve structure**, never
  as a proven defect-reduction intervention.
- The **AI-era priority** that places D3 in the verification cluster (as agents draft and
  "refactor" code, verifying that a fluent-looking change *actually* preserved behavior rises in
  importance; spec §12) is `[Verified-adjacent]` — **priority-steering, not proof**; the
  supporting productivity data is partly contested and vendor-sourced (`evidence-base.md` →
  AI-era honesty caveats).
- The **curriculum-wide transfer caveat** applies in full: that drilling refactoring judgment on
  synthetic snippets *causally* improves a given engineer's real restructuring is the open
  question. The coach leans on the transfer task (§9) — refactoring the learner's **own real
  code** under their **own tests** — as the honest individual-level evidence.

No claim in this module is dressed above its badge.

---

## 9. Transfer task

**The only honest test of whether the gym drill transferred to the job is applying it to a real
refactor on the learner's own code** (`assessment.md` Part 4; `evidence-base.md` → transfer
caveat, consequence 2).

> **Your turn:** Find a function in **your own codebase** that you have been meaning to clean up
> — one that is awkward, nested, duplicated, or that you are **about to change** for an upcoming
> feature (that last one is the best candidate: "make the change easy, then make the easy
> change"). Pick the smallest such function.
>
> Now **run the discipline.** **(1) Check the net:** is this code under a test? If **not**, you
> are looking at legacy code — **write a characterization test first** that pins its *current*
> behavior, including any quirky corners, and get it green. (Reduce the function to a runnable
> form and use the runner to capture the actual current outputs for your battery — don't guess
> them.) **(2) One hat on:** put on the *refactoring* hat — restructure in **small steps**, and
> after each step **re-run the test**; add **no** new behavior. **(3) Prove it:** run your input
> battery through the BEFORE and AFTER versions and confirm the outputs are **identical**. If any
> input differs, you changed behavior — that is a bug, not a refactor; back it out and redo the
> step.
>
> Then step back and judge: **was this refactor worth doing now?** Is it making a change you're
> actually about to land easier (good), or is it gold-plating code nothing is coming to (stop)?
> Did you abstract a duplication that has appeared **three** times, or jump on the second
> look-alike (premature)? And the honest one: **did any "cleanup" you wanted to do actually
> change behavior** you happened to dislike — and did you catch yourself trying to sneak it in
> under the refactoring banner?

**Grading is softer and named as such** (`assessment.md` Part 4). Your own code has no clean
answer key for the *judgment*; the coach grades against the §7 rubric (AX1 preserve / AX2 judge)
and says: *"behavior preservation I can verify by running your before/after; whether this was the
right refactor, and your test-first discipline, is a judgment call on your real code, not a
machine-verifiable result."* Where any sub-claim **is** runnable — and the behavior-preservation
claim always is — the coach **uses the runner**: reduce the function to a minimal runnable form,
run the battery through BEFORE and AFTER, and confirm identical output before the learner calls it
a refactor (the same discipline as the §5d check, now on the learner's real code). **Transfer
evidence is weighted heavily:** a learner who aces synthetic snippets but, on real code,
refactors with no test net, bundles a behavior change into the cleanup, or can't produce a battery
that would catch a regression has **not** transferred the skill, and the tracker notes that gap as
more diagnostic than another passed synthetic drill.

---

## Cross-references

- Drill mechanics, the **hybrid grading path** (executable behavior-preservation check +
  rubric judgment), exercise formats (Debug-this, Generation→Comparison, Error analysis,
  Teach-it-back), Frontier escalation: `references/drill-generation.md` (this module
  instantiates §1 and follows §2, §3, §4, §5; the behavior-preservation check uses §2).
- Session delivery (pause/no-spoiler hard stop, tier-faded worked example, direct feedback,
  **surface the BEFORE/AFTER run** so grading isn't hidden, scaffolding ladder):
  `references/coaching-loop.md`.
- D3 entry task, per-skill routing, mastery-rubric shape, held-out re-assessment, **real-code
  transfer** weighting: `references/assessment.md` (the D3 entry task: a BEFORE snippet plus a
  candidate "refactor" — decide refactor-vs-behavior-change, name the deciding inputs, and say
  what you'd test first).
- Evidence grounding (Fowler's definition + Two Hats + Rule of Three + small-steps-under-tests;
  Feathers' "legacy code is code without tests" + characterization tests; Beck's preparatory-
  refactoring line; the honest "refactoring's effect on bugs/maintainability is mixed" caveat;
  the reading spine; the worked-examples / expertise-reversal instructional finding):
  `references/evidence-base.md` → proposed D3 craft-source subsection + reading spine.
- Soft prerequisites: module **B3** (the tests that make refactoring safe — characterization +
  boundary cases), module **D1** (refactoring *toward* deep modules — the design target), and
  the execution-model module **A1** (the aliasing / short-circuit / mutable-default events that
  make a "looks equivalent" change actually change behavior).
- Golden exemplars (~3 per tier, each with a **runner-verified** BEFORE/AFTER behavior-
  preservation check — genuine refactors shown identical, fake ones shown to diverge):
  `exemplars/D3/foundations.md`, `exemplars/D3/working.md`, `exemplars/D3/advanced.md`.
</content>
</invoke>
