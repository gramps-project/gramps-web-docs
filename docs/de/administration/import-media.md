# Medien-Dateien importieren

Wenn Sie einen [Familienstammbaum importiert](import.md) haben und die entsprechenden Mediendateien hochladen müssen, verwenden Sie **Medien-Dateien importieren** auf der [Import-Seite](import.md), unter dem Import des Familienstammbaums. Es wird eine ZIP-Datei erwartet, die die fehlenden Mediendateien enthält. Der Upload ist nur möglich, wenn der Stammbaum Medienobjekte enthält, da die Dateien mit vorhandenen Medienobjekten abgeglichen werden – eine Familienstammbaumdatei verweist nur auf ihre Mediendateien, also importieren Sie sie zuerst.

Dateien werden auf eine der zwei Arten mit Medienobjekten in Ihrem Stammbaum abgeglichen:

- **Nach Prüfziffer.** Für Medienobjekte, die eine Prüfziffer haben – wie es bei Bäumen der Fall ist, die von Gramps Desktop importiert wurden – wird die Datei mit der übereinstimmenden Prüfziffer verwendet, unabhängig von ihrem Namen oder der Ordnerstruktur in der ZIP-Datei. Dies funktioniert nur, wenn die Prüfziffern in der Gramps-Datenbank korrekt sind, was durch das Ausführen des Prüf- und Reparaturwerkzeugs sichergestellt wird.
- **Nach Pfad oder Dateiname.** Medienobjekte ohne Prüfziffer – wie es typischerweise nach einem GEDCOM-Import der Fall ist – werden durch den relativen Pfad abgeglichen, der im Medienobjekt gespeichert ist. Wenn keine Datei in der ZIP diesen Pfad hat, werden sie nur nach Dateiname abgeglichen, wobei Groß- und Kleinschreibung ignoriert wird (seit Gramps Web API 3.26). Dies funktioniert auch für absolute Pfade von anderen Programmen, wie `C:\Users\...\Family\grandpa.jpg`, sodass Sie einfach alle Dateien in die ZIP-Datei legen können. Ein Dateiname wird nur verwendet, wenn er eindeutig ist, sowohl in der ZIP-Datei als auch unter den Medienobjekten, die noch keine Datei haben.

Nach dem Upload zeigt das Ergebnis an, für wie viele Medienobjekte eine Datei gefunden wurde, und listet diejenigen auf, für die die ZIP-Datei keine Datei hatte, mit ihrer Gramps-ID und dem gespeicherten Pfad. Verwenden Sie diese Liste, um die fehlenden Dateien zu finden, und laden Sie dann eine weitere ZIP-Datei mit nur diesen hoch – Dateien, die bereits auf dem Server sind, sind nicht betroffen.

Wenn mehrere Medienobjekte denselben Dateinamen in verschiedenen Ordnern haben, funktioniert der Abgleich nach Dateiname nicht für sie. Entweder rekonstruieren Sie die Ordnerstruktur aus den gespeicherten Pfaden in der ZIP-Datei oder importieren alles zuerst in Gramps Desktop, das mehr Optionen bietet, um vorhandene Mediendateien mit einem importierten Stammbaum zu verknüpfen, und wechseln dann zu Gramps Web, wie in [Von Gramps Desktop kommen](import.md#coming-from-gramps-desktop) beschrieben.

## Status der Mediendateien

Der Abschnitt **Daten** der [Administrationseinstellungen](settings.md) zeigt:

- Die Gesamtzahl der Medienobjekte im Stammbaum und ob einige eine Prüfziffer vermissen
- Die Anzahl der Medienobjekte, deren zugehörige Datei auf dem Server fehlt

Ein grünes Häkchen zeigt an, dass alles in Ordnung ist. Wenn Probleme festgestellt werden, werden Links zu den betroffenen Objekten angezeigt. Fehlende Prüfziffern treten typischerweise auf, wenn Daten aus einem Format wie GEDCOM importiert wurden, das Medienreferenzen, aber nicht die tatsächlichen Dateien enthält. Die fehlenden Dateien können wie oben beschrieben hochgeladen werden.
