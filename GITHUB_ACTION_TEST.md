# Test-Plan für GitHub Action

## Nach dem Setup:

### Test 1: Manuelle Trigger
1. Gehe zu deinem Repo auf GitHub
2. Actions Tab
3. "Auto-Translate Documentation" workflow
4. "Run workflow" → Run on main
5. Beobachte die Logs

### Test 2: File Change Trigger
1. Editiere eine kleine Datei lokal:
   ```bash
   # Kleine Änderung an einer Test-Datei
   echo "\nTest update." >> docs/en/help/help.md
   ```

2. Commit und push:
   ```bash
   git add docs/en/help/help.md
   git commit -m "Test: Update help.md for translation trigger"
   git push test main
   ```

3. Gehe zu GitHub Actions und schaue zu wie:
   - Changed files erkannt werden
   - Nur help.md übersetzt wird (DE + FR)
   - Translations automatisch committed werden

### Test 3: Multiple Files
1. Ändere mehrere Dateien:
   ```bash
   echo "\nUpdate 1" >> docs/en/help/help.md
   echo "\nUpdate 2" >> docs/en/features/index.md
   git add docs/en/
   git commit -m "Test: Update multiple files"
   git push test main
   ```

2. Action sollte beide Dateien übersetzen

### Erwartete Kosten pro Test:
- Test 1 (alle Dateien): ~$0.05
- Test 2 (1 Datei): ~$0.001
- Test 3 (2 Dateien): ~$0.002

### Troubleshooting:
Wenn Action fehlschlägt, checke:
1. OPENAI_API_KEY Secret richtig gesetzt?
2. API Key hat Guthaben?
3. Logs in GitHub Actions für Error Messages
