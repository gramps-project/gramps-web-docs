# Benutzersystem

Gramps Web ist nicht dafür gedacht, öffentlich im Internet zugänglich gemacht zu werden, sondern nur für authentifizierte Benutzer. Benutzerkonten können vom Seiteninhaber über die Befehlszeile oder die Weboberfläche erstellt werden, oder durch Selbstregistrierung und anschließender Genehmigung durch den Seiteninhaber.

## Benutzerrollen

Die folgenden Benutzerrollen sind derzeit definiert.

Rolle | Rollen-ID | Berechtigungen
-----|---------|------------
Gast | 0 | Nicht-private Objekte anzeigen
Mitglied | 1 | Gast + private Objekte anzeigen
Mitwirkender* | 2 | Mitglied + Objekte hinzufügen
Redakteur | 3 | Mitwirkender + Objekte bearbeiten und löschen
Besitzer | 4 | Redakteur + Benutzer verwalten
Admin | 5 | Besitzer + andere Bäume in einer Multi-Baum-Konfiguration bearbeiten

\* Bitte beachten Sie, dass die Rolle "Mitwirkender" derzeit nur teilweise unterstützt wird; z.B. können Familienobjekte nicht hinzugefügt werden, da sie eine Modifikation der zugrunde liegenden Gramps-Personenobjekte von Familienmitgliedern implizieren. Es wird empfohlen, die anderen Rollen wann immer möglich zu verwenden.

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

Der `COMMAND` kann `add` oder `delete` sein. Verwenden Sie `--help` für `[ARGS]`, um die Syntax und mögliche Konfigurationsoptionen anzuzeigen.

### Genehmigung von selbstregistrierten Benutzern

Wenn sich ein Benutzer selbst registriert, erhält er nicht sofort Zugriff. Eine E-Mail wird an den Baum-Besitzer über die neue Benutzerregistrierung gesendet, und der Benutzer erhält eine E-Mail-Anfrage zur Bestätigung seiner E-Mail-Adresse. Die erfolgreiche Bestätigung der E-Mail-Adresse ändert die Rolle des Benutzers von `unconfirmed` zu `disabled`. Solange sich das Benutzerkonto in einer dieser beiden Rollen befindet, kann sich der Benutzer nicht anmelden. Der Baum-Besitzer muss die Anfrage des Benutzers überprüfen und dem Benutzer eine geeignete Rolle zuweisen, bevor er sich anmelden darf.
