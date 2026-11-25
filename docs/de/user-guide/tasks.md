# Verwende die integrierte Aufgabenverwaltung

Gramps Web enthält ein integriertes genealogisches Aufgabenverwaltungswerkzeug. Es soll Forschenden ermöglichen, ihre Aufgaben zu planen und zu priorisieren, aber auch zu dokumentieren. Deshalb werden Aufgaben in der Gramps-Datenbank als Quellen dargestellt. Nach Abschluss einer Aufgabe können die zugehörigen Inhalte als Quelle dienen, die den Forschungsprozess dokumentiert.

## Grundlagen von Aufgaben

Aufgaben haben die folgenden Eigenschaften:

- Status. Dieser kann „Offen“, „In Bearbeitung“, „Blockiert“ oder „Erledigt“ sein
- Priorität. Diese kann „Niedrig“, „Mittel“ oder „Hoch“ sein
- Etiketten. Die Etiketten sind normale Gramps-Etiketten der zugrunde liegenden Quelle. (Beachte, dass alle Aufgaben zusätzlich das Etikett `ToDo` haben, um sie als Aufgaben zu identifizieren. Dieses Etikett wird jedoch in der Aufgabenliste ausgeblendet, um Unübersichtlichkeit zu vermeiden.)
- Titel. Wird in der Aufgabenliste angezeigt
- Beschreibung. Ein Rich-Text-Feld, das verwendet werden kann, um die Problemstellung zu beschreiben, aber auch, um bereits erzielte Fortschritte zu dokumentieren
- Medien. Alle Mediendateien, die an die Aufgabe angehängt sind

## Eine Aufgabe erstellen

Da Aufgaben normale Gramps-Objekte sind, können sie von derselben Benutzergruppe bearbeitet oder erstellt werden, die auch andere Objekte (wie Personen oder Ereignisse) bearbeiten oder erstellen kann.

Um eine Aufgabe zu erstellen, klicke auf der Seite mit der Aufgabenliste auf die Schaltfläche +. Gib mindestens einen Titel und optional eine Priorität, eine Beschreibung, Anhänge und Etiketten ein. Der Status ist beim Erstellen immer „Offen“.

## Die Aufgabenliste

Standardmäßig ist die Aufgabenliste nach Status sortiert – erledigte Aufgaben zuletzt – und innerhalb jedes Status nach Priorität, wobei die höchste Priorität zuerst angezeigt wird. Das Sortiermenü in der Filterleiste sortiert außerdem nach Priorität, Titel oder letzter Änderung (neueste zuerst).

Klicke auf eine Aufgabe, um sie zu öffnen. Benutzer mit Bearbeitungsberechtigungen können auch direkt in der Liste auf das Statussymbol einer Aufgabe klicken, um deren Status zu ändern, beispielsweise um sie als erledigt zu markieren.

Die Schaltfläche **Filter** über der Liste filtert die Aufgaben nach Titel, Status, Priorität oder Etikett, mit einem [GOQL](goql.md)-Ausdruck oder mit dem [erweiterten Filter](lists.md#advanced-filter). Wenn mehrere Status oder Prioritäten ausgewählt werden, werden Aufgaben mit einem beliebigen dieser Werte angezeigt, beispielsweise alle offenen und blockierten Aufgaben.

## Eine Aufgabe bearbeiten

Die Aufgabenseite verfügt nicht wie andere Gramps-Objekte über einen separaten „Bearbeitungsmodus“:

- Klicke auf den Titel, um ihn zu bearbeiten. Drücke die Eingabetaste, klicke auf ✓ oder klicke an eine andere Stelle, um zu speichern; drücke die Escape-Taste oder klicke auf ✕, um abzubrechen.
- Änderungen an Status und Priorität werden sofort angewendet.
- Um die Beschreibung oder die Anhänge zu bearbeiten, klicke auf die Bearbeitungsschaltfläche neben der Überschrift des Abschnitts. Die Beschreibung wird mit der Schaltfläche „Speichern“ darunter gespeichert; die Bearbeitung von Anhängen endet mit **Fertig**.
- Die Schaltfläche zum Sperren legt fest, ob die Aufgabe privat ist. Für die Beschreibung der Aufgabe gilt dieselbe Privatsphäre.

Benutzer ohne Bearbeitungsberechtigungen sehen Status und Priorität als Text, und Abschnitte ohne Inhalt werden ausgeblendet.

Unterhalb des Titels sehen Bearbeiter zwei weitere Schaltflächen: **Quelle bearbeiten** öffnet die Quelle, die die Aufgabe darstellt. Dort können die anderen Notizen, Zitate und Attribute bearbeitet werden. **Löschen** löscht die Aufgabe nach einer Bestätigung und kehrt zur Aufgabenliste zurück; die angezeigte Meldung enthält eine Rückgängig-Schaltfläche, mit der die Aufgabe wiederhergestellt werden kann.

## Aufgabenigenschaften gesammelt ändern

Benutzer mit Bearbeitungsberechtigungen sehen in jeder Zeile der Aufgabenliste ein Kontrollkästchen. Wähle Aufgaben aus und verwende **Priorität festlegen** oder **Status festlegen** über der Liste, um alle ausgewählten Aufgaben gleichzeitig zu ändern.

## Aufgaben in Gramps Desktop

Wenn Aufgaben über Gramps Web hinzugefügt werden, wird sowohl den Quellen als auch den Notizen das Etikett `ToDo` zugewiesen. Dadurch werden die Aufgaben sowohl im Desktop-[To Do Notes Gramplet](https://gramps-project.org/wiki/index.php/Addon:ToDoNotesGramplet) als auch im [To Do Report](https://gramps-project.org/wiki/index.php/Addon:ToDoReport) angezeigt.

Um eine Aufgabe in Gramps Desktop hinzuzufügen oder zu bearbeiten, befolge die folgenden Richtlinien

- Füge eine Quelle mit dem Etikett `ToDo` und dem Aufgabentitel als Titel hinzu
- Füge der Quelle optional eine Notiz mit dem Etikett `ToDo`, dem Typ „To Do“ und der Beschreibung als Text hinzu
- Füge ein Attribut „Status“ hinzu und setze es auf „Offen“, „In Bearbeitung“, „Blockiert“ oder „Erledigt“
- Füge ein Attribut „Priorität“ hinzu und setze es auf 9 für niedrig, 5 für mittel oder 1 für hoch (diese kontraintuitiven Werte stammen aus der iCalendar-Spezifikation)
