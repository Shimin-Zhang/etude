# A2 — Code Reading & Chunking `[Verified]`

> **Module type.** Pure `[Verified]` comprehension module — the second of the Track A
> reading foundation, modeled on A1's anatomy. It teaches the finding that most cleanly
> separates more- from less-skilled readers of code: experts **chunk** code into a few
> larger, meaning-bearing units and read **for structure**, exploiting **beacons** and
> recognizable **plans**, while novices grind **line-by-line on surface syntax**
> (`evidence-base.md` → Findings 2 & 3).
>
> **Core idea.** Don't read code left-to-right, top-to-bottom like prose. **Group the
> lines into 2–4 semantic chunks**, then **name each chunk by what it computes** — using
> the *beacons* (a `swap` in nested loops, an `acc = 0 … acc += … return acc` triad, a
> `lo/hi/mid` halving) that signal a chunk's purpose. *Read for structure, not syntax.*

---

## 1. Evidence basis `[Verified]`

This module rests on **two `[Verified]` findings** of `evidence-base.md`, both confirmed
there against primary sources. Cite via `evidence-base.md`; the anchor sources are:

**Finding 2 — Expertise is better representation; experts chunk code into larger
semantic units.** The signature evidence is a **recall asymmetry** borrowed from the
chess-expertise literature:

- **Shneiderman, B. (1976). Exploratory experiments in programmer behavior.**
  *International Journal of Computer and Information Sciences*, 5(2), 123–143. Programmers
  saw either a normal FORTRAN program or a **scrambled** (line-shuffled) one, then
  recalled it. On the **normal** program, perfect-line recall rose sharply with
  experience — the most experienced recalled **~18 lines vs ~6** for novices, a **3:1
  gap** — but on the **scrambled** program recall barely rose with experience: the
  expert advantage **collapsed toward parity** when the chunkable structure was
  destroyed. The *errors* were the tell: experienced readers replaced variable names and
  statement labels *consistently* and reordered lines in ways that *didn't change the
  result* — evidence they had stored the program's **meaning** (chunks), not its surface
  text.
- **McKeithen, K. B., Reitman, J. S., Rueter, H. H., & Hirtle, S. C. (1981). Knowledge
  organization and skill differences in computer programmers.** *Cognitive Psychology*,
  13(3), 307–325. **Replicated** Shneiderman in **ALGOL** (~18 vs ~6 lines, ordered vs
  scrambled; near-parity across skill levels on scrambled code), and showed experts'
  *recall order* and clustering mirrored the program's **functional structure**.
- **Gobet, F., & Simon, H. A. (1996). Recall of random and distorted chess positions.**
  *Memory & Cognition*, 24(4), 493–503. The chess analogue and the source of the
  curriculum's precise nuance: on **random** positions the expert recall advantage
  **shrinks but does not fully vanish** — a small skill effect survives. So chunking is
  the dominant mechanism, but not the *only* one.

**Finding 3 — Beacons and programming plans are real cues experts exploit.**

- **Brooks, R. (1983). Towards a theory of the comprehension of computer programs.**
  *International Journal of Man-Machine Studies*, 18(6), 543–554. **Origin of "beacons."**
  Comprehension is **top-down and hypothesis-driven**: the reader forms a hypothesis
  about what the program does, then **scans for beacons** — surface features that signal
  a structure — to confirm or reject it, refining hypotheses until each binds to a code
  segment. A beacon is *the line your eye lands on that makes you think "ah, this is a
  sort."*
- **Soloway, E., & Ehrlich, K. (1984). Empirical studies of programming knowledge.**
  *IEEE Transactions on Software Engineering*, SE-10(5), 595–609. Experts hold
  **programming plans** — stereotyped, reusable code fragments (a *running-total* plan, a
  *search* plan) — and **rules of discourse** (conventions, e.g. *a variable's name
  reflects its role*). When the discourse rule was **violated** — they renamed a
  variable to convey the **opposite** of its purpose (`max` → `min`) — **experts** got
  significantly **slower and more error-prone**, while **novices were unaffected**
  (novices weren't using the plans, so breaking them cost nothing). This is the empirical
  root of this module's **misleading-name** drills: a name is a *beacon*, and a beacon
  that lies costs the expert reader the most.
- **Crosby, M. E., Scholtz, J., & Wiedenbeck, S. (2002). The roles beacons play in
  comprehension for novice and expert programmers.** *PPIG 14th Workshop.* Eye-tracking
  evidence: **experts concentrate fixations on the important, beacon-bearing regions** and
  integrate across lines; **novices fixate roughly uniformly** and "do not seem to use
  beacons." Skill *is* selective attention to structure.

**Book anchor (technique).** Hermans, F. *The Programmer's Brain* (2021) —
`evidence-base.md` reading spine — operationalizes Findings 2 & 3 into teachable moves:
the **read-and-recall** chunking exercise (study code briefly, reproduce it, and your
*gaps* reveal what you couldn't chunk), and the taxonomy of **simple beacons**
(meaning-bearing names, operators like `>` / `+=`, structural `if`/`for`) vs **compound
beacons** (a multi-line idiom). Confirmed in the reading spine; cited as the
`[Practitioner-canon]`-flavored *technique layer* on top of the `[Verified]` science.

**Why these license this module.** All five primary sources are confirmed in the evidence
base's fact-checking pass (`evidence-base.md` → Research notes: "Shneiderman 1976 —
confirmed"; "McKeithen et al. 1981 — confirmed (≈18 vs 6; near-parity on scrambled)";
"Gobet & Simon 1996 — confirmed (shrinks but doesn't vanish)"; "Soloway & Ehrlich 1984 —
confirmed"; "Brooks 1983 — confirmed"). The verified claim is exactly what this module
drills: **skilled reading is structure-first chunking guided by beacons and plans, and it
is trainable.**

**Read through the transfer caveat — *and* one finding-specific caveat.** Like all
`[Verified]` findings here, the primary evidence is from **novices/programmers in the
1976–2002 era** in FORTRAN/ALGOL/Pascal (`evidence-base.md` → transfer caveat); the
*direction* is well supported, the *causal* lift for experienced engineers is open, and
the transfer task (§9) is the honest individual test. Additionally, the **plan-catalog**
idea is explicitly **refuted** as a teachable deep structure (`evidence-base.md` →
Refuted; Gilmore & Green 1988 found plan-sensitivity is **notation-dependent** — Pascal
programmers were cued by plans, BASIC programmers were not). So this module teaches plans
as **real cues to recognize**, never as a memorizable catalog that *is* programming. (The
Soloway-Ehrlich discourse result itself is not unchallenged — Gilmore & Green 1988 found
plan-sensitivity is **notation-dependent**, so experts do *not* uniformly benefit from
plan-like structure; see §8.)

---

## 2. Soft prerequisites

**Softly assumes A1 (notional machine).** To say *what a chunk computes* you must be able
to *simulate* it — the chunk `acc = 0; for x in xs: acc += x; return acc` only reads as
"sum" once you can execute the accumulator. So A1's execution model is the natural
under-layer. But this is a **soft** prerequisite, never a gate (`assessment.md` rule 2,
the buffet rule): a learner may open A2 cold, and in fact A2 is part of the **high-evidence
spine** every newcomer is routed to (`assessment.md` §1.2; spec §12 AI-era verification
cluster).

A2 in turn underlies **A3** (tracing — you chunk first, then trace the chunk that matters),
**C1/C2** (debugging and stack-trace reading — locate the suspect *chunk* fast), and **E3**
(code review — review is structure-first reading + judgment). Per `assessment.md`, soft
prerequisites *inform*, they never *block*: if a learner reads everything line-by-line, the
coach notes that downstream tracing/debugging/review speed likely traces back here — but
does not forbid later modules.

---

## 3. The mental model

**Reading code is not reading prose. You do not process it left-to-right, line-by-line.
You group the lines into a few meaning-bearing *chunks*, then label each chunk by *what it
computes* — and you find those chunks using *beacons*, the surface features that signal a
chunk's purpose. Read for structure, not syntax.**

Three moves, in order:

| Move | What you do |
|---|---|
| **1. Chunk** | Partition the function into **2–4 semantic units**, each a contiguous group of lines that does *one thing*: a *setup/init* chunk, a *guard/validate* chunk, a *main loop/transform* chunk, a *combine/return* chunk. The boundaries are usually blank lines, `for`/`while`/`if` headers, and shifts in which variables are touched. A 30-line function you can't hold in your head becomes **3 things you can.** |
| **2. Find beacons** | Within each chunk, spot the **beacon** — the feature that betrays its purpose. *Simple beacons:* a meaning-bearing **name** (`total`, `seen`, `lo`/`hi`), an **operator** (`>` in a loop → comparison/selection; `+=` → accumulation), a **structural** cue (`a[j], a[j+1] = a[j+1], a[j]` → a swap; `(lo+hi)//2` → a midpoint → binary search). *Compound beacons:* the multi-line **plan** itself — `acc = 0 … acc += x … return acc` is the *running-total* plan; `if x not in d: d[x] = [] ; d[x].append(v)` is the *group-by* plan. |
| **3. Name & hypothesize** | Give each chunk a **one-phrase name** ("dedupe by id", "find the max", "bucket events by key"), forming a **hypothesis** about the whole. Then **confirm against the code** (Brooks' top-down loop): does the rest of the chunk fit the hypothesis? If a line contradicts it, your chunk boundary or label is wrong — revise. |

**The discipline in one line: *read for structure, not syntax.*** The novice failure is to
narrate every token in order ("`x` equals `0`, then for `n` in `nums`, then if `n` greater
than…") and arrive with no compressed model — exactly the reader whose recall **collapses
on scrambled code** because they never built chunks (Shneiderman 1976). The expert move is
to see *three chunks and their beacons* and summarize in a sentence.

**Beacons can lie — trust behavior over names.** A beacon is a *hypothesis cue*, not
ground truth. A function named `sort_desc` that calls `sorted()` (ascending), a variable
named `total` that holds a **count**, a `min` that tracks the **max** — these are
**discourse violations** (Soloway & Ehrlich 1984), and they cost the *skilled* reader the
most, precisely because the skilled reader *relies* on the name-beacon. So the model has a
guard rail: **when a name-beacon and the behavior disagree, the behavior wins** — confirm
the chunk's label by what the code *does* (simulate it; A1), not by what it's *called*.

Three reading failures are the usual culprits, and the whole module drills them:

1. **No chunk boundaries.** Reading 30 lines as 30 facts instead of 3 chunks → working
   memory overflows, no model forms (`evidence-base.md` → cognitive load; Hermans).
2. **Missing the beacon.** Scanning past the one line that reveals the structure (the
   swap, the midpoint, the accumulator) → reading every line equally, like a novice's
   uniform eye-fixations (Crosby et al. 2002).
3. **Anchoring on a lying name.** Taking `sort_desc`/`total`/`min` at face value instead
   of confirming against behavior → the discourse-violation trap (Soloway & Ehrlich 1984).

---

## 4. Worked example — chunk, beacon, name, then verify a chunk

*(Foundations depth: every chunk shown and named, and one chunk's computation verified by
the runner. This fades by tier — see the note after the example.)*

The skill is to **stop reading line-by-line and see the chunks.** Consider this unfamiliar
function:

```python
def process(records):
    seen = set()                  # ┐
    out = []                      # ┘  chunk A — setup
    for r in records:             # ┐
        key = r["id"]             # │
        if key in seen:           # │  chunk B — dedupe guard
            continue              # │
        seen.add(key)             # │
        out.append(r)             # ┘
    return out                    #    chunk C — return result

data = [{"id": 1, "v": "a"}, {"id": 2, "v": "b"}, {"id": 1, "v": "c"},
        {"id": 3, "v": "d"}, {"id": 2, "v": "e"}]
result = process(data)
print([r["id"] for r in result])
print(len(result))
```

**Move 1 — Chunk.** Three chunks, not nine lines:

| Chunk | Lines | One-phrase name |
|---|---|---|
| **A — setup** | `seen = set(); out = []` | "a *set* to remember keys, a *list* to collect output" |
| **B — dedupe guard** | the `for` body | "skip any record whose id we've already seen" |
| **C — return** | `return out` | "hand back the kept records" |

**Move 2 — Find the beacons.** Chunk B's beacon is the **`if key in seen: continue`**
idiom paired with **`seen.add(key)`** — the *membership-set / seen-before* plan. The
choice of a **`set`** (not a list) for `seen` is itself a beacon: sets are for fast
membership tests, which signals "this loop tests *have I seen this before?*". The
**`continue`** says "and if so, skip it." That triad is the **deduplication plan.**

**Move 3 — Name & hypothesize.** Whole-function hypothesis: ***"returns the input records
with duplicate ids removed, keeping the first occurrence of each."*** Now **confirm against
the code** (Brooks' top-down check): keys are recorded *after* the skip test, so the
*first* time an id appears it's kept and added to `seen`; every later record with that id
hits `continue`. The hypothesis fits. ✓

**Verify a chunk — "what does chunk B compute?"** (executable-ground-truth discipline,
`drill-generation.md` §2 — the coach *runs* it, never guesses). Lift chunk B out and feed
it the ids `[1, 2, 1, 3, 2]`:

```python
seen = set()
out = []
records = [{"id": 1}, {"id": 2}, {"id": 1}, {"id": 3}, {"id": 2}]
for r in records:
    key = r["id"]
    if key in seen:
        continue
    seen.add(key)
    out.append(key)
print(out)            # which ids survive the guard
print(sorted(seen))   # the running set of ids seen so far
```

```
stdout: "[1, 2, 3]\n[1, 2, 3]\n"
status: ok
```

So chunk B keeps **first occurrences** `[1, 2, 3]` and `seen` accumulates `{1, 2, 3}` —
confirming the label "dedupe, keep first." And the full function:

```
stdout: "[1, 2, 3]\n3\n"
status: ok
```

**What chunking makes visible** (and line-by-line reading hides): you summarized a 9-line
function as **"dedupe records by id, keep first"** in one pass, by recognizing **one plan**
(the membership-set guard) from **two beacons** (`set` + `if … in … : continue`). A reader
narrating tokens (`seen` is a set, then `out` is a list, then for `r` in records, then
`key` is `r` sub `id`…) arrives at the *same loop* with **no compressed model** — and
would have to re-read it next time. The chunk *is* the thing that transfers.

> **Expertise reversal — the example fades by tier.** Per the worked-examples finding
> (`evidence-base.md` → instructional pillar; `coaching-loop.md` Step 2), a fully
> chunked-and-named example *helps novices* (it shows the moves while the schema forms)
> but becomes **redundant load for the more advanced** — they learn more by chunking it
> themselves. So the coach fades it:
>
> | Tier | Worked-example depth at A2 |
> |---|---|
> | **Foundations** | **Full** — coach shows the chunk table, the beacons, the hypothesis, and verifies one chunk's computation, exactly as above. |
> | **Working** | **Partial** — coach marks the chunk *boundaries* (or names chunk A) and leaves the learner to name the remaining chunks, cite the beacons, and write the 1–3-sentence summary. |
> | **Advanced** | **Skeleton** — coach hands the raw snippet and asks only for *the chunk map + the 2 most important chunks and why*; no boundaries pre-drawn. |
> | **Frontier** | **None** — straight to the problem (§6): a denser or adversarially-named snippet. |

---

## 5. Drill-generation spec

Instantiates the generation-spec format of `drill-generation.md` §1 for A2. Grading mode
is declared up front: **mixed** — executable for *"what does this chunk compute?"*,
rubric for *summaries* and *beacon/chunk identification* (§5d).

### 5a. Tier definitions (A2-specific)

The curriculum-wide tier names (`drill-generation.md` §1a) translated to this module:

| Tier | A2 criterion | Example shape |
|---|---|---|
| **Foundations** | A **small** function (≤ ~12 lines, 2–3 chunks) on a familiar plan. **Identify the chunks and the beacon** for each, **and** answer *"what does this chunk compute?"* for a named chunk (runner-checkable). | A max-finder, a strip/filter loop, a bubble sort: name the 2–3 chunks; compute the guard or the loop chunk. |
| **Working** | An **unfamiliar 30–50-line** snippet the learner hasn't seen. **Summarize what it does in 1–3 sentences**, **and** either **recognize the plan/idiom** it implements or **spot a misleadingly-named** variable/function (beacon vs reality). | Summarize a sliding-window scan; name the group-by plan; catch `sort_desc` that sorts ascending. |
| **Advanced** | A **denser** snippet (multiple functions / nested structure, or **unhelpful names**). **Chunk it, name the 2 most important functions/chunks and *why*,** and **recover intent from structure** when names don't help. | Chunk a settlement pipeline and justify the top-2 chunks; recover "binary search" from `g(a,t)` with `lo/hi/mid`-style single letters. |
| **Frontier** | See §6 — a moving target one step past the learner's last comfortable success (denser, longer, or more adversarial naming). | — |

A drill is mis-tiered if a "Foundations" snippet is actually a 40-line unfamiliar one, or
an "Advanced" one has fully helpful names and a single obvious plan; apply the self-check
(`drill-generation.md` §4) and re-level before posing.

### 5b. Parameter space (axes the coach varies to avoid mode-collapse)

Pick a *different point on each axis* across successive drills (`drill-generation.md` §1b,
§4 check 3). The axes for A2:

- **Plan / idiom** — running-total (reduce) · filter/clean · find-extreme (min/max) ·
  membership-set dedupe · group-by / bucketing · sliding-window · two-pointer ·
  binary search · accumulate-into-dict · sort (compound swap beacon) · map/transform ·
  memoized recursion. *(Recognize these as cues — never present a "catalog to memorize";
  `evidence-base.md` → Refuted.)*
- **Beacon type** — name-beacon (`total`, `seen`, `lo`/`hi`) · operator-beacon (`>`, `+=`,
  `//2`) · structural-beacon (swap, `continue`, early `return`) · compound/plan-beacon
  (the multi-line idiom) · **lying** beacon (discourse violation: name says the opposite).
- **Naming quality** — helpful/idiomatic names · neutral names · **single-letter /
  obfuscated** names (forces structure-only recovery) · **misleading** names (beacon vs
  reality).
- **Length / density** — ≤12 lines (Foundations) · 30–50 lines (Working) · multi-function
  or nested (Advanced).
- **Question type** — *what does this chunk compute?* (executable) · *summarize in 1–3
  sentences* (rubric) · *name the chunks + their beacons* (rubric) · *which 2 chunks
  matter most and why?* (rubric) · *spot the lying name* (rubric, confirmable by running) ·
  *what's the plan?* (rubric).
- **Format** (`drill-generation.md` §6) — primarily **Teach-it-back** (summarize/explain
  the structure) and **Generation → Comparison** (learner chunks, then compares to the
  coach's chunk map); also **Trace-the-path** for the "what does this chunk compute?"
  sub-question, and **Debug-this** when a lying name has caused a latent bug.

Keep an in-session log of the `(plan, beacon type, naming quality, question type)` tuples
used; do not repeat a tuple until the others are exercised.

### 5c. Common-error catalog

The *specific* code-reading failures, each with the conceptual gap it diagnoses
(`drill-generation.md` §1c format). These are grounded in the chunking/beacon/plan
literature — Shneiderman 1976, McKeithen 1981, Brooks 1983, Soloway & Ehrlich 1984, Crosby
2002, Hermans 2021 — **not** in trivia. **The root of most of them is one habit: reading
code as a linear sequence of tokens (like prose) instead of grouping it into a few
beacon-anchored chunks and reading for structure.**

```
Error: Narrates the code line-by-line / token-by-token ("x = 0, then for n in nums, then
       if n > best...") and produces no compressed summary, or a summary that just
       restates the lines in order.
Diagnoses: No chunking — processes surface syntax sequentially instead of grouping lines
           into semantic units. The novice signature; the reader whose recall collapses on
           scrambled code because nothing was ever chunked. (Shneiderman 1976; McKeithen
           1981; Hermans — cognitive load.)
Example trigger: any Working snippet — ask for a 1–3 sentence summary; a line-by-line
                 retelling instead of "it finds the highest-sum window" is the tell.

Error: Reads every line with equal weight and misses the one line that reveals the
       structure (the swap, the (lo+hi)//2 midpoint, the acc += x accumulator).
Diagnoses: Not using beacons — fixating roughly uniformly instead of concentrating on the
           meaning-bearing region, so the plan is never recognized. (Crosby et al. 2002 —
           novices "do not seem to use beacons"; Brooks 1983.)
Example trigger: bubble sort with a swap inside nested loops — "name the beacon that tells
                 you it's a sort"; missing the a[j],a[j+1]=a[j+1],a[j] swap is the gap.

Error: Takes a variable/function name at face value when the behavior contradicts it —
       e.g. reports that sort_desc() sorts descending, or that `total` holds a sum when it
       holds a count, or that `min` tracks the minimum when it tracks the max.
Diagnoses: Anchoring on a lying beacon — trusting the name-beacon over behavior, exactly
           the discourse-violation trap that costs skilled readers most. Did not confirm
           the chunk's label against what the code DOES (simulate it). (Soloway & Ehrlich
           1984; A1 — simulate, don't read intent.)
Example trigger: def sort_desc(values): ... return sorted(values), count — "what does it
                 return, and does the name match the behavior?"

Error: Draws chunk boundaries in the wrong place — splits one plan across two "chunks," or
       lumps setup + loop + return into one undifferentiated blob.
Diagnoses: Boundary-detection failure — not seeing that blank lines, loop/branch headers,
           and shifts in which variables are touched delimit semantic units; the chunk map
           doesn't match the program's functional structure. (McKeithen 1981 — expert
           recall clusters on functional structure; Hermans.)
Example trigger: the settlement pipeline — "draw the chunk boundaries"; a map that splits
                 the fee calc from its own loop, or merges validate+settle, is the gap.

Error: Recognizes a familiar surface (a for-loop over a list) and pattern-matches to the
       WRONG plan — calls a filter a reduce, or a group-by a dedupe, because it skimmed the
       beacon instead of confirming it.
Diagnoses: Hypothesis not confirmed against the code — formed a top-down guess from a
           partial beacon and never ran Brooks' verification loop, so a near-miss plan was
           accepted. (Brooks 1983 — hypotheses must bind to the code.)
Example trigger: group-by (if k not in table: table[k]=[]; table[k].append(v)) mislabeled
                 "removes duplicates" — the append (not skip) is the disconfirming beacon.

Error: Cannot say what a function does at all when the names are unhelpful (single letters
       g(a, t), x/y/m), even though the structure is a textbook algorithm.
Diagnoses: Over-reliant on name-beacons; cannot fall back to STRUCTURAL beacons (the
           (x+y)//2 midpoint, the lo/hi-narrowing while-loop) to recover intent when the
           naming layer is stripped. (Brooks 1983; Soloway & Ehrlich 1984 — plans are
           structural, not just lexical.)
Example trigger: binary search written with g(a,t)/x/y/m — "what does this compute, and
                 what structural beacon told you?"

Error: Can label the chunks but cannot say which 1–2 carry the function's essential
       meaning — treats a one-line guard and the core transform as equally important.
Diagnoses: Chunks formed but not RANKED — no model of which chunk is load-bearing vs
           incidental, so the summary buries the point. (Hermans — chunk to find the
           gist; the AI-era review skill of "what matters most," spec §12 → E3.)
Example trigger: settlement pipeline — "name the 2 most important chunks and why"; ranking
                 the rounding over the validate-then-settle split is the gap.

Error: Produces a summary that is accurate at the line level but misses the PURPOSE — says
       "loops over series, adds and subtracts elements, tracks a best value" instead of
       "finds the contiguous window of length k with the largest sum."
Diagnoses: Described the mechanism, not the intent — chunked the operations but didn't lift
           to what the function is FOR. A partial pass: the chunks are seen but not named
           at the right altitude. (Brooks 1983 — comprehension binds code to the problem
           domain; flag as product-without-purpose, cf. illusions of fluency.)
Example trigger: the sliding-window scan — a mechanism-level summary with no "maximum
                 window sum" is the partial-pass signature.
```

### 5d. Grading mode

**Mixed** (`drill-generation.md` §1d, §3). A2 drills split into two grading paths, and the
coach declares which applies to each sub-question:

- **Executable ground truth** for *"what does this chunk compute?"* / *"what does this
  print/return?"* The coach lifts the chunk (or runs the whole snippet) via
  `python <skill-dir>/runtime/python/runner.py snippet.py`, parses the `RunResult` JSON,
  and grades the prediction against `stdout` (strip the trailing newline before comparing
  to a bare prediction) and/or `status`. The coach **never guesses** the output. Use this
  for every Foundations chunk-computation and to **confirm a "lying name" finding** (run
  `sort_desc` and show it returns ascending).
- **Rubric + exemplars** for *summaries*, *chunk/beacon identification*, *"which 2 chunks
  matter"*, and *plan recognition* — there is no single string to match. Grade against the
  **summary rubric** below and the per-tier exemplars in `exemplars/A2/`, citing which
  exemplar the learner's answer is closest to, and say out loud: *"this is a judgment call
  graded against the module's rubric, not a machine-verifiable answer"* (`drill-generation.md`
  §3).

**Summary rubric** (the gold-standard bar for a 1–3-sentence summary; 3 binary criteria):

1. **Purpose, not paraphrase.** Does it state *what the function is FOR* (its intent /
   output contract — "finds the max-sum window of length k"), not a line-by-line retelling?
2. **Right chunks named.** Does it reference the load-bearing chunk(s)/plan correctly
   (the dedupe guard, the group-by, the search), without inventing behavior the code
   doesn't have?
3. **Beacon-justified & behavior-checked.** Can the learner cite the **beacon** that
   signals the structure *and* — where a name is misleading — note that the behavior
   overrides the name?

A pass is **≥2 of 3 with criterion 1 met**; criterion 1 (purpose) is required — a
mechanism-level summary that nails 2 and 3 but misses purpose is a **partial pass**
(product-without-purpose; `drill-generation.md` §3; `evidence-base.md` → illusions of
fluency). A2 drills are commonly **hybrid**: grade the executable chunk-computation via the
runner first, then apply the summary rubric to the prose; **report the two verdicts
separately** (`drill-generation.md` §3).

---

## 6. Frontier band

Frontier is not a fixed tier — it tracks the learner's **demonstrated ceiling** and presses
**one step** past their last comfortable success along a single parameter axis
(`drill-generation.md` §5). Escalating two steps collapses to failure; escalating none
loses the desirable-difficulty benefit.

**What "one step" means here** (per `drill-generation.md` §5):
- **Advanced** = chunk a dense/multi-function or unhelpfully-named snippet and rank the
  top-2 chunks, *one* such challenge at a time.
- **Frontier-N** = N increments beyond Advanced; each increment **adds exactly one**: more
  length, one more interacting plan, a notch worse naming, or removed cues (comments
  stripped). The learner's current Frontier-N is the highest N they have passed.

Escalation directions beyond Advanced for A2, with step counts:

1. **Length & density** (the canonical path): 50-line → ~80-line → a small module of
   several cooperating functions where the learner must chunk **at the function level**
   (what each function is *for*) before chunking within one. Each size jump is one
   increment.

2. **Adversarial naming** (push the discourse-violation axis from Soloway & Ehrlich):
   neutral names → all single letters → **actively misleading** names → a mix where *some*
   names lie and some don't (so the learner can't apply a blanket "ignore the names"
   rule). Each notch is one increment; this is the highest-value escalation for the AI era,
   where the learner must read *generated* code whose names may not match behavior.

3. **Stripped cues.** Remove comments, then remove the blank-line chunk boundaries, forcing
   structure recovery from control flow and variable-usage shifts alone (the read-and-recall
   exercise at its hardest; Hermans). One increment per cue removed.

4. **Interacting plans.** One plan → two nested plans (a filter feeding a group-by) → three
   (sliding-window over a cleaned, bucketed stream). Each added plan the learner must
   separately recognize is one increment.

5. **Cross-language transfer.** Once chunking is fluent in Python, present the *same plan*
   in a language whose surface differs (a JS reduce, a C `for(;;)` loop) — does the learner
   recognize the **plan** through the **notation**? (Honest caveat: Gilmore & Green 1988
   show plan-sensitivity is partly notation-dependent, so treat a miss here as expected
   difficulty, not failure; `evidence-base.md` → Refuted.)

6. **Hand off to A3 / E3.** Once *static* chunking is solid, the natural escalations are
   **A3** (now *trace* the chunk you identified as load-bearing) and **E3** (review a real
   diff — structure-first reading plus judgment about what matters). A2 is the prerequisite
   reading skill both build on.

Track the level as `A2: Frontier-N`. Reset condition: two consecutive failures at the same
level → drop to Advanced for one drill, then re-approach (`drill-generation.md` §5).

---

## 7. Mastery rubric

The observable per-tier bars, instantiating the rubric shape of `assessment.md` Part 2.
Two cross-cutting requirements apply at every tier above Foundations: **product *and*
process** (right answer *and* sound structure-first reasoning — a correct summary with no
chunk/beacon account is a Foundations-level pass at best), and **unaided + durable** (a
same-session streak is provisional until a delayed re-assessment or the real-code transfer
task confirms it; `assessment.md` Parts 3–5).

| Tier | Observable bar for A2 |
|---|---|
| **Foundations** | On a small (≤ ~12-line) familiar function, correctly **identifies the 2–3 chunks and the beacon for each** (the swap → sort, the `acc += x` → running total) **and** correctly answers *"what does this chunk compute?"* for a named chunk (runner-verified). Allowed *with* the worked example faded to marked boundaries the learner names. |
| **Working** | On an **unseen 30–50-line** snippet, produces a **1–3-sentence summary that passes the summary rubric (purpose + right chunks, unaided)** — **and** either **names the plan/idiom** correctly (group-by, sliding-window) **or spots a misleadingly-named** variable/function, *noting that behavior overrides the name*. Reaches "finds the max-sum window of length k", not "loops adding and subtracting elements." |
| **Advanced** | On a **denser / unhelpfully-named** snippet, **chunks it, names the 2 most important functions/chunks and justifies *why* each is load-bearing**, and **recovers intent from structure** when names don't help (recognizes binary search from `g(a,t)`/`x`/`y`/`m` via the `(x+y)//2` midpoint + halving beacons), unaided. Articulates the *general* reading move on a teach-it-back ("I look for the accumulator/guard/search beacon first"), not just the instance. |
| **Frontier** | `Frontier-N`: presses one step past the last comfortable success per §6 / `drill-generation.md` §5 (longer → worse naming → stripped cues → interacting plans → cross-language). A moving target, not a fixed bar. |

Promotion is by **performance, not tenure** (`assessment.md` rule 1); the coach marks a
tier from what the learner *does* on unseen snippets, never from claimed seniority. Held-out
re-assessment and real-code transfer outrank a same-session streak (`assessment.md` Part 5).
A probe to separate *recognition* from *guessing*: ask one consequence question
("what changes if line N flips its comparison?") — a learner who chunked correctly can
answer; one who pattern-matched a label cannot (`assessment.md` A2 entry task).

---

## 8. Anti-patterns & evidence caveat

**Anti-patterns this module exists to break** (each is a catalog entry in §5c, surfaced as
a *behavior*):

- **Reading code like prose, line-by-line.** Processing every token in sequence and
  arriving with no compressed model — the reader whose recall collapses on scrambled code
  because they never chunked (Shneiderman 1976; McKeithen 1981). The fix is mechanical:
  partition into 2–4 chunks and name each. *Read for structure, not syntax.*
- **Reading every line with equal weight.** Not concentrating on the beacon-bearing line
  that reveals the structure — the uniform eye-fixation pattern of novices (Crosby et al.
  2002). The fix: actively hunt the beacon (the swap, the midpoint, the accumulator)
  before reading the rest.
- **Trusting a lying name.** Taking `sort_desc`/`total`/`min` at face value when the
  behavior disagrees — the discourse-violation trap that costs *skilled* readers most
  (Soloway & Ehrlich 1984). The fix: when name-beacon and behavior conflict, **confirm by
  simulating** (A1) — behavior wins.
- **Accepting an unconfirmed hypothesis.** Pattern-matching a partial beacon to the wrong
  plan (a filter called a reduce, a group-by called a dedupe) without running Brooks'
  confirmation loop against the code (Brooks 1983). The fix: bind the hypothesis to the
  lines; one disconfirming beacon means re-chunk.

**Evidence caveat (this is a `[Verified]` module — caveat is targeted, not inflated).** The
two findings this module rests on (Findings 2 & 3) are `[Verified]` and among the
best-supported in the curriculum — the chunking recall-asymmetry **replicated across
languages** (Shneiderman → McKeithen) and matches the chess literature (Gobet & Simon
1996). So the module carries **no inflated claims to walk back.** Three honest limits:

1. **The chunking effect *shrinks but does not vanish* on scrambled material** (Gobet &
   Simon 1996) — a small skill residual survives, so chunking is the dominant mechanism,
   not the only one. Don't overclaim that it's *all* structure.
2. **No plan catalog.** Plans are **real cues to recognize**, but a clean *enumerable
   catalog of plans* taught as the deep structure of programming is **refuted** — plan
   sensitivity is **notation-dependent** (Gilmore & Green 1988: Pascal yes, BASIC no). This
   module drills *recognizing* plans, never *memorizing a canon* (`evidence-base.md` →
   Refuted, constrains B1 too).
3. **The discourse-violation result is contested.** Soloway & Ehrlich (1984) found experts
   hurt most by misleading names, but the expert advantage on plan-like structure is **not
   universal**: Gilmore & Green (1988) found plan-sensitivity is **notation-dependent**
   (Pascal programmers cued by plans, BASIC programmers not; `evidence-base.md` → Refuted), so
   experts do *not* uniformly benefit from plan-like structure. The robust, uncontested claim
   is the *direction* — experts **rely on** name/structure beacons more than novices — which is
   exactly what the misleading-name drills exploit; the coach does not assert a precise effect size.

And the curriculum-wide **transfer caveat** (`evidence-base.md`): the primary evidence is
from *novices/programmers, 1976–2002*, in FORTRAN/ALGOL/Pascal; that explicitly drilling
chunking *causally* improves *experienced* engineers is an open empirical question. (The
AI-era angle — *unaided* comprehension atrophies first under heavy AI assistance, Anthropic
RCT ~17% lower; `evidence-base.md` → AI-era impact — is `[Verified-adjacent]`
priority-steering, not proof; it is *why* A2 is in the verification spine, not a claim of
this module.) The coach leans on the transfer task (§9) — chunking the learner's *own* code
— as the honest individual-level evidence.

---

## 9. Transfer task

**The only honest test of whether the gym drill transferred to the job is applying it to
the learner's own real code** (`assessment.md` Part 4; `evidence-base.md` → transfer
caveat, consequence 2).

> **Your turn:** Open a file in **your own codebase** that you **did not write** (a
> teammate's module, a dependency's source, or your own code from long enough ago that
> it's unfamiliar). Pick the **longest function you can find that you don't already
> understand** — 30+ lines is ideal.
>
> Now **read it for structure.** (1) **Chunk it:** draw 2–5 boundaries and give each chunk
> a one-phrase name. (2) **Find the beacons:** for each chunk, name the feature (a name, an
> operator, an idiom) that told you its purpose. (3) **Summarize the whole function in 1–3
> sentences — purpose, not paraphrase.** (4) **Flag any lying beacon:** a name that
> *disagrees* with the behavior, or a chunk whose purpose surprised you once you traced it.
> Then **verify your weakest chunk:** reduce it to a runnable snippet, predict what it
> computes, and confirm with the runner.

**Grading is softer and named as such** (`assessment.md` Part 4). Real code has no clean
answer key for the *summary* and *chunk map* — the coach grades those against the §7 rubric
and says: *"this is a judgment call on your real code, not a machine-verifiable result."*
But the **chunk-computation sub-claim is still executable**: where the learner's chunk (or a
reduced version) is runnable, the coach uses `runner.py` to confirm what it computes before
discussing it — and uses the runner to **settle any "lying name" dispute** (run it; the
behavior decides). **Transfer evidence is weighted heavily:** a learner who passes generated
drills but cannot chunk and summarize an unfamiliar real function — or who chunks it but
can't say which 2 chunks matter — has not yet transferred the skill; the tracker notes that
gap as more diagnostic than another passed synthetic drill.

---

## Cross-references

- Drill mechanics, exercise formats, executable ground-truth protocol, rubric+exemplars
  path, Frontier escalation: `references/drill-generation.md` (this module instantiates §1
  and follows §2, §3, §4, §5; grading is **mixed** per §1d).
- Session delivery (pause/no-spoiler hard stop, tier-faded worked example, direct feedback,
  scaffolding ladder): `references/coaching-loop.md`.
- Entry task (the ~15–30-line "summarize + name the chunks" task; the consequence-probe),
  per-skill routing, mastery-rubric shape, held-out re-assessment, transfer weighting:
  `references/assessment.md` (A2 entry task).
- Evidence grounding (Findings 2 & 3; Shneiderman 1976; McKeithen 1981; Gobet & Simon 1996;
  Brooks 1983; Soloway & Ehrlich 1984; Crosby et al. 2002; the plan-catalog refutation
  Gilmore & Green 1988; Hermans as technique anchor; the worked-examples /
  expertise-reversal finding): `references/evidence-base.md`.
- Golden exemplars (~3 per tier, runner-verified where executable, gold-standard +
  rubric where not): `exemplars/A2/foundations.md`, `exemplars/A2/working.md`,
  `exemplars/A2/advanced.md`.
