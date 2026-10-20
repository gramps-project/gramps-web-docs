# Verwaltungseinstellungen

Die **Einstellungen > Verwaltung**-Seite ist über das Benutzersymbol in der oberen App-Leiste zugänglich. Sie ist nur für Benutzer mit der Rolle Eigentümer oder Administrator verfügbar und bietet Werkzeuge zur Verwaltung der Familienstammbaum-Datenbank.

Die Seite ist in zusammenklappbare Abschnitte organisiert. Klicken Sie auf eine Abschnittsüberschrift, um sie zu erweitern.

## Daten

Behandelt Nutzungskontingente, Datenimport und Medienverwaltungsdateien.

### Nutzungskontingente

Oben im Abschnitt wird die aktuelle Nutzung im Verhältnis zu den konfigurierten Limits angezeigt:

- **Personen** – die Anzahl der Personenobjekte im Baum im Vergleich zur konfigurierten maximalen Anzahl (∞, wenn unbegrenzt)
- **Medien-Speicher** – die Gesamtgröße der hochgeladenen Mediendateien im Vergleich zum konfigurierten Speicherkontingent (∞, wenn unbegrenzt)

Die Kontingente werden vom Serveradministrator festgelegt; siehe [Serverkonfiguration](../install_setup/configuration.md) für Details.

### Daten importieren

Der Importbereich ermöglicht es Ihnen, eine Familienstammbaumdatei oder ein Medienarchiv hochzuladen. Siehe [Daten importieren](import.md) für vollständige Anweisungen.

### Medienstatus

Dieser Abschnitt zeigt:

- Die Gesamtanzahl der Medienobjekte im Baum und ob einige eine Prüfziffer vermissen
- Die Anzahl der Medienobjekte, deren zugehörige Datei auf dem Server fehlt

Ein grünes Häkchen zeigt an, dass alles in Ordnung ist. Wenn Probleme festgestellt werden, werden Links zu den betroffenen Objekten angezeigt. Fehlende Prüfziffern treten typischerweise auf, wenn Daten aus einem Format wie GEDCOM importiert wurden, das Medienreferenzen, aber nicht die tatsächlichen Dateien enthält. Die fehlenden Dateien können über die Funktion Medienarchiv importieren hochgeladen werden.

### Medienarchiv importieren

Erlaubt das Hochladen einer ZIP-Datei mit Mediendateien, um fehlende Dateien zu ergänzen. Siehe [Daten importieren](import.md) für vollständige Anweisungen.

## Suchindex

### Suchindex verwalten

Gramps Web pflegt einen Volltext-Suchindex, der normalerweise automatisch aktualisiert wird, wenn sich Daten ändern. Der Statusindikator zeigt, wie viele Objekte derzeit indiziert sind im Vergleich zur Gesamtanzahl der Objekte.

Klicken Sie auf **Suchindex aktualisieren**, um einen vollständigen Neuaufbau auszulösen. Ein Fortschrittsindikator wird angezeigt, während die Aufgabe im Hintergrund ausgeführt wird. Dies ist normalerweise nur nach einem Server-Upgrade erforderlich.

### Semantischer Suchindex

!!! warning "Veraltet"
    Die semantische Suche ist veraltet und wird in Gramps Web API 3.25 zusammen mit diesem Abschnitt entfernt. Der AI-Chat benötigt sie nicht, da Gramps Web API 3.24.

Wenn der Server die [semantische (KI-gestützte) Suche aktiviert](../install_setup/chat.md#semantic-search-deprecated) hat, erscheint ein zusätzlicher Abschnitt mit zwei Aktionen:

- **Semantischen Suchindex neu generieren** – baut den gesamten semantischen Index von Grund auf neu. Dies ist rechenintensiv und kann lange dauern.
- **Semantischen Suchindex aktualisieren** – führt ein inkrementelles Update durch, das nur Objekte hinzufügt, die noch nicht indiziert sind. Schneller als ein vollständiger Neuaufbau.

## Baum-Einstellungen

### Name des Familienstammbaums

!!! note
    Das Umbenennen des Baums funktioniert nur in einer [Multi-Baum-Konfiguration](../install_setup/multi-tree.md) oder wenn `TREE_ID` explizit in der [Serverkonfiguration](../install_setup/configuration.md) festgelegt ist. Bei einer Standardinstallation mit einem einzelnen Baum ohne festgelegte `TREE_ID` wird ein Fehler angezeigt.

Dies ermöglicht es, den Namen der zugrunde liegenden Gramps-Familienstammbaum-Datenbank zu ändern. Geben Sie einen neuen Namen ein und klicken Sie auf **Umbenennen**, um die Änderung zu übernehmen.

!!! tip
    Wenn Sie nur den Namen ändern möchten, der in der App-Leiste angezeigt wird, ohne die Datenbank umzubenennen, verwenden Sie stattdessen die Einstellung [App-Titel](#app-title).

### Informationen zum Forscher

Legen Sie den Namen, die Adresse und die Kontaktdaten des Hauptforschers fest. Diese Informationen sind in Exporten (z. B. GEDCOM-Dateien) eingebettet.

## Anpassung

### Farbthemen

Legen Sie eine benutzerdefinierte **Primärfarbe** und **Akzentfarbe** für die Gramps Web-Oberfläche fest. Diese Farben werden auf alle Benutzer dieses Baums angewendet und treten sofort nach dem Speichern in Kraft.

Verwenden Sie die Farbauswähler, um Farben auszuwählen, und klicken Sie dann auf **Speichern**. Klicken Sie auf **Zurücksetzen**, um die Standardwerte wiederherzustellen.

### App-Titel

Legen Sie einen benutzerdefinierten Titel für die Anwendung fest. Wenn festgelegt, überschreibt dies den Namen des Familienstammbaums in der Titelleiste des Browsers und in der oberen App-Leiste.

Geben Sie einen Titel ein und klicken Sie auf **Speichern**. Lassen Sie das Feld leer, um den Standard (den Namen des Familienstammbaums) zu verwenden.

### Notiz auf der Startseite

Wählen Sie ein Gramps **Notiz**-Objekt aus, das auf der Dashboard-Startseite angezeigt werden soll. Der Notizinhalt wird unter den Hauptspalten des Dashboards gerendert und ist für alle Benutzer sichtbar, die Zugriff auf den Baum haben.

Verwenden Sie den Objektauswähler, um nach einer Notiz zu suchen und eine auszuwählen, und speichern Sie dann. Klicken Sie auf **Entfernen**, um die aktuelle Notiz auf der Startseite zu löschen.

### Bild auf der Startseite

Wählen Sie ein Gramps **Medien**-Objekt aus, das als Bild auf der Dashboard-Startseite angezeigt werden soll. In Kombination mit einer Notiz auf der Startseite erscheint das Bild neben dem Notiztext. Ohne eine Notiz wird nur das Bild angezeigt.

Verwenden Sie den Objektauswähler, um nach einem Medienobjekt zu suchen und eines auszuwählen, und speichern Sie dann. Klicken Sie auf **Entfernen**, um das aktuelle Bild auf der Startseite zu löschen.

### Export-/Importeinstellungen

Baumebeneinstellungen (App-Titel, Farbthemen, Notiz/Bild auf der Startseite usw.) können als JSON-Datei für Backups oder zum Kopieren in eine andere Gramps Web-Instanz exportiert werden.

- Klicken Sie auf **Einstellungen exportieren**, um die aktuellen Einstellungen als JSON-Datei herunterzuladen.
- Klicken Sie auf **Baumeinstellungen importieren**, um eine zuvor exportierte JSON-Datei hochzuladen und die Einstellungen anzuwenden.

## Verarbeitung des Familienstammbaums

### Datenbank überprüfen und reparieren

Dieses Tool überprüft die Gramps-Datenbank auf interne Inkonsistenzen und behebt die, die es kann – analog zum [Tool Datenbank überprüfen und reparieren](https://www.gramps-project.org/wiki/index.php/Gramps_5.2_Wiki_Manual_-_Tools#Check_and_Repair_Database) in Gramps Desktop.

Klicken Sie auf **Überprüfen und Reparieren** und warten Sie, bis der Fortschrittsindikator abgeschlossen ist. Das Ergebnis wird unter dem Button angezeigt:

- Wenn keine Fehler gefunden wurden, wird eine Bestätigungsnachricht angezeigt.
- Wenn Fehler gefunden wurden, wird eine Zusammenfassung der durchgeführten Korrekturen angezeigt.

Führen Sie dieses Tool aus, wenn Sie auf unerwartete Fehler oder Verhaltensweisen stoßen, die durch Datenbankinkonsistenzen verursacht werden können, wie z. B. fehlende Beziehungen zwischen Objekten.

### Daten überprüfen

Während [Datenbank überprüfen und reparieren](#check-and-repair-database) nach *technischen* Inkonsistenzen sucht, sucht dieses Tool nach *unplausiblen* Daten – analog zum [Tool Daten überprüfen](https://gramps-project.org/wiki/index.php/Gramps_5.0_Wiki_Manual_-_Tools#Verify_the_Data) in Gramps Desktop. Es berichtet über Dinge, die nicht unmöglich sind, aber unwahrscheinlich genug, um einen zweiten Blick wert zu sein, wie z. B. eine Mutter im Alter von 12 oder eine Person, die 130 Jahre alt wurde.

Unter **Optionen** können Sie die Schwellenwerte anpassen, die die Tests verwenden – maximales Alter, Mindest- und Höchstalter zum Heiraten oder Kinder bekommen, maximale Anzahl von Kindern usw. – sowie ob fehlende oder ungenaue Daten geschätzt werden sollen und ob ungültige Daten wie den 31. Februar gemeldet werden sollen.

Klicken Sie auf **Daten überprüfen**, um zu beginnen. Die Überprüfung läuft als Hintergrundaufgabe, und die Ergebnisse werden dann unter **Ergebnisse der Datenüberprüfung** aufgelistet. Nichts wird durch dieses Tool geändert: Es berichtet nur, was es findet.

!!! note
    Ein Befund ist kein Beweis für einen Fehler. Lange Lebensdauern und große Altersunterschiede kommen vor, also behandeln Sie die Ergebnisse als eine Liste von Dingen, die überprüft werden sollten, und nicht als eine Liste von Dingen, die behoben werden müssen.

## Etiketten

### Etiketten verwalten

Erstellen, umbenennen, umfärben und löschen Sie [Etiketten](../user-guide/tags.md) für den Familienstammbaum. Etiketten werden in der Gramps-Datenbank gespeichert, sind für alle Benutzer gemeinsam und vollständig kompatibel mit Gramps Desktop.

Klicken Sie auf **Neues Etikett**, um ein Etikett zu erstellen. Verwenden Sie die Steuerelemente neben einem vorhandenen Etikett, um es umzubenennen (Bleistiftsymbol), seine Farbe zu ändern (Farbauswähler) oder es zu löschen (Löschsymbol).

!!! note
    Das Löschen eines Etiketts entfernt es von allen Objekten, auf die es angewendet wurde.

Siehe [Etiketten](../user-guide/tags.md) für Informationen, wie Etiketten in Gramps Web verwendet werden, einschließlich der speziellen Etiketten `Blog` und `ToDo`.

## Backups

Ein Backup enthält die Daten des Familienstammbaums, einschließlich privater Aufzeichnungen, der Baumeinstellungen und der Benutzer des Baums. Mediendateien sind nicht enthalten; siehe [Sichern Sie Ihre Mediendateien](export.md#back-up-your-media-files).

### Gespeicherte Backups

Wenn der Serveradministrator ein Backup-Verzeichnis (`BACKUP_DIR`, siehe [Serverkonfiguration](../install_setup/configuration.md)) festgelegt hat, können Backups auf dem Server gespeichert werden. Andernfalls zeigt der Abschnitt eine Mitteilung an, dass das Speichern von Backups nicht konfiguriert ist und nur die Wiederherstellung aus einer hochgeladenen Datei verfügbar ist.

Klicken Sie auf **Backup erstellen...**, um ein Backup zu erstellen. Es wird als Hintergrundaufgabe erstellt und erscheint dann in der Liste der gespeicherten Backups, mit Datum, Anzahl der Personen und Größe. Der Server behält nur die neuesten Backups (standardmäßig fünf) und löscht ältere automatisch. Die Anzahl der Backups, die pro Tag erstellt werden können, ist ebenfalls begrenzt.

Für jedes gespeicherte Backup können Sie:

- **Herunterladen** als `.tar`-Datei, um beispielsweise eine Kopie an einem anderen Ort aufzubewahren.
- **Wiederherstellen**, wie unten beschrieben.
- **Löschen**, nach Bestätigung.

Ein Backup, das mit einer neueren Version von Gramps Web als der auf dem Server laufenden Version erstellt wurde, ist mit einem Warnsymbol gekennzeichnet und kann nicht wiederhergestellt werden.

### Aus Backup wiederherstellen

Stellt den Baum aus einem gespeicherten Backup oder aus einer hochgeladenen Datei wieder her. Um ein gespeichertes Backup wiederherzustellen, klicken Sie auf die Wiederherstelltaste daneben. Um aus einer Datei wiederherzustellen, wählen Sie ein Gramps Web-Backup (`.tar`) oder eine Gramps XML-Datei (`.gramps`) aus und klicken Sie auf **Wiederherstellen**.

!!! danger
    Die Wiederherstellung der Daten ist ein destruktiver Ersatz, kein Merge. Jedes vorhandene Objekt, das im Backup nicht vorhanden ist, wird gelöscht.

Für ein Gramps Web-Backup wird ein Dialog angezeigt, wann das Backup erstellt wurde, für welchen Baum und mit welcher Version, und lässt Sie auswählen, welche Teile wiederhergestellt werden sollen:

- **Daten** – die Objekte des Familienstammbaums
- **Baumeinstellungen** – die Einstellungen dieser Seite, wie Farbthemen, App-Titel und Notiz auf der Startseite
- **Benutzer** – die Benutzer des Baums

Klicken Sie auf **Vorschau**, um zu sehen, was die Wiederherstellung ändern würde. Eine Gramps XML-Datei enthält nur Daten, sodass die Vorschau für eine solche Datei sofort beginnt. Sie werden aufgefordert, sich erneut zu authentifizieren, wenn Ihre Sitzung nicht frisch genug ist. Die Vorschau läuft als Hintergrundaufgabe und öffnet, sobald sie abgeschlossen ist, einen Dialog, der die Änderungen pro Objekttyp (Personen, Familien, Ereignisse, Orte, Zitationen, Quellen, Repositories, Medienobjekte, Notizen, Etiketten) sowie für die Baumeinstellungen und Benutzer, falls ausgewählt:

- **Hinzufügen** – Objekte, die im Backup vorhanden, aber im aktuellen Baum fehlen
- **Aktualisieren** – Objekte, die in beiden vorhanden sind, aber unterschiedlich sind
- **Löschen** – Objekte im aktuellen Baum, die im Backup fehlen
- **Unverändert** – Objekte, die in beiden identisch sind

Wenn Objekte gelöscht werden, warnt der Dialog, wie viele. Überprüfen Sie die Zusammenfassung und klicken Sie dann auf **Wiederherstellen**, um die Änderungen anzuwenden, oder auf **Abbrechen**, um abzubrechen.

Nach der Wiederherstellung werden die Benutzer aufgelistet, die aus dem Backup hinzugefügt wurden. Sie erhalten ein zufälliges Passwort, sodass sie ihr Passwort zurücksetzen müssen, bevor sie sich anmelden können. Benutzer, die bereits auf dem Server existieren, werden niemals geändert. Medienobjekte, deren Dateien auf dem Server fehlen, werden ebenfalls aufgelistet; laden Sie sie über [Medienarchiv importieren](#import-media-archive) hoch.

!!! note
    Die Wiederherstellung von Daten stellt nur die Objekt- und Medienreferenzdaten wieder her. Binäre Mediendateien selbst und Baum-Metadaten (Standardperson, Lesezeichen, Namensgruppen) sind nicht betroffen.

!!! tip
    Verwenden Sie dies, um einen Baum auf ein bekannt gutes Backup zurückzusetzen, beispielsweise nach einem fehlerhaften Import oder einer unerwünschten Massenbearbeitung.

## Gefahrenzone

!!! danger
    Aktionen in der Gefahrenzone sind **irreversibel**. Machen Sie ein [Backup](#backups), bevor Sie fortfahren.

### Alle Objekte löschen

Entfernt Objekte aus dem Familienstammbaum. Ein Klick auf **Löschen** öffnet einen Dialog, in dem Sie wählen können, ob Sie löschen möchten:

- **Alle Objekte** – leert den Baum vollständig
- **Spezifische Objekttypen** – zum Beispiel nur Ereignisse oder nur Medienobjekte

Sie werden aufgefordert, sich erneut zu authentifizieren (sich erneut anzumelden), um die Aktion zu bestätigen. Die Löschung wird als Hintergrundaufgabe ausgeführt und ein Fortschrittsindikator wird angezeigt.

!!! warning
    Das Löschen nur einer Teilmenge von Objekttypen (anstatt aller Objekte auf einmal) kann für große Bäume sehr lange dauern, da der Server alle Beziehungen zwischen Objekten überprüfen und aktualisieren muss.

!!! tip
    Verwenden Sie dies, um frisch zu starten, bevor Sie einen neuen Baum importieren, oder um spezifische Objekttypen zu entfernen, die falsch importiert wurden.
