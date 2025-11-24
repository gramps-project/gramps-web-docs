"""
MkDocs hooks to load translation files and inject them into Jinja2 templates.
This makes translations more maintainable by separating them from template code.
"""

import yaml
from pathlib import Path


def load_translations(translation_file):
    """Load translations from YAML file."""
    file_path = Path(__file__).parent / translation_file
    with open(file_path, 'r', encoding='utf-8') as f:
        return yaml.safe_load(f)


def on_env(env, config, files, **kwargs):
    """MkDocs hook to inject translations into home.html environment."""
    env.globals['home_translations'] = load_translations('home.translations.yml')
    return env
