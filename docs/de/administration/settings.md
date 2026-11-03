# Verwaltungseinstellungen

Die **Einstellungen > Verwaltung**-Seite ist über das Benutzericon in der oberen App-Leiste zugänglich. Sie ist nur für Benutzer mit der Rolle Eigentümer oder Administrator verfügbar und bietet Werkzeuge zur Verwaltung der Familienstammbaum-Datenbank.

Die Seite ist in zusammenklappbare Abschnitte organisiert. Klicken Sie auf einen Abschnittsheader, um ihn zu erweitern.

## Daten

Behandelt Nutzungskontingente, Datenimport und Medienverwaltungsdateien.

### Nutzungskontingente

Oben im Abschnitt werden die aktuellen Nutzungen im Verhältnis zu den konfigurierten Limits angezeigt:

- **Personen** – die Anzahl der Personenobjekte im Baum im Vergleich zum konfigurierten Maximum (∞, wenn unbegrenzt)
- **Medien-Speicher** – die Gesamtgröße der hochgeladenen Mediendateien im Vergleich zum konfigurierten Speicherplatzkontingent (∞, wenn unbegrenzt)

Die Kontingente werden vom Serveradministrator festgelegt; siehe [Serverkonfiguration](../install_setup/configuration.md) für Details.

### Daten importieren

Der Importabschnitt ermöglicht es Ihnen, eine Familienstammbaumdatei oder ein Medienarchiv hochzuladen. Siehe [Daten importieren](import.md) für vollständige Anweisungen.

### Medienstatus

Dieser Abschnitt zeigt:

- Die Gesamtzahl der Medienobjekte im Baum und ob einige eine Prüfziffer vermissen
- Die Anzahl der Medienobjekte, deren zugehörige Datei auf dem Server fehlt

Ein grünes Häkchen zeigt an, dass alles in Ordnung ist. Wenn Probleme festgestellt werden, werden Links zu den betroffenen Objekten angezeigt. Fehlende Prüfziffern treten typischerweise auf, wenn Daten aus einem Format wie GEDCOM importiert wurden, das Medienreferenzen, aber nicht die tatsächlichen Dateien enthält. Die fehlenden Dateien können über die Funktion Medienarchiv importieren hochgeladen werden.

### Medienarchiv importieren

Ermöglicht das Hochladen einer ZIP-Datei von Mediendateien, um fehlende Dateien zu ergänzen. Siehe [Daten importieren](import.md) für vollständige Anweisungen.

## Suchindex

### Suchindex verwalten

Gramps Web pflegt einen Volltext-Suchindex, der normalerweise automatisch aktualisiert wird, wenn sich Daten ändern. Der Statusindikator zeigt, wie viele Objekte derzeit indiziert sind im Vergleich zur Gesamtanzahl der Objekte.

Klicken Sie auf **Suchindex aktualisieren**, um einen vollständigen Neuaufbau auszulösen. Ein Fortschrittsindikator wird angezeigt, während die Aufgabe im Hintergrund ausgeführt wird. Dies ist selten erforderlich.

Wenn ein Baum noch keinen Suchindex hat, beispielsweise nach einem Server-Upgrade, das das Indexformat geändert hat, erstellt Gramps Web ihn im Hintergrund beim ersten Öffnen des Baums. Während er erstellt wird, zeigt der Abschnitt "Der Suchindex wird erstellt." anstelle der Zählungen, **Suchindex aktualisieren** ist deaktiviert, und die Suchergebnisse können unvollständig sein. Der Aufbau wird in [Benachrichtigungen](../user-guide/notifications.md) als "Suchindex aktualisieren"-Aufgabe angezeigt.

## Baum-Einstellungen

### Name des Familienstammbaums

!!! Hinweis
    Das Umbenennen des Baums funktioniert nur in einer [Multi-Baum-Konfiguration](../install_setup/multi-tree.md) oder wenn `TREE_ID` explizit in der [Serverkonfiguration](../install_setup/configuration.md) festgelegt ist. Bei einer Standardinstallation mit einem einzelnen Baum ohne festgelegtes `TREE_ID` tritt ein Fehler auf.

Dies ermöglicht das Ändern des Namens der zugrunde liegenden Gramps-Familienstammbaum-Datenbank. Geben Sie einen neuen Namen ein und klicken Sie auf **Umbenennen**, um die Änderungen anzuwenden.

!!! Tipp
    Wenn Sie nur den Namen ändern möchten, der in der App-Leiste angezeigt wird, ohne die Datenbank umzubenennen, verwenden Sie stattdessen die Einstellung [App-Titel](#app-title).

### Informationen zum Forscher

Legen Sie den Namen, die Adresse und die Kontaktdaten des Hauptforschers fest. Diese Informationen sind in Exporten (z. B. GEDCOM-Dateien) eingebettet.

## Anpassung

### Themenfarben

Legen Sie eine benutzerdefinierte **Primärfarbe** und **Akzentfarbe** für die Gramps Web-Oberfläche fest. Diese Farben werden für alle Benutzer dieses Baums angewendet und treten sofort nach dem Speichern in Kraft.

Verwenden Sie die Farbauswähler, um Farben auszuwählen, und klicken Sie dann auf **Speichern**. Klicken Sie auf **Zurücksetzen**, um die Standardwerte wiederherzustellen.

### App-Titel

Legen Sie einen benutzerdefinierten Titel für die Anwendung fest. Wenn festgelegt, überschreibt dies den Namen des Familienstammbaums in der Titelleiste des Browsers und der oberen App-Leiste.

Geben Sie einen Titel ein und klicken Sie auf **Speichern**. Lassen Sie das Feld leer, um den Standard (den Namen des Familienstammbaums) zu verwenden.

### Hinweis auf der Startseite

Wählen Sie ein Gramps **Notiz**-Objekt aus, das auf der Dashboard-Startseite angezeigt werden soll. Der Inhalt der Notiz wird unter den Hauptdashboard-Spalten gerendert und ist für alle Benutzer sichtbar, die Zugriff auf den Baum haben.

Verwenden Sie den Objektauswähler, um nach einer Notiz zu suchen und eine auszuwählen, und speichern Sie dann. Klicken Sie auf **Entfernen**, um die aktuelle Notiz auf der Startseite zu löschen.

### Bild auf der Startseite

Wählen Sie ein Gramps **Medien**-Objekt aus, das als Bild auf der Dashboard-Startseite angezeigt werden soll. In Kombination mit einer Notiz auf der Startseite erscheint das Bild neben dem Notiztext. Ohne eine Notiz wird nur das Bild angezeigt.

Verwenden Sie den Objektauswähler, um nach einem Medienobjekt zu suchen und eines auszuwählen, und speichern Sie dann. Klicken Sie auf **Entfernen**, um das aktuelle Bild auf der Startseite zu löschen.

### Export-/Importeinstellungen

Baumebene Einstellungen (App-Titel, Themenfarben, Hinweis/Bild auf der Startseite usw.) können als JSON-Datei zur Sicherung oder zum Kopieren in eine andere Gramps Web-Instanz exportiert werden.

- Klicken Sie auf **Einstellungen exportieren**, um die aktuellen Einstellungen als JSON-Datei herunterzuladen.
- Klicken Sie auf **Baumeinstellungen importieren**, um eine zuvor exportierte JSON-Datei hochzuladen und die Einstellungen anzuwenden.

## Verarbeitung des Familienstammbaums

### Datenbank überprüfen und reparieren

Dieses Tool überprüft die Gramps-Datenbank auf interne Inkonsistenzen und behebt die, die es kann – analog zum [Tool Datenbank überprüfen und reparieren](https://www.gramps-project.org/wiki/index.php/Gramps_5.2_Wiki_Manual_-_Tools#Check_and_Repair_Database) in Gramps Desktop.

Klicken Sie auf **Überprüfen und Reparieren** und warten Sie, bis der Fortschrittsindikator abgeschlossen ist. Das Ergebnis wird unter dem Button angezeigt:

- Wenn keine Fehler gefunden wurden, wird eine Bestätigungsnachricht angezeigt.
- Wenn Fehler gefunden wurden, wird eine Zusammenfassung der durchgeführten Reparaturen angezeigt.

Führen Sie dieses Tool aus, wenn Sie unerwartete Fehler oder Verhaltensweisen feststellen, die durch Datenbankinkonsistenzen verursacht werden könnten, wie z. B. fehlende Beziehungen zwischen Objekten.

### Daten überprüfen

Während [Datenbank überprüfen und reparieren](#check-and-repair-database) nach *technischen* Inkonsistenzen sucht, sucht dieses Tool nach *unplausiblen* Daten – analog zum [Tool Daten überprüfen](https://gramps-project.org/wiki/index.php/Gramps_5.0_Wiki_Manual_-_Tools#Verify_the_Data) in Gramps Desktop. Es meldet Dinge, die nicht unmöglich sind, aber unwahrscheinlich genug, um einen zweiten Blick wert zu sein, wie eine Mutter im Alter von 12 oder eine Person, die 130 Jahre alt wurde.

Unter **Optionen** können Sie die Schwellenwerte anpassen, die die Tests verwenden – maximales Alter, Mindest- und Höchstalter zum Heiraten oder Kinder bekommen, maximale Anzahl von Kindern usw. – sowie ob fehlende oder ungenaue Daten geschätzt werden sollen und ob ungültige Daten wie der 31. Februar gemeldet werden sollen.

Klicken Sie auf **Daten überprüfen**, um zu beginnen. Die Überprüfung läuft als Hintergrundaufgabe, und die Ergebnisse werden dann unter **Ergebnisse der Datenüberprüfung** aufgelistet. Nichts wird durch dieses Tool geändert: Es berichtet nur, was es findet.

!!! Hinweis
    Ein Befund ist kein Beweis für einen Fehler. Lange Leben und große Altersunterschiede kommen vor, also behandeln Sie die Ergebnisse als eine Liste von Dingen, die zu überprüfen sind, anstatt als eine Liste von Dingen, die zu beheben sind.

## Etiketten

### Etiketten verwalten

Erstellen, umbenennen, umfärben und löschen Sie [Etiketten](../user-guide/tags.md) für den Familienstammbaum. Etiketten werden in der Gramps-Datenbank gespeichert, sind für alle Benutzer gemeinsam und vollständig kompatibel mit Gramps Desktop.

Klicken Sie auf **Neues Etikett**, um ein Etikett zu erstellen. Verwenden Sie die Steuerelemente neben einem vorhandenen Etikett, um es umzubenennen (Bleistift-Icon), seine Farbe zu ändern (Farbauswähler) oder es zu löschen (Löschen-Icon).

!!! Hinweis
    Das Löschen eines Etiketts entfernt es von allen Objekten, auf die es angewendet wurde.

Siehe [Etiketten](../user-guide/tags.md) für Informationen, wie Etiketten in Gramps Web verwendet werden, einschließlich der speziellen Etiketten `Blog` und `ToDo`.

## Backups

Ein Backup enthält die Daten des Familienstammbaums, einschließlich privater Aufzeichnungen, der Baumeinstellungen und der Benutzer des Baums. Mediendateien sind nicht enthalten; siehe [Sichern Sie Ihre Mediendateien](export.md#back-up-your-media-files).

### Gespeicherte Backups

Wenn der Serveradministrator ein Backup-Verzeichnis (`BACKUP_DIR`, siehe [Serverkonfiguration](../install_setup/configuration.md)) festgelegt hat, können Backups auf dem Server gespeichert werden. Andernfalls zeigt der Abschnitt eine Mitteilung an, dass das Speichern von Backups nicht konfiguriert ist, und nur das Wiederherstellen von einer hochgeladenen Datei ist verfügbar.

Klicken Sie auf **Backup erstellen...**, um ein Backup zu erstellen. Es wird als Hintergrundaufgabe erstellt und erscheint dann in der Liste der gespeicherten Backups, mit Datum, Anzahl der Personen und Größe. Der Server behält nur die neuesten Backups (standardmäßig fünf) und löscht ältere automatisch. Die Anzahl der Backups, die pro Tag erstellt werden können, ist ebenfalls begrenzt.

Für jedes gespeicherte Backup können Sie:

- **Herunterladen** als `.tar`-Datei, zum Beispiel um eine Kopie an einem anderen Ort aufzubewahren.
- **Wiederherstellen**, wie unten beschrieben.
- **Löschen**, nach Bestätigung.

Ein Backup, das mit einer neueren Version von Gramps Web als der auf dem Server laufenden erstellt wurde, wird mit einem Warnsymbol markiert und kann nicht wiederhergestellt werden.

### Aus Backup wiederherstellen

Stellt den Baum aus einem gespeicherten Backup oder einer hochgeladenen Datei wieder her. Um ein gespeichertes Backup wiederherzustellen, klicken Sie auf die Schaltfläche Wiederherstellen daneben. Um von einer Datei wiederherzustellen, wählen Sie ein Gramps Web-Backup (`.tar`) oder eine Gramps-XML-Datei (`.gramps`) aus und klicken Sie auf **Wiederherstellen**.

!!! Gefahr
    Das Wiederherstellen der Daten ist ein destruktiver Ersatz, kein Merge. Jedes vorhandene Objekt, das im Backup nicht vorhanden ist, wird gelöscht.

Für ein Gramps Web-Backup wird ein Dialogfeld angezeigt, in dem angezeigt wird, wann das Backup erstellt wurde, für welchen Baum und mit welcher Version, und Sie können auswählen, welche Teile wiederhergestellt werden sollen:

- **Daten** – die Objekte des Familienstammbaums
- **Baumeinstellungen** – die Einstellungen dieser Seite, wie Themenfarben, App-Titel und Hinweis auf der Startseite
- **Benutzer** – die Benutzer des Baums

Klicken Sie auf **Vorschau**, um zu sehen, was die Wiederherstellung ändern würde. Eine Gramps-XML-Datei enthält nur Daten, sodass die Vorschau für eine solche Datei sofort beginnt. Sie werden aufgefordert, sich erneut zu authentifizieren, wenn Ihre Sitzung nicht frisch genug ist. Die Vorschau läuft als Hintergrundaufgabe und öffnet, sobald sie abgeschlossen ist, einen Dialog, der die Änderungen pro Objekttyp (Personen, Familien, Ereignisse, Orte, Zitationen, Quellen, Repositories, Medienobjekte, Notizen, Etiketten) sowie für die Baumeinstellungen und Benutzer, falls ausgewählt:

- **Hinzufügen** – Objekte, die im Backup vorhanden, aber im aktuellen Baum fehlen
- **Aktualisieren** – Objekte, die in beiden vorhanden sind, aber unterschiedlich sind
- **Löschen** – Objekte im aktuellen Baum, die im Backup fehlen
- **Unverändert** – Objekte, die in beiden identisch sind

Wenn Objekte gelöscht werden würden, warnt der Dialog, wie viele. Überprüfen Sie die Zusammenfassung und klicken Sie dann auf **Wiederherstellen**, um die Änderungen anzuwenden, oder auf **Abbrechen**, um abzubrechen.

Nach der Wiederherstellung werden die Benutzer, die aus dem Backup hinzugefügt wurden, aufgelistet. Sie erhalten ein zufälliges Passwort, sodass sie ihr Passwort zurücksetzen müssen, bevor sie sich anmelden können. Benutzer, die bereits auf dem Server existieren, werden niemals geändert. Medienobjekte, deren Dateien auf dem Server fehlen, werden ebenfalls aufgelistet; laden Sie sie über [Medienarchiv importieren](#import-media-archive) hoch.

!!! Hinweis
    Das Wiederherstellen von Daten stellt nur Objekt-Daten und Medienreferenzen wieder her. Binäre Mediendateien selbst und Metadaten des Baums (Standardperson, Lesezeichen, Namensgruppen) sind nicht betroffen.

!!! Tipp
    Verwenden Sie dies, um einen Baum auf ein bekannt gutes Backup zurückzusetzen, beispielsweise nach einem schlechten Import oder einer unerwünschten Massenbearbeitung.

## Gefahrenzone

!!! Gefahr
    Aktionen in der Gefahrenzone sind **irreversibel**. Machen Sie ein [Backup](#backups), bevor Sie fortfahren.

### Alle Objekte löschen

Entfernt Objekte aus dem Familienstammbaum. Ein Klick auf **Löschen** öffnet einen Dialog, in dem Sie auswählen können, ob Sie löschen möchten:

- **Alle Objekte** – leert den Baum vollständig
- **Spezifische Objekttypen** – zum Beispiel nur Ereignisse oder nur Medienobjekte

Sie werden aufgefordert, sich erneut zu authentifizieren (sich erneut einzuloggen), um die Aktion zu bestätigen. Die Löschung läuft als Hintergrundaufgabe und ein Fortschrittsindikator wird angezeigt.

!!! Warnung
    Das Löschen nur einer Teilmenge von Objekttypen (anstatt aller Objekte auf einmal) kann für große Bäume sehr lange dauern, da der Server alle Beziehungen zwischen Objekten überprüfen und aktualisieren muss.

!!! Tipp
    Verwenden Sie dies, um frisch zu starten, bevor Sie einen neuen Baum importieren, oder um spezifische Objekttypen zu entfernen, die falsch importiert wurden.
