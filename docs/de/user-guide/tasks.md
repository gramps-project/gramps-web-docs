# Verwenden Sie das integrierte Aufgabenmanagement

Gramps Web enthält ein integriertes genealogisches Aufgabenmanagement-Tool. Es soll Forschern ermöglichen, ihre Aufgaben zu planen und zu priorisieren, aber auch zu dokumentieren. Aus diesem Grund werden Aufgaben als Quellen in der Gramps-Datenbank dargestellt. Nach Abschluss einer Aufgabe kann der zugehörige Inhalt als Quelle dienen, die den Forschungsprozess dokumentiert.

## Grundlagen der Aufgaben

Aufgaben haben die folgenden Eigenschaften:

- Status. Dies kann "Offen", "In Bearbeitung", "Blockiert" oder "Fertig" sein
- Priorität. Dies kann "Niedrig", "Mittel" oder "Hoch" sein
- Etiketten. Die Etiketten sind normale Gramps-Etiketten der zugrunde liegenden Quelle. (Beachten Sie, dass alle Aufgaben zusätzlich das Etikett `ToDo` haben, um sie als Aufgaben zu kennzeichnen, dieses Etikett jedoch in der Aufgabenliste ausgeblendet wird, um Unordnung zu vermeiden.)
- Titel. Wird in der Aufgabenliste angezeigt
- Beschreibung. Ein Rich-Text-Feld, das verwendet werden kann, um die Problemstellung zu beschreiben, aber auch um Fortschritte zu dokumentieren
- Medien. Alle Mediendateien, die an die Aufgabe angehängt sind

## Eine Aufgabe erstellen

Da Aufgaben normale Gramps-Objekte sind, können sie von der gleichen Benutzergruppe bearbeitet oder erstellt werden, die auch andere Objekte (wie Personen oder Ereignisse) bearbeiten oder erstellen kann.

Um eine Aufgabe zu erstellen, klicken Sie auf die Schaltfläche + auf der Seite der Aufgabenliste. Geben Sie mindestens einen Titel ein und optional eine Priorität, eine Beschreibung, Anhänge und Etiketten. Der Status wird bei der Erstellung immer "Offen" sein.

## Die Aufgabenliste

Die Aufgabenliste ist nach Status sortiert – erledigte Aufgaben zuletzt – und innerhalb jedes Status nach Priorität, wobei die höchste zuerst kommt.

Klicken Sie auf eine Aufgabe, um sie zu öffnen. Benutzer mit Bearbeitungsberechtigungen können auch auf das Statussymbol einer Aufgabe klicken, um ihren Status direkt in der Liste zu ändern, zum Beispiel um sie als erledigt zu markieren.

Die **Filter**-Schaltfläche über der Liste filtert die Aufgaben nach Etikett, mit einem [GOQL](goql.md)-Ausdruck oder mit dem [erweiterten Filter](lists.md#advanced-filter).

## Eine Aufgabe bearbeiten

Die Aufgaben-Seite hat keinen separaten "Bearbeitungsmodus" wie andere Gramps-Objekte:

- Klicken Sie auf den Titel, um ihn zu bearbeiten. Drücken Sie Enter, klicken Sie auf ✓ oder klicken Sie woanders, um zu speichern; drücken Sie Escape oder klicken Sie auf ✕, um abzubrechen.
- Änderungen am Status und an der Priorität werden sofort angewendet.
- Um die Beschreibung oder die Anhänge zu bearbeiten, klicken Sie auf die Schaltfläche Bearbeiten neben der Überschrift des Abschnitts. Die Beschreibung wird mit der Schaltfläche "Speichern" darunter gespeichert; das Bearbeiten von Anhängen endet mit **Fertig**.
- Die Schaltfläche für das Schloss legt fest, ob die Aufgabe privat ist. Die Beschreibung der Aufgabe erhält die gleiche Privatsphäre.

Benutzer ohne Bearbeitungsberechtigungen sehen den Status und die Priorität als Text, und Abschnitte ohne Inhalt sind ausgeblendet.

Unter dem Titel sehen Bearbeiter zwei weitere Schaltflächen: **Quelle bearbeiten** öffnet die Quelle, die die Aufgabe darstellt, wo ihre anderen Notizen, Zitationen und Attribute bearbeitet werden können. **Löschen** löscht die Aufgabe nach einer Bestätigung und kehrt zur Aufgabenliste zurück; die angezeigte Nachricht hat eine Rückgängig-Schaltfläche, um die Aufgabe wiederherzustellen.

## Massenänderung von Aufgaben-Eigenschaften

Benutzer mit Bearbeitungsberechtigungen sehen ein Kontrollkästchen in jeder Zeile der Aufgabenliste. Wählen Sie Aufgaben aus und verwenden Sie **Priorität festlegen** oder **Status festlegen** über der Liste, um alle ausgewählten Aufgaben auf einmal zu ändern.

## Aufgaben in Gramps Desktop

Beim Hinzufügen von Aufgaben über Gramps Web haben sowohl die Quellen als auch die Notizen das Etikett `ToDo`, sodass die Aufgaben sowohl im Desktop [To Do Notes Gramplet](https://gramps-project.org/wiki/index.php/Addon:ToDoNotesGramplet) als auch im [To Do Report](https://gramps-project.org/wiki/index.php/Addon:ToDoReport) angezeigt werden.

Um eine Aufgabe in Gramps Desktop hinzuzufügen oder zu bearbeiten, verwenden Sie die folgenden Richtlinien:

- Fügen Sie eine Quelle mit dem Etikett `ToDo` und dem Aufgabentitel als Titel hinzu
- Optional, fügen Sie eine Notiz zur Quelle mit dem Etikett `ToDo`, dem Typ "To Do" und der Beschreibung als Text hinzu
- Fügen Sie ein Attribut "Status" hinzu und setzen Sie es auf "Offen", "In Bearbeitung", "Blockiert" oder "Fertig"
- Fügen Sie ein Attribut "Priorität" hinzu und setzen Sie es auf 9 für niedrig, 5 für mittel oder 1 für hoch (diese kontraintuitiven Werte stammen aus der iCalendar-Spezifikation)
