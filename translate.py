#!/usr/bin/env python3
"""
Gramps Web Docs Translation Tool using the OpenAI API
Translates Markdown documentation while preserving formatting.
"""

import argparse
import os
import sys
import time
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables from .env file if it exists
load_dotenv()


# Configuration
CONFIG = {
    "api": {
        "provider": "openai",
        "model": "gpt-5.6-luna",
        "reasoning_effort": "low",
        "timeout": 300,
        "max_retries": 3,
        "retry_delay": 5,
        "workers": 8  # parallel API requests
    },
    "translation": {
        "source_language": "en",
        "target_languages": ["de", "fr", "es", "zh", "vi", "tr", "ru", "pt", "ja", "da", "fi", "it", "uk"],
        "docs_dir": "docs",
        "source_dir": "docs/en"
    }
}

# Language names for prompting and display
LANGUAGE_NAMES = {
    "de": "German",
    "fr": "French",
    "es": "Spanish",
    "zh": "Simplified Chinese",
    "vi": "Vietnamese",
    "tr": "Turkish",
    "ru": "Russian",
    "pt": "Portuguese",
    "ja": "Japanese",
    "da": "Danish",
    "fi": "Finnish",
    "it": "Italian",
    "uk": "Ukrainian",
    "en": "English"
}

# Get API key from environment variable
API_KEY = os.getenv("OPENAI_API_KEY")
if not API_KEY:
    raise ValueError(
        "OPENAI_API_KEY environment variable not set.\n"
        "Set it in .env file or as environment variable."
    )


CLIENT = OpenAI(api_key=API_KEY)  # thread-safe, shared by all workers


def translate_with_openai(content, target_lang, source_lang="en"):
    """Translate Markdown content using the configured OpenAI model"""
    api_config = CONFIG["api"]
    model = api_config["model"]
    
    target_lang_name = LANGUAGE_NAMES.get(target_lang, target_lang)
    source_lang_name = LANGUAGE_NAMES.get(source_lang, source_lang)
    
    # Per-language terminology glossaries for consistent translation of key terms
    GLOSSARIES = {
        "de": """
TERMINOLOGY (always use these translations, consistent with official Gramps German):
- Tag / Tags → Etikett / Etiketten
- Home Person → Hauptperson
""",
    }
    glossary = GLOSSARIES.get(target_lang, "")

    # How to address the reader, matching the existing translations
    ADDRESS = {
        "de": "informal \"du\" (lowercase, never \"Sie\")",
        "fr": "formal \"vous\"",
        "es": "informal \"tú\"",
        "it": "informal \"tu\"",
        "pt": "\"você\"",
        "ru": "formal \"вы\"",
        "uk": "formal \"ви\"",
        "da": "\"du\"",
        "fi": "\"sinä\" (singular verb forms such as \"voit\")",
        "tr": "formal \"siz\"",
        "vi": "\"bạn\"",
        "zh": "polite \"您\"",
        "ja": "polite です/ます style",
    }
    address = ADDRESS.get(target_lang)
    if address:
        glossary += f"\nADDRESS THE READER CONSISTENTLY: use {address} throughout.\n"

    prompt = f"""You are translating technical documentation from {source_lang_name} to {target_lang_name}.

INSTRUCTIONS:
- Translate ALL text content to {target_lang_name}
- Preserve ALL Markdown formatting exactly (tables, links, code blocks, etc.)
- Keep URLs, file paths, and code unchanged
- Maintain the exact structure and line breaks
{glossary}
Document to translate:

{content}

Translated document in {target_lang_name}:"""

    max_retries = api_config.get("max_retries", 3)
    timeout = api_config.get("timeout", 180)
    retry_delay = api_config.get("retry_delay", 5)
    
    for attempt in range(max_retries):
        try:
            response = CLIENT.chat.completions.create(
                model=model,
                messages=[
                    {"role": "system", "content": "You are a professional translator specialized in technical documentation. You preserve Markdown formatting perfectly."},
                    {"role": "user", "content": prompt}
                ],
                reasoning_effort=api_config["reasoning_effort"],
                timeout=timeout
            )

            choice = response.choices[0]
            if choice.finish_reason != "stop":
                # e.g. "length": never save a truncated translation
                raise Exception(f"Incomplete response (finish_reason={choice.finish_reason})")
            translated = choice.message.content
            
            # Remove a markdown code block wrapper if the AI added one. Only
            # strip the closing fence together with an opening wrapper: a
            # document may legitimately end with a code block.
            for opening in ("```markdown\n", "```md\n", "```\n"):
                if translated.startswith(opening) and translated.rstrip().endswith("```"):
                    translated = translated[len(opening):].rstrip()[:-len("```")]
                    break
            
            return translated.strip()
            
        except Exception as e:
            if attempt < max_retries - 1:
                wait_time = retry_delay * (2 ** attempt)  # Exponential backoff
                print(f"   Retry {attempt + 1}/{max_retries} after error: {e}")
                time.sleep(wait_time)
            else:
                raise Exception(f"Translation failed after {max_retries} attempts: {e}")


def translate_file(src_path, target_lang, force=False):
    """Translate a single Markdown file"""
    translation_config = CONFIG["translation"]
    source_dir = Path(translation_config["source_dir"])
    docs_dir = Path(translation_config["docs_dir"])
    
    relative_path = src_path.relative_to(source_dir)
    dst_path = docs_dir / target_lang / relative_path
    
    if dst_path.exists() and not force:
        print(f"    Skipping {dst_path} (already exists)")
        return True
    
    try:
        with open(src_path, "r", encoding="utf-8") as f:
            content = f.read()
        
        print(f"   Translating to {target_lang}: {relative_path}")
        translated = translate_with_openai(content, target_lang)
        
        dst_path.parent.mkdir(parents=True, exist_ok=True)
        with open(dst_path, "w", encoding="utf-8") as f:
            f.write(translated)
            # Ensure file ends with newline
            if not translated.endswith('\n'):
                f.write('\n')
        
        print(f"   Saved: {dst_path}")
        return True
        
    except Exception as e:
        print(f"   ERROR: Failed to translate {src_path} to {target_lang}: {e}")
        return False


def main():
    parser = argparse.ArgumentParser(
        description=f"Translate Gramps Web documentation using OpenAI {CONFIG['api']['model']}"
    )
    parser.add_argument(
        "--file",
        type=str,
        nargs="+",
        help="Translate specific file(s) (relative to docs/en/)"
    )
    parser.add_argument(
        "--workers",
        type=int,
        default=CONFIG["api"]["workers"],
        help="Number of translations to run in parallel"
    )
    parser.add_argument(
        "--lang",
        type=str,
        choices=["de", "fr", "es", "zh", "vi", "tr", "ru", "pt", "ja", "da", "fi", "it", "uk", "all"],
        default="all",
        help="Target language(s)"
    )
    parser.add_argument(
        "--test",
        action="store_true",
        help="Test mode: only translate docs/en/user-guide/first-login.md"
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="Force translation even if target file exists"
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Show what would be done without actually translating"
    )
    
    args = parser.parse_args()
    
    translation_config = CONFIG["translation"]
    source_dir = Path(translation_config["source_dir"])
    
    # Determine target languages
    if args.lang == "all":
        target_languages = translation_config["target_languages"]
    else:
        target_languages = [args.lang]
    
    # Determine files to translate
    if args.test:
        files_to_translate = [source_dir / "user-guide" / "first-login.md"]
    elif args.file:
        files_to_translate = []
        for name in args.file:
            file_path = Path(name)
            if not file_path.is_absolute():
                file_path = source_dir / file_path
            files_to_translate.append(file_path)
    else:
        # Find all .md files recursively
        files_to_translate = sorted(source_dir.rglob("*.md"))

    print("=" * 60)
    print(f"Gramps Web Docs Translation (OpenAI {CONFIG['api']['model']})")
    print("=" * 60)
    print(f"Source: {source_dir}")
    print(f"Target languages: {', '.join(target_languages)}")
    print(f"Files to translate: {len(files_to_translate)}")
    print("=" * 60)
    print()
    
    if args.dry_run:
        print("DRY RUN MODE - No files will be translated")
        for lang in target_languages:
            print(f"\n{lang.upper()}:")
            for file_path in files_to_translate:
                print(f"  Would translate: {file_path.relative_to(source_dir)}")
        return
    
    jobs = []
    for file_path in files_to_translate:
        if not file_path.exists():
            print(f"WARNING: File not found: {file_path}")
            continue
        for lang in target_languages:
            jobs.append((file_path, lang))

    # Run (file, language) translations in parallel
    with ThreadPoolExecutor(max_workers=max(1, args.workers)) as executor:
        results = list(executor.map(
            lambda job: translate_file(job[0], job[1], force=args.force), jobs
        ))

    success_count = sum(results)
    error_count = len(results) - success_count

    print()
    print("=" * 60)
    print(f" Success: {success_count}")
    print(f" Errors: {error_count}")
    print("=" * 60)
    
    sys.exit(0 if error_count == 0 else 1)


if __name__ == "__main__":
    main()
