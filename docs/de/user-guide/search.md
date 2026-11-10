# Suche

Die Suchseite ist zugänglich, indem Sie auf das Lupensymbol in der oberen App-Leiste klicken oder die `s` [Tastenkombination](shortcuts.md) drücken.

## Volltextsuche

Geben Sie eine Abfrage in das Suchfeld ein. Die Ergebnisse erscheinen, während Sie tippen, ab dem zweiten Zeichen; drücken Sie die Eingabetaste, um nach einem einzelnen Zeichen zu suchen. Gramps Web durchsucht alle Objekttypen – Personen, Familien, Ereignisse, Orte, Quellen, Zitationen, Archive, Notizen und Medien – und gibt übereinstimmende Ergebnisse zurück, die nach Relevanz sortiert sind. Um die Suche zu löschen, klicken Sie auf die Schaltfläche zum Löschen im Feld oder drücken Sie die Escape-Taste.

Jedes Ergebnis zeigt den Objekttyp, seinen Namen und einige Details, zum Beispiel das Geburts- und Sterbedatum einer Person, die Heiratsdaten einer Familie, den Autor einer Quelle oder die erste Zeile einer Notiz. Klicken Sie auf ein Ergebnis, um die entsprechende Detailseite zu öffnen.

## Suchsyntax

- **Alle Wörter müssen übereinstimmen.** `Müller Berlin` findet Objekte, die beide Wörter enthalten.
- **`oder`** findet Objekte, die entweder das eine oder das andere Wort enthalten, z.B. `Meyer oder Maier`. `und` kann auch zwischen Wörtern eingegeben werden, macht jedoch keinen Unterschied.
- `oder` gilt für die direkt daneben stehenden Wörter: `Meyer oder Maier Berlin` bedeutet "(Meyer oder Maier) und Berlin". Klammern werden nicht unterstützt.
- **Anführungszeichen** entsprechen einer Phrase, d.h. Wörtern in dieser Reihenfolge: `"Johann Georg"`.
- **Platzhalter:** ein nachgestelltes `*` entspricht jeder Endung, z.B. `Mey*` entspricht "Meyer", "Meyers", "Meyerhofer" usw. Dies funktioniert auch für Phrasen: `"Johann Georg"*`.
- **Das letzte Wort wird vervollständigt.** Wenn die Abfrage mit einem Buchstaben oder einer Ziffer endet, wird sie so durchsucht, als ob sie mit `*` endete, sodass `Anna Smi` bereits "Anna Smith" findet. Um das letzte Wort genau zu suchen, beenden Sie die Abfrage mit einem Leerzeichen oder setzen Sie das Wort in Anführungszeichen. Dasselbe gilt für die Suchfelder der Objektauswähler und die [Karte](map.md#search).
- `oder` und `und` werden in jeder Schreibweise erkannt. Um eines dieser Wörter selbst zu suchen, setzen Sie es in Anführungszeichen.
- Wörter können nicht ausgeschlossen werden; es gibt kein "nicht".

## Was die Suche findet

- Akzente müssen nicht übereinstimmen: "Müller" findet auch "Muller", und "muller" findet "Müller".
- Familien und Ereignisse werden auch über die Namen ihrer Personen gefunden, z.B. "Müller" findet die Familien und Ereignisse aller Personen mit dem Namen Müller. Diese Ergebnisse werden unter direkten Übereinstimmungen eingestuft.
- Standardtypen werden durch ihre Namen in Ihrer Benutzersprache gefunden, z.B. "Taufe" findet Taufen in der deutschen Benutzeroberfläche.
- Unterstriche trennen Wörter, sodass "microfilm" eine Mediendatei mit dem Namen `scanned_microfilm.png` findet.
- Benutzer, die private Datensätze nicht einsehen können, finden keine Objekte durch private Informationen, wie z.B. eine Familie durch den Namen eines privaten Mitglieds.

## Filtern nach Objekttyp

Unter dem Suchfeld ermöglichen Umschaltknöpfe für jeden Objekttyp (Personen, Familien, Ereignisse, Orte, …) eine Eingrenzung der Ergebnisse auf einen oder mehrere spezifische Typen. Standardmäßig werden alle Typen durchsucht. Das Aktivieren eines oder mehrerer Schalter beschränkt die Ergebnisse nur auf diese Typen.
