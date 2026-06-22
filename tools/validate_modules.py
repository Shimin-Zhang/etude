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
