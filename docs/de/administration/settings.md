# Verwaltungseinstellungen

Die **Einstellungen > Verwaltung**-Seite ist über das Benutzersymbol in der oberen App-Leiste zugänglich. Sie ist nur für Benutzer mit der Rolle Eigentümer oder Administrator verfügbar und bietet Werkzeuge zur Verwaltung der Familienstammbaum-Datenbank.

Die Seite ist in zusammenklappbare Abschnitte organisiert. Klicken Sie auf einen Abschnittsüberschrift, um ihn zu erweitern.

## Daten

Behandelt Nutzungskontingente, Datenimport und Medienverwaltungsdateien.

### Nutzungskontingente

Oben im Abschnitt werden die aktuellen Nutzungen im Verhältnis zu den konfigurierten Limits angezeigt:

- **Personen** – die Anzahl der Personenobjekte im Baum im Vergleich zur konfigurierten maximalen Anzahl (∞, wenn unbegrenzt)
- **Medien-Speicher** – die Gesamtgröße der hochgeladenen Mediendateien im Vergleich zum konfigurierten Speicherkontingent (∞, wenn unbegrenzt)

Die Kontingente werden vom Serveradministrator festgelegt; siehe [Serverkonfiguration](../install_setup/configuration.md) für Details.

### Daten importieren

Der Importabschnitt ermöglicht es Ihnen, eine Familienstammbaumdatei oder ein Medienarchiv hochzuladen. Siehe [Daten importieren](import.md) für vollständige Anweisungen.

### Medienstatus

Dieser Abschnitt zeigt:

- Die Gesamtzahl der Medienobjekte im Baum und ob einige eine Prüfziffer vermissen
- Die Anzahl der Medienobjekte, deren zugehörige Datei auf dem Server fehlt

Ein grünes Häkchen zeigt an, dass alles in Ordnung ist. Wenn Probleme erkannt werden, werden Links zu den betroffenen Objekten angezeigt. Fehlende Prüfziffern treten typischerweise auf, wenn Daten aus einem Format wie GEDCOM importiert wurden, das Medienreferenzen, aber nicht die tatsächlichen Dateien enthält. Die fehlenden Dateien können über die Funktion Medienarchiv importieren hochgeladen werden.

### Medienarchiv importieren

Ermöglicht das Hochladen einer ZIP-Datei mit Mediendateien, um fehlende Dateien zu ergänzen. Siehe [Daten importieren](import.md) für vollständige Anweisungen.

## Suchindex

### Suchindex verwalten

Gramps Web pflegt einen Volltext-Suchindex, der normalerweise automatisch aktualisiert wird, wenn sich Daten ändern. Der Statusindikator zeigt, wie viele Objekte derzeit indiziert sind im Vergleich zur Gesamtanzahl der Objekte.

Klicken Sie auf **Suchindex aktualisieren**, um einen vollständigen Neuaufbau auszulösen. Ein Fortschrittsindikator wird angezeigt, während die Aufgabe im Hintergrund ausgeführt wird. Dies ist normalerweise nur nach einem Server-Upgrade erforderlich.

### Semantischer Suchindex

Wenn der Server [semantische (KI-gestützte) Suche aktiviert hat](../install_setup/configuration.md), erscheint ein zusätzlicher Abschnitt mit zwei Aktionen:

- **Semantischen Suchindex neu generieren** – baut den gesamten semantischen Index von Grund auf neu. Dies ist rechenintensiv und kann lange dauern.
- **Semantischen Suchindex aktualisieren** – führt ein inkrementelles Update durch, das nur Objekte hinzufügt, die noch nicht indiziert sind. Schneller als ein vollständiger Neuaufbau.

## Baum-Einstellungen

### Name des Familienstammbaums

!!! note
    Das Umbenennen des Baums funktioniert nur in einer [Multi-Baum-Konfiguration](../install_setup/multi-tree.md) oder wenn `TREE_ID` explizit in der [Serverkonfiguration](../install_setup/configuration.md) festgelegt ist. Bei einer Standardinstallation mit nur einem Baum ohne festgelegte `TREE_ID` wird ein Fehler angezeigt.

Dies ermöglicht das Ändern des Namens der zugrunde liegenden Gramps-Familienstammbaum-Datenbank. Geben Sie einen neuen Namen ein und klicken Sie auf **Umbenennen**, um die Änderung anzuwenden.

!!! tip
    Wenn Sie nur den Namen ändern möchten, der in der App-Leiste angezeigt wird, ohne die Datenbank umzubenennen, verwenden Sie stattdessen die Einstellung [App-Titel](#app-title).

### Informationen zum Forscher

Legen Sie den Namen, die Adresse und die Kontaktdaten des Hauptforschers fest. Diese Informationen sind in Exporten (z. B. GEDCOM-Dateien) eingebettet.

## Anpassung

### Farbthemen

Legen Sie eine benutzerdefinierte **Primärfarbe** und **Akzentfarbe** für die Gramps Web-Oberfläche fest. Diese Farben werden allen Benutzern dieses Baums angewendet und treten sofort nach dem Speichern in Kraft.

Verwenden Sie die Farbauswahl, um Farben auszuwählen, und klicken Sie dann auf **Speichern**. Klicken Sie auf **Zurücksetzen**, um die Standardwerte wiederherzustellen.

### App-Titel

Legen Sie einen benutzerdefinierten Titel für die Anwendung fest. Wenn festgelegt, überschreibt dies den Namen des Familienstammbaums in der Titelleiste des Browsers und der oberen App-Leiste.

Geben Sie einen Titel ein und klicken Sie auf **Speichern**. Lassen Sie das Feld leer, um den Standard (den Namen des Familienstammbaums) zu verwenden.

### Hinweis auf der Startseite

Wählen Sie ein Gramps **Hinweis**-Objekt aus, das auf der Startseite des Dashboards angezeigt werden soll. Der Inhalt des Hinweises wird unter den Hauptspalten des Dashboards gerendert und ist für alle Benutzer sichtbar, die Zugriff auf den Baum haben.

Verwenden Sie den Objektauswähler, um nach einem Hinweis zu suchen und ihn auszuwählen, und speichern Sie dann. Klicken Sie auf **Entfernen**, um den aktuellen Hinweis auf der Startseite zu löschen.

### Bild auf der Startseite

Wählen Sie ein Gramps **Medien**-Objekt aus, das als Bild auf der Startseite des Dashboards angezeigt werden soll. In Kombination mit einem Hinweis auf der Startseite erscheint das Bild neben dem Hinweistext. Ohne einen Hinweis wird nur das Bild angezeigt.

Verwenden Sie den Objektauswähler, um nach einem Medienobjekt zu suchen und es auszuwählen, und speichern Sie dann. Klicken Sie auf **Entfernen**, um das aktuelle Bild auf der Startseite zu löschen.

### Export-/Importeinstellungen

Baumebene Einstellungen (App-Titel, Farbthemen, Hinweis/Bild auf der Startseite usw.) können als JSON-Datei zur Sicherung oder zum Kopieren in eine andere Gramps Web-Instanz exportiert werden.

- Klicken Sie auf **Einstellungen exportieren**, um die aktuellen Einstellungen als JSON-Datei herunterzuladen.
- Klicken Sie auf **Baumeinstellungen importieren**, um eine zuvor exportierte JSON-Datei hochzuladen und die Einstellungen anzuwenden.

## Verarbeitung des Familienstammbaums

### Datenbank überprüfen und reparieren

Dieses Tool überprüft die Gramps-Datenbank auf interne Inkonsistenzen und behebt die, die es kann – analog zum [Tool Datenbank überprüfen und reparieren](https://www.gramps-project.org/wiki/index.php/Gramps_5.2_Wiki_Manual_-_Tools#Check_and_Repair_Database) in Gramps Desktop.

Klicken Sie auf **Überprüfen und Reparieren** und warten Sie, bis der Fortschrittsindikator abgeschlossen ist. Das Ergebnis wird unter dem Button angezeigt:

- Wenn keine Fehler gefunden wurden, wird eine Bestätigungsnachricht angezeigt.
- Wenn Fehler gefunden wurden, wird eine Zusammenfassung der angewendeten Korrekturen angezeigt.

Führen Sie dieses Tool aus, wenn Sie unerwartete Fehler oder Verhaltensweisen feststellen, die durch Datenbankinkonsistenzen verursacht werden könnten, wie z. B. fehlende Beziehungen zwischen Objekten.

## Gefahrenzone

!!! danger
    Aktionen in der Gefahrenzone sind **irreversibel**. Machen Sie ein Backup, bevor Sie fortfahren.

### Alle Objekte löschen

Entfernt Objekte aus dem Familienstammbaum. Ein Klick auf **Löschen** öffnet einen Dialog, in dem Sie wählen können, ob Sie löschen möchten:

- **Alle Objekte** – leert den Baum vollständig
- **Bestimmte Objekttypen** – zum Beispiel nur Ereignisse oder nur Medienobjekte

Sie werden aufgefordert, sich erneut zu authentifizieren (sich erneut anzumelden), um die Aktion zu bestätigen. Die Löschung wird als Hintergrundaufgabe ausgeführt und ein Fortschrittsindikator wird angezeigt.

!!! warning
    Das Löschen nur einer Teilmenge von Objekttypen (anstatt aller Objekte auf einmal) kann bei großen Bäumen sehr lange dauern, da der Server alle Beziehungen zwischen Objekten überprüfen und aktualisieren muss.

!!! tip
    Verwenden Sie dies, um frisch zu starten, bevor Sie einen neuen Baum importieren, oder um bestimmte Objekttypen zu entfernen, die falsch importiert wurden.
