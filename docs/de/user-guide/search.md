# Suche

Die Suchseite ist erreichbar, indem du auf das Lupensymbol in der oberen App-Leiste klickst oder die Tastenkombination `s` [Tastenkombination](shortcuts.md) drückst.

## Volltextsuche

Gib eine Suchanfrage in das Suchfeld ein. Die Ergebnisse werden während der Eingabe ab dem zweiten Zeichen angezeigt. Drücke die Eingabetaste, um nach einem einzelnen Zeichen zu suchen. Gramps Web durchsucht alle Objekttypen – Personen, Familien, Ereignisse, Orte, Quellen, Zitate, Aufbewahrungsorte, Notizen und Medien – und gibt passende Ergebnisse nach Relevanz sortiert zurück. Um die Suche zu löschen, klicke auf die Löschtaste im Feld oder drücke die Esc-Taste.

Jedes Ergebnis zeigt den Objekttyp, seinen Namen und einige Details an, zum Beispiel die Geburt und den Tod einer Person, die Heirat einer Familie, den Autor einer Quelle oder die erste Zeile einer Notiz. Klicke auf ein beliebiges Ergebnis, um die entsprechende Detailseite zu öffnen.

## Suchsyntax

- **Alle Wörter müssen übereinstimmen.** `Müller Berlin` findet Objekte, die beide Wörter enthalten.
- **`or`** findet Objekte, die eines der beiden Wörter enthalten, z. B. `Meyer or Maier`. Zwischen Wörtern kann auch `and` eingegeben werden, dies macht jedoch keinen Unterschied.
- `or` gilt für die direkt angrenzenden Wörter: `Meyer or Maier Berlin` bedeutet „(Meyer oder Maier) und Berlin“. Klammern werden nicht unterstützt.
- **Anführungszeichen** finden eine Wortgruppe, d. h. Wörter in dieser Reihenfolge: `"Johann Georg"`.
- **Platzhalter:** Ein abschließendes `*` entspricht jeder beliebigen Endung, z. B. findet `Mey*` „Meyer“, „Meyers“, „Meyerhofer“ usw. Dies funktioniert auch für Wortgruppen: `"Johann Georg"*`.
- **Das letzte Wort wird vervollständigt.** Wenn die Suchanfrage mit einem Buchstaben oder einer Ziffer endet, wird so gesucht, als würde sie mit `*` enden. Daher findet `Anna Smi` bereits „Anna Smith“. Um exakt nach dem letzten Wort zu suchen, beende die Suchanfrage mit einem Leerzeichen oder setze das Wort in Anführungszeichen. Dies gilt auch für die Suchfelder der Objektauswahl und der [Karte](map.md#search).
- `or` und `and` werden unabhängig von der Groß- und Kleinschreibung erkannt. Um nach einem dieser Wörter selbst zu suchen, setze es in Anführungszeichen.
- Wörter können nicht ausgeschlossen werden; es gibt kein „not“.

## Was die Suche findet

- Akzente müssen nicht übereinstimmen: „Müller“ findet auch „Muller“, und „muller“ findet „Müller“.
- Familien und Ereignisse werden auch über die Namen ihrer Personen gefunden, z. B. findet „Müller“ die Familien und Ereignisse aller Personen namens Müller. Diese Ergebnisse werden unter direkten Treffern eingeordnet.
- Standardtypen werden über ihre Namen in deiner Oberflächensprache gefunden, z. B. findet „Taufe“ Taufen in der deutschen Oberfläche.
- Unterstriche trennen Wörter. Daher findet „microfilm“ eine Mediendatei namens `scanned_microfilm.png`.
- Benutzer, die private Einträge nicht anzeigen können, finden Objekte nicht über private Informationen, z. B. eine Familie über den Namen eines privaten Mitglieds.

## Filtern nach Objekttyp

Unterhalb des Suchfelds kannst du mit Umschaltflächen für jeden Objekttyp (Personen, Familien, Ereignisse, Orte, …) die Ergebnisse auf einen oder mehrere bestimmte Typen eingrenzen. Standardmäßig werden alle Typen durchsucht. Wenn du eine oder mehrere Umschaltflächen aktivierst, werden die Ergebnisse auf diese Typen beschränkt.
