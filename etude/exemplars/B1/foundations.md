# B1 — Foundations exemplars (decomposition & planning)

Golden drills for the **Foundations** tier of module B1. Each is a **small, well-specified
problem with a clean 3–5-piece decomposition and one obvious hard part**. The deliverable is a
**plan, not code**: named sub-problems at one altitude, the data shape between them, the hard
part, and 1–2 edge cases. B1 plans are **rubric-graded** (`drill-generation.md` §3) — there is
**no single correct decomposition**. Where a plan is concrete enough, the gold's **composition
check** was confirmed by **implementing the pieces and running the whole** (`drill-generation.md`
§2):

```
python <skill-dir>/runtime/python/runner.py snippet.py
```

Coverage spans distinct domains and hard-part locations (aggregation + malformed-data policy /
encoding + run-boundary / classification + threshold-boundary) and three formats
(Generation→Comparison / Completion / Error-analysis). Pose one, **hard-stop, wait**
(`coaching-loop.md`). **How to grade** against module §7: **D1** = understood the contract;
**D2** = complete + balanced 3–5 boxes; **D3** = named the hard part + data shapes; **D4** =
surfaced the edge cases. The composition check is **reported separately** — it can prove a piece
doesn't fit, but a clean run does **not** make the plan well-decomposed (§5d).

---

## F1 — Sum a `name,amount` file (Generation → Comparison)

**Problem.** Plan `total_amount(lines)`: given lines of text in the form `name,amount`, return
the **sum of the amounts**. Skip **blank** lines and **malformed** lines (anything that isn't a
name and a numeric amount). No code — give me the decomposition.

> **Your turn:** Decompose this. What are the sub-problems, what data flows between them, what's
> the hard part, and what edge cases will you handle?
>
> (Take your best guess — wrong attempts are useful data.)

**Gold decomposition.**
- **Understand:** input `list[str]`; output a number (the running total). The **contract
  decision**: what counts as "malformed"? → a line that doesn't split into exactly two parts, or
  whose second part isn't a number. Blank lines are skipped, not errors.
- **Sub-problems (one altitude):**
  1. `is_skippable(line)` → bool (blank/whitespace-only).
  2. `parse(line)` → `(name, amount: float)` **or** `None` if malformed. *(the hard box)*
  3. `sum_valid(lines)` → fold: skip blanks, drop the `None`s, add the amounts.
- **Hard part:** the **parse-and-validate** step (#2) — the malformed-line policy is the only
  real decision; #1 and #3 are plumbing.
- **Edge cases:** empty input → `0.0`; a header row like `name,amount` (the amount isn't numeric
  → malformed → skipped, *for free*, if the policy is right); a blank line; a line `x,` with a
  missing amount.

**Composition check (runner-verified — the pieces compose):**

```
total_amount(['alice,10', 'bob,20.5', 'carol,5'])               -> 35.5
total_amount(['name,amount', 'alice,10', 'bob,xx', '', 'carol,5']) -> 15.0   (header + 'bob,xx' + blank skipped)
total_amount([])                                                -> 0.0
total_amount(['   ', 'x,'])                                     -> 0.0   (blank + missing-amount skipped)
status: ok
```

**Why.** The decomposition's whole job is to isolate the **one decision that matters** (the
malformed-line policy) into a single box with a clear contract (`parse -> (name, amount) | None`).
Get that contract right and the header row, the blank line, and the missing amount are all
handled by the *same* rule — no special-casing.

**Diagnoses.** A "plan" that is the opening lines of a `for` loop is **linear translation**
(§5c). A plan that details the splitting and looping but says "skip bad lines" without defining
*what "bad" means* has left the **hard part vague** (§5c, planning-the-easy-parts) — the whole
problem is that definition. A plan that never mentions the empty file or the malformed line is
**happy-path-only** (§5c). Strong plan: three balanced boxes, the parse-or-`None` contract named
as the hard part, the edge cases surfaced up front.

---

## F2 — Run-length encode (Completion)

**Problem.** Plan `encode(s)`: run-length-encode a string, e.g. `"aaabbc"` → `"a3b2c1"`. Here is
a **partial** decomposition — the easy boxes are filled, **the hard one is blank**:

```
1. scan(s)   -> ??????          # <-- the hard box: produce the runs
2. format(runs) -> str          # join each (char, count) into "<char><count>"
```

> **Your turn:** Fill in box 1 — what does `scan` produce (its output data shape), and what is
> the tricky part of producing it correctly? Name the edge cases.
>
> (Take your best guess — wrong attempts are useful data.)

**Gold completion.**
- **Box 1 `scan(s)` → `list[(char, count)]`:** walk the string tracking the **current run's
  character and length**; when the character changes, **emit the finished run** and start a new
  one. **The tricky part is the final flush** — the last run is only emitted *after* the loop
  (there's no "change" to trigger it), and the **empty string** must produce `[]` (no run to
  start). That boundary is the whole difficulty of the box.
- **Edge cases:** `""` → `[]` → `""`; a single char `"x"` → `[("x",1)]` → `"x1"`; all-same
  `"aaaa"` → `[("a",4)]` → `"a4"`; no repeats `"abc"` → `"a1b1c1"`.

**Composition check (runner-verified — the completed pieces compose):**

```
encode('aaabbc') -> 'a3b2c1'
encode('')       -> ''
encode('x')      -> 'x1'
encode('abc')    -> 'a1b1c1'
encode('aaaa')   -> 'a4'
status: ok
```

**Why.** The completion forces the learner onto the **load-bearing** box (the run-boundary +
final-flush), not the comfortable `format` box. Naming the **output data shape** (`list[(char,
count)]`) is what makes `format` a trivial one-liner — the interface *is* the design.

**Diagnoses.** A learner who describes `scan` as "loop and build the string" has **fused** the
two boxes and lost the clean interface (§5c, undefined-interface) — and will usually drop the
final run. A learner who omits the empty-string / single-char boundary has left the box's **hard
edge** unplanned (§5c, happy-path-only). Strong completion: the `list[(char,count)]` contract,
the final-flush named as the difficulty, the empty/single boundaries surfaced.

---

## F3 — Tally letter grades (Error-analysis / Debug-this-plan)

**Problem.** A teammate decomposed `tally(scores)` → "count how many scores fall in each letter
bucket A/B/C/D/F" as:

```
1. classify(score): "A if score > 90, B if score > 80, C if > 70, D if > 60, else F"
2. count(grades): tally how many of each letter
```

> **Your turn:** This decomposition composes fine and runs. Is it **correct**? If not, which
> exact inputs expose the bug, and what's the fix — and what does this tell you about where the
> decomposition went wrong?
>
> (Take your best guess — wrong attempts are useful data.)

**Gold answer.** The decomposition's *structure* is fine (classify → count, two balanced boxes).
The bug is **inside box 1's contract**: strict `>` means the **boundary scores are mis-bucketed**
— a `90` is *not* `> 90`, so it falls to **B**; `80` falls to C; `60` falls to **F**. The hard
part of this problem was the **boundary decision** ("is 90 an A?"), and the plan **answered it
silently and wrongly**. Fix: `>=` at each threshold.

**Composition check (runner-verified — the boundary scores `[90, 80, 70, 60]`):**

```
strict >  (the teammate's plan): {'A': 0, 'B': 1, 'C': 1, 'D': 1, 'F': 1}
correct >=                      : {'A': 1, 'B': 1, 'C': 1, 'D': 1, 'F': 0}
status: ok
```

Every boundary score slips one bucket down, and the `60` falls off the bottom into `F` — a
real grading bug, invisible on non-boundary inputs.

**Why.** This is the module's central lesson at Foundations scale: **a decomposition can compose
cleanly, run without error, and still be wrong**, because the error lives in a **sub-problem's
contract**, not in how the pieces fit. The fix isn't structural — it's surfacing the boundary
decision the plan glossed.

**Diagnoses.** A learner who says "looks fine, the boxes fit" judged the decomposition by
**composition, not contract** (§5c, solving-the-wrong-problem at the box level) — exactly the
trap §5d warns about ("a clean run doesn't prove the plan is good"). A learner who spots `>` vs
`>=` but can't name the **deciding inputs** (the on-boundary scores) has the catch without the
**edge-case discipline** (§5c, happy-path-only). Strong answer: names the boundary scores as the
deciding inputs, fixes the contract to `>=`, and states the principle — *the hard part here was a
boundary decision the plan answered silently*.
