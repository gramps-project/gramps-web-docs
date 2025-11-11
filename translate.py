#!/usr/bin/env python3
"""
Gramps Web Docs Translation Tool using OpenAI GPT-4o-mini
Translates Markdown documentation while preserving formatting.
"""

import argparse
import sys
import time
from pathlib import Path
import yaml
from openai import OpenAI


def load_config():
    """Load configuration from YAML files"""
    config_file = Path("config.yaml.example")
    local_config_file = Path("config_local.yaml")
    
    if not config_file.exists():
        raise FileNotFoundError("config.yaml.example not found")
    
    with open(config_file, "r", encoding="utf-8") as f:
        config = yaml.safe_load(f)
    
    # Merge with local config if it exists
    if local_config_file.exists():
        with open(local_config_file, "r", encoding="utf-8") as f:
            local_config = yaml.safe_load(f)
            if local_config:
                # Deep merge
                for key, value in local_config.items():
                    if isinstance(value, dict) and key in config:
                        config[key].update(value)
                    else:
                        config[key] = value
    
    # Validate
    if not config.get("api", {}).get("openai_api_key"):
        raise ValueError("openai_api_key not found in config. Add it to config_local.yaml")
    
    return config


CONFIG = load_config()


def translate_with_openai(content, target_lang, source_lang="en"):
    """Translate Markdown content using OpenAI GPT-4o-mini"""
    api_config = CONFIG["api"]
    client = OpenAI(api_key=api_config["openai_api_key"])
    model = api_config.get("model", "gpt-4o-mini")
    
    # Language names for better prompting
    lang_names = {
        "de": "German",
        "fr": "French",
        "es": "Spanish",
        "it": "Italian",
        "en": "English"
    }
    
    target_lang_name = lang_names.get(target_lang, target_lang)
    source_lang_name = lang_names.get(source_lang, source_lang)
    
    prompt = f"""You are translating technical documentation from {source_lang_name} to {target_lang_name}.

INSTRUCTIONS:
- Translate ALL text content to {target_lang_name}
- Preserve ALL Markdown formatting exactly (tables, links, code blocks, etc.)
- Keep URLs, file paths, and code unchanged
- Maintain the exact structure and line breaks

Document to translate:

{content}

Translated document in {target_lang_name}:"""

    max_retries = api_config.get("max_retries", 3)
    timeout = api_config.get("timeout", 60)
    
    for attempt in range(max_retries):
        try:
            response = client.chat.completions.create(
                model=model,
                messages=[
                    {"role": "system", "content": "You are a professional translator specialized in technical documentation. You preserve Markdown formatting perfectly."},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.3,  # Lower temperature for more consistent translations
                timeout=timeout
            )
            
            translated = response.choices[0].message.content
            
            # Remove potential markdown code block wrappers if AI added them
            if translated.startswith("```markdown\n"):
                translated = translated[len("```markdown\n"):]
            if translated.startswith("```\n"):
                translated = translated[len("```\n"):]
            if translated.endswith("\n```"):
                translated = translated[:-len("\n```")]
            if translated.endswith("```"):
                translated = translated[:-len("```")]
            
            return translated.strip()
            
        except Exception as e:
            if attempt < max_retries - 1:
                wait_time = 2 ** attempt
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
        print(f"   ERROR: Failed to translate {src_path}: {e}")
        return False


def main():
    parser = argparse.ArgumentParser(
        description="Translate Gramps Web documentation using OpenAI GPT-4o-mini"
    )
    parser.add_argument(
        "--file",
        type=str,
        help="Translate a specific file (relative to docs/en/)"
    )
    parser.add_argument(
        "--lang",
        type=str,
        choices=["de", "fr", "all"],
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
        file_path = Path(args.file)
        if not file_path.is_absolute():
            file_path = source_dir / file_path
        files_to_translate = [file_path]
    else:
        # Find all .md files recursively
        files_to_translate = sorted(source_dir.rglob("*.md"))
    
    print("=" * 60)
    print("Gramps Web Docs Translation (OpenAI GPT-4o-mini)")
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
    
    success_count = 0
    error_count = 0
    
    for file_path in files_to_translate:
        if not file_path.exists():
            print(f"WARNING: File not found: {file_path}")
            continue
        
        print(f"\n{file_path.relative_to(source_dir)}")
        
        for lang in target_languages:
            if translate_file(file_path, lang, force=args.force):
                success_count += 1
            else:
                error_count += 1
    
    print()
    print("=" * 60)
    print(f" Success: {success_count}")
    print(f" Errors: {error_count}")
    print("=" * 60)
    
    sys.exit(0 if error_count == 0 else 1)


if __name__ == "__main__":
    main()
