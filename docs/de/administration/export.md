## Sichern Sie Ihren Stammbaum

Baum-Eigentümer können vollständige Backups des Baums – einschließlich seiner Einstellungen und Benutzer – im Abschnitt [Backups](settings.md#backups) der Administrations-Einstellungen erstellen, herunterladen und wiederherstellen.

Alternativ können Sie, um nur ein Backup der Familienstammdaten zu erstellen, die Export-Seite in Gramps Web öffnen und das Gramps XML-Format auswählen.

Ein Klick auf "exportieren" generiert die Datei und startet den Download, sobald sie bereit ist.

Beachten Sie, dass, wenn Ihr Gramps Web-Benutzer keine Berechtigung hat, private Datensätze anzuzeigen, der Export kein vollständiges Backup sein wird, da er keine privaten Datensätze enthalten wird.

Diese Gramps XML-Datei kann später verwendet werden, um den Baum über [Wiederherstellung aus Backup](settings.md#restore-from-backup) in diesen genauen Zustand wiederherzustellen.

## Teilen Sie Ihren Stammbaum mit Benutzern anderer Genealogie-Programme

Wenn das Teilen genealogischer Daten als Gramps XML keine Option ist, können Sie auch eine GEDCOM-Datei exportieren. Beachten Sie, dass dies nicht als Backup Ihres Gramps Web-Baums geeignet ist.

## Sichern Sie Ihre Mediendateien

Um Ihre Mediendateien zu sichern, können Sie ein ZIP-Archiv aller Mediendateien auf der Export-Seite erstellen und herunterladen.

Beachten Sie, dass dies, insbesondere bei großen Bäumen, eine kostspielige Operation für den Server sein kann und nur durchgeführt werden sollte, wenn es unbedingt notwendig ist. Aus diesem Grund ist die Anzahl der erstellbaren Medienarchive begrenzt (standardmäßig auf eines pro Stunde). Wenn Sie das Limit erreichen, wird dies durch eine Fehlermeldung angezeigt.

Eine bessere Option, um Ihre Mediendateien regelmäßig zu sichern, ist die Verwendung des [Gramps Web Sync-Addons](sync.md) (das selbst keine Backup-Lösung ist) und die Erstellung inkrementeller Backups auf Ihrem lokalen Computer.

In beiden Fällen, wenn Ihr Gramps Web-Benutzer keine Berechtigung hat, private Datensätze anzuzeigen, wird der Export keine Dateien privater Medienobjekte enthalten.

## Wechsel zu einer anderen Gramps Web-Instanz

Gramps Web bindet Sie nicht an einen bestimmten Anbieter und Sie können jederzeit zu einer anderen Gramps Web-Instanz wechseln, ohne Daten zu verlieren und ohne direkten Zugriff auf einen der Server zu haben.

Um eine vollständige Migration zu erreichen, befolgen Sie diese Schritte (vorausgesetzt, Sie haben die Berechtigungen eines Baum-Eigentümers):

1. Gehen Sie zur Export-Seite und exportieren Sie Ihren Baum als Gramps XML (`.gramps`) Datei. Wenn Sie das [Sync-Addon](sync.md) verwenden, können Sie den Export auch in Gramps Desktop generieren.
2. Generieren und laden Sie auf der Export-Seite ein Medienarchiv herunter. Wenn Sie das [Sync-Addon](sync.md) verwenden, können Sie auch einfach Ihren lokalen Gramps-Medienordner ZIPpen.
3. Gehen Sie zu Einstellungen > Verwaltung > Benutzer verwalten und klicken Sie auf die Schaltfläche "Benutzerdetails exportieren". Es wird eine JSON-Datei heruntergeladen.
4. Öffnen Sie in der neuen Gramps Web-Instanz die Import-Seite. Importieren Sie die in Schritt 1 exportierte `.gramps` Datei.
5. Laden Sie auf der Import-Seite der neuen Gramps Web-Instanz das Medienarchiv (ZIP) hoch.
6. Gehen Sie zu Einstellungen > Verwaltung > Benutzer der neuen Gramps Web-Instanz verwalten. Klicken Sie auf die Schaltfläche "Benutzerkonten importieren" und laden Sie die in Schritt 3 heruntergeladene JSON-Datei hoch.

Beachten Sie, dass, während Ihre Benutzerkonten migriert werden, alle Ihre Benutzer neue Passwörter festlegen müssen, indem sie den Link "Passwort vergessen" verwenden, da Passwörter in verschlüsselter Form gespeichert werden und nicht exportiert werden können.
