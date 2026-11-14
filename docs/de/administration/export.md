# Daten exportieren

Die Exportseite ermöglicht es Ihnen, die Familienstammdaten in verschiedenen Formaten herunterzuladen sowie ein Archiv aller Mediendateien.

## Familienstammbaum als Gramps XML exportieren

Um eine Kopie der Familienstammdaten zu erhalten, öffnen Sie die Exportseite in Gramps Web und wählen Sie das Gramps XML-Format aus. Ein Klick auf "exportieren" generiert die Datei und startet den Download, sobald sie bereit ist.

Bitte beachten Sie, dass der Export keine privaten Datensätze enthält, wenn Ihr Gramps Web-Benutzer keine Berechtigung hat, private Datensätze anzuzeigen.

## Sichern Sie Ihren Familienstammbaum

Für vollständige Sicherungen des Baums – einschließlich seiner Einstellungen und Benutzer – siehe [Sichern und Wiederherstellen](backups.md). Ein Gramps XML-Export kann nur als Sicherung der Familienstammdaten dienen und kann über [Wiederherstellen von Backup](backups.md#restore-from-backup) wiederhergestellt werden.

## Teilen Sie Ihren Familienstammbaum mit Benutzern anderer Genealogie-Programme

Wenn das Teilen genealogischer Daten als Gramps XML keine Option ist, können Sie auch eine GEDCOM-Datei exportieren. Bitte beachten Sie, dass dies nicht als Sicherung Ihres Gramps Web-Baums geeignet ist.

## Sichern Sie Ihre Mediendateien

Um Ihre Mediendateien zu sichern, können Sie ein ZIP-Archiv aller Mediendateien auf der Exportseite erstellen und herunterladen.

Bitte beachten Sie, dass dies, insbesondere bei großen Bäumen, eine kostspielige Operation für den Server sein kann und nur durchgeführt werden sollte, wenn es unbedingt notwendig ist. Aus diesem Grund ist die Anzahl der erstellbaren Medienarchive begrenzt (standardmäßig auf eines pro Stunde). Wenn Sie das Limit erreichen, wird eine Fehlermeldung angezeigt.

Eine bessere Option, um Ihre Mediendateien regelmäßig zu sichern, ist die Verwendung des [Gramps Web Sync-Addons](sync.md) (das selbst keine Sicherungslösung ist) und die Erstellung inkrementeller Sicherungen auf Ihrem lokalen Computer.

In beiden Fällen, wenn Ihr Gramps Web-Benutzer keine Berechtigung hat, private Datensätze anzuzeigen, enthält der Export keine Dateien von privaten Medienobjekten.

## Wechsel zu einer anderen Gramps Web-Instanz

Gramps Web schränkt Sie nicht auf einen bestimmten Anbieter ein, und Sie können jederzeit zu einer anderen Gramps Web-Instanz wechseln, ohne Daten zu verlieren und ohne direkten Zugriff auf einen der Server zu haben.

Um eine vollständige Migration zu erreichen, befolgen Sie diese Schritte (vorausgesetzt, Sie haben die Berechtigungen des Baum-Eigentümers):

1. Gehen Sie zur Exportseite und exportieren Sie Ihren Baum als Gramps XML (`.gramps`) Datei. Wenn Sie das [Sync-Addon](sync.md) verwenden, können Sie den Export auch in Gramps Desktop generieren.
2. Generieren und laden Sie auf der Exportseite ein Medienarchiv herunter. Wenn Sie das [Sync-Addon](sync.md) verwenden, können Sie einfach Ihren lokalen Gramps-Medienordner zippen.
3. Gehen Sie zu Einstellungen > Verwaltung > Benutzer verwalten und klicken Sie auf die Schaltfläche "Benutzerdetails exportieren". Es wird eine JSON-Datei heruntergeladen.
4. Öffnen Sie in der neuen Gramps Web-Instanz die Importseite. Importieren Sie die in Schritt 1 exportierte `.gramps`-Datei.
5. Laden Sie auf der Importseite der neuen Gramps Web-Instanz das Medienarchiv (ZIP) hoch.
6. Gehen Sie zu Einstellungen > Verwaltung > Benutzer der neuen Gramps Web-Instanz verwalten. Klicken Sie auf die Schaltfläche "Benutzerkonten importieren" und laden Sie die in Schritt 3 heruntergeladene JSON-Datei hoch.

Bitte beachten Sie, dass, während Ihre Benutzerkonten migriert werden, alle Ihre Benutzer neue Passwörter festlegen müssen, indem sie den Link "Passwort vergessen" verwenden, da Passwörter in verschlüsselter Form gespeichert werden und nicht exportiert werden können.
