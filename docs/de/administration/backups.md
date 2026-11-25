# Sichern und Wiederherstellen

Besitzer von Stammbäumen können im Abschnitt **Sicherungen** der [Administrationseinstellungen](settings.md) Sicherungen des Stammbaums erstellen, herunterladen und wiederherstellen.

Eine Sicherung enthält die Daten des Stammbaums einschließlich privater Datensätze, die Einstellungen des Stammbaums und die Benutzer des Stammbaums. Mediendateien sind nicht enthalten; siehe [Mediendateien sichern](export.md#back-up-your-media-files).

## Gespeicherte Sicherungen

Wenn der Serveradministrator ein Sicherungsverzeichnis (`BACKUP_DIR`, siehe [Serverkonfiguration](../install_setup/configuration.md)) festgelegt hat, können Sicherungen auf dem Server gespeichert werden. Andernfalls wird in diesem Abschnitt ein Hinweis angezeigt, dass das Speichern von Sicherungen nicht konfiguriert ist, und es ist nur die Wiederherstellung aus einer hochgeladenen Datei verfügbar.

Klicke auf **Sicherung erstellen ...**, um eine Sicherung zu erstellen. Sie wird als Hintergrundaufgabe erstellt und erscheint anschließend in der Liste der gespeicherten Sicherungen mit ihrem Datum, der Anzahl der Personen und ihrer Größe. Der Server behält nur die neuesten Sicherungen (standardmäßig fünf) und löscht ältere automatisch. Auch die Anzahl der Sicherungen, die pro Tag erstellt werden können, ist begrenzt.

Für jede gespeicherte Sicherung kannst du:

- sie als `.tar`-Datei **herunterladen**, zum Beispiel um anderswo eine Kopie aufzubewahren.
- sie wie unten beschrieben **wiederherstellen**.
- sie nach einer Bestätigung **löschen**.

Eine Sicherung, die mit einer neueren Version von Gramps Web als der auf dem Server ausgeführten erstellt wurde, ist mit einem Warnsymbol gekennzeichnet und kann nicht wiederhergestellt werden.

## Aus Sicherung wiederherstellen

Stellt den Stammbaum aus einer gespeicherten Sicherung oder einer hochgeladenen Datei wieder her. Um eine gespeicherte Sicherung wiederherzustellen, klicke auf die Wiederherstellungsschaltfläche daneben. Um eine Datei wiederherzustellen, wähle eine Gramps-Web-Sicherung (`.tar`) oder eine Gramps-XML-Datei (`.gramps`) aus und klicke auf **Wiederherstellen**.

!!! danger
    Das Wiederherstellen der Daten ist ein destruktives Ersetzen, keine Zusammenführung. Jedes vorhandene Objekt, das nicht in der Sicherung enthalten ist, wird gelöscht.

Bei einer Gramps-Web-Sicherung wird in einem Dialog angezeigt, wann die Sicherung erstellt wurde, für welchen Stammbaum und mit welcher Version. Außerdem kannst du auswählen, welche Teile wiederhergestellt werden sollen:

- **Daten** – die Objekte des Stammbaums
- **Stammeinstellungen** – die Einstellungen der Administrationsseite, z. B. Designfarben, App-Titel und Notiz der Startseite
- **Benutzer** – die Benutzer des Stammbaums

Klicke auf **Vorschau**, um zu sehen, was durch die Wiederherstellung geändert würde. Eine Gramps-XML-Datei enthält nur Daten. Daher beginnt die Vorschau bei einer solchen Datei sofort. Du wirst aufgefordert, dich erneut zu authentifizieren, wenn deine Sitzung nicht mehr aktuell genug ist. Die Vorschau wird als Hintergrundaufgabe ausgeführt und öffnet nach Abschluss einen Dialog, der die Änderungen nach Objekttyp zusammenfasst (Personen, Familien, Ereignisse, Orte, Zitate, Quellen, Repositorien, Medienobjekte, Notizen, Etiketten) sowie für die Stammeinstellungen und Benutzer, falls ausgewählt:

- **Hinzufügen** – Objekte, die in der Sicherung vorhanden sind, aber im aktuellen Stammbaum fehlen
- **Aktualisieren** – Objekte, die in beiden vorhanden sind, sich aber unterscheiden
- **Löschen** – Objekte im aktuellen Stammbaum, die in der Sicherung fehlen
- **Unverändert** – Objekte, die in beiden identisch sind

Wenn Objekte gelöscht würden, warnt der Dialog mit der entsprechenden Anzahl. Überprüfe die Zusammenfassung und klicke dann auf **Wiederherstellen**, um die Änderungen anzuwenden, oder auf **Abbrechen**, um den Vorgang abzubrechen.

Nach der Wiederherstellung werden die aus der Sicherung hinzugefügten Benutzer aufgelistet. Sie erhalten ein zufälliges Passwort und müssen ihr Passwort daher zurücksetzen, bevor sie sich anmelden können. Benutzer, die bereits auf dem Server vorhanden sind, werden niemals geändert. Medienobjekte, deren Dateien auf dem Server fehlen, werden ebenfalls aufgelistet; lade sie über [Mediendateien importieren](import-media.md) hoch.

!!! note
    Beim Wiederherstellen von Daten werden nur Objektdaten und Medienreferenzen wiederhergestellt. Die binären Mediendateien selbst sowie Metadaten des Stammbaums (Standardperson, Lesezeichen, Namensgruppen) werden nicht beeinflusst.

!!! tip
    Verwende dies, um einen Stammbaum auf eine bekannte funktionierende Sicherung zurückzusetzen, beispielsweise nach einem fehlerhaften Import oder einer unerwünschten Massenbearbeitung.

## Gramps XML als Sicherung

Wenn das Speichern von Sicherungen nicht verfügbar ist oder du nur eine Kopie der Stammbaumdaten aufbewahren möchtest, [exportiere](export.md) den Stammbaum als Gramps XML. Eine solche Datei kann ebenfalls über [Aus Sicherung wiederherstellen](#restore-from-backup) wiederhergestellt werden.

Beachte, dass der Export keine vollständige Sicherung darstellt, wenn dein Gramps-Web-Benutzer nicht die Berechtigung zum Anzeigen privater Datensätze hat, da er keine privaten Datensätze enthalten wird.
