# B1 — Working exemplars (decomposition & planning)

Golden drills for the **Working** tier of module B1. Each is a problem in an **unfamiliar
context** where the **hard sub-problem is non-obvious** *or* the **spec has one ambiguity to
surface** — a naive linear translation diverges from a correct plan. The skill is to **identify
the hard part first** and **surface the edge cases a line-by-line coder misses**, **unaided**.
B1 plans are **rubric-graded** (`drill-generation.md` §3); where concrete enough, the gold's
**composition check** was confirmed by running the implemented pieces (`drill-generation.md` §2):

```
python <skill-dir>/runtime/python/runner.py snippet.py
```

Coverage spans distinct hard-part locations (a **hidden prerequisite step** / a **stateful
window + boundary** / an **unstated spec decision**). Pose one, **hard-stop, wait**
(`coaching-loop.md`). **How to grade** against module §7: **D1** understood the contract; **D2**
balanced decomposition; **D3** named the non-obvious hard part + interfaces; **D4** surfaced the
edge cases + sequenced to de-risk. A plan that details the easy parts and hand-waves the hard one
is a **partial pass — flag it** (the central Finding-5 novice signature: unbalanced, linear).

---

## W1 — Merge overlapping intervals (the hidden prerequisite)

**Problem.** Plan `merge_intervals(intervals)`: given a list of `(start, end)` intervals, return
the **merged** set with all overlapping (and touching) intervals combined, e.g.
`[(1,3),(2,6),(8,10)]` → `[(1,6),(8,10)]`. No code — give me the decomposition, and tell me the
hard part.

> **Your turn:** Decompose this. What are the sub-problems, what's the **non-obvious** hard part,
> and what edge cases will you handle?
>
> (Take your best guess — wrong attempts are useful data.)

**Gold decomposition.**
- **Understand:** input `list[(start, end)]`, output the merged list. "Touching" (`(1,4),(4,5)`)
  counts as overlap → merge. The input may be **unsorted**.
- **The non-obvious hard part — sequencing:** a single left-to-right merge scan only works if the
  intervals are **sorted by start first**. The **sort is a hidden prerequisite sub-problem**;
  without it the scan is intractable (you'd have to compare every interval to every other). The
  merge scan itself is then easy.
- **Sub-problems (one altitude):**
  1. `sort_by_start(intervals)` → sorted `list[(start, end)]`. *(the load-bearing step)*
  2. `merge_scan(sorted)` → walk once, extending the current interval's end while the next start
     ≤ current end, else start a new interval.
- **Edge cases:** empty → `[]`; a single interval; **touching** `(1,4),(4,5)` → `(1,5)`; a
  **fully contained** interval `(1,10),(2,3)` → `(1,10)`; **unsorted** input.

**Composition check (runner-verified — the pieces compose):**

```
merge_intervals([(1,3),(2,6),(8,10),(15,18)]) -> [(1, 6), (8, 10), (15, 18)]
merge_intervals([])                           -> []
merge_intervals([(1,4),(4,5)])                -> [(1, 5)]      (touching merged)
merge_intervals([(1,10),(2,3)])               -> [(1, 10)]     (contained absorbed)
merge_intervals([(8,10),(1,3),(2,6)])         -> [(1, 6), (8, 10)]   (unsorted input handled)
status: ok
```

**The plan that skips the sort — same scan, runs clean, wrong answer** (runner-verified):

```
merge_no_sort([(8,10),(1,3),(2,6)])  -> [(8, 10)]     (the (1,6) merge is silently lost)
```

**Why.** The entire difficulty is a **sequencing insight**: a sub-problem (`sort`) must come
*first* or the main step is broken. A linear coder writes the merge scan they can picture,
omits the sort, and it **composes and runs** — failing only on unsorted input, exactly the case
the plan should have surfaced. Naming "sort first" up front *is* the Working-tier skill here.

**Diagnoses.** A plan that goes straight to "loop and merge adjacent" without the sort step has
**missed the hidden prerequisite** (§5c, planning-the-easy-parts) — and will lose merges on
unsorted input. A plan that never mentions touching/contained/unsorted is **happy-path-only**
(§5c). A learner who pattern-matches "it's an intervals problem, use two pointers" without
noticing the sort precondition has **template-matched** (§5c, refuted-trap). Strong plan: sort
named as the load-bearing first step, the scan as the easy follow-on, touching/contained/unsorted
edges surfaced.

---

## W2 — Sessionize events by inactivity gap (stateful window + boundary)

**Problem.** Plan `session_counts(events, gap=30)`: given `(timestamp_minutes, user)` events
**sorted by time**, count how many **sessions** each user has, where a gap of **more than** `gap`
minutes since that user's previous event starts a **new** session. Return `{user: session_count}`.
No code — decompose it and name the hard part.

> **Your turn:** Decompose this. What state do you carry, what's the boundary decision, and what
> edge cases will you handle?
>
> (Take your best guess — wrong attempts are useful data.)

**Gold decomposition.**
- **Understand:** input sorted `list[(t, user)]`; output `dict[user, int]`. The **boundary
  decision the spec pins**: "**more than** `gap`" — a gap of *exactly* `gap` is the **same**
  session; `gap + 1` is a new one. Each user's first event always starts session 1.
- **The hard part — per-user state across the stream:** you must track **each user's last
  timestamp** independently, and the new-session test is `t - last[user] > gap`. The counting is
  trivial *given* that state; the design decision is "what do I remember, keyed by whom."
- **Sub-problems (one altitude):**
  1. `new_session?(t, last_t, gap)` → bool (`t - last_t > gap`). *(the boundary box)*
  2. `walk(events)` → carry `last[user]` and `counts[user]`; for each event, if first-seen or
     `new_session?`, increment `counts[user]`; update `last[user]`.
- **Edge cases:** empty → `{}`; a single event → `{user: 1}`; a gap of **exactly** `gap` (same
  session) vs **`gap + 1`** (new session) — the two inputs that decide the boundary.

**Composition check (runner-verified — the pieces compose):**

```
session_counts([(0,'a'),(10,'a'),(50,'a'),(5,'b')]) -> {'a': 2, 'b': 1}   (a: 0..10 one session, 50 a new one)
session_counts([(0,'a'),(30,'a')])                  -> {'a': 1}            (gap == 30 -> SAME session)
session_counts([(0,'a'),(31,'a')])                  -> {'a': 2}            (gap == 31 -> NEW session)
session_counts([])                                  -> {}
status: ok
```

**Why.** The two near-identical inputs `(30)` and `(31)` are the **whole** boundary decision, and
the spec settled it (`> gap`, not `>= gap`). A plan that names the boundary box and the two
deciding inputs has surfaced the one place this goes wrong; a plan that says "group events into
sessions" has not.

**Diagnoses.** A plan that carries a **single** "last timestamp" instead of one **per user**
has the wrong state shape — it will merge users' sessions (§5c, undefined/incorrect interface).
A plan that never names the exactly-`gap` vs `gap+1` boundary has left the **hard edge unplanned**
(§5c, happy-path-only) and will likely flip `>` and `>=`. Strong plan: per-user `last`
named as the carried state, the `> gap` boundary box explicit with its two deciding inputs.

---

## W3 — Dedupe records under an unstated policy (surface the ambiguity)

**Problem.** Plan `dedupe(records)`: each record is `{"email", "name", "signup_date"}`. "Remove
the duplicates." That's the whole spec.

> **Your turn:** Before you decompose — is anything here **underspecified**? Name the decisions
> you'd have to make, pick reasonable answers, and *then* decompose.
>
> (Take your best guess — wrong attempts are useful data.)

**Gold answer — the Working skill is surfacing the ambiguity *before* planning.** "Remove
duplicates" hides **two unstated decisions** that change the answer:
- **Duplicate by what key?** Whole-record equality, or by `email`? And is `email` **case- and
  whitespace-sensitive** (`A@x.com` vs `a@x.com`)? *Reasonable assumption:* duplicate by
  **normalized email** (lowercased, stripped).
- **When two records share the key, which one wins?** First-seen? Earliest `signup_date`? Latest?
  *Reasonable assumption:* **keep the first occurrence**, preserve input order.

*Only after stating those* does the decomposition fall out:
- **Sub-problems:** 1. `key(record)` → normalized email; 2. `dedupe_by_key(records, key)` → walk,
  keep first per key, preserve order.
- **Edge cases:** empty → `[]`; case/whitespace variants of one email collapse to one; the
  conflict case (two records, same email) resolves by the stated **first-wins** rule.

**Composition check (runner-verified, *under the stated assumptions* — by lowercased email,
keep first):**

```
dedupe([{'email':'A@x.com',...}, {'email':'a@x.com',...}, {'email':'b@x.com',...}])
  -> kept names ['Al', 'Bo']        ('a@x.com' collapses into 'A@x.com'; first wins)
status: ok
```

**Why.** This drill has **no single correct decomposition** *by design* (§5d) — the point is that
a competent plan **names the missing decisions and commits to assumptions** before drawing boxes.
The composition check only confirms that *one stated policy* composes; it cannot tell you the
policy was right (that's a product decision), which is exactly why B1 is rubric-graded.

**Diagnoses.** A learner who dives straight into "loop and check if seen" has **skipped Stage 1**
and silently baked in *whole-record, case-sensitive* equality (§5c, solving-the-wrong-problem) —
and would split `A@x.com` from `a@x.com`. A learner who asks "by email or whole record?" but never
addresses **which record wins** has surfaced half the ambiguity. Strong answer: both decisions
named, assumptions stated and justified, *then* a clean two-box decomposition — and an explicit
"these are assumptions; confirm with the product owner."
