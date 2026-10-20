# Listen

Jeder Objekttyp in Gramps Web hat eine Listenansicht: Personen, Familien, Ereignisse, Orte, Quellen, Zitationen, Repositories, Notizen und Medien. Sie funktionieren alle gleich und teilen sich die gleichen Werkzeuge zum Sortieren, Filtern und Bearbeiten in großen Mengen.

## Sortieren und Seitenwechsel

Klicken Sie auf die Spaltenüberschrift, um nach dieser Spalte zu sortieren; klicken Sie erneut darauf, um die Reihenfolge umzukehren. Das Sortieren erfolgt durch den Server, sodass es für die gesamte Liste gilt, nicht nur für die Seite, die Sie gerade ansehen.

Lange Listen werden in Seiten aufgeteilt. Verwenden Sie die Paginierungssteuerungen am Ende, um zwischen ihnen zu wechseln.

Auf schmalen Bildschirmen wechselt die Tabelle automatisch zu einem kompakten Layout, sodass die Listenansichten auch auf einem Telefon nutzbar bleiben.

## Spalten auswählen

Klicken Sie auf das Zahnrad-Symbol über der Liste, um den **Spalten**-Dialog zu öffnen. Aktivieren oder deaktivieren Sie eine Spalte, um sie anzuzeigen oder auszublenden. **Zurücksetzen** stellt die Standardauswahl für diese Liste wieder her.

Mindestens eine Spalte muss sichtbar bleiben, sodass die letzte verbleibende Spalte nicht deaktiviert werden kann.

Ihre Spaltenauswahl wird pro Objekttyp und pro Stammbaum gespeichert. Sie wird in Ihrem Browser gespeichert, sodass sie für andere Benutzer nicht sichtbar ist – aber sie folgt Ihnen auch nicht zu einem anderen Browser oder Gerät.

## Filtern

Klicken Sie auf die **Filter**-Schaltfläche, um das Filterpanel zu öffnen. Es bietet drei Möglichkeiten zum Filtern, die kombiniert werden können:

- **Fertige Filter** in zusammenklappbaren Abschnitten, die vom Objekttyp abhängen. Für Personen können Sie beispielsweise nach Geburtsjahr, Sterbejahr, verschiedenen Personenmerkmalen, der Anzahl der Verbindungen, Etiketten und ob ein Objekt privat oder öffentlich ist, filtern.
- **Erweiterter Filter** – ein Bedingungsbuilder für Filter, die die fertigen nicht ausdrücken können, beschrieben [unten](#erweiterter-filter).
- **GQL** – ein Textfeld für eine Abfrage in der [Gramps Query Language](gql.md). Geben Sie die Abfrage ein und drücken Sie die Eingabetaste oder klicken Sie auf **Übernehmen**. Wenn die Abfrage ungültig ist, wird der Rahmen des Feldes rot. Eine Abfrage wird zusätzlich zu den anderen Filtern angewendet.

Aktive Filter werden als Chips über der Liste angezeigt. Entfernen Sie einen einzelnen Filter, indem Sie auf die Löschtaste des Chips klicken, oder verwenden Sie **Alle Filter löschen**, um sie alle auf einmal zu entfernen.

### Erweiterter Filter

Klicken Sie auf **Erweiterter Filter** am Ende des Filterpanels, um den Bedingungsbuilder zu öffnen. Seine Bedingungen sind die Filterregeln, die aus Gramps Desktop bekannt sind, wie "Personen mit dem &lt;name&gt;" oder "Vorfahren von &lt;person&gt;".

- Klicken Sie auf **Bedingung hinzufügen**, um eine Regel auszuwählen. Die Regeln sind in Kategorien gruppiert und können nach Name oder Beschreibung durchsucht werden.
- Füllen Sie die Parameter der Regel aus. Jeder Parameter hat ein passendes Eingabefeld, beispielsweise ein Datumsfeld, einen Etiketteselektor oder einen Objektauswähler für eine Person oder einen Ort.
- Wählen Sie aus, wie die Bedingungen einer Gruppe kombiniert werden: **Alle Bedingungen**, **Eine Bedingung** oder – über das Menü daneben – **Genau eine Bedingung**.
- Klicken Sie auf **Gruppe hinzufügen**, um eine Gruppe von Bedingungen innerhalb einer anderen Gruppe hinzuzufügen, mit ihrer eigenen Art der Kombination.
- Wählen Sie **Nicht** für eine Bedingung oder Gruppe, um sie umzukehren.

Klicken Sie auf **Übernehmen**, um die Liste zu filtern.

Die aktiven fertigen Filter, die Sie beim Öffnen des Builders haben, erscheinen dort als Bedingungen. Wenn der Filter, den Sie erstellen, mit den fertigen Filtern ausgedrückt werden kann, wird er nach dem Anwenden zusammen mit ihnen angezeigt. Andernfalls wird er als einzelner **Erweiterter Filter**-Chip angezeigt, und das Filterpanel bietet eine **Bearbeiten**-Schaltfläche, um den Builder erneut zu öffnen.

!!! Hinweis
    Regeln, die auf benutzerdefinierte Filter verweisen, die in Gramps Desktop gespeichert sind, sind im Builder nicht verfügbar. Die Regeln werden in Ihrer Sprache mit Gramps Web API 3.24 oder neuer angezeigt.

## Objekte auswählen und in großen Mengen bearbeiten

Benutzer mit Bearbeitungsberechtigungen sehen eine **Auswählen**-Schaltfläche neben der Filter-Schaltfläche. Klicken Sie darauf, um den Auswahlmodus zu aktivieren, der jeder Zeile ein Kontrollkästchen hinzufügt.

Aktivieren Sie die gewünschten Objekte, und eine Symbolleiste erscheint, die anzeigt, wie viele ausgewählt sind, zusammen mit einem **Aktion**-Dropdown und einer **Übernehmen**-Schaltfläche.

### Löschen

Wählen Sie ein oder mehrere Objekte aus, wählen Sie **Löschen** und klicken Sie auf **Übernehmen**. Ein Bestätigungsdialog fordert Sie zur Bestätigung auf und warnt, dass die Aktion nicht rückgängig gemacht werden kann.

!!! Tipp
    Löschvorgänge werden in der [Versionsgeschichte](revisions.md) wie jede andere Änderung aufgezeichnet, sodass ein versehentliches Massenlöschen durch das Rückgängigmachen der entsprechenden Transaktion rückgängig gemacht werden kann.

### Zusammenführen

Wählen Sie **genau zwei** Objekte aus, wählen Sie **Zusammenführen** und klicken Sie auf **Übernehmen**. Ein Dialog fragt, welches der beiden die primären Daten für das zusammengeführte Objekt bereitstellen soll; klicken Sie auf das, das Sie als primär behalten möchten. Die Daten des anderen Objekts werden in es zusammengeführt und die Referenzen werden aktualisiert.

Das Zusammenführen ist für Personen, Familien, Ereignisse, Orte, Quellen und Zitationen verfügbar. Es ist nicht für Repositories, Notizen und Medienobjekte verfügbar.

Wenn Sie eine Aktion ohne eine gültige Auswahl wählen – beispielsweise ein Zusammenführen mit nur einem ausgewählten Objekt – erklärt ein Dialog, was erforderlich ist.
