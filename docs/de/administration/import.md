## Bereiten Sie Ihre Gramps-Datenbank vor

Wenn Sie Gramps Desktop verwenden, gibt es zwei Schritte, um Ihre Datenbank vorzubereiten, um sicherzustellen, dass alles reibungslos funktioniert. Wenn Sie von einem anderen Genealogieprogramm migrieren, können Sie diesen Schritt überspringen.

1. Überprüfen und reparieren Sie die Datenbank
    - Optional: Erstellen Sie ein Datenbanksicherung, indem Sie in Gramps XML exportieren
    - Führen Sie das [Tool zur Überprüfung und Reparatur der Datenbank](https://gramps-project.org/wiki/index.php/Gramps_5.2_Wiki_Manual_-_Tools#Check_and_Repair_Database) aus. Dies behebt einige interne Inkonsistenzen, die zu Problemen in Gramps Web führen könnten.
2. Medienpfade in relative umwandeln
    - Verwenden Sie den Gramps Medienmanager, um [alle Medienpfade von absolut in relativ umzuwandeln](https://gramps-project.org/wiki/index.php/Gramps_5.2_Wiki_Manual_-_Tools#Convert_paths_from_relative_to_absolute). Beachten Sie, dass selbst bei relativen Pfaden alle Mediendateien außerhalb Ihres Gramps-Medienverzeichnisses nicht ordnungsgemäß funktionieren, wenn sie mit Gramps Web synchronisiert werden.

## Genealogische Daten importieren

Um einen bestehenden Stammbaum zu importieren, verwenden Sie die Seite "Importieren" und laden Sie eine Datei in einem der von Gramps unterstützten Dateiformate hoch – siehe [Import aus einem anderen Genealogieprogramm](https://www.gramps-project.org/wiki/index.php/Import_from_another_genealogy_program) im Gramps-Wiki.

Wenn Sie bereits Gramps Desktop verwenden, wird dringend empfohlen, das Gramps XML (`.gramps`) Format zu verwenden, um sicherzustellen, dass Ihre Online- und Offline-Bäume dieselben Identifikatoren verwenden und [synchronisiert](sync.md) werden können.

Nachdem Sie auf "Importieren" geklickt haben, wird die Datei zunächst analysiert und ein Dialogfeld "Import bestätigen" zeigt eine Vorschau der Objekte an, die die Datei enthält (Personen, Familien, Ereignisse, Orte usw.), bevor etwas zu Ihrem Baum hinzugefügt wird. Überprüfen Sie die Zählungen und klicken Sie dann im Dialog auf "Importieren", um fortzufahren, oder auf "Abbrechen", um ohne Änderungen abzubrechen.

!!! warning
    Ein regulärer Import ist rein additiv: Er erstellt immer neue Objekte und aktualisiert oder löscht niemals vorhandene, selbst für Objekte, die bereits in Ihrem Baum unter derselben Gramps-ID oder Handhabung existieren. Das zweimalige Importieren derselben Datei – oder das Importieren einer Datei, die sich mit bereits im Baum vorhandenen Daten überschneidet – wird jedes übereinstimmende Objekt duplizieren, anstatt es zusammenzuführen oder zu überspringen.

    Wenn Sie Änderungen, die anderswo an einem bereits importierten Baum vorgenommen wurden, übernehmen müssen, verwenden Sie stattdessen [Wiederherstellen aus Backup](settings.md#restore-from-backup), das den Baum ersetzt, um mit der hochgeladenen Datei übereinzustimmen, anstatt ihn zu ergänzen.

## Warum keine Unterstützung für Gramps XML-Paket?

Während Gramps XML (`.gramps`) das bevorzugte Format zum Importieren von Daten ist, wird das Gramps XML *Paket* (`.gpkg`) von Gramps Web nicht unterstützt. Dies liegt daran, dass die Import- und Export-Routinen für Mediendateien nicht für die Verwendung auf einem Webserver geeignet sind.

Um die zu einer importierten `.gramps`-Datei gehörenden Mediendateien zu importieren, siehe den nächsten Abschnitt.

## Mediendateien importieren

Wenn Sie einen Stammbaum hochgeladen haben und die entsprechenden Mediendateien hochladen müssen, können Sie die Schaltfläche "Medienarchiv importieren" auf der Seite "Importieren" verwenden.

Es wird eine ZIP-Datei mit den fehlenden Mediendateien erwartet. Die Ordnerstruktur in der ZIP-Datei muss nicht mit der Ordnerstruktur im Gramps-Medienordner übereinstimmen, da die Dateien anhand ihrer Prüfziffer den Medienobjekten zugeordnet werden.

Beachten Sie, dass diese Funktion nur für Dateien funktioniert, die die richtige Prüfziffer in der Gramps-Datenbank haben (was sichergestellt werden sollte, indem das Überprüfungs- und Reparaturtool im ersten Schritt ausgeführt wird).

Wenn Sie von einem anderen Genealogieprogramm, das Mediendateien enthält, zu Gramps Web wechseln, wird empfohlen, zunächst alles in Gramps Desktop zu importieren, das mehr Optionen bietet, um vorhandene Mediendateien mit einem importierten Baum zu verknüpfen.
