"""Shared parsing for the Ddakji pipeline. Stdlib only — keep it that way.

The one definition of how repo files parse. Frontmatter here is a
deliberately small YAML subset (scalars, inline lists, one nesting
level) — enough for our templates, simple enough to trust at a privacy
boundary. Anything fancier belongs in the template design discussion,
not in this parser.
"""
from __future__ import annotations

import tomllib
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
WORKS = ("baek-il", "ddakji")
END_SCENE = "<!-- END SCENE -->"
END_POST = "<!-- END POST -->"


def _coerce(value: str):
    value = value.strip()
    if value == "":
        return None
    if value.startswith("[") and value.endswith("]"):
        inner = value[1:-1].strip()
        return [v.strip().strip("'\"") for v in inner.split(",") if v.strip()]
    if value in ("true", "yes"):
        return True
    if value in ("false", "no"):
        return False
    return value.strip("'\"")


def parse_frontmatter(text: str) -> tuple[dict, str]:
    """Return (frontmatter, body). Missing/malformed frontmatter -> ({}, text)."""
    if not text.startswith("---"):
        return {}, text
    lines = text.split("\n")
    fm: dict = {}
    stack_key = None
    body_start = None
    for i, line in enumerate(lines[1:], start=1):
        if line.strip() == "---":
            body_start = i + 1
            break
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        indent = len(line) - len(line.lstrip())
        stripped = line.strip()
        if stripped.startswith("- ") and stack_key:
            fm.setdefault(stack_key, [])
            if isinstance(fm[stack_key], list):
                fm[stack_key].append(_coerce(stripped[2:]))
            continue
        if ":" not in stripped:
            continue
        key, _, raw = stripped.partition(":")
        key = key.strip()
        if indent == 0:
            if raw.strip() == "":
                fm[key] = {}
                stack_key = key
            else:
                fm[key] = _coerce(raw)
                stack_key = key if fm[key] is None else None
                if fm[key] is None:
                    fm[key] = None
        else:
            if stack_key is not None and isinstance(fm.get(stack_key), dict):
                fm[stack_key][key] = _coerce(raw)
    body = "\n".join(lines[body_start:]) if body_start else ""
    return fm, body


def read_doc(path: Path) -> tuple[dict, str]:
    return parse_frontmatter(path.read_text(encoding="utf-8"))


def prose_of(body: str, marker: str) -> str | None:
    """Publishable prose above the END marker; None if the marker is absent
    (fail closed: no marker, nothing publishes)."""
    if marker not in body:
        return None
    return body.split(marker)[0].strip()


def load_workflow(name: str) -> dict:
    with open(ROOT / "process" / "workflows" / f"{name}.toml", "rb") as f:
        return tomllib.load(f)


def scene_docs(work: str):
    d = ROOT / "works" / work / "scenes"
    for p in sorted(d.glob("*.md")):
        fm, body = read_doc(p)
        if fm.get("type") == "scene-doc":
            yield p.stem, fm, body


def draft_path(work: str, slug: str) -> Path:
    return ROOT / "works" / work / "drafts" / f"{slug}.md"


def event_slugs() -> set[str]:
    return {p.stem for p in (ROOT / "world" / "events").glob("*.md")}
