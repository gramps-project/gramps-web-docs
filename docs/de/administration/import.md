# Daten importieren

Sie können einen bestehenden Stammbaum in Gramps Web importieren, indem Sie eine Datei hochladen, die aus einem anderen Genealogieprogramm, einem Online-Dienst oder von Gramps Desktop exportiert wurde.

Der Import befindet sich im Abschnitt **Daten** der [Administrations-Einstellungen](settings.md) (Benutzersymbol in der oberen App-Leiste ▸ Administration), der für Baum-Eigentümer und Administratoren verfügbar ist. Während der Baum noch leer ist, führt die Schaltfläche **Familienstammbaum importieren** auf der "Loslegen"-Karte der Startseite ebenfalls dorthin.

## Welche Datei verwenden

| Kommt von | Exportieren Sie Ihren Baum als | Dateierweiterung |
|---|---|---|
| Ein anderes Genealogieprogramm oder Online-Dienst | GEDCOM | `.ged` |
| Gramps Desktop | Gramps XML | `.gramps` |
| GeneWeb | GeneWeb | `.gw` |
| Pro-Gen | Pro-Gen | `.def` |
| Eine Tabellenkalkulation | Gramps CSV | `.csv` |
| Ein Adressbuch | vCard | `.vcf` |

GEDCOM ist das gängige Austauschformat, das fast jedes Genealogieprogramm und jeden Online-Dienst exportieren kann. Suchen Sie in Ihrem Programm oder auf der Website nach einer "Exportieren"- oder "Herunterladen"-Option und wählen Sie GEDCOM, wenn Ihnen mehrere Formate angeboten werden. Die Gramps-Wiki-Seite [Import aus einem anderen Genealogieprogramm](https://www.gramps-project.org/wiki/index.php/Import_from_another_genealogy_program) enthält Hinweise zu spezifischen Programmen.

Wenn Sie Gramps Desktop verwenden, wählen Sie Gramps XML (`.gramps`) anstelle von GEDCOM. Es enthält alle Gramps-Daten ohne Verlust, und Ihre Online- und Offline-Bäume behalten die gleichen Identifikatoren, sodass sie [synchronisiert](sync.md) werden können. Siehe [Kommt von Gramps Desktop](#coming-from-gramps-desktop) unten.

## Eine Familienstammbaum-Datei importieren

1. Öffnen Sie den Abschnitt **Daten** der Administrations-Einstellungen.
2. Wählen Sie unter "Familienstammbaum importieren" Ihre Datei aus und klicken Sie auf **Importieren**.
3. Die Datei wird zuerst analysiert, und ein Dialogfeld "Import bestätigen" zeigt an, wie viele Objekte sie enthält (Personen, Familien, Ereignisse, Orte usw.). Nichts wurde bisher zu Ihrem Baum hinzugefügt. Überprüfen Sie, ob die Zählungen plausibel erscheinen, und klicken Sie dann auf **Importieren**, um fortzufahren, oder auf **Abbrechen**, um ohne Änderungen abzubrechen.
4. Der Import läuft im Hintergrund, und ein Fortschrittsindikator wird angezeigt. Sobald die Daten importiert sind, wird der Suchindex aktualisiert, was bei einem großen Baum eine Weile dauern kann. Wenn der Import fehlschlägt, wird der Grund angezeigt.

Wenn der Import abgeschlossen ist, überprüfen Sie das Ergebnis: Vergleichen Sie die Anzahl der Personen im **Statistik**-Panel auf der Startseite mit der Anzahl in Ihrem alten Programm und öffnen Sie eine Familie, die Sie gut kennen, um zu sehen, dass Eltern, Kinder, Daten und Orte wie erwartet übertragen wurden.

!!! warning
    Ein regulärer Import ist rein additiv: Er erstellt immer neue Objekte und aktualisiert oder löscht niemals vorhandene, selbst für Objekte, die bereits in Ihrem Baum unter derselben Gramps-ID oder -Bezeichnung existieren. Das zweimalige Importieren derselben Datei – oder das Importieren einer Datei, die sich mit bereits im Baum vorhandenen Daten überschneidet – wird jedes übereinstimmende Objekt duplizieren, anstatt es zusammenzuführen oder zu überspringen.

    Wenn Sie Änderungen, die anderswo an einem bereits importierten Baum vorgenommen wurden, übernehmen müssen, verwenden Sie stattdessen [Wiederherstellen aus Backup](backups.md#restore-from-backup), das den Baum ersetzt, um der hochgeladenen Datei zu entsprechen, anstatt ihn zu ergänzen. Dies erfordert eine Gramps XML-Datei oder ein Gramps Web-Backup.

## Nutzungskontingente

Der Serveradministrator kann Limits für Ihren Baum festlegen (siehe [Serverkonfiguration](../install_setup/configuration.md)). Oben im Abschnitt **Daten** wird die aktuelle Nutzung im Verhältnis zu diesen Limits angezeigt:

- **Personen** – die Anzahl der Personenobjekte im Baum im Vergleich zur konfigurierten maximalen Anzahl (∞, wenn unbegrenzt)
- **Medien-Speicher** – die Gesamtgröße der hochgeladenen Mediendateien im Vergleich zum konfigurierten Speicherplatzkontingent (∞, wenn unbegrenzt)

Ein Import, der das Limit für die Anzahl der Personen überschreiten würde, wird als Ganzes abgelehnt.

## GEDCOM-Dateien

Sowohl GEDCOM 5.5.1- als auch GEDCOM 7-Dateien können importiert werden. Es gibt einige Dinge, die zu beachten sind.

### Zeichencodierung

Eine GEDCOM 5.5.1-Datei gibt ihre Zeichencodierung in ihrem Header an. UTF-8, UTF-16, ANSEL und Windows (ANSI) Codierungen werden unterstützt. Wenn Namen mit Akzenten oder anderen Sonderzeichen nach dem Import verzerrt aussehen (zum Beispiel `MÃ¼ller` anstelle von `Müller`), wurde die Datei wahrscheinlich mit einer anderen Codierung exportiert, als sie angibt. Exportieren Sie die Datei erneut aus Ihrem alten Programm und wählen Sie UTF-8, wenn Ihnen eine Auswahl angeboten wird, und [fangen Sie neu an](#starting-over).

GEDCOM 7-Dateien müssen immer als UTF-8 codiert sein; andere Dateien werden mit einem Fehler "Ungültige GEDCOM-Datei" abgelehnt.

### Programmspezifische Daten

Viele Programme fügen GEDCOM ihre eigenen Erweiterungen hinzu, die andere Programme nicht verstehen. Gramps verwirft solche Daten nicht stillschweigend: Zeilen, die es nicht interpretieren kann, werden in einer Notiz des Typs "GEDCOM-Import" gesammelt, die der Person, Familie oder einem anderen Objekt zugeordnet ist, zu dem sie gehören. Überprüfen Sie diese Notizen, um zu sehen, ob etwas Wichtiges nicht übertragen wurde.

### Mediendateien

Eine GEDCOM-Datei enthält Verweise auf Mediendateien (wie Fotos oder gescannte Dokumente), jedoch nicht die Dateien selbst. Nach dem Import existieren die Medienobjekte in Ihrem Baum, aber ihre Dateien fehlen, was unter [Status der Mediendateien](import-media.md#media-file-status) angezeigt wird. Um die Dateien hinzuzufügen, siehe [Mediendateien importieren](import-media.md).

## Kommt von Gramps Desktop

Wenn Sie Gramps Desktop verwenden, gibt es zwei Schritte, um Ihre Datenbank vorzubereiten, um sicherzustellen, dass alles reibungslos funktioniert.

1. Überprüfen und reparieren Sie die Datenbank
    - Optional: Erstellen Sie ein Datenbank-Backup, indem Sie in Gramps XML exportieren.
    - Führen Sie das [Tool zur Überprüfung und Reparatur der Datenbank](https://gramps-project.org/wiki/index.php/Gramps_5.2_Wiki_Manual_-_Tools#Check_and_Repair_Database) aus. Dies behebt einige interne Inkonsistenzen, die zu Problemen in Gramps Web führen könnten.
2. Konvertieren Sie Medienpfade in relative
    - Verwenden Sie den Gramps Medienmanager, um [alle Medienpfade von absolut auf relativ zu konvertieren](https://gramps-project.org/wiki/index.php/Gramps_5.2_Wiki_Manual_-_Tools#Convert_paths_from_relative_to_absolute). Beachten Sie, dass selbst bei relativen Pfaden alle Mediendateien außerhalb Ihres Gramps-Medienverzeichnisses nicht ordnungsgemäß funktionieren, wenn sie mit Gramps Web synchronisiert werden.

Exportieren Sie dann Ihren Baum in Gramps XML (`.gramps`), importieren Sie ihn wie oben beschrieben und [laden Sie Ihre Mediendateien hoch](import-media.md). Um an demselben Baum auf Ihrem Computer und im Web weiterzuarbeiten, verwenden Sie das [Gramps Web Sync-Addon](sync.md).

### Warum keine Unterstützung für Gramps XML-Paket?

Während Gramps XML (`.gramps`) das bevorzugte Format für den Import von Daten ist, wird das Gramps XML *Paket* (`.gpkg`) von Gramps Web nicht unterstützt. Dies liegt daran, dass die Import- und Export-Routinen für Mediendateien nicht für die Verwendung auf einem Webserver geeignet sind.

## Häufige Probleme

**"Nicht unterstütztes Format".** Nur die oben aufgeführten Dateierweiterungen [können importiert werden](#which-file-to-use). Wenn Ihr Programm oder Online-Dienst Ihnen ein ZIP-Archiv gegeben hat, entpacken Sie es und laden Sie die darin enthaltene `.ged`-Datei hoch.

**Alles erscheint doppelt.** Dieselbe Datei wurde zweimal importiert. Da Importe niemals zusammengeführt werden, [fangen Sie neu an](#starting-over).

**Verzerrte Sonderzeichen.** Siehe [Zeichencodierung](#character-encoding).

**Fotos fehlen.** Siehe [Mediendateien importieren](import-media.md).

### Neu anfangen

Wenn ein Import schiefgegangen ist oder Sie etwas in Ihrem alten Programm korrigieren und erneut importieren möchten, leeren Sie zuerst den Baum mit [Alle Objekte löschen](#delete-all-objects), und importieren Sie dann die korrigierte Datei. Beachten Sie, dass dies auch alle Änderungen löscht, die Sie seit dem Import in Gramps Web vorgenommen haben.

### Alle Objekte löschen

!!! danger
    Das Löschen von Objekten ist **irreversibel**. Machen Sie ein [Backup](backups.md), bevor Sie fortfahren.

**Alle Objekte löschen** befindet sich im Abschnitt **Gefahrenzone** der [Administrations-Einstellungen](settings.md). Ein Klick auf **Löschen** öffnet ein Dialogfeld, in dem Sie wählen können, ob Sie löschen möchten:

- **Alle Objekte** – leert den Baum vollständig
- **Bestimmte Objekttypen** – zum Beispiel nur Ereignisse oder nur Medienobjekte

Sie werden aufgefordert, sich erneut zu authentifizieren (sich erneut anzumelden), um die Aktion zu bestätigen. Das Löschen wird als Hintergrundaufgabe ausgeführt, und ein Fortschrittsindikator wird angezeigt.

!!! warning
    Das Löschen nur einer Teilmenge von Objekttypen (anstatt aller Objekte auf einmal) kann bei großen Bäumen sehr lange dauern, da der Server alle Beziehungen zwischen Objekten überprüfen und aktualisieren muss.
