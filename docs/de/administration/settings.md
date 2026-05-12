# Verwaltungseinstellungen

Die **Einstellungen > Verwaltung**-Seite ist über das Benutzersymbol in der oberen App-Leiste zugänglich. Sie ist nur für Benutzer mit der Rolle Eigentümer oder Administrator verfügbar und bietet Werkzeuge zur Verwaltung der Familienstammbaum-Datenbank.

## Nutzungskontingente

Oben auf der Seite werden die aktuellen Nutzungen im Verhältnis zu den konfigurierten Limits angezeigt:

- **Personen** – die Anzahl der Personenobjekte im Baum im Vergleich zur konfigurierten maximalen Anzahl (∞, wenn unbegrenzt)
- **Medien-Speicher** – die Gesamtgröße der hochgeladenen Mediendateien im Vergleich zum konfigurierten Speicherkontingent (∞, wenn unbegrenzt)

Kontingente werden vom Serveradministrator festgelegt; siehe [Serverkonfiguration](../install_setup/configuration.md) für Details.

## Daten importieren

Der Importbereich ermöglicht es Ihnen, eine Familienstammbaumdatei oder ein Medienarchiv hochzuladen. Siehe [Daten importieren](import.md) für vollständige Anweisungen.

## Status der Mediendateien

Dieser Abschnitt zeigt:

- Die Gesamtzahl der Medienobjekte im Baum und ob einige eine Prüfziffer vermissen
- Die Anzahl der Medienobjekte, deren zugehörige Datei auf dem Server fehlt

Ein grünes Häkchen zeigt an, dass alles in Ordnung ist. Wenn Probleme festgestellt werden, werden Links zu den betroffenen Objekten angezeigt. Fehlende Prüfziffern treten typischerweise auf, wenn Daten aus einem Format wie GEDCOM importiert wurden, das Medienreferenzen, aber nicht die tatsächlichen Dateien enthält. Die fehlenden Dateien können über die Funktion Medienarchiv importieren hochgeladen werden.

## Medienarchiv importieren

Ermöglicht das Hochladen einer ZIP-Datei mit Mediendateien, um fehlende Dateien zu ergänzen. Siehe [Daten importieren](import.md) für vollständige Anweisungen.

## Suchindex verwalten

Gramps Web führt einen Volltext-Suchindex, der normalerweise automatisch aktualisiert wird, wenn sich Daten ändern. Der Statusindikator zeigt, wie viele Objekte derzeit indiziert sind im Vergleich zur Gesamtanzahl der Objekte.

Klicken Sie auf **Suchindex aktualisieren**, um einen vollständigen Neuaufbau auszulösen. Ein Fortschrittsindikator wird angezeigt, während die Aufgabe im Hintergrund ausgeführt wird. Dies ist normalerweise nur nach einem Server-Upgrade erforderlich.

### Semantischer Suchindex

Wenn der Server die [semantische (KI-gestützte) Suche aktiviert hat](../install_setup/configuration.md), erscheint ein zusätzlicher Abschnitt mit zwei Aktionen:

- **Semantischen Suchindex regenerieren** – baut den gesamten semantischen Index von Grund auf neu. Dies ist rechenintensiv und kann lange dauern.
- **Semantischen Suchindex aktualisieren** – führt ein inkrementelles Update durch, bei dem nur Objekte hinzugefügt werden, die noch nicht indiziert sind. Schneller als ein vollständiger Neuaufbau.

## Name des Familienstammbaums

!!! note
    Das Umbenennen des Baums funktioniert nur in einer [Multi-Baum-Konfiguration](../install_setup/multi-tree.md) oder wenn `TREE_ID` explizit in der [Serverkonfiguration](../install_setup/configuration.md) festgelegt ist. Bei einer Standardinstallation mit einem einzelnen Baum ohne festgelegte `TREE_ID` wird ein Fehler angezeigt.

Dies ermöglicht das Ändern des Namens der zugrunde liegenden Gramps-Familienstammbaum-Datenbank. Geben Sie einen neuen Namen ein und klicken Sie auf **Umbenennen**, um die Änderung anzuwenden.

## Datenbank überprüfen und reparieren

Dieses Tool überprüft die Gramps-Datenbank auf interne Inkonsistenzen und behebt die, die es kann – analog zum [Tool Datenbank überprüfen und reparieren](https://www.gramps-project.org/wiki/index.php/Gramps_5.2_Wiki_Manual_-_Tools#Check_and_Repair_Database) in Gramps Desktop.

Klicken Sie auf **Überprüfen und Reparieren** und warten Sie, bis der Fortschrittsindikator abgeschlossen ist. Das Ergebnis wird unter dem Button angezeigt:

- Wenn keine Fehler gefunden wurden, wird eine Bestätigungsnachricht angezeigt.
- Wenn Fehler gefunden wurden, wird eine Zusammenfassung der durchgeführten Reparaturen angezeigt.

Führen Sie dieses Tool aus, wenn Sie unerwartete Fehler oder Verhaltensweisen feststellen, die durch Datenbankinkonsistenzen verursacht werden könnten, wie z. B. fehlende Beziehungen zwischen Objekten.

## Gefahrenzone

!!! danger
    Aktionen in der Gefahrenzone sind **irreversibel**. Machen Sie ein Backup, bevor Sie fortfahren.

### Alle Objekte löschen

Entfernt Objekte aus dem Familienstammbaum. Ein Klick auf **Löschen** öffnet einen Dialog, in dem Sie wählen können, ob Sie löschen möchten:

- **Alle Objekte** – leert den Baum vollständig
- **Spezifische Objekttypen** – zum Beispiel nur Ereignisse oder nur Medienobjekte

Sie werden aufgefordert, sich erneut zu authentifizieren (sich erneut einzuloggen), um die Aktion zu bestätigen. Die Löschung wird als Hintergrundaufgabe ausgeführt und ein Fortschrittsindikator wird angezeigt.

!!! warning
    Das Löschen nur eines Teils der Objekttypen (anstatt aller Objekte auf einmal) kann für große Bäume sehr lange dauern, da der Server alle Beziehungen zwischen den Objekten überprüfen und aktualisieren muss.

!!! tip
    Verwenden Sie dies, um frisch zu starten, bevor Sie einen neuen Baum importieren, oder um spezifische Objekttypen zu entfernen, die falsch importiert wurden.
