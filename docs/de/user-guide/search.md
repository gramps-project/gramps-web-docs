# Suche

Die Suchseite ist zugänglich, indem Sie auf das Lupe-Symbol in der oberen App-Leiste klicken oder die `s` [Tastenkombination](shortcuts.md) drücken.

## Volltextsuche

Geben Sie eine beliebige Abfrage in das Suchfeld ein und drücken Sie die Eingabetaste (oder klicken Sie auf die Schaltfläche "Suchen"). Gramps Web durchsucht alle Objekttypen – Personen, Familien, Ereignisse, Orte, Quellen, Zitationen, Archive, Notizen und Medien – und gibt übereinstimmende Ergebnisse zurück, die nach Relevanz sortiert sind.

Die Ergebnisse zeigen den Objekttyp, den Namen und eine kurze Zusammenfassung. Klicken Sie auf ein Ergebnis, um die entsprechende Detailseite zu öffnen.

## Suchsyntax

- **Alle Wörter müssen übereinstimmen.** `Müller Berlin` findet Objekte, die beide Wörter enthalten.
- **`or`** findet Objekte, die entweder das eine oder das andere Wort enthalten, z.B. `Meyer or Maier`. `and` kann ebenfalls zwischen Wörtern eingegeben werden, hat jedoch keinen Einfluss.
- `or` gilt für die direkt daneben stehenden Wörter: `Meyer or Maier Berlin` bedeutet "(Meyer or Maier) und Berlin". Klammern werden nicht unterstützt.
- **Anführungszeichen** entsprechen einem Satz, d.h. Wörtern in dieser Reihenfolge: `"Johann Georg"`.
- **Wildcard:** ein abschließendes `*` entspricht jeder Endung, z.B. `Mey*` entspricht "Meyer", "Meyers", "Meyerhofer" usw. Dies funktioniert auch für Sätze: `"Johann Georg"*`.
- `or` und `and` werden in jeder Schreibweise erkannt. Um eines dieser Wörter selbst zu suchen, setzen Sie es in Anführungszeichen.
- Wörter können nicht ausgeschlossen werden; es gibt kein "nicht".

## Was die Suche findet

- Akzente müssen nicht übereinstimmen: "Müller" findet auch "Muller", und "muller" findet "Müller".
- Familien und Ereignisse werden auch durch die Namen ihrer Personen gefunden, z.B. "Müller" findet die Familien und Ereignisse aller, die Müller heißen. Diese Ergebnisse werden unter direkten Übereinstimmungen eingestuft.
- Standardtypen werden durch ihre Namen in Ihrer Benutzeroberflächensprache gefunden, z.B. "Taufe" findet Taufen in der deutschen Benutzeroberfläche.
- Unterstriche trennen Wörter, sodass "microfilm" eine Mediendatei mit dem Namen `scanned_microfilm.png` findet.
- Benutzer, die private Aufzeichnungen nicht einsehen können, finden keine Objekte durch private Informationen, wie z.B. eine Familie durch den Namen eines privaten Mitglieds.

## Filtern nach Objekttyp

Unter dem Suchfeld ermöglichen Umschaltknöpfe für jeden Objekttyp (Personen, Familien, Ereignisse, Orte, …) die Einschränkung der Ergebnisse auf einen oder mehrere spezifische Typen. Standardmäßig werden alle Typen durchsucht. Das Aktivieren eines oder mehrerer Umschalter beschränkt die Ergebnisse nur auf diese Typen.
