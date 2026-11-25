# Listen

Jeder Objekttyp in Gramps Web verfügt über eine Listenansicht: Personen, Familien, Ereignisse, Orte, Quellen, Zitate, Repositorien, Notizen und Medien. Sie funktionieren alle auf dieselbe Weise und verwenden dieselben Werkzeuge zum Sortieren, Filtern und Bearbeiten in großen Mengen.

## Sortieren und Seiten

Klicke auf eine Spaltenüberschrift, um nach dieser Spalte zu sortieren; klicke erneut darauf, um die Reihenfolge umzukehren. Die Sortierung wird vom Server durchgeführt und gilt daher für die gesamte Liste, nicht nur für die angezeigte Seite.

Lange Listen werden auf mehrere Seiten aufgeteilt. Verwende die Seitennavigation am unteren Rand, um zwischen den Seiten zu wechseln.

Auf schmalen Bildschirmen wechselt die Tabelle automatisch zu einem kompakten Layout, sodass Listenansichten auch auf einem Smartphone verwendbar bleiben.

## Spalten auswählen

Klicke auf das Zahnradsymbol am rechten Ende der Werkzeugleiste über der Liste, um den Dialog **Spalten** zu öffnen. Aktiviere oder deaktiviere eine Spalte, um sie ein- oder auszublenden. **Zurücksetzen** stellt die Standardauswahl für diese Liste wieder her.

Mindestens eine Spalte muss sichtbar bleiben, daher kann die letzte verbleibende Spalte nicht deaktiviert werden.

Neben den Standardsäulen bietet jede Liste eine Spalte **Etiketten** und für Benutzer, die private Datensätze anzeigen können, eine Spalte **Privatsphäre**, die für jedes private Objekt ein Schloss anzeigt. Wenn du die Spaltenauswahl einer Liste zuvor geändert hast, werden neue Spalten wie **Etiketten** nicht automatisch hinzugefügt; aktiviere sie im Dialog.

Deine Spaltenauswahl wird pro Objekttyp und Familienstammbaum gespeichert. Sie wird in deinem Browser gespeichert und ist daher für andere Benutzer nicht sichtbar – sie wird jedoch auch nicht in einen anderen Browser oder auf ein anderes Gerät übernommen.

## Filtern

Klicke auf die Schaltfläche **Filter**, um das Filterfenster zu öffnen. Es bietet drei kombinierbare Filtermöglichkeiten:

- **Vorgefertigte Filter** in aufklappbaren Abschnitten, die vom Objekttyp abhängen. Bei Personen kannst du beispielsweise nach Name, Geburtsjahr, Todesjahr, verschiedenen Personeneigenschaften, der Anzahl der Verknüpfungen, Etiketten und danach filtern, ob ein Objekt privat oder öffentlich ist. Familien können nach dem Namen des Vaters, der Mutter oder eines Kindes gefiltert werden, Quellen nach dem Autor sowie Orte und Repositorien nach ihrem Typ.
- **Erweiterter Filter** – ein Bedingungsgenerator für Filter, die mit den vorgefertigten Filtern nicht ausgedrückt werden können, beschrieben [weiter unten](#erweiterter-filter).
- **GOQL** – ein Textfeld für einen Ausdruck in der [Gramps Object Query Language](goql.md) mit Syntaxhervorhebung. Gib den Ausdruck ein und drücke die Eingabetaste oder klicke auf **Anwenden**. Wenn der Ausdruck ungültig ist, wird das Feld als fehlerhaft markiert. Ein Ausdruck wird zusätzlich zu den anderen Filtern angewendet.

Aktive Filter werden als Chips in einer Zeile unter der Werkzeugleiste angezeigt. Entferne einen einzelnen Filter, indem du auf die Schaltfläche zum Löschen des Chips klickst, oder verwende **Alle Filter löschen**, um alle Filter gleichzeitig zu entfernen.

### Erweiterter Filter

Klicke am unteren Rand des Filterfensters auf **Erweiterter Filter**, um den Bedingungsgenerator zu öffnen. Seine Bedingungen sind die aus Gramps Desktop bekannten Filterregeln, beispielsweise „Personen mit dem &lt;Namen&gt;“ oder „Vorfahren von &lt;Person&gt;“.

- Klicke auf **Bedingung hinzufügen**, um eine Regel auszuwählen. Die Regeln sind in Kategorien gruppiert und können nach Name oder Beschreibung durchsucht werden.
- Fülle die Parameter der Regel aus. Jeder Parameter verfügt über eine passende Eingabe, beispielsweise ein Datumsfeld, eine Etikettenauswahl oder eine Objektauswahl für eine Person oder einen Ort.
- Wähle aus, wie die Bedingungen einer Gruppe kombiniert werden: **Alle Bedingungen**, **Beliebige Bedingung** oder – über das Menü daneben – **Genau eine Bedingung**.
- Klicke auf **Gruppe hinzufügen**, um innerhalb einer anderen Gruppe eine Gruppe von Bedingungen mit einer eigenen Kombinationsmethode hinzuzufügen.
- Wähle bei einer Bedingung oder Gruppe **Nicht**, um sie umzukehren.

Klicke auf **Anwenden**, um die Liste zu filtern.

Die vorgefertigten Filter und der GOQL-Ausdruck, die beim Öffnen des Generators aktiv sind, werden dort als Bedingungen angezeigt. Ein GOQL-Ausdruck kann auch als eigene Bedingung hinzugefügt werden, beispielsweise um mehrere Ausdrücke mit **Beliebige Bedingung** zu kombinieren. Wenn der von dir erstellte Filter mit den vorgefertigten Filtern ausgedrückt werden kann, wird er nach dem Anwenden zusammen mit diesen angezeigt. Andernfalls wird er als einzelner Chip **Erweiterter Filter** angezeigt, und das Filterfenster bietet eine Schaltfläche **Bearbeiten**, um den Generator erneut zu öffnen.

!!! note
    Regeln, die sich auf in Gramps Desktop gespeicherte benutzerdefinierte Filter beziehen, sind im Generator nicht verfügbar. Die Regeln werden mit Gramps Web API 3.24 oder neuer in deiner Sprache angezeigt.

#### Gespeicherte Filter

Um einen von dir erstellten Filter wiederzuverwenden, klicke im Bedingungsgenerator auf **Speichern** und gib ihm einen Namen. Beim Speichern unter einem bereits vorhandenen Namen wird dieser Filter ersetzt. **Gespeicherte Filter** im Generator führt die gespeicherten Filter für den aktuellen Objekttyp auf; durch Auswahl eines Filters wird er in den Generator geladen, wo du ihn vor dem Klicken auf **Anwenden** ändern kannst.

Gespeicherte Filter werden in deinem Browser pro Familienstammbaum und Objekttyp gespeichert und sind daher für andere Benutzer oder auf deinen anderen Geräten nicht verfügbar.

Ein gespeicherter Filter kann nicht mehr funktionieren, wenn sich der Stammbaum ändert, beispielsweise wenn er sich auf eine inzwischen gelöschte Person bezieht (die Objektauswahl zeigt dann „Nicht gefunden“ an). Ein solcher Filter kann erst angewendet oder gespeichert werden, wenn die Bedingung korrigiert wurde.

## Objekte auswählen und gesammelt bearbeiten

Benutzer mit Bearbeitungsberechtigungen sehen neben der Filterschaltfläche eine Schaltfläche **Auswählen**. Klicke darauf, um den Auswahlmodus zu aktivieren, der jeder Zeile ein Kontrollkästchen hinzufügt.

Aktiviere die gewünschten Objekte. Daraufhin wird eine Werkzeugleiste angezeigt, die angibt, wie viele Objekte ausgewählt sind, und ein Dropdown-Menü **Aktion** sowie eine Schaltfläche **Anwenden** enthält.

Das Kontrollkästchen in der Tabellenüberschrift wählt alle Objekte auf der aktuellen Seite aus. Wenn weitere Objekte den aktuellen Filtern entsprechen, bietet die Werkzeugleiste anschließend **Alle auswählen (N)** an, wodurch alle N passenden Objekte auf allen Seiten ausgewählt werden. Durch das Deaktivieren einer Zeile, das Wechseln der Seite oder der Filter oder das Verlassen des Auswahlmodus wird diese Auswahl beendet.

### Löschen

Wähle ein oder mehrere Objekte aus, wähle **Löschen** und klicke auf **Anwenden**. Ein Bestätigungsdialog fordert dich zur Bestätigung auf und weist darauf hin, dass die Aktion nicht rückgängig gemacht werden kann.

Das Löschen von mehr als zehn Objekten wird als Hintergrundaufgabe ausgeführt. Der Fortschritt wird neben der Schaltfläche **Anwenden** und in den [Benachrichtigungen](notifications.md) angezeigt. Nach Abschluss wird die Liste neu geladen.

!!! tip
    Löschvorgänge werden wie jede andere Änderung in der [Änderungshistorie](revisions.md) aufgezeichnet, sodass ein versehentliches Löschen in großen Mengen durch Rückgängigmachen der entsprechenden Transaktion rückgängig gemacht werden kann.

### Etiketten und Privatsphäre

Die Aktionen **Etikett hinzufügen**, **Etikett entfernen** und **Privatsphäre** ändern alle ausgewählten Objekte gleichzeitig (erfordert Gramps Web API 3.26 oder neuer):

- **Etikett hinzufügen** fügt ein vorhandenes Etikett oder ein neues Etikett hinzu, das du im Dialog erstellst.
- **Etikett entfernen** entfernt ein Etikett von den ausgewählten Objekten, die dieses Etikett besitzen.
- **Privatsphäre** markiert die ausgewählten Objekte als privat oder öffentlich. Dies ändert nur die Objekte selbst, nicht ihre Bestandteile oder die Datensätze, auf die sie verweisen – siehe [Private Datensätze](privacy.md).

Wie beim Löschen wird die Bearbeitung von mehr als zehn Objekten als Hintergrundaufgabe ausgeführt. Die Änderungen werden als eine Transaktion in der [Änderungshistorie](revisions.md) aufgezeichnet, sodass sie gemeinsam rückgängig gemacht werden können.

### Zusammenführen

Wähle **genau zwei** Objekte aus, wähle **Zusammenführen** und klicke auf **Anwenden**. Ein Dialog fragt, welches der beiden Objekte die Primärdaten für das zusammengeführte Objekt bereitstellen soll; klicke auf das Objekt, das du als primär beibehalten möchtest. Die Daten des anderen Objekts werden darin zusammengeführt und Verweise werden aktualisiert.

Das Zusammenführen ist für Personen, Familien, Ereignisse, Orte, Quellen und Zitate verfügbar. Für Repositorien, Notizen und Medienobjekte ist es nicht verfügbar.

In der Medienansicht funktioniert die Auswahl sowohl in der Galerie- als auch in der Listenansicht: Im Auswahlmodus wird ein Objekt durch Klicken auf eine Kachel oder Zeile ausgewählt bzw. die Auswahl aufgehoben. Medienobjekte können nicht zusammengeführt werden.

Wenn du eine Aktion ohne gültige Auswahl auswählst – beispielsweise das Zusammenführen mit nur einem ausgewählten Objekt –, erklärt ein Dialog, was erforderlich ist.
