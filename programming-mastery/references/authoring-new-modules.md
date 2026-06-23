# Authoring a New Curriculum Module — Process & Template

How to author a **new** `modules/<ID>-*.md` from scratch, codified from how the
existing six (A1, A2, A3, B3, E3, F1) were actually built. A1 is the
**executable-graded** reference shape; E3 is the **rubric + exemplar judgment** shape.
Read both real files before you start — this doc tells you the repeatable process; those
two files are the depth/structure bar you must match.

This is a process doc, not a substitute for the references it points at. The authoritative
specs live in `drill-generation.md` (drill format + both grading paths + Frontier-N),
`assessment.md` (entry task + rubric shape), `evidence-base.md` (citation grounding +
the three badges), `coaching-loop.md` (delivery), and `tools/validate_modules.py` (the
mechanical anatomy gate). When this doc and one of those disagree, the reference wins.

---

## 1. Placement

Decide these before writing a line:

- **Track (A–F).** A comprehension · B construction · C debugging · D quality/craft ·
  E scale/staff · F meta/learning. The track sets the default evidence posture (Track A
  is mostly `[Verified]`; D/E are mostly `[Practitioner-canon]`).
- **Stable ID `<Track><n>`** — e.g. `A4`, `D2`. The ID is permanent; downstream files
  cross-reference it. Check `SKILL.md`'s module index for the assigned slot and core idea.
- **Filename `<ID>-<kebab>.md`** — e.g. `A4-concurrency-mental-models.md`. Must match
  the validator regex `^[A-F][1-9][0-9]?-[a-z0-9-]+\.md$` (tracks A–F only; widen the
  regex first if a track G is ever added).
- **Tier badge** — exactly one of `[Verified]` / `[Verified-adjacent]` /
  `[Practitioner-canon]` must appear in the file (the validator checks this). **Mixed is
  allowed and encouraged when honest**: the *file* badge is the closest single validator
  token, but the *prose* badge can be richer (E3's file badge is `[Practitioner-canon]`
  while its honest prose badge is `[Some empirical] + [Canon]`; A4 is `[Verified-adjacent]
  + [Canon]`). Pick the badge from the module's grounding in `evidence-base.md`, never
  from how confident the topic *feels*.
- **Soft prerequisites** — which earlier modules *inform* this one. They never **gate**
  (the buffet rule: any learner may open any module at any tier — `assessment.md` rule 2).
  A1 has none (it is the root); E3 lists A2 recommended, A1/A3/C2 helpful.

---

## 2. Research-as-you-go (REQUIRED)

You research **while** authoring, against primary sources — not after, not from memory.

1. **Ground every claim in `evidence-base.md`.** Each module's evidence basis (§1 of the
   anatomy) and every citation the coach will make must trace to a finding already in
   `evidence-base.md`, badged at its true tier.
2. **If a needed source isn't there yet:** VERIFY it against the primary source, then add
   it to `evidence-base.md` with an **honest badge** and a one-line research note. **Never
   fabricate** a citation, a DOI, a page number, or a statistic. If a source or number
   cannot be confirmed, **flag it** (the "Could not fully confirm" pattern) rather than
   assert it — and prefer "cite less, not more."
3. **Never inflate a badge.** A `[Practitioner-canon]` or `[Verified-adjacent]` claim does
   not become `[Verified]` without a primary source. The coach is forbidden from
   presenting canon as science; your module text must make that impossible to do by
   accident.

**This pattern earns its keep — it has already caught real errors** (`evidence-base.md` →
Research notes):
- **Sala & Gobet 2017 / "r≈.42"** was a *misattribution* (that paper is working-memory
  training in children, not scrambled-code recall) — dropped and re-grounded on McKeithen
  1981 + Gobet & Simon 1996.
- **Adelson 1985 alone** was the wrong anchor for plan-before-code — the right cite is
  **Adelson & Soloway 1985**; both now cited with the correct claim mapped to each.
- **Lopez et al. 2008 "R² ≈ 0.66"** was a real arithmetic error — 0.66 is the bivariate
  correlation r, not the model variance; the verified figure is **46% combined variance
  (R² = 0.46)**.

If you find a spec citation that looks wrong, **correct it and record the correction** in
`evidence-base.md` → Research notes. That is the standing rule for authors.

---

## 3. The 9-part anatomy

Every module is nine numbered sections plus a Cross-references block. The validator
requires a top-level `# ` title and these heading substrings (case-insensitive, so
`## 1. Evidence basis` matches `evidence basis`): `evidence basis` · `soft prerequisites`
· `mental model` · `worked example` · `drill-generation spec` · `frontier band` ·
`mastery rubric` · `anti-patterns` · `transfer task`.

| # | Section | Must contain |
|---|---|---|
| 1 | **Evidence basis** `[badge]` | The 1–2 anchor findings from `evidence-base.md`, named with the confirmed primary sources and the *narrow* claim they license. State the **transfer caveat** (evidence is mostly 1976–1995 novices; causal transfer to experienced engineers is open). For mixed modules, separate the empirical half from the canon half explicitly. |
| 2 | **Soft prerequisites** | Which modules inform this one and why; the explicit "**inform, never gate**" line and the buffet rule (`assessment.md`). |
| 3 | **Mental model** | The one-paragraph core idea, then the structured model (a small state/concept table works well), then "the discipline in one line" + 2–3 corollaries the module drills. |
| 4 | **Worked example** | One concrete fully-worked instance at **Foundations depth**, with **runner-verified / runner-confirmed ground truth** pasted in. **Then the expertise-reversal fade table** — Foundations full → Working partial → Advanced skeleton → Frontier none (`evidence-base.md` → worked examples; `coaching-loop.md` Step 2). The fade is non-negotiable. |
| 5 | **Drill-generation spec** | The four required sub-parts (see §5 below): 5a tier definitions, 5b parameter space, 5c common-error catalog, 5d grading mode. Declare the grading mode up front. |
| 6 | **Frontier band** | What "one step" means here; the Advanced anchor; concrete escalation directions each labeled with a Frontier-N step count; the reset condition (`drill-generation.md` §5). |
| 7 | **Mastery rubric** | The per-tier observable bars, instantiating `assessment.md` Part 2 shape; the two cross-cutting requirements (**product *and* process**; **unaided + durable**); promotion by performance not tenure. |
| 8 | **Anti-patterns & evidence caveat** | The catalog entries from 5c surfaced as *behaviors* to break, each with its fix; then the honest **evidence caveat** walking back anything above its badge. |
| 9 | **Transfer task** | The "your turn" on the learner's **own real code**; the explicit "grading is softer and named as such"; "use the runner for any runnable sub-claim"; transfer evidence weighted heavily (`assessment.md` Part 4). |
| — | **Cross-references** | Pointers to `drill-generation.md`, `coaching-loop.md`, `assessment.md` (incl. this module's entry task), `evidence-base.md`, the soft-prereq modules, and the `exemplars/<ID>/{foundations,working,advanced}.md` files. |

Match A1's structure and **depth** (~30–45 KB is the going rate for a real module). A thin
module that passes the validator is not done.

---

## 4. Choosing the grading mode

Declare it in 5d. Three options; the choice is dictated by whether "is the answer right?"
is a **computation** or a **judgment**.

- **Executable ground truth** (A1's path — predict-output / trace / test-execution
  skills, Tracks A–C). The answer is computable. The coach **runs** the snippet via
  `runner.py`, parses the `RunResult` JSON, and grades the prediction against `stdout`
  (strip trailing `\n` before comparing to a bare prediction) and/or `status` (for
  "does it raise?"). **Never guess output.** *Verification implication:* every drill and
  exemplar key is real runner output, pasted in.
- **Rubric + exemplars** (E3's path — judgment skills: review, naming, design, planning,
  calibration; Tracks D–F and many Advanced/Frontier drills). There is **no executable
  ground truth for the judgment itself** ("is this a good review/name?" is not a
  computation). The coach grades against a small rubric (binary or 3-point criteria) +
  golden exemplars, cites the closest exemplar, and **says out loud it is softer than an
  executable pass** (`drill-generation.md` §3). *Verification implication:* you supply
  gold exemplars as the calibration anchor, AND you still **run any code embedded in the
  drill** (a review drill's planted bug must be confirmed real, and its proposed fix
  confirmed to resolve it).
- **Mixed / hybrid** (most modules in practice). The *output* is executable-graded; the
  *"why"* is rubric-graded. Report the two verdicts **separately** — a correct output with
  a hand-wavy mechanism is a **partial pass**, flagged as such (it often reflects luck, not
  model accuracy — `evidence-base.md` → illusions of fluency). E3 is hybrid the other way:
  the bug-*catch* and the *fix* have an executable sub-claim; the prioritization and
  communication are rubric-graded.

---

## 5. Drill-generation spec (the four required sub-parts)

This block lets the coach generate a fresh, correctly-leveled drill every turn without
rereading the whole module. Instantiate `drill-generation.md` §1 for your module.

**5a — Tier definitions.** Translate the fixed curriculum-wide tiers into *module-specific*
criteria (the names are fixed; the content is yours):
- **Foundations** — core mechanics, single concept, familiar surface.
- **Working** — apply in a context the learner hasn't seen; intent/execution diverge.
- **Advanced** — transfer/adapt/**combine two or more** mechanisms; explain *why*.
- **Frontier** — at or past the demonstrated ceiling (see 6).
Give an example shape per tier. Note the mis-tiering self-check (`drill-generation.md` §4):
a Foundations drill that secretly needs two-concept transfer is mislabeled.

**5b — Parameter space.** Enumerate the axes the coach varies to avoid mode-collapse —
e.g. *mechanism · context · data shape · mutability · predicted artifact · exercise format*
(`drill-generation.md` §6). Instruct the coach to keep an in-session log of the
`(axis-tuple)` used and not repeat one until the others are exercised.

**5c — Common-error catalog.** The heart of the module. The *specific* conceptual errors,
each in this exact format:

```
Error: <what the learner predicts / does incorrectly>
Diagnoses: <the conceptual gap this reveals>   ← THIS is what lets the coach name the gap, not say "incorrect"
Example trigger: <a drill that surfaces it>
```

Ground each entry in the misconception/practice literature cited in `evidence-base.md`, not
in trivia. State the **root misconception** that unifies most of them (A1: "a name is a box
that holds a value" vs. "a name is a label bound to an object"; E3: "spend the review on
what is easy to see, not what matters"). The diagnosis labels are what the coach attaches in
the feedback step — without them, feedback collapses to pass/fail.

**5d — Grading mode.** Declare executable / rubric / hybrid per §4 above, with the concrete
grading procedure for this module and the "report verdicts separately" rule for hybrids.

**Frontier-N (defined once here, used in 6).** Advanced = one non-trivial mechanism in
isolation. **Frontier-N = N increments past Advanced, where each increment adds exactly one
new interacting mechanism OR pushes one parameter-space dimension up one notch** (deeper
call stack, larger data shape, one more evaluation-order wrinkle). Not two at once. The
learner's current Frontier-N is the highest N they have passed (`drill-generation.md` §5).

---

## 6. Exemplars

Author `exemplars/<ID>/foundations.md`, `working.md`, `advanced.md` (one file per tier —
the convention is `exemplars/<ID>/<tier>.md`; no Frontier file, it is a moving target).

- **~3 drills per tier**, each spanning a **different** point in the parameter space — do
  **not** repeat one gotcha three times. (A1 Foundations: rebinding · two accumulators ·
  the failed swap. E3 Working: empty-case · truthiness-drop · mutable-default — three
  distinct bug classes with genuinely-tempting decoys.)
- **Each drill carries:** the snippet/diff, the `> **Your turn:**` prompt block, the
  **runner-verified answer key** (or runner-confirmed planted-bug evidence for judgment
  modules), the **Why**, and the **Diagnoses** label tied back to the 5c catalog. For
  judgment modules also include the prioritized issue list + the **gold** model
  answer/comment, and a "how to grade against §7" note.
- The header of each exemplar file states the tier, the parameter coverage, the runner
  command, and the pause/hard-stop reminder (`coaching-loop.md`).

---

## 7. Verification discipline (NON-NEGOTIABLE)

The single most important rule, and the one most likely to drift if you skip it:

- **Executable drills:** **RUN every snippet through the runner and paste the real
  output as the key.** Never hand-assert what a snippet prints. Use:
  ```
  python programming-mastery/runtime/python/runner.py snippet.py   # from repo root
  ```
  and copy the real `stdout` / `status` from the JSON. This applies to the worked example
  (§4), every exemplar (§6), and every drill the spec implies.
- **Judgment drills:** provide gold exemplars AND **run any embedded code**. For a review
  drill: (a) run the buggy snippet and confirm it actually misbehaves the way you claim,
  and (b) apply the proposed fix and re-run to confirm it resolves the bug. The *review* is
  rubric-graded, but the *planted bug* is executable ground truth — anchor the gold's
  prioritized list to real runner output, never to your guess.

If a snippet won't run (syntax error, unavailable import), fix it before it ships
(`drill-generation.md` §4 check 1).

---

## 8. Consistency checks

Before you consider the module done:

- **Validator passes:** `python tools/validate_modules.py programming-mastery/modules/`
  exits 0 (filename regex · top-level title · all 9 required headings · a valid badge).
- **Entry task matches `assessment.md`.** Each module has an entry task in
  `assessment.md` Part 1.4 and a rubric in Part 2. Your §7 mastery rubric and §9 transfer
  task must be consistent with that task's shape and the partial-knowledge routing boundary
  (Part 1.3: names-mechanism-but-inverts-timing → Working; no-mechanism → Foundations;
  correct-and-articulate → Advanced). If `assessment.md` has no entry task for your module
  yet, add one in the same style.
- **Citations only from `evidence-base.md`.** Every source the module names is present and
  badged there. New sources went through §2.
- **Depth/structure matches A1.** Same nine sections, the fade table, "the discipline in
  one line," the cross-references block, comparable thoroughness.

---

## 9. Review protocol (do this before declaring done)

A second pass that has repeatedly caught drift and fabrication:

1. **Independent re-run of every drill.** Re-run each snippet/embedded-bug **from scratch**
   and diff the output against the pasted key. This catches copy-paste drift and
   hallucinated output — exactly the failure the discipline exists to prevent.
2. **Anatomy + validator.** Confirm the 9 headings, the badge, the filename, and a clean
   validator exit.
3. **Consistency sweep.** Entry-task match, badge honesty (nothing dressed above its tier),
   exemplar parameter-space coverage (no repeated gotcha), buffet/soft-prereq language.
4. **Citation-trace.** Walk every citation back to `evidence-base.md`; confirm no DOI,
   number, or claim was invented or inflated; confirm any new source has an honest badge
   and a research note.

---

## 10. Section skeleton (copy-paste)

```markdown
# <ID> — <Title> `[badge]`

> **Module type.** <one or two lines: executable vs judgment; honest prose badge.>
> **Core idea.** <the one-sentence thesis.>

---

## 1. Evidence basis `[badge]`
<anchor finding(s) from evidence-base.md; confirmed primary sources; the narrow claim
they license; the transfer caveat; for mixed modules, empirical half vs canon half.>

## 2. Soft prerequisites
<which modules inform this; "inform, never gate"; the buffet rule.>

## 3. The mental model
<core paragraph; structured model table; "the discipline in one line"; 2–3 corollaries.>

## 4. Worked example — <what>
*(Foundations depth: every step shown. Fades by tier — see the table after.)*
<one fully-worked instance + RUNNER-VERIFIED ground truth pasted in.>
> **Expertise reversal — the example fades by tier.**
> | Tier | Worked-example depth |
> | Foundations | Full | Working | Partial | Advanced | Skeleton | Frontier | None |

## 5. Drill-generation spec
Grading mode declared up front: <executable | rubric+exemplars | hybrid>.
### 5a. Tier definitions  (Foundations / Working / Advanced criteria + example shapes)
### 5b. Parameter space   (the axes the coach varies; in-session no-repeat log)
### 5c. Common-error catalog
    Error: ... / Diagnoses: ... / Example trigger: ...   (× the real errors; state the root)
### 5d. Grading mode      (concrete procedure; report hybrid verdicts separately)

## 6. Frontier band
<what "one step" means; Advanced anchor; escalation directions w/ Frontier-N counts; reset.>

## 7. Mastery rubric
<per-tier observable bars; product AND process; unaided + durable; performance not tenure.>

## 8. Anti-patterns & evidence caveat
<5c entries as behaviors-to-break + fixes; honest caveat walking back anything above badge.>

## 9. Transfer task
<"your turn" on the learner's own real code; grading is softer + named; runner for runnable
sub-claims; transfer weighted heavily.>

## Cross-references
<drill-generation.md · coaching-loop.md · assessment.md (this module's entry task) ·
evidence-base.md · soft-prereq modules · exemplars/<ID>/{foundations,working,advanced}.md>
```

And `exemplars/<ID>/<tier>.md` per drill: snippet/diff → `> **Your turn:**` block →
runner-verified key (or runner-confirmed planted-bug evidence + gold answer) → Why →
Diagnoses (tied to 5c).

---

## 11. Pre-merge checklist

- [ ] **Placement:** track + ID + filename match the validator regex; badge chosen from
      grounding (mixed allowed); soft prereqs listed as inform-not-gate.
- [ ] **Research:** every claim traces to `evidence-base.md`; any new source verified +
      badged + research-noted; **no fabricated** DOI/number/claim; unconfirmables flagged.
- [ ] **Anatomy:** all 9 required sections present + Cross-references; depth ≈ A1.
- [ ] **Worked example:** Foundations-depth instance with **runner-verified** ground truth;
      **fade-by-tier table** present.
- [ ] **Grading mode:** declared in 5d; hybrid verdicts reported separately.
- [ ] **5c catalog:** real errors in `Error/Diagnoses/Example trigger` format; root
      misconception named; each diagnosis is something the coach can *say*.
- [ ] **Frontier:** escalation directions each labeled with a Frontier-N step count; reset
      condition stated.
- [ ] **Exemplars:** `exemplars/<ID>/{foundations,working,advanced}.md`, ~3 drills/tier,
      spanning the parameter space (no repeated gotcha); each with key + Why + Diagnoses.
- [ ] **Verification:** every executable snippet RUN and real output pasted; every judgment
      drill's planted bug confirmed real and its fix confirmed to resolve it.
- [ ] **Consistency:** `validate_modules.py` exits 0; entry task in `assessment.md` matches;
      citations only from `evidence-base.md`.
- [ ] **Review protocol:** independent re-run of every drill done; anatomy/validator,
      consistency, and citation-trace passes complete.
- [ ] **Do NOT git commit** — the controller integrates after review.
