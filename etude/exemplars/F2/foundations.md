# F2 — Foundations exemplars (designing your own practice)

Golden drills for the **Foundations** tier of module F2. Each is a described practice routine
with **one clear anti-pattern, no decoys**. The skill is to **name the anti-pattern, the
learning-science principle it violates, and the one fix** — the smallest version of the
critique move.

F2 is **rubric-graded** (`drill-generation.md` §3): "is this practice well-designed?" is a
**judgment with no single correct answer**, and the coach says so out loud. Where a redesign
turns a passive element into a **predict-then-check** drill, the embedded snippet is **run** to
show the redesigned practice now has external ground truth (`drill-generation.md` §2):

```
python <skill-dir>/runtime/python/runner.py snippet.py
```

Two of the three Foundations drills below have **no executable ground truth at all** (they are
about practice *structure*) — the coach grades those purely against the rubric and **names the
softness**. Coverage spans three different levers (QUALITY/generation · the META/measurement
lever · SPACING). Pose one, **hard-stop, wait** (`coaching-loop.md`). **How to grade** against
module §7: **D1** = named the real anti-pattern + principle; **D3** = stated the principle, not
just the fix.

---

## F1 — Re-reading solved solutions (QUALITY / generation lever)

> *"I learn Python by **re-reading my old solutions** until they feel familiar. I keep a
> notebook of problems I've solved, and each evening I read back through a dozen of them. By the
> end they read smoothly and I feel ready."*

> **Your turn:** Critique this practice. What's the **anti-pattern**, which **principle** does it
> violate, and what's the **one fix**?
>
> (Take your best guess — wrong attempts are useful data.)

**The anti-pattern.** **Passive consumption — zero generation.** Re-reading solved code produces
a **fluency illusion**: the text reads smoothly, so it *feels* learned, but nothing was
retrieved or produced. "Feels ready" is the symptom, not evidence (Roediger & Karpicke 2006,
generation/testing effect; Koriat & Bjork 2005, illusions of competence).

**The one fix.** Make it **generative**: cover the solution, **predict the output (or rewrite it
from a blank page) before you look**, then **check against ground truth by running it**. The
redesign converts the most passive activity into a retrieval-plus-feedback one.

**Runner-verified evidence** (what the redesigned "predict, then run" practice checks against —
take one solved snippet the learner would otherwise just re-read):

```python
def initials(name):
    return "".join(w[0].upper() for w in name.split())

print(initials("ada lovelace"))     # predict before looking...
print(initials("grace b hopper"))
print(repr(initials("")))           # the edge case re-reading never surfaces
```

```
stdout: "AL\nGBH\n''\n"
status: ok
```

So the redesigned drill has the learner **predict `AL`, `GBH`, and — the case re-reading would
never test — what `initials("")` returns** (it's `''`, because `"".split()` is `[]`). The run is
the feedback the original routine lacked.

**Why.** Re-reading is the single most common "studying" anti-pattern and the easiest to mistake
for progress, because fluency *feels* like mastery. The fix doesn't add time — it changes the
activity from receptive to generative, and bolts on the external check.

**Diagnoses.** A learner who defends re-reading with "but it feels productive" has the
**felt-ease-as-signal** gap on top of the generation gap (§5c). A learner who says "do more
problems" without naming *generation* or *feedback* has the symptom but not the principle (D3
partial) — push for *why* re-reading fails. Strong critique: names passive/no-generation, the
fluency illusion, and the predict-then-check fix.

---

## F2 — Counting hours toward a total (the META / measurement lever)

> *"My plan is simple: I'm going to **hit 10,000 hours**. I log every hour I practice in a
> spreadsheet — I'm at 1,240 so far. As long as the number keeps going up, I know I'm getting
> better."*

> **Your turn:** Critique this practice. What's the **anti-pattern**, which **principle** does it
> violate, and what's the **one fix**?
>
> (Take your best guess — wrong attempts are useful data.)

**This drill has no executable ground truth** — it is about how the learner *measures* practice,
which is a pure judgment. The coach grades it against the rubric and says so.

**The anti-pattern.** **Hour-dosing — the deliberate-practice-dominance folklore.** It conflates
the **input** (time) with the **outcome** (learning), and pins itself to a number that is
**refuted**: deliberate practice explains only **~12% of performance variance overall** (and
**~1% in professions**), the figure comes from **music/sports/chess — not software**, and
time-to-mastery varies **~8×** between people, so no single hour target can be "the answer"
(Macnamara et al. 2014; Gobet & Campitelli 2007; `evidence-base.md` → Folklore).

**The one fix.** Replace the hour counter with a **held-out delta**: pick a small set of *cold,
unseen* problems of a kind you currently fail, attempt them **before and after** a stretch of
practice, and score by **whether they pass a test battery** — not by hours logged
(`assessment.md` Part 3). "Getting better" is the delta on tasks you couldn't do before.

**Why.** Hours are the most seductive metric because they're effortless to track and always go
up — but a rising hour count is fully consistent with *zero* learning (e.g., 1,240 hours of
re-reading). Measuring the **output** is harder and is the only honest signal.

**Diagnoses.** A learner who answers "10,000 is too many, aim for 5,000" has **not** escaped the
frame — they're still dosing hours (the deep gap). A learner who says "track problems solved
instead" is closer but still counting *volume*, not *held-out transfer* — nudge toward the cold
re-test. Strong critique: rejects hour-counting as the DP folklore *and* proposes a held-out
measure. **(Honesty note the coach states: the rejection is bounded — practice matters; what's
refuted is the strong "hours are the dominant cause" thesis, and the magnitude is itself
disputed. Don't let the learner swing to "practice is pointless.")**

---

## F3 — Cramming one topic in a marathon (SPACING lever)

> *"When I tackle a topic — say recursion — I block out a **single 6-hour Sunday** and grind
> nothing but recursion until I've got it. Then I **check it off and move on**, and I don't come
> back to it. One topic, one marathon, done."*

> **Your turn:** Critique this practice. What's the **anti-pattern**, which **principle** does it
> violate, and what's the **one fix**?
>
> (Take your best guess — wrong attempts are useful data.)

**This drill has no executable ground truth** — it's about the *schedule* of practice, a pure
judgment graded against the rubric.

**The anti-pattern.** **Massing / cramming — no spacing, no interleaving, no return.**
Distributed practice beats massing for retention, even though a marathon block *feels* more
efficient and complete (Kornell 2009; Kang 2016, spacing). "Check it off and never come back"
also guarantees the gains decay with nothing to consolidate them.

**The one fix.** **Distribute and revisit**: spread the recursion practice across several
shorter sessions over weeks, **interleave** it with other topics in a session, and **return** to
it on a spaced schedule (a few days later, then a week, then a month). The slower-feeling
schedule is the one that sticks.

**Why.** A 6-hour marathon produces strong *same-session* performance — by hour 6 the learner
feels fluent — which is exactly the **learning ≠ performance** trap: the in-session fluency is a
poor index of what survives to next month (Soderstrom & Bjork 2015). Spacing trades a worse
*feeling* for better *retention*.

**Diagnoses.** A learner who says "6 hours is too long, do 3" has fixed the *duration* but not
the *massing* — the gap is **distribution + return**, not block length. A learner who flags the
marathon but proposes no **revisit/interleave** has a partial fix (D2 partial). Strong critique:
names massing, cites spacing/interleaving, and adds the **spaced return** to old material.
</content>
