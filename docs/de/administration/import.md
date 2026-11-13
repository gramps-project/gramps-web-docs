# Daten importieren

Sie können einen bestehenden Stammbaum in Gramps Web importieren, indem Sie eine Datei hochladen, die aus einem anderen Genealogieprogramm, einem Online-Dienst oder von Gramps Desktop exportiert wurde.

Der Import befindet sich im Abschnitt **Daten** der [Verwaltungseinstellungen](settings.md) (Benutzersymbol in der oberen App-Leiste ▸ Verwaltung), der für Baum-Eigentümer und Administratoren verfügbar ist. Während der Baum noch leer ist, führt der Button **Familienstamm importieren** auf der "Loslegen"-Karte der Startseite ebenfalls dorthin.

## Welche Datei zu verwenden

| Kommt von | Exportieren Sie Ihren Stammbaum als | Dateierweiterung |
|---|---|---|
| Ein anderes Genealogieprogramm oder Online-Dienst | GEDCOM | `.ged` |
| Gramps Desktop | Gramps XML | `.gramps` |
| GeneWeb | GeneWeb | `.gw` |
| Pro-Gen | Pro-Gen | `.def` |
| Eine Tabelle | Gramps CSV | `.csv` |
| Ein Adressbuch | vCard | `.vcf` |

GEDCOM ist das gängige Austauschformat, das fast jedes Genealogieprogramm und jeden Online-Dienst exportieren kann. Suchen Sie nach einer "Exportieren"- oder "Herunterladen"-Option in Ihrem Programm oder auf der Website und wählen Sie GEDCOM, wenn Ihnen mehrere Formate angeboten werden. Die Gramps-Wiki-Seite [Import von einem anderen Genealogieprogramm](https://www.gramps-project.org/wiki/index.php/Import_from_another_genealogy_program) enthält Hinweise zu spezifischen Programmen.

Wenn Sie Gramps Desktop verwenden, wählen Sie Gramps XML (`.gramps`) anstelle von GEDCOM. Es enthält alle Gramps-Daten ohne Verlust, und Ihre Online- und Offline-Bäume behalten die gleichen Identifikatoren, sodass sie [synchronisiert](sync.md) werden können. Siehe [Kommt von Gramps Desktop](#coming-from-gramps-desktop) unten.

## Eine Familienstammdaten-Datei importieren

1. Öffnen Sie den Abschnitt **Daten** der Verwaltungseinstellungen.
2. Wählen Sie unter "Familienstamm importieren" Ihre Datei aus und klicken Sie auf **Importieren**.
3. Die Datei wird zuerst analysiert, und ein Dialogfeld "Import bestätigen" zeigt an, wie viele Objekte sie enthält (Personen, Familien, Ereignisse, Orte usw.). Nichts wurde bisher zu Ihrem Baum hinzugefügt. Überprüfen Sie, ob die Zählungen plausibel erscheinen, und klicken Sie dann auf **Importieren**, um fortzufahren, oder auf **Abbrechen**, um ohne Änderungen abzubrechen.
4. Der Import läuft im Hintergrund, und ein Fortschrittsindikator wird angezeigt. Sobald die Daten importiert sind, wird der Suchindex aktualisiert, was bei einem großen Baum eine Weile dauern kann. Wenn der Import fehlschlägt, wird der Grund angezeigt.

Wenn der Import abgeschlossen ist, überprüfen Sie das Ergebnis: Vergleichen Sie die Anzahl der Personen im **Statistik**-Panel auf der Startseite mit der Anzahl in Ihrem alten Programm und öffnen Sie eine Familie, die Sie gut kennen, um zu sehen, ob Eltern, Kinder, Daten und Orte wie erwartet übertragen wurden.

!!! warning
    Ein regulärer Import ist rein additiv: Er erstellt immer neue Objekte und aktualisiert oder löscht niemals vorhandene, selbst für Objekte, die bereits in Ihrem Baum unter derselben Gramps-ID oder -Bezeichnung existieren. Das Importieren derselben Datei zweimal – oder das Importieren einer Datei, die sich mit bereits im Baum vorhandenen Daten überschneidet – wird jedes übereinstimmende Objekt duplizieren, anstatt es zusammenzuführen oder zu überspringen.

    Wenn Sie Änderungen, die anderswo an einem bereits importierten Baum vorgenommen wurden, einbringen müssen, verwenden Sie stattdessen [Wiederherstellen aus Backup](settings.md#restore-from-backup), das den Baum ersetzt, um der hochgeladenen Datei zu entsprechen, anstatt ihn zu ergänzen. Dies erfordert eine Gramps XML-Datei oder ein Gramps Web-Backup.

Wenn ein Limit für die Anzahl der Personen in Ihrem Baum festgelegt wurde (siehe [Nutzungsquoten](settings.md#usage-quotas)), wird ein Import, der dieses überschreiten würde, insgesamt abgelehnt.

## GEDCOM-Dateien

Sowohl GEDCOM 5.5.1- als auch GEDCOM 7-Dateien können importiert werden. Es gibt einige Dinge, die zu beachten sind.

### Zeichencodierung

Eine GEDCOM 5.5.1-Datei gibt ihre Zeichencodierung in ihrem Header an. UTF-8, UTF-16, ANSEL und Windows (ANSI) Codierungen werden unterstützt. Wenn Namen mit Akzenten oder anderen Sonderzeichen nach dem Import verzerrt aussehen (zum Beispiel `MÃ¼ller` anstelle von `Müller`), wurde die Datei wahrscheinlich mit einer anderen Codierung exportiert, als sie angibt. Exportieren Sie die Datei erneut aus Ihrem alten Programm und wählen Sie UTF-8, wenn Ihnen eine Auswahl angeboten wird, und [fangen Sie neu an](#starting-over).

GEDCOM 7-Dateien müssen immer als UTF-8 codiert sein; andere Dateien werden mit einem Fehler "Ungültige GEDCOM-Datei" abgelehnt.

### Programmspezifische Daten

Viele Programme fügen GEDCOM ihre eigenen Erweiterungen hinzu, die von anderen Programmen nicht verstanden werden. Gramps verwirft solche Daten nicht stillschweigend: Zeilen, die es nicht interpretieren kann, werden in einer Notiz des Typs "GEDCOM-Import" gesammelt, die der Person, Familie oder einem anderen Objekt angehängt ist, zu dem sie gehören. Überprüfen Sie diese Notizen, um zu sehen, ob etwas Wichtiges nicht übertragen wurde.

### Mediendateien

Eine GEDCOM-Datei enthält Verweise auf Mediendateien (wie Fotos oder gescannte Dokumente), jedoch nicht die Dateien selbst. Nach dem Import existieren die Medienobjekte in Ihrem Baum, aber ihre Dateien fehlen, was unter [Status der Mediendateien](settings.md#media-file-status) angezeigt wird. Um die Dateien hinzuzufügen, siehe [Mediendateien importieren](import-media.md).

## Kommt von Gramps Desktop

Wenn Sie Gramps Desktop verwenden, gibt es zwei Schritte, um Ihre Datenbank vorzubereiten, um sicherzustellen, dass alles reibungslos funktioniert.

1. Überprüfen und reparieren Sie die Datenbank
    - Optional: Erstellen Sie ein Datenbank-Backup, indem Sie in Gramps XML exportieren.
    - Führen Sie das [Werkzeug zur Überprüfung und Reparatur der Datenbank](https://gramps-project.org/wiki/index.php/Gramps_5.2_Wiki_Manual_-_Tools#Check_and_Repair_Database) aus. Dies behebt einige interne Inkonsistenzen, die zu Problemen in Gramps Web führen könnten.
2. Konvertieren Sie Medienpfade in relative
    - Verwenden Sie den Gramps Medienmanager, um [alle Medienpfade von absolut in relativ zu konvertieren](https://gramps-project.org/wiki/index.php/Gramps_5.2_Wiki_Manual_-_Tools#Convert_paths_from_relative_to_absolute). Beachten Sie, dass selbst bei relativen Pfaden alle Mediendateien außerhalb Ihres Gramps-Medienverzeichnisses nicht ordnungsgemäß funktionieren, wenn sie mit Gramps Web synchronisiert werden.

Exportieren Sie dann Ihren Baum in Gramps XML (`.gramps`), importieren Sie ihn wie oben beschrieben und [laden Sie Ihre Mediendateien hoch](import-media.md). Um an demselben Baum auf Ihrem Computer und im Web weiterzuarbeiten, verwenden Sie das [Gramps Web Sync-Addon](sync.md).

### Warum keine Unterstützung für Gramps XML-Paket?

Während Gramps XML (`.gramps`) das bevorzugte Format für den Import von Daten ist, wird das Gramps XML *Paket* (`.gpkg`) von Gramps Web nicht unterstützt. Dies liegt daran, dass die Import- und Export-Routinen für Mediendateien nicht für die Verwendung auf einem Webserver geeignet sind.

## Häufige Probleme

**"Nicht unterstütztes Format".** Nur die oben [aufgelisteten](#which-file-to-use) Dateierweiterungen können importiert werden. Wenn Ihr Programm oder Online-Dienst Ihnen ein ZIP-Archiv gegeben hat, entpacken Sie es und laden Sie die darin enthaltene `.ged`-Datei hoch.

**Alles erscheint doppelt.** Dieselbe Datei wurde zweimal importiert. Da Importe niemals zusammengeführt werden, [fangen Sie neu an](#starting-over).

**Verzerrte Sonderzeichen.** Siehe [Zeichencodierung](#character-encoding).

**Fotos fehlen.** Siehe [Mediendateien importieren](import-media.md).

### Neu anfangen

Wenn ein Import schiefgelaufen ist oder Sie etwas in Ihrem alten Programm beheben und erneut importieren möchten, leeren Sie zuerst den Baum mit [Alle Objekte löschen](settings.md#delete-all-objects) im Gefahrenbereich der Verwaltungseinstellungen und importieren Sie dann die korrigierte Datei. Beachten Sie, dass dies auch alle Änderungen löscht, die Sie seit dem Import in Gramps Web vorgenommen haben.
