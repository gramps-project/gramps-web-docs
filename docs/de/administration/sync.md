# Gramps Web und Gramps Desktop synchronisieren

*Gramps Web Sync* ist ein Add-on für Gramps, das die Gramps-Datenbank auf deinem Desktop-Computer mit Gramps Web synchronisiert, einschließlich Mediendateien. Änderungen auf beiden Seiten werden jeweils auf die andere Seite übertragen, sodass du lokal und im Web am selben Stammbaum arbeiten kannst.

Wie jedes Synchronisierungstool ist es kein Backup: Wenn du etwas auf einer Seite löschst, wird es auch auf der anderen Seite gelöscht. Erstelle regelmäßig Backups deines Stammbaums im Gramps-XML-Format.

## Installation

Das Add-on erfordert Gramps 6.0 mit Python 3.10 oder neuer. Es ist in Gramps Desktop verfügbar und kann [auf die übliche Weise](https://www.gramps-project.org/wiki/index.php/5.2_Addons#Installing_Addons_in_Gramps) installiert werden. Diese Dokumentation beschreibt die neueste Version des Add-ons. Verwende bei Bedarf den Gramps-Add-on-Manager, um es zu aktualisieren.

Auf deinem Desktop und deinem Server muss dieselbe Gramps-Version ausgeführt werden. Die Version hat das Format `MAJOR.MINOR.PATCH`, wobei `MAJOR` und `MINOR` übereinstimmen müssen. Unter [Hilfe erhalten](../help/help.md) erfährst du, wie du herausfindest, welche Gramps-Version auf deinem Server ausgeführt wird.

### Serveranforderungen

Das Add-on prüft unmittelbar nach der Verbindung, bevor etwas heruntergeladen wird, zwei Dinge zu deinem Server und bricht mit einer Meldung ab, wenn eine der Anforderungen nicht erfüllt ist:

- **Gramps-Web-API-Version 3.x.** Diese Version des Add-ons für Gramps 6.0 funktioniert mit der Gramps-Web-API 3. Ein älterer Server muss aktualisiert werden. Ein Server mit einer *neueren* API-Hauptversion benötigt eine neuere Gramps-Version, nicht ein neueres Add-on, da jede Gramps-Versionsreihe mit einer API-Version gekoppelt ist. Du findest die Version deines Servers unter *Einstellungen ▸ Versionsinformationen* in Gramps Web.
- **Eine Hintergrundaufgabenwarteschlange.** Änderungen werden auf dem Server als Hintergrundaufgabe angewendet. Ohne eine Aufgabenwarteschlange würde dies synchron ausgeführt und bei jedem realistischen Stammbaum zu einer Zeitüberschreitung führen.

Um Änderungen auf die entfernte Datenbank anzuwenden, benötigst du ein Konto mit der Rolle Editor, Eigentümer oder Administrator.

### Passwort speichern (optional)

Installiere `keyring` (z. B. mit `sudo apt install python3-keyring` oder `sudo dnf install python3-keyring`), um das API-Passwort im Passwortmanager deines Systems zu speichern. Wenn der Schlüsselbund nicht verwendet werden kann, teilt das Add-on dies mit und arbeitet ohne ihn weiter – du wirst dann einfach jedes Mal nach deinem Passwort gefragt.

Beim Gramps-**Snap**-Paket wird der Systemschlüsselbund durch die Einschränkungen blockiert, bis du die Schnittstelle einmal verbindest. Das Add-on zeigt diesen Befehl an, wenn es die Situation erkennt:

```bash
snap connect gramps:password-manager-service
```

Bei vielen Gnome-Desktopkonfigurationen bedeutet ein [Fehler in python keyring](https://github.com/jaraco/keyring/issues/496), dass du die Konfigurationsdatei `~/.config/python_keyring/keyringrc.cfg` mit folgendem Inhalt erstellen musst:

```ini
[backend]
default-keyring=keyring.backends.SecretService.Keyring
```

## Verwendung

Das Add-on ist in Gramps unter *Werkzeuge ▸ Stammbaumverarbeitung ▸ Gramps&nbsp;Web&nbsp;Sync* verfügbar. Nachdem du den Dialog bestätigt hast, der davor warnt, dass der Rückgängig-Verlauf verworfen wird, öffnet sich das Synchronisierungsfenster. Es werden keine Änderungen auf deinen lokalen Stammbaum oder den Server angewendet, bis du sie ausdrücklich bestätigst.

Eine Leiste am oberen Rand des Fensters nennt den Stammbaum, mit dem du synchronisierst, das zugehörige Konto und die Adresse sowie den Zeitpunkt der letzten Synchronisierung. Unten werden die Version des Add-ons und die Version der Web-API des Servers angezeigt, was bei der Meldung eines Problems hilfreich ist.

### Verbinden

Wenn du diesen Stammbaum bereits zuvor synchronisiert hast und dein Passwort gespeichert ist, stellt das Add-on beim Öffnen sofort eine Verbindung her und geht direkt zum Vergleich über. Andernfalls fragt es nach der Basis-URL deiner Gramps-Web-Instanz (Beispiel: `https://mygrampsweb.com/`), deinem Benutzernamen und deinem Passwort.

Die URL und der Benutzername werden als Klartext in deinem Gramps-Benutzerverzeichnis gespeichert. Das Passwort wird nur dann im Passwortmanager deines Systems gespeichert, wenn **Passwort speichern** aktiviert bleibt. Wenn du die Option deaktivierst, wird ein bereits für diesen Server gespeichertes Passwort entfernt. Wenn du eine Adresse eingibst, die mit `http://` statt mit `https://` beginnt, warnt dich das Add-on bereits während der Eingabe, da dein Passwort im Klartext übertragen würde.

Jeder Server, mit dem du synchronisierst, wird separat gespeichert, einschließlich seiner eigenen Aufzeichnung des Zeitpunkts der letzten Synchronisierung, sodass du zwischen zwei Servern wechseln kannst, ohne den jeweils anderen zu beeinflussen. Jeder Eintrag zeichnet außerdem auf, von welchem lokalen Stammbaum zuletzt synchronisiert wurde. Das Add-on stellt nur dann automatisch eine Verbindung her, wenn dieser Stammbaum mit dem geöffneten Stammbaum übereinstimmt. Andernfalls zeigt es die Verbindungsdetails an und wartet darauf, dass du auf *Verbinden* klickst.

Solange keine Daten geschrieben werden, stehen zwei Aktionen zur Verfügung:

- **Server ändern …** in der oberen Leiste führt zurück zu den Verbindungsdetails, damit du diesen Stammbaum auf einen anderen Server verweisen kannst. Ein laufender Vergleich wird unterbrochen, statt dass du auf dessen Abschluss warten musst.
- **Diesen Server vergessen** im Verbindungsbereich entfernt die gespeicherte Adresse, den Benutzernamen und das Passwort sowie die Aufzeichnung des Zeitpunkts, zu dem dieser Stammbaum zuletzt synchronisiert wurde. Bei der nächsten Synchronisierung werden die beiden Stammbäume von Grund auf verglichen.

### Änderungen prüfen

Das Add-on vergleicht die lokale und die entfernte Datenbank und zeigt die geplanten Aktionen an, gruppiert danach, welche Datenbank sie ändern:

```
▾ Wird auf diesem Computer geändert (7 Objekte)
    ▾ 3 Objekte hinzufügen
        Person   John Smith        I0123
    ▾ 4 Objekte aktualisieren
        …
▾ Wird auf dem Server geändert (5 Objekte)
    …
```

Jede Zeile nennt das Objekt, damit du erkennen kannst, wer oder was betroffen ist, statt nur eine Gramps-ID zu sehen. Wenn etwas gelöscht werden soll, weist ein Hinweis über der Liste darauf hin, wie viele Objekte auf welcher Seite betroffen sind.

Klicke auf **Anwenden**, um die in der Liste beschriebenen Aktionen auszuführen.

Das Synchronisierungsfenster blockiert den übrigen Teil von Gramps nicht, sodass du weiterarbeiten kannst, während die Liste geöffnet ist. Wenn du in der Zwischenzeit ein betroffenes Objekt bearbeitest, erkennt das Add-on dies beim Klicken auf „Anwenden“, nimmt keine Änderungen vor und fordert dich auf, den Vergleich erneut durchzuführen.

#### Synchronisierungsmodus

Der Synchronisierungsmodus wird oberhalb der Änderungsliste ausgewählt. Wenn du ihn änderst, wird die Liste neu erstellt, da der Modus bestimmt, was aus jeder Abweichung wird.

- **Bidirektionale Synchronisierung** (Standard) – Änderungen von beiden Seiten werden zusammengeführt. Objekte, die an beiden Orten bearbeitet wurden, werden zusammengeführt.
- **Server an diesen Computer anpassen** – Der Server wird an diesen Computer angepasst. Alles, was nur auf dem Server geändert wurde, wird verworfen.
- **Diesen Computer an den Server anpassen** – Dieser Computer wird an den Server angepasst. Alles, was nur hier geändert wurde, wird verworfen.

Der in Versionen vor 1.5 verfügbare **Zusammenführen**-Modus wurde entfernt. Er unterschied sich von der bidirektionalen Synchronisierung nur dadurch, dass er auf einer Seite gelöschte Objekte wiederherstellte, anstatt die Löschung zu übertragen. Wenn du dich darauf verlassen hast, verwende die bidirektionale Synchronisierung und stelle alles, was du behalten möchtest, aus einem Backup wieder her.

### Mediendateien

Mediendateien werden als Teil derselben Bestätigung verarbeitet, nicht als separater Schritt. Wenn Dateien übertragen werden müssen, bietet ein Kontrollkästchen unterhalb der Liste an, sie zu verschieben:

```
[x] Außerdem 12 Mediendateien übertragen (4 herunterladen, 8 hochladen)
```

Deaktiviere das Kontrollkästchen, um die Objektänderungen zu synchronisieren, ohne die Dateien anzufassen.

Dateien, die auf *beiden* Seiten fehlen, werden separat aufgeführt, da nichts mit ihnen geschehen kann:

```
2 Mediendateien fehlen auf beiden Seiten und können nicht übertragen werden.
```

Die Synchronisierung von Mediendateien hat zwei Einschränkungen:

- Wenn eine lokale Datei eine andere Prüfsumme als die in der Gramps-Datenbank gespeicherte aufweist (dies kann z. B. bei Word-Dateien vorkommen, die nach dem Hinzufügen zu Gramps bearbeitet wurden), schlägt der Upload mit einer Fehlermeldung fehl.
- Das Werkzeug überprüft nicht die Integrität aller lokalen Dateien. Wenn eine Datei unter dem für das Medienobjekt gespeicherten Pfad vorhanden ist, sich aber von der Datei auf dem Server unterscheidet, erkennt das Werkzeug dies nicht. Verwende das Add-on „Medien überprüfen“, um Dateien mit falschen Prüfsummen zu finden.

### Wenn eine Synchronisierung fehlschlägt

Wenn eine Synchronisierung途中 fehlschlägt – etwa wegen einer unterbrochenen Verbindung –, meldet das Add-on, was bereits angewendet wurde, und bietet **Erneut versuchen** an. Dadurch wird mit dem fehlgeschlagenen Schritt fortgefahren, statt von vorn zu beginnen. Die heruntergeladene Kopie des entfernten Stammbaums bleibt erhalten, sodass sie beim erneuten Versuch nicht noch einmal heruntergeladen und verglichen wird.

Technische Einzelheiten zum Fehler sind hinter einem Aufklappelement *Details* verfügbar. Eine Schaltfläche ermöglicht es, sie für einen Fehlerbericht zu kopieren.

## Fehlerbehebung

**Unerwartete Änderungen.** Wenn das Add-on eine alarmierend hohe Anzahl von Löschungen vorschlägt, überprüfe zuerst die obere Leiste: Sie nennt den Stammbaum auf dem Server, in den du gleich schreiben wirst. Wenn du einen Stammbaum mit einem Server abgleichst, der einen *anderen* Stammbaum enthält, führt dies genau zu diesem Symptom.

Andernfalls können unerwartete Unterschiede durch Inkonsistenzen in einer der Datenbanken oder durch nicht synchronisierte Uhren zwischen deinem Computer und deinem Server verursacht werden. Überprüfe, ob beide Uhren korrekt eingestellt sind (die Zeitzone spielt keine Rolle, da das Werkzeug Unix-Zeitstempel verwendet), und führe das Werkzeug zum Prüfen und Reparieren deiner lokalen Datenbank aus. Als letzte Möglichkeit exportierst du deine lokale Datenbank nach Gramps XML und importierst sie in eine neue, leere Datenbank. Dies ist ein verlustfreier Vorgang, stellt aber sicher, dass alle Daten konsistent gespeichert werden.

**Fehler bei Mediendateien.** Ein fehlgeschlagener Upload wird häufig durch eine Abweichung zwischen der Prüfsumme der Datei auf dem Datenträger und der Prüfsumme in der lokalen Gramps-Datenbank verursacht. Dies geschieht bei bearbeitbaren Dateien wie außerhalb von Gramps bearbeiteten Office-Dokumenten. Verwende das Gramps-Add-on „Medien überprüfen“, um die Prüfsummen zu korrigieren.

**Berechtigungsfehler.** Überprüfe die Rolle deines Gramps-Web-Benutzerkontos: Nur Editoren, Eigentümer und Administratoren können Änderungen auf die entfernte Datenbank anwenden.

### Hilfe erhalten

Wenn nichts davon hilft, frage die Community, indem du im [Gramps-Forum in der Kategorie Gramps Web](https://gramps.discourse.group/c/gramps-web/28) einen Beitrag erstellst. Bitte gib Folgendes an:

- die Version des Add-ons Gramps Web Sync, die unten im Synchronisierungsfenster neben der Web-API-Version des Servers angezeigt wird (und verwende bitte die neueste veröffentlichte Version)
- die Version von Gramps Desktop, die du verwendest
- die Versionsinformationen von Gramps Web, zu finden unter *Einstellungen ▸ Versionsinformationen*
- alle Einzelheiten zu deiner Gramps-Web-Installation (selbst gehostet, Grampshub, …)
- die Ausgabe deiner Gramps-Web-Serverprotokolle, falls du darauf Zugriff hast (bei Verwendung von Docker: `docker compose logs --tail 100 grampsweb` und `docker compose logs --tail 100 grampsweb-celery`)

Wenn du um ein Debug-Protokoll gebeten wirst, starte Gramps [über die Befehlszeile](https://gramps-project.org/wiki/index.php/Gramps_5.2_Wiki_Manual_-_Command_Line) mit aktivierter Debug-Protokollierung und reproduziere das Problem:

```bash
gramps --debug grampswebsync
```

## Hintergrund: Funktionsweise des Add-ons

Das Add-on soll eine lokale Gramps-Datenbank mit einer entfernten Gramps-Web-Datenbank synchron halten und dabei Änderungen sowohl lokal als auch entfernt ermöglichen (kollaborative Bearbeitung).

Es ist **nicht geeignet**

- für die Synchronisierung mit einer Datenbank, die keine direkte Ableitung (ausgehend von einer Datenbankkopie oder einem Gramps-XML-Export/-Import) der lokalen Datenbank ist,
- zum Zusammenführen zweier Datenbanken mit einer großen Anzahl von Änderungen auf beiden Seiten, die beim Zusammenführen manuelle Aufmerksamkeit erfordern. Verwende dafür das hervorragende [Werkzeug zum Zusammenführen von Importen](https://www.gramps-project.org/wiki/index.php/Import_Merge_Tool).

Die Funktionsweise beruht auf einfachen Prinzipien:

- Es vergleicht die lokale und die entfernte Datenbank.
- Wenn es Unterschiede gibt, überprüft es den Zeitstempel des letzten identischen Objekts, den wir **t** nennen.
- Wenn ein Objekt, das später als **t** geändert wurde, in einer Datenbank vorhanden ist, in der anderen aber nicht, wird es mit beiden synchronisiert (Annahme: neues Objekt).
- Wenn ein Objekt, das zuletzt vor **t** geändert wurde, in einer Datenbank fehlt, wird es in beiden gelöscht (Annahme: gelöschtes Objekt).
- Wenn ein Objekt unterschiedlich ist, aber nur in einer Datenbank nach **t** geändert wurde, wird es mit der anderen synchronisiert (Annahme: geändertes Objekt).
- Wenn ein Objekt unterschiedlich ist, aber in beiden Datenbanken nach **t** geändert wurde, werden sie zusammengeführt (Annahme: widersprüchliche Änderung).

Der Zeitpunkt der letzten erfolgreichen Synchronisierung wird ebenfalls separat für jeden Server aufgezeichnet und als **t** verwendet, wenn er neuer ist als das neueste identische Objekt.

Dieser Algorithmus ist einfach und robust, da keine Synchronisierungsverläufe nachverfolgt werden müssen. Er funktioniert jedoch am besten, wenn du *häufig synchronisierst*.
