# Listen

Jeder Objekttyp in Gramps Web hat eine Listenansicht: Personen, Familien, Ereignisse, Orte, Quellen, Zitationen, Archive, Notizen und Medien. Sie funktionieren alle gleich und teilen sich die gleichen Werkzeuge zum Sortieren, Filtern und Bearbeiten in großen Mengen.

## Sortieren und Seitenwechsel

Klicken Sie auf eine Spaltenüberschrift, um nach dieser Spalte zu sortieren; klicken Sie erneut darauf, um die Reihenfolge umzukehren. Das Sortieren erfolgt durch den Server, sodass es für die gesamte Liste gilt, nicht nur für die Seite, die Sie gerade ansehen.

Lange Listen werden in Seiten unterteilt. Verwenden Sie die Paginierungssteuerungen am Ende, um zwischen ihnen zu wechseln.

Auf schmalen Bildschirmen wechselt die Tabelle automatisch zu einem kompakten Layout, sodass die Listenansichten auch auf einem Telefon nutzbar bleiben.

## Spalten auswählen

Klicken Sie auf das Zahnrad-Symbol am rechten Ende der Werkzeugleiste über der Liste, um den **Spalten**-Dialog zu öffnen. Aktivieren oder deaktivieren Sie eine Spalte, um sie anzuzeigen oder auszublenden. **Zurücksetzen** stellt die Standardauswahl für diese Liste wieder her.

Mindestens eine Spalte muss sichtbar bleiben, sodass die letzte verbleibende Spalte nicht deaktiviert werden kann.

Ihre Spaltenauswahl wird pro Objekttyp und pro Stammbaum gespeichert. Sie wird in Ihrem Browser gespeichert, sodass sie für andere Benutzer nicht sichtbar ist – aber sie folgt Ihnen auch nicht zu einem anderen Browser oder Gerät.

## Filtern

Klicken Sie auf die **Filter**-Schaltfläche, um das Filterpanel zu öffnen. Es bietet drei Möglichkeiten zum Filtern, die kombiniert werden können:

- **Fertige Filter** in zusammenklappbaren Abschnitten, die vom Objekttyp abhängen. Bei Personen können Sie beispielsweise nach Name, Geburtsjahr, Sterbejahr, verschiedenen Personen-Eigenschaften, der Anzahl der Assoziationen, Etiketten und ob ein Objekt privat oder öffentlich ist, filtern. Familien können nach dem Namen des Vaters, der Mutter oder eines Kindes gefiltert werden, Quellen nach Autor und Orte sowie Archive nach ihrem Typ.
- **Erweiterter Filter** – ein Bedingungsbuilder für Filter, die die fertigen nicht ausdrücken können, beschrieben [unten](#erweiterter-filter).
- **GOQL** – ein Textfeld für einen Ausdruck in der [Gramps Object Query Language](goql.md), mit Syntaxhervorhebung. Geben Sie den Ausdruck ein und drücken Sie die Eingabetaste oder klicken Sie auf **Übernehmen**. Wenn der Ausdruck ungültig ist, wird das Feld als Fehler markiert. Ein Ausdruck wird zusätzlich zu den anderen Filtern angewendet.

Aktive Filter werden als Chips in einer Reihe unter der Werkzeugleiste angezeigt. Entfernen Sie einen einzelnen Filter, indem Sie auf die Schaltfläche zum Löschen des Chips klicken, oder verwenden Sie **Alle Filter löschen**, um sie alle auf einmal zu entfernen.

### Erweiterter Filter

Klicken Sie auf **Erweiterter Filter** am Ende des Filterpanels, um den Bedingungsbuilder zu öffnen. Seine Bedingungen sind die Filterregeln, die aus Gramps Desktop bekannt sind, wie "Personen mit dem &lt;name&gt;" oder "Vorfahren von &lt;person&gt;".

- Klicken Sie auf **Bedingung hinzufügen**, um eine Regel auszuwählen. Die Regeln sind in Kategorien gruppiert und können nach Name oder Beschreibung durchsucht werden.
- Füllen Sie die Parameter der Regel aus. Jeder Parameter hat ein passendes Eingabefeld, zum Beispiel ein Datumsfeld, einen Etiketteselektor oder einen Objektauswähler für eine Person oder einen Ort.
- Wählen Sie aus, wie die Bedingungen einer Gruppe kombiniert werden: **Alle Bedingungen**, **Eine Bedingung** oder – über das Menü daneben – **Genau eine Bedingung**.
- Klicken Sie auf **Gruppe hinzufügen**, um eine Gruppe von Bedingungen innerhalb einer anderen Gruppe hinzuzufügen, mit ihrer eigenen Art der Kombination.
- Wählen Sie **Nicht** bei einer Bedingung oder Gruppe, um sie umzukehren.

Klicken Sie auf **Übernehmen**, um die Liste zu filtern.

Die fertigen Filter und der GOQL-Ausdruck, die aktiv sind, wenn Sie den Builder öffnen, erscheinen dort als Bedingungen. Ein GOQL-Ausdruck kann auch als eigene Bedingung hinzugefügt werden, um beispielsweise mehrere Ausdrücke mit **Eine Bedingung** zu kombinieren. Wenn der Filter, den Sie erstellen, mit den fertigen Filtern ausgedrückt werden kann, wird er nach der Anwendung mit ihnen angezeigt. Andernfalls wird er als einzelner **Erweiterter Filter**-Chip angezeigt, und das Filterpanel bietet eine **Bearbeiten**-Schaltfläche, um den Builder erneut zu öffnen.

!!! Hinweis
    Regeln, die sich auf benutzerdefinierte Filter beziehen, die in Gramps Desktop gespeichert sind, sind im Builder nicht verfügbar. Die Regeln werden in Ihrer Sprache mit der Gramps Web API 3.24 oder neuer angezeigt.

## Objekte auswählen und in großen Mengen bearbeiten

Benutzer mit Bearbeitungsberechtigungen sehen eine **Auswählen**-Schaltfläche neben der Filter-Schaltfläche. Klicken Sie darauf, um den Auswahlmodus zu aktivieren, der jeder Zeile ein Kontrollkästchen hinzufügt.

Aktivieren Sie die gewünschten Objekte, und eine Werkzeugleiste erscheint, die anzeigt, wie viele ausgewählt sind, zusammen mit einem **Aktion**-Dropdown und einer **Übernehmen**-Schaltfläche.

Das Kontrollkästchen in der Tabellenüberschrift wählt alle Objekte auf der aktuellen Seite aus. Wenn mehr Objekte den aktuellen Filtern entsprechen, bietet die Werkzeugleiste dann **Alle auswählen (N)** an, was alle N übereinstimmenden Objekte über alle Seiten hinweg auswählt. Das Deaktivieren einer Zeile, das Wechseln der Seite oder der Filter oder das Verlassen des Auswahlmodus beendet diese Auswahl.

### Löschen

Wählen Sie ein oder mehrere Objekte aus, wählen Sie **Löschen** und klicken Sie auf **Übernehmen**. Ein Bestätigungsdialog fordert Sie auf, zu bestätigen, und warnt, dass die Aktion nicht rückgängig gemacht werden kann.

Das Löschen von mehr als zehn Objekten wird als Hintergrundaufgabe ausgeführt. Der Fortschritt wird neben der **Übernehmen**-Schaltfläche und in [Benachrichtigungen](notifications.md) angezeigt, und die Liste wird neu geladen, wenn es abgeschlossen ist.

!!! Tipp
    Löschvorgänge werden in der [Versionshistorie](revisions.md) wie jede andere Änderung aufgezeichnet, sodass ein versehentliches Massenlöschen durch das Rückgängigmachen der entsprechenden Transaktion rückgängig gemacht werden kann.

### Zusammenführen

Wählen Sie **genau zwei** Objekte aus, wählen Sie **Zusammenführen** und klicken Sie auf **Übernehmen**. Ein Dialog fragt, welches der beiden die primären Daten für das zusammengeführte Objekt bereitstellen soll; klicken Sie auf das, das Sie als primär behalten möchten. Die Daten des anderen Objekts werden in es zusammengeführt und die Referenzen werden aktualisiert.

Das Zusammenführen ist für Personen, Familien, Ereignisse, Orte, Quellen und Zitationen verfügbar. Es ist nicht für Archive, Notizen und Medienobjekte verfügbar.

In der Medienansicht funktioniert die Auswahl sowohl im Galerie- als auch im Listenlayout: Im Auswahlmodus wechselt ein Klick auf eine Kachel oder Zeile den Status. **Löschen** ist die einzige Aktion, die für Medien verfügbar ist.

Wenn Sie eine Aktion ohne eine gültige Auswahl wählen – zum Beispiel ein Zusammenführen mit nur einem ausgewählten Objekt – erklärt ein Dialog, was erforderlich ist.
