# Verwenden Sie das integrierte Aufgabenmanagement

Gramps Web enthält ein integriertes genealogisches Aufgabenmanagement-Tool. Es soll Forschern ermöglichen, ihre Aufgaben zu planen und zu priorisieren, aber auch zu dokumentieren. Aus diesem Grund werden Aufgaben als Quellen in der Gramps-Datenbank dargestellt. Nach Abschluss einer Aufgabe kann der zugehörige Inhalt als Quelle dienen, die den Forschungsprozess dokumentiert.

## Grundlagen der Aufgaben

Aufgaben haben die folgenden Eigenschaften:

- Status. Dies kann "Offen", "In Bearbeitung", "Blockiert" oder "Fertig" sein
- Priorität. Dies kann "Niedrig", "Mittel" oder "Hoch" sein
- Tags. Die Labels sind normale Gramps-Tags der zugrunde liegenden Quelle. (Beachten Sie, dass alle Aufgaben zusätzlich das Label `ToDo` haben, um sie als Aufgaben zu kennzeichnen, aber dieses Label in der Aufgabenliste ausgeblendet ist, um Unordnung zu vermeiden.)
- Titel. Wird in der Aufgabenliste angezeigt
- Beschreibung. Ein Rich-Text-Feld, das verwendet werden kann, um die Problemstellung zu beschreiben, aber auch um Fortschritte zu dokumentieren
- Medien. Alle Mediendateien, die an die Aufgabe angehängt sind

## Eine Aufgabe erstellen

Da Aufgaben normale Gramps-Objekte sind, können sie von derselben Benutzergruppe bearbeitet oder erstellt werden, die auch andere Objekte (wie Personen oder Ereignisse) bearbeiten oder erstellen kann.

Um eine Aufgabe zu erstellen, klicken Sie auf die Schaltfläche + auf der Seite der Aufgabenliste. Geben Sie mindestens einen Titel ein. Der Status wird bei der Erstellung immer "Offen" sein.

## Eine Aufgabe bearbeiten

Um Details einer Aufgabe zu ändern, klicken Sie auf die Aufgabe in der Aufgabenliste.

Die Detailseite der Aufgabe hat keinen separaten "Bearbeitungsmodus" wie andere Gramps-Objekte. Änderungen am Titel, Status und an der Priorität werden sofort angewendet. Änderungen an der Rich-Text-Beschreibung erfordern, dass Sie die Schaltfläche "Speichern" darunter klicken.

## Massenänderung von Aufgaben-Eigenschaften

Die Priorität und der Status von Aufgaben können in großen Mengen geändert werden, indem die Kontrollkästchen in der Aufgabenliste zur Auswahl verwendet und die entsprechenden Schaltflächen über der Aufgabenliste betätigt werden.

## Aufgaben in Gramps Desktop

Beim Hinzufügen von Aufgaben über Gramps Web werden sowohl die Quellen als auch die Notizen mit dem Tag `ToDo` versehen, sodass die Aufgaben im Desktop [To Do Notes Gramplet](https://gramps-project.org/wiki/index.php/Addon:ToDoNotesGramplet) sowie im [To Do Report](https://gramps-project.org/wiki/index.php/Addon:ToDoReport) angezeigt werden.

Um eine Aufgabe in Gramps Desktop hinzuzufügen oder zu bearbeiten, verwenden Sie die folgenden Richtlinien:

- Fügen Sie eine Quelle mit dem Tag `ToDo` und dem Aufgabentitel als Titel hinzu
- Optional: Fügen Sie der Quelle eine Notiz mit dem Tag `ToDo`, dem Typ "To Do" und der Beschreibung als Text hinzu
- Fügen Sie ein Attribut "Status" hinzu und setzen Sie es auf "Offen", "In Bearbeitung", "Blockiert" oder "Fertig"
- Fügen Sie ein Attribut "Priorität" hinzu und setzen Sie es auf 9 für niedrig, 5 für mittel oder 1 für hoch (diese kontraintuitiven Werte stammen aus der iCalendar-Spezifikation)
