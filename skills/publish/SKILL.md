---
name: publish
description: Export a work or the blog to publish/ through the publish checklist. Usage - /publish <work|blog>
---

# /publish — the single aperture

Procedure (checklist source of truth:
`process/workflows/publish-pipeline.toml` — walk every `[[check]]` in
order; any failure stops the run and is reported honestly):

1. Identify candidates: scene docs (or blog posts) with
   `publish: true`.
2. Run the checks: status locked · serial buffer (N+2 drafted) ·
   no unverified load-bearing facts · interview consent
   (`quotable: yes`) · asset licenses (no reference-only) · blog
   excerpt rule · outstanding coverage addressed or explicitly waived.
3. Run `python3 tools/export.py <target>`. The exporter is
   whitelist-only and stamps copyright; never hand-edit its output.
4. Show the author the `git diff` of `publish/` and WAIT for approval —
   publishing is irreversible in rights terms.
5. On approval, commit as `works: publish <target> ...` (publish/ is a
   generated path, not a prose path).
6. If content was already public and changed: this is errata — the
   change must be visible (errata note), never silent.
7. Remind the author if the release is unversioned: `/release` pairs
   with publishing milestones.
