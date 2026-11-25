# Mediendateien importieren

Wenn du [einen Stammbaum importiert hast](import.md) und die zugehörigen Mediendateien hochladen musst, verwende **Mediendateien importieren** auf der [Importseite](import.md) unterhalb des Stammbaumimports. Es wird eine ZIP-Datei erwartet, die die fehlenden Mediendateien enthält. Der Upload ist erst möglich, wenn der Stammbaum Medienobjekte enthält, da die Dateien vorhandenen Medienobjekten zugeordnet werden – eine Stammbaumdatei verweist lediglich auf ihre Mediendateien, daher musst du sie zuerst importieren.

Dateien werden auf eine von zwei Arten Medienobjekten in deinem Stammbaum zugeordnet:

- **Nach Prüfsumme.** Für Medienobjekte, die eine Prüfsumme haben – wie es bei aus Gramps Desktop importierten Stammbäumen der Fall ist –, wird die Datei mit der passenden Prüfsumme verwendet, unabhängig von ihrem Namen oder der Ordnerstruktur in der ZIP-Datei. Dies funktioniert nur, wenn die Prüfsummen in der Gramps-Datenbank korrekt sind. Das wird durch die Ausführung des Werkzeugs zum Prüfen und Reparieren sichergestellt.
- **Nach Pfad oder Dateiname.** Medienobjekte ohne Prüfsumme – wie es nach einem GEDCOM-Import üblich ist – werden anhand des im Medienobjekt gespeicherten relativen Pfads zugeordnet. Wenn keine Datei in der ZIP-Datei diesen Pfad hat, werden sie allein anhand des Dateinamens zugeordnet, wobei Groß- und Kleinschreibung ignoriert wird (seit Gramps Web API 3.26). Dies funktioniert auch für absolute Pfade aus anderen Programmen, wie etwa `C:\Users\...\Family\grandpa.jpg`, sodass du einfach alle Dateien in die ZIP-Datei legen kannst. Ein Dateiname wird nur verwendet, wenn er sowohl in der ZIP-Datei als auch unter den Medienobjekten, denen noch keine Datei zugeordnet ist, eindeutig ist.

Nach dem Upload wird angezeigt, für wie viele Medienobjekte eine Datei gefunden wurde. Außerdem werden diejenigen aufgelistet, für die die ZIP-Datei keine Datei enthielt, einschließlich ihrer Gramps-ID und des gespeicherten Pfads. Verwende diese Liste, um die fehlenden Dateien zu finden, und lade anschließend eine weitere ZIP-Datei hoch, die nur diese Dateien enthält – Dateien, die sich bereits auf dem Server befinden, sind davon nicht betroffen.

Wenn mehrere Medienobjekte in verschiedenen Ordnern denselben Dateinamen haben, funktioniert die Zuordnung anhand des Dateinamens für sie nicht. Stelle entweder die Ordnerstruktur anhand der gespeicherten Pfade in der ZIP-Datei wieder her oder importiere zunächst alles in Gramps Desktop. Dort gibt es mehr Möglichkeiten, vorhandene Mediendateien einem importierten Stammbaum zuzuordnen. Wechsle anschließend wie unter [Aus Gramps Desktop kommend](import.md#coming-from-gramps-desktop) beschrieben zu Gramps Web.

## Status der Mediendateien

Der Abschnitt **Daten** der [Administrationseinstellungen](settings.md) zeigt:

- Die Gesamtzahl der Medienobjekte im Stammbaum und ob bei einem davon die Prüfsumme fehlt
- Die Anzahl der Medienobjekte, deren zugehörige Datei auf dem Server fehlt

Ein grünes Häkchen zeigt an, dass alles in Ordnung ist. Wenn Probleme festgestellt werden, werden Links zu den betroffenen Objekten angezeigt. Fehlende Prüfsummen treten typischerweise auf, wenn Daten aus einem Format wie GEDCOM importiert wurden, das Medienreferenzen, aber nicht die eigentlichen Dateien enthält. Die fehlenden Dateien können wie oben beschrieben hochgeladen werden.
