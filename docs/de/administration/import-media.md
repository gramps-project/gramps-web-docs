# Medien-Dateien importieren

Wenn Sie einen [Familienstammbaum importiert](import.md) haben und die entsprechenden Mediendateien hochladen müssen, verwenden Sie **Medien-Dateien importieren** im Datenbereich der [Verwaltungseinstellungen](settings.md). Es wird eine ZIP-Datei erwartet, die die fehlenden Mediendateien enthält. Dateien werden auf eine von zwei Arten mit Medienobjekten in Ihrem Baum abgeglichen:

- **Nach Prüfziffer.** Für Medienobjekte, die eine Prüfziffer haben – wie es bei Bäumen der Fall ist, die von Gramps Desktop importiert wurden – wird die Datei mit der übereinstimmenden Prüfziffer verwendet, unabhängig von ihrem Namen oder der Ordnerstruktur in der ZIP-Datei. Dies funktioniert nur, wenn die Prüfziffern in der Gramps-Datenbank korrekt sind, was durch das Ausführen des Prüf- und Reparaturtools sichergestellt wird.
- **Nach Pfad.** Medienobjekte ohne Prüfziffer – wie es typischerweise nach einem GEDCOM-Import der Fall ist – werden nach ihrem Pfad abgeglichen: Die ZIP-Datei muss die Datei genau unter dem relativen Pfad enthalten, der im Medienobjekt gespeichert ist.

Wenn die in Ihrer GEDCOM-Datei gespeicherten Pfade absolut sind (zum Beispiel `C:\Users\...\photo.jpg`), funktioniert der Abgleich nach Pfad nicht. In diesem Fall wird empfohlen, zunächst alles in Gramps Desktop zu importieren, das mehr Optionen bietet, um vorhandene Mediendateien mit einem importierten Baum zu verknüpfen, und dann zu Gramps Web zu wechseln, wie in [Von Gramps Desktop kommend](import.md#coming-from-gramps-desktop) beschrieben.

## Status der Mediendateien

Der **Daten**-Bereich der [Verwaltungseinstellungen](settings.md) zeigt:

- Die Gesamtzahl der Medienobjekte im Baum und ob einige eine Prüfziffer vermissen
- Die Anzahl der Medienobjekte, deren zugehörige Datei auf dem Server fehlt

Ein grünes Häkchen zeigt an, dass alles in Ordnung ist. Wenn Probleme festgestellt werden, werden Links zu den betroffenen Objekten angezeigt. Fehlende Prüfziffern treten typischerweise auf, wenn Daten aus einem Format wie GEDCOM importiert wurden, das Medienreferenzen, aber nicht die tatsächlichen Dateien enthält. Die fehlenden Dateien können wie oben beschrieben hochgeladen werden.
