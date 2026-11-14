# Backup und Wiederherstellung

Baum-Eigentümer können im Abschnitt **Backups** der [Administrations-Einstellungen](settings.md) Backups des Baums erstellen, herunterladen und wiederherstellen.

Ein Backup enthält die Daten des Stammbaums, einschließlich privater Datensätze, der Baumeinstellungen und der Benutzer des Baums. Mediendateien sind nicht enthalten; siehe [Sichern Sie Ihre Mediendateien](export.md#back-up-your-media-files).

## Gespeicherte Backups

Wenn der Serveradministrator ein Backup-Verzeichnis (`BACKUP_DIR`, siehe [Serverkonfiguration](../install_setup/configuration.md)) festgelegt hat, können Backups auf dem Server gespeichert werden. Andernfalls zeigt der Abschnitt eine Mitteilung an, dass das Speichern von Backups nicht konfiguriert ist und nur die Wiederherstellung aus einer hochgeladenen Datei verfügbar ist.

Klicken Sie auf **Backup erstellen...**, um ein Backup zu erstellen. Es wird als Hintergrundaufgabe erstellt und erscheint dann in der Liste der gespeicherten Backups mit Datum, Anzahl der Personen und Größe. Der Server behält nur die neuesten Backups (standardmäßig fünf) und löscht ältere automatisch. Auch die Anzahl der Backups, die pro Tag erstellt werden können, ist begrenzt.

Für jedes gespeicherte Backup können Sie:

- **Herunterladen** als `.tar`-Datei, zum Beispiel um eine Kopie an einem anderen Ort aufzubewahren.
- **Wiederherstellen**, wie unten beschrieben.
- **Löschen**, nach Bestätigung.

Ein Backup, das mit einer neueren Version von Gramps Web als der auf dem Server laufenden erstellt wurde, ist mit einem Warnsymbol gekennzeichnet und kann nicht wiederhergestellt werden.

## Wiederherstellung aus Backup

Stellt den Baum aus einem gespeicherten Backup oder aus einer hochgeladenen Datei wieder her. Um ein gespeichertes Backup wiederherzustellen, klicken Sie auf die Schaltfläche Wiederherstellen daneben. Um aus einer Datei wiederherzustellen, wählen Sie ein Gramps Web-Backup (`.tar`) oder eine Gramps XML-Datei (`.gramps`) aus und klicken Sie auf **Wiederherstellen**.

!!! danger
    Die Wiederherstellung der Daten ist ein destruktiver Ersatz, kein Merge. Jedes vorhandene Objekt, das im Backup nicht vorhanden ist, wird gelöscht.

Für ein Gramps Web-Backup wird ein Dialog angezeigt, der zeigt, wann das Backup erstellt wurde, für welchen Baum und mit welcher Version, und lässt Sie auswählen, welche Teile wiederhergestellt werden sollen:

- **Daten** – die Objekte des Stammbaums
- **Baumeinstellungen** – die Einstellungen der Administrationsseite, wie Farbthemen, App-Titel und Notiz auf der Startseite
- **Benutzer** – die Benutzer des Baums

Klicken Sie auf **Vorschau**, um zu sehen, was die Wiederherstellung ändern würde. Eine Gramps XML-Datei enthält nur Daten, sodass die Vorschau für eine solche Datei sofort beginnt. Sie werden aufgefordert, sich erneut zu authentifizieren, wenn Ihre Sitzung nicht frisch genug ist. Die Vorschau läuft als Hintergrundaufgabe und öffnet, sobald sie abgeschlossen ist, einen Dialog, der die Änderungen pro Objekttyp (Personen, Familien, Ereignisse, Orte, Zitationen, Quellen, Repositories, Medienobjekte, Notizen, Etiketten) sowie für die Baumeinstellungen und Benutzer, falls ausgewählt:

- **Hinzufügen** – Objekte, die im Backup vorhanden, aber im aktuellen Baum fehlen
- **Aktualisieren** – Objekte, die in beiden vorhanden sind, aber unterschiedlich sind
- **Löschen** – Objekte im aktuellen Baum, die im Backup fehlen
- **Unverändert** – Objekte, die in beiden identisch sind

Wenn Objekte gelöscht werden würden, warnt der Dialog, wie viele. Überprüfen Sie die Zusammenfassung und klicken Sie dann auf **Wiederherstellen**, um die Änderungen anzuwenden, oder auf **Abbrechen**, um abzubrechen.

Nach der Wiederherstellung werden die Benutzer, die aus dem Backup hinzugefügt wurden, aufgelistet. Sie erhalten ein zufälliges Passwort, sodass sie ihr Passwort zurücksetzen müssen, bevor sie sich anmelden können. Benutzer, die bereits auf dem Server existieren, werden niemals geändert. Medienobjekte, deren Dateien auf dem Server fehlen, werden ebenfalls aufgelistet; laden Sie sie über [Medien-Dateien importieren](import-media.md) hoch.

!!! note
    Die Wiederherstellung von Daten stellt nur die Objektdaten und Medienreferenzen wieder her. Binäre Mediendateien selbst und Baum-Metadaten (Standardperson, Lesezeichen, Namensgruppen) sind nicht betroffen.

!!! tip
    Verwenden Sie dies, um einen Baum auf ein bekannt gutes Backup zurückzusetzen, zum Beispiel nach einem schlechten Import oder einer unerwünschten Massenbearbeitung.

## Gramps XML als Backup

Wenn das Speichern von Backups nicht verfügbar ist oder Sie nur eine Kopie der Stammbaumdaten aufbewahren möchten, [exportieren](export.md) Sie den Baum als Gramps XML. Eine solche Datei kann ebenfalls über [Wiederherstellung aus Backup](#restore-from-backup) wiederhergestellt werden.

Bitte beachten Sie, dass, wenn Ihr Gramps Web-Benutzer keine Berechtigung hat, private Datensätze anzuzeigen, der Export kein vollständiges Backup sein wird, da er keine privaten Datensätze enthalten wird.
