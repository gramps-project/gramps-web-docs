#!/usr/bin/env python3
"""
Gramps Web Docs Translation Tool
"""

import os
import re
import sys
import time
import argparse
import requests
from pathlib import Path
from typing import Dict
import yaml


def load_config():
    """Load configuration from config.yaml.example and config_local.yaml"""
    config = {}
    
    # Load base config
    config_file = Path("config.yaml.example")
    if config_file.exists():
        with open(config_file, "r", encoding="utf-8") as f:
            config = yaml.safe_load(f) or {}
    
    # Override with local config (contains API key)
    local_config_file = Path("config_local.yaml")
    if local_config_file.exists():
        with open(local_config_file, "r", encoding="utf-8") as f:
            local_config = yaml.safe_load(f) or {}
            if "api" in local_config:
                config.setdefault("api", {}).update(local_config["api"])
    
    # Validate required fields
    if "api" not in config or "api_key" not in config["api"]:
        print("ERROR: API key not found in config_local.yaml")
        sys.exit(1)
    
    return config


CONFIG = load_config()


class MarkdownProtector:
    """Protects Markdown elements from translation"""
    
    def __init__(self):
        self.placeholders = {}
        self.counter = 0
    
    def _create_placeholder(self, original):
        self.counter += 1
        # Use hex to avoid translation: XPROTX instead of words
        placeholder = f"XPROTX{self.counter:04d}XPROTX"
        self.placeholders[placeholder] = original
        return placeholder
    
    def protect(self, text):
        # Protect Front Matter
        text = re.sub(
            r"^---\n.*?\n---\n",
            lambda m: self._create_placeholder(m.group(0)),
            text,
            flags=re.DOTALL | re.MULTILINE
        )
        
        # Protect Admonition blocks (e.g., !!! info, !!! warning)
        text = re.sub(
            r"^!!! .+$",
            lambda m: self._create_placeholder(m.group(0)),
            text,
            flags=re.MULTILINE
        )
        
        # Protect Code Blocks
        text = re.sub(
            r"```.*?```",
            lambda m: self._create_placeholder(m.group(0)),
            text,
            flags=re.DOTALL
        )
        
        # Protect Inline Code
        text = re.sub(
            r"`[^`\n]+`",
            lambda m: self._create_placeholder(m.group(0)),
            text
        )
        
        # Protect Images
        text = re.sub(
            r"!\[([^\]]*)\]\([^\)]+\)",
            lambda m: self._create_placeholder(m.group(0)),
            text
        )
        
        # Protect Links (entire link including text)
        text = re.sub(
            r"\[([^\]]+)\]\(([^\)]+)\)",
            lambda m: self._create_placeholder(m.group(0)),
            text
        )
        
        # Protect HTML tags
        text = re.sub(
            r"<[^>]+>",
            lambda m: self._create_placeholder(m.group(0)),
            text
        )
        
        # Protect heading IDs
        text = re.sub(
            r"\{#[^\}]+\}",
            lambda m: self._create_placeholder(m.group(0)),
            text
        )
        
        # Protect URLs
        text = re.sub(
            r"https?://[^\s<>\"{}|\\^`\[\]]+",
            lambda m: self._create_placeholder(m.group(0)),
            text
        )
        
        return text
    
    def restore(self, text):
        for placeholder, original in self.placeholders.items():
            text = text.replace(placeholder, original)
        return text


def translate_table(table_text, target_lang, source_lang="en"):
    """Translate Markdown table cell by cell while preserving structure"""
    print(f"   DEBUG: Translating table with {len(table_text)} chars")
    lines = table_text.split('\n')
    if len(lines) < 2:
        return table_text
    
    translated_lines = []
    
    for i, line in enumerate(lines):
        # Check if this is a separator line (contains only |, -, :, spaces)
        if re.match(r'^[\s\|:\-]+$', line):
            # Keep separator as-is
            translated_lines.append(line)
            continue
        
        # This is a content line - translate each cell
        if '|' in line:
            # Split by pipe, but keep leading/trailing pipes
            cells = line.split('|')
            translated_cells = []
            
            for cell in cells:
                cell_content = cell.strip()
                if cell_content:
                    try:
                        # Translate individual cell
                        translated_cell = translate_text(cell_content, target_lang, source_lang)
                        # Preserve original spacing
                        if cell.startswith(' '):
                            translated_cell = ' ' + translated_cell.strip()
                        if cell.endswith(' '):
                            translated_cell = translated_cell.strip() + ' '
                        translated_cells.append(translated_cell)
                    except Exception as e:
                        print(f"   Warning: Failed to translate cell '{cell_content}': {e}")
                        translated_cells.append(cell)
                else:
                    # Empty cell
                    translated_cells.append(cell)
            
            translated_lines.append('|'.join(translated_cells))
        else:
            # No pipes - shouldn't happen in a table, but handle it
            translated_lines.append(line)
    
    return '\n'.join(translated_lines)


def translate_text(text, target_lang, source_lang="en"):
    """Translate text using LibreTranslate API"""
    api_config = CONFIG["api"]
    url = api_config["url"]
    api_key = api_config["api_key"]
    timeout = api_config.get("timeout", 30)
    max_retries = api_config.get("max_retries", 3)
    max_chars = api_config.get("max_chars_per_request", 5000)
    
    if len(text) > max_chars:
        raise ValueError(f"Text too long: {len(text)} chars (max: {max_chars})")
    
    if not text.strip():
        return text
    
    headers = {
        "Content-Type": "application/json",
        "Authorization": api_key
    }
    
    payload = {
        "q": text,
        "source": source_lang,
        "target": target_lang,
        "format": "text"
    }
    
    for attempt in range(max_retries):
        try:
            response = requests.post(url, json=payload, headers=headers, timeout=timeout)
            response.raise_for_status()
            result = response.json()
            return result.get("translatedText", text)
        
        except requests.exceptions.HTTPError as e:
            if response.status_code == 429:
                wait_time = (2 ** attempt) * 2
                print(f"Rate limited. Waiting {wait_time}s...")
                time.sleep(wait_time)
            elif response.status_code == 403:
                raise Exception("API authentication failed. Check your API key.")
            else:
                raise Exception(f"HTTP error: {e}")
        
        except requests.exceptions.Timeout:
            if attempt < max_retries - 1:
                wait_time = (2 ** attempt)
                print(f"Timeout. Retrying in {wait_time}s...")
                time.sleep(wait_time)
            else:
                raise Exception("Translation timeout")
        
        except requests.exceptions.RequestException as e:
            if attempt < max_retries - 1:
                wait_time = (2 ** attempt)
                print(f"Request failed: {e}. Retrying in {wait_time}s...")
                time.sleep(wait_time)
            else:
                raise Exception(f"Translation failed: {e}")
    
    raise Exception("Translation failed: max retries exceeded")


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
        
        # Preserve trailing newlines (LibreTranslate adds artifacts if text ends with \n)
        trailing_newlines = len(content) - len(content.rstrip('\n'))
        content_stripped = content.rstrip('\n')
        
        # Step 1: Find and translate tables separately
        def translate_table_match(match):
            table_text = match.group(0)
            try:
                return translate_table(table_text, target_lang)
            except Exception as e:
                print(f"   Warning: Table translation failed: {e}")
                return table_text
        
        # Pattern to match Markdown tables (header + separator + rows)
        table_pattern = r'^(.+\|.+)\n([\-:|]+\|[\-:|]+)\n((.*\|.*\n?)+)'
        content_with_translated_tables = re.sub(
            table_pattern,
            translate_table_match,
            content_stripped,
            flags=re.MULTILINE
        )
        
        # Step 2: Protect Markdown elements and translate rest
        protector = MarkdownProtector()
        protected_content = protector.protect(content_with_translated_tables)
        
        print(f"   Translating to {target_lang}: {relative_path}")
        translated = translate_text(protected_content, target_lang)
        
        final_content = protector.restore(translated)
        
        # Restore trailing newlines
        final_content += '\n' * trailing_newlines
        
        dst_path.parent.mkdir(parents=True, exist_ok=True)
        with open(dst_path, "w", encoding="utf-8") as f:
            f.write(final_content)
        
        print(f"   Saved: {dst_path}")
        return True
    
    except Exception as e:
        print(f"   ERROR: {e}")
        return False


def main():
    parser = argparse.ArgumentParser(description="Translate Gramps Web documentation")
    parser.add_argument("--file", type=Path, help="Translate a specific file")
    parser.add_argument("--lang", default="de", help="Target language (de, fr, or all)")
    parser.add_argument("--test", action="store_true", help="Test mode")
    parser.add_argument("--force", action="store_true", help="Overwrite existing")
    parser.add_argument("--dry-run", action="store_true", help="Dry run")
    
    args = parser.parse_args()
    
    translation_config = CONFIG["translation"]
    if args.lang == "all":
        target_langs = translation_config["target_languages"]
    else:
        target_langs = [args.lang]
    
    if args.test:
        files = [Path("docs/en/user-guide/first-login.md")]
    elif args.file:
        files = [args.file]
    else:
        source_dir = Path(translation_config["source_dir"])
        files = sorted(source_dir.rglob("*.md"))
    
    print("=" * 60)
    print("Gramps Web Docs Translation")
    print("=" * 60)
    print(f"Source: {translation_config['source_dir']}")
    print(f"Target languages: {', '.join(target_langs)}")
    print(f"Files to translate: {len(files)}")
    if args.dry_run:
        print("  DRY RUN MODE")
    print("=" * 60)
    
    if args.dry_run:
        for file in files:
            print(f"Would translate: {file}")
        return
    
    success_count = 0
    error_count = 0
    
    for file in files:
        if not file.exists():
            print(f" File not found: {file}")
            error_count += 1
            continue
        
        print(f"\n {file}")
        for lang in target_langs:
            if translate_file(file, lang, force=args.force):
                success_count += 1
            else:
                error_count += 1
    
    print("\n" + "=" * 60)
    print(f" Success: {success_count}")
    print(f" Errors: {error_count}")
    print("=" * 60)


if __name__ == "__main__":
    main()
