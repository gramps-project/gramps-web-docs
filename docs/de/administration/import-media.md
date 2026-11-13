# Importieren von Mediendateien

Wenn Sie einen [Familienstammbaum importiert](import.md) haben und die entsprechenden Mediendateien hochladen müssen, verwenden Sie **Mediendateien importieren** im Datenbereich der [Verwaltungseinstellungen](settings.md). Es wird eine ZIP-Datei erwartet, die die fehlenden Mediendateien enthält. Dateien werden auf eine von zwei Arten mit Medienobjekten in Ihrem Baum abgeglichen:

- **Nach Prüfziffer.** Für Medienobjekte, die eine Prüfziffer haben – wie es bei Bäumen der Fall ist, die von Gramps Desktop importiert wurden – wird die Datei mit der übereinstimmenden Prüfziffer verwendet, unabhängig von ihrem Namen oder der Ordnerstruktur in der ZIP-Datei. Dies funktioniert nur, wenn die Prüfziffern in der Gramps-Datenbank korrekt sind, was durch das Ausführen des Prüf- und Reparaturwerkzeugs sichergestellt wird.
- **Nach Pfad.** Medienobjekte ohne Prüfziffer – wie es typischerweise nach einem GEDCOM-Import der Fall ist – werden nach ihrem Pfad abgeglichen: Die ZIP-Datei muss die Datei unter genau dem relativen Pfad enthalten, der im Medienobjekt gespeichert ist.

Wenn die in Ihrer GEDCOM-Datei gespeicherten Pfade absolut sind (zum Beispiel `C:\Users\...\photo.jpg`), funktioniert der Abgleich nach Pfad nicht. In diesem Fall wird empfohlen, zunächst alles in Gramps Desktop zu importieren, das mehr Optionen bietet, um vorhandene Mediendateien mit einem importierten Baum zu verknüpfen, und dann zu Gramps Web zu wechseln, wie in [Von Gramps Desktop kommend](import.md#coming-from-gramps-desktop) beschrieben.
