# D2 — Naming `[Practitioner-canon]`

> **Module type.** `[Some empirical] + [Practitioner-canon]` — a **hybrid module**. It has a
> genuine empirical layer (unusual for Track D): controlled experiments show that
> **descriptive identifiers aid comprehension** (Hofmeister, Siegmund & Holt 2017; Lawrie,
> Morrell, Feild & Binkley 2006; Feitelson et al. 2022). The *specific prescriptions* — what
> "precise" means, the precision+consistency doctrine, length heuristics — are respected
> **craft** (Ousterhout, *A Philosophy of Software Design*), **not** measured findings. The
> coach must keep the two apart and must never present a naming *convention* as proven. (The
> validator badge on this file is `[Practitioner-canon]`; the honest prose badge is
> `[Some empirical] + [Practitioner-canon]`.)
>
> **Core idea.** A name is the **cheapest documentation you will ever write**: it rides along
> for free on every read. A good name says what a thing **is or does** with **precision** (no
> more, no less), is used **consistently** across the codebase, and — the one non-negotiable —
> **never lies about behavior**. This is the *writing* side of A2's *reading* skill (name
> beacons; lying names). A name that says one thing while the code does another is a defect,
> and which one wins is **decided by running the code**.

---

## 1. Evidence basis `[Some empirical] + [Practitioner-canon]`

This module is **mixed-status by design**, and the split matters more here than almost
anywhere in Track D, because — unlike the pure-craft naming advice you will read elsewhere —
there *is* real empirical work on identifier comprehension. The honesty rule
(`evidence-base.md` → badge rules) is: badge the empirically-supported claim distinctly from
the craft prescriptions, and do not let the famous design book's *opinion* about *how* to name
borrow the empirical layer's credibility.

### (a) The empirical half — descriptive identifiers aid comprehension `[Some empirical]`

Cite via `evidence-base.md` → *Naming & identifier comprehension (module D2)*. Three primary
studies, each verified against its primary source during authoring:

- **Hofmeister, J., Siegmund, J., & Holt, D. V. (2017). Shorter identifier names take longer
  to comprehend.** *SANER 2017*, 217–227 (extended as *Empirical Software Engineering* 24(1),
  2019). A controlled, **within-subjects** experiment with **72 professional C# developers**
  who **looked for defects** in source-code snippets in three identifier styles — **letters,
  abbreviations, words** — with time-to-find-a-defect measured. **The verified headline,
  verbatim from the abstract:** *"words lead to, on average, 19% faster comprehension speed
  compared to letters and abbreviations, but we did not find a significant difference in speed
  between letters and abbreviations."* This is the cleanest empirical support the module has
  for "descriptive names help." **Read the 19% carefully:** it is *faster defect-finding speed
  for full words over BOTH single letters AND abbreviations* — and crucially, **abbreviations
  were no better than single letters.** It is **not** a general "19% better code" claim, and
  the original authors' own framing is modest (the effect is real but "fairly small").

- **Lawrie, D., Morrell, C., Feild, H., & Binkley, D. (2006). What's in a Name? A Study of
  Identifiers.** *ICPC 2006*, 3–12. **128 participants** described **twelve functions**, each
  shown in three variants — **full words / abbreviations / single letters** — and the
  free-form descriptions were rated 0–5 by two raters (κ = 0.71, substantial agreement). The
  verified findings, from the abstract: *"full word identifiers lead to the best comprehension;
  however, in many cases, there is no statistical difference between full words and
  abbreviations."* And from the results: *"full word identifiers lead to significantly better
  description ratings than single letter identifiers… There is never a statistical difference
  between full words and abbreviations."* **Note the honest nuance — and the disagreement with
  Hofmeister:** both papers agree **words beat single letters**, but Lawrie found **abbreviations
  ≈ full words** (good), while Hofmeister found **abbreviations ≈ letters** (poor). The
  *direction* "more descriptive → more comprehensible" is supported; the *fine ordering of
  abbreviations* is genuinely unsettled across studies. Lawrie measured **description quality +
  confidence**, not speed — so the "19%" figure is **not** from this paper (a common
  secondary-source misattribution; see the research note).

- **Feitelson, D. G., Mizrahi, A., Noy, N., Ben Shabat, A., Eliyahu, O., & Sheffer, R. (2022).
  How Developers Choose Names.** *IEEE TSE* 48(1), 37–52. **334 subjects** chose names for
  given scenarios. Two verified findings frame the module's humility: (1) **there is no single
  "correct" name** — *"in the 47 instances in our experiments the median probability [that two
  developers pick the same name] was only 6.9%"*; yet (2) **a chosen name is usually legible** —
  *"given that a specific name is chosen, it is usually understood by the majority of
  developers."* Their model (pick the concepts → choose words for each → assemble) and
  follow-up found that names built this way were judged superior ~2:1 and used **more concepts
  and longer names**. So: naming is *underdetermined* (don't bikeshed toward a mythical "right"
  name), but *precision and concept-coverage measurably help legibility.*

**What the empirical half licenses — and what it does NOT.** It licenses, at `[Some empirical]`:
**descriptive, full-word identifiers are comprehended faster and more accurately than single
letters; vague/generic names degrade comprehension; there is no uniquely correct name but more
precise, concept-complete names are more legible.** It does **NOT** license: any specific
*convention* (camelCase vs snake_case; a length limit; a casing rule) as empirically superior.
It does **NOT** license treating a famous book's prescriptions as proven.

**The contested case — naming *style* (camelCase vs snake_case) is mixed, not settled.**
Flag this explicitly. **Binkley, Davis, Lawrie & Morrell (2009)** (*"To CamelCase or
Under_score"*, ICPC; 135 subjects, timed) found camelCase gave **higher accuracy**, and those
*trained* in camelCase recognized it faster — **but all subjects were on average 13.5% *slower*
on camelCase** than underscore (p < 0.0001). **Sharif & Maletic (2010)** (eye-tracking
replication) found **"no difference in accuracy between the [styles]."** The take, badged
honestly: *style/casing effects are small, training-dependent, and contradictory across
studies* — so the module teaches **consistency of style**, not a *winner*. Anyone who tells you
the studies prove camelCase (or snake_case) is better has overread them.

### (b) The craft half — precision, consistency, "names are documentation" `[Practitioner-canon]`

Vetted during authoring against the named source; respected, widely taught **craft wisdom**,
**not** empirical findings. The coach says: *"this is respected practice — not a verified
research result."* Cite via `evidence-base.md` → *Naming & identifier comprehension (module D2)*.

- **Ousterhout, J. (2018/2021). *A Philosophy of Software Design*, Ch. 14 "Choosing Names."**
  `[Practitioner-canon]`. The craft anchor. Verbatim positions verified against the text:
  - **"Good names are a form of documentation: they make code easier to understand. They reduce
    the need for other documentation and make it easier to detect errors."** ← the module's
    thesis, in the author's words.
  - **The goal: "create an image in the mind of the reader about the nature of the thing being
    named. A good name conveys a lot of information about what the underlying entity is, and,
    just as important, what it is not."**
  - **"Good names have two properties: precision and consistency."** Precision: *"The most
    common problem with names is that they are too generic or vague"* (his examples: `count`,
    `x`/`y`, `blinkStatus`, a `result` in a method with no return value). Consistency's three
    requirements, verbatim: *"first, always use the common name for the given purpose; second,
    never use the common name for anything other than the given purpose; third, make sure that
    the purpose is narrow enough that all variables with the name have the same behavior."*
  - **Two red flags, verbatim:** *"Red Flag: Vague Name — If a variable or method name is broad
    enough to refer to many different things, then it doesn't convey much information…"* and
    *"Red Flag: Hard to Pick Name — If it's hard to find a simple name… that creates a clear
    image of the underlying object, that's a hint that the underlying object may not have a
    clean design."*
  - **The honest counterpoint — the book itself flags the dispute.** Ousterhout's §14.5 ("A
    different opinion: Go style guide") quotes Andrew Gerrand: *"long names obscure what the
    code does,"* and shows a single-letter Go example its authors consider *more* readable.
    Ousterhout disagrees, but **prints the disagreement** — so even the canon concedes that
    *name length* is a matter of taste, not law. The module inherits that honesty: descriptive
    > single-letter is empirically supported; the *exact length* is craft, and contested.

- **Martin, R. C. (2008). *Clean Code*, Ch. 2 "Meaningful Names."** `[Practitioner-canon]` —
  **cite with care; treat as contested opinion, not consensus.** *Clean Code* popularized
  much naming advice ("intention-revealing names," "avoid disinformation," "pronounceable
  names"), and some of it overlaps the precision principle above. But the book as a whole is
  **widely contested** in the professional community (its broader prescriptions on function
  length, side effects, and "clean" structure are disputed), so the coach must **not** present
  it as settled craft on a par with Ousterhout's narrower, better-argued naming chapter. Where
  this module echoes a *Clean Code* point, it is because the point also stands on its own or on
  the empirical layer — never on the book's authority alone.

**Why these license this module.** The empirical half (Hofmeister/Lawrie/Feitelson) grounds the
**direction** at `[Some empirical]`: descriptive names measurably aid comprehension; there is no
single right name but precision and concept-coverage help. Ousterhout grounds the **technique**
at `[Practitioner-canon]`: *precise + consistent + never-lying* as the working definition of a
good name, plus the two red flags the module drills. The lying-name half ties straight back to
**A2** (reading name beacons; the "the name says X but the code does Y" violation) and to
**A1's superbug** (trusting the name over the machine) — and *that* half is **executable**: a
lying name is confirmed by **running the code**, never by opinion.

**Read through the transfer caveat.** The empirical studies are controlled comprehension
experiments (C# defect-finding, function-description rating, name-elicitation) — **not** a proof
that *coaching naming* causally improves a given engineer's production code, the open question
every module here carries (`evidence-base.md` → transfer caveat). And the craft half is craft.
The transfer task (§9) — renaming on the learner's **own** codebase — is the honest
individual-level test. **AI-era note:** as agents draft most first-draft code, the reader's job
shifts from writing to *verifying* code they didn't write, and **a name that lies is the cheapest
way for fluent-looking agent output to mislead a reviewer** — making "does this name tell the
truth about the behavior?" part of the verification cluster (`evidence-base.md` → AI-era
section; spec §12). That priority is `[Verified-adjacent]` — steering, not proof.

---

## 2. Soft prerequisites

**A2 (code reading & chunking) recommended — this module is its mirror image.** A2 teaches you
to *read* names as **beacons** (Soloway & Ehrlich's discourse rules: a name is a cue to the
plan) and to catch **lying names** (the name says X, the code does Y). D2 is the **writing**
side of the same coin: producing names that *are* honest beacons. A learner who, in A2, kept
getting burned by a name that didn't match behavior is exactly who D2 is for.

**A1 (notional machine) helps**, for two reasons. First, the module's executable half *is* an
A1 event seen from the author's chair: a function named `is_valid` that **mutates** shared
state, or `get_user` that **creates** a row, is a rebinding-vs-mutation / side-effect surprise
(A1 §5c) wearing a misleading label. Second, A1's **superbug** — trusting the name/intent over
what the machine actually does — is the precise failure a lying name *exploits*; D2 teaches you
not to *plant* that trap. **A3 (tracing)** helps when deciding whether a name lies: you confirm
behavior by tracing/running, not by reading the name. **B3 (testing)** is adjacent — a name is a
tiny spec, and "does the code honor the name?" is a property you can test.

Per `assessment.md`, soft prerequisites **inform, never gate** — the buffet rule holds (any
learner may open any module at any tier). If a learner flails at D2 because they can't tell
whether a name lies, the coach notes the gap likely traces to A2/A3 and *suggests* shoring those
up — but never forbids D2.

---

## 3. The mental model

**A name is documentation that the reader cannot skip.** Comments can be ignored or go stale;
the name is *in your face* at every call site, every read, every diff. So the name is the
highest-leverage, lowest-cost documentation in the codebase — and, like all documentation, it
can be **wrong**. A good name does three jobs; the third is non-negotiable.

| Property | What it means | What goes wrong without it |
|---|---|---|
| **1. Precise** | The name says what the thing **is or does** — *no more, no less*. Specific enough that a reader guessing from the name alone (no docs, no body) lands close; not so specific it over-claims. Ousterhout: *"create an image… what it is, and just as important, what it is not."* | **Vague** (`data`, `tmp`, `count`, `result`, `process()`) → the reader learns nothing and may assume the wrong thing (Ousterhout's `block` bug: one vague name, six months, a data-corruption bug). **Over-claiming** (`sorted_copy` that mutates in place) → the reader trusts a guarantee that isn't there. |
| **2. Consistent** | One concept → one name, **everywhere**; and one name → one concept (never reused for a second meaning). Same idea, same word; different idea, different word. | The same thing called `user`, `usr`, `account`, `u` in four files → the reader can't tell they're the same; or `block` meaning *disk block* here and *file block* there → a false assumption → a bug. Inconsistency is, in Ousterhout's words, *"a major contributor to obscurity."* |
| **3. Honest (never lies)** | The name's claim **matches the behavior**. `is_valid` returns a bool and has no side effect; `get_X` reads and does not write; `filter_active` returns the active ones, not the inactive. | **The name lies.** `is_valid` mutates; `get_user` creates a row; `filter_active` returns the *inactive* set; `count_items` returns a *bool*. This is the worst failure — it actively *misleads*, and it is the one A2 teaches readers to fear. **Behavior wins: the code does what it does regardless of the label.** |

**The discipline in one line: *name a thing for what it actually does — precisely, consistently,
and never a word more than the truth.*** Three corollaries the module drills:

1. **Behavior is ground truth; the name is a claim about it.** When the name and the code
   disagree, the **code wins** — and the name is the bug. You confirm which by *running it*, not
   by arguing. This is the direct executable tie to A2's "lying name" and A1's superbug: never
   trust the label over the machine, and never *write* a label the machine contradicts.
2. **Precision is bounded on both sides.** Too vague (`tmp`, `data`) tells the reader nothing;
   *too specific* (a `selection` parameter on a method that works on any `range`) tells them
   something **false**. Aim for the few words that capture *what's most important* and omit the
   rest (Ousterhout: names get unwieldy past two or three words). The empirical layer backs the
   *descriptive > cryptic* direction; the exact length is craft (and the Go camp disagrees).
3. **If you can't name it, the design — not the name — is the problem.** A name you can't make
   precise and short is Ousterhout's *"Hard to Pick Name"* red flag: the entity probably does
   two things, or has no clean purpose. The fix is to *split or rethink the thing*, then name the
   pieces. Naming is a **design probe**, not just a labeling chore.

---

## 4. Worked example — judging a name, and catching one that lies

*(Foundations depth: both halves shown — the name-quality judgment AND the runner-confirmed
lying-name catch. This fades by tier; see the note after.)*

The skill has two moves, and this example shows both because the module grades them
**separately** (§5d).

### Move A — judge a name's quality and propose a better one (rubric)

Here is a real-shaped helper. Read the name, then the body:

```python
def tmp(p, r):
    return round(p + p * r, 2)
```

**Step 1 — what does it actually do?** Don't guess from `tmp` — it tells you nothing. *Run
representative inputs* (you confirm behavior, you don't assume it):

```
tmp(100, 0.08)   -> 108.0     # 100 plus 8%
tmp(49.99, 0.20) -> 59.99     # 49.99 plus 20%
```

**Runner-verified ground truth** (the coach *runs* it — `drill-generation.md` §2 — even to grade
a naming judgment, because the *behavior* the name should describe is executable):

```
$ python3 runtime/python/runner.py /tmp/D2_namequal.py
{"status": "ok", "stdout": "108.0\n59.99\n", ...}
```

So `tmp` computes **a price plus a tax/markup rate** — it's `price_with_tax` (or
`gross_price`). The parameters `p`, `r` are equally opaque: `price`, `tax_rate`.

**Step 2 — judge against the rubric and propose a fix:**

| Criterion | Verdict on `tmp` / `p` / `r` |
|---|---|
| **Precise?** | **No.** `tmp` ("temporary") names the *lifetime*, not the *meaning* — maximally vague (Ousterhout's #1 problem). `p`/`r` are single letters whose range of use spans the function but whose meaning isn't obvious. |
| **Consistent?** | Can't tell in isolation — but if the codebase elsewhere calls this concept `gross_price`, then `tmp` is also an inconsistency. |
| **Honest?** | Vacuously — `tmp` claims nothing, so it can't *lie*; it just *informs nothing*. (A vague name is a lesser sin than a lying one, but still a sin.) |

> **Better:** `def price_with_tax(price, tax_rate): return round(price + price * tax_rate, 2)`.
> Now a reader at the call site — `total = price_with_tax(item.price, region.tax_rate)` — knows
> what they're getting **without opening the function**. That is the name paying for itself.

### Move B — catch a name that *lies* (executable; behavior wins)

Now the non-negotiable half. Read this — the name makes a **promise**:

```python
users = ["ada", "grace"]

def is_valid(name):
    # name promises a boolean PREDICATE (no side effect).
    users.append(name)            # ...but it MUTATES the module list.
    return name in users

print(is_valid("alan"))
print(users)
```

**The promise in the name:** `is_valid` is a predicate — it should *answer a question* (return
a bool) and *change nothing*. Does it keep that promise? **Don't argue — run it:**

```
$ python3 runtime/python/runner.py /tmp/D2_worked.py
{"status": "ok", "stdout": "True\n['ada', 'grace', 'alan']\n", ...}
```

```
is_valid("alan")  ->  True
users             ->  ['ada', 'grace', 'alan']     # the "predicate" CHANGED THE WORLD
```

**Behavior wins, and the behavior convicts the name.** `is_valid` *mutated* `users` (it appended
`"alan"`) and — worse — it returns `True` *because* it just inserted the value it was "checking."
The name lies twice: it claims to be side-effect-free (it isn't) and it claims to *validate*
(it actually *registers-then-rubber-stamps*). A reader who trusts the name — the A1 superbug, the
A2 lying-name trap — ships a bug. **The two honest fixes:** either make the name tell the truth
(`def register_and_confirm(name): ...`), or, far better, make the *behavior* match the honest
name (a real `is_valid` does `return name in users` with **no** `append`). Which is right is a
*design* call — but the diagnosis ("the name lies; here is the run that proves it") is
**executable, not a matter of taste.**

**What the example makes visible:** the two moves are different evidence. *Move A* (is `tmp` a
good name?) is a **judgment** — graded against a rubric, softer. *Move B* (does `is_valid`
lie?) is a **fact** — the runner settles it. The module reports them **separately** (§5d): you
can write a gorgeous name and still have it lie, and you can correctly catch a lie while
proposing a mediocre replacement.

> **Expertise reversal — the example fades by tier.** Per the worked-examples finding
> (`evidence-base.md` → instructional pillar; `coaching-loop.md` Step 2), a fully worked
> judgment helps **novices** (it shows the two moves) but is **redundant load for the more
> advanced**, who learn more by doing it themselves. So the coach fades it:
>
> | Tier | Worked-example depth at D2 |
> |---|---|
> | **Foundations** | **Full** — both moves shown, the rubric table and the runner-confirmed lie above, every step. |
> | **Working** | **Partial** — coach runs the snippet and shows the output, but leaves the *diagnosis* (does the name lie? what's the better name?) to the learner. |
> | **Advanced** | **Skeleton** — coach hands over the snippet and the rubric only; learner runs/reasons, names the lie, and proposes the fix unaided. |
> | **Frontier** | **None** — straight to the code (§6). |

---

## 5. Drill-generation spec

Instantiates the generation-spec format of `drill-generation.md` §1 for D2. Grading mode is
declared up front: **hybrid** (§5d) — the **lying-name behavior** sub-claim is **executable**
(run it; behavior wins), and the **name-quality** sub-claim is **rubric + golden exemplars**.
Report the two verdicts **separately**.

### 5a. Tier definitions (D2-specific)

The curriculum-wide tier names (`drill-generation.md` §1a) translated to this module. Drills
come in two flavors that the parameter space (§5b) mixes: **name-quality** drills (judge/propose
a name) and **lying-name** drills (does the name match behavior? — confirmed by running).

| Tier | D2 criterion | Example shape |
|---|---|---|
| **Foundations** | A **single, clear** naming problem on a familiar surface. *Name-quality:* a blatantly vague name (`tmp`, `data`, `do_it`) to diagnose and improve. *Lying-name:* a name with **one** obvious behavior mismatch (`get_average` that returns the sum; `sorted_copy` that mutates). **Diagnose it (run it) and fix it.** No decoys. | `get_average([2,4,6])` returns `12`; predict + name the lie. |
| **Working** | The mismatch is **less obvious** or the name is **plausible-but-wrong**: a predicate that returns a non-bool (`is_empty` returning a length), a silent no-op (`save_user` that drops falsy input), an inverted polarity. Intent and behavior diverge in a way a skim misses. **Catch it via the run, state the impact, propose a precise+honest name or fix.** | `is_empty(c)` returns `len(c)`; "looks right" for `[]` and `[1]`, breaks on `== True` for `[1,2]`. |
| **Advanced** | **Two interacting issues** or a codebase-level fault: a lying name **plus** a hidden state effect (`get_config` that persists the first default), a **consistency** violation across two functions (`fetch_user` vs `get_user` for the same concept, with **different return types** that crash a caller), or an inverted predicate inside otherwise-correct code. **Find it, prove it with a run, explain the impact, and propose the consistent/honest fix.** Articulate *why*. | `fetch_user`→dict, `get_user`→str; a caller's `b["name"]` raises `TypeError`. |
| **Frontier** | See §6 — one step past the learner's last comfortable success. | — |

A drill is mis-tiered if a Foundations lying-name hides its mismatch behind a decoy, or a
Working drill's name is *blatantly* wrong (that's Foundations), or an Advanced drill turns on a
single obvious lie with no second mechanism or consistency dimension. Apply the self-check
(`drill-generation.md` §4) and re-level before posing.

### 5b. Parameter space (axes the coach varies to avoid mode-collapse)

Pick a *different point on each axis* across successive drills (`drill-generation.md` §1b, §4
check 3). The axes for D2:

- **Drill flavor** — *name-quality* (judge/propose) · *lying-name* (does it match behavior?) ·
  *consistency* (two+ names for one concept, or one name for two concepts) · *naming-as-design-probe*
  (a name you can't make precise → split the entity).
- **Lie class** (the executable axis) — predicate with a **side effect** · `get_`/`fetch_` that
  **writes/creates** · name says **average/count/total** but returns a different quantity ·
  **`copy`/`new`** that mutates in place · **inverted polarity** (`filter_active` returns
  inactive; `is_X` returns `not X`) · wrong **return type** (predicate returns int/length; "count"
  returns bool) · **silent no-op** (a `save_`/`update_` that drops some inputs with no signal) ·
  **stale/over-claiming** (`sorted`, `validated`, `cached` when it isn't).
- **Vagueness class** (the rubric axis) — meaningless (`tmp`, `data`, `foo`, `x`) · too generic
  (`count`, `result`, `process`, `manager`, `handle`) · **too specific / over-claiming**
  (`selection` for any range; `emailString` for any contact) · disinformative (`list` that's a
  dict; `userArray` in Python).
- **Surface** — a standalone function · a function + its call site (where the lie bites) · **two
  functions** that should name a concept the same way · a small class with field names.
- **Data shape** — scalar · list · dict · object/record (consistency lies often surface across
  record-vs-field returns).
- **What the drill must produce** — *diagnose + run + rename* (Foundations) · *catch the subtle
  mismatch + impact + honest fix* (Working) · *catch two-issue/consistency fault + prove + explain
  why* (Advanced) · *teach-back the precision/consistency/honesty principle* (Advanced/Frontier).
- **Format** (`drill-generation.md` §6) — primarily **Debug-this** (here the "bug" is the
  name/behavior mismatch) and **Generation → Comparison** (learner proposes a name, coach reveals
  the gold); also **Error analysis** ("here is a name someone shipped — what does it mislead a
  reader into assuming?") and **Teach-it-back** (state the rule).

Keep an in-session log of the `(flavor, lie/vagueness class, surface, format)` tuples used; do
not repeat a tuple until the others are exercised.

### 5c. Common-error catalog

The *specific* naming failures, each with the conceptual gap it diagnoses
(`drill-generation.md` §1c format). Grounded in the comprehension studies (Hofmeister 2017;
Lawrie 2006; Feitelson 2022) and the precision/consistency canon (Ousterhout Ch. 14), **not** in
trivia. **The root of most of them is one inversion: writing the name for what the author
*meant* (or what was easy to type) instead of what the code *actually does* — the authoring-side
twin of A1's superbug (trusting intent over the machine) and A2's lying-name trap.** A name is a
*claim about behavior*; behavior is *ground truth*; when they diverge, the name is the defect.

```
Error: Ships a LYING name — the name claims one thing, the code does another (is_valid that
       mutates; get_user that creates; filter_active that returns the inactive; a "count" that
       returns a bool).
Diagnoses: Wrote the name from intent, not behavior. The single worst naming failure: it
           actively misleads every future reader (and every reviewer of AI-drafted code).
           Behavior wins — and the run proves the name false. (A2 lying-name; A1 superbug;
           Ousterhout: poor names "create ambiguities and misunderstandings that can result in
           bugs.")
Example trigger: any lying-name drill (Foundations get_average→sum; Working is_empty→length;
                 Advanced filter_active inverted). The coach RUNS it and shows the convicting output.

Error: Settles for a VAGUE name — tmp, data, val, result, count, process(), manager, do_it —
       that names the lifetime or the type but not the meaning.
Diagnoses: "Reasonably close" instead of precise; the name conveys ~no information, so the
           reader must read the body (defeating the name's purpose as documentation).
           (Ousterhout Red Flag: Vague Name; his block bug. Empirically, single-letter/cryptic
           names slow comprehension — Hofmeister 19%; Lawrie words > letters.)
Example trigger: name-quality drill on a `tmp(p, r)` that actually computes price-with-tax.

Error: Names the SAME concept inconsistently across the codebase — user / usr / account / u for
       one thing; fetch_/get_/load_ for the same operation; or reuses ONE name for TWO concepts
       (block = disk block here, file block there).
Diagnoses: No one-concept-one-name discipline. Breaks the reader's ability to reuse knowledge
           and (when one name means two things) plants a false assumption → a bug. (Ousterhout's
           three consistency requirements; the block bug is requirement #3 violated.)
Example trigger: Advanced fetch_user (→dict) vs get_user (→str) for the same concept; a caller's
                 `b["name"]` raises TypeError — the inconsistency is RUN to prove the crash.

Error: OVER-claims with a too-specific or guarantee-bearing name — sorted_copy that mutates;
       a `selection` parameter on a method that works on any range; `cachedResult` that isn't
       cached; `validatedInput` that wasn't validated.
Diagnoses: Precision overshoot: the name promises MORE than the code delivers, so the reader
           relies on a guarantee that doesn't exist. As misleading as a lie, by a different
           mechanism. (Ousterhout: a name can be "too specific," e.g. `selection` → use `range`.)
Example trigger: Foundations sorted_copy that calls items.sort() in place (run shows the caller's
                 list mutated and `result is original` True).

Error: Wrong RETURN TYPE for the name's word-class — a predicate (is_/has_/can_) that returns a
       non-bool (a length, an int, a string); a "count"/"num" that returns a bool.
Diagnoses: The name's grammatical class (predicate, noun-count) implies a type the code violates,
           so "looks right by luck" on some inputs and breaks on others (is_empty→len: 0 is falsy
           so [] reads right, but 2 == True is False so [1,2] breaks). (Ousterhout: "names of
           boolean variables should always be predicates.")
Example trigger: Working is_empty(c) -> len(c); run `is_empty([1,2]) == True` -> False.

Error: SILENT no-op / partial action under a name that promises the action — save_user that
       returns without saving on falsy input; update_X that skips when a guard fails, with no
       error and no signal.
Diagnoses: The name promises an effect the code sometimes doesn't perform, and gives the caller
           no way to know. The caller believes the postcondition holds. (Honesty failure #3: the
           name over-promises on a code path.)
Example trigger: Working save_user("") returns None and saves nothing; run shows `saved` missing
                 the input the caller "saved."

Error: BIKESHEDS toward a mythical "correct" name — relitigates a perfectly clear name, or blocks
       on a naming preference with no behavioral basis.
Diagnoses: Treats naming as having a unique right answer. Feitelson: two devs agree on a name only
           ~6.9% of the time, yet a clear name is usually understood — so precision + legibility
           matter, "the one true name" does not. Don't burn the review on it. (Ties to E3: naming
           is the classic bikeshed that buries the real issue.)
Example trigger: a learner who rejects a precise `price_with_tax` to insist on `grossPrice`, or
                 who debates casing while a lying name sits unflagged.

Error: Claims a naming CONVENTION (camelCase vs snake_case; a length rule) is empirically proven.
Diagnoses: Inflates contested/mixed evidence to [Verified]. The style studies CONTRADICT each
           other (Binkley 2009: camelCase more accurate but 13.5% slower; Sharif & Maletic 2010:
           no accuracy difference). The supported claim is "descriptive > cryptic," NOT "style X
           wins." (evidence-base.md honesty rule.)
Example trigger: a teach-back where the learner asserts "snake_case is proven more readable" —
                 corrected: consistency is what's defensible; the winner is not established.
```

### 5d. Grading mode

**Hybrid** (`drill-generation.md` §1d, §3, and the executable path §2). D2 deliberately has
**one executable sub-claim and one rubric sub-claim**, and the coach grades and reports them
**separately**:

1. **The lying-name sub-claim is EXECUTABLE — behavior wins.** "Does the name match the
   behavior?" is **not** an opinion. The coach **writes the snippet, runs it** via
   `python <skill-dir>/runtime/python/runner.py snippet.py` (`drill-generation.md` §2), and the
   **observed behavior settles it**: if `is_valid` mutates, it mutates; if `filter_active`
   returns the inactive set, the output shows it; if the inconsistent return type crashes a
   caller, the `status: error` / `TypeError` is the proof. **The coach surfaces the run** —
   pastes the exact snippet and its exact `stdout`/`status` into the reply (`coaching-loop.md` →
   Surface ground truth), because a grade whose evidence the learner can't see reads as a guess.
   This is the **direct tie to A2**: the lying name is convicted by the machine, never by the
   coach's say-so. Grading a learner's *proposed fix* uses the same path — apply it and re-run:
   the honest-named version must behave as named.

2. **The name-quality sub-claim is RUBRIC + golden exemplars.** "Is this a *good* name? is this
   a *better* name?" has **no executable ground truth** — it's a judgment (Feitelson: there is no
   uniquely correct name). The coach scores the learner's diagnosis/rename against the D2 rubric
   (§7), criterion by criterion (**precise? consistent? honest?**, each 3-point), and cites the
   closest exemplar in `exemplars/D2/<tier>.md`. The coach **says out loud**: *"the lie is a
   machine-verified fact; the name-quality call is a judgment graded against the module's rubric +
   exemplars, softer than the run."*

**Report the two verdicts separately.** A learner who **correctly catches the lie** (executable:
yes — they predicted the mutation/inversion and the run confirms it) but **proposes a weak
rename** (rubric: vague) is a **partial pass**, flagged exactly that way — and the reverse
(a lovely proposed name while *missing* that the original lies) is the more dangerous partial,
because the lie is the bug that ships. Per `drill-generation.md` §3, **rubric passes are softer
evidence than executable passes**; the coach never conflates "plausible name" with "provably
honest behavior."

---

## 6. Frontier band

Frontier is not a fixed tier — it tracks the learner's **demonstrated ceiling** and presses
**one step** past their last comfortable success along a single parameter axis
(`drill-generation.md` §5). Escalating two steps collapses to failure; escalating none loses the
desirable-difficulty benefit.

**What "one step" means here** (per `drill-generation.md` §5):
- **Advanced** = one non-trivial naming fault (a subtle lie + a second mechanism, or a
  cross-function consistency fault) found, **proven by a run**, and fixed with a precise+honest
  name, *with* an explanation of why.
- **Frontier-N** = N increments beyond Advanced; each increment adds exactly one new interacting
  dimension OR pushes one parameter-space axis up one notch.
- The learner's current Frontier-N is the highest N they have passed.

Escalation directions beyond Advanced for D2, with step counts:

1. **Subtler / costlier lie** (push the lie-class axis): from an inverted predicate → to a
   **silent partial-action** that only drops *some* inputs (Frontier-1) → to a name that is
   honest on the **happy path** but lies on an **edge case** the run must be crafted to expose
   (Frontier-2) → to a name whose lie only manifests **across two calls** (state persisted under
   a "pure" name, Frontier-3). Each is one increment, and each demands a *sharper* run to convict.

2. **Wider consistency fault** (push the consistency/surface axis): from two functions naming one
   concept differently → to **three+ call sites** where the same name silently means **two**
   things (the `block`-bug shape) and the learner must find *which* usage is the wrong one
   (Frontier-1) → to a **multi-file** rename where making one name consistent forces a cascade
   (Frontier-2). Each added surface/conflict is one increment.

3. **Naming as a design probe** (push the flavor axis): a name the learner *cannot* make precise
   because the entity does two jobs — the right answer is **"split the function/field, then name
   the pieces,"** not "find a cleverer single word" (Ousterhout's *Hard to Pick Name* red flag).
   Recognizing that the naming difficulty is a *design* signal is one increment; proposing the
   split is another.

4. **The contested-evidence frontier** (push the honesty axis): hand the learner a *style/casing*
   argument or a *Clean Code*-flavored prescription and ask them to **separate what the evidence
   supports from what is craft/contested**. Holding "descriptive > cryptic is `[Some empirical]`"
   apart from "camelCase wins is *not* established" — and refusing to inflate either — is one
   increment over a clean catch-and-rename.

5. **Reviewing AI-drafted names → the AI-era frontier.** Agent output reads fluently and tends to
   produce *plausible-sounding* names that may not match the behavior it generated. A diff where
   the name is idiomatic and confident but the body **lies** is the spec-§12 apex case: one
   increment for "AI-plausible name," another for "and you must *run it* rather than trust the
   fluent label." (Ties to F1 calibration — over-trusting fluent output is the documented miss;
   here the antidote is "behavior wins, so run it.")

Track the level as `D2: Frontier-N`. Reset condition: two consecutive failures at the same level
→ drop to Advanced for one drill, then re-approach (`drill-generation.md` §5).

---

## 7. Mastery rubric

The observable per-tier bars, instantiating the rubric shape of `assessment.md` Part 2, scored
against the three D2 dimensions. Two cross-cutting requirements apply at every tier above
Foundations: **product *and* process** (caught the lie / proposed the name *and* can say **why**
— a correct catch with a hand-wavy reason, or a rename with no principle, is a Foundations-level
pass at best), and **unaided + durable** (a same-session streak is provisional until a delayed
re-assessment or the real-code transfer task confirms it; `assessment.md` Parts 3–5).

**The three scored dimensions** (each 3-point: absent / partial / solid). The first is the
**executable** one; the latter two are **rubric** — report them separately (§5d):

- **D1 — Honest? (executable, behavior wins).** Did the learner correctly determine whether the
  name matches the behavior — *confirmed by the run*? Catching a real lie (or correctly clearing
  an honest name) is the machine-verified half.
- **D2 — Precise? (rubric).** Is the proposed/judged name specific enough to convey *what it is
  and isn't*, without over-claiming? Did they diagnose vagueness or over-specificity correctly?
- **D3 — Consistent? (rubric).** Did they apply (or flag the violation of) one-concept-one-name,
  and avoid bikeshedding toward a mythical "right" name?

| Tier | Observable bar for D2 |
|---|---|
| **Foundations** | On a single-issue drill: for a **lying name**, predicts the mismatch and — after the coach runs it — **names the lie and its impact** ("`get_average` returns the *sum*: `get_average([2,4,6])` is `12`, not `4`"); for a **vague name**, diagnoses *why* it's uninformative and proposes a precise replacement. D1 solid (the run confirms the catch); D2 at least partial. Allowed *with* the worked example faded to one missing step. |
| **Working** | On a **plausible-but-wrong** name (predicate returning a non-bool; silent no-op; inverted polarity), **unaided**: catches the mismatch and **uses the run as the proof** (D1), states the impact at the call site, **and** proposes a precise + honest name *or* the behavior fix (D2/D3). Catches the lie but proposes a vague rename ⇒ partial pass, flagged. On 3 of 4 unseen drills, mixing name-quality and lying-name flavors. |
| **Advanced** | On a **two-issue / consistency** drill (lying name + hidden state effect, or `fetch_`/`get_` inconsistency that crashes a caller), **unaided**: finds it, **proves it with a run** (D1 — e.g. shows the `TypeError` the inconsistency causes), **explains the impact precisely**, and proposes the **consistent, honest** fix (verified by the coach re-running it). Articulates the **principle** on a teach-it-back (`drill-generation.md` §6) — "a name is a claim about behavior; precise + consistent + never-lying; behavior is ground truth" — and correctly separates `[Some empirical]` (descriptive > cryptic) from `[Practitioner-canon]`/contested (style conventions). |
| **Frontier** | `Frontier-N`: presses one dimension past the last comfortable success per §6 / `drill-generation.md` §5 (subtler/cross-call lie → wider consistency fault → naming-as-design-probe → contested-evidence → AI-drafted names). A moving target, not a fixed bar. |

Promotion is by **performance, not tenure** (`assessment.md` rule 1); the coach marks a tier from
what the learner *does* on unseen drills, never from "I write clean code." Held-out re-assessment
and **real-code transfer** outrank a same-session streak (`assessment.md` Part 5) — and for the
*name-quality* (rubric) half especially, the real-code signal is weighted heavily (a clean
synthetic streak that doesn't show up when the learner renames their *own* lying functions is not
yet mastery). The *lying-name* (executable) half is firmer evidence, but still subject to the
transfer caveat.

---

## 8. Anti-patterns & evidence caveat

**Anti-patterns this module exists to break** (each is a catalog entry in §5c, surfaced as a
*behavior*):

- **Shipping a name that lies.** The cardinal sin: `is_valid` that mutates, `get_user` that
  creates, `filter_active` that returns the inactive, a "count" that returns a bool. It misleads
  every future reader and every reviewer of AI-drafted code. The fix is mechanical and
  **executable**: *run the code, see what it does, and make the name (or the behavior) tell that
  truth.* Behavior wins — so let it.
- **Settling for vague.** `tmp`, `data`, `result`, `process()`, `manager`. The name should
  create an image of *what it is and isn't*; a vague name forces the reader into the body, which
  is the whole cost the name was supposed to remove. The fix: name the *meaning*, not the
  lifetime or the type.
- **Over-claiming.** `sorted_copy` that mutates, `cachedX` that isn't cached, a `selection`
  parameter on a method that takes any range. Promising a guarantee the code doesn't keep is a
  lie by overshoot. The fix: name only what's true; widen an over-specific name.
- **Naming the same concept five ways (or one name two ways).** Inconsistency is a top cause of
  obscurity, and a name reused for two meanings is how the `block` bug happened. The fix:
  one concept → one name, everywhere; one name → one concept, never shared.
- **Bikeshedding the name / chasing the "one true name."** Relitigating a clear name, or blocking
  on casing, while a lying name sits unflagged. Feitelson: agreement is ~6.9%, yet a clear name is
  usually understood — so optimize for *precision and legibility*, not consensus, and spend the
  review on the issue that matters (E3).

**Evidence caveat (this is a `[Some empirical] + [Practitioner-canon]` module — say so).** The
honesty stance here is sharper than for most of Track D *because* a real empirical layer exists,
and the temptation is to let the famous book borrow its credibility:

- The **empirical** half is **real but narrow**. Three controlled studies support **"descriptive,
  full-word identifiers aid comprehension"** (Hofmeister 2017: words **19% faster** at
  defect-finding than letters *and* abbreviations, N=72 C# devs — *and the authors call the effect
  "fairly small"*; Lawrie 2006: full words best, **no difference between full words and
  abbreviations**, N=128; Feitelson 2022: no uniquely correct name, but precise/concept-complete
  names are more legible, N=334). State this as *"controlled studies show descriptive names help
  comprehension,"* **not** *"research proves my naming rules."* The two papers even **disagree on
  abbreviations** — honest evidence is messier than the slogan.
- The **`19%` belongs to Hofmeister, not Lawrie.** A widespread secondary-source misattribution
  pins "19% comprehension increase" on Lawrie 2006; the figure is **not in that paper** (which
  measured description-quality ratings, not speed). The 19% is Hofmeister 2017's *defect-finding
  speed* result. The coach cites it correctly or not at all.
- **Style conventions are NOT proven.** camelCase vs snake_case is **contested and
  contradictory** (Binkley 2009: camelCase more accurate but **13.5% slower**; Sharif & Maletic
  2010: **no accuracy difference**). The coach must **never** present a casing/length convention
  as empirically settled. What *is* defensible is **consistency**; the *winner* is not.
- The **craft** half (precision + consistency, the two red flags, "names are documentation") is
  **`[Practitioner-canon]`** — Ousterhout Ch. 14, respected and well-argued, but **craft, not
  science**; and even *it* prints the Go camp's dissent on name length. **Clean Code** is cited
  **with care**: contested opinion, leaned on only where the point also stands on its own.
- The **curriculum-wide transfer caveat** applies in full: that *coaching naming on synthetic
  snippets* causally improves a given engineer's production naming is the open question. The
  lying-name (executable) half is firmer — behavior is ground truth — but the *causal upskilling*
  claim is not. The coach leans on the transfer task (§9) — renaming the learner's **own** code —
  as the honest individual-level evidence.

No claim in this module is dressed above its badge: descriptive-names-help is `[Some empirical]`;
the prescriptions are `[Practitioner-canon]`; style conventions are flagged contested; the
lying-name verdict is executable fact.

---

## 9. Transfer task

**The only honest test of whether the gym drill transferred to the job is applying it to the
learner's own real code** (`assessment.md` Part 4; `evidence-base.md` → transfer caveat,
consequence 2).

> **Your turn:** Open **your own codebase** and find **two** things.
>
> **(1) A name that lies — or that you had to read the body to trust.** A function, variable, or
> field whose name once made you (or a teammate) assume the wrong behavior: a `get_`/`load_` that
> secretly writes, an `is_`/`has_` with a side effect, a `count`/`total`/`average` that returns
> something else, a `copy` that mutates, a flag whose name doesn't say what `True` means. **Then
> prove it:** reduce it to a minimal snippet and **run it through `runner.py`** — confirm the
> behavior the name hides, exactly as the worked example convicts `is_valid`. State the lie, the
> impact at a call site, and the fix (rename, or change the behavior to match the honest name).
>
> **(2) A concept your codebase names inconsistently** — the same thing called `user`/`usr`/`u`
> across files, or `fetch_`/`get_`/`load_` for the same operation, or (worst) **one** name used
> for **two** different concepts. Pick the single name you'd standardize on, say why, and note
> where the inconsistency could plant a false assumption.
>
> Then step back: for the lying name, **was it written from what the author *meant*, or from what
> the code *does*?** That gap — intent over behavior — is the exact trap this module targets, and
> it's the same superbug A2 teaches readers to fear.

**Grading is softer and named as such** (`assessment.md` Part 4). Real code has no clean answer
key for *name quality*; the coach grades against the §7 rubric (D1 honest / D2 precise / D3
consistent) and says: *"the lie itself I can verify by running your snippet — that part is fact;
whether your replacement name is the best one is a judgment call on your real code, not a
machine-verifiable result."* **For the lying-name find, the executable sub-claim is real and the
coach uses the runner:** reduce the suspected mismatch to a minimal snippet, run it through
`runner.py`, and confirm the hidden behavior *before* the learner asserts the lie — the same
discipline as the §5d catch, now on the learner's own code. **Transfer evidence is weighted
heavily:** a learner who aces synthetic naming drills but cannot find a single lying or
inconsistent name in their own repo — or who finds one but can't make the run convict it — has
**not** transferred the skill, and the tracker notes that gap as more diagnostic than another
passed synthetic drill.

---

## Cross-references

- Drill mechanics, the **hybrid grading path** (executable lying-name check via §2 + rubric +
  exemplars via §3), exercise formats (Debug-this, Generation→Comparison, Error analysis,
  Teach-it-back), Frontier escalation: `references/drill-generation.md` (this module instantiates
  §1 and follows §2, §3, §4, §5).
- Session delivery (pause/no-spoiler hard stop, tier-faded worked example, **surface the run** so
  the learner sees the lie convicted, direct feedback, scaffolding ladder):
  `references/coaching-loop.md`.
- D2 entry task, per-skill routing, mastery-rubric shape, held-out re-assessment, **real-code
  transfer** weighting: `references/assessment.md` (the D2 entry task: judge a vague/lying name,
  propose a better one, and say whether the name matches the behavior — with the
  lying-name half verified by running it).
- Evidence grounding (the naming/identifier-comprehension studies — Hofmeister 2017, Lawrie 2006,
  Feitelson 2022 — at `[Some empirical]`; the precision/consistency canon — Ousterhout Ch. 14 —
  at `[Practitioner-canon]`; the contested style evidence — Binkley 2009 / Sharif & Maletic 2010;
  the worked-examples / expertise-reversal instructional finding): `references/evidence-base.md`
  → *Naming & identifier comprehension (module D2)*.
- Soft prerequisite (reading name beacons and catching lying names — the *reading* side this
  module writes toward): module **A2** (code reading & chunking); related execution-model modules
  **A1** (the superbug; side-effect/mutation surprises) and **A3** (tracing to confirm behavior);
  adjacent **B3** (a name is a tiny spec) and **E3** (don't let naming be the bikeshed that buries
  the real issue).
- Golden exemplars (~3 per tier, each with a **runner-verified** lying-name catch *or* a
  name-quality gold + rubric note): `exemplars/D2/foundations.md`, `exemplars/D2/working.md`,
  `exemplars/D2/advanced.md`.
</content>
</invoke>
