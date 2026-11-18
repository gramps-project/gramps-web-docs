# Benutzersystem

Gramps Web ist nicht dafür gedacht, öffentlich im Internet zugänglich zu sein, sondern nur für authentifizierte Benutzer. Benutzerkonten können vom Seiteninhaber über die Befehlszeile oder die Weboberfläche erstellt werden oder durch Selbstregistrierung und anschließende Genehmigung durch den Seiteninhaber.

## Benutzerrollen

Die folgenden Benutzerrollen sind derzeit definiert.

Rolle | Rollen-ID | Berechtigungen
-----|---------|------------
Gast | 0 | Nicht-private Objekte anzeigen
Mitglied | 1 | Gast + private Objekte anzeigen
Beitragsleistender* | 2 | Mitglied + Objekte hinzufügen
Redakteur | 3 | Beitragsleistender + Objekte bearbeiten und löschen
Besitzer | 4 | Redakteur + Benutzer verwalten
Admin | 5 | Besitzer + andere Bäume in einer Multi-Baum-Konfiguration bearbeiten

Ob ein Datensatz privat ist, wird pro Datensatz festgelegt, siehe [Private Datensätze](../user-guide/privacy.md). Standardmäßig ist nichts privat, nicht einmal lebende Personen.

\* Beachten Sie, dass die Rolle "Beitragsleistender" derzeit nur teilweise unterstützt wird; z.B. können Familienobjekte nicht hinzugefügt werden, da sie eine Änderung der zugrunde liegenden Gramps-Personenobjekte von Familienmitgliedern implizieren. Es wird empfohlen, die anderen Rollen wann immer möglich zu verwenden.

## Konfigurieren, wer den KI-Chat nutzen kann

Wenn Sie [den KI-Chat konfiguriert haben](chat.md), sehen Sie hier eine Option, um auszuwählen, welche Benutzergruppen die Chat-Funktion nutzen dürfen.

## Benutzer verwalten

Es gibt zwei Möglichkeiten, Benutzer zu verwalten:

- Mit Besitzerberechtigungen über die Weboberfläche
- Über die Befehlszeile auf dem Server

Das für den ersten Zugriff auf die Webanwendung erforderliche Besitzerkonto kann im Onboarding-Assistenten hinzugefügt werden, der automatisch gestartet wird, wenn Sie Gramps Web mit einer leeren Benutzerdatenbank aufrufen.

### Benutzer über die Befehlszeile verwalten

Beim Einsatz von [Docker Compose](deployment.md) lautet der grundlegende Befehl

```bash
docker compose run grampsweb python3 -m gramps_webapi user COMMAND [ARGS]
```

Der `COMMAND` kann `add`, `set-password` oder `delete` sein. Verwenden Sie `--help` für `[ARGS]`, um die Syntax und mögliche Konfigurationsoptionen anzuzeigen.

`set-password NAME` setzt ein neues Passwort für einen vorhandenen Benutzer, ohne das alte zu benötigen, zum Beispiel wenn sich niemand mehr anmelden kann und die E-Mail nicht für Passwortzurücksetzungen eingerichtet ist (Gramps Web API 3.26+). Es wird zweimal nach dem Passwort gefragt, ohne es anzuzeigen, sodass das Passwort nicht im Shell-Verlauf landet. Alle Sitzungen des Benutzers werden beendet.

### Genehmigung selbstregistrierter Benutzer

Wenn sich ein Benutzer selbst registriert, erhält er nicht sofort Zugriff. Eine E-Mail wird an den Baum-Besitzer über die neue Benutzerregistrierung gesendet, und der Benutzer erhält eine E-Mail-Anfrage zur Bestätigung seiner E-Mail-Adresse. Die erfolgreiche Bestätigung der E-Mail-Adresse ändert die Rolle des Benutzers von `unconfirmed` zu `disabled`. Solange sich das Benutzerkonto in einer dieser beiden Rollen befindet, kann sich der Benutzer nicht anmelden. Der Baum-Besitzer muss die Anfrage des Benutzers überprüfen und dem Benutzer eine geeignete Rolle zuweisen, bevor er sich anmelden darf.
