# Daten importieren

Sie können einen bestehenden Stammbaum in Gramps Web importieren, indem Sie eine Datei hochladen, die aus einem anderen Genealogieprogramm, einem Online-Dienst oder von Gramps Desktop exportiert wurde.

Der Import befindet sich im Abschnitt **Daten** der [Administrations-Einstellungen](settings.md) (Benutzersymbol in der oberen App-Leiste ▸ Verwaltung), der für Baum-Eigentümer und Administratoren verfügbar ist. Während der Baum noch leer ist, führt der **Familienstammbaum importieren**-Button auf der "Loslegen"-Karte der Startseite ebenfalls dorthin.

## Welche Datei zu verwenden

| Kommt von | Exportieren Sie Ihren Baum als | Dateiendung |
|---|---|---|
| Ein anderes Genealogieprogramm oder Online-Dienst | GEDCOM | `.ged` |
| Gramps Desktop | Gramps XML | `.gramps` |
| GeneWeb | GeneWeb | `.gw` |
| Pro-Gen | Pro-Gen | `.def` |
| Eine Tabellenkalkulation | Gramps CSV | `.csv` |
| Ein Adressbuch | vCard | `.vcf` |

GEDCOM ist das gängige Austauschformat, das fast jedes Genealogieprogramm und jeden Online-Dienst exportieren kann. Suchen Sie in Ihrem Programm oder auf der Website nach einer "Exportieren"- oder "Herunterladen"-Option und wählen Sie GEDCOM, wenn Ihnen mehrere Formate angeboten werden. Die Gramps-Wiki-Seite [Import aus einem anderen Genealogieprogramm](https://www.gramps-project.org/wiki/index.php/Import_from_another_genealogy_program) enthält Hinweise zu bestimmten Programmen.

Wenn Sie Gramps Desktop verwenden, wählen Sie Gramps XML (`.gramps`) anstelle von GEDCOM. Es trägt alle Gramps-Daten ohne Verlust und Ihre Online- und Offline-Bäume behalten die gleichen Identifikatoren, sodass sie [synchronisiert](sync.md) werden können. Siehe [Kommt von Gramps Desktop](#coming-from-gramps-desktop) unten.

## Eine Familienstammbaum-Datei importieren

1. Öffnen Sie den Abschnitt **Daten** der Administrations-Einstellungen.
2. Wählen Sie unter "Familienstammbaum importieren" Ihre Datei aus und klicken Sie auf **Importieren**.
3. Die Datei wird zuerst analysiert, und ein Dialogfeld "Import bestätigen" zeigt an, wie viele Objekte sie enthält (Personen, Familien, Ereignisse, Orte usw.). Nichts wurde bisher zu Ihrem Baum hinzugefügt. Überprüfen Sie, ob die Zählungen plausibel erscheinen, und klicken Sie dann auf **Importieren**, um fortzufahren, oder auf **Abbrechen**, um ohne Änderungen abzubrechen.
4. Der Import läuft im Hintergrund und ein Fortschrittsindikator wird angezeigt. Sobald die Daten importiert sind, wird der Suchindex aktualisiert, was bei einem großen Baum eine Weile dauern kann.

Wenn der Import abgeschlossen ist, überprüfen Sie das Ergebnis: Vergleichen Sie die Anzahl der Personen im **Statistik**-Panel auf der Startseite mit der Anzahl in Ihrem alten Programm und öffnen Sie eine Familie, die Sie gut kennen, um zu sehen, dass Eltern, Kinder, Daten und Orte wie erwartet übertragen wurden.

!!! warning
    Ein regulärer Import ist rein additiv: Er erstellt immer neue Objekte und aktualisiert oder löscht niemals vorhandene, selbst für Objekte, die bereits in Ihrem Baum unter derselben Gramps-ID oder -Bezeichnung existieren. Wenn Sie dieselbe Datei zweimal importieren – oder eine Datei importieren, die sich mit bereits im Baum vorhandenen Daten überschneidet – werden alle übereinstimmenden Objekte dupliziert, anstatt sie zusammenzuführen oder zu überspringen.

    Wenn Sie Änderungen, die anderswo an einem bereits importierten Baum vorgenommen wurden, einbringen müssen, verwenden Sie stattdessen [Wiederherstellen aus Backup](settings.md#restore-from-backup), das den Baum ersetzt, um der hochgeladenen Datei zu entsprechen, anstatt ihn zu ergänzen. Dies erfordert eine Gramps XML-Datei oder ein Gramps Web-Backup.

Wenn eine Begrenzung der Anzahl der Personen für Ihren Baum festgelegt wurde (siehe [Nutzungsquoten](settings.md#usage-quotas)), wird ein Import, der diese überschreiten würde, insgesamt abgelehnt.

## GEDCOM-Dateien

Sowohl GEDCOM 5.5.1- als auch GEDCOM 7-Dateien können importiert werden. Es gibt einige Dinge zu beachten.

### Zeichencodierung

Eine GEDCOM 5.5.1-Datei gibt ihre Zeichencodierung in ihrem Header an. UTF-8, UTF-16, ANSEL und Windows (ANSI) Codierungen werden unterstützt. Wenn Namen mit Akzenten oder anderen Sonderzeichen nach dem Import verzerrt erscheinen (zum Beispiel `MÃ¼ller` anstelle von `Müller`), wurde die Datei wahrscheinlich mit einer anderen Codierung exportiert, als sie angibt. Exportieren Sie die Datei erneut aus Ihrem alten Programm und wählen Sie UTF-8, wenn es eine Auswahl bietet, und [fangen Sie neu an](#starting-over).

GEDCOM 7-Dateien müssen immer als UTF-8 codiert sein; andere Dateien werden mit einem "Ungültige GEDCOM-Datei"-Fehler abgelehnt.

### Programmspezifische Daten

Viele Programme fügen GEDCOM ihre eigenen Erweiterungen hinzu, die andere Programme nicht verstehen. Gramps verwirft solche Daten nicht stillschweigend: Zeilen, die es nicht interpretieren kann, werden in einer Notiz des Typs "GEDCOM-Import" gesammelt, die der Person, Familie oder einem anderen Objekt angehängt ist, zu dem sie gehören. Überprüfen Sie diese Notizen, um zu sehen, ob etwas Wichtiges nicht übertragen wurde.

### Mediendateien

Eine GEDCOM-Datei enthält Verweise auf Mediendateien (wie Fotos oder gescannte Dokumente), jedoch nicht die Dateien selbst. Nach dem Import existieren die Medienobjekte in Ihrem Baum, aber ihre Dateien fehlen, was unter [Status der Mediendateien](settings.md#media-file-status) angezeigt wird. Um die Dateien hinzuzufügen, siehe [Mediendateien importieren](#import-media-files) unten.

## Kommt von Gramps Desktop

Wenn Sie Gramps Desktop verwenden, gibt es zwei Schritte, um Ihre Datenbank vorzubereiten, um sicherzustellen, dass alles reibungslos verläuft.

1. Überprüfen und reparieren Sie die Datenbank
    - Optional: Erstellen Sie ein Datenbank-Backup, indem Sie in Gramps XML exportieren.
    - Führen Sie das [Tool zur Überprüfung und Reparatur der Datenbank](https://gramps-project.org/wiki/index.php/Gramps_5.2_Wiki_Manual_-_Tools#Check_and_Repair_Database) aus. Dies behebt einige interne Inkonsistenzen, die zu Problemen in Gramps Web führen könnten.
2. Konvertieren Sie Medienpfade in relative
    - Verwenden Sie den Gramps Medienmanager, um [alle Medienpfade von absolut auf relativ zu konvertieren](https://gramps-project.org/wiki/index.php/Gramps_5.2_Wiki_Manual_-_Tools#Convert_paths_from_relative_to_absolute). Beachten Sie, dass selbst bei relativen Pfaden alle Mediendateien außerhalb Ihres Gramps-Medienverzeichnisses nicht richtig funktionieren, wenn sie mit Gramps Web synchronisiert werden.

Exportieren Sie dann Ihren Baum in Gramps XML (`.gramps`), importieren Sie ihn wie oben beschrieben und laden Sie Ihre Mediendateien wie im nächsten Abschnitt beschrieben hoch. Um an demselben Baum auf Ihrem Computer und im Web weiterzuarbeiten, verwenden Sie das [Gramps Web Sync-Addon](sync.md).

### Warum keine Unterstützung für Gramps XML-Paket?

Während Gramps XML (`.gramps`) das bevorzugte Format für den Import von Daten ist, wird das Gramps XML *Paket* (`.gpkg`) von Gramps Web nicht unterstützt. Dies liegt daran, dass die Import- und Export-Routinen für Mediendateien nicht für die Verwendung auf einem Webserver geeignet sind.

## Mediendateien importieren

Wenn Sie einen Familienstammbaum importiert haben und die entsprechenden Mediendateien hochladen müssen, verwenden Sie **Mediendateien importieren** im Datenbereich der Administrations-Einstellungen. Es erwartet eine ZIP-Datei, die die fehlenden Mediendateien enthält. Dateien werden auf eine der beiden Arten mit Medienobjekten in Ihrem Baum abgeglichen:

- **Nach Prüfziffer.** Für Medienobjekte, die eine Prüfziffer haben – wie es bei Bäumen der Fall ist, die aus Gramps Desktop importiert wurden – wird die Datei mit der übereinstimmenden Prüfziffer verwendet, unabhängig von ihrem Namen oder der Ordnerstruktur in der ZIP-Datei. Dies funktioniert nur, wenn die Prüfziffern in der Gramps-Datenbank korrekt sind, was durch das Ausführen des Überprüfungs- und Reparaturtools sichergestellt wird.
- **Nach Pfad.** Medienobjekte ohne Prüfziffer – wie es typischerweise nach einem GEDCOM-Import der Fall ist – werden nach ihrem Pfad abgeglichen: Die ZIP-Datei muss die Datei unter genau dem relativen Pfad enthalten, der im Medienobjekt gespeichert ist.

Wenn die in Ihrer GEDCOM-Datei gespeicherten Pfade absolut sind (zum Beispiel `C:\Users\...\photo.jpg`), funktioniert der Abgleich nach Pfad nicht. In diesem Fall wird empfohlen, zuerst alles in Gramps Desktop zu importieren, das mehr Optionen bietet, um vorhandene Mediendateien mit einem importierten Baum zu verknüpfen, und dann zu Gramps Web zu wechseln, wie in [Kommt von Gramps Desktop](#coming-from-gramps-desktop) beschrieben.

## Häufige Probleme

**"Nicht unterstütztes Format".** Nur die oben aufgeführten Dateiendungen [können importiert werden](#which-file-to-use). Wenn Ihr Programm oder Online-Dienst Ihnen ein ZIP-Archiv gegeben hat, entpacken Sie es und laden Sie die darin enthaltene `.ged`-Datei hoch.

**Alles erscheint doppelt.** Dieselbe Datei wurde zweimal importiert. Da Importe niemals zusammengeführt werden, [fangen Sie neu an](#starting-over).

**Verzerrte Sonderzeichen.** Siehe [Zeichencodierung](#character-encoding).

**Fotos fehlen.** Siehe [Mediendateien importieren](#import-media-files).

### Neu anfangen

Wenn ein Import schiefgelaufen ist oder Sie etwas in Ihrem alten Programm beheben und erneut importieren möchten, leeren Sie zuerst den Baum mit [Alle Objekte löschen](settings.md#delete-all-objects) im Gefahrenbereich der Administrations-Einstellungen und importieren Sie dann die korrigierte Datei. Beachten Sie, dass dies auch alle Änderungen löscht, die Sie seit dem Import in Gramps Web vorgenommen haben.
