# A1 — Notional Machine / Execution Model `[Verified]`

> **Module type.** Pure `[Verified]` comprehension module — the reference module the
> other 19 are modeled on. It teaches the single most curriculum-actionable finding in
> the evidence base: the durable barrier to programming is grasping the **runtime
> dynamics of execution**, not memorizing syntax (`evidence-base.md` → Finding 1).
>
> **Core idea.** A program is a **machine with state**; running it is a sequence of
> **deterministic state transitions**. The skill is to *simulate the machine*, step by
> step, rather than read the code for what the author *meant*.

---

## 1. Evidence basis `[Verified]`

This module rests directly on **Finding 1** of `evidence-base.md` — "the notional
machine is the durable barrier, not syntax" — which is `[Verified]` there against
primary sources. Cite via `evidence-base.md`; the two anchor sources are:

- **Sorva, J. (2013). Notional machines and introductory programming education.**
  *ACM Transactions on Computing Education*, 13(2), Article 8, 1–31.
  doi:10.1145/2483710.2483713. A *notional machine* is "an abstract computer for
  executing programs of a particular kind." Sorva synthesizes the misconception,
  mental-model, and threshold-concept literature and argues the notional machine should
  be an **explicit, primary learning objective** — addressed directly in teaching, not
  left to osmosis. His pedagogy (visual program simulation) has the learner **take on
  the role of the computer**, tracing execution step by step and tracking variable
  state, precisely because "reasoning about program execution" is the central novice
  difficulty. That is the move this whole module drills: *simulate, don't read intent.*

- **du Boulay, B. (1986). Some difficulties of learning to program.**
  *Journal of Educational Computing Research*, 2(1), 57–73. The **origin of the
  "notional machine" framing**. du Boulay decomposes early programming difficulty into
  five domains — *general orientation, the notional machine, notation, structures,*
  and *pragmatics* — and treats the notional machine ("the general properties of the
  machine one is learning to control") as foundational, with **assignment** as its
  flagship difficulty (e.g., the misconception that `A = B` and `B = A` are equivalent,
  or that `A = B + 1` stores the *formula* rather than the evaluated value).

**Why these license this module.** Both sources are confirmed in the evidence base's
fact-checking pass (`evidence-base.md` → Research notes: "Sorva 2013 — confirmed";
"du Boulay 1986 — confirmed"). The verified claim they support is narrow and exactly
what this module teaches: **the execution model is the barrier, and it improves when
the learner explicitly simulates state transitions rather than reading for intent.**

**Read through the transfer caveat.** Like all `[Verified]` findings here, the primary
evidence is from **novices in introductory courses (1976–1995)** in BASIC/Pascal/etc.
The *direction* — execution-model fluency is the durable foundation — is well
supported; its causal application to upskilling experienced engineers is an open
question (`evidence-base.md` → transfer caveat). The transfer task (§9) is the honest
test for the individual learner.

---

## 2. Soft prerequisites

**None — this is the foundational module.** A1 is the root of Track A and is presupposed
(softly, never as a gate) by tracing (A3), debugging (C1/C2), and concurrency (A4). A
learner may start here cold. There is no skill below it to lean on; everything else in
the curriculum leans on *it*.

Per `assessment.md`, soft prerequisites *inform*, they never *block*: the buffet rule
holds (any learner may open any module at any tier). If a learner is weak on A1, the
coach notes that downstream tracing/debugging gaps likely trace back here — but does
not forbid them from attempting later modules.

---

## 3. The mental model

**A running program is a machine with state. Execution is a sequence of deterministic
state transitions. To predict what code does, you simulate the machine — you do not
read the code for what the author intended.**

Four pieces of state, and the rule that moves them:

| State component | What it holds |
|---|---|
| **Variables (the namespace)** | A set of **names**, each **bound to** an object. A name is a *label*, not a box that holds a value — `y = x` makes `y` a second label on the *same* object `x` refers to; it neither copies the object nor permanently links the two names. |
| **The heap (objects)** | The actual objects (lists, dicts, ints, functions…). Some are **mutable** (a list can change *in place*) and some are not. Two names can point at one heap object — that is **aliasing**. |
| **The call stack (frames)** | One **frame per active function call**, each with its **own** local namespace, its arguments, and where to return. Calls **push** frames; returns **pop** them, unwinding the stack. A function's locals are private to its frame — they are *not* shared across calls. |
| **The program counter** | *Where execution is right now.* Statements run **one at a time, top to bottom**, except where control flow (branches, loops, calls, returns) moves the counter. Nothing runs "in parallel"; nothing "looks ahead." |

**The transition rule.** Each statement reads the current state and produces the next
state, deterministically. Same start state + same statement ⇒ same next state, every
time. To predict output, walk the statements in counter order and write down what
changes in the namespace, the heap, and the stack at each step. That hand-simulation —
not your reading of the author's intent — is ground truth.

**The discipline in one line: *simulate, don't read intent.*** The machine has no
"hidden mind" that figures out what you meant (Pea 1986 calls the belief that it does
the *superbug*). It does *exactly* what the transition rule says — `y = x` does not
"keep `y` updated," `if` does not "fire the moment its condition becomes true," a name
on the left of `=` is not "computed from a formula." When a prediction is wrong, it is
almost always because the reader *narrated intent* where they should have *executed the
rule*.

Three transitions are the usual culprits, and the whole module drills them:

1. **Rebinding vs. mutation.** `x = <new object>` moves the *label* `x` (other labels
   are untouched). `x.append(...)` / `x += ...` mutates the *object in place* (every
   label on it sees the change). Conflating these is the single most common
   execution-model error (`drill-generation.md` §1c).
2. **When code runs.** Defaults are evaluated **once, at definition time**; closures
   read their captured variable **at call time**; `and`/`or` **short-circuit** (the
   right operand may never run). "When" is itself state.
3. **Frames are independent.** Each call gets fresh locals; the stack unwinds on
   return; it is finite (deep recursion overflows it).

---

## 4. Worked example — a full state-table trace

*(Foundations depth: every step shown. This fades by tier — see the note after the
table.)*

The skill is to **be the machine**: keep a table of the live state and update one row
per statement in program-counter order. Consider:

```python
def total(prices):
    acc = 0
    for p in prices:
        acc = acc + p
    return acc

print(total([10, 20, 5]))
```

**Setup.** Line 7 calls `total([10, 20, 5])`. That **pushes a frame** for `total` whose
local `prices` is bound to the list `[10, 20, 5]`. We now trace *inside that frame*.
Columns are the live locals; each row is the state **after** the statement on that line
runs.

| Step | Statement (counter) | `prices` | `acc` | `p` | Heap / notes |
|---|---|---|---|---|---|
| 0 | *(frame pushed; args bound)* | `[10, 20, 5]` | — | — | one list object on the heap; `prices` labels it |
| 1 | `acc = 0` | `[10, 20, 5]` | `0` | — | name `acc` bound to int `0` |
| 2 | `for p in prices:` → take `10` | `[10, 20, 5]` | `0` | `10` | loop binds `p`; counter enters body |
| 3 | `acc = acc + p` | `[10, 20, 5]` | `10` | `10` | reads `acc` (0) + `p` (10); **rebinds** `acc` to new int `10` |
| 4 | `for` → take `20` | `[10, 20, 5]` | `10` | `20` | next iteration; `p` rebound |
| 5 | `acc = acc + p` | `[10, 20, 5]` | `30` | `20` | `acc` rebound to `30` |
| 6 | `for` → take `5` | `[10, 20, 5]` | `30` | `5` | last element |
| 7 | `acc = acc + p` | `[10, 20, 5]` | `35` | `5` | `acc` rebound to `35` |
| 8 | `for` → exhausted | `[10, 20, 5]` | `35` | `5` | iterator done; counter exits loop |
| 9 | `return acc` | — | — | — | returns `35`; **frame popped**, stack unwinds |
| 10 | `print(...)` (caller) | — | — | — | prints the returned `35` |

**Verified ground truth** (executable-ground-truth discipline, `drill-generation.md`
§2 — the coach *runs* it, never guesses):

```
stdout: "35\n"
status: ok
```

**What the trace makes visible** (and intent-reading hides): `acc = acc + p` is a
**rebind** every iteration — a *new* int object each time, the old one discarded — not
a mutation of a single mutable counter. The list `prices` is **never mutated**; it is
only read. And the loop variable `p` is rebound on each pass, not accumulated. Reading
"it sums the list" gets the *answer* but skips the *mechanism* — and it is the mechanism
that transfers to the cases where intent and execution diverge (aliasing, closures,
mutable defaults).

> **Expertise reversal — the example fades by tier.** Per the worked-examples finding
> (`evidence-base.md` → instructional pillar; `coaching-loop.md` Step 2), a full trace
> *helps novices* (it lowers extraneous load while the schema forms) but becomes
> **redundant load for the more advanced** — they learn more by doing the trace
> themselves. So the coach fades it:
>
> | Tier | Worked-example depth at A1 |
> |---|---|
> | **Foundations** | **Full** — the complete state table above, every row shown and explained. |
> | **Working** | **Partial** — coach fills the table through the first loop iteration, then leaves the remaining rows (and the final output) for the learner to complete. |
> | **Advanced** | **Skeleton** — coach names the columns (the relevant state) and hands the learner a blank table to fill; or drops the table and asks only for the final state + a one-line statement of the mechanism. |
> | **Frontier** | **None** — straight to the problem (§6). |

---

## 5. Drill-generation spec

Instantiates the generation-spec format of `drill-generation.md` §1 for A1. Grading mode
is declared up front: **executable ground truth** (§5d).

### 5a. Tier definitions (A1-specific)

The curriculum-wide tier names (`drill-generation.md` §1a) translated to this module:

| Tier | A1 criterion | Example shape |
|---|---|---|
| **Foundations** | Single mechanism on a familiar surface: rebinding, one straight-line block, or one loop with a running accumulator and 2–3 variables. Predict the **final value(s) / output**. | `x = 10; y = x; x = x + 1` → predict `x, y`. A loop summing a short list. |
| **Working** | Apply the model in a context the learner hasn't seen, where **intent and execution diverge**: aliasing vs. rebinding, a mutable default argument across two calls, late-binding closure capture, or an early `return`. Predict output **and** name the state change. | `make_adders()` loop of lambdas → predict `a(10) b(10) c(10)` (prints `12 12 12`). |
| **Advanced** | Combine two or more mechanisms, or a mechanism whose runtime behavior is non-obvious: recursion (the call stack), generator/iterator exhaustion, left-to-right evaluation order + short-circuit, augmented assignment on a mutable (incl. inside a tuple). Predict output/`status` **and** explain *why*. | `t = ([1],); t[0] += [2]` → predict that it **raises** *and* mutates. |
| **Frontier** | See §6 — a moving target one step past the learner's last comfortable success. | — |

A drill is mis-tiered if it requires more mechanisms than its tier allows; apply the
self-check (`drill-generation.md` §4) and re-level before posing.

### 5b. Parameter space (axes the coach varies to avoid mode-collapse)

Pick a *different point on each axis* across successive drills (`drill-generation.md`
§1b, §4 check 3). The axes for A1:

- **Mechanism** — rebinding · aliasing/shared-reference · mutation-vs-rebind (`+=`/
  `.append`) · mutable default argument · late-binding closure · scope &
  `UnboundLocalError` · evaluation order & short-circuit · iterator/generator
  exhaustion · recursion / call stack · augmented assignment on a mutable (incl. in a
  tuple).
- **Context** — standalone statements · inside a function · inside a loop · across two
  calls of the same function · in a comprehension · in a nested/recursive call.
- **Data shape** — scalar (int/str) · list · tuple · dict · generator/iterator ·
  function object.
- **Mutability** — mutable target vs. immutable target (the same operation, e.g. `+=`,
  flips behavior between list and tuple/int — a high-value contrast).
- **Predicted artifact** — final variable value · printed `stdout` · *whether it
  raises* (`status` / exception type) · the *order/count* of side effects (e.g. how many
  times a logged function ran).
- **Format** (`drill-generation.md` §6) — primarily **Prediction → Observation →
  Reflection** (the home format for notional-machine drills); also **Trace-the-path**
  (pause at each step, not just the end), **Debug-this** (a plausible execution-model
  bug), and **Teach-it-back** (articulate the state model after a pass).

Keep an in-session log of the `(mechanism, context, data shape, format)` tuples used;
do not repeat a tuple until the others are exercised.

### 5c. Common-error catalog

The *specific* execution-model misconceptions, each with the conceptual gap it
diagnoses (`drill-generation.md` §1c format). These are grounded in the misconception
literature — Pea 1986, du Boulay 1986, Kaczmarczyk et al. 2010, Qian & Lehman 2017,
and the Python Programming FAQ — not in trivia. **The root of most of them is one
misconception: "a name is a box that holds a value, and `=` copies the value into the
box." Python's model is "a name is a label bound to an object; `=` rebinds the label —
it never copies the object and never mutates it."**

```
Error: Predicts that reassigning a variable changes the other names that were
       assigned from it (e.g. y = x; x = x + 1; predicts y is now 11).
Diagnoses: Copy-on-assign / "linked names" model instead of name-binding. The learner
           thinks `y = x` either copies the data or permanently links the names, so
           rebinding one rebinds the other. (du Boulay 1986; Kaczmarczyk T1.)
Example trigger: x = 10; y = x; x = x + 1; predict x and y.

Error: Predicts that mutating an object through one name leaves a second name that
       points at it unchanged (b = a; a.append(4); predicts b == [1,2,3]).
Diagnoses: Does not model aliasing — two labels on ONE heap object. Confuses
           "different name" with "different object." (Python FAQ; CSC110 "mutation at
           a distance.")
Example trigger: a = [1,2,3]; b = a; a.append(4); predict b.

Error: Treats `x += [v]` and `x = x + [v]` as interchangeable for a list, so gets the
       aliasing consequence backwards.
Diagnoses: Models `+=` as pure sugar for `x = x + y`, missing that on a mutable it is an
           in-place __iadd__ mutation (aliases see it) THEN a rebind, whereas `x + y`
           builds a NEW object and rebinds only x. (PEP 203; Python FAQ.)
Example trigger: a=[1,2]; b=a; a += [3]; predict b. Then a=[1,2]; b=a; a=a+[3]; predict b.

Error: Predicts a mutable default argument is re-initialized on each call
       (def f(x, acc=[]): predicts f(1) then f(2) gives [1] then [2]).
Diagnoses: Models the default expression as evaluated at CALL time, fresh each call,
           instead of ONCE at definition time, stored on the function object
           (f.__defaults__) and shared across calls. (Python FAQ; Hitchhiker's Guide.)
Example trigger: def collect(item, bin=[]): bin.append(item); return bin
                 — predict collect(1) then collect(2).

Error: Predicts a loop of closures captures the value of the loop variable at each
       step (make_adders loop → predicts 10 11 12 instead of 12 12 12).
Diagnoses: "Copy-at-definition / snapshot" model of closures. The learner thinks a
           closure photographs its free variables when defined, instead of capturing
           the VARIABLE (the shared cell) and reading it at CALL time — by which point
           the loop has finished and all closures see the final value. (Python FAQ;
           Hitchhiker's Guide. Not peculiar to lambda — applies to def too.)
Example trigger: the make_adders / lambda-in-loop drill (prints 12 12 12).

Error: Expects reading a name before its in-function assignment to fall back to the
       global of the same name, rather than raising UnboundLocalError.
Diagnoses: Models scope as dynamic and positional ("local only after the assignment
           line") instead of statically determined for the WHOLE function: any binding
           anywhere makes the name local everywhere, so a pre-assignment read is an
           unbound local, not a global fallback. (Python FAQ; Bendersky.)
Example trigger: x = 10; def f(): print(x); x = x + 1 — predict whether f() raises.

Error: Assumes both operands of `and`/`or` always evaluate, and/or that they return
       True/False rather than an operand.
Diagnoses: Models boolean operators as always-bool, always-evaluate-both, instead of
           operand-returning short-circuit operators where the deciding operand is
           returned unchanged and the other side may never run (so its exceptions/side
           effects don't happen). (Python FAQ; mathspp Pydon't.)
Example trigger: 0 or 7 or (1//0) → predict the value AND whether it raises.

Error: Iterates a generator/zip/map a second time and expects the same values again;
       or drains it with a debug print(list(g)) and is surprised the real loop is empty.
Diagnoses: Models a generator as a re-iterable lazy LIST instead of a one-shot stateful
           CURSOR that is consumed on first iteration and yields nothing thereafter.
           (LabEx; Python data model.)
Example trigger: g = (n*n for n in range(4)); list(g) then list(g) — predict the second.

Error: Cannot explain why an inner recursive call doesn't clobber the caller's locals,
       and/or expects unbounded recursion to run for free.
Diagnoses: No stack-of-frames model — assumes one shared set of locals across calls, or
           no notion that each call costs a frame and depth is bounded (Python does no
           tail-call optimization → RecursionError near the limit). (Ned Batchelder.)
Example trigger: fact(4) — trace the frames and the unwind; or f(n): return f(n+1).

Error: Assumes augmented assignment is atomic, so if `t[0] += [2]` raises (tuple item
       assignment), the list is left unchanged.
Diagnoses: Models `+=` as one all-or-nothing operation, missing that it is two phases —
           in-place __iadd__ mutation (which COMMITS) then a rebind (which here raises
           on the tuple). The statement both mutates the list AND raises. (Python
           Morsels; PEP 203.)
Example trigger: t = ([1],); t[0] += [2] — predict whether it raises AND the value of t.

Error: Narrates what the code is "trying to do" / what the author meant and reports
       that as the output, without simulating the statements.
Diagnoses: The superbug — attributing a "hidden mind" to the machine; reading for
           intent instead of executing the transition rule. The root meta-error this
           module targets. (Pea 1986.)
Example trigger: any drill where intent and execution diverge (closures, aliasing,
                 mutable defaults, short-circuit).
```

### 5d. Grading mode

**Executable ground truth** (`drill-generation.md` §1d, §2). Every A1 drill has a
computable answer: the coach **runs the snippet** via
`python <skill-dir>/runtime/python/runner.py snippet.py`, parses the `RunResult` JSON,
and grades the prediction against `stdout` (strip the trailing newline before comparing
to a bare prediction) and/or `status` when the drill asks *whether it raises*. The coach
**never guesses** the output.

A1 drills are commonly **hybrid** (`drill-generation.md` §3): the *output* prediction is
executable-graded; the *"why"* (the state-transition explanation) is rubric-graded
against the per-tier bar in §7 and the catalog in §5c. Report the two verdicts
separately — a correct output with a hand-wavy or wrong mechanism is a **partial pass**
and is flagged as such (it often reflects luck, not model accuracy;
`evidence-base.md` → illusions of fluency).

---

## 6. Frontier band

Frontier is not a fixed tier — it tracks the learner's **demonstrated ceiling** and
presses **one step** past their last comfortable success along a single parameter axis
(`drill-generation.md` §5). Escalating two steps collapses to failure; escalating none
loses the desirable-difficulty benefit.

**What "one step" means here** (per `drill-generation.md` §5):
- **Advanced** = one non-trivial mechanism exercised in isolation.
- **Frontier-N** = N increments beyond Advanced; each increment adds exactly one new
  interacting mechanism OR pushes one parameter-space dimension up one notch.
- The learner's current Frontier-N is the highest N they have passed.

Escalation directions beyond Advanced for A1, with step counts:

1. **Compose mechanisms** (the canonical path from `drill-generation.md` §5):
   - Frontier-1: mutable default argument + aliasing across two calls (Advanced + 1 extra mechanism).
   - Frontier-2: mutable default + aliasing + closure capture in the same snippet (+ 1 more).
   - Frontier-3: the above + a decorator wrapping the function (+ 1 more).
   Each additional interacting mechanism is exactly one Frontier increment.

2. **Deeper call stacks** (push the call-stack parameter dimension): mutual recursion;
   an accumulator passed *down* the stack vs. combined *on the way up*; tracing the
   frame-by-frame state of a tree recursion; reasoning about the recursion-limit boundary.
   Each of these is one increment over whichever mechanism they are layered on.

3. **Lazy evaluation.** Chained generators (`map` over a `filter` over a generator);
   `itertools` pipelines; the interaction of generator state with `tee`; the difference
   between a generator object and a generator *factory*.

4. **Evaluation order at the edges.** Order of side effects across function arguments;
   comprehension scoping (the loop variable does **not** leak out of a comprehension in
   Python 3); operator-overloaded `__iadd__` / `__radd__` dispatch.

5. **Interleavings → hand off to A4.** Once the *single-threaded* notional machine is
   solid, the natural escalation is the **concurrent** notional machine — multiple
   instruction streams, interleavings, happens-before, and nondeterminism. That is a
   different machine and a different module: escalate into **A4 (concurrency mental
   models)** rather than stretching A1. A1 is the prerequisite intuition A4 builds on.

Track the level as `A1: Frontier-N`. Reset condition: two consecutive failures at the
same level → drop to Advanced for one drill, then re-approach (`drill-generation.md`
§5).

---

## 7. Mastery rubric

The observable per-tier bars, instantiating the rubric shape of `assessment.md` Part 2.
Two cross-cutting requirements apply at every tier above Foundations: **product *and*
process** (right answer *and* sound state-model reasoning — a correct answer with an
absent/wrong "why" is a Foundations-level pass at best), and **unaided + durable** (a
same-session streak is provisional until a delayed re-assessment or the real-code
transfer task confirms it; `assessment.md` Parts 3–5).

| Tier | Observable bar for A1 |
|---|---|
| **Foundations** | Correctly predicts the final value/output of a single-mechanism snippet — rebinding (`x = 10; y = x; x = x + 1` → `11 10`) or one loop with a running accumulator — **and** explains it in name-binding terms (assignment binds a *name* to a *value*; rebinding `x` does not touch `y`). Allowed *with* the worked example faded to one missing step. |
| **Working** | On **4 of 5 unseen drills** — including **at least one aliasing case and at least one closure/mutable-default case** — predicts the final state **and** output **unaided**, **and** can articulate the state model: distinguishes **rebinding** (moves one label) from **mutation** (changes the shared object, seen by all aliases), and names **when** code runs (defaults at definition time; closures read their variable at call time). Predicts `12 12 12` for the late-binding closure drill *and explains why* (the lambdas capture the variable `i`, read at call time, not its per-iteration value). |
| **Advanced** | On a **multi-mechanism** snippet, predicts output/`status` **and explains why**, unaided — e.g. correctly predicts that `t[0] += [2]` on `t = ([1],)` **both raises a `TypeError` and mutates the list**, naming the two-phase mutate-then-rebind; or traces a recursive call's frame-by-frame state and explains the unwind; or predicts that a generator is empty on its second `list()`. Articulates the underlying principle on a teach-it-back (`drill-generation.md` §6), not just the instance. |
| **Frontier** | `Frontier-N`: presses one mechanism past the last comfortable success per §6 / `drill-generation.md` §5 (e.g. mutable default + aliasing across calls → + closure capture → + a wrapping decorator). A moving target, not a fixed bar. |

Promotion is by **performance, not tenure** (`assessment.md` rule 1); the coach marks a
tier from what the learner *does* on unseen drills, never from claimed seniority. Held-out
re-assessment and real-code transfer outrank a same-session streak (`assessment.md`
Part 5).

---

## 8. Anti-patterns & evidence caveat

**Anti-patterns this module exists to break** (each is a catalog entry in §5c, surfaced
as a *behavior*):

- **Reading for intent instead of simulating.** Reporting what the code is "trying to
  do" / what the author meant as if it were the output, without walking the statements.
  This is Pea's *superbug* — attributing a hidden interpreting mind to the machine. The
  fix is mechanical: keep a state table and apply the transition rule. *Simulate, don't
  read intent.*
- **Trusting names over behavior.** Assuming a variable called `total` holds the total,
  a function called `sort` sorts, or that `y = x` keeps `y` "in sync" with `x`. Names
  are documentation, not execution; the machine binds and rebinds labels regardless of
  what they are called. (du Boulay's assignment misconceptions live here.)
- **Skipping the stack.** Reasoning about function calls as if there were one shared set
  of variables, or ignoring that the call stack is finite. Each call is its own frame
  with its own locals; the stack pushes on call and pops on return, and it overflows if
  you recurse too deep.
- **Conflating rebinding with mutation.** The highest-frequency concrete error: treating
  `x = ...` (move a label) and `x.append(...)` / `x += ...` (change the shared object)
  as the same kind of event. They produce opposite aliasing consequences.

**Evidence caveat (minimal — this is a pure `[Verified]` module).** The execution-model
finding (Finding 1) is `[Verified]` and among the best-supported in the curriculum, so
this module carries **no inflated claims to walk back**. The one honest caveat is the
curriculum-wide **transfer caveat** (`evidence-base.md`): the primary evidence is from
*novices in introductory courses, 1976–1995*; that explicitly drilling the notional
machine *causally* improves *experienced* engineers is an open empirical question. The
coach states this when relevant and leans on the transfer task (§9) — the skill working
on the learner's *own* code — as the honest individual-level evidence. No
`[Practitioner-canon]` or extrapolated claims are made in this module.

---

## 9. Transfer task

**The only honest test of whether the gym drill transferred to the job is applying it to
the learner's own real code** (`assessment.md` Part 4; `evidence-base.md` → transfer
caveat, consequence 2).

> **Your turn:** Find a function in **your own codebase** whose behavior once
> **surprised you** — a bug that made you say "wait, why did it do *that*?", or code
> you had to run to believe. Pick the smallest such function you can.
>
> Now **be the machine.** Trace it as a state table (namespace, heap, stack, counter),
> step by step, the way the worked example in §4 does. Then **explain the surprise as a
> state-machine event**: name the exact transition that did not match the intent you
> read into the code. Was it a rebinding you read as a mutation (or vice versa)? An
> alias you didn't know two names shared? A default evaluated once at definition time?
> A closure reading its variable at call time? A short-circuit that skipped a side
> effect? A frame whose locals you thought were shared?

**Grading is softer and named as such** (`assessment.md` Part 4). Real code has no clean
answer key; the coach grades against the §7 rubric and says: *"this is a judgment call
on your real code, not a machine-verifiable result."* Where the learner's code (or a
reduced version of it) **is runnable**, the coach still uses the runner for any
executable sub-claim — e.g., reduce the surprise to a minimal snippet and confirm the
behavior via `runner.py` before discussing it. **Transfer evidence is weighted heavily:**
a learner who passes generated drills but cannot locate or explain a real-code surprise
as a state-machine event has not yet transferred the skill — the tracker notes that gap
as more diagnostic than another passed synthetic drill.

---

## Cross-references

- Drill mechanics, exercise formats, executable ground-truth protocol, Frontier
  escalation: `references/drill-generation.md` (this module instantiates §1 and follows
  §2, §4, §5).
- Session delivery (pause/no-spoiler hard stop, tier-faded worked example, direct
  feedback, scaffolding ladder): `references/coaching-loop.md`.
- Entry task, per-skill routing, mastery-rubric shape, held-out re-assessment, transfer
  weighting: `references/assessment.md` (A1 entry task; the closure example printing
  `12 12 12`).
- Evidence grounding (Finding 1; Sorva 2013; du Boulay 1986; transfer caveat; the
  worked-examples / expertise-reversal instructional finding): `references/evidence-base.md`.
- Golden exemplars (~3 per tier, runner-verified): `exemplars/A1/foundations.md`,
  `exemplars/A1/working.md`, `exemplars/A1/advanced.md`.
