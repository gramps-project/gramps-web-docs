# Suche

Die Suchseite ist zugänglich, indem Sie auf das Lupe-Symbol in der oberen App-Leiste klicken oder die `s` [Tastenkombination](shortcuts.md) drücken.

## Volltextsuche

Geben Sie eine beliebige Abfrage in das Suchfeld ein und drücken Sie die Eingabetaste (oder klicken Sie auf die Suchschaltfläche). Gramps Web durchsucht alle Objekttypen – Personen, Familien, Ereignisse, Orte, Quellen, Zitationen, Archive, Notizen und Medien – und gibt übereinstimmende Ergebnisse zurück, die nach Relevanz sortiert sind.

Die Ergebnisse zeigen den Objekttyp, den Namen und eine kurze Zusammenfassung. Klicken Sie auf ein Ergebnis, um die entsprechende Detailseite zu öffnen.

Ein nachgestelltes `*` kann als Platzhalter verwendet werden, z. B. `Mey*` entspricht "Meyer", "Meyers", "Meyerhofer" usw.

## Filtern nach Objekttyp

Unter dem Suchfeld ermöglichen Umschaltknöpfe für jeden Objekttyp (Personen, Familien, Ereignisse, Orte, …) die Eingrenzung der Ergebnisse auf einen oder mehrere spezifische Typen. Standardmäßig werden alle Typen durchsucht. Das Aktivieren eines oder mehrerer Umschalter beschränkt die Ergebnisse nur auf diese Typen.

## Semantische Suche

!!! warning "Veraltet"
    Die semantische Suche ist veraltet und wird in der Gramps Web API 3.25 entfernt. Die oben beschriebene Volltextsuche ist davon nicht betroffen.

Wenn der Serveradministrator die [semantische (KI-gestützte) Suche](../install_setup/chat.md#semantic-search-deprecated) aktiviert hat, erscheint in der oberen rechten Ecke der Suchseite ein Modus-Umschalter mit zwei Optionen:

- **Suche** – standardmäßige Volltextsuche (die Standardoption)
- **Semantisch** – KI-gestützte Suche, die die Bedeutung Ihrer Abfrage versteht, anstatt exakte Wörter zuzuordnen

Die semantische Suche ist nützlich für Abfragen in natürlicher Sprache wie "Bauer in Bayern im 19. Jahrhundert". Sie erfordert, dass der Index für die semantische Suche gefüllt ist; siehe [Verwaltungseinstellungen](../administration/settings.md) für Informationen zum Erstellen oder Aktualisieren des Index.
