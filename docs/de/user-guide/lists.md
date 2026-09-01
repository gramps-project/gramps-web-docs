# Listen

Jeder Objekttyp in Gramps Web hat eine Listenansicht: Personen, Familien, Ereignisse, Orte, Quellen, Zitationen, Repositories, Notizen und Medien. Sie funktionieren alle gleich und teilen sich die gleichen Werkzeuge zum Sortieren, Filtern und Bearbeiten in großen Mengen.

## Sortieren und Seitenwechsel

Klicken Sie auf einen Spaltenkopf, um nach dieser Spalte zu sortieren; klicken Sie erneut darauf, um die Reihenfolge umzukehren. Das Sortieren erfolgt durch den Server, sodass es für die gesamte Liste gilt, nicht nur für die Seite, die Sie gerade ansehen.

Lange Listen werden in Seiten aufgeteilt. Verwenden Sie die Paginierungssteuerungen am Ende, um zwischen ihnen zu wechseln.

Auf schmalen Bildschirmen wechselt die Tabelle automatisch zu einem kompakten Layout, sodass die Listenansichten auch auf einem Telefon nutzbar bleiben.

## Spalten auswählen

Klicken Sie auf das Zahnradsymbol über der Liste, um den **Spalten**-Dialog zu öffnen. Aktivieren oder deaktivieren Sie eine Spalte, um sie anzuzeigen oder auszublenden. **Zurücksetzen** stellt die Standardauswahl für diese Liste wieder her.

Mindestens eine Spalte muss sichtbar bleiben, sodass die letzte verbleibende Spalte nicht deaktiviert werden kann.

Ihre Spaltenauswahl wird pro Objekttyp und pro Stammbaum gespeichert. Sie wird in Ihrem Browser gespeichert, sodass sie für andere Benutzer nicht sichtbar ist – aber sie folgt Ihnen auch nicht zu einem anderen Browser oder Gerät.

## Filtern

Klicken Sie auf die **Filter**-Schaltfläche, um das Filterpanel zu öffnen. Ein Pillenumschalter oben im Panel wechselt zwischen zwei Modi:

- **einfach** – eine Reihe von vorgefertigten Filtern, die vom Objekttyp abhängen. Für Personen können Sie beispielsweise nach Geburtsjahr, Sterbejahr, verschiedenen Personenmerkmalen, der Anzahl der Assoziationen, Etiketten und ob ein Objekt privat oder öffentlich ist, filtern.
- **GQL** – ein einzelnes Textfeld für eine erweiterte Abfrage in der [Gramps Query Language](gql.md). Geben Sie die Abfrage ein und drücken Sie die Eingabetaste oder klicken Sie auf **Anwenden**. Wenn die Abfrage ungültig ist, wird der Rahmen des Feldes rot.

Aktive Filter werden als Chips über der Liste angezeigt. Entfernen Sie einen einzelnen Filter, indem Sie auf die Schaltfläche zum Löschen des Chips klicken, oder verwenden Sie **Alle Filter löschen**, um sie alle auf einmal zu entfernen.

!!! Hinweis
    Die beiden Modi sind Alternativen, nicht additiv: Eine GQL-Abfrage ersetzt die einfachen Filter, und das Zurückwechseln in den einfachen Modus entfernt die Abfrage.

## Objekte auswählen und in großen Mengen handeln

Benutzer mit Bearbeitungsberechtigungen sehen eine **Auswählen**-Schaltfläche neben der Filter-Schaltfläche. Klicken Sie darauf, um in den Auswahlmodus zu wechseln, der jeder Zeile ein Kontrollkästchen hinzufügt.

Aktivieren Sie die Objekte, die Sie möchten, und eine Symbolleiste erscheint, die anzeigt, wie viele ausgewählt sind, zusammen mit einem **Aktion**-Dropdown und einer **Anwenden**-Schaltfläche.

### Löschen

Wählen Sie ein oder mehrere Objekte aus, wählen Sie **Löschen** und klicken Sie auf **Anwenden**. Ein Bestätigungsdialog fordert Sie zur Bestätigung auf und warnt, dass die Aktion nicht rückgängig gemacht werden kann.

!!! Tipp
    Löschvorgänge werden in der [Versionsgeschichte](revisions.md) wie jede andere Änderung aufgezeichnet, sodass ein versehentliches Massenlöschen durch das Rückgängigmachen der entsprechenden Transaktion rückgängig gemacht werden kann.

### Zusammenführen

Wählen Sie **genau zwei** Objekte aus, wählen Sie **Zusammenführen** und klicken Sie auf **Anwenden**. Ein Dialog fragt, welches der beiden die primären Daten für das zusammengeführte Objekt bereitstellen soll; klicken Sie auf das, das Sie als primär behalten möchten. Die Daten des anderen Objekts werden in es zusammengeführt und die Referenzen werden aktualisiert.

Das Zusammenführen ist für Personen, Familien, Ereignisse, Orte, Quellen und Zitationen verfügbar. Es ist nicht für Repositories, Notizen und Medienobjekte verfügbar.

Wenn Sie eine Aktion ohne eine gültige Auswahl wählen – zum Beispiel ein Zusammenführen mit nur einem ausgewählten Objekt – erklärt ein Dialog, was erforderlich ist.
