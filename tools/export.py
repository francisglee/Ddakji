"""Export publishable content to publish/ — the single aperture.

Whitelist-only and fail-closed (process/roles/automation.md axiom 1):
only explicitly public frontmatter fields and prose above the END marker
ever leave; anything missing, unmarked, or unlocked is skipped with a
report line, never guessed at. Checklist gating (consent, buffer, facts)
is the /publish skill's job — this script is the mechanical last step.

Usage: python3 tools/export.py <baek-il|ddakji|blog>
"""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import lib

COPYRIGHT = "© 2026 Francis Lee. All rights reserved."
WORK_WHITELIST = ("title", "pov")  # scene-doc fields allowed to publish
BLOG_WHITELIST = ("title", "date", "tags")


def export_work(work: str) -> int:
    outdir = lib.ROOT / "works" / work / "publish"
    outdir.mkdir(exist_ok=True)
    n = 0
    for slug, fm, _ in lib.scene_docs(work):
        if fm.get("publish") is not True:
            continue
        if fm.get("status") != "locked":
            print(f"SKIP {slug}: publish:true but status is {fm.get('status')!r}, not locked")
            continue
        draft = lib.draft_path(work, slug)
        if not draft.exists():
            print(f"SKIP {slug}: no draft file")
            continue
        _, body = lib.read_doc(draft)
        prose = lib.prose_of(body, lib.END_SCENE)
        if prose is None:
            print(f"SKIP {slug}: draft has no END SCENE marker (fail closed)")
            continue
        header = "\n".join(
            f"{k}: {fm[k]}" for k in WORK_WHITELIST if fm.get(k) not in (None, "")
        )
        out = f"---\n{header}\n---\n\n{prose}\n\n---\n{COPYRIGHT}\n"
        (outdir / f"{slug}.md").write_text(out, encoding="utf-8")
        print(f"exported {work}/{slug}")
        n += 1
    return n


def export_blog() -> int:
    outdir = lib.ROOT / "blog" / "publish"
    outdir.mkdir(exist_ok=True)
    n = 0
    for p in sorted((lib.ROOT / "blog" / "drafts").glob("*.md")):
        fm, body = lib.read_doc(p)
        if fm.get("publish") is not True:
            continue
        prose = lib.prose_of(body, lib.END_POST)
        if prose is None:
            print(f"SKIP {p.stem}: no END POST marker (fail closed)")
            continue
        header = "\n".join(
            f"{k}: {fm[k]}" for k in BLOG_WHITELIST if fm.get(k) not in (None, "")
        )
        out = f"---\n{header}\n---\n\n{prose}\n\n---\n{COPYRIGHT}\n"
        (outdir / f"{p.stem}.md").write_text(out, encoding="utf-8")
        print(f"exported blog/{p.stem}")
        n += 1
    return n


def main() -> int:
    if len(sys.argv) != 2 or sys.argv[1] not in (*lib.WORKS, "blog"):
        print(__doc__)
        return 2
    target = sys.argv[1]
    n = export_blog() if target == "blog" else export_work(target)
    print(f"{n} item(s) exported. Review the git diff of publish/ before committing.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
