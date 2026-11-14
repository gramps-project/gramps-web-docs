"""
MkDocs hooks to load translation files and inject them into Jinja2 templates.
This makes translations more maintainable by separating them from template code.
"""

import json
import yaml
import re
import logging
from pathlib import Path

from mkdocs.plugins import event_priority

log = logging.getLogger(f"mkdocs.plugins.hooks")

# Search index settings per locale. Locales not listed here use the lunr
# language of the same name. Material ships no lunr support for Ukrainian, and
# for Chinese it relies on build-time segmentation with jieba instead of a lunr
# language (settings taken from Material's partials/languages/*.html).
SEARCH_DEFAULT_SEPARATOR = r"[\s\-]+"
SEARCH_CONFIG_OVERRIDES = {
    "en": {"pipeline": ["stopWordFilter"]},
    "uk": {"lang": ["en"], "pipeline": []},
    "zh": {
        "lang": ["en"],
        "separator": r"[\s​　\-、。，．？！；]+",
        "pipeline": ["stemmer"],
    },
    "ja": {"separator": r"[\s\-　、。，．]+", "pipeline": ["stemmer"]},
}


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


_default_404 = None


def on_post_template(output_content, template_name, config, **kwargs):
    """
    Keep the 404 page in the default language.

    There is only one 404.html at the site root, but mkdocs-static-i18n renders
    it again for every language, so the last language built would win. The
    default language is built first (outside the i18n plugin's inner builds),
    so remember its 404 page and reuse it for all other languages.
    """
    global _default_404
    if template_name != "404.html":
        return output_content
    i18n = config.plugins.get("i18n")
    if i18n is None or not getattr(i18n, "building", False):
        _default_404 = output_content
        return output_content
    return _default_404 or output_content


def _search_config(locale, base_config):
    """Return the lunr configuration for a single-language search index."""
    search_config = dict(base_config)
    search_config.update(
        {"lang": [locale], "separator": SEARCH_DEFAULT_SEPARATOR, "pipeline": []}
    )
    search_config.update(SEARCH_CONFIG_OVERRIDES.get(locale, {}))
    return search_config


@event_priority(-200)
def on_post_build(config, **kwargs):
    """
    Split the combined search index into one index per language.

    mkdocs-static-i18n merges the entries of all languages into a single
    search/search_index.json, configured for every language at once. That
    makes search slow and returns results in all languages. After the i18n
    plugin has written the merged index (priority -100), this hook writes
    search/search_index.json for the default language and
    <locale>/search/search_index.json for each other language. The template
    override in main.html makes each page load the index of its language.
    """
    i18n = config.plugins.get("i18n")
    if i18n is None or getattr(i18n, "building", False):
        # inner per-language build of the i18n plugin; wait for the final run
        return

    site_dir = Path(config.site_dir)
    index_path = site_dir / "search" / "search_index.json"
    if not index_path.exists():
        return
    index = json.loads(index_path.read_text(encoding="utf-8"))

    languages = [lang for lang in i18n.config.languages if lang.build]
    default = next(lang.locale for lang in languages if lang.default)
    other_locales = [lang.locale for lang in languages if not lang.default]

    docs_by_locale = {locale: [] for locale in [default, *other_locales]}
    for doc in index["docs"]:
        prefix = doc["location"].split("/", 1)[0]
        locale = prefix if prefix in docs_by_locale else default
        docs_by_locale[locale].append(doc)

    for locale, docs in docs_by_locale.items():
        target_dir = site_dir if locale == default else site_dir / locale
        path = target_dir / "search" / "search_index.json"
        path.parent.mkdir(parents=True, exist_ok=True)
        data = {"config": _search_config(locale, index["config"]), "docs": docs}
        path.write_text(
            json.dumps(data, separators=(",", ":"), ensure_ascii=False),
            encoding="utf-8",
        )
    log.info(
        "Split search index into %d languages (%d entries)",
        len(docs_by_locale),
        len(index["docs"]),
    )
