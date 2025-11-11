# GitHub Actions Permissions Fix

## Problem
```
remote: Write access to repository not granted.
fatal: unable to access 'https://github.com/...': The requested URL returned error: 403
```

## Lösung 1: Workflow-Datei gefixed ✅

Die `.github/workflows/translate.yml` wurde aktualisiert mit:

```yaml
jobs:
  translate:
    permissions:
      contents: write  # ← Schreibrechte hinzugefügt
```

## Lösung 2: Repository Settings aktivieren

Du musst auch im **GitHub Repository** die Permissions aktivieren:

### Schritt-für-Schritt:

1. Gehe zu deinem Repo: `https://github.com/eddyoaa/grampsDokuTest`

2. Klick **Settings** (oben rechts)

3. In der linken Sidebar: **Actions** → **General**

4. Scrolle runter zu **"Workflow permissions"**

5. Wähle aus:
   - ✅ **"Read and write permissions"** (statt "Read repository contents")
   - ✅ **"Allow GitHub Actions to create and approve pull requests"**

6. Klick **Save**

## Lösung 3: Branch Protection Rules checken

Falls du Branch Protection auf `main` hast:

1. **Settings** → **Branches**
2. Bei "Branch protection rules" für `main`:
3. Stelle sicher dass **"Allow force pushes"** für GitHub Actions aktiviert ist
   - ODER: Aktiviere **"Do not include administrators"** falls du Admin bist

## Nach dem Fix:

1. Commit und push die aktualisierte `translate.yml`:
   ```bash
   git add .github/workflows/translate.yml
   git commit -m "Fix: Add write permissions for GitHub Actions"
   git push test main
   ```

2. Teste den Workflow erneut:
   - GitHub Actions → "Auto-Translate Documentation" → "Run workflow"

## Erwartetes Ergebnis:

✅ Workflow läuft durch
✅ Translations werden committed
✅ Keine 403 Errors mehr

## Alternative: Verwende einen Personal Access Token

Falls die obigen Lösungen nicht funktionieren:

1. Erstelle einen Personal Access Token:
   - GitHub → Settings (dein Profil) → Developer Settings → Personal Access Tokens → Tokens (classic)
   - "Generate new token (classic)"
   - Scope: `repo` (Full control)
   - Generieren und kopieren

2. Füge als Secret hinzu:
   - Repo Settings → Secrets → Actions
   - Name: `PAT_TOKEN`
   - Value: Dein Token

3. Update Workflow:
   ```yaml
   - name: Checkout repository
     uses: actions/checkout@v4
     with:
       token: ${{ secrets.PAT_TOKEN }}  # Statt GITHUB_TOKEN
   ```

Aber das sollte mit den obigen Fixes **nicht nötig** sein!
