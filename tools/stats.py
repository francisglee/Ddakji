"""Scene table + lint over the repo's metadata layer.

Reads state definitions from process/workflows/ (never hardcoded —
Layering Rule). Reports, per work: scene table (pov, date, status,
turns, words) and lint findings: invalid status values, spec/draft
pairing gaps, dangling event references. Read-only.

Usage: python3 tools/stats.py
"""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import lib


def word_count(work: str, slug: str) -> int | None:
    draft = lib.draft_path(work, slug)
    if not draft.exists():
        return None
    _, body = lib.read_doc(draft)
    prose = lib.prose_of(body, lib.END_SCENE)
    return len(prose.split()) if prose else 0


def main() -> int:
    states = set(lib.load_workflow("scene-status")["states"])
    events = lib.event_slugs()
    problems: list[str] = []

    for work in lib.WORKS:
        rows = []
        for slug, fm, _ in lib.scene_docs(work):
            status = fm.get("status")
            if status not in states:
                problems.append(f"{work}/{slug}: invalid status {status!r}")
            for ev in fm.get("events") or []:
                if ev not in events:
                    problems.append(f"{work}/{slug}: dangling event ref {ev!r}")
            words = word_count(work, slug)
            if words is None and status not in (None, "sketch"):
                problems.append(f"{work}/{slug}: status {status!r} but no draft file")
            rows.append((slug, fm.get("pov") or "-", str(fm.get("date") or "-"),
                         status or "-", str(fm.get("turns") or "-"),
                         "-" if words is None else str(words)))
        # orphan drafts: prose with no spec
        specs = {slug for slug, _, _ in lib.scene_docs(work)}
        for p in (lib.ROOT / "works" / work / "drafts").glob("*.md"):
            if p.stem not in specs:
                problems.append(f"{work}/drafts/{p.stem}: draft has no scene doc")

        print(f"\n== {work} ==")
        if not rows:
            print("  (no scenes)")
            continue
        header = ("scene", "pov", "date", "status", "turns", "words")
        widths = [max(len(r[i]) for r in rows + [header]) for i in range(6)]
        for r in [header] + rows:
            print("  " + "  ".join(v.ljust(w) for v, w in zip(r, widths)))
        total = sum(int(r[5]) for r in rows if r[5].isdigit())
        print(f"  total words: {total}")

    print("\n== lint ==")
    if problems:
        for p in problems:
            print(f"  ! {p}")
        return 1
    print("  clean")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
