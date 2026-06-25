# B2 — Code Writing & Composition `[Verified-adjacent]`

> **Module type.** `[Verified-adjacent]` (concept) **+ `[Practitioner-canon]`** (method) —
> a **construction** module, and the **most executable** of its cluster. Its *concept* —
> that writing sits at the top of a **reading → tracing → writing** developmental
> hierarchy and rests on the intermediate skills below it — is the `[Verified-adjacent]`
> correlational finding of `evidence-base.md` → Finding 6. Its *method* — **compose
> correct code in small verified steps** — is `[Practitioner-canon]` incremental-development
> craft, **not** a proven causal lever. The two are graded differently and badged
> separately throughout.
>
> **Grading.** The learner writes a function to a spec; the coach **runs it against a
> battery** (happy path **and** edge cases) through the runner and grades on **real
> pass/fail output** — that verdict is executable. The **composition *process*** (built up
> in small confirmed steps) is **rubric-graded**. The coach reports the **two verdicts
> separately**.
>
> **Core idea.** Don't write a big block and hope. **Grow the program one *confirmed* step
> at a time:** state the spec and its edge cases, write the smallest piece you can run,
> predict it, run it to confirm it does what you intended, and *only then* extend — never
> building on a line you have not confirmed.

---

**Relationship to A3, B1, and B3.** B2 is the **writing** end of the comprehension chain,
and it is deliberately surrounded by three siblings it leans on:

- **A3 (tracing & explain-in-plain-English)** is the skill *underneath* writing in
  Finding 6's hierarchy. To compose in verified steps you must be able to **predict what
  your own piece does** (trace it) and **say what it is for** (explain it) before you run
  it. B2 turns A3's reading-someone-else's-code skill *outward*, onto code you are
  producing.
- **B1 (decomposition & planning)** comes *before* the first line: B1 decides *what the
  pieces are*; B2 *writes* one piece at a time and confirms each. A learner who cannot
  decompose will compose a tangle; a learner who can decompose but writes big-bang will
  still ship the edge-case bug. The two are distinct skills.
- **B3 (testing & specifying correctness)** is the **battery** B2 is graded against, and
  the discipline that names the edge cases *before* the code exists. B2's "the edge case is
  part of the spec" corollary **is** the B3 hinge, applied while writing rather than after.

B2 does not re-teach A3's trace table, B1's decomposition, or B3's case enumeration; it
**operates** them in the act of producing code, and points back to each.

---

## 1. Evidence basis `[Verified-adjacent] + [Practitioner-canon]`

This module is **mixed-status by design**, and the coach must keep the two halves apart —
never presenting the craft method as if it were the verified finding (`evidence-base.md` →
badge rules).

### (a) The concept — Finding 6, the reading → tracing → writing hierarchy `[Verified-adjacent]`

B2 rests on **Finding 6** of `evidence-base.md` — "reading → tracing → writing is a
developmental hierarchy" — which is the **same anchor as A3** (cite it via
`evidence-base.md`; do **not** re-derive it). The narrow, confirmed claim:

- **Lopez, M., Whalley, J., Robbins, P., & Lister, R. (2008). Relationships between
  reading, tracing and writing skills in introductory programming.** *ICER '08*, 101–112.
  doi:10.1145/1404520.1404531. The keystone result: in combination, **tracing of iterative
  code and "explain in plain English" account for ~46% of the variance in code-writing**
  ability (R² = 0.46). The study fits a **skill hierarchy** — basic constructs at the
  bottom, **tracing and explaining as intermediate levels, code-writing at the top** — via
  path analysis. *Writing is the apex skill, and it is predicted by the two skills below
  it.* (Precision note, per the standing rule: the verified headline is the **46% combined
  variance**; each skill alone is weaker — iterative-tracing ≈15%, explaining ≈7%. The
  evidence base's earlier "R² ≈ 0.66" was a corrected error — that figure is the bivariate
  correlation r ≈ 0.63, a different quantity. This module cites only the 46%.)

- **Lister, R., Fidge, C., & Teague, D. (2009). Further evidence of a relationship between
  explaining, tracing and writing skills in introductory programming.** *ITiCSE '09*,
  161–165. doi:10.1145/1595496.1562930. The **replication** (a new institution, in
  **Python**, non-parametric analysis): **students who cannot trace usually cannot
  explain, and good writers have *usually* acquired both.** Crucially, the authors are
  **explicit that this is a soft prerequisite *tendency*, not a strict gate** — *one
  student wrote well despite failing both tracing and explaining.* This exception is
  load-bearing for B2's honesty: the hierarchy is a **correlational ordering**, not a law,
  and **not a proof that tracing drills *cause* writing ability**.

**Why this licenses the module — and the exact line it does not cross.** Finding 6 is
`[Verified]` *as a correlational developmental hierarchy* (`evidence-base.md` → Research
notes: "Lopez et al. 2008 (BRACElet) — confirmed"). It licenses B2 to teach writing **on a
foundation of tracing and explaining** — to have the learner predict and confirm each piece
(trace) and state the spec (explain) as they compose. It does **not** license the claim
that **drilling tracing causally improves writing**: that causal arrow is **open**, and
Lister, Fidge & Teague (2009) document an explicit exception. **B2's badge is
`[Verified-adjacent]`, not `[Verified]`, for exactly this reason** — the hierarchy is
verified-correlational; the causal lift is unestablished. The coach says: *"tracing and
explaining are strongly associated with, and developmentally prior to, writing — not a
guaranteed causal lever."*

### (b) The method — compose in small verified steps `[Practitioner-canon]`

The *process* B2 drills — **write the smallest runnable piece, confirm it, then extend** —
is **respected incremental-development craft**, taught for decades (grow a program; run as
you go; don't write past what you've confirmed). It is **practitioner consensus**, badged
as craft, **not** science, in the same way C2's "read the traceback bottom-up" is
(`evidence-base.md` → C2: a practice resting on consensus, deliberately *citing less* rather
than asserting an unverified result).

The **one empirical hint** in its favor is already in the evidence base, and it is
**contested** — so the coach reuses it carefully and never inflates it:

- **Fucci, D., et al. (2017). A dissection of the test-driven development process** (*IEEE
  TSE* 43(7), 597–614; `evidence-base.md` → B3b, the **contested TDD layer**). The finding:
  **"sequencing — the order in which test and production code are written — had no important
  influence"**; what helped was **granularity and uniformity (small, steady steps)**. That
  is suggestive support for B2's *small-verified-steps* discipline — but it sits in the
  **honestly-mixed, not-undisputed** TDD evidence layer (Turhan et al. 2010; Rafique & Mišić
  2013 — "small positive effect on quality, little/no effect on productivity"). **Treat it
  as a hint, not proof.** The coach says: *"the one study that points this way found small
  steps mattered more than the test-first ritual — but that whole literature is contested;
  this is respected craft, not a verified result."*

So: **concept `[Verified-adjacent]` (Finding 6, correlational), method `[Practitioner-canon]`
(incremental development, with one contested empirical hint).** The file badge is the closest
single token, `[Verified-adjacent]`; the honest prose badge is the mixed one above.

### Read through the transfer caveat

Finding 6's primary evidence is from **novices in introductory courses** (BRACElet,
~2004–2009, Java/Python). The *direction* — writing rests on tracing and explaining — is
well supported; that explicitly drilling composition *causally* improves *experienced*
engineers is an **open empirical question** (`evidence-base.md` → transfer caveat). The
transfer task (§9) — composing in the learner's **own** codebase — is the honest
individual-level test.

**AI-era note.** As coding agents draft most first-pass code, the human's composition skill
turns *outward*: the leverage moves from typing the happy path to **writing the precise
spec** and **the verifying battery** that pins it — exactly B2's two halves, aimed at code
one did not write. A NUS/Google CS-education consensus calls precise **specification +
verification** "arguably the most durable technical skill a graduate can possess," and ~45%
of AI-generated samples carried security vulnerabilities (Veracode 2025; `evidence-base.md` →
AI-era impact). That makes
B2's "edge case is part of the spec" and "confirm every step" disciplines *more* central,
not less — but the AI-era weighting is `[Verified-adjacent]` **priority-steering, not
proof**.

---

## 2. Soft prerequisites

**A3 (tracing & explain-in-plain-English) recommended, and B1/B3 adjacent.** Per Finding 6,
A3's two skills sit developmentally *below* writing — to compose in verified steps the
learner must **predict each piece** (trace) and **state the spec** (explain). **B1
(decomposition)** informs *what the pieces are* before B2 writes them; **B3 (testing)** is
the *battery* B2 is graded against and the source of the edge-case enumeration B2 composes
toward. **A1 (notional machine)** matters narrowly: the "return a new list vs mutate in
place" contract is an A1 rebinding-vs-mutation event seen from the *author's* side.

Per `assessment.md`, soft prerequisites **inform, never gate** — the buffet rule holds (any
learner may open any module at any tier). If a learner's writing fails and **A3 is also
weak**, the coach notes that the tracing/explaining gap likely underlies the writing gap and
*may* pull the relevant A3 drill — but does **not** forbid B2. This is the
`assessment.md` B2 routing signal stated verbatim there: *"if B2 is weak but A3 is also weak,
the tracker should note that tracing likely underlies the writing gap (do not gate — just
inform)."* The BRACElet data itself supports **soft** ordering only (Lister, Fidge & Teague
2009 — a tendency with exceptions), which is exactly why these are recommendations, not
locks.

---

## 3. The mental model

**Writing is not transcribing a finished solution from your head in one pass and finding out
at the end whether it works. Writing is *growing* a program in small, verified steps.** You
state the spec — *including its edge cases* — then repeatedly: write the smallest piece you
can run, **predict** what it does, **run** it to confirm it matches the spec, and **only
then extend**. The unit of progress is a **confirmed step**, not a written line.

The composition loop — five phases, run in a tight cycle, one small piece at a time:

| Phase | What you do | What goes wrong without it |
|---|---|---|
| **1. Spec** | Restate what the function must do and name its **contract**, including the **edge cases** (empty · single · boundary · duplicate · degenerate) and what each should return. *Explain it before you write it.* | You compose toward a target you never articulated — you code the *typical example* and silently miss the contract. (The writing-end of Finding 6: you cannot reliably write what you cannot explain.) |
| **2. Smallest piece** | Write the **smallest runnable fragment** that makes progress — often one branch or the happy path. Not the whole function. | You write a big block; when it fails, a defect could be *anywhere*, and you cannot localize it. |
| **3. Predict** | Before running, **predict** what this piece outputs on a concrete input — *trace your own code* (A3). | You run blind. A green result you did not predict is weak evidence — it may be right by luck, or right for the wrong reason (`evidence-base.md` → illusions of fluency). |
| **4. Run + confirm** | **Run** the piece; compare to your prediction *and* the spec. This piece is now a **confirmed point**. | "Looks right" is not "is right." A passing run shows the *presence* of correct behavior on that input, **never its absence of bugs in general** (Dijkstra; `evidence-base.md` → B3a). |
| **5. Extend** | Add the next piece — the next branch, the edge case — and **loop back to Predict**. Never build on an unconfirmed point. | The bug compounds underneath new code; the confirmed foundation you thought you had was never confirmed. |

**The discipline in one line: *grow the program one confirmed step at a time — write the
smallest piece you can run, predict it, run it, confirm it matches the spec, then extend;
never build on a line you have not confirmed.***

Three corollaries the module drills:

1. **The spec includes its edge cases.** A function that handles the typical input but
   mishandles the empty / boundary / degenerate case the spec *implies* is **unfinished**,
   not "working with a known bug." Name the edge cases **before** you write (the B3 hinge;
   Myers' boundary-value and equivalence-partition thinking — `evidence-base.md` → B3a). In
   the worked example, the even-length median is the edge a naive one-liner silently drops.

2. **Predict before you run; confirm before you extend.** Writing rests on tracing
   (Finding 6): you must be able to predict your own piece's behavior and confirm it against
   the spec *before* composing on top of it. A green run you did **not** predict tells you
   less than a predicted-then-confirmed one — use the runner to **confirm a prediction**, not
   to **discover** the answer.

3. **Stop at the spec's boundary.** Compose *exactly* what the contract requires — not less
   (happy-path-only) and not more (speculative generality for inputs the spec excludes).
   Every extra line is one more thing to verify and one more thing to get wrong.

---

## 4. Worked example — compose `median(xs)` in verified steps

*(Foundations depth: every step shown, with the runner-confirmed result pasted at each
confirmed point. This fades by tier — see the table after.)*

**The spec.** Write `median(xs)`: return the median of a **non-empty** list of numbers. For
**odd** length, it is the **middle value** of the sorted list; for **even** length, it is
the **average of the two middle values**. (Precondition: `xs` is non-empty.)

### Step 1 — State the spec back; name the edge case (don't write yet)

> *"Median = the middle of the sorted data. **Two cases:** odd length → one middle element;
> even length → the average of the two middle elements. The **even case is the trap** — a
> naive `sorted(xs)[n//2]` returns one element and is wrong on even-length input. And
> **empty** has no median; the precondition says non-empty, so I'll decide what happens if
> it's violated."*

That sentence is the **explain-before-write** move (Finding 6). Notice it has already named
both edge classes — *even length* and *empty* — **before any syntax exists.**

### Step 2 — Smallest runnable piece: sort + the odd case

Write the *smallest* thing that runs and makes progress — the odd-length path only:

```python
def median(xs):
    s = sorted(xs)
    n = len(s)
    return s[n // 2]      # odd-length case only, so far
```

**Predict, then run.** Predict `median([3, 1, 2])` → sorted `[1, 2, 3]`, middle is `2`. Now
run it — *and also run an even-length input on purpose*, to see the gap the spec warned about:

```
v2  median([3, 1, 2])    = 2     # status: ok   -> matches prediction (odd works)
v2  median([4, 1, 2, 3]) = 3     # status: ok   -> spec wants 2.5 -> the EVEN GAP is visible
```

The odd case is now a **confirmed point**. The run *also* made the even-length gap concrete:
`3`, not `2.5`. We did not "hope" the even case was handled — we **ran it and saw it isn't.**

### Step 3 — Extend: handle the even case (loop back to Predict → Run)

Add the even branch and re-confirm the *whole* battery:

```python
def median(xs):
    s = sorted(xs)
    n = len(s)
    if n % 2 == 1:
        return s[n // 2]
    return (s[n // 2 - 1] + s[n // 2]) / 2
```

**Runner-verified battery** (executable ground-truth discipline, `drill-generation.md` §2 —
the coach *runs* it, never guesses):

```
median([3, 1, 2])     = 2      # odd
median([4, 1, 2, 3])  = 2.5    # even  -> now correct (was 3)
median([5])           = 5      # single element (odd, n=1)
median([1, 3])        = 2.0    # two elements (even) -> float average
median([7, 7, 7, 1])  = 7.0    # even, duplicates -> (7 + 7) / 2
status: ok
```

Every prepared case is now a confirmed point. Note the run pins a detail a guess would miss:
the even branch returns a **float** (`2.0`, `7.0`) because `/` is true division — the odd
branch returns an **int**. That is a real, testable behavior the spec implicitly allows.

### Step 4 — Probe the remaining edge: empty input → decide the contract

The spec's precondition is "non-empty." Compose the *check* by running the boundary:

```
median([])    # n = 0, even branch -> (s[-1] + s[0]) / 2
status: error
stderr: "...
  File ..., line 6, in median
    return (s[n // 2 - 1] + s[n // 2]) / 2
            ~^^^^^^^^^^^^
IndexError: list index out of range"
```

The empty list **raises `IndexError`** — confirmed by running, not asserted. Now make a
**contract decision** (corollary 3): the precondition says non-empty, so either document it
and let it raise, or raise a *clear* error (`raise ValueError("median() of empty list")`) so
a caller gets a meaningful message instead of an opaque `IndexError`. Either is defensible;
*silently returning `0` or `None` is not*, because it hides the violated precondition. **The
edge case forced a design decision — that is the point of surfacing it before shipping.**

### What the verified-steps process made visible (and big-bang writing hides)

A learner who wrote the whole function in one block and ran it once on `[3, 1, 2]` would see
`2`, conclude "it works," and **ship the even-length bug** — the naive `sorted(xs)[n//2]`
returns `2` on that input *by luck of it being odd*. Building in steps **forced** the even
input to be run early, where the gap was cheap to see; and probing empty **forced** the
contract decision. The unit of progress was the **confirmed step**, not the written line.

> **Expertise reversal — the example fades by tier.** Per the worked-examples finding
> (`evidence-base.md` → instructional pillar; `coaching-loop.md` Step 2), a fully worked
> composition *helps novices* (it lowers extraneous load while the schema forms) but becomes
> **redundant load for the more advanced** — they learn more by composing themselves. So the
> coach fades it:
>
> | Tier | Worked-example depth at B2 |
> |---|---|
> | **Foundations** | **Full** — every step shown: spec stated, smallest piece, predict-and-run at each confirmed point, the even extension, the empty-edge contract decision, all runner-verified, as above. |
> | **Working** | **Partial** — coach states the spec and writes the *first* confirmed piece (e.g. the happy path), runs it, then leaves the **edge extension** and its battery for the learner to compose and confirm. |
> | **Advanced** | **Skeleton** — coach gives the spec and the contract only; the learner states the edge cases, composes in verified steps, and runs their own battery unaided. |
> | **Frontier** | **None** — straight to the spec (§6). |

---

## 5. Drill-generation spec

Instantiates the generation-spec format of `drill-generation.md` §1 for B2. Grading mode is
declared up front and is **two-tracked**: the **written function is executable-graded**
against a battery; the **composition process is rubric-graded** (§5d).

### 5a. Tier definitions (B2-specific)

The curriculum-wide tier names (`drill-generation.md` §1a) translated to this module. The
B2-specific axes are **how many pieces must be composed** and **whether the spec hides an
edge case a naive version misses**.

| Tier | B2 criterion | Example shape |
|---|---|---|
| **Foundations** | Write a function for a spec with a **single, clear behavior** on a familiar surface; happy path dominates and any edge is gentle/obvious. Build it in at least one confirmed step; pass the happy-path battery. | `clamp(x, lo, hi)` — clamp a number into a range. `count_evens(xs)`. `initials(name)`. |
| **Working** | Write a function whose spec **hides at least one edge case a naive version misses** (empty · boundary · even/odd · duplicate · normalization). **Name the edge before coding**, build in verified steps, pass the **full battery including the edge**. | `median(xs)` (even-length); `truncate(s, n)` (don't append when short enough); `is_palindrome(s)` (ignore case/punctuation); `chunk(xs, k)` (the remainder). |
| **Advanced** | **Compose two or more sub-behaviors** (parse + aggregate + format; helper + caller; a two-pointer merge with a remainder drain) **or** a spec where multiple edges interact and the **contract itself must be decided**. Pass the battery **and explain the composition** — why each step, why this contract. | `parse_kv(text)` (skip blank/malformed, later-key-wins); `merge_sorted(a, b)` (drain remainders); `summarize_scores(rows)` (group + average + round). |
| **Frontier** | See §6 — a moving target one step past the learner's last comfortable success. | — |

A drill is mis-tiered if a Foundations spec secretly hides a naive-misses-it edge (that is
Working), or a Working spec needs two interacting sub-functions (that is Advanced). Apply the
self-check (`drill-generation.md` §4) and re-level before posing. **Note the deliberate
difference from B1's tiers:** B1 levels by *how ambiguous the problem is to decompose*; B2
levels by *how many pieces must be composed and whether an edge case is hidden in the spec.*
B1 asks "what are the pieces?"; B2 asks "can you write each piece and confirm it before
building on it?"

### 5b. Parameter space (axes the coach varies to avoid mode-collapse)

Pick a *different point on each axis* across successive drills (`drill-generation.md` §1b, §4
check 3). The axes for B2:

- **Spec domain** — numeric / arithmetic · string / text · list transform · dict / grouping ·
  parsing · search or lookup.
- **Hidden edge class** (the Working/Advanced engine) — empty input · single element ·
  boundary (off-by-one, inclusive vs exclusive) · even/odd or parity · duplicates / ties ·
  remainder (non-divisible) · normalization (case, whitespace, punctuation) · negative / zero ·
  precondition violation (contract decision).
- **Output shape** — scalar · new list · dict · boolean · string · *raises on a violated
  precondition*.
- **Composition depth** — one piece · two sequential steps (transform then reduce) · helper +
  caller · two interacting conditions / a loop with a remainder drain.
- **What's given** — spec only (write from scratch) · a partial skeleton (a **completion
  prompt** at the teaching point) · a **happy-path version to extend** to pass the edge
  battery.
- **Format** (`drill-generation.md` §6) — primarily **Generation → Comparison** (learner
  composes, coach runs the battery, then reveals the gold); also **Completion prompts** (fill
  the gap at the exact teaching point), **Debug-this / extend** (here is a happy-path version —
  make it pass the edge battery), and **Teach-it-back** (explain the composition / justify the
  contract).

Keep an in-session log of the `(spec domain, hidden edge class, composition depth, format)`
tuples used; do not repeat a tuple until the others are exercised. **Do not reuse the same
hidden-edge gotcha** (e.g. "empty list") across consecutive Working drills — vary the edge
class, or the learner pattern-matches the gotcha instead of the discipline.

### 5c. Common-error catalog

The *specific* composition failures, each with the conceptual gap it diagnoses
(`drill-generation.md` §1c format). These are grounded in the comprehension-hierarchy and
test-design literature cited in `evidence-base.md` — Finding 6 (writing rests on
trace+explain), Finding 5 (the *linear-translation* novice signature), Myers' boundary/
equivalence thinking (B3a), Dijkstra (passing ≠ correct, B3a), and A1's rebinding-vs-mutation —
not in trivia. **The root of most of them is one misconception: *writing code is transcribing
a finished solution from your head in one pass, and you find out whether it works by running
the whole thing at the end.* The composition model is: *writing is growing a program in small
verified steps — state the spec (with its edge cases) first, write the smallest piece you can
run, predict it and run it to confirm it matches intent, and only then extend; the edge cases
are part of the contract you compose toward, not bugs to patch afterward.***

```
Error: Writes the entire function in one block, then runs it once at the end; when a case
       fails, cannot localize which piece is wrong (rewrites the whole thing or guesses).
Diagnoses: Big-bang composition — no incremental verification. Composes past the last
           confirmed point, so a defect could be anywhere and there is no confirmed
           foundation to stand on. The central B2 process failure. (Incremental-development
           craft; the one empirical hint, Fucci et al. 2017 "small steady steps," is
           contested — §1b; A3: trace each piece.)
Example trigger: any Working/Advanced spec — watch whether the learner runs intermediate
                 pieces or only the finished block; ask them to show their confirmed steps.

Error: Writes code that works on the typical input but silently mishandles the empty /
       boundary / even / duplicate case the spec implies (e.g. median via sorted(xs)[n//2]).
Diagnoses: Happy-path-only composition — treats the spec as its TYPICAL EXAMPLE rather than
           its full CONTRACT; did not enumerate the edge cases before writing. The function
           is unfinished, not "working with a bug." (B3 hinge; Myers boundary-value /
           equivalence partitioning, evidence-base.md -> B3a.)
Example trigger: median([4,1,2,3]) -> 3 not 2.5; truncate("hi",5) -> "hi..." not "hi";
                 chunk([1,2,3,4,5],2) dropping the [5] remainder.

Error: Jumps straight to the first line of syntax without restating what the function must
       do or naming the edge cases.
Diagnoses: Linear translation — translating the problem into code one step at a time
           (the documented novice signature, evidence-base.md -> Finding 5) instead of
           composing toward an ARTICULATED target. You cannot reliably write what you cannot
           explain (the writing-end of Finding 6).
Example trigger: pose any spec; score whether the learner states the spec + edges back before
                 typing, or starts coding immediately (a Teach-it-back/spec-restate prompt).

Error: Adds a piece and runs it without first predicting what it should output — uses the
       runner as a guess-checker rather than a confirmation of a prediction.
Diagnoses: Missing the trace-your-own-code half (A3 / Finding 6). A green run you did not
           predict is weak evidence: it can be right by luck or right for the wrong reason
           (evidence-base.md -> illusions of fluency). Use the runner to CONFIRM a prediction,
           not to DISCOVER the answer.
Example trigger: a learner who pastes a piece, runs it, and reads off the output as "correct"
                 without having said what they expected first.

Error: Extends or wraps a sub-piece that was never actually run, so the bug compounds
       underneath new code.
Diagnoses: No "confirmed point" discipline — treats WRITTEN as WORKING. The foundation the
           learner is building on was never confirmed, so a later failure has two suspects at
           once. (Dijkstra: a passing run shows presence, never absence; an UNRUN piece shows
           nothing at all -- evidence-base.md -> B3a.)
Example trigger: an Advanced compose (merge_sorted) where the learner writes the loop AND the
                 remainder drain together and runs only at the end.

Error: "Confirms" a step by re-running only the one input that already passed, never the
       edge / boundary.
Diagnoses: Confirmation testing inside composition — re-running a passing case is not NEW
           evidence. The boundary, where construction bugs live, goes unrun. (B3
           confirmation-bias entry; Myers -- the cases most likely to find errors are the
           ones not yet tried.)
Example trigger: after extending median, the learner re-runs [3,1,2] (odd, already green) and
                 declares done, never running an even-length or empty input.

Error: Off-by-one / wrong boundary in the composed logic — an inclusive/exclusive slip, a
       range that is one short or one long, a slice that drops the last element.
Diagnoses: The boundary was not TRACED while composing — a classic construction defect that a
           single predicted-then-run step at the boundary would have caught. (A1/A3 tracing +
           B3 boundary-value analysis.)
Example trigger: chunk with range(len(xs)//k) dropping the remainder; an "inclusive" range
                 built with range(a, b) that drops b.

Error: The spec says "return a NEW list/dict," but the learner mutates the argument in place
       (sort the input, append to a passed-in list) and returns it.
Diagnoses: Rebinding-vs-mutation surfacing from the AUTHOR's side (A1 / Finding 1) — an
           in-place operation violates a "return a new X / leave the input untouched"
           contract, and aliasing means the caller's object changes under them.
Example trigger: a spec requiring a non-mutating transform; the learner calls xs.sort() (in
                 place) instead of sorted(xs), or appends to the input list.

Error: Over-engineers — adds handling for inputs the spec EXCLUDES, generalizes prematurely,
       or builds configuration the contract never asked for.
Diagnoses: Composing PAST the contract (corollary 3) — every extra branch is more surface to
           verify and more to get wrong, and it obscures the piece that matters. The spec is
           the boundary; stop at it. (Craft; the "better not perfect / simple interface"
           lens of D1, applied to writing.)
Example trigger: a clamp(x, lo, hi) spec answered with a configurable multi-mode clamper that
                 also validates types and logs -- none of which the spec requested.
```

### 5d. Grading mode

**Two-tracked — executable product + rubric process — declared up front**
(`drill-generation.md` §1d, §2, §3). This is the most executable module in its cluster; the
*written function* has computable ground truth, but the *composition process* does not.

**The grading procedure, concretely:**

1. **Build the battery (never guess the expected outputs).** From the spec, enumerate the
   **happy-path** cases **and** the **edge** cases (empty · boundary · even/odd · duplicate ·
   degenerate — §5b). Compute each *expected* output by **running a reference solution** through
   `python <skill-dir>/runtime/python/runner.py snippet.py` — the gold is anchored to runner
   output, never to the coach's reading.

2. **Run the learner's function against the battery.** Execute the learner's code on each case
   via the runner; record **real per-case pass/fail** from `stdout` / `status` (an edge case may
   be `status: error` — e.g. an unguarded empty input raising). **Surface the evidence:** paste
   the cases you ran and their output into the reply (`coaching-loop.md` → Surface ground truth)
   — a hidden run reads as a guessed answer key.

3. **Report the executable verdict, happy vs edge separately.** "Passes all happy-path cases;
   **fails the even-length edge** (`median([4,1,2,3])` returned `3`, battery expected `2.5`)."

4. **Grade the process against the rubric (§7).** Three criteria (binary): (a) **Spec stated /
   edge named *before* coding?** (b) **Built in verified steps** — composed and confirmed small
   pieces, predicting before running — rather than one big-bang block? (c) **Stopped at the
   contract** — neither happy-path-only nor over-engineered? Cite the closest golden exemplar.

5. **Report the two verdicts separately, and name the soft one as soft.** The coach says: *"the
   function's pass/fail is machine-verified; the *process* grade is a judgment call against the
   rubric + exemplars, softer than the executable pass"* (`drill-generation.md` §3). A function
   that **passes the full battery but was written big-bang with no incremental verification**, or
   that **passes only the happy path**, is a **partial pass** and the coach flags exactly which
   half fell short — because B2's whole thesis is that the *confirmed-step process*, not just the
   final green, is the skill (Finding 6: the intermediate skills predict writing).

6. **The battery is a falsifier, not a proof.** Passing every prepared case is **necessary, not
   sufficient** — "program testing can be used to show the presence of bugs, but never to show
   their absence" (Dijkstra; `evidence-base.md` → B3a). The coach states this out loud and never
   upgrades "passed the battery" to "provably correct." A learner who concludes "all green, so
   it's correct" has made a scored error (the B3 "coverage is not correctness" trap, surfacing in
   composition).

B2 drills are thus **hybrid the executable way**: the *product* is the firmer, machine-checked
verdict; the *process* is the softer, rubric-graded one. Report both, weight transfer (§9)
heavily, and never let a green battery stand in for a confirmed process.

---

## 6. Frontier band

Frontier is not a fixed tier — it tracks the learner's **demonstrated ceiling** and presses
**one step** past their last comfortable success along a single parameter axis
(`drill-generation.md` §5). Escalating two steps collapses to failure; escalating none loses
the desirable-difficulty benefit.

**What "one step" means here** (per `drill-generation.md` §5):
- **Advanced** = compose a function with **two interacting sub-behaviors** (or a contract
  decision), passing the full edge battery and explaining the composition.
- **Frontier-N** = N increments beyond Advanced; **each increment adds exactly one** new
  interacting piece OR pushes one parameter-space dimension up one notch (one more edge class,
  one more sub-function, a stateful invariant, a property instead of examples).
- The learner's current Frontier-N is the highest N they have passed.

Escalation directions beyond Advanced for B2, with step counts:

1. **More interacting pieces** (push the composition-depth dimension):
   - Frontier-1: a third sub-behavior on top of the two (e.g. `parse_kv` → **typed** values:
     parse + coerce-to-int-or-keep-string + build, with a malformed-number contract) — Advanced
     + 1 piece.
   - Frontier-2: the above where the pieces **share state** — a small **class** with an
     invariant maintained across methods (a running-statistics accumulator: `add` then `mean`
     then `reset`, the invariant being count/total consistency) (+ 1).
   - Frontier-3: the class plus a method whose **contract interacts** with another (`undo` that
     must restore the exact prior state) (+ 1). Each added interacting piece is one increment.

2. **More edge classes that interact** (push the hidden-edge dimension): a single spec where
   **empty AND ties AND a boundary** all matter at once (e.g. "top-k by frequency, ties broken by
   first occurrence, k larger than the number of distinct values, empty input") — each additional
   *interacting* edge class is one increment over the single-edge Working drill.

3. **Compose against a property, not examples** (push from example-batteries toward invariants):
   the output must satisfy a **property for all inputs** — `merge_sorted(a, b)` must be sorted
   **and** a permutation of `a + b`; a `roundtrip` where `decode(encode(x)) == x`. The learner
   composes toward the invariant and the coach checks it on generated inputs (ties to **B3**'s
   property-based testing). One increment.

4. **Compose the verifier, not just the code** — the **AI-era frontier**: given an agent-drafted
   function that *looks* correct, the learner's job is to **write the spec and the battery that
   pins it** and find the input that breaks it (ties **B3** and **E3**; `evidence-base.md` →
   AI-era impact). One increment for "verify code you did not write," another for "and the code
   reads fluent and confident, so do not rubber-stamp it."

Track the level as `B2: Frontier-N`. Reset condition: two consecutive failures at the same
level → drop to Advanced for one drill, then re-approach (`drill-generation.md` §5).

---

## 7. Mastery rubric

The observable per-tier bars, instantiating the rubric shape of `assessment.md` Part 2, scored
on **both** verdicts (executable product + rubric process). Two cross-cutting requirements apply
at every tier above Foundations: **product *and* process** (the battery passes — *including the
edge cases* — **and** the function was composed in verified steps, stopping at the contract; a
green battery from a big-bang write, or a happy-path-only pass, is a Foundations-level pass at
best), and **unaided + durable** (a same-session streak is provisional until a delayed
re-assessment or the real-code transfer task confirms it; `assessment.md` Parts 3–5).

| Tier | Observable bar for B2 |
|---|---|
| **Foundations** | Writes a **single-behavior** function (familiar surface) that **passes the happy-path battery** when run, built with at least one confirmed intermediate step (not a guess pasted whole). Allowed *with* the worked example faded to one missing step. The signature pass is **runnable, correct code on the typical cases** — edge handling may be gentle or scaffolded. |
| **Working** | On **unseen specs that hide one naive-misses-it edge case**, **unaided**: **names the edge case before coding**, builds the function in **verified steps**, and **passes the full battery including the edge** (e.g. `median([4,1,2,3]) == 2.5`, `truncate("hi",5) == "hi"`, the `chunk` remainder kept). Passing only the happy path, or passing the full battery but composing big-bang, is a **partial pass — flagged on the half that fell short**. On 3 of 4 such unseen drills. |
| **Advanced** | On a spec requiring **two or more composed sub-behaviors or a contract decision**, **unaided**: composes in verified steps, **passes the full battery**, makes and **justifies the contract** for the edge inputs (what empty / malformed returns and why), does **not** over-engineer past the spec, **and explains the composition** on a teach-it-back (`drill-generation.md` §6) — *why each step, why this contract* — not just the instance. |
| **Frontier** | `Frontier-N`: presses one step past the last comfortable success per §6 / `drill-generation.md` §5 (more interacting pieces → interacting edge classes → a property → verifying agent-drafted code). A moving target, not a fixed bar. |

Promotion is by **performance, not tenure** (`assessment.md` rule 1); the coach marks a tier
from what the learner *does* on unseen specs — specifically from **the edge cases passing *and*
the confirmed-step process**, never from a happy-path green alone and never from claimed
seniority. Held-out re-assessment and real-code transfer outrank a same-session streak
(`assessment.md` Part 5). This product-*and*-process bar is doing real work: Finding 6's whole
point is that the *intermediate* skills — being able to predict and confirm each piece — are
what underlie reliable writing, so a function that happens to pass without a confirmed process is
not yet evidence of the skill.

---

## 8. Anti-patterns & evidence caveat

**Anti-patterns this module exists to break** (each is a catalog entry in §5c, surfaced as a
*behavior*):

- **Big-bang writing.** Composing the whole function and running it once at the end, so a
  failure could be anywhere. The fix is mechanical: **write the smallest runnable piece, predict
  it, run it, confirm it, then extend.** The unit of progress is the *confirmed step*.
- **Happy-path-only composition.** Coding the typical example and silently missing the empty /
  boundary / even / duplicate case the spec implies. The function is *unfinished*. The fix:
  **name the edge cases before you write** (the B3 hinge), and compose toward the full contract.
- **Coding before stating the spec.** Translating linearly into syntax without restating the
  contract — the novice signature (Finding 5). The fix: **explain it before you write it** (the
  writing-end of Finding 6); you cannot reliably write what you cannot articulate.
- **Running without predicting.** Using the runner to *discover* the answer instead of to
  *confirm a prediction*. A green run you did not predict is weak evidence. The fix: **trace your
  own piece first** (A3), then run to confirm.
- **Building on an unconfirmed step.** Extending a piece you never ran, so the bug compounds.
  The fix: never build on a line you have not confirmed — *written is not working.*
- **Mutating the input when a new object was specified / over-engineering past the spec.** An
  in-place op that violates a "return a new X" contract (A1 rebind-vs-mutate from the author's
  side), or speculative generality the contract never asked for. The fix: honor the exact
  contract — **stop at the spec's boundary.**

**Evidence caveat (this is a `[Verified-adjacent] + [Practitioner-canon]` module — say so).**
Unlike the pure-`[Verified]` Track-A modules, B2's grounding is **mixed and must not be
oversold:**

- The **concept** (writing sits atop a reading → tracing → writing hierarchy and rests on the
  intermediate skills) is **`[Verified-adjacent]`** — Finding 6 is a **verified *correlational*
  hierarchy** (Lopez et al. 2008: ~46% combined variance; Lister, Fidge & Teague 2009:
  replication). **The coach must NOT claim that drilling tracing *causally* improves writing.**
  The causal arrow is **open**, and Lister, Fidge & Teague (2009) document an **explicit
  exception** — a student who wrote well despite failing both tracing and explaining. State it
  as *"strongly associated with, and developmentally prior to, writing — not a proven causal
  lever."*
- The **method** (compose in small verified steps) is **`[Practitioner-canon]`** — respected
  incremental-development craft, **practitioner consensus, not science.** Its **one empirical
  hint** — Fucci et al. 2017's "granularity and uniformity (small, steady steps) mattered more
  than the test-first ritual" — sits in the **contested TDD evidence layer** (`evidence-base.md`
  → B3b; Turhan et al. 2010; Rafique & Mišić 2013) and is **suggestive, not proof.** The coach
  never sells "build in small steps" as a measured causal win.
- The **battery is a falsifier, not a proof** (Dijkstra; `evidence-base.md` → B3a): passing every
  prepared case is **necessary, not sufficient.** The coach never upgrades "passed the battery"
  to "provably correct," and "high coverage ≠ correct" (Inozemtseva & Holmes 2014, B3b) applies.
- The **curriculum-wide transfer caveat** applies in full: the BRACElet evidence is from *novices
  in introductory courses*; that composing-in-verified-steps *causally* improves *experienced*
  engineers is the open question. The coach leans on the transfer task (§9) — the skill on the
  learner's **own** code — as the honest individual-level evidence.
- The **AI-era weighting** (composition turning outward into specification + verification as
  agents draft code; `evidence-base.md` → AI-era impact) is **`[Verified-adjacent]` priority-
  steering, not proof** — the productivity data is partly contested and vendor-sourced; the
  load-bearing claim is the small-N RCT and the CS-education consensus on specification +
  verification.

No claim in this module is dressed above its badge.

---

## 9. Transfer task

**The only honest test of whether the gym drill transferred to the job is composing against the
learner's own real code** (`assessment.md` Part 4; `evidence-base.md` → transfer caveat,
consequence 2).

> **Your turn:** Pick a **small function you are about to write (or recently wrote) in your own
> codebase** — ideally one with at least one non-obvious edge case, or one a coding agent
> drafted that you have not yet verified. Keep it small enough to compose in a sitting.
>
> Then run the loop **out loud**:
> 1. **State the spec and its edge cases** — what must it do, and what should it do on the
>    empty / boundary / degenerate / duplicate input? Decide the contract *before* writing.
> 2. **Compose in verified steps** — write the smallest runnable piece, **predict** what it does
>    on a concrete input, **run** it (reduce to a runnable snippet if needed) to confirm, **then
>    extend.** Keep going until every piece is a confirmed point.
> 3. **Run your own battery** — the happy path **and** the edge cases you named. If a case fails,
>    note *which step* the gap is in (the verified-steps process should localize it). If the code
>    was agent-drafted, your job is to **write the battery that pins it** and find the input that
>    breaks it.
>
> Then step back: **did you write the whole thing and hope, or did you confirm each step? Did the
> edge case you named show up in your battery — or did you discover it only when something broke?**
> If you wrote big-bang and the edge surfaced late, that is the exact gap this module targets.

**Grading is softer and named as such** (`assessment.md` Part 4). Real code has no clean answer
key for the *process*; the coach grades the composition against the §7 rubric and says: *"this is
a judgment call on your real code, not a machine-verifiable result."* But the **product half stays
executable**: where the learner's function (or a reduced version) **is runnable**, the coach
**uses the runner** — builds the battery, runs the learner's code against it, and reports real
pass/fail before discussing it (the same discipline as §5d, now on the learner's real function).
**Transfer evidence is weighted heavily:** a learner who passes generated drills but, on their own
code, writes big-bang and ships the edge-case bug — or cannot state the spec before writing — has
**not** transferred the skill, and the tracker notes that gap as more diagnostic than another
passed synthetic drill. This task is also the **AI-era** move in miniature: writing the spec and
the verifying battery for code you did not fully author is precisely the composition-turned-
verification skill the AI era rewards (`evidence-base.md` → AI-era impact).

---

## Cross-references

- Drill mechanics, the **Generation → Comparison** and **Completion-prompt** formats, the
  executable ground-truth protocol (build the battery, run the learner's function, surface the
  output), Frontier escalation: `references/drill-generation.md` (this module instantiates §1 and
  follows §2, §3, §4, §5).
- Session delivery (pause/no-spoiler hard stop, tier-faded worked example, **surface the battery
  output**, direct feedback, scaffolding ladder): `references/coaching-loop.md`.
- B2 entry task, per-skill routing (incl. the **"if B2 weak and A3 weak, note tracing underlies
  it"** signal), mastery-rubric shape, held-out re-assessment, real-code transfer weighting:
  `references/assessment.md` (the B2 entry task — write a small function to a spec with an edge
  case a naive version misses; "correct on the happy path only → Working; correct including the
  edge, with clean composition → Advanced").
- The **tracing & explaining** skills writing rests on (predict your own piece; state the
  purpose): `modules/A3-execution-tracing.md` (B2 operates A3 outward, on code being produced —
  it does not re-teach it). The **decomposition** that precedes the first line:
  `modules/B1-*` (what the pieces are). The **battery** B2 is graded against and the edge-case
  enumeration B2 composes toward: `modules/B3-testing-and-correctness.md`. The **rebinding-vs-
  mutation** contract ("return a new X"): `modules/A1-notional-machine.md`.
- Evidence grounding (Finding 6 — reading → tracing → writing, Lopez et al. 2008, Lister, Fidge &
  Teague 2009 with the explicit exception; the build-in-steps **method** as `[Practitioner-canon]`
  incremental-development craft with one **contested** empirical hint, Fucci et al. 2017 in the
  B3b TDD layer; Dijkstra's "presence not absence"; the transfer caveat; the AI-era
  specification-and-verification priority): `references/evidence-base.md`.
- Golden exemplars (~3 per tier, every battery **runner-verified**, the composition process
  graded against the rubric + gold): `exemplars/B2/foundations.md`, `exemplars/B2/working.md`,
  `exemplars/B2/advanced.md`.
