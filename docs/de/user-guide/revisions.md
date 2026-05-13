# Änderungsverlauf

Die Ansicht des Änderungsverlaufs zeigt alle Änderungen, die am Stammbaum vorgenommen wurden.

Die Listenansicht zeigt die Änderungen gruppiert nach "Transaktionen". Eine Transaktion ist eine Gruppe von einer oder mehreren Hinzufügungen, Löschungen oder Änderungen an Gramps-Objekten. Zum Beispiel erzeugt das Hinzufügen einer neuen Familie mit zwei bestehenden Personen als Vater und Mutter eine Transaktion mit einem hinzugefügten Familienobjekt und zwei modifizierten Personenobjekten (da sie den Link zum neuen Familienobjekt enthalten).

Ein Klick auf eine Transaktion öffnet die Detailansicht der Transaktion. Sie enthält die Liste der einzelnen Hinzufügungen, Löschungen und Aktualisierungen nach Gramps-Objekt.

Die Auswahl einer einzelnen Änderung öffnet eine Ansicht der rohen JSON-Darstellung des Gramps-Objekts, wobei Hinzufügungen und Löschungen jeweils in Grün und Rot hervorgehoben sind.

## Rückgängig machen einer Revision

Auf der Detailseite der Transaktion ermöglicht eine **Rückgängig**-Schaltfläche, diese Transaktion rückgängig zu machen. Ein Klick darauf prüft, ob das Rückgängigmachen sauber durchgeführt werden kann.

**Sauberes Rückgängigmachen** – wenn keines der von der Transaktion betroffenen Objekte seitdem geändert wurde, kann das Rückgängigmachen ohne Risiko erfolgen. Ein Bestätigungsdialog wird angezeigt, und ein Klick auf **Rückgängig** macht die Transaktion rückgängig.

**Zwang erforderlich** – wenn eines oder mehrere betroffene Objekte von einer späteren Transaktion geändert wurden, ist ein sauberes Rückgängigmachen nicht möglich. Der Dialog warnt, dass das Zwangsrückgängigmachen zu Dateninkonsistenzen führen kann, da spätere Änderungen, die von den betreffenden Objekten abhängen, unverändert beibehalten werden, auch wenn die zugrunde liegenden Objekte zurückgesetzt werden. Sie können dann entweder abbrechen oder auf **Zwangsrückgängig** klicken, um dennoch fortzufahren.

In beiden Fällen wird das Rückgängigmachen als Hintergrundaufgabe ausgeführt und ein Fortschrittsindikator wird angezeigt.
