# Benutzer verwalten

Die Benutzerverwaltungsoberfläche ist über **Einstellungen > Benutzer verwalten** (das Benutzersymbol in der oberen App-Leiste) zugänglich. Sie ist nur für Benutzer mit der Rolle Eigentümer oder Administrator verfügbar.

## Benutzerrollen

Siehe [Benutzersystem](../install_setup/users.md) für eine vollständige Beschreibung der verfügbaren Benutzerrollen und deren Berechtigungen. Der Hauptunterschied zwischen Gästen und Mitgliedern besteht darin, dass Gäste keine [privaten Datensätze](../user-guide/privacy.md) sehen können, wählen Sie also die Rolle zusammen mit dem, was Sie als privat markieren.

## Benutzer anzeigen und filtern

Die Seite Benutzer verwalten zeigt eine Tabelle aller registrierten Benutzerkonten mit den folgenden Spalten:

- **Benutzername** – der Anmeldename
- **Vollständiger Name** – der Anzeigename
- **E-Mail** – die E-Mail-Adresse des Benutzers
- **Rolle** – die zugewiesene Rolle (Gast, Mitglied, Mitwirkender, Redakteur, Eigentümer oder Administrator)
- **Kontenquelle** – entweder "Passwort" (lokales Konto) oder der Name eines externen Identitätsanbieters (z. B. bei Verwendung von OIDC)

Verwenden Sie das Suchfeld und das Rollenauswahlfeld oben in der Tabelle, um die Liste zu filtern. Klicken Sie auf die Schaltfläche zum Zurücksetzen der Filter, um alle Filter zurückzusetzen.

## Benutzer bearbeiten

Klicken Sie auf das Bearbeiten (Bleistift)-Symbol in einer beliebigen Zeile, um den Bearbeitungsdialog zu öffnen. Sie können die folgenden Informationen des Benutzers ändern:

- Vollständiger Name
- E-Mail-Adresse
- Rolle

Dies ist der primäre Weg, um **einen neu selbstregistrierten Benutzer zu aktivieren**: Ändern Sie seine Rolle von *deaktiviert* zu einer aktiven Rolle (z. B. Mitglied oder Redakteur).

E-Mail-Adressen müssen nicht einzigartig sein (seit Gramps Web API 3.22), sodass mehrere Konten dieselbe Adresse teilen können.

Das Deaktivieren eines Benutzers oder das Ändern seines Passworts beendet alle seine Sitzungen innerhalb von 15 Minuten.

!!! Hinweis
    Eigentümer können Benutzer mit einer höheren Rolle, wie den Site-Administrator, nicht bearbeiten, das Passwort ändern oder löschen. Benutzer mit derselben Rolle, wie zwei Eigentümer eines Baums, können sich gegenseitig verwalten.

## Benutzer manuell hinzufügen

Klicken Sie auf das **Benutzer hinzufügen** (person-add)-Symbol über der Tabelle, um ein neues Benutzerkonto direkt zu erstellen, ohne dass eine Selbstregistrierung erforderlich ist. Füllen Sie im Dialogfeld den Benutzernamen, den vollständigen Namen, die E-Mail-Adresse, das Passwort und die Rolle aus und klicken Sie auf **Speichern**.

## Benutzer löschen

Klicken Sie auf das Löschen (Mülltonne)-Symbol in einer beliebigen Zeile und bestätigen Sie den Dialog. Diese Aktion kann nicht rückgängig gemacht werden.

!!! Hinweis
    Um zu verhindern, dass ein Baum ohne jemanden bleibt, der ihn verwalten kann, können Sie Ihre eigene Rolle nicht unter Eigentümer herabsetzen oder Ihr eigenes Konto löschen, wenn Sie der einzige Eigentümer oder Administrator des Baums sind. Befördern Sie zuerst einen anderen Benutzer zum Eigentümer. Ein Administrator kann weiterhin den letzten Eigentümer eines Baums eines anderen Benutzers ändern oder entfernen, da er einen neuen ernennen kann.

## Benutzerkonten exportieren und importieren

Diese Schaltflächen sind nützlich, wenn Sie [zu einer anderen Gramps Web-Instanz migrieren](export.md).

- **Benutzerdetails exportieren** (Download-Symbol) – lädt eine JSON-Datei herunter, die alle Benutzerkonten enthält (ohne Passwörter, da Passwörter in verschlüsselter Form gespeichert werden).
- **Benutzerkonten importieren** (Gruppen hinzufügen-Symbol) – lädt eine zuvor exportierte JSON-Datei hoch, um Benutzerkonten in großen Mengen zu erstellen. Alle importierten Benutzer müssen ein neues Passwort über den Link "Passwort vergessen" festlegen, da Passwörter nicht übertragen werden können.

## Registrierungslink (nur bei Mehrbaum-Setup)

In einem Mehrbaum-Setup wird der Registrierungslink für neue Benutzer oben auf der Seite Benutzer verwalten angezeigt. Sie können diesen Link kopieren und mit Personen teilen, die Sie einladen möchten, ein Konto auf Ihrem Baum zu registrieren.

!!! Hinweis
    In einem Einbaum-Setup gibt es einen generischen "Registrieren"-Link auf der Anmeldeseite; der registrierungsspezifische Link pro Baum wird nur in Mehrbaum-Installationen benötigt.

## AI-Chat-Berechtigungen

Wenn der AI-Chat auf dem Server aktiviert wurde, können Sie über ein Dropdown-Menü oben auf der Seite steuern, welche Benutzerrollen die Chat-Funktion nutzen dürfen:

- Jeder (einschließlich Gäste)
- Mitglied und höher
- Mitwirkender und höher
- Redakteur und höher
- Nur Eigentümer und Administratoren
- Niemand (Chat für alle Benutzer deaktivieren)
