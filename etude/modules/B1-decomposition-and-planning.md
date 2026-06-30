# B1 — Problem Decomposition & Planning `[Verified-adjacent]`

> **Module type.** `[Verified] finding, taught as a [Verified-adjacent] skill` — a
> **judgment module**. Its concept rests on a `[Verified]` expert/novice *difference*
> (experts form an abstract, balanced plan before coding — `evidence-base.md` → Finding 5),
> but that finding is **correlational** (it describes what experts *do*, not a proof that
> *teaching* planning causally lifts an experienced engineer), so the skill is badged
> `[Verified-adjacent]`. There is **no executable ground truth for "is this a good plan?"** —
> a plan is graded against a **rubric + golden exemplars**. *Where a plan is concrete enough,
> one executable sub-claim is available* — implement the decomposed pieces and run the whole
> against a battery: **do the pieces compose to a correct result?** That check is reported
> **separately** from, and never substitutes for, the rubric verdict on the plan's quality.
>
> **Core idea.** Before you write any of the solution, build a representation of **all** of
> it: understand the problem, decompose it **top-down** into balanced sub-problems, name the
> **hard** one, and sequence the work to resolve that uncertainty first — rather than
> translating the requirements into code one line at a time.

---

## 1. Evidence basis `[Verified-adjacent]`

This module is **mixed-status** by design, and the coach must keep the empirical half apart
from the craft half (`evidence-base.md` → badge rules).

**(a) The empirical half — Finding 5 `[Verified]` (correlational).** Cite via
`evidence-base.md` → **Finding 5** ("Experts plan top-down before coding; novices translate
step-by-step"). It is `[Verified]` there against primary sources; **do not re-derive it** —
the finding and its citations already live in the evidence base. The narrow, verified claim
it licenses:

- **More-skilled programmers form an abstract, relatively complete representation of the
  solution *before* writing code** — decomposing the problem and **keeping all parts of the
  design at a comparable level of abstraction** before refining any one part — whereas
  **novices tend to translate the problem into code more linearly, one step at a time.** The
  anchor source is **Adelson & Soloway (1985)**, *The role of domain experience in software
  design* (IEEE TSE SE-11(11), 1351–1360): experts build a mental model and a **balanced**
  top-down plan, and **mentally simulate** it, before committing to code. Supporting:
  **Rist (1991)** on schema creation in programming (*Cognitive Science* 15, 389–414) and
  **Koubek & Salvendy** on expert/novice problem representation — both named in Finding 5.

That is the whole verified substance of this module: **the *direction* — represent and
decompose before coding, and keep the parts balanced — separates more- from less-skilled
programmers.** Two things it does **not** license, both load-bearing:

**(b) The craft half — sequencing & de-risking `[Practitioner-canon]`.** The specific
operational moves this module drills *beyond* "represent before coding" — **identify the hard
sub-problem and resolve it first**, **name the data shape that flows between pieces**, and
**decompose toward independently testable units** — are **respected engineering craft**, not
separate verified findings. Adelson & Soloway show experts *build and simulate a balanced
model* (from which the hard part becomes visible early); that the disciplined *practice* of
front-loading the load-bearing uncertainty causally improves outcomes is **craft inference**,
not a measured result. The coach says: *"this is respected practice — not a verified research
finding."*

**The hard honesty bound (the REFUTED claim that constrains this module).** The seductive
wrong turn here is to teach a **catalog of "programming plans"** — a memorizable library of
stereotyped solution templates you pattern-match a problem onto. **That is refuted**
(`evidence-base.md` → Refuted under verification). **Gilmore & Green (1988)** found that plan
sensitivity is **notation-dependent** — Pascal programmers were cued by plan structure but
BASIC programmers were **not** sensitive to the same plans — so plans **cannot** be the
language-independent "deep structure" of programming that you enumerate and drill. This module
therefore teaches decomposition as a **process** (understand → represent → decompose →
sequence, hard-part-first), and explicitly treats **"match the problem to a memorized
template"** as an **anti-pattern** (§8), not the skill.

**Read through the transfer caveat.** Like every `[Verified]` finding here, Finding 5's primary
evidence is from **novices vs. experts in study settings, largely 1976–1995**
(`evidence-base.md` → transfer caveat). The expert/novice *difference* is well supported; that
**explicitly teaching** decomposition **causally** improves a working engineer's real
performance is the open question the whole curriculum carries — which is exactly why the file
badge is `[Verified-adjacent]`, not `[Verified]`. The transfer task (§9) — decomposing a feature
the learner is **about to build for real** — is the honest individual-level test.

---

## 2. Soft prerequisites

**A1 (notional machine) and A3 (tracing) recommended — you can only plan what you can
simulate.** A decomposition is a set of claims about *what each piece will compute and what
flows between them*; verifying that the pieces compose is mental (or actual) execution. A
learner who cannot trace a loop (A3) or predict an aliasing/order-of-operations result (A1)
will write plans whose pieces *look* like they fit but don't — the failure §5c calls a broken
interface. **B2 (code writing & composition)** is the natural **downstream** module:
decomposition feeds composition — B1 produces the balanced sub-problems, B2 implements and
wires them. **B3 (testing & specifying correctness)** is the other tie: a good decomposition
breaks the problem into **independently testable units** and **surfaces the edge cases** up
front, which is exactly what B3 then drills as adversarial case-enumeration.

Per `assessment.md`, soft prerequisites **inform, never gate** — the buffet rule holds (any
learner may open any module at any tier). If a learner's plans keep failing to compose because
they mis-predict execution, the coach notes the gap likely traces to A1/A3 and *suggests*
shoring those up — but does **not** forbid B1. Conversely B1 is itself an upstream signal: a
learner strong on writing single functions (B2) but who flails on a multi-part problem is
exactly who B1 is for.

---

## 3. The mental model

**Decomposition is building the whole solution in your head before you build any of it in
code.** You read the problem until you can restate its contract; you sketch the **entire**
solution as a small set of sub-problems *at one altitude*; you find the **hard** sub-problem
and the **data that flows between pieces**; you sequence the work to resolve the hard part
first. The failure mode is not "wrote a bug" — it is **translating the requirements into code
one line at a time**, so that the shape of the solution is discovered *while* coding, the parts
end up at wildly different levels of detail, and the load-bearing difficulty ambushes you late.

Four stages, in order. They are a pipeline; a miss at an earlier stage poisons the later ones.

| Stage | What you produce | What goes wrong without it |
|---|---|---|
| **1. Understand** | Restate the problem's **contract**: inputs, outputs, the implicit constraints, what "correct" means. The deciding examples and the edge cases. | You solve the **wrong problem** — a flawless plan for a question nobody asked (counts all logins, not *failed* ones; misreads "last hour"). The most expensive miss, because everything downstream is wasted. |
| **2. Represent (top-down)** | The **whole** solution as **3–6 named sub-problems at a comparable level of abstraction** — the skeleton, before any one piece is refined. | **Linear translation**: you start coding piece 1 in full before pieces 4–6 exist, so the plan is **unbalanced** (one fully-coded step, three vague ones) and the overall shape is improvised. The Finding-5 novice signature. |
| **3. Decompose & find the hard part** | For each sub-problem: the **data shape** that flows in and out (so the pieces *compose*), and an explicit flag on the **hard / uncertain** one — the tricky ordering, the unfamiliar core, the ambiguous spec. | A **broken interface** (pieces that don't fit) and being **blindsided**: you discover the load-bearing difficulty only after sinking effort into the easy, comfortable parts. |
| **4. Sequence & de-risk** | An **order** to build the pieces that resolves the **hard sub-problem first**, and a note of which pieces are **independently testable**. | You build the easy parts, feel productive, and hit the wall last — when re-deciding the hard part forces you to throw the easy parts away. |

**The discipline in one line: *represent the whole before you write the parts — decompose
top-down into balanced sub-problems, name the hard one, and resolve it first; do not translate
requirements line by line.*** Three corollaries the module drills:

1. **Balance the altitude.** Every sub-problem in the plan sits at a comparable level of
   abstraction. A plan with one fully-coded step beside three one-word steps is the
   **canonical novice tell** (Finding 5: experts keep the parts balanced). The fix is to hold
   *all* parts at "named box + its contract" until the whole skeleton exists, then refine.
2. **Find the hard sub-problem first.** The plan's real job is to **surface the load-bearing
   uncertainty early** — the part you don't know how to do, or the decision the spec leaves
   open — so you attack it while it is still cheap to change course. The comfortable parts
   (I/O, looping, formatting) are not where the risk lives.
3. **Make the pieces compose.** A decomposition is only real if the **data shape between
   pieces** is named, so they actually fit — and ideally each piece is **independently
   testable** (ties to B2 composition and B3 case-enumeration). "Then do the analysis" is not a
   sub-problem; "`count(words: list[str]) -> dict[str,int]`" is.

**What this module is *not*.** It is **not** a catalog of plan templates to memorize and
match (refuted — Gilmore & Green 1988; §1, §8). There is **no single correct decomposition** of
a real problem; the rubric rewards a decomposition that is **complete, balanced, hard-part-aware,
and composable** — not one that matches a template.

---

## 4. Worked example — decomposing "top-N word frequency"

*(Foundations depth: the full decomposition shown, then verified by running the composed
pieces. This fades by tier; see the note after the example.)*

The skill is to **plan like an expert**: understand the contract, lay out the *whole* solution
at one altitude, name the hard part, sequence to de-risk it — **before** writing code. Consider
the problem:

> *Write `top_words(text, n, stopwords)` that returns the `n` most frequent words in `text`,
> case-insensitive, excluding `stopwords`, as `(word, count)` tuples. Order by count, highest
> first.*

**Stage 1 — Understand (restate the contract, surface the ambiguity).** Inputs: `text: str`,
`n: int`, `stopwords: set[str]`. Output: `list[(word, count)]`, length ≤ `n`. The spec says
"order by count, highest first" — but **what breaks ties?** Three words tied at count 2 and
`n = 2`: which two, in which order? The spec is **silent**, and a silent tie-break makes the
output **nondeterministic**. *Decision surfaced now, not discovered later:* ties broken
**alphabetically** (`word` ascending). Also: what is a "word"? *Decision:* a maximal run of
letters, lowercased (digits/punctuation are separators). These two decisions are the
**understand-stage** output — and they are exactly what a linear coder discovers *after*
writing the counter, when the tests come back flaky.

**Stage 2 — Represent (the whole skeleton, one altitude).** Five sub-problems, each a named
box with a contract — none refined yet:

| # | Sub-problem | Data in → out |
|---|---|---|
| 1 | `tokenize` | `text: str` → `list[str]` (lowercased letter-runs) |
| 2 | `remove_stopwords` | `list[str]`, `set[str]` → `list[str]` |
| 3 | `count` | `list[str]` → `dict[str, int]` |
| 4 | `rank` | `dict[str, int]` → `list[(word, count)]` sorted by **(count desc, word asc)** |
| 5 | `take` | `list[(word, count)]`, `n` → first `n` |

**Stage 3 — Find the hard part.** Four of these are routine. The **load-bearing** sub-problem
is **#4, `rank`** — specifically the **tie-break**, because it is the one decision that is
(a) not stated in the spec and (b) silently determines whether the function is even
deterministic. The token definition (#1) is the secondary uncertainty. *Everything else is
plumbing.*

**Stage 4 — Sequence & de-risk.** Build #4's ranking rule first (it is where the risk lives),
pin the token rule (#1), then the plumbing (1→2→3→5) in data-flow order. Each box is
**independently testable** — `rank({'a':2,'b':2,'c':1})` can be checked in isolation before any
of it is wired together.

**Now implement the pieces exactly as decomposed, wire them in order, and run the whole** — the
one executable sub-claim (`drill-generation.md` §2): *do the pieces compose to a correct
result?* The composed function, run through the runner against a battery (normal text, a 3-way
tie at the `n`-boundary, empty, `n` > vocabulary, all-stopwords, case+punctuation):

```python
def top_words(text, n, stop):
    words  = remove_stopwords(tokenize(text), stop)
    counts = count_words(words)
    return take(rank(counts), n)              # rank: sorted by (-count, word)
```

```
=== CORRECT decomposition (runner-verified) ===
top_words('the cat sat on the mat the cat', 2, {'the','on'})            -> [('cat', 2), ('mat', 1)]
top_words('banana apple cherry apple banana cherry date', 2, set())     -> [('apple', 2), ('banana', 2)]
top_words('', 3, set())                                                 -> []
top_words('alpha beta', 5, set())                                       -> [('alpha', 1), ('beta', 1)]
top_words('the the the', 1, {'the'})                                    -> []
top_words('Hello, hello! HELLO? world.', 2, set())                      -> [('hello', 3), ('world', 1)]
status: ok
```

**Why surfacing the hard part *first* paid off.** Watch what a linear translator gets instead.
They write tokenize → filter → count → "sort by count" → take, never deciding the tie-break,
so `rank` sorts by count **only**. Same five pieces, composed the same way — and it **runs
clean**. But on the 3-way tie:

```
=== FLAWED decomposition: rank by count only, tie-break never decided (runner-verified) ===
top_words('banana apple cherry apple banana cherry date', 2, set())  -> [('banana', 2), ('apple', 2)]
```

The correct plan returns `[('apple', 2), ('banana', 2)]`; the flawed plan returns
`[('banana', 2), ('apple', 2)]` — a **different answer**, decided by first-seen insertion order
rather than the contract. The pieces *composed*; the **plan was incomplete**, and the gap stays
hidden until a tie reaches the `n`-cut. **This is the whole module in one contrast:** the
executable check (does it compose?) and the rubric verdict (is the decomposition complete and
hard-part-aware?) are **different questions** — the flawed plan returns the contract's answer on
**four of the six** battery inputs — diverging only where a tie reaches the cut (the 3-way tie
shown above, **and** the `sat`/`mat` count-1 tie hidden inside the very first 'normal' input) —
and still fails the rubric, because it never surfaced the load-bearing decision. *Plan the hard
part first, or it ambushes you.*

> **Expertise reversal — the example fades by tier.** Per the worked-examples finding
> (`evidence-base.md` → instructional pillar; `coaching-loop.md` Step 2), a fully worked
> decomposition helps **novices** (it shows the four stages) but is **redundant load for the
> more advanced**, who learn more by decomposing themselves. So the coach fades it:
>
> | Tier | Worked-example depth at B1 |
> |---|---|
> | **Foundations** | **Full** — all four stages shown, the contract restated, the hard part named, the composition run and verified, including the flawed-plan contrast. |
> | **Working** | **Partial** — coach restates the contract and names the sub-problems, then leaves the **hard-part identification** and the **edge-case/data-shape decisions** for the learner. |
> | **Advanced** | **Skeleton** — coach hands over only the problem statement and the rubric; the learner produces the whole decomposition, names the load-bearing uncertainty, and justifies the sequencing unaided. |
> | **Frontier** | **None** — straight to the problem (§6). |

---

## 5. Drill-generation spec

Instantiates the generation-spec format of `drill-generation.md` §1 for B1. Grading mode is
declared up front: **rubric + golden exemplars, with a separately-reported executable
composition check** (§5d) — this is a judgment module, not an executable one. A B1 drill is a
**problem to decompose**; the deliverable is a **plan, not code** (`drill-generation.md` §6,
Generation → Comparison).

### 5a. Tier definitions (B1-specific)

The curriculum-wide tier names (`drill-generation.md` §1a) translated to this module. Every
drill poses a problem and asks for a **decomposition + plan** (inputs/outputs, the named
sub-problems with their data shapes, the hard part, the edge cases) — **no full code required**:

| Tier | B1 criterion | Example shape |
|---|---|---|
| **Foundations** | A **small, well-specified** problem with a clean 3–5-piece decomposition and **one obvious hard part**. Decompose into named sub-problems at a consistent altitude, name the data shape between them, and surface 1–2 edge cases. | Sum a `name,amount` file skipping malformed lines; run-length-encode a string; tally letter grades. |
| **Working** | A problem in an **unfamiliar context** where the **hard sub-problem is non-obvious** *or* the spec has **one ambiguity to surface**; a naive linear translation diverges from a correct plan. Must identify the hard part **first** and surface the edge cases a line-by-line coder misses. | Merge overlapping intervals (the hidden prerequisite is *sort first*); sessionize events by inactivity gap; dedupe under an **unstated** key/conflict policy. |
| **Advanced** | A problem that **combines two or more interacting sub-systems**, or where the **decomposition choice itself changes the difficulty** (a good split makes the hard part tractable; a bad one creates an intractable interface or solves the wrong problem). Must justify **why** this decomposition and sequence, name the load-bearing uncertainty, **and** teach-back the principle. | Replay an order-dependent ledger with overdraft rejection; tokenize→parse→eval an expression; critique a decomposition that *composes but solves the wrong problem*. |
| **Frontier** | See §6 — one step past the learner's last comfortable success. | — |

A drill is mis-tiered if a Foundations problem hides its hard part or its spec ambiguity (that
is Working), or a Working problem has an obvious single decomposition with no non-obvious hard
part, or an Advanced problem is really one routine pipeline. Apply the self-check
(`drill-generation.md` §4) and re-level before posing.

### 5b. Parameter space (axes the coach varies to avoid mode-collapse)

Pick a *different point on each axis* across successive drills (`drill-generation.md` §1b, §4
check 3). The axes for B1:

- **Problem domain/shape** — data aggregation/summary · parsing & transformation · search/lookup
  · stateful simulation / replay · windowing over time · small interpreter/evaluator ·
  algorithmic (the underlying *shape* of the problem).
- **Where the hard sub-problem lives** (the judgment axis) — a tricky **ordering / tie-break** ·
  a **hidden prerequisite step** (e.g. must sort first) · an **ambiguous / underspecified** spec
  · **edge-case density** · an **order-dependence** (cannot reorder/parallelize) · an
  **interface** between pieces (the data shape *is* the problem) · an **unfamiliar core
  algorithm**.
- **Ambiguity level** — fully specified · one decision to surface · genuinely underspecified
  (the learner must state assumptions before decomposing).
- **What the drill stresses** — completeness of the decomposition · **balance of abstraction
  levels** · **identifying the hard part first** · **data-shape/interface** between pieces ·
  **edge-case surfacing** · **sequencing / de-risking**.
- **Format** (`drill-generation.md` §6) — primarily **Generation → Comparison** (learner plans,
  coach reveals a gold decomposition); also **Completion** (here is a partial decomposition —
  fill the missing piece / the hard part), **Error analysis / Debug-this-plan** (here is a
  flawed decomposition — what breaks, and on which input?), and **Teach-it-back** (articulate
  the decomposition principle after a pass).

Keep an in-session log of the `(domain, hard-part-location, ambiguity, format)` tuples used; do
not repeat a tuple until the others are exercised.

### 5c. Common-error catalog

The *specific* decomposition failures, each with the conceptual gap it diagnoses
(`drill-generation.md` §1c format). Grounded in **Finding 5** (Adelson & Soloway 1985 — experts
form a balanced top-down plan; novices translate linearly) and the **refuted** plan-catalog
result (Gilmore & Green 1988), not in trivia. **The root of most of them is one inversion:
translating the requirements into code one line at a time instead of representing the whole
solution first — so the solution's shape, its balance, its hard part, and its edge cases are
all discovered *during* coding instead of *before* it.**

```
Error: Jumps straight into writing code (or pseudo-code at code-level detail) for the first
       step before the whole solution shape exists.
Diagnoses: Linear translation instead of top-down representation — the Finding-5 novice
           signature. The learner treats "plan" as "start typing"; the overall structure is
           improvised as they go, so later sub-problems are never represented. (Finding 5;
           Adelson & Soloway 1985.)
Example trigger: any Foundations/Working problem where the learner's "plan" is the opening
                 lines of an implementation rather than named sub-problems.

Error: Produces an UNBALANCED plan — one sub-problem fully detailed (sometimes fully coded)
       while the others stay vague one-liners ("...then do the analysis").
Diagnoses: Parts not kept at a comparable level of abstraction — the exact expert/novice
           difference in Finding 5. The learner refined the comfortable piece and hand-waved
           the rest, so the plan hides its own gaps. (Finding 5; Adelson & Soloway 1985.)
Example trigger: the log/sessionize problems, where parsing gets three detailed lines and the
                 actual aggregation gets "then count them."

Error: Spends the plan on the easy, familiar parts (I/O, looping, formatting) and leaves the
       genuinely hard or uncertain part unaddressed or hand-waved.
Diagnoses: Did not identify and FRONT-LOAD the load-bearing uncertainty. The plan optimizes
           for feeling productive on the comfortable parts instead of de-risking the part the
           learner doesn't yet know how to do. (Craft corollary of Finding 5's "simulate the
           model first.")
Example trigger: top-N-with-ties or merge-intervals, where the learner details the tokenizer /
                 the I/O and never decides the tie-break / the sort prerequisite.

Error: Names sub-steps but never says WHAT DATA flows between them, so the pieces won't
       actually compose.
Diagnoses: Decomposition without specifying the interface/contract between pieces. "Parse",
           "process", "output" with no data shapes is a list of verbs, not a decomposition;
           the pieces are assumed to fit. (Ties to B2 composition; surfaces as a broken
           interface when implemented.)
Example trigger: the expression-evaluator problem, where "parse it then evaluate it" omits the
                 token-stream / tree contract that IS the problem.

Error: Plans only the happy path; empty input, ties, boundaries, malformed data, and
       single-element cases are never mentioned.
Diagnoses: Represented the problem INCOMPLETELY — treated the spec as the happy path only.
           The edge cases are part of the contract (Stage 1), not an afterthought. (Ties to
           B3 case-enumeration.)
Example trigger: any problem with a non-trivial boundary (exactly-at-the-gap session, empty
                 file, n > vocabulary, the contained interval) the learner omits.

Error: The decomposition is internally tidy but answers a DIFFERENT question than the one
       asked (counts all events, not the failed ones; misreads "last hour" / "first-seen").
Diagnoses: Skipped Stage 1 (Understand) — a flawless plan for the wrong problem. The most
           expensive miss: the pieces compose perfectly and the result is confidently wrong.
           (Finding 5's "build the model" presupposes the right problem.)
Example trigger: the bracket-balance problem decomposed as "equal counts of ( and )", which
                 composes and runs but mis-defines "balanced" (")(" passes).

Error: Forces the problem onto a memorized template ("it's a map-reduce / it's two pointers,
       so...") and misses where THIS problem doesn't fit the template.
Diagnoses: Pattern-matching to a canned plan instead of decomposing THIS problem — the
           notation/problem-dependent failure of plan catalogs. Plans are real cues but NOT a
           transferable deep structure to match against. (REFUTED: Gilmore & Green 1988;
           evidence-base.md -> Refuted. This is an anti-pattern, not the skill.)
Example trigger: any problem that superficially resembles a known pattern but has a twist the
                 template hides (intervals that must be sorted; a tie-break the template omits).

Error: Wrong granularity — explodes into 15 trivial micro-steps, or collapses into one
       mega-step, so the decomposition does no real work.
Diagnoses: Granularity not matched to the problem. Over-decomposition is false precision (and
           buries the hard part among trivia); under-decomposition is no chunking at all. The
           target is 3-6 sub-problems at a comparable altitude. (Finding 5 — balanced
           representation.)
Example trigger: a learner who lists "open file, read line, split line, strip whitespace,
                 check length, ..." as ten steps, or "parse and compute the answer" as one.
```

### 5d. Grading mode

**Rubric + golden exemplars, with a separately-reported executable composition check**
(`drill-generation.md` §1d, §3). B1 has **no executable ground truth for the plan's quality** —
"is this a good decomposition?" is a judgment, not a computation (and there is **no single
correct decomposition**; Stage-1 ambiguity means reasonable plans differ). The coach grades a
learner's plan like this (the §3 judgment path, made concrete for B1):

1. **Score the plan against the B1 rubric (§7), criterion by criterion** — *did they understand
   the contract (not solve the wrong problem)? is the decomposition complete and balanced in
   altitude? did they name the hard sub-problem and the data shapes between pieces? did they
   surface the edge cases?* Each is a 3-point criterion (§7), graded explicitly, one by one.
2. **Cite the closest golden exemplar.** Compare the learner's plan to the tier's golds in
   `exemplars/B1/<tier>.md` — "your plan is close to the **weak** exemplar: balanced sub-problems
   but the tie-break never surfaced" vs. "close to the **strong** exemplar: named the hard part
   first and the edge cases up front." The golds are the calibration anchor.
3. **Run the composition check where the plan is concrete enough (the one executable sub-claim,
   reported separately).** If the decomposition is specific enough to implement, the coach
   implements each named piece **faithfully to the learner's plan**, wires them in the stated
   sequence, and runs the whole through `python <skill-dir>/runtime/python/runner.py snippet.py`
   against a battery **including the edge cases** (`drill-generation.md` §2). This answers a
   **different** question from the rubric: *do the pieces, as decomposed, compose to a correct
   result?* A plan that **fails the battery on an edge case it never surfaced** is executable
   proof the decomposition was incomplete — the coach shows the **exact input and the wrong
   output** (as in §4's flawed-plan contrast), never an assertion. A plan that **passes** the
   battery is **necessary, not sufficient**: composing on the tested inputs does **not** make a
   decomposition well-formed (it may be unbalanced, template-matched, or hard-part-blind and
   still pass) — so the composition check **never overrides** a weak rubric verdict.
4. **Name it as soft.** The coach says out loud: "**the plan's quality is a judgment call graded
   against the module's rubric + exemplars, not a machine-verifiable answer; the composition run
   is a separate check — it can prove a piece *doesn't* fit, but a clean run doesn't prove the
   plan is good**" (`drill-generation.md` §3; `assessment.md` §1.2).

B1 drills are thus **hybrid, the unusual way round**: the *plan quality* (the main event) is
rubric-graded; the *composition* (a sub-claim, only where concrete enough) has an executable
check. **Report the two verdicts separately** — a learner whose plan **composes** on the battery
(executable: passes) but is **unbalanced and never named the hard part** (rubric: weak) is a
**partial pass**, and the coach flags exactly that, because "it ran" is not "it was well
decomposed" — the central B1 confusion.

---

## 6. Frontier band

Frontier is not a fixed tier — it tracks the learner's **demonstrated ceiling** and presses
**one step** past their last comfortable success along a single parameter axis
(`drill-generation.md` §5). Escalating two steps collapses to failure; escalating none loses the
desirable-difficulty benefit.

**What "one step" means here** (per `drill-generation.md` §5):
- **Advanced** = a problem combining two interacting sub-systems *or* where the decomposition
  choice changes the difficulty, decomposed and justified with the hard part named.
- **Frontier-N** = N increments beyond Advanced; each increment adds exactly one new dimension
  of difficulty OR pushes one parameter-space dimension up one notch.
- The learner's current Frontier-N is the highest N they have passed.

Escalation directions beyond Advanced for B1, with step counts:

1. **More interacting sub-systems** (push the domain axis): from two coupled sub-systems → to a
   problem where **three** sub-systems interact and the **interface between them** is itself a
   design decision (Frontier-1) → to one where an early decomposition choice **forces a
   re-decomposition** of a later piece (Frontier-2). Each added interacting sub-system or forced
   re-decomposition is one increment.

2. **More ambiguity to resolve** (push the ambiguity axis): from one decision to surface → to a
   **genuinely underspecified** problem where the learner must **state several assumptions and
   justify them** before decomposing → to a problem where **two reasonable decompositions exist**
   and the learner must argue the trade-off (which makes the hard part tractable, which creates
   an intractable interface). Each is one increment.

3. **Decompose toward delegation & verification — the AI-era frontier.** A problem the learner
   must decompose well enough that each sub-problem could be **handed to an agent** and the
   **composition independently verified** — i.e. decomposition as the skill that makes
   agent-generated pieces *checkable* (`evidence-base.md` → AI-era impact; spec §12). One
   increment for "decompose into independently specifiable/testable units"; another for "and
   define the composition check that catches a piece the agent got subtly wrong." (Ties to B3
   specification and E3 review — verifying pieces you did not write.)

4. **Real-system cross-cutting concerns** (push toward the transfer task): a feature touching
   error handling, persistence, and an external call at once, where the decomposition must
   isolate the **decision likely to change** (ties to D1's deep-module / information-hiding
   framing). Each cross-cutting concern the plan must isolate is one increment.

Track the level as `B1: Frontier-N`. Reset condition: two consecutive failures at the same
level → drop to Advanced for one drill, then re-approach (`drill-generation.md` §5).

---

## 7. Mastery rubric

The observable per-tier bars, instantiating the rubric shape of `assessment.md` Part 2, scored
against the B1 dimensions. Two cross-cutting requirements apply at every tier above Foundations:
**product *and* process** (a complete-looking plan *and* sound top-down reasoning — a plan that
composes but is unbalanced or hard-part-blind is a Foundations-level pass at best), and
**unaided + durable** (a same-session streak is provisional until a delayed re-assessment or the
real-code transfer task confirms it; `assessment.md` Parts 3–5).

**The scored dimensions** (each 3-point: absent / partial / solid):

- **D1 — Understand.** Did they restate the contract and solve the **right** problem (not a tidy
  plan for the wrong question)?
- **D2 — Decompose & balance.** Is the decomposition **complete** and at a **consistent
  altitude** (3–6 named sub-problems, not one coded step beside three vague ones)?
- **D3 — Hard part & interfaces.** Did they **name the load-bearing uncertainty** and the **data
  shapes between pieces** (so the plan composes), rather than detailing the easy parts?
- **D4 — Edge cases & sequencing.** Did they **surface the edge cases** and **sequence to
  resolve the hard part first**? *(Composition sub-claim: where concrete enough, the plan is run
  against a battery incl. edge cases — §5d.)*

| Tier | Observable bar for B1 |
|---|---|
| **Foundations** | On a small well-specified problem, produces a **complete, balanced** 3–5-piece decomposition with the **data shapes** named and **1–2 edge cases** surfaced (D2 solid; D3 at least partial). Names the one obvious hard part. Allowed *with* the worked example faded to one missing decision. |
| **Working** | On an unfamiliar-context problem, **unaided**: understands the contract (D1), produces a balanced decomposition (D2), **identifies the non-obvious hard sub-problem first** and names the interfaces (D3), **and surfaces the edge cases a linear coder would miss** and sequences to de-risk (D4) — e.g. names "*sort first*" as the hidden prerequisite for merge-intervals, or **surfaces the unstated dedupe key** before planning. Detailing the easy parts while hand-waving the hard one ⇒ partial pass, flagged. On 3 of 4 such unseen drills. |
| **Advanced** | On a problem that **combines sub-systems** or where the **decomposition choice changes the difficulty**, **unaided**: produces the whole balanced decomposition, **justifies why this split and sequence** (which decomposition makes the hard part tractable; which would create a broken interface or solve the wrong problem), names the load-bearing uncertainty, **and** articulates the **underlying principle** on a teach-it-back (`drill-generation.md` §6) — "represent the whole first; find and resolve the hard part before the easy ones; there is no template to match" — not just the instance. Catches a decomposition that *composes but solves the wrong problem*. |
| **Frontier** | `Frontier-N`: presses one dimension past the last comfortable success per §6 / `drill-generation.md` §5 (more interacting sub-systems → more ambiguity to resolve → decompose-for-delegation/verification → real-system cross-cutting concerns). A moving target, not a fixed bar. |

Promotion is by **performance, not tenure** (`assessment.md` rule 1); the coach marks a tier from
what the learner *does* on unseen decomposition drills, never from claimed seniority or "I design
systems all day." Held-out re-assessment and **real-feature transfer** outrank a same-session
streak (`assessment.md` Part 5) — and for a judgment module especially, the real-code signal is
weighted heavily (a clean synthetic-plan streak that doesn't show up when the learner decomposes
their own feature is not yet mastery).

The **partial-knowledge routing boundary** (`assessment.md` §1.3), instantiated for B1: a learner
who **translates linearly / can't engage decomposition at all** (jumps to code, or one
undifferentiated blob) → **Foundations** (the model needs building); a learner who **decomposes
but unbalanced**, or **misses the hard part / the spec ambiguity**, or **omits the edge cases**
→ **Working** (a partial planning model to correct — they decompose but measure altitude or risk
wrong); a learner who **decomposes completely and balanced, names the hard part and interfaces,
and surfaces the edge cases**, articulating *why* → **Advanced**.

---

## 8. Anti-patterns & evidence caveat

**Anti-patterns this module exists to break** (each is a catalog entry in §5c, surfaced as a
*behavior*):

- **Linear translation.** Starting to write code for step 1 before steps 4–6 exist — discovering
  the solution's shape *while* coding. The Finding-5 novice signature. The fix is mechanical:
  represent the **whole** solution as named sub-problems at one altitude *before* refining any
  one of them.
- **The unbalanced plan.** One fully-detailed (or fully-coded) step beside three vague
  one-liners. The fix: hold every part at "named box + its contract" until the skeleton is
  complete; a plan is only as strong as its vaguest box.
- **Planning the easy parts.** Detailing the I/O and the loop while the tricky ordering, the
  unfamiliar core, or the open decision goes unaddressed. The fix: **find the hard sub-problem
  and resolve it first** — the comfortable parts are not where the risk lives.
- **The undefined interface.** A list of verbs ("parse, process, output") with no data shapes,
  so the pieces are *assumed* to compose. The fix: name what flows in and out of each box; "the
  data shape between pieces" is often the actual problem (the interpreter drill).
- **Happy-path-only.** A plan that never mentions empty input, ties, boundaries, or malformed
  data. The fix: edge cases are part of the contract (Stage 1), surfaced up front — the B3 move,
  done *before* coding.
- **Solving the wrong problem.** A tidy decomposition that answers a different question than the
  one asked. The fix: restate the contract and check the deciding examples **before** decomposing
  — the most expensive miss, because the pieces compose and the result is confidently wrong.
- **Template-matching (the refuted trap).** Forcing the problem onto a memorized "plan" and
  missing where it doesn't fit. The fix: decompose **this** problem from its contract — plans are
  real cues but **not** a transferable catalog to match against (Gilmore & Green 1988).

**Evidence caveat (this is a `[Verified-adjacent]` module — say so).** B1's grounding is **mixed
and must not be oversold**:

- The **empirical** half — that experts form an **abstract, balanced top-down plan before
  coding** while novices **translate linearly** — is **`[Verified]`** (Finding 5; Adelson &
  Soloway 1985 and the supporting sources). But it is a **correlational expert/novice
  difference**, largely from **study settings, 1976–1995** — it describes what experts *do*, not
  a controlled proof that *teaching* decomposition *causally* improves a working engineer. State
  it as "this is how experts differ," not "research proves planning makes you better."
- The **craft** half — **find the hard part first, name the interfaces, decompose toward testable
  units, sequence to de-risk** — is **`[Practitioner-canon]`**: respected, widely taught practice,
  vetted against Finding 5 during authoring, **not** a separate empirical finding. The coach must
  never present it as verified science (`evidence-base.md` → badge rules).
- The **refuted bound binds hard.** Teaching a **catalog of programming plans** as the
  transferable deep structure of programming is **refuted** (Gilmore & Green 1988 — plan
  sensitivity is notation-dependent). This module teaches decomposition as a **process** and
  treats template-matching as an **anti-pattern**; the coach must never reintroduce a plan
  catalog as "the skill."
- The **AI-era priority** — decomposition is what makes agent-generated pieces *specifiable and
  verifiable*, so it gains value as agents draft code (spec §12) — is **`[Verified-adjacent]`**:
  priority-steering, not proof (`evidence-base.md` → AI-era honesty caveats).
- The **curriculum-wide transfer caveat** applies in full: that decomposing synthetic problems
  *causally* improves a given engineer's real-feature planning is the open question. The coach
  leans on the transfer task (§9) — decomposing a **real feature** — as the honest individual-level
  evidence, and grades it as the soft judgment it is.

No claim in this module is dressed above its badge.

---

## 9. Transfer task

**The only honest test of whether the gym drill transferred to the job is applying it to a real
feature the learner is about to build** (`assessment.md` Part 4; `evidence-base.md` → transfer
caveat, consequence 2).

> **Your turn:** Pick a **feature or function you actually need to build** — something on your
> real backlog, big enough to have parts but small enough to plan in a sitting (a few hundred
> lines at most). **Before writing any code:**
>
> **(1) Understand.** Restate the contract in your own words: inputs, outputs, what "correct"
> means, and the constraints the ticket left implicit. Write down the **deciding examples** and
> the **edge cases**. Is there an **ambiguity** you've been about to code straight past?
> **(2) Represent.** Lay out the **whole** solution as **3–6 named sub-problems at one altitude**
> — each a box with the **data shape** flowing in and out. Resist refining any one box until the
> skeleton is complete. **(3) Find the hard part.** Mark the **load-bearing** sub-problem — the
> one you don't yet know how to do, or the decision the spec leaves open. Be honest: is it the
> part you've been avoiding? **(4) Sequence.** Order the work to **resolve the hard part first**,
> and note which boxes are **independently testable**.
>
> Then step back: **was your first instinct to start typing the easy part?** If your plan has one
> detailed box beside three vague ones, that is the unbalanced-plan trap — re-level them. And if
> you can reduce any sub-problem to a runnable stub, **wire the boxes and run the composition** on
> your edge cases before you trust that the pieces fit.

**Grading is softer and named as such** (`assessment.md` Part 4). A real feature has no clean
answer key, and there is **no single correct decomposition**; the coach grades against the §7
rubric (D1 understand / D2 decompose & balance / D3 hard part & interfaces / D4 edge cases &
sequencing) and says: *"this is a judgment call on your real plan, not a machine-verifiable
result."* Where any sub-problem **is** runnable — the learner can stub the pieces — the coach
still uses the runner: **implement the decomposition as the learner specified it and run the
composed whole against the edge cases**, surfacing the exact input where the pieces don't compose
(the same separately-reported composition check as §5d, now on the learner's real plan).
**Transfer evidence is weighted heavily:** a learner who aces synthetic decomposition drills but,
on a real feature, translates linearly — details the I/O and discovers the hard part halfway
through coding — has **not** transferred the skill, and the tracker notes that gap as more
diagnostic than another passed synthetic drill.

---

## Cross-references

- Drill mechanics, the **rubric + exemplars judgment path**, the separately-reported executable
  **composition check**, exercise formats (Generation→Comparison, Completion, Error-analysis,
  Teach-it-back), Frontier escalation: `references/drill-generation.md` (this module instantiates
  §1 and follows §3, §4, §5; the composition check uses §2).
- Session delivery (pause/no-spoiler hard stop, tier-faded worked example, direct feedback,
  scaffolding ladder): `references/coaching-loop.md`.
- B1 entry task, per-skill routing, the partial-knowledge boundary, mastery-rubric shape,
  held-out re-assessment, **real-feature transfer** weighting: `references/assessment.md` (the B1
  entry task: decompose a small ambiguous problem — the top-3 users by failed logins in the last
  hour — into named sub-problems and a plan, *no code*; judgment-graded, **not** against any plan
  catalog).
- Evidence grounding (**Finding 5** — experts plan top-down, Adelson & Soloway 1985 + Rist 1991 +
  Koubek & Salvendy; the **refuted** plan-catalog claim — Gilmore & Green 1988; the
  worked-examples / expertise-reversal instructional finding; the AI-era priority):
  `references/evidence-base.md`.
- Soft prerequisites (simulate the pieces you plan): modules **A1** (notional machine), **A3**
  (tracing); downstream **B2** (code writing & composition — decomposition feeds composition) and
  **B3** (testing & correctness — decompose toward testable units, surface edge cases); related
  **D1** (deep modules / information hiding — what a sub-problem should isolate).
- Golden exemplars (~3 per tier, each with a gold decomposition + rubric note, and a
  **runner-verified composition check** where the plan is concrete enough):
  `exemplars/B1/foundations.md`, `exemplars/B1/working.md`, `exemplars/B1/advanced.md`.
