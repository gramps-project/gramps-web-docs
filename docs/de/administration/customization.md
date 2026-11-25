# Den Stammbaum anpassen

Stammbaumbesitzer und Administratoren können den Namen und das Erscheinungsbild des Stammbaums sowie dessen Startseite für alle Benutzer anpassen. Diese Einstellungen befinden sich in den Abschnitten **Stammbau-Einstellungen** und **Anpassung** der [Administrationseinstellungen](settings.md).

## Name des Familienstammbaums

!!! note
    Das Umbenennen des Stammbaums funktioniert nur in einer [Konfiguration mit mehreren Stammbäumen](../install_setup/multi-tree.md) oder wenn `TREE_ID` in der [Serverkonfiguration](../install_setup/configuration.md) ausdrücklich festgelegt ist. Bei einer standardmäßigen Installation mit nur einem Stammbaum, bei der `TREE_ID` nicht festgelegt ist, führt dies zu einem Fehler.

Damit kannst du den Namen der zugrunde liegenden Gramps-Familienstammbaumdatenbank ändern. Gib einen neuen Namen ein und klicke auf **Umbenennen**, um die Änderung anzuwenden.

!!! tip
    Wenn du nur den in der App-Leiste angezeigten Namen ändern möchtest, ohne die Datenbank umzubenennen, verwende stattdessen die Einstellung [App-Titel](#app-title).

## Informationen zum Forscher

Lege den Namen, die Adresse und die Kontaktdaten des Hauptforschers fest. Diese Informationen werden in Exporte eingebettet (z. B. GEDCOM-Dateien).

## Designfarben

Lege eine benutzerdefinierte **Primärfarbe** und **Akzentfarbe** für die Gramps-Web-Oberfläche fest. Diese Farben werden auf alle Benutzer dieses Stammbaums angewendet und sind unmittelbar nach dem Speichern wirksam.

Verwende die Farbauswahl, um Farben auszuwählen, und klicke anschließend auf **Speichern**. Klicke auf **Zurücksetzen**, um die Standardwerte wiederherzustellen.

## App-Titel

Lege einen benutzerdefinierten Titel für die Anwendung fest. Wenn dieser festgelegt ist, überschreibt er den Namen des Familienstammbaums in der Titelleiste des Browsers und in der oberen App-Leiste.

Gib einen Titel ein und klicke auf **Speichern**. Lass das Feld leer, um den Standardwert (den Namen des Familienstammbaums) zu verwenden.

## Hinweis auf der Startseite

Wähle ein Gramps-Objekt vom Typ **Notiz** aus, das auf der Startseite des Dashboards angezeigt werden soll. Der Inhalt der Notiz wird unterhalb der Hauptspalten des Dashboards dargestellt und ist für alle Benutzer sichtbar, die Zugriff auf den Stammbaum haben.

Verwende die Objektauswahl, um nach einer Notiz zu suchen und sie auszuwählen, und speichere anschließend. Klicke auf **Entfernen**, um den aktuellen Hinweis auf der Startseite zu löschen.

## Bild auf der Startseite

Wähle ein Gramps-Objekt vom Typ **Medium** aus, das als Bild auf der Startseite des Dashboards angezeigt werden soll. In Kombination mit einem Hinweis auf der Startseite wird das Bild neben dem Text des Hinweises angezeigt. Ohne Hinweis wird nur das Bild angezeigt.

Verwende die Objektauswahl, um nach einem Medienobjekt zu suchen und es auszuwählen, und speichere anschließend. Klicke auf **Entfernen**, um das aktuelle Bild auf der Startseite zu löschen.

## Einstellungen exportieren/importieren

Einstellungen auf Stammbaumebene (App-Titel, Designfarben, Hinweis/Bild auf der Startseite usw.) können als JSON-Datei zur Sicherung oder zum Kopieren in eine andere Gramps-Web-Instanz exportiert werden.

- Klicke auf **Einstellungen exportieren**, um die aktuellen Einstellungen als JSON-Datei herunterzuladen.
- Klicke auf **Stammbaum-Einstellungen importieren**, um eine zuvor exportierte JSON-Datei hochzuladen und die Einstellungen anzuwenden.
