# Revisionsverlauf

Die Ansicht des Revisionsverlaufs zeigt alle Bearbeitungen, die am Stammbaum vorgenommen wurden.

Die Listenansicht zeigt die Bearbeitungen, gruppiert nach „Transaktionen“. Eine Transaktion ist eine Gruppe aus einer oder mehreren Hinzufügungen, Löschungen oder Änderungen an Gramps-Objekten. Wenn du beispielsweise eine neue Familie mit zwei bereits vorhandenen Personen als Vater und Mutter hinzufügst, wird eine Transaktion mit einem hinzugefügten Familienobjekt und zwei geänderten Personenobjekten erzeugt (da diese den Verweis auf das neue Familienobjekt enthalten).

Wenn du auf eine Transaktion klickst, wird die Detailansicht der Transaktion geöffnet. Sie enthält die Liste der einzelnen Hinzufügungen, Löschungen und Aktualisierungen nach Gramps-Objekt.

Wenn du eine einzelne Änderung auswählst, wird eine Ansicht der rohen JSON-Darstellung des Gramps-Objekts geöffnet, in der Hinzufügungen beziehungsweise Löschungen grün beziehungsweise rot hervorgehoben sind. Über eine Schaltfläche oberhalb des Diffs gelangst du direkt zur eigenen Seite des Objekts.

## Revisionen eines einzelnen Objekts

Um den Verlauf einer bestimmten Person, Familie, eines Ereignisses oder eines anderen Objekts anzuzeigen, öffne dessen Seite und wechsle zum Tab **Revisionen**. Dort wird jede an diesem Objekt vorgenommene Änderung angezeigt, die neueste zuerst, einschließlich der Art der Änderung (hinzugefügt, aktualisiert oder gelöscht), des Benutzers, der sie vorgenommen hat, und des Zeitpunkts. Wenn du auf einen Eintrag klickst, wird die zugehörige Transaktion geöffnet, in der du den Diff prüfen oder die Änderung rückgängig machen kannst.

Klicke auf **Mehr anzeigen**, um ältere Einträge zu laden. Bei Objekten mit einem sehr langen Verlauf werden nur die neuesten Revisionen angezeigt. Bei Objekten, die zuletzt geändert wurden, bevor der Revisionsverlauf aufgezeichnet wurde, zeigt der Tab nur den Zeitpunkt der letzten Änderung an.

!!! note
    Der Tab „Revisionen“ ist für Mitglieder und höhere Rollen sichtbar und erfordert Gramps Web API Version 3.22 oder höher.

## Rückgängigmachen einer Revision

Auf der Detailseite einer Transaktion kannst du mit der Schaltfläche **Rückgängig** diese Transaktion rückgängig machen. Wenn du darauf klickst, wird geprüft, ob die Änderung ohne Konflikte rückgängig gemacht werden kann.

**Rückgängigmachen ohne Konflikte** – wenn keines der von der Transaktion betroffenen Objekte seitdem geändert wurde, kann die Änderung ohne Risiko rückgängig gemacht werden. Ein Bestätigungsdialog wird angezeigt. Wenn du auf **Rückgängig** klickst, wird die Transaktion rückgängig gemacht.

**Erzwingen erforderlich** – wenn eines oder mehrere der betroffenen Objekte durch eine spätere Transaktion geändert wurden, ist ein Rückgängigmachen ohne Konflikte nicht möglich. Der Dialog weist darauf hin, dass das Erzwingen des Rückgängigmachens zu Inkonsistenzen in den Daten führen kann, da spätere Änderungen, die von den betreffenden Objekten abhängen, unverändert beibehalten werden, obwohl die zugrunde liegenden Objekte zurückgesetzt werden. Du kannst dann entweder abbrechen oder auf **Rückgängig erzwingen** klicken, um trotzdem fortzufahren.

In beiden Fällen wird das Rückgängigmachen als Hintergrundaufgabe ausgeführt und ein Fortschrittsindikator angezeigt.
