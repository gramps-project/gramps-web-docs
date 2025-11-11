# Synchronisieren von Gramps Web und Gramps Desktop

*Gramps Web Sync* ist ein Addon für Gramps, das es ermöglicht, Ihre Gramps-Datenbank auf Ihrem Desktop-Computer mit Gramps Web zu synchronisieren, einschließlich Mediendateien.

!!! warning
    Wie bei jedem Synchronisierungstool sollten Sie dies nicht als Backup-Tool betrachten. Eine versehentliche Löschung auf einer Seite wird auf die andere Seite übertragen. Stellen Sie sicher, dass Sie regelmäßige Backups (im Gramps XML-Format) Ihres Stammbaums erstellen.

!!! info
    Die Dokumentation bezieht sich auf die neueste Version des Gramps Web Sync Addons. Bitte verwenden Sie den Gramps-Addon-Manager, um das Addon bei Bedarf auf die neueste Version zu aktualisieren.

## Installation

Das Addon erfordert Gramps 6.0, das auf Python 3.10 oder neuer läuft. Es ist in Gramps Desktop verfügbar und kann [auf die übliche Weise](https://www.gramps-project.org/wiki/index.php/5.2_Addons#Installing_Addons_in_Gramps) installiert werden.

!!! warn
    Bitte stellen Sie sicher, dass Sie die gleiche Version von Gramps auf Ihrem Desktop verwenden wie die, die auf Ihrem Server läuft. Siehe den Abschnitt [Hilfe erhalten](../help/help.md), um herauszufinden, welche Gramps-Version Ihr Server verwendet. Die Gramps-Version hat die Form `MAJOR.MINOR.PATCH`, und `MAJOR` und `MINOR` müssen sowohl im Web als auch auf dem Desktop gleich sein.

Optionaler Schritt:

??? note inline end "Gnome-Keyring-Fehler"
    Derzeit gibt es einen [Fehler im Python-Keyring](https://github.com/jaraco/keyring/issues/496), der viele Gnome-Desktop-Konfigurationen betrifft. Möglicherweise müssen Sie die Konfigurationsdatei `~/.config/python_keyring/keyringrc.cfg` erstellen und sie so bearbeiten:

        [backend]
        default-keyring=keyring.backends.SecretService.Keyring

- Installieren Sie `keyring` (z. B. `sudo apt install python3-keyring` oder `sudo dnf install python3-keyring`), um das sichere Speichern des API-Passworts im Passwortmanager Ihres Systems zu ermöglichen.

## Verwendung

Nach der Installation ist das Addon in Gramps unter *Werkzeuge > Stammbaumverarbeitung > Gramps&nbsp;Web&nbsp;Sync* verfügbar. Nach dem Start und der Bestätigung des Dialogs, dass der Rückgängig-Verlauf verworfen wird, wird ein Assistent Sie durch die Synchronisierungsschritte führen. Beachten Sie, dass keine Änderungen an Ihrem lokalen Baum oder am Server vorgenommen werden, bis Sie diese ausdrücklich bestätigen.

### Schritt 1: Serveranmeldeinformationen eingeben

Das Tool fragt Sie nach der Basis-URL (Beispiel: `https://mygrampsweb.com/`) Ihrer Gramps Web-Instanz, Ihrem Benutzernamen und Passwort. Sie benötigen ein Konto mit mindestens Bearbeitungsrechten, um Änderungen in Ihre entfernte Datenbank zurückzusynchronisieren. Der Benutzername und die URL werden im Klartext in Ihrem Gramps-Benutzerverzeichnis gespeichert, das Passwort wird nur gespeichert, wenn `keyring` installiert ist (siehe oben).

### Schritt 2: Änderungen überprüfen

Nachdem Sie Ihre Anmeldeinformationen bestätigt haben, vergleicht das Tool die lokalen und entfernten Datenbanken und bewertet, ob es Unterschiede gibt. Wenn ja, wird eine Liste der Objektänderungen angezeigt (wobei ein Objekt eine Person, Familie, Ereignis, Ort usw. sein kann), die einer der folgenden Kategorien angehören:

- lokal hinzugefügt
- lokal gelöscht
- lokal geändert
- remote hinzugefügt 
- remote gelöscht
- remote geändert
- gleichzeitig geändert (d. h. auf beiden Seiten)

Das Tool verwendet Zeitstempel, um zu bewerten, welche Seite für jedes Objekt neuer ist (siehe "Hintergrund" unten, wenn Sie an den Details interessiert sind).

Wenn die Änderungen wie erwartet aussehen, können Sie auf "Anwenden" klicken, um die erforderlichen Änderungen an den lokalen und den entfernten Datenbanken anzuwenden.

!!! tip "Erweitert: Synchronisierungsmodus"
    Unter der Liste der Änderungen können Sie einen Synchronisierungsmodus auswählen.

    Der Standardmodus, **bidirektionale Synchronisierung**, bedeutet, dass Änderungen auf beiden Seiten (lokal und remote) angewendet werden, indem die erkannten Änderungen repliziert werden (lokal hinzugefügte Objekte werden auf der remote Seite hinzugefügt usw.). Objekte, die auf beiden Seiten geändert wurden, werden ebenfalls zusammengeführt und aktualisiert.

    Die Option **remote auf lokal zurücksetzen** stellt sicher, dass die entfernte Gramps-Datenbank genau wie die lokale aussieht. Alle Objekte, die als "remote hinzugefügt" erkannt wurden, werden wieder gelöscht, Objekte, die als "remote gelöscht" erkannt wurden, werden wieder hinzugefügt usw. *Es werden keine Änderungen an der lokalen Gramps-Datenbank angewendet.*

    Die Option **lokal auf remote zurücksetzen** funktioniert umgekehrt und setzt den lokalen Zustand auf den der entfernten Datenbank. *Es werden keine Änderungen an der entfernten Datenbank angewendet.*

    Schließlich ist die Option **zusammenführen** ähnlich wie die bidirektionale Synchronisierung, da sie beide Datenbanken ändert, aber *keine Objekte löscht*, sondern stattdessen alle Objekte wiederherstellt, die nur auf einer Seite gelöscht wurden.

### Schritt 3: Mediendateien synchronisieren

*Nachdem* die Datenbanken synchronisiert wurden, überprüft das Tool auf neue oder aktualisierte Mediendateien. Wenn es welche findet, wird eine Liste angezeigt und um Bestätigung gebeten, um die erforderlichen Dateien hochzuladen/herunterzuladen.

Beachten Sie die folgenden Einschränkungen der Mediendateisynchronisierung:

- Wenn eine lokale Datei eine andere Prüfziffer hat als die in der Gramps-Datenbank gespeicherte (dies kann z. B. bei Word-Dateien passieren, wenn sie nach dem Hinzufügen zu Gramps bearbeitet werden), schlägt der Upload mit einer Fehlermeldung fehl.
- Das Tool überprüft nicht die Integrität aller lokalen Dateien. Wenn eine lokale Datei unter dem für das Medienobjekt gespeicherten Pfad existiert, die Datei jedoch von der Datei auf dem Server abweicht, wird das Tool dies nicht erkennen. Verwenden Sie das Media Verify Addon, um Dateien mit falschen Prüfziffern zu erkennen.

## Fehlersuche

### Debug-Protokollierung

Wenn Sie Probleme mit dem Sync-Addon haben, starten Sie Gramps bitte mit aktivierter Debug-Protokollierung, indem Sie [Gramps von der Kommandozeile aus starten](https://gramps-project.org/wiki/index.php/Gramps_5.2_Wiki_Manual_-_Command_Line) mit der folgenden Option:

```bash
gramps --debug grampswebsync
```

Dies wird viele hilfreiche Protokollmeldungen in der Kommandozeile ausgeben, die Ihnen helfen, die Ursache des Problems zu identifizieren.

### Serveranmeldeinformationen

Wenn der erste Schritt bereits fehlschlägt, überprüfen Sie bitte die Server-URL, Ihren Benutzernamen und Ihr Passwort.

### Berechtigungsprobleme

Wenn Sie auf einen Fehler stoßen, der Berechtigungen betrifft, überprüfen Sie bitte die Benutzerrolle Ihres Gramps Web-Benutzerkontos. Sie können nur Änderungen an der entfernten Datenbank vornehmen, wenn Sie ein Benutzer mit der Rolle Editor, Eigentümer oder Administrator sind.

### Unerwartete Datenbankänderungen

Wenn das Synchronisierungstool Änderungen erkennt, von denen Sie denken, dass sie nicht passiert sind, könnte es sein, dass es Inkonsistenzen in einer der Datenbanken gibt, die Gramps dazu bringen, einen Unterschied zu erkennen, oder dass die Zeit zwischen Ihrem lokalen Computer und Ihrem Server nicht synchron ist.

Bitte überprüfen Sie, ob die Uhren auf beiden Maschinen korrekt eingestellt sind (beachten Sie, dass die Zeitzone keine Rolle spielt, da das Tool Unix-Zeitstempel verwendet, die zeitzonenunabhängig sind).

Sie können auch das Überprüfungs- und Reparaturtool auf Ihrer lokalen Datenbank ausführen und sehen, ob dies hilft.

Eine brutale, aber effektive Methode, um sicherzustellen, dass Inkonsistenzen in Ihrer lokalen Datenbank keine falschen Positivmeldungen verursachen, besteht darin, Ihre Datenbank in Gramps XML zu exportieren und in eine neue, leere Datenbank zu importieren. Dies ist ein verlustfreier Vorgang, stellt jedoch sicher, dass alle Daten konsistent importiert werden.

### Timeout-Fehler

Wenn Sie Timeout-Fehler (z. B. angezeigt durch einen HTTP-Status 408-Fehler oder eine andere Fehlermeldung, die das Wort "Timeout" enthält) erleben, liegt dies wahrscheinlich an einer großen Anzahl von Änderungen, die mit Ihrer Serverkonfiguration synchronisiert werden müssen.

Für Versionen des Sync-Addons vor v1.2.0 und Versionen der Gramps Web API vor v2.7.0 (siehe den Versionsinformationen-Tab in Gramps Web) wurde die Synchronisierung zur Serverseite in einer einzigen Anfrage verarbeitet, die je nach Serverkonfiguration nach ein bis maximal wenigen Minuten abgelaufen ist. Bei großen Synchronisierungen (z. B. nach dem Import von Tausenden von Objekten in die lokale Datenbank oder dem Versuch, eine vollständige lokale Datenbank mit einer leeren Serverdatenbank zu synchronisieren) kann dies zu kurz sein.

Wenn Sie das Sync-Addon v1.2.0 oder später und die Gramps Web API v2.7.0 oder später verwenden, wird die serverseitige Synchronisierung von einem Hintergrundarbeiter verarbeitet und kann sehr lange laufen (ein Fortschrittsbalken wird angezeigt), und Timeout-Fehler sollten nicht auftreten.

### Unerwartete Fehler bei Mediendateien

Wenn das Hochladen einer Mediendatei fehlschlägt, liegt dies oft an einer Diskrepanz in der Prüfziffer der tatsächlichen Datei auf der Festplatte und der Prüfziffer in der lokalen Gramps-Datenbank. Dies geschieht häufig bei bearbeitbaren Dateien wie Office-Dokumenten, die außerhalb von Gramps bearbeitet wurden. Bitte verwenden Sie das Gramps Media Verify Addon, um die Prüfziffern aller Mediendateien zu korrigieren.

### Hilfe anfordern

Wenn all dies nicht hilft, können Sie die Community um Hilfe bitten, indem Sie im [Gramps Web-Bereich des Gramps-Forums](https://gramps.discourse.group/c/gramps-web/28) posten. Bitte stellen Sie sicher, dass Sie Folgendes angeben:

- die Version des Gramps Web Sync-Addons (und verwenden Sie bitte die neueste veröffentlichte Version)
- die Version von Gramps Desktop, die Sie verwenden
- die Ausgabe der Gramps-Debug-Protokollierung, die wie oben beschrieben aktiviert wurde
- die Versionsinformationen von Gramps Web (Sie finden sie unter Einstellungen/Versionsinformationen)
- alle Details, die Sie zu Ihrer Gramps Web-Installation angeben können (selbstgehostet, Grampshub, ...)
- die Ausgabe Ihrer Gramps Web-Serverprotokolle, wenn Sie Zugriff darauf haben (bei Verwendung von Docker: `docker compose logs --tail 100 grampsweb` und `docker compose logs --tail 100 grampsweb-celery`)

## Hintergrund: Wie das Addon funktioniert

Wenn Sie neugierig sind, wie das Addon tatsächlich funktioniert, finden Sie in diesem Abschnitt einige weitere Details.

Das Addon soll eine lokale Gramps-Datenbank mit einer entfernten Gramps Web-Datenbank synchron halten, um sowohl lokale als auch entfernte Änderungen zu ermöglichen (kollaborative Bearbeitung).

Es ist **nicht geeignet**

- um mit einer Datenbank zu synchronisieren, die nicht eine direkte Ableitung (beginnend mit einer Datenbankkopie oder Gramps XML-Export/Import) der lokalen Datenbank ist
- um zwei Datenbanken mit einer großen Anzahl von Änderungen auf beiden Seiten zu verschmelzen, die manuelle Aufmerksamkeit für das Zusammenführen erfordern. Verwenden Sie zu diesem Zweck das ausgezeichnete [Import Merge Tool](https://www.gramps-project.org/wiki/index.php/Import_Merge_Tool).

Die Funktionsprinzipien des Tools sind sehr einfach:

- Es vergleicht die lokalen und entfernten Datenbanken
- Wenn es Unterschiede gibt, überprüft es den Zeitstempel des letzten identischen Objekts, nennen wir es **t**
- Wenn ein Objekt in einer Datenbank existiert, das nach **t** geändert wurde, aber nicht in der anderen, wird es in beide synchronisiert (angenommen neues Objekt)
- Wenn ein Objekt das letzte Mal vor **t** geändert wurde und in einer Datenbank fehlt, wird es in beiden gelöscht (angenommen gelöschtes Objekt)
- Wenn ein Objekt unterschiedlich ist, aber nach **t** nur in einer Datenbank geändert wurde, wird es in die andere synchronisiert (angenommen modifiziertes Objekt)
- Wenn ein Objekt unterschiedlich ist, aber nach **t** in beiden Datenbanken geändert wurde, werden sie zusammengeführt (angenommene Konfliktänderung)

Dieser Algorithmus ist einfach und robust, da er keine Verfolgung der Synchronisierungshistorie erfordert. Er funktioniert jedoch am besten, wenn Sie *häufig synchronisieren*.
