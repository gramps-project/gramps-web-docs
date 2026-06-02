# AGENTS.md

Guidance for AI coding agents (and a quick orientation for new human contributors)
working in this repository. See [CONTRIBUTING.md](CONTRIBUTING.md) for the full contributor guide.

## What this repository is

This is the **source for the [Gramps Web documentation site](https://www.grampsweb.org/)** — a
[MkDocs](https://www.mkdocs.org/) ([Material](https://squidfunk.github.io/mkdocs-material/)) site.
It contains **documentation only**. The application code lives elsewhere; report code issues there,
not here:

- Backend (Python): <https://github.com/gramps-project/gramps-web-api>
- Frontend (JavaScript): <https://github.com/gramps-project/gramps-web>

## Setup and local preview

```bash
python -m pip install -r requirements.txt   # ideally in a virtualenv
mkdocs serve -a localhost:8211 -o           # live-reloading preview
```

For a faster English-only preview you can use the dev config: `mkdocs serve -f mkdocs.dev.yml`.

## The one rule that matters most: edit English only

- **`docs/en/` is the single source of truth.** Every page on grampsweb.org is a Markdown file here.
- The other language folders (`docs/de/`, `docs/fr/`, `docs/es/`, …) are **machine-translated from
  `docs/en/`** by `translate.py` (OpenAI GPT-4o-mini), run by maintainers. **Do not hand-edit the
  translated files** — your changes will be overwritten, and editing them creates drift. Only ever
  add or change content under `docs/en/`.

## Adding or editing a page

1. Create/edit the Markdown file under `docs/en/<section>/<page>.md`.
2. Register it in the **navigation** in `mkdocs.yml`, under the appropriate section, matching the
   surrounding indentation and ordering. (If you can, also add the nav label translations in
   `mkdocs.yml` — the nav and `home.html` are translated manually, the page bodies automatically.)
3. Preview with `mkdocs serve` and confirm the page renders and the nav link works.

## Style conventions

- Plain Markdown with MkDocs-Material features: admonitions (`!!! note`), fenced code blocks with
  language hints, and tables. Match the tone and structure of existing pages.
- Use relative links between docs pages. Keep line length reasonable; one sentence per line is fine.
- Don't add marketing copy, tracking, or invented contact details.

## Things not to touch

- The **`gh-pages`** branch is generated output — never edit it by hand.
- Translated language folders other than `docs/en/` (see above).
- `translate.py` runs require an `OPENAI_API_KEY`; translation is a maintainer step, not part of a
  normal docs PR.

## Pull requests

Keep PRs small and focused (one topic per PR). Don't commit build output or local artifacts. Follow
[CONTRIBUTING.md](CONTRIBUTING.md). Commit messages should describe the documentation change.
