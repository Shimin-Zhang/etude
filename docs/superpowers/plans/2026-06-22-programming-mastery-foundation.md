# Programming Mastery — Foundation (Plan 1) Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build the tested code foundation for the `programming-mastery` coaching skill — a sandboxed Python runner (for executable drill ground-truth) and a module-anatomy validator — plus an installable skill skeleton.

**Architecture:** Most of the skill is authored markdown (instructions the coach follows). Plan 1 builds only the two genuine *code* components — `runtime/python/runner.py` (executes code drills under timeout + resource limits) and `tools/validate_modules.py` (lints module files against the spec's fixed anatomy) — both via TDD, plus a minimal real `SKILL.md` and `progress-template.md`. Content (evidence base, coaching loop, drill generation, and the modules themselves) lands in later plans.

**Tech Stack:** Python 3.11+, pytest, standard library only (`subprocess`, `resource`, `tempfile`, `re`, `dataclasses`).

**Spec:** `docs/superpowers/specs/2026-06-22-programming-mastery-skill-design.md`

---

## Plan roadmap (this is Plan 1 of a sequence)

1. **Foundation (this plan)** — sandbox runner + module validator + skill skeleton. *Tested code.*
2. **Engine content** — `references/evidence-base.md`, `coaching-loop.md`, `drill-generation.md`, `assessment.md`; expand `SKILL.md`. *Authored; acceptance = validator + smoke session.*
3. **Module A1 (notional machine) end-to-end** — teaching content + generation spec + golden exemplars + executable grading + Frontier band. *The reference module; acceptance = full coached smoke session with live execution.*
4. **Remaining modules by track** — A2–A4, B1–B3, C1–C3, D1–D4, E1–E3, F1–F3, each following the A1 template; then extract `references/authoring-new-modules.md`.

Plans 2–4 are authoring-heavy (prose + exemplars), so they are scoped and written after Plan 1's pattern is proven in code.

## File structure (Plan 1)

- Create: `pyproject.toml` — project + pytest config (`pythonpath`, `testpaths`).
- Create: `.gitignore` — Python caches.
- Create: `programming-mastery/runtime/python/runner.py` — sandboxed snippet executor + CLI.
- Create: `programming-mastery/SKILL.md` — installable skill entry point (lean but real).
- Create: `programming-mastery/progress-template.md` — per-learner tracker template.
- Create: `programming-mastery/references/.gitkeep`, `programming-mastery/modules/.gitkeep`, `programming-mastery/exemplars/.gitkeep` — scaffold for later plans.
- Create: `tools/validate_modules.py` — module-anatomy linter + CLI.
- Create: `tests/test_runner.py`, `tests/test_validate_modules.py` — pytest suites.

---

### Task 0: Project scaffold & tooling

**Files:**
- Create: `pyproject.toml`
- Create: `.gitignore`
- Create: directory tree under `programming-mastery/` and `tools/`, `tests/`

- [ ] **Step 1: Create the directory tree**

```bash
mkdir -p programming-mastery/runtime/python \
         programming-mastery/references \
         programming-mastery/modules \
         programming-mastery/exemplars \
         tools tests
touch programming-mastery/references/.gitkeep \
      programming-mastery/modules/.gitkeep \
      programming-mastery/exemplars/.gitkeep
```

- [ ] **Step 2: Write `pyproject.toml`**

```toml
[project]
name = "programming-mastery"
version = "0.1.0"
description = "Evidence-based programming-skills coaching skill"
requires-python = ">=3.11"

[tool.pytest.ini_options]
pythonpath = ["programming-mastery/runtime/python", "tools"]
testpaths = ["tests"]
addopts = "-q"
```

- [ ] **Step 3: Write `.gitignore`**

```gitignore
__pycache__/
*.py[cod]
.pytest_cache/
.venv/
*.egg-info/
```

- [ ] **Step 4: Install pytest**

Run: `python -m pip install pytest`
Expected: pytest installs successfully (or "Requirement already satisfied").

- [ ] **Step 5: Verify pytest collects nothing yet (no error)**

Run: `python -m pytest`
Expected: `no tests ran` (exit code 5 is fine — collection works, suite is empty).

- [ ] **Step 6: Commit**

```bash
git add pyproject.toml .gitignore programming-mastery tools tests
git commit -m "chore: scaffold programming-mastery project + pytest config"
```

---

### Task 1: Sandboxed Python runner (executable ground truth)

**Files:**
- Create: `programming-mastery/runtime/python/runner.py`
- Test: `tests/test_runner.py`

- [ ] **Step 1: Write the failing tests**

```python
# tests/test_runner.py
import json
import sys

import pytest

from runner import run_snippet


def test_normal_output_is_ok():
    r = run_snippet("print(2 + 2)")
    assert r.status == "ok"
    assert r.stdout.strip() == "4"
    assert r.returncode == 0


def test_runtime_error_is_captured_not_raised():
    r = run_snippet("raise ValueError('boom')")
    assert r.status == "error"
    assert "ValueError" in r.stderr
    assert "boom" in r.stderr
    assert r.returncode != 0


def test_timeout_on_infinite_loop():
    r = run_snippet("while True:\n    pass\n", timeout_s=1.0)
    assert r.status == "timeout"
    assert r.returncode is None


def test_stdout_and_stderr_are_separated():
    r = run_snippet("import sys\nprint('out')\nprint('err', file=sys.stderr)\n")
    assert "out" in r.stdout and "err" not in r.stdout
    assert "err" in r.stderr


def test_to_json_roundtrips_fields():
    r = run_snippet("print('hi')")
    data = json.loads(r.to_json())
    assert data["status"] == "ok"
    assert "hi" in data["stdout"]


@pytest.mark.skipif(sys.platform == "win32", reason="resource limits are Unix-only")
def test_memory_limit_triggers_error():
    # ~1 GiB allocation under a 128 MB cap should fail (MemoryError / nonzero exit).
    r = run_snippet("x = bytearray(1024 * 1024 * 1024)\n", mem_mb=128, timeout_s=5.0)
    assert r.status == "error"
```

- [ ] **Step 2: Run tests to verify they fail**

Run: `python -m pytest tests/test_runner.py`
Expected: FAIL — `ModuleNotFoundError: No module named 'runner'`.

- [ ] **Step 3: Implement `runner.py`**

```python
# programming-mastery/runtime/python/runner.py
"""Sandboxed execution of Python snippets for drill ground-truth.

v1 threat model: this runs coach-generated drill snippets and the learner's own
practice code. It is a ROBUSTNESS sandbox (timeout + address-space/CPU limits to
stop runaway loops and memory blowups), NOT a security boundary against
deliberately hostile code. Container-level isolation is future work (spec §10
risk #2).
"""
from __future__ import annotations

import dataclasses
import json
import subprocess
import sys
import tempfile
import time
from pathlib import Path

try:
    import resource  # Unix-only
except ImportError:  # pragma: no cover - non-Unix fallback
    resource = None


@dataclasses.dataclass
class RunResult:
    status: str           # "ok" | "timeout" | "error"
    stdout: str
    stderr: str
    returncode: int | None
    duration_s: float

    def to_json(self) -> str:
        return json.dumps(dataclasses.asdict(self))


def _limit_resources(mem_mb: int, cpu_s: int) -> None:
    """preexec_fn run in the child before exec: cap memory and CPU (Unix)."""
    if resource is None:  # pragma: no cover
        return
    mem_bytes = mem_mb * 1024 * 1024
    resource.setrlimit(resource.RLIMIT_AS, (mem_bytes, mem_bytes))
    resource.setrlimit(resource.RLIMIT_CPU, (cpu_s, cpu_s))


def run_snippet(code: str, *, timeout_s: float = 5.0, mem_mb: int = 256) -> RunResult:
    """Execute `code` as an isolated Python process and capture its output.

    Ordinary errors in `code` surface as status="error" (never raised); only
    harness misuse raises.
    """
    with tempfile.TemporaryDirectory() as tmp:
        script = Path(tmp) / "snippet.py"
        script.write_text(code)
        preexec = None
        if resource is not None:
            cpu_s = max(1, int(timeout_s) + 1)
            preexec = lambda: _limit_resources(mem_mb, cpu_s)
        start = time.monotonic()
        try:
            proc = subprocess.run(
                [sys.executable, "-I", str(script)],
                capture_output=True,
                text=True,
                timeout=timeout_s,
                cwd=tmp,
                preexec_fn=preexec,
            )
        except subprocess.TimeoutExpired as exc:
            return RunResult(
                "timeout",
                exc.stdout or "",
                exc.stderr or "",
                None,
                time.monotonic() - start,
            )
        return RunResult(
            "ok" if proc.returncode == 0 else "error",
            proc.stdout,
            proc.stderr,
            proc.returncode,
            time.monotonic() - start,
        )


def main(argv: list[str]) -> int:
    """CLI: `python runner.py <script.py>` prints a RunResult as JSON."""
    if len(argv) != 2:
        print("usage: runner.py <script.py>", file=sys.stderr)
        return 2
    code = Path(argv[1]).read_text()
    print(run_snippet(code).to_json())
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
```

- [ ] **Step 4: Run tests to verify they pass**

Run: `python -m pytest tests/test_runner.py`
Expected: PASS (6 passed; the memory test may be skipped on non-Unix).

- [ ] **Step 5: Smoke-test the CLI**

```bash
printf 'print(6 * 7)\n' > /tmp/snippet.py
python programming-mastery/runtime/python/runner.py /tmp/snippet.py
```
Expected: JSON like `{"status": "ok", "stdout": "42\n", "stderr": "", "returncode": 0, "duration_s": ...}`.

- [ ] **Step 6: Commit**

```bash
git add programming-mastery/runtime/python/runner.py tests/test_runner.py
git commit -m "feat: sandboxed python runner for executable drill ground-truth"
```

---

### Task 2: Module-anatomy validator

**Files:**
- Create: `tools/validate_modules.py`
- Test: `tests/test_validate_modules.py`

- [ ] **Step 1: Write the failing tests**

```python
# tests/test_validate_modules.py
import textwrap
from pathlib import Path

from validate_modules import validate_module

VALID = textwrap.dedent("""\
    # A1 — Notional Machine

    ## Evidence basis
    [Verified] Sorva 2013 (ACM TOCE); du Boulay 1986.

    ## Soft prerequisites
    None — this is a foundational module.

    ## The mental model
    A program is a machine with state; execution is deterministic state transitions.

    ## Worked example
    A traced state table for a small function.

    ## Drill-generation spec
    Tier definitions, parameter space, common-error catalog. Grading mode: executable ground truth.

    ## Frontier band
    Escalate to recursion, async, language-specific gotchas.

    ## Mastery rubric
    Predict final state + output on 4/5 unseen drills incl. one aliasing case.

    ## Anti-patterns & evidence caveat
    Reading for intent instead of simulating.

    ## Transfer task
    Trace a function from your own codebase that once surprised you.
    """)


def _write(tmp_path: Path, name: str = "A1-notional-machine.md", body: str = VALID) -> Path:
    p = tmp_path / name
    p.write_text(body)
    return p


def test_valid_module_has_no_problems(tmp_path):
    assert validate_module(_write(tmp_path)) == []


def test_missing_required_section_is_flagged(tmp_path):
    body = VALID.replace(
        "## Transfer task\nTrace a function from your own codebase that once surprised you.\n",
        "",
    )
    problems = validate_module(_write(tmp_path, body=body))
    assert any("transfer task" in p.message for p in problems)


def test_bad_filename_is_flagged(tmp_path):
    problems = validate_module(_write(tmp_path, name="notional-machine.md"))
    assert any("filename" in p.message for p in problems)


def test_missing_tier_badge_is_flagged(tmp_path):
    body = VALID.replace("[Verified] Sorva 2013 (ACM TOCE); du Boulay 1986.", "Sorva 2013.")
    problems = validate_module(_write(tmp_path, body=body))
    assert any("badge" in p.message for p in problems)


def test_missing_title_is_flagged(tmp_path):
    body = VALID.replace("# A1 — Notional Machine\n", "")
    problems = validate_module(_write(tmp_path, body=body))
    assert any("title" in p.message for p in problems)
```

- [ ] **Step 2: Run tests to verify they fail**

Run: `python -m pytest tests/test_validate_modules.py`
Expected: FAIL — `ModuleNotFoundError: No module named 'validate_modules'`.

- [ ] **Step 3: Implement `validate_modules.py`**

```python
# tools/validate_modules.py
"""Validate that programming-mastery module files follow the required anatomy.

Usage:
    python tools/validate_modules.py programming-mastery/modules/

Exit 0 if all module files are valid; 1 if any problems (printed to stderr).
"""
from __future__ import annotations

import dataclasses
import re
import sys
from pathlib import Path

REQUIRED_SECTIONS = [
    "evidence basis",
    "soft prerequisites",
    "mental model",
    "worked example",
    "drill-generation spec",
    "frontier band",
    "mastery rubric",
    "anti-patterns",
    "transfer task",
]
VALID_BADGES = ["[Verified]", "[Verified-adjacent]", "[Practitioner-canon]"]
FILENAME_RE = re.compile(r"^[A-F][1-9][0-9]?-[a-z0-9-]+\.md$")
HEADING_RE = re.compile(r"^#{1,6}\s+(.*)$", re.MULTILINE)


@dataclasses.dataclass
class Problem:
    path: str
    message: str


def _headings(text: str) -> list[str]:
    return [m.group(1).strip().lower() for m in HEADING_RE.finditer(text)]


def validate_module(path: Path) -> list[Problem]:
    problems: list[Problem] = []
    if not FILENAME_RE.match(path.name):
        problems.append(Problem(
            str(path),
            f"filename '{path.name}' must match <TrackID>-<kebab>.md "
            "(e.g. A1-notional-machine.md)",
        ))
    text = path.read_text()
    if not text.lstrip().startswith("# "):
        problems.append(Problem(str(path), "missing a top-level '# ' title"))
    headings = "\n".join(_headings(text))
    for section in REQUIRED_SECTIONS:
        if section not in headings:
            problems.append(Problem(str(path), f"missing required section: '{section}'"))
    if not any(badge in text for badge in VALID_BADGES):
        problems.append(Problem(
            str(path),
            f"missing an evidence tier badge (one of {', '.join(VALID_BADGES)})",
        ))
    return problems


def validate_dir(modules_dir: Path) -> list[Problem]:
    problems: list[Problem] = []
    for f in sorted(modules_dir.glob("*.md")):
        problems.extend(validate_module(f))
    return problems


def main(argv: list[str]) -> int:
    if len(argv) != 2:
        print("usage: validate_modules.py <modules_dir>", file=sys.stderr)
        return 2
    modules_dir = Path(argv[1])
    if not modules_dir.is_dir():
        print(f"not a directory: {modules_dir}", file=sys.stderr)
        return 2
    problems = validate_dir(modules_dir)
    for p in problems:
        print(f"{p.path}: {p.message}", file=sys.stderr)
    count = len(list(modules_dir.glob("*.md")))
    if problems:
        print(f"{len(problems)} problem(s) across {count} module file(s)", file=sys.stderr)
        return 1
    print(f"ok: {count} module file(s) valid")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
```

- [ ] **Step 4: Run tests to verify they pass**

Run: `python -m pytest tests/test_validate_modules.py`
Expected: PASS (5 passed).

- [ ] **Step 5: Smoke-test the CLI against the (empty) modules dir**

Run: `python tools/validate_modules.py programming-mastery/modules/`
Expected: `ok: 0 module file(s) valid` (exit 0 — no modules yet, no problems).

- [ ] **Step 6: Commit**

```bash
git add tools/validate_modules.py tests/test_validate_modules.py
git commit -m "feat: module-anatomy validator enforcing the spec module model"
```

---

### Task 3: Installable skill skeleton

**Files:**
- Create: `programming-mastery/SKILL.md`
- Create: `programming-mastery/progress-template.md`

- [ ] **Step 1: Write `SKILL.md`**

```markdown
---
name: programming-mastery
description: Coach a developer to measurably improve specific programming skills — the notional machine, code reading, execution tracing, debugging, testing, code review, calibration, and more — through performance assessment, freshly generated practice drills graded against executable ground truth, and specific feedback. Use when a developer wants deliberate, evidence-based practice to get better at programming; not for writing production code on their behalf.
---

# Programming Mastery — Coach

You coach a developer to get measurably better at programming. You assess them,
route to the right skill and tier, generate fresh drills, grade attempts against
ground truth, give specific feedback, and track progress. The curriculum is a
sampleable buffet of skill modules; load only the one in play.

## Running a session (skeleton)
1. Find or create the learner's tracker by copying `progress-template.md` to
   `programming-mastery-progress.md` in their working directory.
2. Pick the skill + tier the learner wants (or recommend one).
3. Load the module from `modules/<ID>-*.md` and follow its drill-generation spec
   to produce ONE fresh drill at the learner's tier.
4. The learner attempts it. Grade it:
   - Executable drills: obtain ground truth by RUNNING code via
     `runtime/python/runner.py` (`python runtime/python/runner.py snippet.py`).
     Never guess the answer.
   - Judgment drills: grade against the module's rubric + exemplars.
5. Give targeted feedback naming the specific gap; update the tracker.

Deeper protocol (coaching loop, assessment, drill generation, evidence base)
lives in `references/` and is filled in as the curriculum is built. Modules live
in `modules/`; their golden exemplars in `exemplars/<ID>/<tier>/`.

## Honesty rules
- Never present `[Practitioner-canon]` claims as verified science; respect each
  module's evidence badge.
- Grade executable drills by running code, not by predicting output.
- This measures within-person progress on defined skills — not a certified
  expertise grade.
```

- [ ] **Step 2: Write `progress-template.md`**

```markdown
# Programming Mastery — Progress Tracker

Within-person progress on defined skills. Not a certified expertise grade.

| Module | Tier | Frontier | Baseline (date / score) | Drills passed | Recurring errors | Last reviewed |
|---|---|---|---|---|---|---|
| _e.g. A1 Notional machine_ | Working | — | 2026-06-22: 2/5 | 7/9 | closure capture; aliasing | 2026-06-29 |
```

- [ ] **Step 3: Verify the full suite is green and CLIs work**

Run: `python -m pytest`
Expected: PASS (all tests; memory test may show as skipped on non-Unix).

Run: `python tools/validate_modules.py programming-mastery/modules/`
Expected: `ok: 0 module file(s) valid`.

- [ ] **Step 4: Verify the skill is structurally installable**

Run: `test -f programming-mastery/SKILL.md && head -3 programming-mastery/SKILL.md`
Expected: prints the YAML frontmatter opening (`---`, `name: programming-mastery`, ...).

- [ ] **Step 5: Commit**

```bash
git add programming-mastery/SKILL.md programming-mastery/progress-template.md
git commit -m "feat: installable programming-mastery skill skeleton + progress tracker"
```

---

## Self-review

**1. Spec coverage (Plan 1 scope):** Plan 1 implements spec build-order step 3 (Python runtime + progress-template), the validator that enforces the spec §5 module model, and a real `SKILL.md` (spec §4 entry point). Spec §2 evidence base, §7 coaching loop, §5 drill-generation content, §8 assessment, and all 20 modules are **intentionally deferred** to Plans 2–4 (see roadmap). No in-scope requirement is unaddressed.

**2. Placeholder scan:** No `TODO`/`TBD`/"implement later" in code or steps; every code step contains complete, runnable content. The `.gitkeep` files and "filled in as the curriculum is built" note in `SKILL.md` are scaffold/forward-references, not placeholders for Plan 1 work.

**3. Type consistency:** `run_snippet(code, *, timeout_s, mem_mb) -> RunResult`; `RunResult` fields (`status`, `stdout`, `stderr`, `returncode`, `duration_s`, `.to_json()`) are used identically in `tests/test_runner.py` and the CLI. `validate_module(path) -> list[Problem]`; `Problem(path, message)` fields used identically in tests and `validate_dir`/`main`. CLI entry points both return `int` and are wrapped in `SystemExit`. Heading/section names in the validator's `REQUIRED_SECTIONS` match the section titles used in the `VALID` test fixture and the spec §5 anatomy.

_No issues found on review._
