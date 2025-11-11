# Git Setup für neues privates Repo

# 1. Aktuelles Git Repo Status checken
git status

# 2. Alle Änderungen committen (Translation System + erste Übersetzungen)
git add .
git commit -m "Add OpenAI-based translation system

- Replaced LibreTranslate with OpenAI GPT-4o-mini
- Added translate.py with CLI
- Added config system (config.yaml.example + config_local.yaml)
- Added GitHub Action for auto-translation
- Added TRANSLATION.md documentation
- Initial translations for DE and FR"

# 3. Remote für dein neues privates Repo hinzufügen
# WICHTIG: Ersetze <YOUR-USERNAME> mit deinem GitHub Username
git remote add test https://github.com/<YOUR-USERNAME>/gramps-web-docs-translation-test.git

# 4. Push zum neuen Repo
git push test main

# Optional: Wenn du auch einen neuen Branch erstellen willst
git checkout -b translation-system
git push test translation-system
