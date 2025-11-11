# Gramps Web Documentation Translation

Automated translation system for Gramps Web documentation using OpenAI GPT-4o-mini.

## Features

- ✅ Translates Markdown while preserving formatting (tables, code blocks, links)
- ✅ Supports multiple target languages (currently: German, French)
- ✅ Smart translation with OpenAI GPT-4o-mini (~$0.05 for all docs)
- ✅ CLI for manual translation
- ✅ GitHub Actions for automated translation on changes
- ✅ Preserves URLs, code, and Markdown structure

## Setup

### 1. Install Dependencies

```bash
python -m venv venv
.\venv\Scripts\Activate.ps1  # Windows PowerShell
# or: source venv/bin/activate  # Linux/Mac

pip install -r requirements.txt
pip install openai
```

### 2. Configure API Key

1. Create an OpenAI account at https://platform.openai.com
2. Generate an API key at https://platform.openai.com/api-keys
3. Copy `config.yaml.example` to `config_local.yaml`:

```bash
Copy-Item config.yaml.example config_local.yaml
```

4. Edit `config_local.yaml` and add your API key:

```yaml
# Local Configuration (not committed to Git)
api:
  openai_api_key: "sk-proj-YOUR-KEY-HERE"
```

**Note:** `config_local.yaml` is in `.gitignore` to keep your API key private.

### 3. Configuration

Edit `config.yaml.example` to change settings:

```yaml
# OpenAI API Configuration
api:
  provider: "openai"
  model: "gpt-4o-mini"  # Fast and cheap
  timeout: 60
  max_retries: 3

# Translation Settings
translation:
  source_language: "en"
  target_languages:
    - "de"  # German
    - "fr"  # French
  source_dir: "docs/en"
  docs_dir: "docs"
```

## Usage

### Translate Single File

```bash
# Test with a small file
python translate.py --test --lang de

# Translate specific file
python translate.py --file install_setup/users.md --lang de

# Force re-translation (overwrite existing)
python translate.py --file install_setup/users.md --lang de --force

# Translate to all configured languages
python translate.py --file install_setup/users.md --lang all
```

### Translate All Files

```bash
# Dry run (see what would be translated)
python translate.py --lang all --dry-run

# Translate everything
python translate.py --lang all

# Force re-translate all files
python translate.py --lang all --force
```

### Command Line Options

```
--file <path>      Translate specific file (relative to docs/en/)
--lang <lang>      Target language: de, fr, or all
--test             Test mode: only translate first-login.md
--force            Overwrite existing translations
--dry-run          Show what would be done without translating
```

## How It Works

1. **Source Files:** All Markdown files in `docs/en/`
2. **Translation:** OpenAI GPT-4o-mini translates content while preserving:
   - Markdown formatting (tables, lists, headers)
   - Code blocks and inline code
   - URLs and links
   - HTML tags
   - YAML front matter
3. **Output:** Translated files saved to `docs/de/` and `docs/fr/`

## Cost Estimation

Using **GPT-4o-mini** (November 2025 pricing):
- Input: $0.15 / 1M tokens
- Output: $0.60 / 1M tokens

**Your docs (~50 files, ~135KB, ~34K tokens):**
- Initial translation (all files, 2 languages): **~$0.05**
- Single file update: **~$0.001** (0.1 cent)

**Very affordable for high-quality translations!**

## GitHub Actions (CI/CD)

Automatically translate changed files when you push to `docs/en/`:

### Setup

1. Add your OpenAI API key to GitHub Secrets:
   - Go to repository Settings → Secrets and variables → Actions
   - Add secret: `OPENAI_API_KEY` with your key

2. The workflow file `.github/workflows/translate.yml` will:
   - Trigger on changes to `docs/en/**/*.md`
   - Translate only changed files
   - Commit translations to `docs/de/` and `docs/fr/`
   - Create a pull request with translations

## Troubleshooting

### "openai_api_key not found"
- Make sure `config_local.yaml` exists and contains your API key
- Check the key format: `openai_api_key: "sk-proj-..."`

### Translation Quality Issues
- GPT-4o-mini is very good, but check critical translations manually
- You can adjust the `temperature` parameter in `translate.py` (line 100)
- Lower temperature (0.1-0.3) = more consistent, higher (0.5-0.7) = more creative

### API Rate Limits
- OpenAI has rate limits based on your account tier
- The script has retry logic with exponential backoff
- If you hit limits, wait a few minutes and retry

### Cost Control
- Use `--dry-run` to see what would be translated
- Use `--file` to translate only specific files
- Monitor usage at https://platform.openai.com/usage

## File Structure

```
gramps-web-docs/
├── docs/
│   ├── en/           # Source (English)
│   ├── de/           # German translations
│   └── fr/           # French translations
├── translate.py      # Translation script
├── config.yaml.example   # Template configuration
├── config_local.yaml     # Your API key (gitignored)
├── .gitignore
└── TRANSLATION.md    # This file
```

## Adding New Languages

1. Edit `config.yaml.example`:

```yaml
translation:
  target_languages:
    - "de"
    - "fr"
    - "es"  # Spanish
    - "it"  # Italian
```

2. Run translation:

```bash
python translate.py --lang all
```

3. Update `mkdocs.yml` to include new language.

## Examples

### Example 1: Quick Test
```bash
python translate.py --test --lang de
```

### Example 2: Translate Documentation for New Feature
```bash
# You added a new file: docs/en/features/new-feature.md
python translate.py --file features/new-feature.md --lang all
```

### Example 3: Update Existing Translation
```bash
# You edited docs/en/install_setup/users.md
python translate.py --file install_setup/users.md --lang all --force
```

### Example 4: Full Re-translation
```bash
# Re-translate everything (e.g., after improving translation prompts)
python translate.py --lang all --force
```

## Technical Details

### Translation Process

1. **Load Configuration:** Merge `config.yaml.example` and `config_local.yaml`
2. **Find Files:** Recursively scan `docs/en/` for `.md` files
3. **For Each File:**
   - Read content
   - Send to OpenAI API with specialized prompt
   - Prompt ensures Markdown preservation
   - Save translated content to `docs/<lang>/`
4. **Report:** Show success/error count

### API Prompt Strategy

The script uses a carefully crafted prompt that:
- Explicitly instructs to translate ALL text
- Preserves Markdown formatting
- Keeps URLs and code unchanged
- Maintains table structure
- Uses low temperature (0.3) for consistency

### Error Handling

- **Retry Logic:** 3 attempts with exponential backoff
- **Timeout:** 60 seconds per API call
- **Error Reporting:** Failed files are reported at the end
- **Partial Success:** Script continues even if some files fail

## Maintenance

### Updating Translations

When you edit English docs:

```bash
# Option 1: Translate only changed file
python translate.py --file path/to/changed.md --lang all --force

# Option 2: Let GitHub Actions do it automatically (after setup)
git add docs/en/path/to/changed.md
git commit -m "Update documentation"
git push
# GitHub Actions will translate and create PR
```

### Monitoring Costs

Check your usage at: https://platform.openai.com/usage

Set up billing alerts at: https://platform.openai.com/account/billing/payment-methods

## License

Same as Gramps Web documentation.

## Support

- Issues: https://github.com/gramps-project/gramps-web-docs/issues
- OpenAI API Docs: https://platform.openai.com/docs
- GPT-4o-mini Info: https://openai.com/index/gpt-4o-mini-advancing-cost-efficient-intelligence/
