# Daten importieren

Du kannst einen bestehenden Stammbaum in Gramps Web übernehmen, indem du eine Datei hochlädst, die aus einem anderen Genealogieprogramm, einem Onlinedienst oder aus Gramps Desktop exportiert wurde.

Der Import hat eine eigene Seite, die Stammbaumeigentümern und Administratoren zur Verfügung steht. Öffne sie mit **Stammbaum importieren** im Abschnitt **Daten** der [Administrationseinstellungen](settings.md) (Benutzersymbol in der oberen App-Leiste ▸ Administration). Solange der Stammbaum noch leer ist, führt auch die Schaltfläche **Stammbaum importieren** der Karte „Erste Schritte“ auf der Startseite, im Stammbaum und in den Listen dorthin.

## Welche Datei verwenden?

| Quelle | Stammbaum exportieren als | Dateierweiterung |
|---|---|---|
| Anderes Genealogieprogramm oder Onlinedienst | GEDCOM | `.ged` |
| Gramps Desktop | Gramps XML | `.gramps` |
| GeneWeb | GeneWeb | `.gw` |
| Pro-Gen | Pro-Gen | `.def` |
| Tabellenkalkulation | Gramps CSV | `.csv` |
| Adressbuch | vCard | `.vcf` |

GEDCOM ist das übliche Austauschformat, das fast jedes Genealogieprogramm und jeder Onlinedienst exportieren kann. Suche in deinem Programm oder auf der Website nach einer Option „Exportieren“ oder „Herunterladen“ und wähle GEDCOM, wenn dir mehrere Formate angeboten werden. Die Gramps-Wiki-Seite [Aus einem anderen Genealogieprogramm importieren](https://www.gramps-project.org/wiki/index.php/Import_from_another_genealogy_program) enthält Hinweise zu bestimmten Programmen.

Wenn du Gramps Desktop verwendest, wähle Gramps XML (`.gramps`) statt GEDCOM. Dieses Format enthält alle Gramps-Daten ohne Verluste, und deine Online- und Offline-Stammbäume behalten dieselben Bezeichner, sodass sie [synchronisiert](sync.md) werden können. Siehe unten [Aus Gramps Desktop](#coming-from-gramps-desktop).

## Eine Stammbaumdatei importieren

1. Öffne die Importseite wie oben beschrieben.
2. Wähle unter „Stammbaum importieren“ deine Datei aus und klicke auf **Importieren**. Der Upload-Fortschritt wird angezeigt.
3. Die Datei wird zunächst gelesen, und ein Dialog „Import bestätigen“ zeigt, wie viele Objekte sie enthält (Personen, Familien, Ereignisse, Orte und so weiter), sowie den [Bericht](#the-import-report) des Importers, falls vorhanden. Deinem Stammbaum wurde noch nichts hinzugefügt. Überprüfe, ob die Anzahl plausibel erscheint, und klicke dann auf **Importieren**, um fortzufahren, oder auf **Abbrechen**, um den Vorgang ohne Änderungen zu beenden. Wenn dein Stammbaum bereits Personen enthält, weist der Dialog darauf hin, dass der erneute Import derselben Daten Duplikate erzeugt.
4. Der Import läuft im Hintergrund, und ein Fortschrittsindikator wird angezeigt. Sobald die Daten importiert wurden, wird der Suchindex aktualisiert. Bei einem großen Stammbaum kann dies eine Weile dauern. Wenn der Import fehlschlägt, wird der Grund angezeigt.
5. Wenn der Stammbaum noch keine Hauptperson hat, wirst du aufgefordert, eine auszuwählen.

Überprüfe nach Abschluss des Imports das Ergebnis: Vergleiche die Anzahl der Personen im Bereich **Statistiken** auf der Startseite mit der Anzahl in deinem alten Programm und öffne eine dir gut bekannte Familie, um zu prüfen, ob Eltern, Kinder, Daten und Orte wie erwartet übernommen wurden. Wenn die Datei auf Fotos oder andere Mediendateien verweist, füge diese anschließend unter [Mediendateien importieren](import-media.md) auf derselben Seite hinzu.

!!! warning
    Ein normaler Import fügt ausschließlich Daten hinzu: Er erstellt immer neue Objekte und aktualisiert oder löscht niemals vorhandene Objekte – auch dann nicht, wenn Objekte bereits unter derselben Gramps-ID oder demselben Handle in deinem Stammbaum vorhanden sind. Wenn du dieselbe Datei zweimal importierst oder eine Datei importierst, deren Daten sich mit bereits im Stammbaum vorhandenen Daten überschneiden, wird jedes übereinstimmende Objekt dupliziert, anstatt zusammengeführt oder übersprungen zu werden.

    Wenn du Änderungen, die an anderer Stelle vorgenommen wurden, in einen bereits importierten Stammbaum übernehmen musst, verwende stattdessen [Aus Sicherung wiederherstellen](backups.md#restore-from-backup). Dadurch wird der Stammbaum so ersetzt, dass er der hochgeladenen Datei entspricht, anstatt Daten hinzuzufügen. Dafür benötigst du eine Gramps-XML-Datei oder eine Gramps-Web-Sicherung.

## Der Importbericht

Importer melden, was sie nicht vollständig importieren konnten, beispielsweise GEDCOM-Zeilen, die sie nicht verstanden haben, Verweise auf Datensätze, die in der Datei fehlen, oder ein veraltetes Dateiformat. Der Bericht wird unter **Bericht** sowohl im Bestätigungsdialog als auch nach dem Import angezeigt. Lies ihn, bevor du den Import bestätigst: Er erklärt häufig Probleme, die dir sonst erst später im Stammbaum auffallen würden.

Nicht jede Meldung weist auf ein Problem hin – viele GEDCOM-Dateien enthalten programmspezifische Daten, die gemeldet, aber beibehalten werden; siehe [Programmspezifische Daten](#program-specific-data). Mit den Schaltflächen neben dem Bericht kannst du ihn kopieren oder als Textdatei herunterladen, beispielsweise um im [Forum](../help/help.md) um Hilfe zu bitten.

## Nutzungsgrenzen

Der Serveradministrator kann für deinen Stammbaum Grenzen festlegen (siehe [Serverkonfiguration](../install_setup/configuration.md)). Oben im Abschnitt **Daten** wird die aktuelle Nutzung im Verhältnis zu diesen Grenzen angezeigt:

- **Personen** – die Anzahl der Personenobjekte im Stammbaum im Vergleich zum konfigurierten Maximum (∞ bei unbegrenzter Anzahl)
- **Medienspeicher** – die Gesamtgröße der hochgeladenen Mediendateien im Vergleich zum konfigurierten Speicherkontingent (∞ bei unbegrenztem Speicher)

Ein Import, durch den die Personenanzahl das Limit überschreiten würde, wird vollständig abgelehnt.

## GEDCOM-Dateien

GEDCOM-5.5.1- und GEDCOM-7-Dateien können importiert werden. Dabei solltest du einige Dinge beachten.

### Zeichenkodierung

Eine GEDCOM-5.5.1-Datei gibt ihre Zeichenkodierung im Kopfbereich an. UTF-8-, UTF-16-, ANSEL- und Windows-(ANSI-)Kodierungen werden unterstützt. Wenn Namen mit Akzenten oder anderen Sonderzeichen nach dem Import fehlerhaft dargestellt werden (beispielsweise `MÃ¼ller` statt `Müller), wurde die Datei wahrscheinlich mit einer anderen Kodierung exportiert als der angegebenen. Exportiere die Datei erneut aus deinem alten Programm, wähle dabei UTF-8, falls diese Option angeboten wird, und [beginne von vorn](#starting-over).

GEDCOM-7-Dateien müssen immer als UTF-8 kodiert sein; andere Dateien werden mit dem Fehler „Ungültige GEDCOM-Datei“ abgelehnt.

### Programmspezifische Daten

Viele Programme fügen GEDCOM eigene Erweiterungen hinzu, die andere Programme nicht verstehen. Gramps verwirft solche Daten nicht stillschweigend: Zeilen, die nicht interpretiert werden können, werden in einer Notiz des Typs „GEDCOM-Import“ gesammelt, die der zugehörigen Person, Familie oder dem sonstigen Objekt zugeordnet wird. Überprüfe diese Notizen, um festzustellen, ob wichtige Informationen nicht übernommen wurden.

### Mediendateien

Eine GEDCOM-Datei enthält Verweise auf Mediendateien (beispielsweise Fotos oder gescannte Dokumente), nicht jedoch die Dateien selbst. Nach dem Import existieren die Medienobjekte in deinem Stammbaum, aber ihre Dateien fehlen. Dies wird unter [Status der Mediendateien](import-media.md#media-file-status) angezeigt. Informationen zum Hinzufügen der Dateien findest du unter [Mediendateien importieren](import-media.md).

## Aus Gramps Desktop

Wenn du Gramps Desktop verwendest, sind zwei Schritte erforderlich, um deine Datenbank vorzubereiten und einen reibungslosen Ablauf sicherzustellen.

1. Datenbank überprüfen und reparieren
    - Optional: Erstelle eine Datenbanksicherung, indem du die Datenbank als Gramps XML exportierst.
    - Führe das [Werkzeug „Datenbank überprüfen und reparieren“](https://gramps-project.org/wiki/index.php/Gramps_5.2_Wiki_Manual_-_Tools#Check_and_Repair_Database) aus. Dadurch werden einige interne Inkonsistenzen behoben, die zu Problemen in Gramps Web führen können.
2. Medienpfade in relative Pfade umwandeln
    - Verwende den Gramps-Medienverwalter, um [alle Medienpfade von absolut in relativ umzuwandeln](https://gramps-project.org/wiki/index.php/Gramps_5.2_Wiki_Manual_-_Tools#Convert_paths_from_relative_to_absolute). Beachte, dass Mediendateien außerhalb deines Gramps-Medienverzeichnisses auch bei relativen Pfaden bei der Synchronisierung mit Gramps Web nicht ordnungsgemäß funktionieren.

Exportiere deinen Stammbaum anschließend als Gramps XML (`.gramps`), importiere ihn wie oben beschrieben und [lade deine Mediendateien hoch](import-media.md). Um auf deinem Computer und im Web am selben Stammbaum weiterzuarbeiten, verwende das [Gramps-Web-Sync-Addon](sync.md).

### Warum werden Gramps-XML-Pakete nicht unterstützt?

Gramps XML (`.gramps`) ist zwar das bevorzugte Format für den Datenimport, Gramps-XML-*Pakete* (`.gpkg`) werden von Gramps Web jedoch nicht unterstützt. Der Grund dafür ist, dass die Import- und Exportroutinen für Mediendateien nicht für den Einsatz auf einem Webserver geeignet sind.

## Häufige Probleme

**„Nicht unterstütztes Format“.** Es können nur die [oben](#which-file-to-use) aufgeführten Dateierweiterungen importiert werden. Wenn dein Programm oder Onlinedienst ein ZIP-Archiv bereitgestellt hat, entpacke es und lade die darin enthaltene `.ged`-Datei hoch.

**Alles erscheint doppelt.** Dieselbe Datei wurde zweimal importiert. Da Importe niemals zusammengeführt werden, [beginne von vorn](#starting-over).

**Fehlerhafte Sonderzeichen.** Siehe [Zeichenkodierung](#character-encoding).

**Fotos fehlen.** Siehe [Mediendateien importieren](import-media.md).

### Von vorn beginnen

Wenn beim Import etwas schiefgegangen ist oder du in deinem alten Programm etwas korrigieren und anschließend erneut importieren möchtest, leere zuerst den Stammbaum mit [Alle Objekte löschen](#delete-all-objects) und importiere dann die korrigierte Datei. Beachte, dass dadurch auch alle Änderungen gelöscht werden, die du seit dem Import in Gramps Web vorgenommen hast.

### Alle Objekte löschen

!!! danger
    Das Löschen von Objekten ist **unumkehrbar**. Erstelle eine [Sicherung](backups.md), bevor du fortfährst.

**Alle Objekte löschen** befindet sich im Abschnitt **Gefahrenzone** der [Administrationseinstellungen](settings.md). Wenn du auf **Löschen** klickst, öffnet sich ein Dialog, in dem du auswählen kannst, was gelöscht werden soll:

- **Alle Objekte** – leert den Stammbaum vollständig
- **Bestimmte Objekttypen** – beispielsweise nur Ereignisse oder nur Medienobjekte

Du wirst aufgefordert, dich zur Bestätigung der Aktion erneut zu authentifizieren (dich erneut anzumelden). Der Löschvorgang läuft als Hintergrundaufgabe, und ein Fortschrittsindikator wird angezeigt.

!!! warning
    Das Löschen nur einer Teilmenge von Objekttypen (anstatt aller Objekte gleichzeitig) kann bei großen Stammbäumen sehr lange dauern, da der Server alle Beziehungen zwischen den Objekten überprüfen und aktualisieren muss.
