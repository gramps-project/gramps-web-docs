# Benutzer verwalten

Die Benutzerverwaltungsoberfläche ist über **Einstellungen > Benutzer verwalten** (das Benutzersymbol in der oberen App-Leiste) erreichbar. Sie ist nur für Benutzer mit der Rolle „Besitzer“ oder „Administrator“ verfügbar.

## Benutzerrollen

Eine vollständige Beschreibung der verfügbaren Benutzerrollen und ihrer Berechtigungen findest du unter [Benutzersystem](../install_setup/users.md). Der wichtigste Unterschied zwischen Gästen und Mitgliedern besteht darin, dass Gäste [private Datensätze](../user-guide/privacy.md) nicht sehen können. Wähle die Rolle daher zusammen mit der Einstellung aus, welche Datensätze du als privat markierst.

## Benutzer anzeigen und filtern

Auf der Seite zur Benutzerverwaltung wird eine Tabelle mit allen registrierten Benutzerkonten und den folgenden Spalten angezeigt:

- **Benutzername** – der Anmeldename
- **Vollständiger Name** – der Anzeigename
- **E-Mail** – die E-Mail-Adresse des Benutzers
- **Rolle** – die zugewiesene Rolle (Gast, Mitglied, Mitwirkender, Bearbeiter, Besitzer oder Administrator)
- **Kontenquelle** – entweder „Passwort“ (lokales Konto) oder der Name eines externen Identitätsanbieters (z. B. bei Verwendung von OIDC)

Verwende das Suchfeld und das Rollen-Drop-down oben in der Tabelle, um die Liste zu filtern. Klicke auf die Schaltfläche zum Löschen der Filter, um alle Filter zurückzusetzen.

## Einen Benutzer bearbeiten

Klicke in einer beliebigen Zeile auf das Bearbeitungssymbol (Stift), um den Bearbeitungsdialog zu öffnen. Du kannst Folgendes am Benutzer ändern:

- Vollständiger Name
- E-Mail-Adresse
- Rolle

Dies ist die wichtigste Möglichkeit, um einen **neu selbstregistrierten Benutzer zu aktivieren**: Ändere dessen Rolle von *deaktiviert* in eine beliebige aktive Rolle (z. B. Mitglied oder Bearbeiter).

E-Mail-Adressen müssen nicht eindeutig sein (seit Gramps Web API 3.22), sodass mehrere Konten dieselbe Adresse verwenden können.

Wenn du einen Benutzer deaktivierst oder sein Passwort änderst, werden alle seine Sitzungen innerhalb von 15 Minuten beendet.

!!! note
    Besitzer können keine Benutzer mit einer höheren Rolle, wie z. B. den Website-Administrator, bearbeiten, deren Passwort ändern oder sie löschen. Benutzer mit derselben Rolle, z. B. zwei Besitzer eines Stammbaums, können sich gegenseitig verwalten.

## Einen Benutzer manuell hinzufügen

Klicke oberhalb der Tabelle auf das Symbol **Benutzer hinzufügen** (Person-mit-Plus-Symbol), um direkt ein neues Benutzerkonto zu erstellen, ohne eine Selbstregistrierung zu benötigen. Gib im Dialog den Benutzernamen, den vollständigen Namen, die E-Mail-Adresse, das Passwort und die Rolle ein und klicke auf **Speichern**.

## Einen Benutzer löschen

Klicke in einer beliebigen Zeile auf das Löschsymbol (Papierkorb) und bestätige den Dialog. Diese Aktion kann nicht rückgängig gemacht werden.

!!! note
    Damit ein Stammbaum nicht ohne jemanden bleibt, der ihn verwalten kann, kannst du deine eigene Rolle nicht unter „Besitzer“ herabstufen und dein eigenes Konto nicht löschen, wenn du der einzige Besitzer oder Administrator des Stammbaums bist. Befördere zuerst einen anderen Benutzer zum Besitzer. Ein Administrator kann den letzten Besitzer des Stammbaums eines anderen Benutzers weiterhin ändern oder entfernen, da er einen neuen Besitzer ernennen kann.

## Benutzerkonten exportieren und importieren

Diese Schaltflächen sind nützlich, wenn du [zu einer anderen Gramps-Web-Instanz migrierst](export.md).

- **Benutzerdetails exportieren** (Downloadsymbol) – lädt eine JSON-Datei mit allen Benutzerkonten herunter (ohne Passwörter, da Passwörter in verschlüsselter Form gespeichert werden).
- **Benutzerkonten importieren** (Symbol „Gruppe hinzufügen“) – lädt eine zuvor exportierte JSON-Datei hoch, um Benutzerkonten gesammelt zu erstellen. Alle importierten Benutzer müssen über den Link „Passwort vergessen“ ein neues Passwort festlegen, da Passwörter nicht übertragen werden können.

## Registrierungslink (nur Einrichtung mit mehreren Stammbäumen)

Bei einer Einrichtung mit mehreren Stammbäumen wird der Registrierungslink für neue Benutzer oben auf der Seite zur Benutzerverwaltung angezeigt. Du kannst diesen Link kopieren und mit Personen teilen, die du zur Registrierung eines Kontos in deinem Stammbaum einladen möchtest.

!!! note
    Bei einer Einrichtung mit nur einem Stammbaum gibt es auf der Anmeldeseite einen allgemeinen Link „Registrieren“. Der Registrierungslink pro Stammbaum wird nur bei Installationen mit mehreren Stammbäumen benötigt.

## Berechtigungen für den KI-Chat

Wenn der KI-Chat auf dem Server aktiviert wurde, kannst du über ein Drop-down oben auf der Seite festlegen, welche Benutzerrollen die Chat-Funktion verwenden dürfen:

- Alle (einschließlich Gästen)
- Mitglied und höher
- Mitwirkender und höher
- Bearbeiter und höher
- Nur Besitzer und Administratoren
- Niemand (Chat für alle Benutzer deaktivieren)
