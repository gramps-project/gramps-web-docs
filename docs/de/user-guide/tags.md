# Etiketten

Etiketten sind Bezeichnungen, die auf jedes Objekt in der Gramps-Datenbank angewendet werden können – Personen, Familien, Ereignisse, Orte, Quellen, Zitationen, Repositories, Notizen und Medien. Sie sind nützlich zum Gruppieren und Filtern von Objekten. Etiketten werden in der Gramps-Familienstammbaum-Datenbank gespeichert und sind für alle Benutzer zugänglich; sie sind auch vollständig kompatibel mit Etiketten, die in Gramps Desktop erstellt wurden.

## Verwaltung von Etiketten

Etiketten werden im Abschnitt **Etiketten** der [Administrations-Einstellungen](../administration/settings.md#tags) verwaltet, der nur für Benutzer mit der Rolle Eigentümer oder Administrator verfügbar ist. Es werden alle vorhandenen Etiketten angezeigt und Sie können:

- **Ein neues Etikett erstellen** mit der Schaltfläche **Neues Etikett**
- **Ein Etikett umbenennen** mit dem Bearbeiten (Bleistift)-Symbol
- **Die Farbe eines Etiketts ändern** mit dem Farbauswahlwerkzeug
- **Ein Etikett löschen** mit dem Löschsymbol

!!! Hinweis
    Das Löschen eines Etiketts entfernt es von allen Objekten, auf die es angewendet wurde.

## Anwenden von Etiketten auf Objekte

Etiketten können auf einem Objekt auf seiner Detailseite im Bearbeitungsmodus angewendet oder entfernt werden. Um viele Objekte auf einmal zu etikettieren, wählen Sie sie in einer Liste aus und verwenden Sie die Aktion **Etikett hinzufügen** oder **Etikett entfernen**, siehe [Listen](lists.md#tags-and-privacy).

Etiketten werden in der **Etiketten**-Spalte der Listen sowie in Suchergebnissen, Lesezeichen und der Historie angezeigt. Wenn eine Liste die Spalte nicht anzeigt, aktivieren Sie sie im Spaltenauswahlwerkzeug.

## Filtern nach Etikett

Alle [Objektlisten-Seiten](lists.md) (Personen, Familien, Ereignisse, Orte, Quellen, Zitationen, Repositories, Notizen, Medien) enthalten einen Etikettenfilter. Verwenden Sie ihn, um nur Objekte anzuzeigen, die ein bestimmtes Etikett haben.

## Besondere Etiketten

Zwei Etiketten haben eine besondere Bedeutung in Gramps Web:

- **`Blog`** – jede Quelle, die mit `Blog` etikettiert ist, wird als Blogbeitrag behandelt und erscheint in der [Blog](blog.md)-Ansicht
- **`ToDo`** – jede Notiz, die mit `ToDo` etikettiert ist, wird als Forschungsaufgabe behandelt und erscheint in der [Aufgaben](tasks.md)-Ansicht

Diese Etiketten werden automatisch erstellt, wenn Sie die Blog- oder Aufgabenfunktionen zum ersten Mal verwenden. Das Umbenennen oder Löschen dieser Etiketten wird die entsprechende Funktion beeinträchtigen.
