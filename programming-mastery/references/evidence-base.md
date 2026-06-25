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
  doi:10.1145/1404520.1404531. `[Verified]` — The keystone result: **in combination,
  tracing of iterative code and "explain in plain English" accounted for ~46% of the
  variance in code-writing** ability (R² = 0.46). *(Precision note: the headline figure
  is the **46% combined variance**. Each skill alone is much weaker — iterative-tracing
  ≈15% (R²=0.15) and explaining ≈7% (R²=0.07) of writing variance. The "R² ≈ 0.66"
  previously cited here was **wrong**: 0.66 is not the model variance but the bivariate
  **correlation r ≈ 0.63** (r = 0.6267) between iterative-tracing and writing — a
  different quantity. Corrected to cite only the verified 46% combined-variance figure;
  see [Research notes](#research-notes).)*

**The intermediate skills (trace + explain-in-plain-English) and the SOLO
relational/multistructural distinction** — these peer-reviewed BRACElet/SOLO sources
ground module **A3** (tracing & explain-in-plain-English) and were verified during A3's
authoring:

- Lister, R., Fidge, C., & Teague, D. (2009). Further evidence of a relationship between
  explaining, tracing and writing skills in introductory programming. *ITiCSE '09*,
  161–165. doi:10.1145/1595496.1562930. `[Verified]` — Replication at a new institution,
  in **Python**, with non-parametric analysis: students who cannot trace usually cannot
  explain, and good writers have *usually* acquired both. The authors are explicit that
  this supports a **soft prerequisite *tendency*, not a strict gate** (one student wrote
  well despite failing both) — which is why A1/A2 are soft, not hard, prerequisites.
- Whalley, J. L., Lister, R., Thompson, E., Clear, T., Robbins, P., Kumar, P. K. A., &
  Prasad, C. (2006). An Australasian study of reading and comprehension skills in novice
  programmers, using the Bloom and SOLO taxonomies. *ACE 2006*, CRPIT Vol. 52, 243–252.
  `[Verified]` — Source of the **relational vs. multistructural** EiPE contrast: a
  *relational* answer states the code's **purpose**; a *multistructural* one is a
  *line-by-line* retelling. The novice signature is line-by-line narration.
- Lister, R., Simon, B., Thompson, E., Whalley, J. L., & Prasad, C. (2006). Not seeing
  the forest for the trees: novice programmers and the SOLO taxonomy. *ITiCSE '06*,
  118–122. doi:10.1145/1140124.1140157. `[Verified]` — Documents that experienced readers
  summarize at the relational (purpose) level while many novices retell line-by-line;
  the empirical root of A3's explain-in-plain-English half.
- Vainio, V., & Sajaniemi, J. (2007). Factors in novice programmers' poor tracing skills.
  *ITiCSE '07*, 236–240. doi:10.1145/1268784.1268853. `[Verified]` — Identifies
  **single-value tracing** (tracking only a variable's *latest* value rather than its
  history) as a documented novice tracing failure; grounds A3's common-error catalog.
- Sirkiä, T., & Sorva, J. (2012). Exploring programming misconceptions: an analysis of
  student mistakes in visual program simulation exercises. *Koli Calling '12*, 19–28.
  doi:10.1145/2401796.2401799. `[Verified]` — Function-call/parameter simulation and
  recursion-frame tracing appear as documented mistake clusters; grounds A3's
  call-tree/stack tracing errors.
- Cunningham, K., Blanchard, S., Ericson, B., & Guzdial, M. (2017). Using tracing and
  sketching to solve programming problems: replicating and extending an analysis of what
  students draw. *ICER '17*, 164–172. doi:10.1145/3105726.3106190. `[Verified]` —
  Replicating the Leeds Working Group (Lister et al. 2004): students who **sketch a
  trace** succeed more, and sketches that **track multiple values of the same variable
  over time** correlate most with correct answers — the empirical case for A3's
  "externalize state, don't hold it in your head" discipline.
- Lister, R., et al. — the BRACElet project (multi-institution, 2004 onward); see also
  "A closer look at tracing, explaining and code writing skills in the novice
  programmer" (Venables, Tan & Lister, *ICER '09*) and the Leeds Working Group (Lister
  et al. 2004, *ITiCSE-WGR '04*, "A multi-national study of reading and tracing skills in
  novice programmers").

→ Drives modules **A3** (tracing / explain-in-plain-English) and **B2** (writing).
Implication: build writing on a foundation of tracing and explaining; do not jump
learners straight to composition. **Caveat (per the standing rule):** BRACElet
establishes a **correlational hierarchy and a soft prerequisite ordering**, *not* a proof
that tracing *causes* writing ability — Lister, Fidge & Teague (2009) are explicit it is
a tendency with exceptions.

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

---

## Module-specific & craft sources

Grounding for the verification-cluster modules whose citations are **not** covered by the
Findings above. Each was verified against primary sources during that module's authoring and
is **badged here at its true tier** — the honesty rule holds: never present canon as verified
science, and never inflate contested empirical evidence. (A3's tracing/EiPE sources live with
[Finding 6](#6-reading--tracing--writing-is-a-developmental-hierarchy-verified); A2's chunking
sources with [Findings 2](#2-expertise-is-better-representation-experts-chunk-code-into-larger-semantic-units-verified)
& [3](#3-beacons-and-programming-plans-are-real-cues-experts-exploit-verified).)

### Testing & specifying correctness (module B3)

**B3 is mixed-status by design** (its file badge is `[Practitioner-canon]`): the test-*design*
techniques are craft, and the *only* empirical layer — TDD — is **genuinely contested**. The
coach must keep the two apart and must **not** sell TDD as proven.

**B3a — Test-design & oracle/property canon `[Practitioner-canon]` (methods/surveys).**
Respected, widely taught craft and peer-reviewed *survey/methods* papers — **not**
effectiveness experiments. The coach says: *"respected practice — not a verified research
finding."*

- Myers, G. J. (1979). *The Art of Software Testing.* Wiley (later eds. 2004/2011 with
  Sandler, Badgett, Thomas). Canonical source for **equivalence partitioning** and
  **boundary-value analysis**, and the argument that **exhaustive testing is generally
  impossible** — so the problem is choosing the cases most likely to find errors. Craft
  doctrine, not a replicated result.
- Dijkstra, E. W. (1969/1970). *Notes on Structured Programming* (EWD249); published as the
  lead essay in Dahl, Dijkstra & Hoare, *Structured Programming* (Academic Press, 1972).
  Source of the aphorism, verbatim: **"Program testing can be used to show the presence of
  bugs, but never to show their absence!"** A *logical* observation by a major figure, not
  data; provenance exactly verifiable (EWD249).
- Barr, E. T., Harman, M., McMinn, P., Shahbaz, M., & Yoo, S. (2015). The oracle problem in
  software testing: a survey. *IEEE TSE*, 41(5), 507–525. doi:10.1109/TSE.2014.2372785.
  Peer-reviewed **survey**. Defines the **test oracle** and names the **oracle problem**
  (deciding the correct behavior for an input is itself hard) — the motivation for properties.
- Claessen, K., & Hughes, J. (2000). QuickCheck: a lightweight tool for random testing of
  Haskell programs. *ICFP '00*, 268–279. doi:10.1145/351240.351266. Origin of
  **property-based testing**. SIGPLAN Most-Influential-Paper award. A **tool/methods** paper,
  **not** an empirical effectiveness study. *(Verified caveat: the original 2000 paper does
  NOT have built-in automatic shrinking — minimization of failing cases came later in the
  QuickCheck/Hedgehog/Hypothesis lineage.)*
- Hughes, J. (2019). How to specify it! A guide to writing properties of pure functions.
  *Trends in Functional Programming (TFP 2019)*, LNCS 12053, 58–83.
  doi:10.1007/978-3-030-47147-7_4. Practitioner tutorial: a taxonomy of property kinds
  (invariants, postconditions, metamorphic/algebraic relations, model-based). Canon/tutorial,
  not science.
- Chen, T. Y., Cheung, S. C., & Yiu, S. M. (1998). *Metamorphic testing: a new approach for
  generating next test cases.* Tech. Report HKUST-CS98-01, Hong Kong Univ. of Science &
  Technology. Origin of **metamorphic testing** (checking relations between *multiple*
  executions that hold even when the exact correct output is unknown). **⚠ Flag:** this is a
  **technical report**; its content here is sourced **via the Segura et al. 2016 survey**
  below, not from a directly-pinned TR copy — cite as origin-of-record, lean on the survey
  for the substance.
- Segura, S., Fraser, G., Sánchez, A. B., & Ruiz-Cortés, A. (2016). A survey on metamorphic
  testing. *IEEE TSE*, 42(9), 805–824. doi:10.1109/TSE.2016.2532875. Peer-reviewed **survey**;
  the load-bearing source for the metamorphic-relation material (and the verifying record for
  Chen et al. 1998).

**B3b — The TDD evidence layer `[Some empirical]` — MIXED / contested.** This is the only
part of B3 with replicated-ish empirical weight, and it is **honestly mixed**. **Do NOT inflate
to "TDD works."** The honest line: *specify behavior and work in small, steady steps; the
test-first ceremony is not what the evidence credits, and high coverage does not prove
correctness.*

- Rafique, Y., & Mišić, V. B. (2013). The effects of test-driven development on external
  quality and productivity: a meta-analysis. *IEEE TSE*, 39(6), 835–856.
  doi:10.1109/TSE.2012.28. Meta-analysis of 27 studies: TDD has **"a small positive effect on
  quality but little to no discernible effect on productivity,"** with the productivity drop
  tracking how much *more* the TDD group tested — a **confound**, not a clean TDD effect.
- Turhan, B., Layman, L., Diep, M., Erdogmus, H., & Shull, F. (2010). How effective is
  test-driven development? Ch. 12 in *Making Software* (O'Reilly, eds. Oram & Wilson),
  207–217. Narrative systematic review (22 reports / 32 trials): **"the evidence is not
  undisputedly consistent regarding TDD's effects on any of the measures,"** and the apparent
  external-quality benefit **"disappears after filtering out the less rigorous studies."**
- Fucci, D., Erdogmus, H., Turhan, B., Oivo, M., & Juristo, N. (2017). A dissection of the
  test-driven development process: does it really matter to test-first or to test-last?
  *IEEE TSE*, 43(7), 597–614. doi:10.1109/TSE.2016.2616877. **"Sequencing, the order in which
  test and production code are written, had no important influence"** — what helped was
  **granularity and uniformity** (small, steady steps). *The test-first ritual that defines
  TDD is not the active ingredient.* (Companion replication: Fucci et al. (2016), *An external
  replication … multi-site blind analysis*, *ESEM '16*, doi:10.1145/2961111.2962592 — TDD
  effects largely **not** significant.)
- Inozemtseva, L., & Holmes, R. (2014). Coverage is not strongly correlated with test suite
  effectiveness. *ICSE '14*, 435–445. doi:10.1145/2568225.2568271 (ACM Distinguished Paper;
  ICSE most-influential-paper N-10 in 2024). Once you **control for the number of test cases**,
  coverage is only *low-to-moderately* correlated with fault detection, and stronger coverage
  criteria don't help much: **high coverage ≠ good tests.** The empirical backstop for B3's
  "coverage is not correctness" anti-pattern. *(Page range 435–445 confirmed against ACM DL —
  the author's "not-fully-pinned" flag is now resolved.)*

### Metacognition & calibration (module F1)

**F1's general calibration science is `[Verified]` *as general cognitive/educational
psychology*; the programming-specific transfer is `[Verified-adjacent]`** (extrapolated, per
the tier table). It was established on **general-knowledge questions, text comprehension, and
classroom learning — not professional code** — so the coach says: *"solid learning science in
general; the programming-specific evidence is thinner."* (The AI-era amplification — METR 2025
/ Fernandes 2025 / Tankelevitch 2024 — is already in [AI-era impact](#ai-era-impact-202627-verified-adjacent)
and the [instructional pillar](#learning-science-instructional-pillar).)

- Flavell, J. H. (1979). Metacognition and cognitive monitoring: a new area of
  cognitive–developmental inquiry. *American Psychologist*, 34(10), 906–911.
  doi:10.1037/0003-066X.34.10.906. `[Verified]` (general) — Established **metacognition** and
  split it into **metacognitive knowledge** and **monitoring/experiences**; the *monitoring*
  half (flagging confusion *early*) is what F1 drills.
- Nelson, T. O., & Narens, L. (1990). Metamemory: a theoretical framework and some new
  findings. *Psychology of Learning and Motivation*, 26, 125–173. `[Verified]` (general) — The
  **monitoring ↔ control** framework (meta-level model of an object-level; information read
  *up* as monitoring, decisions sent *down* as control). F1's mechanism *is* this loop run
  against an external truth source (the runner).
- Lichtenstein, S., & Fischhoff, B. (1977). Do those who know more also know more about how
  much they know? *Organizational Behavior and Human Performance*, 20(2), 159–183.
  `[Verified]` (general) — Foundational calibration work: **systematic overconfidence** and the
  **hard–easy effect** (accuracy falls faster than confidence as tasks get harder, so
  overconfidence *grows* where being wrong costs most).
- Kruger, J., & Dunning, D. (1999). Unskilled and unaware of it. *Journal of Personality and
  Social Psychology*, 77(6), 1121–1134. doi:10.1037/0022-3514.77.6.1121. `[Verified]` (general)
  — The **dual burden**: the skills to *do* a task overlap the skills to *judge* whether you
  did it well, so the least skilled are least able to detect they're wrong — the rationale for
  measuring calibration **separately** from correctness. *(Note: the strongest popular
  *misreadings* of this paper are contested; F1 uses only the robust core — monitoring accuracy
  is itself a skill that can lag raw ability.)*
- Koriat, A., & Bjork, R. A. (2005). Illusions of competence in monitoring one's knowledge
  during study. *Journal of Experimental Psychology: LMC*, 31(2), 187–194.
  doi:10.1037/0278-7393.31.2.187. `[Verified]` (general) — The **fluency/foresight illusion**:
  information that is *present and easy to process* feels *known*. Programming cognate: code
  that **reads** smoothly feels **understood** — until you must predict its output or modify it.
- Dunlosky, J., & Rawson, K. A. (2012). Overconfidence produces underachievement: inaccurate
  self-evaluations undermine students' learning and retention. *Learning and Instruction*,
  22(4), 271–280. doi:10.1016/j.learninstruc.2011.08.003. `[Verified]` (general) —
  **Overconfidence causally degrades learning**: students who overestimate their understanding
  **stop studying too early**. Engineering cognate: overconfidence makes you **stop verifying
  too early** and ship the bug.

→ Drives module **F1** (metacognition & calibration). **Programming-specific transfer is
`[Verified-adjacent]`, not `[Verified]`:** that calibration training *causally improves
software work* is extrapolation, honestly labeled; the transfer task is the individual-level test.

### Code review craft (module E3)

Extends the **review-as-bottleneck** AI-era line and the empirical anchor **Bacchelli & Bird
2013** (already in [AI-era impact](#ai-era-impact-202627-verified-adjacent)). These are the
**craft `[Practitioner-canon]`** sources for the *how* of effective review — vetted against the
named sources during authoring; respected, widely taught wisdom, **not** measured causation.
(Weinberg's *Psychology of Computer Programming* — egoless review — is already on the
[reading spine](#reading-spine-book-canon).)

- Google. *eng-practices: The Standard of Code Review* (Google Engineering Practices
  Documentation). `[Practitioner-canon]` — "The primary purpose of code review is to make sure
  that the overall **code health** of the codebase is improving over time"; **"there is no such
  thing as 'perfect' code — only better code"**; "**technical facts and data overrule opinions
  and personal preferences**"; comment **on the code, not the developer**; prefix non-blocking
  polish with "**Nit:**". Reviewers look at **design, functionality, complexity, tests, naming,
  comments, style** — design first. <https://google.github.io/eng-practices/review/reviewer/standard.html>
- Greiler, M. — code-review practice and research (e.g. *Code Reviewing in the Trenches*,
  *IEEE Software*, 2018, with Bird, Bacchelli & others; and her *Code Review Pyramid* /
  Microsoft developer-productivity work). `[Practitioner-canon]` — practical guidance on
  review *effectiveness*, reviewer guidelines, and prioritizing high-value feedback over
  mechanical nits; the craft companion to the Bacchelli & Bird empirical core.

→ Drives module **E3** (code review). The *concept* leans on Bacchelli & Bird 2013 (one
in-depth field study — direction, not replicated causation); the *how* is `[Practitioner-canon]`
(Google + Greiler + Weinberg). The AI-era priority that makes review the apex verification
skill is `[Verified-adjacent]` — priority-steering, not proof.

### Systematic debugging method (module C1)

Extends **Finding 4** (comprehension is active and hypothesis-driven — Brooks 1983; Pennington 1987; von Mayrhauser & Vans 1995; already in [Verified findings](#4-comprehension-is-active-and-hypothesis-driven-verified)), which supplies C1's **`[Verified]` model half**: debugging proceeds as *predict → check*, not reading until it "clicks." The sources below are the **craft `[Practitioner-canon]`** anchors for C1's **method half** — the disciplined loop, bisection, and input minimization — vetted against the named primary sources during authoring; respected, widely taught wisdom, **not** measured causation. (Zeller's *Why Programs Fail* is already on the [reading spine](#reading-spine-book-canon); itemized here for the specific claims C1 cites.)

- Zeller, A. (2009). *Why Programs Fail: A Guide to Systematic Debugging* (2nd ed.). Morgan Kaufmann. ISBN 978-0-12-374515-6. `[Practitioner-canon]` — The **scientific method of debugging**: from a working theory of the program, **generate a hypothesis**, **design an experiment that could falsify it**, run it, fold the result back into the theory, and **repeat until the theory explains the failure**, recorded in an explicit **debugging logbook**. The observe→hypothesize→predict→test loop C1 drills. Craft doctrine, not an effectiveness experiment.
- Zeller, A., & Hildebrandt, R. (2002). Simplifying and isolating failure-inducing input. *IEEE Transactions on Software Engineering*, 28(2), 183–200. doi:10.1109/32.988498. `[Practitioner-canon]` (algorithm/methods) — **Delta debugging / `ddmin`**: systematically shrink a failing input (or change set) to the **minimal** part that still triggers the failure, and isolate the difference between a passing and a failing run. The basis for C1's **bisection** (over commits) and **input-minimization** drills. A tool/algorithm paper; the famous Mozilla case (896 HTML lines → 1) is an illustration, not a controlled effectiveness study.
- Agans, D. J. (2002). *Debugging: The 9 Indispensable Rules for Finding Even the Most Elusive Software and Hardware Problems.* AMACOM. ISBN 978-0-8144-7457-0. `[Practitioner-canon]` — The nine rules, verbatim: **Understand the System · Make It Fail · Quit Thinking and Look · Divide and Conquer · Change One Thing at a Time · Keep an Audit Trail · Check the Plug · Get a Fresh View · If You Didn't Fix It, It Ain't Fixed.** Agans is explicitly **observation-first** — his "Quit Thinking and Look" chapter takes its epigraph from Sherlock Holmes's "it is a capital mistake to theorize before one has data" (Conan Doyle, *A Scandal in Bohemia*) — which is why C1 puts *Observe* before *Hypothesize*. War-stories-and-rules craft book, not empirical research.

→ Drives module **C1** (systematic / hypothesis-driven debugging). The *model* is `[Verified]` (Finding 4); the *method* is `[Practitioner-canon]` (above). **Hard honesty bound (already recorded in [Refuted under verification](#refuted-under-verification)):** do **not** claim systematic debugging is *causally* superior to skilled ad-hoc debugging — that exact claim ("systematic control/data-flow tracing causally yields better mental models and fewer errors than as-needed reading") was **refuted**. C1 sells the method as **tractability + falsifiability** (a reliable fallback when intuition stalls, and a guard against the "I think it's fixed" failure), never as a proven performance edge. The AI-era priority placing C1 in the verification cluster (debugging code one didn't write rises as agents draft it; spec §12) is `[Verified-adjacent]` — priority-steering, not proof.

### Reading stack traces & error messages (module C2)

**C2 is mixed-status by design** (its file badge is `[Practitioner-canon]`): the trace-*reading
technique* is craft, grounded by the **`[Verified]`** principles already in this file —
[Finding 1](#1-the-notional-machine-is-the-durable-barrier--not-syntax-verified) (a traceback
*is* the notional machine's call stack made visible) and
[Finding 4](#4-comprehension-is-active-and-hypothesis-driven-verified) (debugging is
evidence-driven prediction→check, and the traceback is the cheapest evidence available). The
coach must keep the two apart: *the four-move reading procedure is respected practice, not a
controlled finding; what each exception class and chaining line **mean** are documented facts.*

**C2 — Traceback semantics & the read-bottom-up procedure `[Practitioner-canon]` (docs/spec
facts + craft).** Primary, verifiable sources for *what a traceback is*, *what each built-in
exception class signals*, and *what the chaining lines mean* — pinned to the Python
documentation and the language spec; the *reading order* itself is craft consensus, badged
accordingly. The coach says: *"this is respected practice on a verified foundation — not a
verified research result of its own."*

- **The Python Tutorial — §8 "Errors and Exceptions"; and the Python Library Reference —
  "Built-in Exceptions" (docs.python.org).** `[Practitioner-canon]` (documentation, factual).
  §8.2 describes the traceback verbatim: the error message "contains a stack traceback listing
  source lines; however, it will not display lines read from standard input." §8.5 "Exception
  Chaining" documents implicit chaining and the `raise … from` / `from None` forms. The
  Built-in Exceptions page is the **origin-of-record for what each class signals**
  (`NameError`, `UnboundLocalError`, `TypeError`, `AttributeError`, `KeyError`, `IndexError`,
  `ValueError`, `RecursionError`, …) — the grounding for C2's exception-class catalog (§5c).
  *Verified against docs.python.org/3/tutorial/errors.html (§8.2, §8.5 confirmed) in this
  pass.*
- **PEP 3134 — "Exception Chaining and Embedded Tracebacks" (Ka-Ping Yee, 12 May 2005;
  targets Python 3.0).** `[Practitioner-canon]` (language spec, factual). Defines the two
  chaining attributes and their rendered banners: **`__context__`** (implicit) →
  **"During handling of the above exception, another exception occurred"**; **`__cause__`**
  (explicit `raise … from …`) → **"The above exception was the direct cause of the following
  exception"**; plus **`__traceback__`**. This is the load-bearing source for C2's
  "which traceback holds the original cause" Advanced skill. *Verified against
  peps.python.org/pep-3134 (author, date, target version, both message strings, and the
  `__context__`/`__cause__`/`raise … from` semantics all confirmed verbatim) in this pass;
  the two banner strings were independently re-confirmed as live runner output.* **Correction
  recorded:** an early draft of the C2 module attributed PEP 3134 to "Cannon & Yee" — the
  actual sole author is **Ka-Ping Yee**; corrected at the source.
- **The read-bottom-up reading order** — `[Practitioner-canon]` (craft). The verifiable
  anchor is the Python docs' own header, **"Traceback (most recent call last)"**: by
  construction the **last** line is the failure (the exception type + message) and the
  **bottom** frame is where it raised, so the trace is meant to be read bottom-first. The
  further "walk up to the deepest frame that is *your* code (skip library/stdlib internals)"
  step is widely-taught practitioner consensus, **not** a measured result — badged as craft,
  not science. *(No specific book was pinned for this step in this pass; it rests on the
  verified docs framing plus practitioner consensus, deliberately citing less rather than
  asserting an unverified page.)*

→ Drives module **C2** (reading stack traces & error messages). The *technique* (bottom line
first → deepest your-code frame → site-vs-cause → map onto the machine) is
`[Practitioner-canon]`; the *foundation* it rests on is `[Verified]` (Findings 1 & 4); what
the exception classes and chaining lines **mean** are documented **facts** (Python docs; PEP
3134). The **AI-era priority** that makes fast trace-reading part of the verification cluster
(as agents draft code, the first artifact of a failure is a traceback; spec §12) is
`[Verified-adjacent]` — priority-steering, not proof. **Research note:** every traceback used
in C2's worked example and its nine tier exemplars is **real runner output** (Python 3.13),
independently re-run from scratch during authoring and confirmed byte-for-byte against the
pasted keys (exception class, frame line numbers, fine-grained caret spans, and the chaining
banners); the executable grading path means the coach reads the *actual* `stderr`, never a
guessed one.

### Production & concurrency debugging (module C3)

Extends **Finding 1** (the notional machine) into the *concurrent* setting, and the
**systematic-debugging** line anchored by Zeller (already on the
[reading spine](#reading-spine-book-canon): *Why Programs Fail*, "anchors C1 and C3"). C3 is
**mixed-status** (its file badge is `[Verified-adjacent]`): the concurrency *taxonomy* is a strong
empirical characterization, and the production-debugging *method* is craft. The coach must keep the
two apart and must **not** sell the method as verified science.

**C3a — The concurrency-bug taxonomy `[Verified-adjacent]` (empirical characterization).** The
single best real-world characterization of what concurrency bugs *look like* — strong empirical
footing, but **descriptive field data**, from C/C++ applications circa 2008, **not** a causal
learning result and **not** Python. It is `[Verified-adjacent]` because it *extends* the verified
execution-model finding (Finding 1) into the concurrent setting on solid empirical ground — not
because the *pedagogy* is proven.

- Lu, S., Park, S., Seo, E., & Zhou, Y. (2008). Learning from mistakes: a comprehensive study on
  real-world concurrency bug characteristics. *ASPLOS '08* (13th Int'l Conf. on Architectural
  Support for Programming Languages and Operating Systems), 329–339.
  doi:10.1145/1346281.1346323. `[Verified-adjacent]` — The first comprehensive real-world
  concurrency-bug study: **105 randomly selected bugs** from four large mature open-source
  applications (**MySQL, Apache, Mozilla, OpenOffice**), split into **74 non-deadlock and 31
  deadlock**. Findings that ground C3 (numbers + wording verified against the primary PDF during
  authoring): *Finding (1):* "**Most (72 out of 74) of the examined non-deadlock concurrency bugs
  are covered by two simple patterns: atomicity-violation and order-violation**" (Table 4: 51
  atomicity, 24 order, 2 other; 3 counted as both). *Definitions (verbatim):* an **atomicity
  violation** is when "the desired serializability among multiple memory accesses is violated";
  an **order violation** is when "the desired order between two (groups of) memory accesses is
  flipped." *Finding (2):* "**A significant number (24 out of 74) ... are order bugs**" — and
  order bugs "may not be easily expressed via synchronization primitives like locks." *Finding
  (3):* "**The manifestation of most (101 out of 105) ... involves no more than two threads**"
  (96%); *Finding (5):* "**Many (66%) ... [involve] concurrent accesses to only one variable**"
  (34% involve multiple variables). *Finding (9):* "**Three quarters (73%) of the examined
  non-deadlock bugs are fixed by techniques other than adding/changing locks**". ASPLOS
  Influential Paper Award 2022. *(Research note: the abstract phrases Finding (1) as "almost all
  (97%)"; the body's exact count is "72 out of 74" — C3 cites the precise body figure. The
  canonical proceedings DOI is 10.1145/1346281.1346323; SIGARCH/SIGOPS/SIGPLAN co-prints carry
  1353534/1353535.1346323. All figures and the two definitions verified against the freely
  available author PDF.)*

**C3b — Production / observability-driven debugging `[Practitioner-canon]` (method).** Respected,
widely taught craft for debugging a live system you cannot pause — vetted against the named sources
during authoring; **not** an effectiveness experiment. The coach says: *"respected practice — not a
verified research finding."* (Per [Refuted](#refuted-under-verification), that *systematic tracing
causally* beats skilled as-needed reading was **not** established; the method is taught as
disciplined practice, exactly as C1's is.)

- Zeller, A. (2009). *Why Programs Fail: A Guide to Systematic Debugging* (2nd ed.). Morgan
  Kaufmann. ISBN 978-0-12-374515-6. `[Practitioner-canon]` — Already on the
  [reading spine](#reading-spine-book-canon). Debugging as the **scientific method run against a
  program**: from an observed failure, form a **hypothesis** about the cause, **predict** a
  checkable consequence, **observe**, and **refine** — narrowing systematically rather than
  guessing. C3 stresses the parts that bite at scale: **reproduction** (a failure you cannot
  reproduce on demand is the hardest case) and reasoning from **recorded** evidence when you cannot
  re-run at will.
- Majors, C., Fong-Jones, L., & Miranda, G. (2022). *Observability Engineering: Achieving
  Production Excellence.* O'Reilly. ISBN 978-1-492-07644-5. `[Practitioner-canon]` — The anchor for
  the observability-driven stance: in production you **cannot attach a debugger and step** (remote,
  concurrent, intermittent), so you debug from the **evidence the running system emits** —
  structured **logs**, **metrics**, distributed **traces** — and the engineering goal is to emit
  *enough* of the right evidence to ask new questions of past behavior **without shipping code to
  reproduce it**. *(Verified: 1st-ed. authors Majors, Fong-Jones & Miranda, 2022; the 2nd ed.,
  2024, adds Austin Parker — C3 cites the 1st edition's author list.)*

→ Drives module **C3** (production & concurrency debugging). The *what* (the atomicity/order
taxonomy; bugs are small — two threads, one variable; locks aren't the universal fix) leans on Lu
et al. 2008 (`[Verified-adjacent]` — strong characterization, not proven pedagogy); the *how*
(hypothesis-driven reasoning under non-reproducibility; reason from emitted evidence) is
`[Practitioner-canon]` (Zeller + the observability canon). Sibling module **A4 (concurrency mental
models)** — not yet built — will own the *concurrent notional machine itself* (interleavings,
happens-before, memory models); C3 uses the slice of that model it needs and references A4 softly.

---

### Managing complexity & abstraction (module D1)

**D1 is `[Practitioner-canon]` by design** (its file badge is `[Practitioner-canon]`): its core
is a respected practitioner *philosophy* on a foundational design-principle paper, and its only
contact with empirical literature is a **counterweight** — the famous complexity *metric* is
weak/contested. The coach must keep these apart and must **never** present the craft as verified
science or let a metric stand in for "real" complexity. (Ousterhout's *A Philosophy of Software
Design* is already on the [reading spine](#reading-spine-book-canon) — *"Complexity, deep vs
shallow modules. Craft anchor for D1–D3"*; itemized here for the specific claims D1 cites.)

**D1a — Complexity & deep-module philosophy `[Practitioner-canon]` (craft).** Respected, widely
taught design wisdom, vetted against the named source during authoring — **not** an effectiveness
experiment. The coach says: *"a useful, respected lens — one experienced engineer's philosophy,
not a measured result."*

- Ousterhout, J. K. (2018; **2nd ed.** July 2021). *A Philosophy of Software Design.* Yaknyam
  Press. ISBN 978-1-7321022-0-0 (1st ed.); 978-1-7321022-1-7 (2nd ed.). `[Practitioner-canon]` —
  Source of D1's whole vocabulary, confirmed against the text during authoring: **complexity** is
  *"anything related to the structure of a software system that makes it hard to understand and
  modify the system"*; its **two causes** are **dependencies** and **obscurity**; its **three
  symptoms** are **change amplification**, **cognitive load**, and **unknown-unknowns** (the
  *worst*). The central craft move: **deep modules** (powerful functionality behind a *simple
  interface*) over **shallow** ones (interface ≈ implementation in complexity); *"it is more
  important for a module to have a simple interface than a simple implementation"* (**pull
  complexity downward**); and **tactical vs strategic** programming (invest continuously in design
  rather than just shipping features). **⚠ Honesty flag:** the book is **explicitly opinion** —
  Ousterhout opens by asking *"what makes me think I know all the answers about software design? To
  be honest, I don't"* and tells the reader to *"take the suggestions in this book with a grain of
  salt."* It distills his Stanford **CS190** course (classroom experience, not a study), and parts
  of it — notably **module depth / "classitis"** — are **genuinely contested** among experienced
  engineers. Craft doctrine, not science.

**D1b — The information-hiding foundation `[Practitioner-canon]` (foundational design principle).**

- Parnas, D. L. (1972). "On the Criteria To Be Used in Decomposing Systems into Modules."
  *Communications of the ACM*, 15(12), 1053–1058. doi:10.1145/361598.361623. `[Practitioner-canon]`
  (foundational) — The origin of **information hiding** and the answer to *what* a deep module
  should hide: decompose a system so that **each module hides a design decision that is likely to
  change**, behind an interface that does not change when the decision does. Parnas contrasts two
  decompositions of one program (a conventional flowchart split vs. an information-hiding split) and
  argues the latter yields modules that can be **changed independently** and **understood
  independently**. The classic origin of the deep-module / encapsulation line; Ousterhout's "deep
  module" is largely "a module that hides a likely-to-change decision well." A design *criterion*
  and argument by a major figure — **not** an empirical result. *(Citation, venue, pages, and the
  information-hiding / likely-to-change-decision thesis verified against the CACM record during D1's
  authoring.)*

**D1c — Complexity metrics are weak/contested `[Some empirical, contested]` — the honest fence.**
Included **precisely to keep the module honest**: the number people reach for to "measure
complexity" does **not** measure what D1 is about. **Do NOT use a metric to settle a design
question or to upgrade D1's craft core toward `[Verified]`.**

- McCabe, T. J. (1976). "A Complexity Measure." *IEEE Transactions on Software Engineering*,
  SE-2(4), 308–320. doi:10.1109/TSE.1976.233837. `[Some empirical, contested]` — Defines
  **cyclomatic complexity** (independent paths through a function), proposed as a reliability/
  testability predictor. As a **defect predictor it is weak and contested**.
- Shepperd, M. (1988). "A critique of cyclomatic complexity as a software metric." *Software
  Engineering Journal*, 3(2), 30–36. doi:10.1049/sej.1988.0003. `[Some empirical, contested]` —
  Argues the metric rests on *"poor theoretical foundations"* and that *"for a large class of
  software it is no more than a proxy for, and in many cases is outperformed by, lines of code."*
  The standing critique that cyclomatic complexity mostly re-measures **size**. *(Verified caveat,
  re-confirmed during D1 authoring: cyclomatic complexity is strongly correlated with LOC, and
  **"reducing the cyclomatic complexity of code is not proven to reduce the number of errors or
  bugs"**; Les Hatton's finding that it has "the same predictive ability as lines of code" is the
  same conclusion. The coach NEVER claims a metric measures "real" complexity.)*

→ Drives module **D1** (managing complexity / abstraction). The *concept* (deep vs shallow,
dependencies + obscurity, the three symptoms, pull complexity down, tactical vs strategic) is
`[Practitioner-canon]` (Ousterhout); the *foundation* (hide the decision likely to change) is
`[Practitioner-canon]`, foundational (Parnas 1972); the metric literature is the
`[Some empirical, contested]` **fence** that stops design quality being treated as a measurable
scalar. **Hard honesty bounds:** (1) Ousterhout's philosophy is opinion from a course, not a study,
and "classitis"/module-depth is genuinely contested — never "research shows." (2) **"Good
abstractions / refactoring toward depth reduce bugs" is NOT an established empirical finding** —
plausible craft only; keep the claimed win as *understandability and changeability*, not measured
defect rates. (3) **Mechanical-sympathy / cache-locality** arguments (a cousin of "pull complexity
down") matter in systems/HFT but are **overstated for typical application code**; D1 does not lean
on them. The AI-era priority placing D1 in the verification cluster (judging whether an
agent-generated abstraction is deep or just plausible-looking rises as agents draft code; spec §12)
is `[Verified-adjacent]` — priority-steering, not proof. **Research note:** every snippet in D1's
worked example and its nine tier exemplars is **real runner output** (Python 3.13), independently
re-run from scratch during authoring and confirmed byte-for-byte against the pasted keys; because
design quality is *not* executable ground truth, the runner is used only to pin **behavioral**
sub-claims — most often that two designs are **behaviorally identical** (so any difference between
them is a *complexity* difference, e.g. the worked example's `same? True`), or that a leaked
invariant **actually bites** (a temporal-decomposition class raises when called out of order) — and
the *design verdict* is rubric-graded against the golden exemplars, named out loud as softer than an
executable pass.

### Naming & identifier comprehension (module D2)

**D2 is mixed-status by design** (its file badge is `[Practitioner-canon]`), and the split is
sharper here than elsewhere in Track D *because a genuine empirical layer exists*: controlled
experiments support "**descriptive identifiers aid comprehension**" at `[Some empirical]`, while
the specific prescriptions (what "precise" means, the precision+consistency doctrine, length/style
heuristics) are `[Practitioner-canon]`. The honesty rule binds hard: badge the empirically-supported
claim distinctly from the craft, do **not** let the famous design book borrow the empirical layer's
credibility, and do **not** present a naming *convention* as proven. (Ousterhout's *A Philosophy of
Software Design* is already on the [reading spine](#reading-spine-book-canon) as a D1–D3 anchor;
itemized here for the specific Ch. 14 claims D2 cites.)

**D2a — Identifier-comprehension evidence `[Some empirical]` (controlled experiments).** Real but
narrow empirical work; the *direction* (descriptive > cryptic) is supported, the fine ordering is
not settled, and no *convention* is proven. The coach says: *"controlled studies show descriptive
names help comprehension — not that any naming rule is proven."*

- Hofmeister, J., Siegmund, J., & Holt, D. V. (2017). Shorter identifier names take longer to
  comprehend. *SANER 2017* (IEEE 24th Int'l Conf. on Software Analysis, Evolution and
  Reengineering), 217–227. doi:10.1109/SANER.2017.7884623. (Extended journal version: *Empirical
  Software Engineering* 24(1), 417–443, 2019, doi:10.1007/s10664-018-9621-x.) `[Some empirical]` —
  Controlled **within-subjects** experiment, **72 professional C# developers** who **looked for
  defects** in code in three identifier styles (**letters, abbreviations, words**), with
  defect-finding time measured. **Verified headline (abstract, verbatim):** *"words lead to, on
  average, 19% faster comprehension speed compared to letters and abbreviations, but we did not
  find a significant difference in speed between letters and abbreviations."* This is the
  load-bearing source for "descriptive names help." **The 19% belongs to THIS paper** (defect-find
  speed, full words over BOTH letters and abbreviations) — *not* to Lawrie 2006 (see research
  note). The authors' own framing of the effect is modest ("fairly small").
- Lawrie, D., Morrell, C., Feild, H., & Binkley, D. (2006). What's in a Name? A Study of
  Identifiers. *ICPC 2006* (14th IEEE Int'l Conf. on Program Comprehension), 3–12.
  doi:10.1109/ICPC.2006.51. `[Some empirical]` — **128 participants** rated descriptions of twelve
  functions shown in three variants (**full words / abbreviations / single letters**); free-form
  descriptions scored 0–5 by two raters (κ = 0.71). **Verified (abstract):** *"full word
  identifiers lead to the best comprehension; however, in many cases, there is no statistical
  difference between full words and abbreviations."* **Verified (results):** full words give
  significantly better description ratings than single letters; *"There is never a statistical
  difference between full words and abbreviations."* Measured **description quality + confidence**,
  **not speed**. Note the honest tension with Hofmeister: both agree **words > single letters**,
  but Lawrie found **abbreviations ≈ full words** while Hofmeister found **abbreviations ≈ letters**
  — the abbreviation ordering is genuinely unsettled across studies.
- Feitelson, D. G., Mizrahi, A., Noy, N., Ben Shabat, A., Eliyahu, O., & Sheffer, R. (2022). How
  Developers Choose Names. *IEEE Transactions on Software Engineering* 48(1), 37–52.
  doi:10.1109/TSE.2020.2976920. (Preprint arXiv:2103.07487.) `[Some empirical]` — **334 subjects**
  chose names for given scenarios. Two verified findings frame D2's humility: (1) **no single
  "correct" name** — *"in the 47 instances in our experiments the median probability [that two
  developers pick the same name] was only 6.9%"*; yet (2) **a chosen name is usually legible** —
  *"given that a specific name is chosen, it is usually understood by the majority of developers."*
  Their model (pick concepts → choose words → assemble) produced names judged superior ~2:1, using
  *more concepts and longer names*. So naming is underdetermined (don't bikeshed the "right" name),
  but precision and concept-coverage measurably aid legibility.

**D2b — Naming style/casing is CONTESTED `[Some empirical] — mixed/weak`.** Flag explicitly: the
camelCase-vs-snake_case studies **contradict each other**, so style/casing is **not** an
empirically settled convention. What is defensible is **consistency**; the *winner* is not.

- Binkley, D., Davis, M., Lawrie, D., & Morrell, C. (2009). To CamelCase or Under_score. *ICPC
  2009* (17th IEEE Int'l Conf. on Program Comprehension), 158–167. doi:10.1109/ICPC.2009.5090039.
  `[Some empirical]` — **135 subjects**, timed identifier-recognition task: camelCase gave **higher
  accuracy**, and subjects *trained* in camelCase recognized it faster — **but all subjects were on
  average 13.5% *slower* on camelCase than underscore** (p < 0.0001).
- Sharif, B., & Maletic, J. I. (2010). An Eye Tracking Study on camelCase and under_score
  Identifier Styles. *ICPC 2010*, 196–205. doi:10.1109/ICPC.2010.41. `[Some empirical]` —
  Eye-tracking replication of Binkley et al.: found **"no difference in accuracy between the
  [styles]."** Reading-research on un-spaced text suggests camelCase trade-offs. Net:
  small, training-dependent, contradictory — *do not* assert a style winner.

**D2c — Naming craft `[Practitioner-canon]` (precision, consistency, "names are documentation").**
Respected, well-argued craft, vetted during authoring against the named source — **not** empirical
findings. The coach says: *"respected practice — not a verified research result."*

- Ousterhout, J. (2018/2021). *A Philosophy of Software Design*, Ch. 14 "Choosing Names."
  ISBN 978-1-7321022-0-0. `[Practitioner-canon]` — The craft anchor. Verbatim positions verified
  against the text: **"Good names are a form of documentation: they make code easier to understand.
  They reduce the need for other documentation and make it easier to detect errors."** The goal is
  to **"create an image in the mind of the reader… what the underlying entity is, and, just as
  important, what it is not."** **"Good names have two properties: precision and consistency."**
  Consistency's three requirements, verbatim: *"first, always use the common name for the given
  purpose; second, never use the common name for anything other than the given purpose; third,
  make sure that the purpose is narrow enough that all variables with the name have the same
  behavior."* Two red flags, verbatim: **"Red Flag: Vague Name"** and **"Red Flag: Hard to Pick
  Name."** Illustrated by the author's six-month `block` data-corruption bug (one name used for
  *disk block* and *file block*). **Honest counterpoint the book itself prints:** §14.5 quotes the
  Go camp (Andrew Gerrand: *"long names obscure what the code does"*) and shows a single-letter
  example its authors consider *more* readable — so even the canon concedes name *length* is a
  matter of taste, not law.
- Martin, R. C. (2008). *Clean Code*, Ch. 2 "Meaningful Names." ISBN 978-0-13-235088-4.
  `[Practitioner-canon]` — **cite with care; contested opinion, not consensus.** Popularized
  intention-revealing names, avoid-disinformation, pronounceable names; some overlaps the precision
  principle. But the book's broader prescriptions (function length, structure) are widely disputed
  in the profession, so the coach must **not** present it on a par with Ousterhout's narrower,
  better-argued naming chapter. D2 leans on a *Clean Code* point only where it also stands on its
  own or on the empirical layer — never on the book's authority alone.

→ Drives module **D2** (naming). The *direction* (descriptive identifiers aid comprehension; no
uniquely correct name but precision/concept-coverage help) is `[Some empirical]` (Hofmeister 2017;
Lawrie 2006; Feitelson 2022); naming *style/casing* is contested (Binkley 2009 vs Sharif & Maletic
2010) and **not** a proven convention; the *technique* (precise + consistent + never-lying; the two
red flags) is `[Practitioner-canon]` (Ousterhout Ch. 14; *Clean Code* with care). D2's **lying-name**
half is **executable**: a name that claims one behavior while the code does another is convicted by
**running the code** — the authored-side twin of A2's lying-name reading skill and A1's superbug. The
AI-era priority placing "does this name tell the truth about the behavior?" in the verification
cluster (fluent agent output produces plausible-sounding names that may not match the code; spec §12)
is `[Verified-adjacent]` — priority-steering, not proof.

**Research note (verified against primary sources; one correction recorded).** The Hofmeister 2017
"**19% faster comprehension speed**" figure and "**no significant difference between letters and
abbreviations**," the N=72 C# defect-finding design, and the Lawrie 2006 "**full word… best…; no
statistical difference between full words and abbreviations**" + N=128 + κ=0.71 were confirmed
verbatim against the authors' own PDFs. Feitelson 2022's **6.9%** median name-agreement and "**usually
understood by the majority of developers**" and N=334 were confirmed against the abstract. The
Binkley 2009 **13.5%-slower-camelCase** (p<0.0001) and Sharif & Maletic 2010 **no-accuracy-difference**
were confirmed against the Sharif & Maletic primary PDF (which quotes Binkley's result). All
Ousterhout Ch. 14 quotes were confirmed against the book text. **Correction recorded:** a widespread
secondary-source claim attributes "**~19% increase in comprehension**" to **Lawrie et al. 2006** —
this figure is **NOT in that paper** (which measured description-quality ratings, not speed). The 19%
is **Hofmeister et al. 2017**'s defect-finding-speed result. D2 cites the 19% to Hofmeister only, and
states the Lawrie finding qualitatively (full words best; words = abbreviations; both > single
letters). Exact TSE page range for Feitelson 2022 is cited from the TSE 48(1) record (37–52); if a
module needs to pin the page range to the page, treat it as the one detail to re-confirm against the
publisher copy.

### Refactoring judgment (module D3)

Extends the **reading-spine** anchors **Fowler, *Refactoring* (2nd ed., 2018)** and **Feathers,
*Working Effectively with Legacy Code* (2004)** (already on the [reading spine](#reading-spine-book-canon))
into a teachable judgment skill. **D3 is `[Practitioner-canon]` (craft) with one EXECUTABLE
definition-anchor** (behavior preservation, enforced by the runner). The coach must keep these
apart: the *definition* is verifiable by execution; the *discipline and judgment* are respected
craft, **not** measured causation; and the *outcome* claim ("refactoring reduces bugs / improves
maintainability") is **explicitly not established**.

**D3a — The definition-anchor: behavior preservation `[Practitioner-canon]` (a definition the
runner enforces).** Refactoring is *defined* by unchanged observable behavior, so "is this a
refactor?" is decidable by running the same inputs through the BEFORE and AFTER code and diffing
`stdout`/`status`. This is a **definition**, not an empirical finding; and the runner is a
**falsifier** (one differing input disproves "refactor"), not a proof of total equivalence (the
Dijkstra "presence not absence" caveat in [B3a](#testing--specifying-correctness-module-b3)).

- Fowler, M. (2018). *Refactoring: Improving the Design of Existing Code* (2nd ed.).
  Addison-Wesley. ISBN 978-0-13-475759-9. `[Practitioner-canon]` — Source of the **definitions**
  (verified verbatim against martinfowler.com → *DefinitionOfRefactoring*, mirrored in ch. 2):
  refactoring *(noun)* is **"a change made to the internal structure of software to make it easier
  to understand and cheaper to modify without changing its observable behavior"**; *(verb)* **"to
  restructure software by applying a series of refactorings without changing its observable
  behavior."** Also the discipline of **small steps under tests** (make a tiny change, run the
  tests, so a red test localizes the mistake to the last step — ch. 1, paraphrased, not pinned),
  the **Two Hats** (at any moment you are *either* adding behavior *or* refactoring — never both in
  one step), and the **Rule of Three** (ch. 2, attributed to **Don Roberts**: refactor on the
  third duplication, not the first). Craft doctrine, not an effectiveness experiment. *(Verified:
  both definitions confirmed verbatim on martinfowler.com/bliki/DefinitionOfRefactoring.html;
  Rule-of-Three attribution to Don Roberts confirmed across multiple secondary sources; the exact
  Roberts wording is cited in its standard published form, not as a page-pinned quote.)*
- Beck, K. (2012, Sep 25). *"for each desired change, make the change easy (warning: this may be
  hard), then make the easy change."* `[Practitioner-canon]` — The **preparatory-refactoring**
  line: when a feature is awkward to add, first refactor (behavior-preserving) so the new shape
  fits, then add it. The operational form of "refactor the code you are about to touch." *(Verified
  verbatim against Beck's own post: x.com/KentBeck/status/250733358307500032, dated 2012-09-25.)*

**D3b — Legacy code & characterization tests `[Practitioner-canon]` (the "when not to refactor
yet" discipline).** The honest answer to "refactor untested code?" is: **not until you have pinned
its behavior with a characterization test first** — the quirk may be load-bearing.

- Feathers, M. C. (2004). *Working Effectively with Legacy Code.* Prentice Hall (Robert C. Martin
  Series). ISBN 978-0-13-117705-5. `[Practitioner-canon]` — Source of the operational definition
  **"legacy code is code without tests"** (*old* isn't the problem; *untested* is, because you
  cannot change it safely) and the **characterization test** — "a test that characterizes the
  actual behavior of a piece of code": when code has no tests, you do **not** clean it up first;
  you pin its *current* behavior (including its weird corners) with characterization tests, then
  refactor under that green net. Also the **seams / dependency-breaking** techniques for getting
  untestable code into a harness. Craft doctrine, not an effectiveness experiment. *(Verified:
  definition and characterization-test concept confirmed against multiple authoritative summaries
  and the book's Internet Archive copy; not independently page-pinned in this pass — cited as
  origin-of-record for the concepts.)*

**Honesty bound for D3 (the load-bearing one).** Refactoring is **respected craft, not a verified
intervention.** Its *causal* effect on defect rate and long-term maintainability has only **mixed,
contradictory, and limited** empirical support — studies disagree (some report fewer defects after
refactoring, others report *more* bug reports following heavy refactoring, and at least one large
study found *no clear effect* on maintainability/modifiability). **Do NOT claim "refactoring
reduces bugs" or "improves maintainability" as proven.** The one part that *feels* verified —
behavior preservation — is a **definition enforced by the runner**, not an empirical outcome
finding. *(Research note: the "mixed/contradictory" characterization here rests on a secondary
synthesis of the refactoring-vs-defects literature [e.g. the often-contrasted Ratzinger et al.
2008 vs. Weißgerber & Diehl 2006, and Bavota et al. 2015's "no clear effect" on
maintainability/modifiability]; these individual primaries were **not** each pinned against their
own PDFs in this pass, so the module cites the *direction* — "the evidence is mixed and limited" —
and deliberately does **not** cite a specific effect size. Cite less, not more.)*

→ Drives module **D3** (refactoring judgment). The *definition* (D3a) is verifiable by the runner;
the *discipline and judgment* (D3a Two-Hats/Rule-of-Three/small-steps; D3b characterize-first) are
`[Practitioner-canon]`; the *outcome* claim is **not established**. Sibling **D1 (deep modules,
Ousterhout)** owns the design *target* refactoring moves toward; **B3** owns the tests that make
the small steps safe. The AI-era priority placing D3 in the verification cluster (verifying that a
fluent agent "refactor" *actually* preserved behavior; spec §12) is `[Verified-adjacent]` —
priority-steering, not proof.

### Performance & mechanical sympathy (module D4)

**D4 is the most extrapolation-heavy module in the curriculum** (its file badge is
`[Practitioner-canon]`): it mixes a small genuine empirical core, exact mathematics dressed in
engineering doctrine, and a hardware layer that is real in specific domains but **overstated for
typical application code**. The coach must keep the four statuses apart and never present the canon
or the extrapolation as verified science.

**D4a — "Measure, don't guess the bottleneck" `[Some empirical]`.** The originator's *reported
universal experience*, not a controlled study — but a real empirical observation, not a
prescription. The coach says: *"Knuth reported this and it's widely echoed — not 'studies prove.'"*

- Knuth, D. E. (1974). Structured Programming with `go to` Statements. *ACM Computing Surveys*,
  6(4), 261–301, **on p. 268**. doi:10.1145/356635.356640. `[Some empirical]` — In the same passage as the famous aphorism (a few sentences later, just past the "critical 3%" qualifier), Knuth writes (verified verbatim against the primary source during
  authoring): **"It is often a mistake to make *a priori* judgments about what parts of a program
  are really critical, since the universal experience of programmers who have been using
  measurement tools has been that their intuitive guesses fail."** This is the empirical anchor for
  D4's "profile / count operations before you optimize" discipline — the originator's report that
  hot-path intuition is unreliable. Badged `[Some empirical]` (one expert's reported experience,
  1974, not a replicated controlled study), not `[Verified]`.

**D4b — "Premature optimization is the root of all evil," IN CONTEXT `[Practitioner-canon]`.** The
most-misquoted sentence in the field. The verifiable origin-of-record and the **full** quote, which
*preserves the critical 3%*:

- Knuth, D. E. (1974). Structured Programming with `go to` Statements. *ACM Computing Surveys*,
  6(4), 261–301, **p. 268**. `[Practitioner-canon]` (aphorism in context). Verbatim (verified
  against the primary source): **"We should forget about small efficiencies, say about 97% of the
  time: premature optimization is the root of all evil. Yet we should not pass up our opportunities
  in that critical 3%. … he will be wise to look carefully at the critical code; but only after
  that code has been identified."** Three corrections D4 makes in-text: (1) it does **not** mean
  "never optimize" — it preserves the 3% to optimize *once identified by measurement*; (2) the
  sentence just before argues *against* blanket "ignore efficiency" advice ("a 12% improvement,
  easily obtained, is never considered marginal"); (3) it is sometimes called **"Hoare's dictum"** —
  Knuth attributed it to C. A. R. Hoare in 1989 ("The Errors of TeX"), but **that attribution is
  doubtful** and Knuth 1974 is the origin-of-record. (A variant of the aphorism also appears in Knuth's
  1974 Turing Award lecture, "Computer Programming as an Art," *CACM* 17(12), 667–673, p. 670: "premature optimization is the root of all evil (or at least most of it) in programming.")
  Cite Knuth 1974 as origin; do **not** assert the Hoare attribution as fact.

**D4c — Big-O cost models: math + doctrine `[Practitioner-canon]`.** Asymptotic complexity is
*mathematics* (`O(n log n)` is the comparison-sort lower bound by proof); what is **canon** is the
*engineering doctrine* built on it — that asymptotic class is the right first-order model of "what
scales," that you should know your data structures' per-operation costs, and that an algorithmic
change usually dwarfs a micro-optimization. The coach says: *"respected practice on an exact
mathematical foundation — not 'research shows.'"*

- Cormen, T. H., Leiserson, C. E., Rivest, R. L., & Stein, C. (2009). *Introduction to Algorithms*
  (3rd ed.). MIT Press. ISBN 978-0-262-03384-8. `[Practitioner-canon]` (textbook) — Standard
  reference for the asymptotic (Θ/O/Ω) definitions and the cost of canonical algorithms. The math
  is exact; its *application as engineering doctrine* is craft.
- **Python Wiki — *TimeComplexity*** (<https://wiki.python.org/moin/TimeComplexity>).
  `[Practitioner-canon]` (CPython reference, factual). The de-facto reference for per-operation
  costs in CPython, used to ground D4's worked example and drills. Figures **verified against the
  page during authoring**: list `x in s` (membership) **O(n)**; list `Insert` **O(n)**, `Get Item`
  **O(1)**; `set` `x in s` **O(1) average / O(n) worst**; `dict` `Get Item` **O(1) average / O(n)
  worst**. The page's own note grounds the front-insert trap: "Internally, a list is represented as
  an array; the largest costs come from … inserting or deleting somewhere near the beginning
  (because everything after that must move)."

**D4d — "Mechanical sympathy" `[Practitioner-canon]` (in its domains) + EXTRAPOLATION (for general
code).** The honesty fault line of the module. The term comes from racing (a driver's feel for the
car) and was **popularized for software by Martin Thompson** (the *Mechanical Sympathy* blog; the
LMAX Disruptor). It is *real and decisive* in systems / HFT / game-engine / numeric-kernel work,
and **overstated for typical application code**, where algorithmic complexity and I/O dominate and
cache-level reasoning is usually premature (and largely invisible in interpreted Python).

- Thompson, M. — *Mechanical Sympathy* blog (<https://mechanical-sympathy.blogspot.com>) and the
  **LMAX Disruptor**. `[Practitioner-canon]` + extrapolation. Origin of the software usage; the
  Disruptor is the canonical demonstration that cache-aware, allocation-aware, contention-aware
  design can beat a queue by a large margin **in the right domain**. *Honesty note:* the Disruptor's
  latency/throughput advantage is reported by **its authors / practitioner write-ups** (see also
  Fowler, M., "The LMAX Architecture," martinfowler.com, 2011), not an independent controlled
  study — cite as a domain demonstration, not measured general fact.
- Thompson, M. — *On Mechanical Sympathy* (SE Radio Episode 201, 2014), where Thompson explains the
  term's racing origin and its relevance to program performance. `[Practitioner-canon]` (interview)
  — supporting origin-of-record for the term's software popularization.

→ Drives module **D4** (performance & mechanical sympathy). The *measure-don't-guess* core is
`[Some empirical]` (Knuth 1974, p. 268 — a reported experience, not a replicated study); *Big-O* is
exact math whose *application* is `[Practitioner-canon]` (CLRS; CPython complexity reference, both
verified); *mechanical sympathy* is `[Practitioner-canon]` in systems/HFT/game contexts **and
extrapolation** for the claim that it matters to the median program. The coach must say plainly: for
most code, fix the **algorithm** and the **I/O** first; cache-line reasoning is a specialist tool,
not a default. The curriculum-wide transfer caveat applies in full — the transfer task (a real slow
path in the learner's own code) is the honest individual-level test. **Research note:** every
operation count, growth ratio, timeout status, and behavior-preservation check in D4's worked
example and its nine tier exemplars is **real runner output**, independently re-run from scratch
during authoring and confirmed against the pasted keys; precise wall-clock (`duration_s`) is treated
as **noisy and indicative only** (the runner crosses ~5s for naive `fib` at a machine-dependent n —
`fib(40)` reliably times out here, while `fib(32)`/`fib(35)` complete — which is exactly why the
deterministic op-counts are the primary signal and timeout-status is the dramatic confirmation).

---

### Concurrency mental models (module A4)

Extends [Finding 1](#1-the-notional-machine-is-the-durable-barrier--not-syntax-verified) (the notional
machine) into the *concurrent* setting, and **reuses the concurrency-bug taxonomy** (Lu, Park, Seo &
Zhou 2008) already itemized under [Production & concurrency debugging (module C3)](#production--concurrency-debugging-module-c3)
— A4 **cites** that taxonomy (atomicity/order violations) as its classification vocabulary; it is
**not** re-added here. **A4 is mixed-status by design** (its file badge is `[Verified-adjacent]`): the
*concurrent notional machine* (reason about the *set* of interleavings, not the one run) is
`[Verified-adjacent]` because it extends a verified finding; the *formalism* it reasons with — the
**happens-before** partial order and **sequential consistency** (Lamport) — is foundational CS
**theory**, `[Practitioner-canon]`; and *what CPython's GIL makes atomic* is **documented fact**,
`[Practitioner-canon]`. The coach must keep these apart, never present the theory/facts as an empirical
*learning* result, and **never teach "Python is thread-safe."**

**A4a — The concurrent notional machine `[Verified-adjacent]` (extends Finding 1).** No new source: A4
removes A1's single-machine assumption (one program counter advancing deterministically) and replaces
it with **N interleaved instruction streams** whose merge (the *interleaving*) is chosen by the
scheduler, not the programmer. This is `[Verified-adjacent]` for the same reason C3's taxonomy half is
— it *extends* the `[Verified]` execution-model finding (Finding 1; Sorva 2013; du Boulay 1986) into
the concurrent setting on solid ground, **not** because "drilling interleaving-reasoning causally
improves engineers" is shown (it is not — the open transfer question).

**A4b — Happens-before & sequential consistency `[Practitioner-canon]` (foundational CS theory).**
Rigorous definitions/models by the field's founding figure — exact *theory*, not empirical learning
findings; badged as foundational canon in the same sense as Parnas 1972 (information hiding) and the
Big-O cost models (D4c): the result is exact, its *use as a reasoning method* is craft. The coach says:
*"foundational, rigorously-established CS theory — not a verified result that teaching it improves your
code."*

- Lamport, L. (1978). Time, Clocks, and the Ordering of Events in a Distributed System. *Communications
  of the ACM*, 21(7), 558–565. doi:10.1145/359545.359563. `[Practitioner-canon]` (foundational) —
  Origin of the **"happened-before" relation** (`→`), a **partial ordering** of events: program order
  within a process; a message send before its receipt; transitivity. Two events with **no `→` path
  either way are *concurrent*** (neither can causally influence the other). A4 uses the standard
  shared-memory specialization — program order within a thread; `start`→the thread; the thread→`join`;
  lock release→a later acquire; `Event.set()`→an observing `wait()`; queue `put`→`get` — to decide what
  is **ordered** vs **genuinely concurrent** (and so where a **data race** can occur). Among the work
  recognized by Lamport's 2013 Turing Award; one of the most-cited papers in CS.
- Lamport, L. (1979). How to Make a Multiprocessor Computer That Correctly Executes Multiprocess
  Programs. *IEEE Transactions on Computers*, C-28(9), 690–691. doi:10.1109/TC.1979.1675439.
  `[Practitioner-canon]` (foundational) — The canonical definition of **sequential consistency**, in its
  universally-reproduced form: *"the result of any execution is the same as if the operations of all the
  processors were executed in some sequential order, and the operations of each individual processor
  appear in this sequence in the order specified by its program."* A4 uses SC as the **intuitive model
  A1 silently assumes** and makes explicit — and the reason **weaker** real-world memory models (and the
  publish-via-flag pattern) are hazards absent a happens-before edge.

**A4c — What CPython's GIL makes atomic `[Practitioner-canon]` (documentation, factual).** Documented
facts about the **reference implementation**, *not* a language guarantee — the same status as C2's
Python-docs/PEP citations.

- **Python documentation — Programming FAQ, *"What kinds of global value mutation are thread-safe?"***
  (docs.python.org/3/faq/library.html). `[Practitioner-canon]` (documentation, factual). Verbatim
  (verified against the page during authoring): a **global interpreter lock (GIL)** "is used internally
  to ensure that only one thread runs in the Python VM at a time"; Python "offers to switch among threads
  only between bytecode instructions; how frequently it switches can be set via `sys.setswitchinterval()`";
  therefore "**each bytecode instruction … is … atomic from the point of view of a Python program.**" The
  page lists operations that **are** atomic (`L.append(x)`, `x = L[i]`, `D[x] = y`, `D1.update(D2)`,
  `x = y`, `x.field = y`, …) and ones that are **not** (`i = i+1`, `L.append(L[-1])`, `L[i] = L[j]`,
  `D[x] = D[x] + 1`). A4 grounds its GIL-atomicity drills here and adds the **bound**: the GIL is a
  **CPython implementation detail** (PyPy/Jython differ; CPython 3.13 ships an experimental
  **free-threaded / no-GIL** build, **PEP 703**, "Making the Global Interpreter Lock Optional in
  CPython"), so it removes low-level *data races* (no torn reads) but **not** *race conditions* (lost
  updates, check-then-act) — which is exactly why "the GIL makes Python thread-safe" is false.

→ Drives module **A4** (concurrency mental models). The *model* (the concurrent notional machine; reason
about the set of interleavings) is `[Verified-adjacent]` (extends Finding 1); the *formalism*
(happens-before, sequential consistency — Lamport 1978/1979) is `[Practitioner-canon]` foundational CS
theory; the *GIL facts* are `[Practitioner-canon]` documentation; and the *classification vocabulary*
(atomicity vs order) is the **reused** Lu et al. 2008 taxonomy ([C3a](#production--concurrency-debugging-module-c3),
`[Verified-adjacent]`). Sibling module **C3** owns *debugging* races (non-reproducibility, heisenbugs,
observability) and references A4 softly; A4 owns the *model* C3's debugging runs on. The AI-era priority
placing concurrency reasoning in the broader verification cluster (judging whether agent-generated
concurrent code is correct under *all* schedules, not just the run it was tested on; spec §12) is
`[Verified-adjacent]` — priority-steering, not proof. **Research note:** every executable sub-claim in
A4's worked example and its nine tier exemplars is **real runner output** (Python 3.13.2), independently
re-run from scratch during authoring and confirmed against the pasted keys — the deterministic
**interleaving-set enumeration** (6 valid interleavings of two `+1`s; 2 correct, 4 lose an update), the
**forced** `Event` interleavings (the lost update → `1`; the use-before-init read → `KeyError`; the
check-then-act → `compute` runs twice; the deadlock → runner **timeout**), and the **disassembly**
showing a read-modify-write is `BINARY_SUBSCR … STORE_SUBSCR` (a read then a separate write) while an
atomic store is a single `STORE_SUBSCR`. Because concurrency correctness is a property of *all* schedules,
the runner is used only to **prove a bug exists on a forced/enumerated schedule** (never to certify a fix
over all interleavings) and the *reasoning* is rubric-graded, named out loud as softer than A1's
executable pass. **Citations verified:** Lamport 1978 (CACM 21(7):558–565; doi:10.1145/359545.359563) and
Lamport 1979 (IEEE TC C-28(9):690–691; doi:10.1109/TC.1979.1675439) confirmed against the ACM Digital
Library / IEEE catalog records; the sequential-consistency definition cross-checked verbatim against two
authoritative secondary sources (its universally-reproduced form). The Python FAQ text was confirmed
verbatim against docs.python.org. **Flagged honestly:** both Lamport primary PDFs rendered as
corrupted/binary text via automated fetch in this pass, so the *exact verbatim phrasing* of Lamport
1978's "concurrent" definition and Lamport 1979's SC sentence was **not extracted from the primary PDF
directly** — the citations/DOIs/pages are confirmed against the publisher records, the SC quote against
secondary sources matching the canonical form, and the happens-before content is standard textbook CS;
A4 paraphrases the happens-before relation rather than quoting it.

### Large-codebase comprehension (module E1)

Extends the **`[Verified]`** comprehension findings already in this file — [Finding 2](#2-expertise-is-better-representation-experts-chunk-code-into-larger-semantic-units-verified) (chunking), [Finding 3](#3-beacons-and-programming-plans-are-real-cues-experts-exploit-verified) (beacons/plans, where **Storey 2005/2006** already lives), and [Finding 6](#6-reading--tracing--writing-is-a-developmental-hierarchy-verified) (reading→tracing→writing) — **one grain up**, from the line/function to the file/module: a directory tree is a chunk map; `routes.py`/`models.py`/`__main__.py`/`tests/`/high-churn files are repo-scale beacons; and you trace one cross-file path rather than the whole system. **E1 is mixed-status** (file badge `[Verified]`): those *mechanisms* are `[Verified]`, but the evidence is from people comprehending a **single program/function** — applying them at repository grain is a **reasonable extension, not a separately verified result** — and the **seven-step orient procedure** itself is `[Practitioner-canon]` craft. The coach keeps the two apart and never presents the procedure as a measured result. (Feathers, *Working Effectively with Legacy Code* is already on the [reading spine](#reading-spine-book-canon) as E1's staff anchor; itemized below.)

**E1a — Strategic code reading & the orient procedure `[Practitioner-canon]` (craft).** Respected, widely-taught practice for reading large, real code in priority order — not an effectiveness experiment. The coach says: *"respected practice — not a verified research finding."*

- Spinellis, D. (2003). *Code Reading: The Open Source Perspective.* Addison-Wesley (Effective Software Development Series, Vol. 1). ISBN 978-0-201-79940-8. `[Practitioner-canon]` — the canonical text on reading **large, unfamiliar** codebases *strategically*: start from the entry points, build/configuration files, and the **directory structure as a map**, and read **for what you need, in priority order** rather than end-to-end. 600+ real-world examples; Software Development Productivity Award (2004). The craft anchor for E1's "orient, don't crawl." *(Verified during E1 authoring: title, publisher, series, ISBN-13 978-0-201-79940-8, and 2003 date confirmed against the Pearson catalog and the Internet Archive copy.)*
- **The orient procedure** (README → directory-tree → entry points → tests-as-spec → core modules → git-churn → gateway artifact) is **adapted from the `orient` module by Dr. Michael Mullarkey**, in Cat Hicks' *Learning Opportunities* (CC-BY 4.0; see [Attribution](#attribution)). `[Practitioner-canon]` — **credited**; E1 grounds each step in the `[Verified]` mechanisms above. *(The broader Storey program-comprehension survey that situates beacons/plans is already cited under [Finding 3](#3-beacons-and-programming-plans-are-real-cues-experts-exploit-verified); not re-added here.)*

**E1b — The gateway artifact / developer documentation `[Practitioner-canon]` (empirical study of practice).** A field study of how open-source documentation is created and evolved — descriptive practice data, not a controlled learning result.

- Dagenais, B., & Robillard, M. P. (2010). Creating and evolving developer documentation: understanding the decisions of open source contributors. *Proceedings of the 18th ACM SIGSOFT International Symposium on the Foundations of Software Engineering (FSE 2010)*, 127–136. doi:10.1145/1882291.1882312. `[Practitioner-canon]` — an interview-and-document-history study of open-source projects finding that developer documentation is a **deliberately created and evolved artifact** whose authors make explicit decisions about what a **newcomer needs to orient**. Grounds E1's **gateway-artifact** step (the one doc/file that unlocks the rest). **⚠ Honesty flags:** (1) **"gateway artifact" / "the one file that unlocks the rest" is the curriculum's framing of the orient procedure, NOT a verbatim term from the paper** — E1 says so in-text. (2) Author, venue, year, and **page range 127–136** are confirmed (the author's own publications list + the dblp/ACM record); the *abstract* could not be opened against the primary PDF in this pass (ACM DL and ResearchGate returned HTTP 403), so the study's exact method counts are **deliberately not cited** — the module characterizes the finding qualitatively (cite less, not more). (3) A study of *practice*, not a causal effectiveness result.

**E1c — Orienting in untested / legacy code `[Practitioner-canon]` (the no-docs corner).**

- Feathers, M. C. (2004). *Working Effectively with Legacy Code.* Prentice Hall. ISBN 978-0-13-117705-5. `[Practitioner-canon]` — already on the [reading spine](#reading-spine-book-canon) as E1's staff anchor; itemized here for the claims E1 cites. When a repo has **no README and no tests**, you orient from **structure + change history**, find a **seam**, and pin behavior with a **characterization test** before changing anything (the quirks may be load-bearing). The discipline for the stripped-cue corner of the orient procedure. *(Origin-of-record for "legacy code is code without tests" and the characterization test; cited as concepts, not independently page-pinned — same status as the D3 refactoring subsection.)*

→ Drives module **E1** (large-codebase comprehension). The *mechanisms* (chunk at file grain; structural beacons; trace one cross-file path) are `[Verified]` extended one grain up (Findings 2/3/6 — **cited, not re-derived**); the *orient procedure* (and **git-churn-as-core-finder**, cited as a useful heuristic with **no effect size** — cite less, not more) is `[Practitioner-canon]` (Spinellis 2003; the `orient` module, Mullarkey; Dagenais & Robillard 2010; Feathers 2004). The AI-era priority placing E1 in the verification cluster (engineers inherit large, unfamiliar, agent-generated repos; *unaided* comprehension atrophies first — Anthropic RCT, ~17% lower, already in [AI-era impact](#ai-era-impact-202627-verified-adjacent)) is `[Verified-adjacent]` — priority-steering, not proof. **Research note:** every *test-as-executable-spec* sub-claim in E1's worked example and its nine tier exemplars is **real runner output** (Python 3.13), independently re-run from scratch during authoring and confirmed against the pasted keys; because orienting is a *strategy*, the runner is used only to pin the one executable sub-claim — *what a module does* — by collapsing the module + its test into a single runnable file, while the orientation **map** (entry/core/feature-location/first-file) is rubric-graded against the golden exemplars and named out loud as softer than an executable pass.

### Architectural & technical judgment (module E2)

**E2 is `[Practitioner-canon]` by design — the softest-graded module in the curriculum.** Its
substance is respected, widely taught *engineering judgment*, vetted against the named sources
during authoring — **not** an empirical finding. There is **no executable ground truth for a
design tradeoff** and usually **no single right answer**; the coach grades the *reasoning*
(named the tradeoff on both sides? the failure mode? the cost? what breaks first?) against a
rubric + exemplars, and uses the runner only to prove a **named failure mode is real** (a retry
double-charges; a cache goes stale; an unbounded wait hangs), **never** to decide which design
is right. Unlike B3/D2/C3, E2 has **no `[Some empirical]` content layer to borrow** — the coach
must never dress these judgments as science. (Ousterhout's *A Philosophy of Software Design* —
strategic vs tactical — is **reused from [D1a](#managing-complexity--abstraction-module-d1)**, not
re-added here; Kleppmann's *Designing Data-Intensive Applications* is already on the
[reading spine](#reading-spine-book-canon) as the E2 staff anchor and is itemized below.)

**E2a — The three concerns + tradeoff framing `[Practitioner-canon]` (craft).**

- Kleppmann, M. (2017). *Designing Data-Intensive Applications: The Big Ideas Behind Reliable,
  Scalable, and Maintainable Systems.* O'Reilly. ISBN 978-1-449-37332-0. `[Practitioner-canon]` —
  Source of E2's scaffolding, confirmed during authoring: the **three concerns** every system is
  judged against — **reliability** (*"continue to work correctly … even in the face of
  adversity"* — faults and human error), **scalability** (reasonable ways to cope with growth in
  data/traffic/complexity), **maintainability** (operability, simplicity, evolvability); the
  **fault vs. failure** distinction (a *fault* is one component deviating from spec; a *failure*
  is the system as a whole stopping service — you cannot eliminate all faults, so you build
  **fault-tolerance** to stop a fault becoming a failure, and may deliberately *induce* faults,
  e.g. Chaos Monkey, to prove it); the discipline of **describing load and performance** (load
  parameters; response-time percentiles and tail latency, not a misleading average) *before*
  claiming a design "scales"; and above all the *method* — there is **no universally right
  answer**, you reason about **tradeoffs**. That tradeoff-analysis stance *is* this module.
  Respected systems craft, **not** a controlled study.

**E2b — Designing for failure: the Fallacies of Distributed Computing `[Practitioner-canon]`
(attributed folklore).** The canonical checklist of false assumptions that make a design fragile
the moment it crosses a process boundary. Originated at **Sun Microsystems**: **L. Peter Deutsch**
articulated seven (c. 1994, incorporating four that **Bill Joy and Dave Lyon** had named) and
**James Gosling** added the eighth (c. 1997): **(1) the network is reliable; (2) latency is zero;
(3) bandwidth is infinite; (4) the network is secure; (5) topology doesn't change; (6) there is
one administrator; (7) transport cost is zero; (8) the network is homogeneous.** Standard
explanatory reference: **Rotem-Gal-Oz, A. (2006). *Fallacies of Distributed Computing Explained.***
**⚠ Provenance flag:** there is **no single canonical primary publication** — the list propagated
as an internal/oral Sun list, so this is *attributed folklore*, cited as origin-of-record with the
Rotem-Gal-Oz essay as the explanatory source. The coach presents it as a respected checklist with
honest provenance, **not** a sourced theorem.

**E2c — When *not* to build: YAGNI `[Practitioner-canon]` (craft).**

- "You Aren't Gonna Need It" — the Extreme Programming maxim (Beck/Jeffries; the XP practice of
  **Simple Design**) against building **presumptive features**. Load-bearing modern statement:
  **Fowler, M. (2015, 26 May). *Yagni* (bliki, martinfowler.com).** `[Practitioner-canon]` —
  Confirmed verbatim during authoring: a presumptive feature is *"any code that supports a feature
  that isn't yet being made available for use"*; building it on spec costs **build / delay / carry
  / repair**, where **cost of carry** is *"the code for the presumptive feature adds some
  complexity … this complexity makes it harder to modify and debug that software, thus increasing
  the cost of other features."* **Crucial nuance, verbatim:** *"Yagni only applies to capabilities
  built into the software to support a presumptive feature; it does not apply to effort to make the
  software easier to modify."* So YAGNI is **not** "never abstract / never leave a seam" —
  refactoring and keeping code malleable are how YAGNI stays safe (the "design for the change you
  can name" half of E2). Craft maxim, not an experiment.

→ Drives module **E2** (architectural & technical judgment). The *concerns and tradeoff method*
are `[Practitioner-canon]` (Kleppmann); the *failure checklist* is `[Practitioner-canon]`,
attributed folklore (the fallacies — Deutsch/Gosling/Sun; Rotem-Gal-Oz 2006); the *don't-build-it
half* is `[Practitioner-canon]` (YAGNI — Beck XP; Fowler 2015); the *investment stance* is reused
from D1a (Ousterhout, strategic vs tactical). **There is no empirical half** — the coach never
says "research shows," and the runner proves only that a named **failure** is real, never that a
**tradeoff** is the right call. The AI-era priority placing E2 in the verification cluster (judging
whether a fluent, confident, often *over-engineered* agent-proposed architecture is sound rises as
agents draft code and designs; spec §12; ties D1/E3/F1) is `[Verified-adjacent]` — priority-steering,
not proof.

**Research note (verified against primary sources where one exists; flags recorded).** Kleppmann's
**three concerns** and the **fault vs. failure** distinction were confirmed (publisher record +
multiple Chapter-1 summaries); the ISBN 978-1-449-37332-0 was confirmed against the publisher/Amazon
records. **Flag:** finer Chapter-1 specifics cited as framing — *load parameters*, response-time
**percentiles / tail latency**, and the **operability / simplicity / evolvability** triad — are
well-established DDIA Ch.1 content confirmed via secondary summaries but **not re-pinned page-by-page
to the primary text** in this pass; the module cites them as Kleppmann's framing, not as page-pinned
quotes. The **Fowler *Yagni*** date (26 May 2015), the presumptive-feature definition, the four
costs, the **cost-of-carry** quote, and the **refactoring-nuance** quote were confirmed **verbatim**
against martinfowler.com/bliki/Yagni.html. The **Fallacies** attribution (Deutsch's seven c. 1994
incorporating Joy & Lyon's four; Gosling's eighth c. 1997; Sun Microsystems) and the eight-item list
were confirmed against the standard references; **flag:** there is **no single primary publication**
(attributed folklore), and the Rotem-Gal-Oz 2006 PDF body did not render for direct text extraction
(author "arnonrgo" / 2006 confirmed via PDF metadata; the list and attribution sourced from
secondary consensus) — recorded honestly rather than asserted as a pinned primary. Every failure-mode
anchor in E2's worked example and its nine tier exemplars is **real runner output** (Python 3.13),
independently re-run from scratch during authoring and confirmed against the pasted keys; because a
design verdict is *not* executable ground truth, the runner pins only **behavioral** sub-claims (a
retry double-applies; a cache returns stale data; an unbounded wait yields `status: timeout`; a
partial failure splits state; an out-of-order delivery corrupts; two designs are behaviorally
identical today), and the *tradeoff verdict* is rubric-graded, named out loud as the softest grading
in the curriculum.

### Learning new languages & frameworks — transfer of learning (module F3)

**F3's general transfer science is `[Verified]` *as general cognitive/educational
psychology*; the programming-specific transfer is `[Verified-adjacent]`** (extrapolated). It
rests on **Finding 1** (the notional machine it *ports* — already verified above; do **not**
re-derive) and is fenced by the **Gilmore & Green 1988** notation-dependence result (already
in [Refuted under verification](#refuted-under-verification) and the Finding 3 caveat — the
*false-friend* anchor; **reuse, do not re-add**). The coach says: *"transfer of learning is
solid learning science in general; the programming-specific evidence is thinner — and the
analogy you map with can be a false friend."*

- Thorndike, E. L., & Woodworth, R. S. (1901). The influence of improvement in one mental
  function upon the efficiency of other functions. *Psychological Review*, 8, 247–261 (Part I
  of a three-part 1901 series). `[Verified]` (general; foundational) — the **identical-
  elements** theory: one function transfers to another *"spread of practice occurs only where identical elements are concerned in the influencing and influenced function."* The mechanism behind
  both halves of F3 at once: the parts a new language **shares** with one you know (sequencing,
  branching, call/return, arithmetic) transfer for **free**; the non-shared, notation-specific
  parts do **not** — and *look like they should* (**false friends**). *(Verified against the
  primary text via Classics in the History of Psychology and the gwern PDF; the 1901 identical-elements wording confirmed (the popular "in so far as ... in part identical" formulation is actually from Thorndike 1906, *The Principles of Teaching*, not this 1901 paper). Part I = pp. 247–261; the exact page ranges of Parts II and III
  were not separately pinned in this pass — the module cites only Part I and the direction.)*
- Salomon, G., & Perkins, D. N. (1989). Rocky roads to transfer: Rethinking mechanisms of a
  neglected phenomenon. *Educational Psychologist*, 24(2), 113–142.
  doi:10.1207/s15326985ep2402_1. `[Verified]` (general) — **near vs. far** transfer and
  **low-road** (reflexive, from extensive/varied practice) vs. **high-road** (mindful,
  deliberate abstraction) transfer. The reading F3 uses: the *closer* the new language, the
  more transfers automatically — **and** the more dangerous an unchecked analogy becomes; the
  more *distant* the paradigm, the more it needs the deliberate high road. *(Verified against
  the Taylor & Francis journal record / DOI; the low-road/high-road definitions confirmed.)*
- Singley, M. K., & Anderson, J. R. (1989). *The Transfer of Cognitive Skill.* Cambridge, MA:
  Harvard University Press. ISBN 978-0-674-90340-1. `[Verified]` (general; **programming-
  adjacent**) — the closest anchor to programming, and the honest limit of how close we can
  get. Revives Thorndike's identical-elements in the ACT* framework: transfer is roughly
  proportional to **shared productions** (shared procedural knowledge), demonstrated on
  **text-editor** transfer and related cognitive skills. **Honest bound:** this is **1989, on
  editors / small skills**, *not* modern frameworks — it makes the *direction* (transfer ∝
  shared structure) credible for programming, **not** any quantitative promise about picking up
  a new framework. *(Verified via the Harvard Univ. Press record and the CMU ACT-R publications
  page; the ACT* "transfer ∝ shared productions / common elements" claim and the text-editor
  transfer experiments confirmed. Specific experiment page numbers were not pinned; the module
  cites only the direction.)*
- Barnett, S. M., & Ceci, S. J. (2002). When and where do we apply what we learn? A taxonomy
  for far transfer. *Psychological Bulletin*, 128(4), 612–637. doi:10.1037/0033-2909.128.4.612.
  `[Verified]` (general) — the **honesty fence**. Surveying a century of work, the authors
  conclude that whether **far** transfer reliably occurs is *still disputed*, and it frequently
  **does not happen spontaneously**. This is *why F3 exists*: you cannot rely on osmosis to map
  a new language — you must map **deliberately** and **verify**. *(Verified against PubMed
  12081085 and the journal record; the "far transfer is unresolved/unreliable" conclusion and
  the nine-dimension taxonomy confirmed.)*

→ Drives module **F3** (learning new languages & frameworks fast). The machine it **ports** is
`[Verified]` (Finding 1); **why** porting works is `[Verified]`-general transfer science
(Thorndike & Woodworth 1901; Salomon & Perkins 1989; Singley & Anderson 1989) whose
**programming-specific** application is `[Verified-adjacent]` (extrapolated — the evidence is
general and old/editor-based, not modern-framework); **why** porting is unsafe is the
**reused** Gilmore & Green 1988 notation-dependence (idioms are partly notation-specific →
false friends) plus Barnett & Ceci 2002 (far transfer is unreliable and often fails to happen
on its own). The **AI-era priority** placing "verify code in an unfamiliar stack" in the
verification cluster (false-friend risk is highest, and fluent agent output most dangerous, in
a language you don't yet own; spec §12) is `[Verified-adjacent]` — priority-steering, not
proof. **Research note:** F3 is a **hybrid** module; every Python idiom in its worked example
and nine tier exemplars is **real runner output** (Python 3.13, independently re-run from
scratch during authoring and confirmed against the pasted keys), because the *run* is what
**verifies the mapping** — a false friend is convicted by the machine, not asserted — while the
*mapping judgment* (true/false friend / new / re-notated, plus the execution-model reason) is
rubric-graded against the golden exemplars and named out loud as softer than an executable
pass. The runner is **Python-only**, so the executable verification is *demonstrated* on Python
idioms treated as "new," and the *principle* (a mapping is a hypothesis; verify it against
ground truth) is taught as generalizing to stacks the runner cannot execute (where "the runner"
becomes that language's REPL / unit test / spec).

---

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
- **Lopez et al. 2008 (BRACElet)** — confirmed: ICER '08, doi:10.1145/1404520.1404531;
  tracing + explaining together explained **~46% of code-writing variance (R² = 0.46)**;
  each alone is weaker (iterative-tracing ≈15%, explaining ≈7%). **Correction:** an
  earlier draft cited "R² ≈ 0.66 across the skills" — that was wrong; 0.66 is not the
  model variance but the **bivariate correlation r ≈ 0.63** (r = 0.6267) between
  iterative-tracing and writing in the same paper, a different quantity. Now cites only
  the verified **46% combined-variance** figure (and labels r ≈ 0.63 as the correlation,
  not variance). ✓
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
5. **Lopez et al. 2008 (Finding 6) — "R² ≈ 0.66" was a real error, now corrected.** An
   earlier draft of Finding 6 (and its Research-notes line) stated "R² ≈ 0.66 across the
   skills." That **conflated two different quantities**: the verified headline is that
   tracing + explaining **together** explain **~46% of code-writing variance (R² = 0.46)**;
   0.66 is instead the bivariate **correlation r ≈ 0.63** (r = 0.6267) between
   iterative-tracing and writing. Re-verified against the primary source (each skill
   alone: tracing ≈15%, explaining ≈7%). Finding 6 now cites **only** the 46%
   combined-variance figure and, where the correlation is mentioned, labels it r ≈ 0.63 —
   not variance. The A3 module already flagged this discrepancy during its authoring; this
   resolves it at the source.

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
