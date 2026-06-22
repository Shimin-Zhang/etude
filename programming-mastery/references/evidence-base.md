# Evidence Base — Programming Mastery

The grounding document. Every module's evidence badge and every citation the coach
makes traces back to here. This file exists to keep the curriculum **honest**: it
openly separates **verified science** from **practitioner canon** from **debunked
folklore**, and it states the limits of the evidence out loud.

Each finding below was fact-checked against primary sources during authoring
(see [Research notes](#research-notes) at the end for what was confirmed, what was
corrected, and what could not be confirmed). When in doubt, the rule is: cite less,
not more; flag, don't inflate; never fabricate a citation or a DOI.

---

## How to read the evidence tiers

The coach must never present a lower tier as if it were a higher one. Three badges,
used on every module and every claim:

| Badge | Meaning | What it licenses the coach to say |
|---|---|---|
| `[Verified]` | Confirmed in this fact-checked research pass against primary sources. Replicated or strongly supported empirical finding, mostly from the program-comprehension and cognitive-psychology literature. | "Research shows…" — but still subject to the transfer caveat below. |
| `[Verified-adjacent]` | Extends a `[Verified]` finding, **or** rests on well-established *general* cognitive/educational science (e.g. retrieval practice, spacing, metacognition). The *general* science is solid; the **programming-specific** evidence is thin or extrapolated. | "Well-established in learning science generally; programming-specific evidence is thinner." |
| `[Practitioner-canon]` | Respected, widely taught engineering practice that is **not** empirically established. Grounded and vetted during authoring against the named book/source, but it is craft wisdom, not science. | "This is respected practice — not a verified research finding." |

A module may carry a **mixed** badge when its *concept* and its *method* differ in
status. Example: C1 (systematic debugging) rests on a `[Verified]` comprehension
model but a `[Practitioner-canon]` method, because the *causal* superiority of
systematic tracing over as-needed reading was **not** established (see
[Refuted under verification](#refuted-under-verification)).

---

## Verified findings we build on

High confidence. Each confirmed against primary sources in this pass. These describe
*what separates more- from less-skilled programmers* and *what the durable learning
barriers are* — the substance the curriculum teaches toward.

> **Read every row through the [transfer caveat](#the-transfer-caveat-that-shapes-the-whole-design).**
> Most of this evidence comes from **novices in introductory courses, 1976–1995**, in
> BASIC / Pascal / Fortran / ALGOL. The *direction* of these findings is well
> supported; their *causal* application to upskilling experienced engineers is an
> open question.

### 1. The notional machine is the durable barrier — not syntax `[Verified]`

The single most curriculum-actionable finding. The persistent difficulty for learners
is grasping the **runtime dynamics of execution** — what the machine actually *does*,
step by step, to program state — not memorizing syntax. The "notional machine" is the
idealized model of the executing computer that a learner must build to reason about
their code. Sorva's synthesis argues this should be an **explicit learning objective**,
addressed directly in teaching rather than left to osmosis.

- Sorva, J. (2013). Notional machines and introductory programming education.
  *ACM Transactions on Computing Education*, 13(2), Article 8, 1–31.
  doi:10.1145/2483710.2483713
- du Boulay, B. (1986). Some difficulties of learning to program.
  *Journal of Educational Computing Research*, 2(1), 57–73. *(Origin of the
  "notional machine" framing; emphasizes mechanistic models of the machine.)*

**Novice execution-model misconceptions** — the module also cites these three
peer-reviewed sources on the *specific* conceptual errors learners hold about
execution; they ground the common-error catalog in module A1 §5c:

- Pea, R. D. (1986). Language-independent conceptual "bugs" in novice programming.
  *Journal of Educational Computing Research*, 2(1), 25–36.
  doi:10.2190/689T-1R2A-X4W4-29J2. `[Verified]` — Identifies three classes of
  persistent, language-independent conceptual bugs — *intentionality* (attributing
  goals/foresight to the machine), *parallelism* (expecting simultaneous execution),
  and *egocentrism* (assuming the machine shares the programmer's context) — rooted
  in a unifying "superbug": the belief that a hidden interpreting mind lives inside
  the language. Confirmed against the primary source; peer-reviewed empirical work
  with novices from primary-school to college age.
- Kaczmarczyk, L. C., Petrick, E. R., East, J. P., & Herman, G. L. (2010).
  Identifying student misconceptions of programming. *Proceedings of the 41st ACM
  Technical Symposium on Computer Science Education (SIGCSE '10)*, 107–111.
  doi:10.1145/1734263.1734299. `[Verified]` — Formal interview study revealing four
  distinct misconception themes in core CS1 topics, including persistent memory-model
  and data-assignment errors. Voted #1 paper in SIGCSE's 50-year history. Confirmed
  against ACM DL and multiple secondary sources.
- Qian, Y., & Lehman, J. (2017). Students' misconceptions and other difficulties in
  introductory programming: A literature review. *ACM Transactions on Computing
  Education*, 18(1), Article 1, 1–24. doi:10.1145/3077618. `[Verified]` — Systematic
  literature review synthesizing misconceptions across syntactic, conceptual, and
  strategic knowledge in introductory programming; identifies patterns across many
  studies and implications for instruction. Confirmed against ACM DL; peer-reviewed
  literature review in a top CS-education venue.

→ Drives module **A1** (notional machine / execution model). Implication: teach the
execution model as a first-class objective; have the learner *simulate* state
transitions rather than read for intent.

### 2. Expertise is better representation: experts chunk code into larger semantic units `[Verified]`

Skilled programmers recognize patterns and group code into larger, meaning-bearing
chunks; less-skilled readers process more line-by-line on surface syntax. The
signature evidence is a recall asymmetry borrowed from the chess-expertise literature:
experts reproduce far more of a **well-structured** program after a brief viewing than
novices do — but that advantage **shrinks toward parity on *scrambled* code**, where
the chunkable structure is destroyed. Crucially the advantage *shrinks but does not
fully vanish*: a small skill effect survives even on scrambled material.

- McKeithen, K. B., Reitman, J. S., Rueter, H. H., & Hirtle, S. C. (1981). Knowledge
  organization and skill differences in computer programmers. *Cognitive Psychology*,
  13(3), 307–325. *(ALGOL: experts ~18 vs ~6 lines recalled on ordered vs scrambled
  programs; near-parity across skill levels on scrambled code.)*
- Shneiderman, B. (1976). Exploratory experiments in programmer behavior.
  *International Journal of Computer and Information Sciences*, 5(2), 123–143.
  *(Early memorization/recall evidence for semantic vs syntactic knowledge.)*
- Bidlake, L., Aubanel, E., & Voyer, D. (2020/2023). Systematic literature review of
  empirical studies on mental representations of programs. arXiv:2212.07763
  *(Modern synthesis of the mental-representation literature.)*
- **Chess-chunking analogue:** Gobet, F., & Simon, H. A. (1996). Recall of random and
  distorted chess positions. *Memory & Cognition*, 24(4), 493–503. *(Experts' recall
  advantage shrinks on random positions but a small skill effect remains — the source
  of the "shrinks but doesn't vanish" nuance.)*

→ Drives module **A2** (code reading & chunking). Implication: train reading *for
structure*, recognizing recurring patterns, and summarizing unfamiliar code fast —
not slow line-by-line decoding.

### 3. Beacons and programming plans are real cues experts exploit `[Verified]`

Certain code features ("beacons") reliably signal a program's purpose to experienced
readers, and experts recognize stereotyped solution fragments ("programming plans").
Eye-tracking and recognition studies confirm experts fixate and rely on these cues
more than novices.

- Brooks, R. (1983). Towards a theory of the comprehension of computer programs.
  *International Journal of Man-Machine Studies*, 18(6), 543–554. *(Introduces beacons
  in a top-down, hypothesis-driven comprehension model.)*
- Soloway, E., & Ehrlich, K. (1984). Empirical studies of programming knowledge.
  *IEEE Transactions on Software Engineering*, SE-10(5), 595–609. *(Programming plans
  and rules of discourse; expert advantage on "plan-like" programs.)*
- Crosby, M. E., Scholtz, J., & Wiedenbeck, S. (2002). The roles beacons play in
  comprehension for novice and expert programmers. *PPIG 14th Workshop.*
- Storey, M.-A. (2005/2006). Theories, methods and tools in program comprehension:
  past, present and future. *IEEE IWPC.* *(Survey situating beacons/plans.)*

→ Feeds module **A2**. Caveat: that plans are *real cues* is verified; that a clean
*catalog* of plans can be taught as the deep structure of programming is **not** (see
[Refuted](#refuted-under-verification) — Gilmore & Green 1988).

### 4. Comprehension is active and hypothesis-driven `[Verified]`

Reading code is not passive intake. Experts run a cycle of forming hypotheses about
what code does and confirming them against the text — combining **top-down**
(expectation-driven, Brooks) and **bottom-up** (text-driven, Pennington) strategies,
**switching modes** opportunistically as the task demands (von Mayrhauser & Vans).

- Brooks, R. (1983). *(top-down, beacons — full cite above.)*
- Pennington, N. (1987). Stereotyped knowledge structures (program model vs domain
  model) and comprehension strategies in programming. *Cognitive Psychology*, 19,
  295–341 / Empirical Studies of Programmers, 2nd Workshop. *(Bottom-up program model;
  procedural/control-flow units form the base representation.)*
- von Mayrhauser, A., & Vans, A. M. (1995). Program comprehension during software
  maintenance and evolution. *IEEE Computer*, 28(8), 44–55. *(Integrated metamodel:
  programmers switch between top-down and bottom-up.)*

→ Drives modules **A3** (tracing) and **C1** (debugging). Implication: teach
comprehension and debugging as *prediction → check*, not as reading until it "clicks."
**Note the boundary:** the *two-model program/situation theory* itself did not survive
adversarial fact-checking as a teachable decomposition (see [Refuted](#refuted-under-verification));
we use top-down/bottom-up + mode-switching as the supported frame.

### 5. Experts plan top-down before coding; novices translate step-by-step `[Verified]`

More-skilled programmers form an **abstract, relatively complete representation of the
solution** before writing code — decomposing the problem and keeping all parts of the
design at a comparable level of abstraction before refining — whereas novices tend to
translate the problem into code more linearly, one step at a time.

- Adelson, B., & Soloway, E. (1985). The role of domain experience in software design.
  *IEEE Transactions on Software Engineering*, SE-11(11), 1351–1360. *(Experts build a
  mental model and balanced top-down plan before committing to code.)*
- Adelson, B. (1985). Comparing natural and abstract categories: a case study from
  computer science. *Cognitive Science*, 9(4), 417–430. *(Experts organize knowledge
  by function/abstraction; novices by surface syntax — supports the *representation*
  half of the claim.)*
- Supporting: Soloway & Ehrlich 1984; Hoc, Green, Samurçay & Gilmore (eds.) work on
  planning; Rist, R. S. (1991), schema creation in programming, *Cognitive Science*,
  15, 389–414; Koubek & Salvendy (1988/1991) on expert/novice problem representation.

→ Drives module **B1** (decomposition & planning). **Teach plan-before-code and
decomposition — NOT a "plan catalog"** (the catalog claim was refuted; see below).

### 6. Reading → tracing → writing is a developmental hierarchy `[Verified]`

The ability to **trace** code (hand-simulate execution) and to **explain code in plain
English** track strongly with the ability to **write** code. Across the BRACElet
studies, tracing and explaining sit *below* writing in a skill hierarchy: students who
cannot reliably trace usually cannot explain, and tracing+explaining tasks account for
a large share of variance in writing performance.

- Lopez, M., Whalley, J., Robbins, P., & Lister, R. (2008). Relationships between
  reading, tracing and writing skills in introductory programming. *ICER '08*, 101–112.
  *(Tracing + explaining explained ~46% of variance in code-writing; R² ≈ 0.66 across
  the skills.)*
- Lister, R., et al. — the BRACElet project (multi-institution, 2004 onward); see also
  "A closer look at tracing, explaining and code writing skills in the novice
  programmer" and "Further evidence of a relationship between explaining, tracing and
  writing skills" (SIGCSE Bulletin, 2009).

→ Drives modules **A3** (tracing / explain-in-plain-English) and **B2** (writing).
Implication: build writing on a foundation of tracing and explaining; do not jump
learners straight to composition.

### 7. Years of experience ≠ expertise — tenure is a weak proxy `[Verified]`

Expertise in programming is poorly operationalized in the literature, and **years of
experience is an unreliable proxy** for measured skill. Self-rated and tenure-based
"expertise" correlate weakly and inconsistently with performance. The practical
consequence: **assess by performance, not by résumé.**

- Bidlake, L., Aubanel, E., & Voyer, D. (2020). On the relationship between experience
  and self-assessed expertise; and the SLR (arXiv:2212.07763) on the inconsistent
  operationalization of programming expertise. *(Experience-in-years correlated with
  self-assessed expertise for some samples but **not** for the experienced-developer
  sample.)*
- Baltes, S., & Diehl, S. (2018). Towards a theory of software development expertise.
  *ESEC/FSE 2018.* arXiv:1807.06087. *(Experience alone does not make an expert;
  monitoring/feedback matter.)*
- Peitek, N., Apel, S., Parnin, C., Brechmann, A., & Siegmund, J. (2022). Correlates of
  programmer efficacy and their link to experience: a combined EEG and eye-tracking
  study. *ESEC/FSE 2022.* *(Programmer efficacy links only weakly to years of
  experience.)*

→ Drives the **entry assessment** (`references/assessment.md`): recommend tier by a
short *performance* task per skill; never gate by claimed seniority.

---

## Learning-science instructional pillar

The findings above are about **what** separates experts. This pillar is about **how to
teach** — robust results from cognitive and educational psychology that govern how the
coach delivers drills (the coaching loop in `references/coaching-loop.md`).

These are **`[Verified-adjacent]`**: the *general* science is well-established and
replicated; the **programming-specific** transfer carries the same open-question caveat
as everything else here. The coach should present them as solid learning science, not
as programming-specific proof.

This pillar was **surfaced via Cat Hicks' _Learning Opportunities_** project (see the
[attribution note](#attribution)), whose independently assembled bibliography overlaps
ours (Hermans, Storey, Ericsson, Tankelevitch) — independent assembly converging on the
same sources is mild cross-validation of the foundation.

| Technique | Finding (direction) | How the coach applies it |
|---|---|---|
| **Generation & testing effect** | Producing or retrieving information beats passively consuming it, even when *immediate* performance is worse — the benefit shows up on *delayed* tests. | Generate-before-reveal; teach-it-back; predict before tracing. |
| **Pre-testing** | Attempting a problem *before* being shown the answer improves later retention of the to-be-learned material — even when the attempt **fails**. Shown specifically for people learning programming concepts. | Have the learner predict/sketch/attempt first, then reveal. Wrong attempts are valuable data. |
| **Spacing** | Distributing practice over time beats massing it ("cramming"). It *feels* worse and is *judged* less effective by learners, yet produces better retention for most. | Spaced review; retrieval check-ins at session start. |
| **Worked examples + expertise reversal** | Studying worked examples helps **novices** (lowers extraneous load during schema-building); for **experts** the shown steps become redundant load and the benefit **reverses** — they learn more by solving. | Full worked example at Foundations; *fade* by tier; go straight to problems at Advanced/Frontier. |
| **Desirable difficulties** | Conditions that slow short-term performance often improve long-term retention and transfer. | Don't simplify the challenge under struggle; scaffold the *setup*, not the answer. |
| **Learning ≠ performance** | Immediate (same-session) performance is a poor index of *durable* learning. | Weight delayed re-assessment and real-code transfer over same-session streaks; treat a hot streak as provisional. |
| **Illusions of fluency / effort** | Fluent reading and the *feeling* of effort are both mistaken for knowledge; learners are systematically miscalibrated about what they've learned. | Feeds F1 calibration work; probe consequences ("what changes if line N changes?") rather than accepting "I get it." |
| **Metacognition** | Monitoring and calibration are trainable and predict outcomes *independent of raw ability*. | F1 (metacognition & calibration); reflection prompts; self-assessment of confidence. |

**Citations (instructional pillar):**

- Roediger, H. L., III, & Karpicke, J. D. (2006). The power of testing memory: basic
  research and implications for educational practice. *Perspectives on Psychological
  Science*, 1(3), 181–210. *(Companion empirical paper: "Test-enhanced learning,"
  *Psychological Science*, 17(3), 249–255 — delayed retention ~21% higher for tested
  vs restudied material.)*
- Murphy, D. H., Little, J. L., & Bjork, E. L. (2023). The value of using tests in
  education as tools for learning — not just for assessment. *Educational Psychology
  Review*, 35(3), 89.
- Giebl, S., Mena, S., Storm, B. C., Bjork, E. L., & Bjork, R. A. (2021). Answer first
  or Google first? Using the internet in ways that enhance, not impair, one's
  subsequent retention of needed information. *Psychology Learning & Teaching*, 20(1),
  58–75. *(Pre-testing benefit demonstrated with people learning programming concepts.)*
- Kornell, N. (2009). Optimising learning using flashcards: spacing is more effective
  than cramming. *Applied Cognitive Psychology*, 23(9), 1297–1317.
- Kang, S. H. K. (2016). Spaced repetition promotes efficient and effective learning.
  *Policy Insights from the Behavioral and Brain Sciences*, 3(1), 12–19.
- Sweller, J., & Cooper, G. A. (1985). The use of worked examples as a substitute for
  problem solving in learning algebra. *Cognition and Instruction*, 2(1), 59–89.
- Kalyuga, S. (2007). Expertise reversal effect and its implications for
  learner-tailored instruction. *Educational Psychology Review*, 19(4), 509–539.
- Bjork, R. A. — desirable difficulties (see Bjork, Dunlosky & Kornell 2013, below).
- Soderstrom, N. C., & Bjork, R. A. (2015). Learning versus performance: an integrative
  review. *Perspectives on Psychological Science*, 10(2), 176–199.
- Bjork, R. A., Dunlosky, J., & Kornell, N. (2013). Self-regulated learning: beliefs,
  techniques, and illusions. *Annual Review of Psychology*, 64, 417–444.
- Dunlosky, J., Rawson, K. A., Marsh, E. J., Nathan, M. J., & Willingham, D. T. (2013).
  Improving students' learning with effective learning techniques. *Psychological
  Science in the Public Interest*, 14(1), 4–58.
- Tankelevitch, L., Kewenig, V., Simkute, A., Scott, A. E., Sarkar, A., Sellen, A., &
  Rintel, S. (2024). The metacognitive demands and opportunities of generative AI.
  *CHI 2024.*

---

## Folklore we explicitly reject

The curriculum actively debunks these. The debunking of each was confirmed in this pass.

### "The camel has two humps" — there is no born-programmer aptitude test

The claim: a simple test sorts people who can learn to program from people who never
will, supposedly revealing a bimodal ("two humps") distribution. **Retracted by its own
author.** Richard Bornat's 2014 retraction states plainly that the test does not work
and that the strongest claims were made during an SSRI-induced manic episode.

In Bornat's own words (from the retraction): *"Dehnadi didn't discover a programming
aptitude test. He didn't find a way of dividing programming sheep from non-programming
goats."* On the "100% accurate" claim he had circulated: *"It was a palpably false
claim, as Dehnadi's data at the time showed."* And on the circumstances: he was on an
SSRI that left him *"grandiose, extremely self-righteous and very combative"* and
*"believed, at the time, that there were people who couldn't learn to program… an
absurd claim because I didn't have the extraordinary evidence."*

- Bornat, R. (2014). *Camels and humps: a retraction.* Middlesex University.
- *Retraction Watch* (18 July 2014): "The camel doesn't have two humps: programming
  'aptitude test' canned for overzealous conclusion."

→ The skill **never** sorts learners into "can/can't program." It measures
within-person progress on defined skills. (See [transfer caveat](#the-transfer-caveat-that-shapes-the-whole-design).)

### The strong 10,000-hour / 10-year rule — deliberate practice is *not* the dominant cause of expertise

The popular claim that ~10,000 hours of practice is the dominant determinant of expert
performance does **not** hold as a strong thesis. Meta-analytic evidence:

- Deliberate practice explained roughly **12% of the variance in performance overall**
  (pooled across domains) in Macnamara, Hambrick & Oswald (2014) — and only ~**1% in
  professions**, ~4% in education, ~18% in sports, ~21% in music, ~26% in games. Most
  of the variance is explained by *other* factors.
- The effect **loses most of its power at elite levels** and where practice is best
  measured; retrospective recall of practice hours tends to **inflate** estimates.
- **Time-to-mastery varies enormously** — in chess, the slower player needed ~**8×** as
  much practice as the faster player to reach master level (Gobet & Campitelli 2007).

**Honest framing for the coach:** the numbers above come from **music, sports, chess,
and games — NOT software.** And there is a **live scientific dispute**: K. Anders
Ericsson and colleagues contested the *magnitude* and definition used in these
meta-analyses. So state the conclusion carefully: *"the strong 10,000-hour claim is not
supported; practice matters but is far from the whole story; the precise numbers aren't
from programming."*

- Macnamara, B. N., Hambrick, D. Z., & Oswald, F. L. (2014). Deliberate practice and
  performance in music, games, sports, education, and professions: a meta-analysis.
  *Psychological Science*, 25(8), 1608–1618.
- Hambrick, D. Z., et al. (2014). Deliberate practice: is that all it takes to become
  an expert? *Intelligence*, 45, 34–45. *(DP ≈ one-third of variance in music/chess;
  most variance unexplained.)*
- Hambrick, D. Z., Macnamara, B. N., & Oswald, F. L. (2018/2020) — follow-up analyses
  reaffirming the limited share of variance.
- Gobet, F., & Campitelli, G. (2007). The role of domain-specific practice, handedness
  and starting age in chess. *Developmental Psychology*, 43(1), 159–172. *(~8× spread
  in time-to-master.)*

→ Drives module **F2** (designing your own practice): what matters is **quality +
immediate feedback + individualized targeting**, NOT hour-dosing. *Peak* (Ericsson &
Pool) is on the reading spine **to be read critically**, precisely because of this
dispute.

---

## Refuted under verification

**Do NOT author modules asserting these.** Each *sounded* right and is repeated in the
secondary literature, but did **not** survive adversarial fact-checking as a clean,
teachable claim. They are listed so future module authors don't reintroduce them.

- **"Teach the catalog of programming plans + discourse rules ⇒ expertise"** (i.e.,
  plans as a clean, transferable deep structure you can enumerate and drill). *Refuted:*
  plan sensitivity is partly **notation-dependent** — Gilmore & Green (1988) found Pascal
  programmers were cued by plan structure but BASIC programmers were **not** sensitive to
  the same plans, so plans cannot be the language-independent deep structure.
  *Constrains B1:* teach planning and decomposition, **not** a plan catalog.
  - Gilmore, D. J., & Green, T. R. G. (1988). Programming plans and programming
    expertise. *Quarterly Journal of Experimental Psychology*, 40A(3), 423–442.
- **"Experts use function-based mental models; novices use data-flow models."**
  *Refuted (weak/contradictory support).* Do not assert a clean function-vs-data-flow
  expert/novice split.
- **"Two-model theory (a separate program-model and situation-model) is the structure
  of comprehension."** *Refuted as a teachable decomposition (weak support).* We use
  top-down + bottom-up + mode-switching (Finding 4) instead.
- **"Experts search breadth-first; novices depth-first."** *Refuted (weak/contradictory
  support).* Do not teach a breadth-vs-depth expertise signature.
- **"Systematic control/data-flow tracing *causally* yields better mental models and
  fewer errors than as-needed reading."** *Refuted as a causal claim.* Teach tracing as
  **a** strategy in the toolkit; do **not** claim it is causally superior to skilled
  as-needed reading. *(This is why C1's method is `[Practitioner-canon]`, not
  `[Verified]`.)*

---

## The transfer caveat that shapes the whole design

> **Read this before trusting any `[Verified]` badge as a promise about working- or
> staff-level developers.**

Nearly all of the *verified* evidence above is drawn from **novices in introductory
courses**, mostly **1976–1995**, working in **BASIC / Pascal / Fortran / ALGOL**.
Whether explicitly teaching these skills *causally improves experienced developers* —
and whether the novice→expert *findings* extrapolate to **working- and staff-level
depth** — is an **open empirical question**. Staff-level module content (Tracks D/E) is
largely **extrapolation and practitioner canon**, honestly labeled as such.

Three consequences are baked into the skill's design:

1. **Measurement is built in from day one.** The skill measures **within-learner deltas
   on concrete performance tasks** against the learner's own baseline — not an absolute,
   certified expertise grade (no validated absolute measure of programming expertise
   exists).
2. **Every module ends with a transfer task on the learner's *own real code*** — the
   only honest test of whether a gym drill transferred.
3. **Depth beyond the evidence is labeled**, via the tier badges and per-module
   "rests on canon, not verified research" notes.

The coach states this out loud when relevant: *this is within-person progress on
defined skills, not a certified expertise score.*

---

## AI-era impact (2026–27) `[Verified-adjacent]`

As coding agents draft most first-draft code, developer value shifts from *writing* code to *verifying* code one didn't write. A five-angle research synthesis (productivity RCTs, practitioner commentary, code-quality data, agentic-role analysis, deskilling studies) converged on a "verification cluster" that grounds the AI-era priority for modules **E3, F1, A2/A3, B3** (see spec §12).

- **Calibration gap** (→ F1): in a randomized controlled trial, experienced developers were **~19% slower** with AI tools while *believing* they were ~20% faster (METR 2025); and more AI-literate users were *more* overconfident (Fernandes et al. 2025, *Computers in Human Behavior*). The single best-evidenced AI-era finding.
- **Review is the new bottleneck** (→ E3): when agents generate code, human review load rises sharply (Faros telemetry; DORA 2025 — "AI doesn't replace code review; it makes it more critical"). Code review has prior empirical grounding (Bacchelli & Bird 2013, ICSE — *Expectations, Outcomes, and Challenges of Modern Code Review*).
- **Comprehension atrophies first** (→ A2/A3): AI-assisted engineers scored **~17% lower** on later *unaided* comprehension/debugging (Anthropic RCT, N=52).
- **AI code carries defects** (→ B3): ~45% of AI-generated samples carried security vulnerabilities (Veracode 2025); a NUS/Google CS-education consensus calls precise specification + verification "arguably the most durable technical skill a graduate can possess."

**Honesty caveats.** The productivity *direction* is contested (METR is revising its finding after late-2025/2026 data showed an ~18% *speedup*); much "AI degrades quality" data is vendor-sourced (GitClear was independently rebutted); the **RCTs** (METR, Anthropic, Stanford CCS'23) are the load-bearing evidence; coding-specific *causal* evidence is thin and small-N. Treat this as **priority-steering, not proof** — hence the `[Verified-adjacent]` badge.

## Reading spine (book canon)

The curriculum's book-length sources. These are **not** all peer-reviewed evidence;
some are practitioner canon (badge accordingly when a module leans on them).

| Book | Role in the curriculum |
|---|---|
| Hermans, F. *The Programmer's Brain* (2021) | **Comprehension core.** Synthesizes the verified findings (chunking, notional machines, working memory / cognitive load) into teachable technique. Primary book anchor for Tracks A. |
| Zeller, A. *Why Programs Fail* (2nd ed., 2009) | Scientific, hypothesis-driven debugging. Anchors **C1** and **C3**. |
| Weinberg, G. *The Psychology of Computer Programming* (1971/1998) | Foundational context on the human side of programming; egoless programming, review culture. |
| Ericsson, K. A., & Pool, R. *Peak* (2016) | Deliberate practice — **read critically.** Frames F2, but its strong claims are exactly what the meta-analyses dispute (see folklore section). Use for the *quality-of-practice* ideas, not the hour-dosing thesis. |
| Ousterhout, J. *A Philosophy of Software Design* (2018) | Complexity, deep vs shallow modules. Craft anchor for **D1–D3** `[Practitioner-canon]`. |
| Fowler, M. *Refactoring* (2nd ed., 2018) | Behavior-preserving change, refactoring catalog. Craft anchor for **D3** `[Practitioner-canon]`. |
| Feathers, M. *Working Effectively with Legacy Code* (2004) | Getting legacy code under test; seams. Staff anchor for **E1** `[Practitioner-canon]`. |
| Kleppmann, M. *Designing Data-Intensive Applications* (2017) | Systems/architecture judgment at scale. Staff anchor for **E2** `[Practitioner-canon]`. |

---

## Attribution

The **learning-science instructional pillar** (and several instructional-design
choices echoed in the coaching loop) were **surfaced via Cat Hicks' _Learning
Opportunities_ project** — a Claude Code / Codex skill for deliberate skill development
during agentic coding. Its independently assembled bibliography (generation/testing
effect, pre-testing, spacing, worked examples + expertise reversal, desirable
difficulties, learning≠performance, metacognition) overlaps and cross-validates this
file's foundation, and its PRINCIPLES document informed how those findings are framed
for a coaching context.

> *Learning Opportunities* by **Dr. Cat Hicks** (with the *orient* module by
> Dr. Michael Mullarkey) is licensed **CC-BY 4.0**. Findings and citations are reused
> here **with credit**. See <https://drcathicks.com> and the project's newsletter
> *Fight for the Human*. The affective self-report measures used elsewhere in this
> skill (`references/assessment.md`) derive from CC-BY-SA-4.0 open-access measures and
> carry their own share-alike attribution block there.

---

## Research notes

What was verified, corrected, or could not be confirmed in this fact-checking pass.
Recorded for transparency and to keep future authors honest.

**Confirmed against primary sources (direction, and magnitude where a number is claimed):**

- **Sorva 2013** — confirmed: ACM TOCE 13(2), Article 8, doi:10.1145/2483710.2483713;
  argues the notional machine should be an explicit learning objective. ✓
- **du Boulay 1986** — confirmed: *J. Educational Computing Research* 2(1), 57–73;
  origin of the notional-machine framing. ✓
- **Pea 1986** — confirmed: *J. Educational Computing Research* 2(1), 25–36,
  doi:10.2190/689T-1R2A-X4W4-29J2; "superbug" framing (hidden-mind belief as root
  of intentionality/parallelism/egocentrism bugs); confirmed via SAGE/journals.sagepub
  and ERIC EJ331846. ✓
- **Kaczmarczyk, Petrick, East & Herman 2010** — confirmed: SIGCSE '10, pp. 107–111,
  doi:10.1145/1734263.1734299; four-theme interview study of CS1 misconceptions;
  confirmed via ACM DL and Illinois/NJIT institutional records; voted #1 SIGCSE paper
  in 50-year history. ✓
- **Qian & Lehman 2017** — confirmed: ACM TOCE 18(1), Article 1, pp. 1–24,
  doi:10.1145/3077618; literature review of misconceptions in introductory
  programming; confirmed via ACM DL. ✓
- **McKeithen et al. 1981** — confirmed: on *ordered* programs experts recalled ~3× more
  than novices (≈18 vs 6 lines); on *scrambled* code the groups converged toward
  near-parity (a small expert residual remains). ✓
- **Shneiderman 1976** — confirmed: *Int. J. Computer & Information Sciences* 5(2),
  123–143; memorization/recall evidence for semantic vs syntactic knowledge. ✓
- **Soloway & Ehrlich 1984** — confirmed: IEEE TSE SE-10(5), 595–609; plans + discourse
  rules. ✓
- **Brooks 1983 / Pennington 1987 / von Mayrhauser & Vans 1995** — confirmed:
  top-down (beacons), bottom-up (program model), and mode-switching metamodel
  respectively. ✓
- **Lopez et al. 2008 (BRACElet)** — confirmed: ICER '08; tracing + explaining
  explained ~46% of code-writing variance (R² ≈ 0.66 across skills). ✓
- **Bidlake, Aubanel & Voyer 2020 / Baltes & Diehl 2018 / Peitek et al. 2022** —
  confirmed: experience-in-years is a weak/inconsistent proxy for measured expertise. ✓
- **Bornat 2014 retraction + Retraction Watch 2014** — confirmed with direct quotes;
  the "100% accurate" aptitude claim was retracted and attributed to an SSRI-induced
  manic episode. ✓
- **Macnamara, Hambrick & Oswald 2014** — confirmed: **~12% of variance overall**
  (pooled); per-domain 26% games / 21% music / 18% sports / 4% education / <1%
  professions. The spec's "~12–14%" is accurate (12% is the headline pooled figure).
  Hambrick 2014 (*Intelligence* 45) corroborates "~one-third of variance in music/chess,
  most unexplained." ✓
- **Gobet & Campitelli 2007** — confirmed: ~8× spread in time-to-master in chess. ✓
- **Gilmore & Green 1988** — confirmed: Pascal programmers cued by plan structure,
  BASIC programmers **not** → plans are notation-dependent → refutes the "plan catalog =
  deep structure" claim. ✓
- **Instructional pillar** (Roediger & Karpicke 2006; Murphy 2023; Giebl 2021;
  Kornell 2009; Kang 2016; Sweller & Cooper 1985; Kalyuga 2007; Soderstrom & Bjork 2015;
  Bjork/Dunlosky 2013; Tankelevitch 2024) — all confirmed as cited; effect directions
  match. Giebl 2021 confirmed to involve people learning **programming** concepts. ✓
- **Hermans, _The Programmer's Brain_** — confirmed as the comprehension-core synthesis
  (chunking, notional machines, cognitive load). ✓

**Citations corrected / re-grounded (flagged, not silently changed):**

1. **Chess-chunking analogue — "Sala & Gobet 2017, r≈.42" (as in the spec) appears
   MISATTRIBUTED.** Sala & Gobet (2017), *Developmental Psychology*, is a meta-analysis
   of **working-memory training in children** (near-transfer g̅≈0.46, far-transfer
   g̅≈0.12) — it does **not** concern scrambled-code or chess-position recall, and I
   could not locate an "r≈.42" for the chunking effect in it. The scrambled-code /
   chess-chunking analogue is correctly grounded by **McKeithen et al. 1981** (the
   programming evidence) and **Gobet & Simon 1996** (the chess random-position evidence,
   which is the actual source of "shrinks but doesn't vanish"). I have re-grounded
   Finding 2 on those sources and **dropped the Sala & Gobet 2017 / r≈.42 citation**
   rather than reproduce an unverifiable number.
2. **Top-down planning (Finding 5) — Adelson 1985 alone is the wrong anchor.** The
   *Cognitive Science* 1985 paper ("Comparing natural and abstract categories") supports
   the **representation/categorization** half (experts organize by function/abstraction).
   The **plan-before-code / equal-abstraction** claim is **Adelson & Soloway 1985**
   ("The role of domain experience in software design," IEEE TSE SE-11(11)). Both are now
   cited, with the right claim mapped to each.
3. **"Years ≠ expertise" — Peitek/Parnin/Apel 2022 precise paper.** The correct paper is
   **"Correlates of programmer efficacy and their link to experience"** (ESEC/FSE 2022),
   not the group's fMRI/code-complexity paper (ICSE 2021). Cited precisely.
4. **Roediger & Karpicke 2006 — two papers exist.** The spec/PRINCIPLES cite the
   *Perspectives on Psychological Science* review (1:181–210); the empirical companion
   with the ~21% delayed-retention result is *Psychological Science* 17:249–255. Both are
   genuine 2006 Roediger & Karpicke papers; I cite the review as primary and note the
   companion. No error — precision only.

**Could not fully confirm (flagged honestly):**

- **Hambrick et al. 2018, 2020** — the *existence* of follow-up Hambrick/Macnamara
  analyses reaffirming a limited variance share is confirmed in secondary sources, but I
  did not pin exact venue/page for each year in this pass. The *direction* (DP explains a
  limited share; the strong thesis is unsupported) is solid; treat the 2018/2020 cites as
  supporting, with primary weight on Macnamara 2014 and Hambrick 2014.
- **Ericsson's "live dispute"** — confirmed that Ericsson and colleagues publicly
  contested the meta-analyses' magnitude/definition; the curriculum frames it as an
  ongoing dispute rather than a settled refutation, which is the honest state.
- **Exact arXiv:2212.07763 internal findings** — the abstract and the program-comprehension
  literature it synthesizes were confirmed, but the PDF body did not render for direct
  quotation in this pass. Its role here is as a *modern synthesis* citation; the load-bearing
  empirical claims rest on the primary 1976–2008 sources, not on the SLR alone.

**Standing rule for future authors:** cite only sources you have actually verified or
that are well-established; if a spec citation looks wrong, **correct it and note the
correction here** — do not invent DOIs, and do not upgrade a `[Practitioner-canon]` or
`[Verified-adjacent]` claim to `[Verified]` without a primary source.
