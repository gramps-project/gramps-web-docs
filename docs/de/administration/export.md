# Daten exportieren

Auf der Exportseite kannst du die Daten des Familienstammbaums in verschiedenen Formaten sowie ein Archiv aller Mediendateien herunterladen.

## Familienstammbaum als Gramps-XML exportieren

Um eine Kopie der Daten des Familienstammbaums zu erhalten, öffne die Exportseite in Gramps Web und wähle das Gramps-XML-Format aus. Klicke auf **Generieren**, um die Datei zu erstellen, und anschließend auf **Herunterladen**, sobald sie bereit ist. Bei einem großen Stammbaum kann die Erstellung der Datei einige Zeit dauern. Du kannst die Seite in der Zwischenzeit verlassen und die Datei später über ihren Eintrag in den [Benachrichtigungen](../user-guide/notifications.md) herunterladen.

Beachte, dass der Export keine privaten Datensätze enthält, wenn dein Gramps-Web-Benutzer nicht dazu berechtigt ist, private Datensätze anzuzeigen.

## Familienstammbaum sichern

Eine vollständige Sicherung des Stammbaums – einschließlich seiner Einstellungen und Benutzer – findest du unter [Sichern und Wiederherstellen](backups.md). Ein Gramps-XML-Export kann nur als Sicherung der Daten des Familienstammbaums dienen und über [Aus Sicherung wiederherstellen](backups.md#restore-from-backup) wiederhergestellt werden.

## Familienstammbaum mit Benutzern anderer Genealogieprogramme teilen

Wenn das Teilen genealogischer Daten als Gramps XML nicht möglich ist, kannst du auch eine GEDCOM-Datei exportieren. Beachte, dass diese nicht als Sicherung deines Gramps-Web-Stammbaums geeignet ist.

## Mediendateien sichern

Um deine Mediendateien zu sichern, kannst du auf der Exportseite ein ZIP-Archiv aller Mediendateien erstellen und herunterladen.

Beachte, dass dies insbesondere bei großen Stammbäumen einen hohen Aufwand für den Server verursachen kann und nur durchgeführt werden sollte, wenn es unbedingt notwendig ist. Daher ist die Anzahl der erstellbaren Medienarchive begrenzt (standardmäßig auf eines pro Stunde). Wenn du das Limit erreichst, wird dies in der Fehlermeldung angezeigt.

Eine bessere Möglichkeit, deine Mediendateien regelmäßig zu sichern, besteht darin, das [Gramps-Web-Sync-Addon](sync.md) zu verwenden (das selbst keine Sicherungslösung ist) und inkrementelle Sicherungen auf deinem lokalen Computer zu erstellen.

In beiden Fällen enthält der Export keine Dateien privater Medienobjekte, wenn dein Gramps-Web-Benutzer nicht dazu berechtigt ist, private Datensätze anzuzeigen.

## Zu einer anderen Gramps-Web-Instanz wechseln

Gramps Web bindet dich nicht an einen bestimmten Anbieter. Du kannst jederzeit zu einer anderen Gramps-Web-Instanz wechseln, ohne Daten zu verlieren und ohne direkten Zugriff auf einen der beiden Server zu benötigen.

Führe für eine vollständige Migration die folgenden Schritte aus (vorausgesetzt, du verfügst über Berechtigungen als Stammbaumbesitzer):

1. Gehe zur Exportseite und exportiere deinen Stammbaum als Gramps-XML-Datei (`.gramps`). Wenn du das [Sync-Addon](sync.md) verwendest, kannst du den Export auch in Gramps Desktop erstellen.
2. Erstelle und lade auf der Exportseite ein Medienarchiv herunter. Wenn du das [Sync-Addon](sync.md) verwendest, kannst du deinen lokalen Gramps-Medienordner auch einfach als ZIP-Archiv komprimieren.
3. Gehe zu Einstellungen > Administration > Benutzer verwalten und klicke auf die Schaltfläche „Benutzerdetails exportieren“. Dadurch wird eine JSON-Datei heruntergeladen.
4. Öffne in der neuen Gramps-Web-Instanz die [Importseite](import.md). Importiere die in Schritt 1 exportierte `.gramps`-Datei.
5. Lade auf der Importseite der neuen Gramps-Web-Instanz unter [Mediendateien importieren](import-media.md) das Medienarchiv (ZIP) hoch.
6. Gehe in der neuen Gramps-Web-Instanz zu Einstellungen > Administration > Benutzer verwalten. Klicke auf die Schaltfläche „Benutzerkonten importieren“ und lade die in Schritt 3 heruntergeladene JSON-Datei hoch.

Beachte, dass deine Benutzerkonten zwar migriert werden, alle deine Benutzer jedoch über den Link „Passwort vergessen“ neue Passwörter festlegen müssen, da Passwörter verschlüsselt gespeichert und nicht exportiert werden können.
