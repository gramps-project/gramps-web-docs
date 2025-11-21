# Gramps Web Docs Contributing Guide

Thanks for helping to improve the Gramps Web documentation! This guide will help you get started with contributing.

## Finding your way around

The documentation pages are written in Markdown and stored in the `docs/en` directory. Each page on [grampsweb.org](https://www.grampsweb.org/) corresponds to a `.md` file in this directory.

The navigation structure is defined in the `mkdocs.yml` file at the root of the repository. This file controls how the pages are organized and displayed in the sidebar.

There is a automated translation service implemented, which will translate all new/changed files in `docs/en` to the other languages.

## Making changes

To make changes to the documentation, simply change the relevant Markdown files in the `docs/en` directory and submit a pull request.

If you are proficient with git, you can clone the repository, make your changes locally, and push them to your fork. If you're not familiar with git, you can also edit files directly on Github using the web interface.

## Adding new pages

To add a new page to the documentation, create a new Markdown file in the `docs/en` directory and add it to the `mkdocs.yml` file under the appropriate section. Make sure to follow the existing structure and formatting. If you can, also add the translations for the navigation under `mkdocs.yml` .

## Adding translations

The documentation currently supports English (default), German, and French. The translations of the actual `.md files` are managed automatically using OpenAI GPT-4o-mini. The navigation (under `mkdocs.yml`) and `home.html` need to be translated manually.

### Adding a new language

To add a new language to the documentation:

1. **Update the configuration** in `translate.py` and add the Language under **LANGUAGE_NAMES**:

   ```python
   CONFIG = {
       "translation": {
           "target_languages": ["de", "fr", "es"],  # Add your language code
           ...
       }
   }

   # Language names for prompting and display
   LANGUAGE_NAMES = {
       "de": "German",
       "fr": "French",
       "es": "Spanish",
       "it": "Italian",
       "en": "English"
   }
   ```

2. **Add the language to MkDocs** in `mkdocs.yml`:

   ```yaml
   plugins:
     - i18n:
         languages:
           - locale: es
             name: Español
             build: true
             nav_translations:
               Home: Inicio
               Features: Características
               # ... add all navigation translations
   ```

3. **Add homepage translations** in `overrides/translations/home.yml`:

   ```yaml
   hero:
     es:
       title: "Gramps Web"
       description: "..."
       demo_button: "..."
   learn_more:
     es:
       title: "..."
       # ... add all homepage translations
   ```

4. **Run the translation**:

   ```bash
   python translate.py --lang es
   ```

### Translating content

All English source files are in `docs/en/`. When you modify an English file, translations are automatically generated via GitHub Actions. For manual translation:

```bash
# Set up your OpenAI API key
cp .env.example .env
# Add your API key to .env

# Translate specific file
python translate.py --file user-guide/blog.md --lang de

# Translate all files
python translate.py --lang all
```

## Previewing changes

If you are just editing or adding Markdown to a page, there may not be a need to preview your changes. However, if you are making significant changes or adding new pages, you can preview your changes locally by following these steps:

1. Install the necessary dependencies:

```bash
python -m pip install -r requirements.txt
```

2. Run the MkDocs development server:

```bash
python -m mkdocs serve -a localhost:8211
```

3. Open your web browser and go to [http://localhost:8211](http://localhost:8211) to see your changes live. The web server will automatically reload when you make changes to the Markdown files.
