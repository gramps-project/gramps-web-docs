# Änderungsverlauf

Die Ansicht des Änderungsverlaufs zeigt alle Änderungen, die am Stammbaum vorgenommen wurden.

Die Listenansicht zeigt die Änderungen gruppiert nach "Transaktionen". Eine Transaktion ist eine Gruppe von einer oder mehreren Hinzufügungen, Löschungen oder Änderungen an Gramps-Objekten. Zum Beispiel erzeugt das Hinzufügen einer neuen Familie mit zwei bestehenden Personen als Vater und Mutter eine Transaktion mit einem hinzugefügten Familienobjekt und zwei modifizierten Personenobjekten (da sie den Link zum neuen Familienobjekt enthalten).

Ein Klick auf eine Transaktion öffnet die Detailansicht der Transaktion. Sie enthält die Liste der einzelnen Hinzufügungen, Löschungen und Aktualisierungen nach Gramps-Objekt.

Die Auswahl einer einzelnen Änderung öffnet eine Ansicht der rohen JSON-Darstellung des Gramps-Objekts, wobei Hinzufügungen und Löschungen jeweils in Grün und Rot hervorgehoben sind. Ein Button über dem Diff führt Sie direkt zur eigenen Seite des Objekts.

## Revisionen eines einzelnen Objekts

Um die Historie einer bestimmten Person, Familie, eines Ereignisses oder eines anderen Objekts zu sehen, öffnen Sie dessen Seite und wechseln Sie zum Tab **Revisionen**. Er listet jede Änderung auf, die an diesem Objekt vorgenommen wurde, die neueste zuerst, mit der Art der Änderung (hinzugefügt, aktualisiert oder gelöscht), dem Benutzer, der sie vorgenommen hat, und wann. Ein Klick auf einen Eintrag öffnet die Transaktion, zu der er gehört, wo Sie den Diff einsehen oder ihn rückgängig machen können.

Klicken Sie auf **Mehr anzeigen**, um ältere Einträge zu laden; bei Objekten mit einer sehr langen Historie werden nur die neuesten Revisionen angezeigt. Für Objekte, die zuletzt geändert wurden, bevor der Änderungsverlauf aufgezeichnet wurde, zeigt der Tab nur die Zeit der letzten Änderung an.

!!! Hinweis
    Der Tab Revisionen ist für Mitglieder und höher sichtbar und erfordert die Gramps Web API Version 3.22 oder höher.

## Rückgängigmachen einer Revision

Auf der Detailseite der Transaktion ermöglicht ein **Rückgängig**-Button, diese Transaktion rückgängig zu machen. Ein Klick darauf überprüft, ob das Rückgängigmachen sauber durchgeführt werden kann.

**Sauberes Rückgängigmachen** – wenn keines der von der Transaktion betroffenen Objekte seitdem geändert wurde, kann das Rückgängigmachen ohne Risiko erfolgen. Ein Bestätigungsdialog wird angezeigt, und ein Klick auf **Rückgängig** macht die Transaktion rückgängig.

**Zwang erforderlich** – wenn eines oder mehrere betroffene Objekte durch eine spätere Transaktion geändert wurden, ist ein sauberes Rückgängigmachen nicht möglich. Der Dialog warnt, dass das Erzwingen des Rückgängigmachens zu Dateninkonsistenzen führen kann, da spätere Änderungen, die von den betreffenden Objekten abhängen, unverändert beibehalten werden, obwohl die zugrunde liegenden Objekte zurückgesetzt werden. Sie können dann entweder abbrechen oder auf **Zwangsrückgängig** klicken, um dennoch fortzufahren.

In beiden Fällen wird das Rückgängigmachen als Hintergrundaufgabe ausgeführt und ein Fortschrittsindikator wird angezeigt.
