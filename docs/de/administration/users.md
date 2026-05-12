# Benutzer verwalten

Die Benutzerverwaltungsoberfläche ist über **Einstellungen > Benutzer verwalten** (das Benutzersymbol in der oberen App-Leiste) zugänglich. Sie ist nur für Benutzer mit der Rolle Eigentümer oder Administrator verfügbar.

## Benutzerrollen

Siehe [Benutzersystem](../install_setup/users.md) für eine vollständige Beschreibung der verfügbaren Benutzerrollen und deren Berechtigungen.

## Benutzer anzeigen und filtern

Die Seite "Benutzer verwalten" zeigt eine Tabelle aller registrierten Benutzerkonten mit den folgenden Spalten:

- **Benutzername** — der Anmeldename
- **Vollständiger Name** — der Anzeigename
- **E-Mail** — die E-Mail-Adresse des Benutzers
- **Rolle** — die zugewiesene Rolle (Gast, Mitglied, Mitwirkender, Redakteur, Eigentümer oder Administrator)
- **Kontenquelle** — entweder "Passwort" (lokales Konto) oder der Name eines externen Identitätsanbieters (z. B. bei Verwendung von OIDC)

Verwenden Sie das Suchfeld und das Rollenauswahlfeld oben in der Tabelle, um die Liste zu filtern. Klicken Sie auf die Schaltfläche zum Zurücksetzen der Filter, um alle Filter zurückzusetzen.

## Benutzer bearbeiten

Klicken Sie auf das Bearbeiten (Stift)-Symbol in einer beliebigen Zeile, um den Bearbeitungsdialog zu öffnen. Sie können die folgenden Informationen des Benutzers ändern:

- Vollständiger Name
- E-Mail-Adresse
- Rolle

Dies ist der primäre Weg, um **einen neu selbst registrierten Benutzer zu aktivieren**: Ändern Sie seine Rolle von *deaktiviert* zu einer aktiven Rolle (z. B. Mitglied oder Redakteur).

## Benutzer manuell hinzufügen

Klicken Sie auf das **Benutzer hinzufügen** (Person hinzufügen)-Symbol über der Tabelle, um ein neues Benutzerkonto direkt zu erstellen, ohne eine Selbstregistrierung zu benötigen. Füllen Sie im Dialogfeld den Benutzernamen, den vollständigen Namen, die E-Mail-Adresse, das Passwort und die Rolle aus und klicken Sie auf **Speichern**.

## Benutzer löschen

Klicken Sie auf das Löschen (Müll)-Symbol in einer beliebigen Zeile und bestätigen Sie den Dialog. Diese Aktion kann nicht rückgängig gemacht werden.

## Benutzerkonten exportieren und importieren

Diese Schaltflächen sind nützlich beim [Migrieren zu einer anderen Gramps Web-Instanz](export.md).

- **Benutzerdetails exportieren** (Download-Symbol) — lädt eine JSON-Datei herunter, die alle Benutzerkonten enthält (ohne Passwörter, da Passwörter in verschlüsselter Form gespeichert werden).
- **Benutzerkonten importieren** (Gruppe hinzufügen-Symbol) — lädt eine zuvor exportierte JSON-Datei hoch, um Benutzerkonten in großen Mengen zu erstellen. Alle importierten Benutzer müssen ein neues Passwort über den Link "Passwort vergessen" festlegen, da Passwörter nicht übertragen werden können.

## Registrierungslink (nur Mehrbaum-Setup)

In einem Mehrbaum-Setup wird der Registrierungslink für neue Benutzer oben auf der Seite "Benutzer verwalten" angezeigt. Sie können diesen Link kopieren und mit Personen teilen, die Sie einladen möchten, ein Konto auf Ihrem Baum zu registrieren.

!!! Hinweis
    In einem Einzelbaum-Setup gibt es einen generischen "Registrieren"-Link auf der Anmeldeseite; der pro-Baum-Registrierungslink wird nur in Mehrbaum-Installationen benötigt.

## AI-Chat-Berechtigungen

Wenn der AI-Chat auf dem Server aktiviert wurde, können Sie über ein Dropdown-Menü oben auf der Seite steuern, welche Benutzerrollen berechtigt sind, die Chat-Funktion zu nutzen:

- Jeder (einschließlich Gäste)
- Mitglieder und höher
- Mitwirkende und höher
- Redakteure und höher
- Nur Eigentümer und Administratoren
- Niemand (Chat für alle Benutzer deaktivieren)
