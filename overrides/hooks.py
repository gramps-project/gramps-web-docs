"""
MkDocs hooks to load translation files and inject them into Jinja2 templates.
This makes translations more maintainable by separating them from template code.
"""

import yaml
import re
import logging
from pathlib import Path

log = logging.getLogger(f"mkdocs.plugins.hooks")


def load_translations(translation_file):
    """Load translations from YAML file."""
    file_path = Path(__file__).parent / translation_file
    with open(file_path, 'r', encoding='utf-8') as f:
        return yaml.safe_load(f)


def on_env(env, config, files, **kwargs):
    """MkDocs hook to inject translations into home.html environment."""
    env.globals['home_translations'] = load_translations('home.translations.yml')
    return env


def on_page_context(context, page, config, nav, **kwargs):
    """
    MkDocs hook to force edit URLs to always point to English version.
    Since translations are auto-generated, all edits should be made to /en/ files.
    
    The Material theme uses page.edit_url to generate the edit button.
    We modify it to always point to /docs/en/ regardless of the current language.
    """
    if page and hasattr(page, 'edit_url') and page.edit_url:
        original_url = page.edit_url
        # Replace any language code with 'en' in the edit URL
        # Pattern: /docs/{language}/ -> /docs/en/
        new_url = re.sub(r'/docs/[a-z]{2}/', '/docs/en/', original_url)
        
        if original_url != new_url:
            page.edit_url = new_url
    
    return context
