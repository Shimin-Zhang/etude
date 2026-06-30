# E3 — Code Review as a Skill `[Practitioner-canon]`

> **Module type.** `[Some empirical] + [Canon]` — a **judgment module**. Its concept is
> partly empirical (Bacchelli & Bird 2013, the one in-depth field study of modern code
> review) and partly practitioner canon (Google's eng-practices; Weinberg's egoless
> review). There is **no executable ground truth for "review quality"** — a review is
> graded against a **rubric + golden exemplars**, not by running it. (The validator badge
> on this file is `[Practitioner-canon]`; the honest prose badge is `[Some empirical] +
> [Canon]`.)
>
> **Core idea.** A code review is **reading + judgment + communication**. The skill is to
> understand the change well enough to find the *important* issue, decide what actually
> matters, and say it precisely, actionably, and kindly — **not** to flag every nit while
> the real defect sails through. Finding the most-consequential issue and communicating it
> well beats comment volume.

---

## 1. Evidence basis `[Some empirical] + [Canon]`

This module is **mixed-status** by design, and the coach must never present its canon half
as verified science (`evidence-base.md` → badge rules). Two pillars:

**(a) The empirical half — Bacchelli & Bird 2013 `[Some empirical]`.** Cite via
`evidence-base.md` → AI-era section ("Review is the new bottleneck"; the paper is named
there as the prior empirical grounding for code review). The study is *Expectations,
Outcomes, and Challenges of Modern Code Review* (ICSE 2013): an in-depth, mixed-method
field study at Microsoft — 17 developers observed and interviewed, **570 review comments
card-sorted**, surveys of **165 managers and 873 programmers** on the CodeFlow tool. Its
findings ground this module's whole stance:

- **The expectation/outcome gap.** *Finding defects* is the **top motivation** (the first
  reason for review for 44% of surveyed programmers) — but in practice defects are only the
  **4th most frequent** kind of comment, **14% (78 of 570)**. The most frequent category is
  **code improvement, 29%**, then **understanding**, then social communication. So the thing
  reviewers *say* review is for is not the thing review mostly *produces*.
- **Most found defects are "micro."** Of those 78 defect comments, **65 were small logical
  issues** (corner cases, comparison values, operator precedence), 6 high-level, 5 security,
  3 exception handling. The paper's own words: review "**more rarely detects deep, subtle,
  or 'macro' level issues. Relying on code review in this way for quality assurance may be
  fraught.**" Defect-finding is **harder than expected**, not the easy win.
- **The real value is understanding and knowledge transfer.** The paper's headline:
  "**code and change understanding is the key aspect of code reviewing**" — and *understanding
  the reason for the change* is reviewers' **single biggest challenge** ("the most difficult
  thing when doing a code review is understanding the reason of the change"). 91% of
  programmers said reviewing **unfamiliar** files takes longer; 82% said a reviewer who
  *understands* the change gives **deeper** feedback.
- **Understanding changes the feedback you give.** When understanding is high (e.g., the
  reviewer owns the file), comments are "**more conceptual (better ideas, approaches)
  instead of superficial (naming, mechanical style, etc.)**," "**more actionable and
  pertinent**," and "**more likely to find subtle defects**." When it is low, reviewers fall
  back on what is easy to see — style and formatting. One interviewee's warning is the
  anti-pattern this module targets: "**I've seen quite a few code reviews where someone
  commented on formatting while missing the fact that there were security issues or data
  model issues.**" Another: some reviewers "focus on formatting mistakes because they are
  easy […] but it doesn't really help."

**(b) The canon half — effective-review practice `[Canon]`.** Vetted during authoring
against the named sources; craft wisdom, not empirical findings:

- **Google's *eng-practices* — "The Standard of Code Review."** "The primary purpose of code
  review is to make sure that the overall code health of the codebase is improving over
  time." "**There is no such thing as 'perfect' code — there is only better code.**"
  Reviewers approve once a change **definitely improves code health**, even if imperfect —
  "continuous improvement," not perfection. "**Technical facts and data overrule opinions and
  personal preferences.**" Comment **on the code, never on the developer**; call out what is
  *good*, not only what is wrong; prefix non-blocking polish with "**Nit:**." What reviewers
  look at: **design, functionality, complexity, tests, naming, comments, style** — *in that
  priority*, design first.
- **Weinberg, *The Psychology of Computer Programming* (1971) — egoless programming**
  (`evidence-base.md` → reading spine). Review is a social act; the author's worth is not on
  trial; feedback attacks the code, not the person. This is the communication half of the
  skill.

**Why these license this module.** Bacchelli & Bird is the empirical anchor for the *what*
(review is understanding; the easy-style-nit trap is real and named by practitioners; deep
defects are hard); Google + Weinberg are the canon anchors for the *how* (prioritize code
health and design, give precise/actionable/kind feedback, don't gate on perfection). The
combined claim this module teaches: **a good review understands the change, prioritizes the
issue that matters most, and communicates it precisely and kindly.**

**Read through the transfer caveat.** Bacchelli & Bird is a **single-company qualitative
study** (Microsoft, 2013); the canon sources are **craft wisdom, not measured causation**.
The *direction* is well grounded; that drilling review on synthetic diffs *causally* improves
a given engineer's real-PR reviewing is the open question every module here carries
(`evidence-base.md` → transfer caveat). The transfer task (§9) — reviewing a **real PR** — is
the honest individual-level test. **AI-era note:** as agents draft most first-draft code,
review load rises and review becomes the apex verification skill (`evidence-base.md` → AI-era
section; spec §12) — `[Verified-adjacent]` as a *priority*, not proof.

---

## 2. Soft prerequisites

**A2 (code reading & chunking) recommended.** You cannot review what you cannot read: the
empirical core of this module is that *understanding the change is the bottleneck*, and A2 is
the skill of building that understanding fast (chunking, beacons, reading for structure). A
reviewer who narrates a diff line-by-line without a whole-change model is doing the A2 gap
**inside** a review. **A1 (notional machine)** and **A3 (tracing)** help for the same reason —
several planted bugs here (aliasing, mutable defaults, evaluation order) are A1 execution-model
events seen in someone else's code; **C2 (reading stack traces)** helps when a review includes
a failing test.

Per `assessment.md`, soft prerequisites **inform, never gate** — the buffet rule holds (any
learner may open any module at any tier). If a learner flails at E3 because they cannot grasp
the diff, the coach notes the gap likely traces to A2/A3 and *suggests* shoring those up — but
does not forbid E3. Conversely, E3 is itself a **soft prerequisite signal** the other way: a
learner strong on reading but weak on *prioritization and feedback* is exactly who E3 is for.

---

## 3. The mental model

**A code review is reading + judgment + communication.** You read the change until you
understand *what it does and why it exists*; you exercise judgment to decide *which issue
matters most*; you communicate that issue *precisely, actionably, and kindly*. The failure
mode is not "missed a typo" — it is **bikeshedding the style while the real defect ships**.

Three moves, in order. They are a pipeline: a miss at an earlier stage poisons the later ones.

| Move | What it is | What goes wrong without it |
|---|---|---|
| **1. Understand the change** | Build a whole-change model: what is the diff trying to do, why does it exist, what is the contract of the code it touches, what inputs flow through it? Read the *whole change*, not line-by-line in isolation. **Run it / trace it** where you can. | You review the lines you can see and miss the ones you can't reason about. Bacchelli & Bird: low understanding ⇒ reviewers retreat to easy, superficial style comments and miss the deep issue. This is the **#1 empirical challenge**. |
| **2. Judge what matters** | Triage the issues you find by **consequence**: correctness/security/data-loss first; design/maintainability next; style/nits last. Pick the **most important** thing. Not every observation is a comment; not every comment blocks merge. | You produce 20 naming nits and zero mention of the money bug. "There is only better code" — but *which* better matters: a reviewer who fixes the spelling while the off-by-one ships has inverted the priority. |
| **3. Communicate precisely & kindly** | For the issue that matters: **reference the exact line**, **explain the impact** (what breaks, for whom, when), **suggest a fix or a question**. Comment on the **code, not the person** (egoless). Separate **blocking** from **Nit:**. State facts, not preferences. | Vague feedback ("this feels off," "clean this up") gives the author nothing to act on and erodes the relationship. A correct catch, badly phrased, is half a review. |

**The discipline in one line: *find the issue that matters, and say it so the author can act on it.*** Three corollaries the module drills:

1. **Prioritize by consequence, not by how easy it was to spot.** The easiest issues to *see*
   (style, formatting) are usually the least important; the issues that *matter*
   (correctness, security, edge cases, races) take understanding to find. Bacchelli & Bird's
   central caution: do not let "easy to comment on" stand in for "worth commenting on."
2. **Don't gate on perfection.** Approve a change that **definitely improves code health**
   even if imperfect (Google). The point is *better*, not *perfect* — but "better" is judged
   on the consequential axis, not the cosmetic one.
3. **Precise + actionable + kind are one bundle, not three nice-to-haves.** *Precise*: name
   the line and the exact condition. *Actionable*: say what would fix it (or ask the question
   that surfaces the fix). *Kind*: attack the code, credit the good, assume competence
   (egoless review). A comment missing any one of these is weaker than it looks.

---

## 4. Worked example — a review of a small diff, prioritized

*(Foundations depth: the full review shown — issues found, triaged, and one model comment.
This fades by tier; see the note after the example.)*

The skill is to **review like a senior reviewer**: understand the change, list every issue,
**rank them by consequence**, then write a precise comment on the one that matters. Consider
this diff (a helper that prices a cart):

```python
def cart_total(cart, discount_pct):
    t = 0
    for i in cart:
        t = t + i["price"] * i["qty"]
    t = t - t * discount_pct / 100
    return round(t)
```

**Step 1 — Understand the change.** Contract (from the spec): given a cart of
`{"price", "qty"}` items and a percent discount, return the **total after discount, in
dollars-and-cents**. Money. So the output must keep 2 decimal places.

**Step 2 — List issues, then rank by consequence** (this is the judgment move):

| # | Issue | Severity | Why |
|---|---|---|---|
| 1 | `return round(t)` rounds to **whole dollars**, silently dropping the cents (`round(x)` with no `ndigits` returns an int). | **Blocking (correctness)** | A money function that loses cents is wrong. `cart_total([...], 10)` returns `22`, not `22.03`. **Verified by running** (see ground truth). |
| 2 | Discount has **no range guard** and the rounding/discount logic is inlined with a magic `100`. | Design smell | A `discount_pct` of `150` silently yields a negative total; the pricing rule isn't isolated or testable. Worth a comment, not a block. |
| 3 | `t` and `i` are uninformative names (`i` is a *dict*, not an index). | Nit | Readability only. Does not change behavior. |

**Step 3 — The model comment** (precise · references the line · explains impact · suggests a
fix · kind). Lead with the issue that matters; the nits go *after*, clearly marked:

> **`return round(t)` (line 6) — blocking.** This rounds the total to whole dollars and drops
> the cents, because `round(x)` with no second argument returns an `int`. For
> `cart_total([{"price": 9.99, "qty": 2}, {"price": 4.50, "qty": 1}], 10)` it returns `22`
> instead of `22.03` — a real money bug. Suggest `return round(t, 2)` (and a quick test
> asserting the cents survive).
>
> Two smaller things, non-blocking:
> **Nit:** consider guarding `discount_pct` to `[0, 100]` (or documenting that callers
> pre-validate) — right now `discount_pct=150` returns a negative total.
> **Nit:** `i` is a dict here, not an index — `item` would read clearer.
>
> The loop and the discount math themselves look right. Nice and compact.

**Verified ground truth** (the coach *runs* the buggy snippet to confirm the catch is real,
exactly as for executable drills — `drill-generation.md` §2 — even though the *review* is
rubric-graded):

```
buggy:   cart_total([{"price":9.99,"qty":2},{"price":4.50,"qty":1}], 10)
  stdout (demonstration): cart_total = 22   (spec wants 22.03)
with the suggested fix `round(t, 2)`:
  stdout (demonstration): fixed cart_total = 22.03
  status: ok
```

**What the example makes visible** (and a line-by-line skim hides): the *most important* issue
(lost cents) is **invisible without understanding the contract** (that this is money). A
reviewer who lacked that understanding would land on the names (`t`, `i`) — the easy,
superficial comments Bacchelli & Bird describe — and **ship the money bug**. Prioritization is
not politeness; it is the core of the skill. And the comment *earns its keep* by being
precise (names the line and the exact int-vs-float cause), actionable (gives the one-line
fix), and kind (credits what's right, marks nits as nits).

> **Expertise reversal — the example fades by tier.** Per the worked-examples finding
> (`evidence-base.md` → instructional pillar; `coaching-loop.md` Step 2), a fully worked
> review helps **novices** (it shows the triage move) but is **redundant load for the more
> advanced**, who learn more by triaging themselves. So the coach fades it:
>
> | Tier | Worked-example depth at E3 |
> |---|---|
> | **Foundations** | **Full** — the complete issue table and model comment above, every step shown. |
> | **Working** | **Partial** — coach names the issues found but leaves the **ranking** and the **comment** for the learner to produce. |
> | **Advanced** | **Skeleton** — coach hands over the diff and the rubric only; learner finds, triages, and writes the comment unaided. |
> | **Frontier** | **None** — straight to the diff (§6). |

---

## 5. Drill-generation spec

Instantiates the generation-spec format of `drill-generation.md` §1 for E3. Grading mode is
declared up front: **rubric + golden exemplars** (§5d) — this is a judgment module, not an
executable one. (The *planted bug's misbehavior* is still confirmed by running it; the
*review* is graded against the rubric.)

### 5a. Tier definitions (E3-specific)

The curriculum-wide tier names (`drill-generation.md` §1a) translated to this module. **Every
drill is a small diff/function to review** (a "Debug-this"/review format, `drill-generation.md`
§6), and **every drill has exactly one planted issue verified by running it** (plus, at
Working/Advanced, decoy nits/smells):

| Tier | E3 criterion | Example shape |
|---|---|---|
| **Foundations** | One **clear** planted bug on a familiar surface (off-by-one, wrong boundary operator, wrong slice). **Find it and explain why it's wrong.** No decoys; the skill is *catching the defect and articulating impact*. | A loop summing an "inclusive" range with `range(a, b)`; predict that the upper bound is dropped. |
| **Working** | A **mix**: one real **correctness bug** + a **style nit** + a **design smell** in the same ~10–20-line diff. **Prioritize the correctness bug**, give precise/kind feedback on each, mark nits as nits. The skill is *triage + communication*, not just spotting. | A cart-pricing function with a money-rounding bug, a single-letter name, and an inlined magic number. |
| **Advanced** | A **subtle** correctness / security / concurrency / edge-case bug **hidden among plausible code** that looks correct and survives shallow testing. **Find it, articulate the impact, propose a fix.** | A bisect-left with a broken `hi` update that passes on the extremes but fails interior targets; a path-join with no containment check; a non-atomic counter. |
| **Frontier** | See §6 — one step past the learner's last comfortable success. | — |

A drill is mis-tiered if a Foundations diff hides its bug among decoys, or a Working diff has
no genuine nit/smell to *de*-prioritize, or an Advanced bug is obvious on a skim. Apply the
self-check (`drill-generation.md` §4) and re-level before posing.

### 5b. Parameter space (axes the coach varies to avoid mode-collapse)

Pick a *different point on each axis* across successive drills (`drill-generation.md` §1b, §4
check 3). The axes for E3:

- **Bug class** — off-by-one / boundary · wrong operator or comparison · wrong slice/index ·
  silent type/precision loss (e.g. `round` to int) · truthiness swallowing falsy values ·
  mutable-default / aliasing / caller mutation · broken loop or search **invariant** ·
  **security** (path traversal, injection, unsafe deserialization, missing authz check) ·
  **concurrency** (race / lost update / non-atomic read-modify-write) · **edge case**
  (empty / single / duplicate / boundary input the code mishandles) · resource leak
  (unclosed file/handle).
- **Decoy mix** (the judgment axis) — none (Foundations) · one nit · one design smell · a nit
  **and** a smell that *tempt the reviewer away* from the real bug (Working/Advanced). The
  decoys must be *plausible* things a real reviewer would notice.
- **Surface** — a standalone function · a small diff/patch (added/changed lines marked) · a
  function plus a failing test · a function plus its call site.
- **What the review must produce** — *catch + explain* (Foundations) · *triage (rank) +
  comment on each* (Working) · *catch the hidden issue + impact + proposed fix* (Advanced) ·
  *plus a teach-it-back of the review principle* (Advanced/Frontier).
- **Communication target** — the model comment must hit: references the **line**; states the
  **impact**; proposes a **fix or question**; **kind / egoless** tone; **blocking vs Nit:**
  separation. Vary which of these the drill stresses.
- **Format** (`drill-generation.md` §6) — primarily **Debug-this** (review a planted-bug
  diff); also **Generation → Comparison** (learner writes the review, coach reveals the gold),
  **Teach-it-back** (articulate the prioritization principle), and **Error analysis** (here is
  a *weak review someone wrote* — what did it miss / mis-prioritize?).

Keep an in-session log of the `(bug class, decoy mix, surface, format)` tuples used; do not
repeat a tuple until the others are exercised.

### 5c. Common-error catalog

The *specific* review failures, each with the conceptual gap it diagnoses
(`drill-generation.md` §1c format). These are grounded in **real review failures** documented
by Bacchelli & Bird 2013 and the effective-review canon (Google eng-practices; Greiler;
egoless review), not in trivia. **The root of most of them is one inversion: spending the
review on what is *easy to see* (style) instead of what *matters* (correctness / design),
because the reviewer did not invest in *understanding the change*.**

```
Error: Rubber-stamps — approves with "LGTM" / a trivial nit, having found no substantive
       issue, when a real correctness/security/edge-case bug is present.
Diagnoses: Did not actually review — skimmed for surface plausibility without building a
           whole-change model or running/tracing the change. The defect was findable; the
           reviewer did not look. (Bacchelli & Bird: low understanding ⇒ shallow review;
           Google: review exists to improve code health, not to wave changes through.)
Example trigger: any Advanced diff whose bug needs understanding the invariant/contract
                 (bisect `hi` update; path containment; non-atomic counter).

Error: Nitpicks style while missing the design/correctness issue — files multiple comments
       on naming/formatting/whitespace and never mentions the money bug / race / security
       hole sitting in the same diff.
Diagnoses: Inverted priority — commented on what was EASY to spot instead of what MATTERS.
           The signature failure of code review. (Bacchelli & Bird, verbatim: "commented on
           formatting while missing the fact that there were security issues or data model
           issues"; reviewers "focus on formatting mistakes because they are easy [...] but
           it doesn't really help.")
Example trigger: any Working diff (correctness bug + nit + smell) where the learner leads
                 with — or stops at — the nit.

Error: Gives vague feedback — "this is confusing," "clean this up," "feels off," "could be
       better" — with no line, no impact, no suggested change.
Diagnoses: Communication failure: not actionable. The author cannot act on it and cannot
           tell whether it blocks. Precise+actionable is half the skill, not a finishing
           polish. (Google: be clear and helpful; technical facts over vague opinion.)
Example trigger: a learner who identifies the right region but writes "the discount logic
                 looks wrong somewhere" instead of naming line and cause.

Error: Did not run or trace the change — asserts a bug that isn't one, or misses a bug that
       only shows on a specific input, because they reasoned about the code in their head and
       guessed.
Diagnoses: Skipped the executable check the change invited. Review of testable code without
           running/tracing it is guessing. (A1/A3 gap surfacing inside review; Bacchelli &
           Bird: understanding the change, often by running it, is the key aspect.)
Example trigger: Advanced bugs that pass on the obvious inputs and fail on interior/edge
                 ones (the bisect drill passes on 0 and 8; fails on 4 and 5).

Error: Reviews line-by-line without a whole-change model — comments locally on each changed
       line but never reasons about the change's overall behavior, contract, or interaction
       with its callers, so a cross-line or contract-level bug is invisible.
Diagnoses: No A2-style chunking of the change; treats a diff as independent lines, not as
           one coherent edit with a purpose. (Bacchelli & Bird: "the most difficult thing
           [...] is understanding the reason of the change"; A2 chunking gap.)
Example trigger: the cart drill (the bug is a contract violation — "this is money" — not a
                 bad single line) or the merge-defaults drill (the bug spans calls).

Error: Bikesheds / demands perfection — blocks the change over personal style preferences or
       a rewrite the reviewer would have done differently, with no technical basis.
Diagnoses: "Perfect" instead of "better"; opinion presented as a blocker. (Google: "there is
           no such thing as perfect code — only better code"; "technical facts and data
           overrule opinions and personal preferences"; defer on pure preference.)
Example trigger: a learner who blocks a correct, improving diff to impose a preferred idiom,
                 or escalates a true Nit to blocking.

Error: Attacks the author, not the code — "you always do this," "why would you write it this
       way," "did you even test this?"
Diagnoses: Non-egoless review; makes the person the subject. Erodes the relationship and the
           willingness to act on the feedback, independent of whether the catch is right.
           (Weinberg, egoless programming; Google: comment on the code, never the developer.)
Example trigger: any drill where the learner's catch is correct but the phrasing is hostile —
                 graded down on the communication dimension even though the issue is right.

Error: Over-reports / "finds" defects that aren't there — flags correct code as buggy to look
       thorough, or pads with low-value comments.
Diagnoses: Comment volume as a proxy for review quality. Bacchelli & Bird: deep defects are
           genuinely rare and hard; manufacturing findings wastes the author's time and
           buries the one comment that mattered. Catching what matters > comment count.
Example trigger: a learner who, on a Foundations single-bug diff, files five spurious
                 "issues" around the one real one.
```

### 5d. Grading mode

**Rubric + golden exemplars** (`drill-generation.md` §1d, §3). E3 has **no executable ground
truth for the review itself** — "is this a good review?" is a judgment, not a computation. The
coach grades a learner's review like this (the §3 judgment path, made concrete for E3):

1. **Run the planted bug first (the one executable sub-claim).** Although the *review* is
   rubric-graded, the **diff's bug is verified by running it** through
   `python <skill-dir>/runtime/python/runner.py snippet.py` (`drill-generation.md` §2). This
   establishes the ground truth of *what the correct review should catch* — the gold's
   prioritized list is anchored to runner output, never to the coach's guess. If the learner
   *disputes* whether something is a bug, the coach **runs it** and shows the evidence. (This
   is also how the coach grades a learner's *proposed fix*: apply it and re-run.)
2. **Score the review against the E3 rubric (§7), criterion by criterion** — *did they catch
   the most important issue? did they prioritize correctly (not bury it under nits)? is the
   feedback precise, actionable, and kind?* Each is a 3-point criterion (§7), graded
   explicitly, one by one.
3. **Cite the closest golden exemplar.** Compare the learner's review to the tier's golds in
   `exemplars/E3/<tier>.md` — "your review is close to the **weak** exemplar: you caught the
   bug but led with the naming nit" vs. "close to the **strong** exemplar: led with the
   correctness issue, named the line, gave a fix." The golds are the calibration anchor.
4. **Name it as soft.** The coach says out loud: "**this is a judgment call graded against the
   module's rubric + exemplars, not a machine-verifiable answer**" (`drill-generation.md` §3;
   `assessment.md` §1.2). Do **not** conflate a plausible review with a provably-correct one;
   rubric passes are **softer evidence** than executable passes.

E3 drills are thus **partly hybrid**: the *catch* ("is X actually a bug?") and the *fix* have
an executable sub-claim graded by the runner; the *prioritization* and *communication* are
rubric-graded. Report the verdicts separately — a learner who **catches** the bug (executable:
yes) but **buries it under nits** (rubric: poor prioritization) is a **partial pass**, and the
coach flags exactly that, because catching-without-prioritizing is the central E3 failure
(Bacchelli & Bird; §5c).

---

## 6. Frontier band

Frontier is not a fixed tier — it tracks the learner's **demonstrated ceiling** and presses
**one step** past their last comfortable success along a single parameter axis
(`drill-generation.md` §5). Escalating two steps collapses to failure; escalating none loses
the desirable-difficulty benefit.

**What "one step" means here** (per `drill-generation.md` §5):
- **Advanced** = one subtle hidden bug (correctness/security/concurrency/edge) among plausible
  code, found and explained with a proposed fix.
- **Frontier-N** = N increments beyond Advanced; each increment adds exactly one new
  dimension of difficulty OR pushes one parameter-space dimension up one notch.
- The learner's current Frontier-N is the highest N they have passed.

Escalation directions beyond Advanced for E3, with step counts:

1. **Subtler / costlier bug class** (push the bug-class axis): from a logic edge case →
   to a **security** bug (Frontier-1) → to a **concurrency** race that only manifests under
   contention (Frontier-2) → to a bug that is correct *in isolation* but wrong given the
   **caller's** assumptions / the surrounding system (Frontier-3). Each is one increment.

2. **More decoys, better camouflage** (push the decoy axis): the diff contains **two**
   plausible-but-minor issues and **one** that matters, and a *fourth* "issue" that is
   actually **correct code the learner must NOT flag** (testing over-reporting). Each added
   distractor that raises the triage difficulty is one increment.

3. **Bigger surface** (push the surface axis): from a single function → to a **multi-file
   diff** where the bug is an interaction between two changed files → to a change where the
   *right* review is "this is the wrong approach; here is the alternative" (Bacchelli & Bird's
   *alternative solutions* outcome), not a line fix. Each is one increment.

4. **Communication under tension** (push the communication axis): the correct review is one
   the author will resist — a **blocking** call on a change someone is attached to, or a
   **design** disagreement. The learner must hold the line on a technical fact **and** stay
   egoless and kind (Google conflict-resolution; Weinberg). Phrasing a hard "no" precisely and
   without ego is one increment over a friendly catch.

5. **Review of AI-generated code → the AI-era frontier.** A diff that *looks* fluent and
   idiomatic (as agent output does) but carries a plausible-surface defect — the spec-§12 apex
   skill. Verifying code one didn't write, that reads as confident, is the hardest review:
   one increment for "AI-plausible surface," another for "and you must not rubber-stamp the
   fluency." (Ties to F1 calibration — over-trusting fluent output is the documented AI-era
   miss.)

Track the level as `E3: Frontier-N`. Reset condition: two consecutive failures at the same
level → drop to Advanced for one drill, then re-approach (`drill-generation.md` §5).

---

## 7. Mastery rubric

The observable per-tier bars, instantiating the rubric shape of `assessment.md` Part 2, scored
against the three E3 dimensions. Two cross-cutting requirements apply at every tier above
Foundations: **product *and* process** (caught the right issue *and* prioritized + communicated
it well — a correct catch buried under nits, or phrased vaguely/harshly, is a Foundations-level
pass at best), and **unaided + durable** (a same-session streak is provisional until a delayed
re-assessment or the real-PR transfer task confirms it; `assessment.md` Parts 3–5).

**The three scored dimensions** (each 3-point: absent / partial / solid):

- **D1 — Catch (did they find the issue that matters?).** Did the review surface the
  consequential bug — not a decoy, not a hallucinated one? *(Executable sub-claim: the bug is
  confirmed real by the runner; §5d.)*
- **D2 — Prioritize (judgment).** Did they rank by consequence — lead with correctness/
  security, mark nits as nits, not block on perfection, not over-report?
- **D3 — Communicate (precise · actionable · kind).** Does the comment name the **line**,
  explain the **impact**, propose a **fix/question**, separate **blocking vs Nit:**, and attack
  the **code not the person**?

| Tier | Observable bar for E3 |
|---|---|
| **Foundations** | On a single-bug diff (no decoys), **catches the planted bug and explains *why* it's wrong** — names the defect and its impact (e.g., "`range(a, b)` drops the upper bound, so `sum_inclusive(1,5)` returns 10, not 15"). D1 solid; D3 at least partial (precise about the cause). Allowed *with* the worked example faded to one missing step. |
| **Working** | On a mixed diff (correctness bug + nit + smell), **unaided**: catches the correctness bug (D1), **prioritizes it above the nit/smell** (D2 — leads with it, marks nits as `Nit:`, doesn't gate on the smell), **and** writes a comment that names the line, gives the impact, and suggests a fix in a kind/egoless tone (D3). Buries the bug under nits ⇒ partial pass, flagged. On 3 of 4 such unseen drills. |
| **Advanced** | On a diff with a **subtle hidden** correctness/security/concurrency/edge bug among plausible code, **unaided**: finds it (D1), **articulates the impact precisely** and **proposes a working fix** (verified by the coach re-running with the fix), **and** does not over-report correct code (D2). Articulates the **underlying review principle** on a teach-it-back (`drill-generation.md` §6) — "prioritize by consequence; the easy-to-see issue is rarely the one that matters" — not just the instance. |
| **Frontier** | `Frontier-N`: presses one dimension past the last comfortable success per §6 / `drill-generation.md` §5 (subtler bug class → more/better-camouflaged decoys → multi-file surface → hard-news communication → AI-plausible code). A moving target, not a fixed bar. |

Promotion is by **performance, not tenure** (`assessment.md` rule 1); the coach marks a tier
from what the learner *does* on unseen review drills, never from claimed seniority or "I review
PRs all day." Held-out re-assessment and **real-PR transfer** outrank a same-session streak
(`assessment.md` Part 5) — and for a judgment module especially, the real-code signal is
weighted heavily (a clean synthetic-diff streak that doesn't show up on the learner's actual
PRs is not yet mastery).

---

## 8. Anti-patterns & evidence caveat

**Anti-patterns this module exists to break** (each is a catalog entry in §5c, surfaced as a
*behavior*):

- **Rubber-stamping.** "LGTM" on a change you did not actually understand or run. Review that
  doesn't build a whole-change model isn't review; it's a signature. The fix is mechanical:
  understand the change (read for structure, run/trace it) *before* approving.
- **Nitpicking the style while the design/correctness issue ships.** The signature failure,
  named verbatim by practitioners in Bacchelli & Bird. Commenting on what is *easy to see*
  (naming, formatting) instead of what *matters* (the money bug, the race, the security hole).
  The fix: **triage by consequence**; lead with the issue that matters; mark style as `Nit:`.
- **Vague feedback.** "This is confusing / clean this up / feels off" — no line, no impact, no
  suggestion. Unactionable. The fix: name the line, state the impact, propose a fix or ask the
  question that surfaces one.
- **Reviewing line-by-line without the whole-change model.** Commenting locally on each line
  while a contract- or cross-line-level bug stays invisible. The fix is the A2 move: chunk the
  *change* into its intent and contract before judging its lines.
- **Bikeshedding / demanding perfection / attacking the author.** Blocking on preference,
  chasing "perfect" over "better," or making the person the subject. The fix: facts over
  opinion, *better* not *perfect*, comment on the **code not the developer** (egoless).

**Evidence caveat (this is a `[Some empirical] + [Canon]` module — say so).** Unlike the pure
`[Verified]` Track-A modules, E3's grounding is **mixed and must not be oversold**:

- The **empirical** half is **one in-depth field study** (Bacchelli & Bird 2013, Microsoft,
  qualitative + survey). It robustly establishes the *direction* — review is dominated by
  understanding and code-improvement, deep defects are rare and hard, and the
  easy-style-nit-over-real-issue trap is real — but it is **one company, one tool, 2013**, not
  a replicated causal result. State it as "the best field study we have," not "research
  proves."
- The **how** half (prioritize code health, precise/kind feedback, *better* not *perfect*,
  egoless review) is **`[Practitioner-canon]`** — Google's eng-practices and Weinberg. Respected,
  widely taught **craft wisdom**, vetted against the named sources during authoring — **not**
  an empirical finding. The coach must never present it as verified science
  (`evidence-base.md` → badge rules).
- The **AI-era priority** that makes review the apex skill (review load rises as agents draft
  code; spec §12) is `[Verified-adjacent]` — **priority-steering, not proof**; the supporting
  productivity data is partly contested and vendor-sourced (`evidence-base.md` → AI-era
  honesty caveats).
- The **curriculum-wide transfer caveat** applies in full: that drilling review on synthetic
  diffs *causally* improves a given engineer's real-PR reviewing is the open question. The
  coach leans on the transfer task (§9) — the skill on a **real PR** — as the honest
  individual-level evidence, and grades it as the soft judgment it is.

No claim in this module is dressed above its badge.

---

## 9. Transfer task

**The only honest test of whether the gym drill transferred to the job is applying it to a real
review** (`assessment.md` Part 4; `evidence-base.md` → transfer caveat, consequence 2).

> **Your turn:** Find a **real pull request** — one open on a project you work on, a recent PR
> from your team's history, or an open-source PR in a repo you know well. Pick one small enough
> to review properly in a sitting (a few changed files, not a 2,000-line refactor).
>
> Now **run the three moves.** **(1) Understand the change:** what is it trying to do, why does
> it exist, what is the contract of the code it touches? Read the *whole change* — and where
> you can, **check out the branch and run it / trace the key path** rather than reasoning in
> your head. **(2) Judge what matters:** list the issues you find and **rank them by
> consequence** — correctness/security/data-loss first, design next, style last. Name the **one
> most important** thing. **(3) Communicate:** write the comment you'd actually leave on the
> issue that matters — reference the line, explain the impact, propose a fix or ask the
> question, mark blocking vs `Nit:`, and keep it about the **code, not the author**.
>
> Then step back: **was the most important issue the easiest one to see, or did it take
> understanding to find?** If you found yourself reaching first for naming and formatting, that
> is the exact trap this module targets — re-rank.

**Grading is softer and named as such** (`assessment.md` Part 4). A real PR has no clean answer
key; the coach grades against the §7 rubric (D1 catch / D2 prioritize / D3 communicate) and says:
*"this is a judgment call on your real review, not a machine-verifiable result."* Where any
sub-claim **is** runnable — the learner suspects a bug and the code can be exercised — the coach
still uses the runner: **reduce the suspected issue to a minimal snippet, run it through
`runner.py`, and confirm the misbehavior before the learner asserts it in the review** (the same
discipline as the §5d planted-bug check, now on the learner's real find). **Transfer evidence is
weighted heavily:** a learner who aces synthetic diffs but, on a real PR, drowns the one
consequential issue under style comments — or rubber-stamps it — has **not** transferred the
skill, and the tracker notes that gap as more diagnostic than another passed synthetic drill.

---

## Cross-references

- Drill mechanics, the **rubric + exemplars judgment path**, the executable check on the
  planted bug, exercise formats (Debug-this, Generation→Comparison, Teach-it-back, Error
  analysis), Frontier escalation: `references/drill-generation.md` (this module instantiates §1
  and follows §3, §4, §5; the planted-bug check uses §2).
- Session delivery (pause/no-spoiler hard stop, tier-faded worked example, direct feedback,
  scaffolding ladder): `references/coaching-loop.md`.
- E3 entry task, per-skill routing, mastery-rubric shape, held-out re-assessment, **real-PR
  transfer** weighting: `references/assessment.md` (the E3 entry task: a ~20–40-line diff with
  one substantive issue + a couple of nits — catch what matters, prioritize, phrase it well).
- Evidence grounding (Bacchelli & Bird 2013 in the AI-era section; the review-as-bottleneck
  AI-era priority; the reading spine — Weinberg's egoless review; the worked-examples /
  expertise-reversal instructional finding): `references/evidence-base.md`.
- Soft prerequisite (reading the change you must review): module **A2** (code reading &
  chunking); related execution-model modules **A1**, **A3**, **C2**.
- Golden exemplars (~3 per tier, each with a **runner-verified** planted bug + prioritized
  issue list + model comment): `exemplars/E3/foundations.md`, `exemplars/E3/working.md`,
  `exemplars/E3/advanced.md`.
