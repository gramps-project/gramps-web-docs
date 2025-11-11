## Sichern Sie Ihren Stammbaum

Um ein Backup Ihres Stammbaums zu erstellen, öffnen Sie die Exportseite in Gramps Web und wählen Sie das Gramps XML-Format aus.

Ein Klick auf "exportieren" generiert die Datei und startet den Download, sobald sie bereit ist.

Bitte beachten Sie, dass, wenn Ihr Gramps Web-Benutzer keine Berechtigung hat, private Datensätze anzuzeigen, der Export kein vollständiges Backup sein wird, da er keine privaten Datensätze enthält.

## Teilen Sie Ihren Stammbaum mit Nutzern anderer Genealogie-Programme

Wenn das Teilen genealogischer Daten im Gramps XML-Format keine Option ist, können Sie auch eine GEDCOM-Datei exportieren. Bitte beachten Sie, dass dies nicht als Backup Ihres Gramps Web-Stammbaums geeignet ist.

## Sichern Sie Ihre Mediendateien

Um Ihre Mediendateien zu sichern, können Sie ein ZIP-Archiv aller Mediendateien auf der Exportseite erstellen und herunterladen.

Bitte beachten Sie, dass dies, insbesondere bei großen Bäumen, eine kostspielige Operation für den Server sein kann und nur durchgeführt werden sollte, wenn es unbedingt notwendig ist.

Eine bessere Option, um Ihre Mediendateien regelmäßig zu sichern, ist die Verwendung des [Gramps Web Sync-Addons](sync.md) (das selbst keine Backup-Lösung ist) und die Erstellung inkrementeller Backups auf Ihrem lokalen Computer.

In beiden Fällen, wenn Ihr Gramps Web-Benutzer keine Berechtigung hat, private Datensätze anzuzeigen, wird der Export keine Dateien privater Medienobjekte enthalten.

## Wechsel zu einer anderen Gramps Web-Instanz

Gramps Web bindet Sie nicht an einen bestimmten Anbieter, und Sie können jederzeit zu einer anderen Gramps Web-Instanz wechseln, ohne Daten zu verlieren und ohne direkten Zugriff auf einen der Server zu haben.

Um eine vollständige Migration zu erreichen, befolgen Sie diese Schritte (vorausgesetzt, Sie haben die Berechtigung als Baum-Eigentümer):

1. Gehen Sie zur Exportseite und exportieren Sie Ihren Baum als Gramps XML (`.gramps`) Datei. Wenn Sie das [Sync-Addon](sync.md) verwenden, können Sie den Export auch in Gramps Desktop generieren.
2. Erstellen und laden Sie auf der Exportseite ein Medienarchiv herunter. Wenn Sie das [Sync-Addon](sync.md) verwenden, können Sie auch einfach Ihren lokalen Gramps-Medienordner ZIP-en.
3. Gehen Sie zu Einstellungen > Verwaltung > Benutzer verwalten und klicken Sie auf die Schaltfläche "Benutzerdetails exportieren". Es wird eine JSON-Datei heruntergeladen.
4. Öffnen Sie in der neuen Gramps Web-Instanz die Importseite. Importieren Sie die in Schritt 1 exportierte `.gramps`-Datei.
5. Laden Sie auf der Importseite der neuen Gramps Web-Instanz das Medienarchiv (ZIP) hoch.
6. Gehen Sie zu Einstellungen > Verwaltung > Benutzer der neuen Gramps Web-Instanz verwalten. Klicken Sie auf die Schaltfläche "Benutzerkonten importieren" und laden Sie die in Schritt 3 heruntergeladene JSON-Datei hoch.

Bitte beachten Sie, dass, während Ihre Benutzerkonten migriert werden, alle Ihre Benutzer neue Passwörter über den Link "Passwort vergessen" festlegen müssen, da Passwörter in verschlüsselter Form gespeichert werden und nicht exportiert werden können.
