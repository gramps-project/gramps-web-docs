# Benutzersystem

Gramps Web ist nicht dafür vorgesehen, für den öffentlichen Zugriff im Internet verfügbar zu sein, sondern nur für authentifizierte Benutzer. Benutzerkonten können vom Eigentümer der Website über die Befehlszeile oder die Weboberfläche erstellt werden oder durch Selbstregistrierung und anschließende Genehmigung durch den Eigentümer der Website.

## Benutzerrollen

Die folgenden Benutzerrollen sind derzeit definiert.

Rolle | Rollen-ID | Berechtigungen
-----|---------|------------
Gast | 0 | Nicht-private Objekte anzeigen
Mitglied | 1 | Gast + private Objekte anzeigen
Beitragender* | 2 | Mitglied + Objekte hinzufügen
Bearbeiter | 3 | Beitragender + Objekte bearbeiten und löschen
Eigentümer | 4 | Bearbeiter + Benutzer verwalten
Administrator | 5 | Eigentümer + andere Stammbäume in einer Umgebung mit mehreren Stammbäumen bearbeiten

Ob ein Datensatz privat ist, wird pro Datensatz festgelegt; siehe [Private Datensätze](../user-guide/privacy.md). Standardmäßig ist nichts privat, auch nicht lebende Personen.

\* Beachte, dass die Rolle „Beitragender“ derzeit nur teilweise unterstützt wird. Beispielsweise können Familienobjekte nicht hinzugefügt werden, da dies eine Änderung der zugrunde liegenden Gramps-Personenobjekte der Familienmitglieder voraussetzt. Es wird empfohlen, nach Möglichkeit die anderen Rollen zu verwenden.

## Konfigurieren, wer den KI-Chat verwenden darf

Wenn du den [KI-Chat konfiguriert](chat.md) hast, wird hier eine Option angezeigt, mit der du auswählen kannst, welche Benutzergruppen die Chat-Funktion verwenden dürfen.

## Benutzer verwalten

Es gibt zwei Möglichkeiten, Benutzer zu verwalten:

- Mit Eigentümerberechtigungen über die Weboberfläche
- Über die Befehlszeile auf dem Server

Das Eigentümerkonto, das für den erstmaligen Zugriff auf die Webanwendung erforderlich ist, kann im Einrichtungsassistenten hinzugefügt werden, der automatisch gestartet wird, wenn auf Gramps Web mit einer leeren Benutzerdatenbank zugegriffen wird.

### Benutzer über die Befehlszeile verwalten

Bei Verwendung von [Docker Compose](deployment.md) lautet der grundlegende Befehl

```bash
docker compose run grampsweb python3 -m gramps_webapi user COMMAND [ARGS]
```

`COMMAND` kann `add`, `set-password` oder `delete` sein. Verwende `--help` für `[ARGS]`, um die Syntax und mögliche Konfigurationsoptionen anzuzeigen.

`set-password NAME` legt ein neues Passwort für einen vorhandenen Benutzer fest, ohne dass das alte benötigt wird, beispielsweise wenn sich niemand mehr anmelden kann und keine E-Mail für das Zurücksetzen von Passwörtern eingerichtet ist (Gramps Web API 3.26+). Du wirst zweimal nach dem Passwort gefragt, ohne dass es angezeigt wird, sodass das Passwort nicht im Shell-Verlauf landet. Alle Sitzungen des Benutzers werden beendet.

### Selbstregistrierte Benutzer genehmigen

Wenn sich ein Benutzer selbst registriert, erhält er nicht sofort Zugriff. Der Eigentümer des Stammbaums erhält eine E-Mail über die neue Benutzerregistrierung, und der Benutzer erhält eine E-Mail mit der Aufforderung, seine E-Mail-Adresse zu bestätigen. Durch die erfolgreiche Bestätigung seiner E-Mail-Adresse wird seine Rolle von `unconfirmed` in `disabled` geändert. Solange sich das Benutzerkonto in einer dieser beiden Rollen befindet, kann sich der Benutzer nicht anmelden. Der Eigentümer des Stammbaums muss die Anfrage des Benutzers prüfen und ihm eine geeignete Rolle zuweisen, bevor er sich anmelden darf.
