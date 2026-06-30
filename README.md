# Étude

A deliberate-practice coaching system for working developers — packaged as a Claude Code skill — that helps you get *measurably* better at the skills the research says actually separate experts from novices: the notional machine, code reading, execution tracing, debugging, testing, code review, and metacognition.

It is a **gym, not a code generator**. It assesses your current skill per topic, generates **fresh practice drills** each session, grades your attempts against **executable ground truth** (it runs the code rather than guessing the output), gives blunt and specific feedback about the gap, and tracks within-person progress over time.

Its defining commitment is **evidence honesty**: every claim is traceable to its source and openly labeled as verified science, practitioner canon, or extrapolation. It never presents folklore as fact — the "two humps" aptitude myth and the strong "10,000-hour" thesis are rejected outright, with citations.

## What's here

```
etude/        # the skill itself
  SKILL.md                  #   the coach: routing, coaching loop, module index
  modules/                  #   20 teaching modules across 6 tracks (A1–F3)
  exemplars/                #   ~3 golden drills per module per tier (few-shot + offline fallback)
  references/               #   evidence-base, coaching-loop, drill-generation, assessment, authoring guide
  runtime/python/runner.py  #   sandboxed runner for executable ground truth (Python, v1)
  progress-template.md      #   per-learner mastery tracker

docs/superpowers/           # build trail: design spec, plans, smoke tests
tests/                      # pytest suite for the runner + module validator
tools/validate_modules.py   # structural validator for module files
pyproject.toml
```

### The 20 modules

A sampleable **buffet** — tracks suggest a recommended order but gate nothing. Each module is tier-badged by the strength of its evidence.

| Track | Modules | Evidence |
|---|---|---|
| **A — Comprehension** | A1 notional machine · A2 code reading & chunking · A3 execution tracing · A4 concurrency models | `[Verified]` core |
| **B — Construction** | B1 decomposition & planning · B2 code writing · B3 testing & correctness | `[Verified-adjacent]` / canon |
| **C — Debugging** | C1 systematic debugging · C2 stack traces & errors · C3 production & concurrency debugging | verified model + canon method |
| **D — Quality & craft** | D1 managing complexity · D2 naming · D3 refactoring judgment · D4 performance & mechanical sympathy | `[Practitioner-canon]` |
| **E — Scale & staff** | E1 large-codebase comprehension · E2 architectural judgment · E3 code review | mixed / canon |
| **F — Meta & learning** | F1 metacognition & calibration · F2 designing your practice · F3 learning new languages fast | `[Verified-adjacent]` |

Badge meanings: `[Verified]` confirmed in the fact-checked research pass · `[Verified-adjacent]` extends a verified finding or rests on well-established general learning science, thin programming-specific evidence · `[Practitioner-canon]` respected practice, not empirically established. The full grounding — findings, sources, the explicitly-refuted list, and badge definitions — lives in `etude/references/evidence-base.md`.

## Two ways to use it

**As a curriculum (just read it).** The `modules/*.md` files are self-contained teaching units. Read any one directly.

**As a coach (run the skill).** Install it into Claude Code, then ask Claude to coach you. The coach assesses you, routes you to a tier, generates drills, and grades them.

### Install as a Claude Code skill

Symlink (or copy) the skill directory into your skills folder:

```sh
ln -s "$PWD/etude" ~/.claude/skills/etude
```

Then in a Claude Code session, invoke the `etude` skill (or just ask to "coach me on execution tracing"). The coach looks for `etude-progress.md` in your working directory and creates one from `progress-template.md` if it's absent.

> The coach resolves `runtime/python/runner.py` relative to **the skill's own directory**, so executable grading works the same whether the skill is installed under `~/.claude/skills/` or run from a repo checkout.

## Development

```sh
pytest                          # run the test suite
python tools/validate_modules.py   # validate module file structure
```

Requires Python ≥ 3.11. Adding a module is a documented, repeatable operation — see `etude/references/authoring-new-modules.md`.

## Status & honest caveats

- **All 20 modules are authored** and structurally validated. Grading is executable for verifiable drills (A1–A3, tracing, etc.) and rubric+exemplar based for judgment skills (B3, D1–D3, E2, F1) — the latter is inherently softer, and the coach surfaces that uncertainty.
- This measures **within-person progress** on defined skills against your own baseline. It is **not** a certified expertise grade — no validated absolute measure of programming expertise exists.
- Nearly all the *verified* evidence comes from studies of **novices** in intro courses, mostly **1976–1995**. Whether teaching these skills causally improves experienced developers is an **open question** — so measurement is built in, every module ends with a transfer task on your real code, and depth beyond the evidence is labeled as extrapolation.
- The Python runtime is v1 only. Non-Python runtimes, a spaced-repetition scheduler, and an empirical transfer-validation study are out of scope for now.

## Credits

The learning-science delivery disciplines (pause/no-spoiler, pre-testing, fading scaffolding, desirable difficulty), the affective self-report measures, and the `orient` codebase-orientation procedure are adapted from **Cat Hicks'** *Learning Opportunities* skill and **Michael Mullarkey's** *orient* companion ([github.com/DrCatHicks/learning-opportunities](https://github.com/DrCatHicks/learning-opportunities)). Their principles are CC-BY-4.0; their survey measures are CC-BY-SA-4.0. See `docs/superpowers/specs/` §13 for the full attribution table.
