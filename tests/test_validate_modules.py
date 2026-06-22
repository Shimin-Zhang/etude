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
