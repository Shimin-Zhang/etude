# E1 — Large-codebase comprehension `[Verified]`

> **Module type.** **Mixed-status by design.** Honest prose badge:
> **`[Verified]` core (the comprehension findings) + `[Practitioner-canon]` scale (the
> orient procedure)**. The *mechanisms* E1 uses — chunking, beacons, hypothesis-driven
> tracing — are `[Verified]` (`evidence-base.md` → Findings 2, 3, 6), but the evidence is
> from people reading **one program / one function**; applying those mechanisms at
> **repository grain**, and the **seven-step orient procedure** itself, are
> `[Practitioner-canon]` craft. The validator badge on this file is `[Verified]`; the
> coach must never present the orient procedure as a measured causal result.
>
> **Core idea.** To understand a big unfamiliar repo, you do **not** read it. You **chunk
> it at the file/module level first** — read the directory tree as a table of contents,
> find the entry points, read the tests as the executable spec, locate the core modules
> — and build a **map** (where it starts, what the core is, where feature X lives, the one
> file to open first). Strategic, **not** exhaustive. *Orient, don't crawl.*

---

## 1. Evidence basis `[Verified]` core + `[Practitioner-canon]` scale

E1 is **two layers, badged separately**, and the coach keeps them apart
(`evidence-base.md` → badge rules):

### (a) The `[Verified]` core — comprehension mechanisms, extended to repo scale

E1 rests on **three `[Verified]` findings already in `evidence-base.md`** — cite them via
`evidence-base.md` → Finding N; **do not re-derive or duplicate** them here. What E1 adds
is the move *up one grain*: the same mechanisms, applied to **files and modules** instead
of lines and statements.

- **Finding 2 — experts chunk code into larger semantic units** (Shneiderman 1976;
  McKeithen 1981; Gobet & Simon 1996). At function scale a *chunk* is a group of lines
  (A2). **At repo scale a chunk is a directory / package**: the top-level layout is the
  architecture's intended decomposition — `api/`, `models/`, `cli/`, `tests/` — and you
  read the **tree** before any file. A repo you can't hold in your head becomes **five or
  six parts you can.** Same mechanism, coarser unit.
- **Finding 3 — beacons and plans are real cues experts exploit** (Brooks 1983; Soloway &
  Ehrlich 1984; Crosby et al. 2002). At function scale a beacon is a swap or an
  accumulator (A2). **At repo scale the beacons are structural**: a `routes.py`/`urls.py`
  signals "the request surface," a `models.py` "the domain," a `__main__.py`/`cli.py`/
  `app.py` "the entry point," a `tests/` directory "the spec," and a **frequently-changed
  file** (git churn) "the heart." You scan for these instead of reading every file
  equally — exactly the experts' selective attention to structure, one level up.
- **Finding 6 — reading → tracing → writing is a developmental hierarchy** (Lopez et al.
  2008; tracing is `[Verified]`). At function scale you trace one function (A3). **At repo
  scale you trace ONE path** — one request, one command — *across files*, from the entry
  point to the code that owns the behavior, rather than the whole system. Tracing extends
  from a call tree to a cross-file path.

**Honest boundary on the extension.** Findings 2/3/6 were established on people
comprehending a **single program or function** (FORTRAN/ALGOL/Pascal, 1976–2008). That the
*same* chunking/beacon/tracing advantage holds when the unit is a **file or a package** is
a **reasonable application of verified mechanisms, not a separately verified result.** The
coach says "we're applying verified comprehension findings at a coarser grain," never
"research shows the orient procedure improves repo comprehension."

### (b) The `[Practitioner-canon]` scale — the orient procedure (craft)

The **seven-step orient procedure** itself (README → directory-tree → entry points →
tests-as-spec → core modules → git-churn → gateway artifact) is **respected craft**, vetted
during authoring against the named sources — **not** an empirical finding. Cite via
`evidence-base.md` → *Large-codebase comprehension (module E1)* (proposed addition):

- **The orient procedure is credited to the `orient` module by Dr. Michael Mullarkey**, in
  Cat Hicks' *Learning Opportunities* (CC-BY 4.0; `evidence-base.md` → Attribution). E1
  adapts its strategic, artifact-first sequence and grounds each step in the comprehension
  science above. **Credit them.**
- **Spinellis, D. (2003). *Code Reading: The Open Source Perspective.*** Addison-Wesley.
  `[Practitioner-canon]` — the canonical text on reading **real, large** code strategically
  (entry points, build/configuration files, the directory structure as a map), with 600+
  real-world examples. The craft anchor for "read for what you need, in priority order."
- **Dagenais, B., & Robillard, M. P. (2010). Creating and evolving developer
  documentation.** *FSE 2010*, 127–136. `[Practitioner-canon]` (empirical study of OSS
  documentation practice) — grounds the **gateway-artifact** idea: developer documentation
  is a *deliberately created and evolved* artifact whose authors decide what a newcomer
  needs to orient. **(Honesty flag: "gateway artifact" / "the one file that unlocks the
  rest" is the curriculum's framing of the orient procedure, not a verbatim term from the
  paper.)**
- **Feathers, M. C. (2004). *Working Effectively with Legacy Code.*** Prentice Hall
  (`evidence-base.md` → reading spine, staff anchor for E1). `[Practitioner-canon]` —
  orienting in code **without tests** you didn't write: find a **seam**, pin behavior with
  a **characterization test**, then work outward. The discipline for the
  no-documentation, no-tests corner of the orient procedure.

**Why these license this module.** The verified findings license the *mechanisms* (chunk at
file grain; scan structural beacons; trace one path); the craft sources license the
*procedure* (which seven artifacts to read, in what order, to build the map fastest). The
combined claim E1 teaches: **orient in a big unfamiliar repo by mapping it from a handful of
high-signal artifacts — entry point, tests, core, churn, gateway doc — before reading any
file in full.**

**Read through the transfer caveat.** Beyond the function→repo extension caveat above, the
curriculum-wide transfer caveat applies in full (`evidence-base.md`): the verified evidence
is from *novices in introductory courses*, and that drilling orientation on synthetic repos
*causally* improves an engineer's real-repo onboarding is the open question the transfer
task (§9) tests honestly. **AI-era note:** orienting fast in code you didn't write is a core
verification-era skill — engineers increasingly inherit large agent-generated and
unfamiliar codebases, and *unaided* comprehension is what atrophies first under heavy AI
assistance (`evidence-base.md` → AI-era impact: Anthropic RCT, ~17% lower unaided
comprehension/debugging). That is `[Verified-adjacent]` **priority-steering, not proof** —
it is *why* E1 matters now, not a claim of this module.

---

## 2. Soft prerequisites

**Softly assumes A2 (code reading & chunking) and A3 (execution tracing).** E1 is A2 and A3
**one grain up**: A2 chunks a function into semantic units; E1 chunks a *repo* into
packages. A3 traces one function; E1 traces one *cross-file path*. A learner who cannot
chunk or trace a single function will struggle to chunk a tree or trace a request — the gap
surfaces *inside* the orientation. **C2 (reading stack traces)** also informs E1: a
traceback is often the *entry into* an unfamiliar repo — it names the files and frames in
the failing path, and C2's "walk to the deepest frame that is your code" is orientation in
miniature. **A1 (notional machine)** sits under all of it (to say what a module *does* you
must be able to simulate it).

Per `assessment.md`, soft prerequisites **inform, never gate** — the buffet rule holds (any
learner may open any module at any tier). If a learner flails at E1 because they read every
file linearly or can't trace across files, the coach notes the gap likely traces to A2/A3
and *suggests* shoring those up — but does **not** forbid E1. Conversely, E1 underlies
**E2** (architectural judgment — you must orient before you can judge a structure) and
**C3** (debugging a failure across a system you first had to map).

---

## 3. The mental model

**A big repo is not a big file. You do not read it top to bottom. You build a *map* from a
few high-signal artifacts — the README, the directory tree, the entry points, the tests,
the core modules, the change history, the one gateway doc — and you read **only** the path
that matters. Chunk at the file/module level first; read for structure, not for
completeness.**

The procedure is the model. Seven artifacts, in priority order — each answers one
orientation question, and each is anchored to a **repo-scale beacon**:

| # | Artifact | The question it answers | The repo-scale beacon / why it's high-signal |
|---|---|---|---|
| 1 | **README** | *What is this, and how do I run it?* | The project's own elevator pitch + the install/run command — the cheapest "what & how" in the repo. |
| 2 | **Directory tree** (as table of contents) | *What are the major parts, and how is it decomposed?* | Top-level dirs are the architecture's **intended chunks** (`api/`, `models/`, `cli/`, `tests/`). Chunk the repo *here* — Finding 2 at file grain. |
| 3 | **Entry points** (`main` / CLI / routes) | *Where does execution actually begin?* | `__main__.py`, `cli.py`, `app.py`, `urls.py`/`routes.py`, a `console_scripts` line — the **door** into the running system. |
| 4 | **Tests** (as executable spec) | *What is it* supposed *to do?* | A test names a unit and **asserts its intended behavior** — and it **runs**, so it is executable ground truth for "what does module M do?" (the one runnable sub-claim — §5d). |
| 5 | **Core modules** | *What is the domain; what does everything depend on?* | The **most-imported** files / the ones defining the central types (`models.py`, `core.py`). The semantic center of the map. |
| 6 | **Git churn** (as core-finder) | *Where does the real work concentrate?* | **Frequently-changed** files are where behavior lives and evolves — a beacon that only exists at repo scale, over time. |
| 7 | **The gateway artifact** | *The one doc/file that unlocks the rest.* | A `CONTRIBUTING.md`, an `ARCHITECTURE.md`, or the central `models.py` — the single highest-leverage **first read** (Dagenais & Robillard: dev docs are written to orient contributors). |

You do **not** run all seven every time — you run **as many as it takes to answer the
question**, in this priority order. The output is a four-part **map**: **entry point · core
module · where feature X lives · the one file to open first (and why).**

**The discipline in one line: *orient, don't crawl* — map the repo from a handful of
high-signal artifacts before you read any file in full.** The novice failure is to open the
first (or biggest, or alphabetically-first) file and read linearly, arriving with no map —
the repo-scale version of narrating a function token-by-token (A2). The expert move is to
read the **tree, the entry point, and one test**, and summarize the system in a sentence.

Three corollaries the module drills:

1. **Chunk at the file/module level before the line level.** The directory tree *is* a
   chunk map; read it first. A 200-file repo is **six packages** you can reason about
   (A2's chunking, one grain up; `evidence-base.md` → Finding 2).
2. **Strategic, not exhaustive.** You read the **5–7 highest-information artifacts**, not
   the whole repo. Orienting is *triage* (Spinellis), not crawling. "I'd have to read
   everything first" is the anti-pattern, not the method.
3. **Behavior over names — at scale too.** A folder called `core/` may be dead; a `utils.py`
   may be the heart; the real entry point may hide in a `console_scripts` line, not a
   `__main__.py`. When a **directory-name beacon** and the **behavior** disagree, the
   behavior wins — confirm the entry/core by **tracing the import-and-call chain or running
   a test**, not by the folder's name (A2's lying-beacon, one grain up; Soloway & Ehrlich
   1984; `evidence-base.md` → Finding 3).

---

## 4. Worked example — orient in a small CLI repo, then verify a module with its test

*(Foundations depth: the full orient pass and the four-part map shown, and one module's
behavior verified by running its test. This fades by tier — see the note after the
example.)*

The skill is to **read the map, not the territory.** You are dropped into this unfamiliar
repo (shown as a file tree + the key files) and asked to **orient**:

```
taskcli/
├── README.md
├── pyproject.toml          #  [project.scripts]  task = "taskcli.__main__:main"
├── taskcli/
│   ├── __init__.py
│   ├── __main__.py         #  entry: parse argv, dispatch  (also `python -m taskcli`)
│   ├── cli.py              #  command parsing / dispatch table
│   ├── commands.py         #  add / done / list  implementations
│   ├── models.py           #  Task dataclass + sort_key (priority logic)
│   └── store.py            #  load / save tasks to JSON
└── tests/
    ├── test_models.py      #  asserts how `list` orders tasks
    └── test_store.py       #  asserts the JSON round-trip
```

```python
# README.md (excerpt)
#   taskcli — a tiny command-line task tracker.
#   Usage:  python -m taskcli add "ship release" --priority 5
#           python -m taskcli list

# taskcli/__main__.py
import sys
from taskcli.cli import dispatch
def main(argv=None):
    return dispatch(sys.argv[1:] if argv is None else argv)

# taskcli/cli.py  (only PARSES argv and routes to a command)
from taskcli import commands, store
def dispatch(argv):
    tasks = store.load("tasks.json")
    if argv and argv[0] == "list":
        return commands.list_tasks(tasks)
    # ... add / done elided ...

# taskcli/commands.py
from taskcli.models import Task
def list_tasks(tasks):
    return [t.text for t in sorted(tasks, key=Task.sort_key)]   # <- delegates ordering

# taskcli/models.py
from dataclasses import dataclass
@dataclass
class Task:
    text: str
    priority: int = 1          # higher = more urgent
    done: bool = False
    def sort_key(self):        # not-done first; higher priority first; then text
        return (self.done, -self.priority, self.text)
```

**Run the orient procedure (steps 1–5; churn/gateway noted):**

| Step | What I read | What it told me |
|---|---|---|
| 1 **README** | "tiny command-line task tracker"; `python -m taskcli list` | *What & how to run* in two lines. |
| 2 **Tree** | `taskcli/` package + `tests/`; six modules | Chunks: **entry** (`__main__`/`cli`) · **domain** (`models`) · **behavior** (`commands`) · **persistence** (`store`). |
| 3 **Entry** | `pyproject` `[project.scripts] task = "taskcli.__main__:main"` **and** `__main__.py` | Execution begins at **`taskcli/__main__.py:main`** → `cli.dispatch`. |
| 4 **Tests** | `test_models.py` asserts list ordering | The **spec** for "how does `list` order tasks?" — and it **runs** (below). |
| 5 **Core** | `models.py` defines `Task`, imported by `commands` (and indirectly `cli`) | **`models.py`** is the domain center — the type everything passes around. |

**The four-part map (the answer):**

- **Entry point:** `taskcli/__main__.py` → `main()` → `cli.dispatch(argv)`. Confirmed by
  *two* beacons: the README run line and the `pyproject` `console_scripts` entry.
- **Core module:** `taskcli/models.py` — defines `Task` and `sort_key`; imported by
  `commands.py`. The domain everything depends on.
- **Where to change feature X = "how `list` orders tasks"** (say, sort by due-date instead
  of priority): **`models.py` → `Task.sort_key`** (the ordering *rule*), reached from
  `commands.list_tasks`. **Not** `cli.py` — `cli.py` only matches the word `"list"` and
  routes it; it owns *no* ordering logic. This is the trace step: follow `__main__` →
  `cli.dispatch` → `commands.list_tasks` → `Task.sort_key`.
- **First file to open:** **`README.md`** (the gateway — what it is + how to run, the
  cheapest orientation), then **`models.py`** (the domain type the rest is built on). You
  rank the gateway *above* the nine source files.

**Verify a module with its test** (the one executable sub-claim — `drill-generation.md` §2;
the coach *runs* it, never guesses). Lift `models.py` + `tests/test_models.py` into one
runnable file (the multi-file example collapsed to a single snippet the runner accepts) and
run it:

```
$ python <skill-dir>/runtime/python/runner.py E1_worked_sortkey.py
order: ['ship release', 'call dentist', 'buy milk', 'archive logs']
test_models.py: 1 passed
status: ok
```

So `test_models.py` **pins the ordering rule**: not-done before done, then higher priority
first, then text — and it lives in **`Task.sort_key`**. To change how `list` orders tasks,
you change `sort_key` in `models.py`. The **test is the executable spec**, and running it
*confirms* the map's feature-X answer instead of asserting it.

**What orienting makes visible** (and crawling hides): you summarized a six-module package
as **"a CLI task tracker; entry at `__main__`, domain in `models`, ordering owned by
`Task.sort_key`"** by reading the **README, the tree, one entry file, and one test** —
four artifacts, not nine files. A reader who opened `cli.py` first and read top-to-bottom would land on the
*dispatch table* and likely answer "change ordering in `cli.py`" — **wrong**, because
`cli.py` only routes the command; the behavior is one trace-hop away in `models.py`. The
**map** is the thing that transfers.

> **Expertise reversal — the example fades by tier.** Per the worked-examples finding
> (`evidence-base.md` → instructional pillar; `coaching-loop.md` Step 2), a fully-worked
> orient pass *helps novices* (it shows the moves while the schema forms) but becomes
> **redundant load for the more advanced** — they learn more by orienting themselves. So
> the coach fades it:
>
> | Tier | Worked-example depth at E1 |
> |---|---|
> | **Foundations** | **Full** — coach shows the orient table, the four-part map, and runs one test, exactly as above. |
> | **Working** | **Partial** — coach gives the tree + README and names the **entry point**, leaving the learner to find the core module, locate feature X (one trace-hop), and pick the first file. |
> | **Advanced** | **Skeleton** — coach hands the raw tree + key files only; learner produces the whole map unaided, justifies the ranking, and confirms one module via its test. |
> | **Frontier** | **None** — straight to a denser / lying-structure / cue-stripped repo (§6). |

---

## 5. Drill-generation spec

Instantiates the generation-spec format of `drill-generation.md` §1 for E1. Grading mode is
declared up front: **hybrid, mostly rubric** (§5d) — orienting in a repo is a **strategy,
not a computation**, so the **map** is rubric-graded against golden exemplars; the **one
executable sub-claim** is *"what does module M do?"*, confirmed by **running its test**.

### 5a. Tier definitions (E1-specific)

Every drill **presents a small multi-file codebase AS TEXT** (a file tree + the key files)
and asks for the **orientation map**: entry point · core module · where to change feature X
· the one file to open first (and why).

| Tier | E1 criterion | Example shape |
|---|---|---|
| **Foundations** | A **small** repo (≤ ~6 files, **helpful names**, feature owned by **one** file). **Name the entry point and the core module**, each justified by a beacon (the `__main__`/README run line; the most-imported file), and answer *"what does module M do?"* for a module with a test (runner-checkable). | A tiny CLI, a one-function library, or a minimal Flask app: name the entry + core; run the core's test. |
| **Working** | An **unseen ~8–15-file** repo, **mixed cues**. Produce the **full four-part map unaided**, where **feature X takes one trace-hop** (the behavior lives one import away from where the feature is *named*). Justify each answer by structure/beacons, not folder names; confirm one module via its test where available. | A CLI where "filter/sort" lives in `commands`/`models`, not `cli`; a web service where the discount rule lives in `pricing`, not the `routes` that name the endpoint. |
| **Advanced** | A **denser / partly-lying-structure** repo: misleading folder names, an entry point hidden in `console_scripts`, or a **cross-cutting feature spread across 3 files**. Recover the **real** entry/core when names mislead (confirm by tracing the import-call chain or running a test), trace the cross-file path, **rank the one gateway file**, and articulate the orient procedure as a general method (teach-it-back). | A repo whose `core/` is dead code and whose heart is `services/`; a uniqueness rule spread over `routes → service → repository`. |
| **Frontier** | See §6 — a moving target one step past the learner's last comfortable success (more files, worse-lying names, more trace-hops, stripped cues). | — |

A drill is mis-tiered if a "Foundations" repo hides its entry behind a lying name, or an
"Advanced" repo has fully helpful names and a one-file feature; apply the self-check
(`drill-generation.md` §4) and re-level before posing.

### 5b. Parameter space (axes the coach varies to avoid mode-collapse)

Pick a *different point on each axis* across successive drills (`drill-generation.md` §1b,
§4 check 3). The axes for E1:

- **Repo shape / domain** — CLI app · web service (routes/views) · library / package ·
  data pipeline (extract→transform→load) · framework app (Django/Flask conventions).
- **Entry-point kind** — `__main__.py` / `python -m` · a `console_scripts` line in
  `pyproject.toml`/`setup.py` · a Flask `app.py` / `create_app()` · `urls.py` → `views.py`
  · a `main()` in a named module.
- **Naming honesty** — helpful/idiomatic · neutral · **lying** folder/file names (`core/`
  is dead; `utils.py` is the heart) · a *mix* where some names lie and some don't.
- **Feature-X spread** — owned by **one** file (Foundations) · a **two-hop** path
  (Working) · a **three-hop** cross-cutting path (Advanced).
- **Cue availability** — README present · README thin/absent · tests present · tests absent
  · **git-churn** summary given (a short "most-changed files" list).
- **Question stressed** — *entry point?* · *core module?* · *where to change feature X?* ·
  *which file first + why?* · *what does module M do?* (the executable, test-backed one).
- **Format** (`drill-generation.md` §6) — primarily **Generation → Comparison** (learner
  produces the map, coach reveals the gold) and **Teach-it-back** (articulate the orient
  method); also **Trace-the-path** for the feature-X location and **Debug-this** when a
  lying name has hidden the real owner of a behavior.

Keep an in-session log of the `(repo shape, entry kind, naming honesty, feature spread,
question)` tuples used; do not repeat a tuple until the others are exercised.

### 5c. Common-error catalog

The *specific* orientation failures, each with the conceptual gap it diagnoses
(`drill-generation.md` §1c format). Grounded in the comprehension findings
(`evidence-base.md` → Findings 2/3/6) and the orient/code-reading craft (Spinellis 2003;
Dagenais & Robillard 2010; Feathers 2004; the `orient` module), **not** in trivia. **The
root of most of them is one misconception: "to understand a repo you must read it (file by
file, top to bottom), so a big repo is just a big version of reading one file." The orient
move is the opposite: you *map* the repo from a few high-signal artifacts, then read only
the path that matters.**

```
Error: Starts reading files linearly — opens the first / biggest / alphabetically-first
       file and reads top-to-bottom — and arrives with no map.
Diagnoses: Crawl, not orient. Treats a repo as one long file to read linearly; no triage of
           which artifacts carry the most orientation value, no file-level chunking. The
           repo-scale version of narrating a function token-by-token. (Finding 2 at file
           grain; Spinellis — read strategically, in priority order.)
Example trigger: any Working repo — ask for the map; a learner who says "I'd open app.py and
                 start reading" instead of reading the tree + a test is the tell.

Error: Skips the README and the directory tree; dives straight into source.
Diagnoses: Ignores the cheapest, highest-information artifacts — the project's own pitch and
           map — and reconstructs from scratch what the repo already documents. (Orient
           steps 1-2; Dagenais & Robillard — the gateway doc exists to orient you.)
Example trigger: a repo with an informative README and a clear tree — the learner never
                 cites either and rebuilds the layout by reading modules.

Error: Names a folder as the entry point / core by its NAME (`core/`, `main/`, `utils/`)
       without confirming what actually runs or what is actually imported.
Diagnoses: Trusts a directory-name beacon over behavior — the repo-scale discourse violation.
           `core/` may be dead; the real entry may be a console_scripts line. Did not confirm
           by tracing the import-call chain or running a test. (A2 lying-beacon, one grain up;
           Soloway & Ehrlich 1984; corollary 3.)
Example trigger: the lying-structure repo — `core/legacy.py` looks central but nothing
                 imports it; the heart is `services/billing.py`.

Error: "I'd have to read the whole repo first" — tries to read everything before answering,
       or refuses to commit to a map without exhaustive reading.
Diagnoses: Exhaustive-reading reflex; no model of strategic triage. Orienting is reading
           5-7 artifacts, not all of them. (Spinellis; the orient procedure is strategic by
           design; corollary 2.)
Example trigger: any Advanced repo under a time box — the learner asks to see every file
                 instead of the tree + entry + one test.

Error: Never opens `tests/`, or treats the tests as noise rather than as the spec.
Diagnoses: Misses that the test suite is the executable spec — the cheapest confirmation of
           what a module is FOR, and the one runnable artifact in the orient procedure.
           (Finding 6 tracing; tests-as-spec, step 4.)
Example trigger: a repo where test_models.py names the exact behavior the feature-X question
                 asks about — and the learner answers without consulting it.

Error: Locates "where to change feature X" by grepping the feature's surface string and
       stopping at the first hit (the CLI word, the UI label, the route path) instead of
       the module that owns the behavior.
Diagnoses: Confuses where a feature is NAMED/displayed/routed with where its LOGIC lives;
           stops at the first textual match rather than tracing to the owning module. (Active,
           hypothesis-driven comprehension — bind the hypothesis to the code; the trace step.)
Example trigger: the CLI "filter/sort" drill — the learner answers "cli.py" (where "list" is
                 parsed) instead of "commands.py/models.py" (where the filtering/ordering lives).

Error: Builds a map but can't rank it — treats every file as equally important; can't name
       the ONE file to open first, or picks an incidental file.
Diagnoses: Chunks formed but not RANKED — no model of the load-bearing artifact (the gateway).
           The repo-scale twin of A2's "can't say which 2 chunks matter." (A2 5c ranking
           error; step 7; the AI-era "what matters most" skill, spec §12 -> E3.)
Example trigger: "which one file would you open first, and why?" — a learner who names a
                 utility/helper, or shrugs, instead of the README/architecture doc/core model.

Error: Ignores git history, or reads high churn as "buggy / bad files to avoid."
Diagnoses: Doesn't use change-frequency as a core-finder — either ignores the signal or
           inverts it. High churn marks the HEART (active development), not a warning sign.
           (Churn beacon, step 6.)
Example trigger: a drill that supplies a "most-changed files" list — the learner doesn't use
                 it to locate the core, or calls the hot file "the one to stay away from."
```

### 5d. Grading mode

**Hybrid, mostly rubric** (`drill-generation.md` §1d, §3). E1 is a **judgment module**:
"is this a good orientation map?" is a strategy call, not a computation — there is rarely a
single string to match. The coach grades like this:

1. **Score the orientation map against the E1 rubric (§7), part by part** — *entry point ·
   core module · feature-X location · first-file-and-why*. Each is a 3-point criterion
   (absent / partial / solid; §7), graded explicitly. **Process counts:** an answer that is
   right but justified by a **folder name** rather than a **beacon / trace** is a partial
   pass (it may be a lucky name-match, not orientation).
2. **Run the one executable sub-claim where it exists** — *"what does module M do?"* When
   the repo includes a test for the module in question, the coach **collapses that module +
   its test into one runnable file** and runs it via
   `python <skill-dir>/runtime/python/runner.py snippet.py` (`drill-generation.md` §2),
   pasting the real output. This is **executable ground truth** for that sub-claim only: it
   confirms what the module is *for* (and settles any dispute about where a behavior lives —
   run it, the test decides). The coach **surfaces the snippet and output** in the message
   (`coaching-loop.md` → surface ground truth), never leaving it in a collapsed tool call.
3. **Cite the closest golden exemplar** in `exemplars/E1/<tier>.md` — "your map is close to
   the **weak** exemplar: you named `core/` by its folder name; running the test shows it's
   dead" vs. "close to the **strong** exemplar: you traced `__main__ → cli → commands →
   models` and confirmed it." The golds are the calibration anchor.
4. **Name it as soft.** The coach says out loud: "**orienting in a repo is a strategy graded
   against the module's rubric + exemplars, not a machine-verifiable answer** — the only
   hard sub-claim here is *what a module does*, which I confirmed by running its test"
   (`drill-generation.md` §3; `assessment.md` §1.2). Rubric passes are **softer evidence**
   than executable passes.

**Report the two verdicts separately.** A learner who produces a plausible map (rubric:
partial/ok) but whose claim *"module M does X"* is **refuted by running M's test**
(executable: no) is a **partial pass**, flagged exactly there — because trusting a guessed
behavior over the runnable spec is a central E1 failure (§5c, "never opens tests").

---

## 6. Frontier band

Frontier is not a fixed tier — it tracks the learner's **demonstrated ceiling** and presses
**one step** past their last comfortable success along a single parameter axis
(`drill-generation.md` §5). Escalating two steps collapses to failure; escalating none loses
the desirable-difficulty benefit.

**What "one step" means here** (per `drill-generation.md` §5):
- **Advanced** = orient in a dense / partly-lying / cross-cutting repo and rank the gateway,
  *one* such challenge at a time.
- **Frontier-N** = N increments beyond Advanced; each increment **adds exactly one**: more
  files, a notch worse-lying names, one more trace-hop for feature X, or one more cue
  removed. The learner's current Frontier-N is the highest N they have passed.

Escalation directions beyond Advanced for E1, with step counts:

1. **Size & nesting** (the canonical path): ~15 files → ~30 files → a tree of **several
   cooperating packages** where the learner must chunk **at the package level** (what each
   package is *for*) before chunking within one. Each size jump is one increment.

2. **Adversarial / lying structure** (push the discourse-violation axis): neutral names →
   one lying folder (`core/` dead) → an entry point hidden in a `console_scripts` line with
   no `__main__.py` → a *mix* where some names lie and some don't (so no blanket "ignore the
   names" rule works). Each notch is one increment; **the highest-value AI-era escalation**,
   where the learner orients in inherited / generated code whose structure may not match its
   names.

3. **Cross-cutting feature** (push the trace axis): feature X owned by one file → a two-hop
   path (route → service) → a **three-hop** path (route → service → repository/model) where
   "where to change it" is a *path with a named owner at each hop*, not one file. Each added
   hop is one increment.

4. **Stripped cues** (push cue availability): remove the README, then the tests, forcing
   orientation from **structure + git-churn alone** — the Feathers corner (no docs, no
   tests: find a seam, characterize, work outward). One increment per cue removed.

5. **Framework / polyglot conventions**: a Django/Flask/FastAPI repo whose entry points and
   "core" are **framework conventions** (`urls.py` → `views.py`, `app/__init__.py`'s
   `create_app`, `settings.py`) the learner must recognize, or a repo split across two
   languages where the Python package is one slice. One increment per unfamiliar convention.

6. **Hand off to E2 / C3.** Once *static* orientation is solid, the natural escalations are
   **E2** (now *judge* the structure you mapped — is this decomposition good, where will it
   resist change?) and **C3** (debug a failure that spans the system you just oriented in).
   E1 is the prerequisite map both build on.

Track the level as `E1: Frontier-N`. Reset condition: two consecutive failures at the same
level → drop to Advanced for one drill, then re-approach (`drill-generation.md` §5).

---

## 7. Mastery rubric

The observable per-tier bars, instantiating the rubric shape of `assessment.md` Part 2,
scored against the four parts of the orientation map. Two cross-cutting requirements apply
at every tier above Foundations: **product *and* process** (the right map *and* sound
structure-first justification — a correct entry/core named from a *folder name* rather than
a *beacon/trace* is a Foundations-level pass at best), and **unaided + durable** (a
same-session streak is provisional until a delayed re-assessment or the real-repo transfer
task confirms it; `assessment.md` Parts 3–5).

**The four scored parts** (each 3-point: absent / partial / solid):

- **P1 — Entry point.** Names where execution actually begins, justified by a beacon (the
  `__main__`/`console_scripts`/`app.py` + the README run line), not a folder guess.
- **P2 — Core module.** Names the file that owns the domain / is most depended-on, justified
  by imports or churn, not by a folder called `core/`.
- **P3 — Feature-X location.** Points to the module that owns the *behavior* (where you'd
  edit), reached by **tracing** from the entry point — not the first keyword hit.
- **P4 — First file + why.** Names the single highest-leverage first read (the gateway) and
  **ranks** it above the source files, with a reason.

| Tier | Observable bar for E1 |
|---|---|
| **Foundations** | On a small (≤ ~6-file), helpfully-named repo, correctly **names the entry point (P1) and the core module (P2), each justified by a beacon** (the README/`__main__` run line; the most-imported file) **and** correctly answers *"what does module M do?"* for a module with a test (runner-verified). Allowed *with* the worked example faded to a partial map. |
| **Working** | On an **unseen ~8–15-file** repo, produces the **full four-part map unaided** — P1–P4 — where **feature X takes one trace-hop**, and justifies each by structure/beacons rather than folder names (answers "change ordering in `models.py`/`commands.py`", not "in `cli.py`"). Confirms one *"what does M do?"* via its test where available. On **3 of 4** such unseen repos. |
| **Advanced** | On a **denser / partly-lying-structure** repo, produces the map unaided, **recovers the real entry/core when names mislead** (confirms by tracing the import-call chain or running a test — convicts the dead `core/`), **traces a cross-file feature path** naming the owner at each hop, **ranks the one gateway file** with a reason, and does not over-trust a name. Articulates the **orient procedure as a general method** on a teach-it-back ("tree → entry → tests → core → churn → gateway; behavior over names"), not just the instance. |
| **Frontier** | `Frontier-N`: presses one step past the last comfortable success per §6 / `drill-generation.md` §5 (more files → worse-lying names → more trace-hops → stripped cues → framework conventions). A moving target, not a fixed bar. |

Promotion is by **performance, not tenure** (`assessment.md` rule 1); the coach marks a tier
from what the learner *does* on unseen repos, never from claimed seniority or "I work in a
big monorepo all day." Held-out re-assessment and **real-repo transfer** outrank a
same-session streak (`assessment.md` Part 5) — and for a judgment module especially, the
real-code signal is weighted heavily (a clean synthetic-repo streak that doesn't show up
when the learner orients in their *own* unfamiliar service is not yet mastery).

---

## 8. Anti-patterns & evidence caveat

**Anti-patterns this module exists to break** (each is a catalog entry in §5c, surfaced as a
*behavior*):

- **Crawling instead of orienting.** Opening the first/biggest file and reading top-to-bottom,
  arriving with no map — the repo-scale version of narrating a function token-by-token. The
  fix is mechanical: read the **tree** and the **entry point** first; chunk at the file level.
  *Orient, don't crawl.*
- **Skipping the README and the tree.** Reconstructing from source what the project already
  documents about itself. The fix: spend the first 60 seconds on the README + directory tree —
  the cheapest, highest-information artifacts in the repo.
- **Trusting a lying folder name.** Calling `core/` the core or `main/` the entry because of
  the name, when the behavior disagrees — the repo-scale discourse violation. The fix: confirm
  the entry/core by **tracing the import-call chain or running a test**; behavior wins (A2,
  one grain up).
- **Exhaustive-reading reflex.** "I'd have to read everything first." The fix: triage —
  orienting is reading 5–7 artifacts, not all of them (Spinellis). Commit to a map from the
  high-signal reads and *refine* it, don't perfect it before committing.
- **Ignoring the tests.** Never opening `tests/`, so the cheapest confirmation of "what does
  module M do?" — and the one runnable artifact — goes unused. The fix: read the test that
  names the behavior you're asked about; run it to settle disputes.
- **Locating a feature by its surface string.** Stopping at the CLI word / route path / UI
  label instead of tracing to the module that owns the logic. The fix: trace from the entry
  point to the behavior; the name and the owner are usually one hop apart.

**Evidence caveat (this is a `[Verified]`-core + `[Practitioner-canon]`-scale module — say
so).** E1's grounding is **mixed and must not be oversold**:

- The **mechanisms** (chunking, beacons, hypothesis-driven tracing) are `[Verified]`
  (`evidence-base.md` → Findings 2/3/6) — but the evidence is from people comprehending **one
  program / one function** (1976–2008). Applying them at **file/module grain** is a
  **reasonable extension of verified findings, not a separately verified result.** The coach
  says "we're applying verified comprehension findings one grain up," never "research shows
  the orient procedure improves repo comprehension."
- The **orient procedure** (the seven-step sequence; git-churn-as-core-finder;
  gateway-artifact) is **`[Practitioner-canon]`** — Spinellis 2003, Feathers 2004, Dagenais &
  Robillard 2010, and the `orient` module (Mullarkey, in Cat Hicks' *Learning
  Opportunities*). Respected, widely-taught craft, vetted against the named sources during
  authoring — **not** a measured causal result. The coach **never** presents it as verified
  science, and cites **no effect size** for churn-as-core-finder (it is a useful heuristic,
  not a validated metric here — cite less, not more).
- The **gateway-artifact** framing is the curriculum's term; Dagenais & Robillard 2010
  establishes that developer documentation is *deliberately created to orient contributors*,
  not that "the one gateway file" is a measured construct. Flagged honestly.
- The **AI-era priority** that makes orientation a verification-cluster skill (engineers
  inherit large unfamiliar / agent-generated repos; *unaided* comprehension atrophies first —
  Anthropic RCT, ~17% lower) is `[Verified-adjacent]` — **priority-steering, not proof**; the
  productivity evidence is partly contested (`evidence-base.md` → AI-era honesty caveats).
- The **curriculum-wide transfer caveat** applies in full: that drilling orientation on
  synthetic repos *causally* improves a given engineer's real-repo onboarding is the open
  question. The coach leans on the transfer task (§9) — orienting in the learner's **own**
  unfamiliar repo — as the honest individual-level evidence.

No claim in this module is dressed above its badge.

---

## 9. Transfer task

**The only honest test of whether the gym drill transferred to the job is applying it to the
learner's own real code** (`assessment.md` Part 4; `evidence-base.md` → transfer caveat,
consequence 2).

> **Your turn:** Find a **real repository you do not already understand** — a service your
> team owns that you've never worked in, a dependency whose source you've never read, an
> open-source project you want to contribute to, or your own code from long enough ago that
> it's unfamiliar. Pick one you could plausibly need to change a feature in.
>
> Now **orient — don't crawl.** Run the procedure and produce the **four-part map**:
> **(1)** read the **README + directory tree** and chunk the repo into its major parts;
> **(2)** find the **entry point** (`main`/CLI/routes/`console_scripts`) and confirm it
> (trace the call, or run it); **(3)** open the **tests** for the area you care about and
> note what they pin; **(4)** name the **core module** (most-imported, or the churn hot-spot
> from `git log`), **where you'd change one concrete feature X** (trace from the entry point
> to the owning module — don't stop at the first keyword hit), and **the one file you'd open
> first, and why.** Then **verify one module with its test:** reduce it to a runnable
> snippet (the module + its test), predict what it asserts, and confirm with the runner.

**Grading is softer and named as such** (`assessment.md` Part 4). A real repo has no clean
answer key for the *map* — the coach grades against the §7 rubric (P1 entry / P2 core / P3
feature-X / P4 first-file) and says: *"this is a judgment call on your real repo, not a
machine-verifiable result."* Where any sub-claim **is** runnable — "what does module M do?",
or "does the entry point reach this file?" — the coach still uses the runner: **collapse the
module + its test into a snippet, run it through `runner.py`, and confirm the behavior before
the learner asserts it in the map** (the same discipline as §5d, now on the learner's real
code; and the runner **settles any "this folder is the core" dispute** — trace/run it, the
behavior decides). **Transfer evidence is weighted heavily:** a learner who aces synthetic
repos but, on their own unfamiliar service, crawls file-by-file or names `core/` by its
folder name has **not** transferred the skill, and the tracker notes that gap as more
diagnostic than another passed synthetic drill.

---

## Cross-references

- Drill mechanics, exercise formats, the **rubric + exemplars judgment path**, the executable
  test-as-spec check, Frontier escalation: `references/drill-generation.md` (this module
  instantiates §1 and follows §3, §4, §5; the test-as-spec check uses §2).
- Session delivery (pause/no-spoiler hard stop, tier-faded worked example, direct feedback,
  scaffolding ladder, surface-ground-truth): `references/coaching-loop.md`.
- E1 entry task (orient in a provided small repo: name the entry point, the core module,
  where you'd change feature X, and the one file you'd open first and why), per-skill routing,
  mastery-rubric shape, held-out re-assessment, **real-repo transfer** weighting:
  `references/assessment.md` (Part 1.4 — E1).
- Evidence grounding — the `[Verified]` mechanisms (Findings 2, 3, 6: chunking, beacons,
  tracing — **cited, not re-derived**), the `[Practitioner-canon]` orient sources (Spinellis
  2003; Dagenais & Robillard 2010; Feathers 2004; the `orient` module by Mullarkey, in Cat
  Hicks' *Learning Opportunities* — **credited**), and the worked-examples / expertise-reversal
  instructional finding: `references/evidence-base.md` (Findings 2/3/6; *Large-codebase
  comprehension (module E1)*; Attribution).
- Soft prerequisites (chunk and trace one function before a repo): modules **A2** (code
  reading & chunking), **A3** (execution tracing); related **C2** (a traceback is the entry
  into an unfamiliar repo), **A1** (notional machine). Hands off up to **E2** (architectural
  judgment) and **C3** (debugging across the mapped system).
- Golden exemplars (~3 per tier, each with the gold orientation map + rubric note, and a
  **runner-verified** test-as-spec where one exists): `exemplars/E1/foundations.md`,
  `exemplars/E1/working.md`, `exemplars/E1/advanced.md`.
