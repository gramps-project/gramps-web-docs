# Synchronisieren von Gramps Web und Gramps Desktop

*Gramps Web Sync* ist ein Addon für Gramps, das die Gramps-Datenbank auf Ihrem Desktop-Computer mit Gramps Web synchronisiert, einschließlich Mediendateien. Änderungen, die auf einer Seite vorgenommen werden, werden auf die andere übertragen, sodass Sie lokal und im Web am selben Stammbaum arbeiten können.

Wie bei jedem Synchronisierungstool ist es kein Backup: Wenn Sie etwas auf einer Seite löschen, wird es auch auf der anderen Seite gelöscht. Halten Sie regelmäßige Backups Ihres Stammbaums im Gramps XML-Format.

## Installation

Das Addon erfordert Gramps 6.0, das auf Python 3.10 oder neuer läuft. Es ist in Gramps Desktop verfügbar und kann [auf die übliche Weise](https://www.gramps-project.org/wiki/index.php/5.2_Addons#Installing_Addons_in_Gramps) installiert werden. Diese Dokumentation beschreibt die neueste Version des Addons; verwenden Sie den Gramps-Addon-Manager, um es bei Bedarf zu aktualisieren.

Ihr Desktop und Ihr Server müssen die gleiche Version von Gramps ausführen. Die Version hat die Form `MAJOR.MINOR.PATCH`, und `MAJOR` und `MINOR` müssen übereinstimmen. Siehe [Hilfe erhalten](../help/help.md), um herauszufinden, welche Gramps-Version Ihr Server verwendet.

### Serveranforderungen

Das Addon überprüft zwei Dinge über Ihren Server, sobald es sich verbindet, bevor irgendetwas heruntergeladen wird, und stoppt mit einer Nachricht, wenn eines davon nicht erfüllt ist:

- **Gramps Web API Version 3.x.** Diese Version des Addons, für Gramps 6.0, funktioniert mit Gramps Web API 3. Ein älterer Server muss aktualisiert werden; ein Server, der eine *neuere* API-Hauptversion ausführt, benötigt eine neuere Version von Gramps, nicht ein neueres Addon, da jede Gramps-Version mit einer API-Version gepaart ist. Sie können die Version Ihres Servers unter *Einstellungen ▸ Versionsinfo* in Gramps Web finden.
- **Eine Hintergrundaufgabenwarteschlange.** Änderungen werden auf dem Server als Hintergrundaufgabe angewendet. Ohne eine Aufgabenwarteschlange würde dies synchron ausgeführt werden und bei jedem echten Stammbaum zeitlich auslaufen.

Um Änderungen an der entfernten Datenbank anzuwenden, benötigen Sie ein Konto mit der Rolle Editor, Eigentümer oder Administrator.

### Speicherung Ihres Passworts (optional)

Installieren Sie `keyring` (z.B. `sudo apt install python3-keyring` oder `sudo dnf install python3-keyring`), um das API-Passwort im Passwortmanager Ihres Systems zu speichern. Wenn der Schlüsselbund nicht verwendet werden kann, sagt das Addon dies und fährt ohne ihn fort – Sie werden einfach jedes Mal nach Ihrem Passwort gefragt.

Im Gramps **Snap**-Paket ist der System-Schlüsselbund durch Einschränkungen blockiert, bis Sie die Schnittstelle einmal verbinden. Das Addon zeigt diesen Befehl an, wenn es die Situation erkennt:

```bash
snap connect gramps:password-manager-service
```

In vielen Gnome-Desktop-Konfigurationen bedeutet ein [Fehler im Python-Keyring](https://github.com/jaraco/keyring/issues/496), dass Sie die Konfigurationsdatei `~/.config/python_keyring/keyringrc.cfg` mit folgendem Inhalt erstellen müssen:

```ini
[backend]
default-keyring=keyring.backends.SecretService.Keyring
```

## Verwendung

Das Addon ist in Gramps unter *Werkzeuge ▸ Stammbaumverarbeitung ▸ Gramps&nbsp;Web&nbsp;Sync* verfügbar. Nach Bestätigung der Dialogwarnung, dass der Rückgängig-Verlauf verworfen wird, öffnet sich das Synchronisierungsfenster. Es werden keine Änderungen an Ihrem lokalen Baum oder am Server angewendet, bis Sie diese ausdrücklich bestätigen.

Ein Streifen oben im Fenster nennt den Stammbaum, mit dem Sie synchronisieren, das Konto und die Adresse, zu der es gehört, und wann es zuletzt synchronisiert wurde. Unten werden die Version des Addons und der Web-API des Servers angezeigt, was nützlich ist, wenn Sie ein Problem melden.

### Verbindung herstellen

Wenn Sie diesen Stammbaum zuvor synchronisiert haben und Ihr Passwort gespeichert ist, verbindet sich das Addon, sobald es geöffnet wird, und geht direkt zum Vergleich über. Andernfalls fragt es nach der Basis-URL Ihrer Gramps Web-Instanz (Beispiel: `https://mygrampsweb.com/`), Ihrem Benutzernamen und Ihrem Passwort.

Die URL und der Benutzername werden im Klartext in Ihrem Gramps-Benutzerverzeichnis gespeichert. Das Passwort wird nur im Passwortmanager Ihres Systems gespeichert, wenn Sie **Passwort merken** aktiviert lassen; das Deaktivieren entfernt jedes bereits für diesen Server gespeicherte Passwort. Wenn Sie eine Adresse eingeben, die mit `http://` anstelle von `https://` beginnt, warnt Sie das Addon beim Tippen, da Ihr Passwort im Klartext gesendet würde.

Jeder Server, mit dem Sie synchronisieren, wird separat gespeichert, zusammen mit seinem eigenen Datensatz, wann er zuletzt synchronisiert wurde, sodass Sie zwischen zwei Servern wechseln können, ohne den einen oder anderen zu stören. Jeder Eintrag zeichnet auch auf, von welchem lokalen Stammbaum er zuletzt synchronisiert wurde. Das Addon verbindet sich nur von selbst, wenn dies mit dem Baum übereinstimmt, den Sie geöffnet haben; andernfalls zeigt es die Verbindungsdetails an und wartet darauf, dass Sie auf *Verbinden* drücken.

Zwei Aktionen sind verfügbar, während nichts geschrieben wird:

- **Server ändern…**, oben im Streifen, kehrt zu den Verbindungsdetails zurück, sodass Sie diesen Baum auf einen anderen Server verweisen können. Es unterbricht einen laufenden Vergleich, anstatt Sie warten zu lassen, bis dieser abgeschlossen ist.
- **Diesen Server vergessen**, im Verbindungsbereich, entfernt die gespeicherte Adresse, den Benutzernamen und das Passwort sowie den Datensatz, wann dieser Baum zuletzt synchronisiert wurde. Die nächste Synchronisierung vergleicht dann die beiden Bäume von Grund auf neu.

### Änderungen überprüfen

Das Addon vergleicht die lokalen und entfernten Datenbanken und zeigt die Aktionen an, die es vorschlägt durchzuführen, gruppiert nach welcher Datenbank sie geändert werden:

```
▾ Wird auf diesem Computer geändert (7 Objekte)
    ▾ 3 Objekte hinzufügen
        Person   John Smith        I0123
    ▾ 4 Objekte aktualisieren
        …
▾ Wird auf dem Server geändert (5 Objekte)
    …
```

Jede Zeile benennt das Objekt, sodass Sie erkennen können, wer oder was betroffen ist, anstatt nur eine Gramps-ID zu sehen. Wenn etwas gelöscht werden soll, steht eine Notiz über der Liste, wie viele Objekte und auf welcher Seite.

Drücken Sie **Übernehmen**, um das auszuführen, was die Liste beschreibt.

Das Synchronisierungsfenster blockiert den Rest von Gramps nicht, sodass Sie weiterarbeiten können, während die Liste geöffnet ist. Wenn Sie in der Zwischenzeit ein betroffenes Objekt bearbeiten, bemerkt das Addon dies, wenn Sie auf Übernehmen drücken, stoppt ohne etwas zu ändern und fordert Sie auf, erneut zu vergleichen.

#### Synchronisierungsmodus

Der Synchronisierungsmodus wird über der Liste der Änderungen ausgewählt. Eine Änderung davon baut die Liste neu auf, da der Modus bestimmt, was jeder Unterschied wird.

- **Bidirektionale Synchronisierung** (Standard) – Änderungen von beiden Seiten werden kombiniert. Objekte, die an beiden Orten bearbeitet wurden, werden zusammengeführt.
- **Server zurücksetzen, um mit diesem Computer übereinzustimmen** – der Server wird so eingestellt, dass er mit diesem Computer übereinstimmt. Alles, was nur auf dem Server geändert wurde, wird verworfen.
- **Diesen Computer zurücksetzen, um mit dem Server übereinzustimmen** – dieser Computer wird so eingestellt, dass er mit dem Server übereinstimmt. Alles, was nur hier geändert wurde, wird verworfen.

Der **Merge**-Modus, der in Versionen vor 1.5 verfügbar war, wurde entfernt. Er unterschied sich von der bidirektionalen Synchronisierung nur darin, dass Objekte, die auf einer Seite gelöscht wurden, wiederhergestellt wurden, anstatt die Löschung zu propagieren. Wenn Sie darauf angewiesen waren, verwenden Sie die bidirektionale Synchronisierung und stellen Sie alles, was Sie behalten möchten, aus einem Backup wieder her.

### Mediendateien

Mediendateien werden als Teil derselben Bestätigung behandelt, nicht als separater Schritt. Wenn Dateien übertragen werden müssen, bietet ein Kontrollkästchen unter der Liste an, sie zu verschieben:

```
[x] Auch 12 Mediendateien übertragen (4 zum Herunterladen, 8 zum Hochladen)
```

Deaktivieren Sie es, um die Objektänderungen zu synchronisieren, ohne die Dateien zu berühren.

Dateien, die auf *beiden* Seiten fehlen, werden separat aufgelistet, da nichts dagegen unternommen werden kann:

```
2 Mediendateien fehlen auf beiden Seiten und können nicht übertragen werden.
```

Die Synchronisierung von Mediendateien hat zwei Einschränkungen:

- Wenn eine lokale Datei eine andere Prüfziffer als die in der Gramps-Datenbank gespeicherte hat (dies kann z.B. bei Word-Dateien passieren, die nach dem Hinzufügen zu Gramps bearbeitet wurden), schlägt der Upload mit einer Fehlermeldung fehl.
- Das Tool überprüft nicht die Integrität aller lokalen Dateien. Wenn eine Datei unter dem für das Medienobjekt gespeicherten Pfad existiert, aber von der Datei auf dem Server abweicht, wird das Tool dies nicht erkennen. Verwenden Sie das Media Verify Addon, um Dateien mit falschen Prüfziffern zu finden.

### Wenn eine Synchronisierung fehlschlägt

Wenn eine Synchronisierung teilweise fehlschlägt – z.B. durch eine unterbrochene Verbindung – berichtet das Addon, was es bereits angewendet hat, und bietet **Erneut versuchen** an, was an dem Schritt fortsetzt, der fehlgeschlagen ist, anstatt von vorne zu beginnen. Die heruntergeladene Kopie des entfernten Baums wird aufbewahrt, sodass ein erneuter Versuch nicht erneut herunterlädt und vergleicht.

Technische Details des Fehlers sind hinter einem *Details*-Erweiterer verfügbar, mit einer Schaltfläche, um sie für einen Fehlerbericht zu kopieren.

## Fehlersuche

**Unerwartete Änderungen.** Wenn das Addon eine alarmierende Anzahl von Löschungen vorschlägt, überprüfen Sie zuerst den oberen Streifen: Er nennt den Stammbaum auf dem Server, auf den Sie schreiben möchten. Die Synchronisierung eines Baums gegen einen Server, der einen *anderen* Baum enthält, erzeugt genau dieses Symptom.

Andernfalls können Unterschiede, die Sie nicht erwartet haben, aus Inkonsistenzen in einer der Datenbanken oder aus Uhren resultieren, die zwischen Ihrem Computer und Ihrem Server nicht synchron sind. Überprüfen Sie, ob beide Uhren korrekt eingestellt sind (die Zeitzone spielt keine Rolle, da das Tool Unix-Zeitstempel verwendet) und führen Sie das Überprüfungs- und Reparaturtool auf Ihrer lokalen Datenbank aus. Als letzte Möglichkeit können Sie Ihre lokale Datenbank in Gramps XML exportieren und in eine neue, leere Datenbank importieren. Dies ist ein verlustfreier Vorgang, stellt jedoch sicher, dass alle Daten konsistent gespeichert werden.

**Fehler bei Mediendateien.** Ein fehlgeschlagener Upload wird häufig durch eine Diskrepanz zwischen der Prüfziffer der Datei auf der Festplatte und der Prüfziffer in der lokalen Gramps-Datenbank verursacht, was bei bearbeitbaren Dateien wie Bürodokumenten, die außerhalb von Gramps bearbeitet wurden, passiert. Verwenden Sie das Gramps Media Verify Addon, um die Prüfziffern zu korrigieren.

**Berechtigungsfehler.** Überprüfen Sie die Rolle Ihres Gramps Web-Benutzerkontos: Nur Editoren, Eigentümer und Administratoren können Änderungen an der entfernten Datenbank anwenden.

### Hilfe anfordern

Wenn keine der oben genannten Maßnahmen hilft, fragen Sie die Community, indem Sie im [Gramps Web-Bereich des Gramps-Forums](https://gramps.discourse.group/c/gramps-web/28) posten. Bitte geben Sie an:

- die Version des Gramps Web Sync-Addons, die unten im Synchronisierungsfenster neben der Web-API-Version des Servers angezeigt wird (und verwenden Sie bitte die neueste veröffentlichte Version)
- die Version von Gramps Desktop, die Sie verwenden
- die Versionsinformationen von Gramps Web, die unter *Einstellungen ▸ Versionsinfo* zu finden sind
- alle Details zu Ihrer Gramps Web-Installation (selbst gehostet, Grampshub, ...)
- die Ausgabe Ihrer Gramps Web-Serverprotokolle, wenn Sie Zugriff darauf haben (bei Verwendung von Docker: `docker compose logs --tail 100 grampsweb` und `docker compose logs --tail 100 grampsweb-celery`)

Wenn Sie nach einem Debug-Protokoll gefragt werden, starten Sie Gramps [von der Kommandozeile](https://gramps-project.org/wiki/index.php/Gramps_5.2_Wiki_Manual_-_Command_Line) mit aktivierter Debug-Protokollierung und reproduzieren Sie das Problem:

```bash
gramps --debug grampswebsync
```

## Hintergrund: wie das Addon funktioniert

Das Addon soll eine lokale Gramps-Datenbank mit einer entfernten Gramps Web-Datenbank synchron halten, sodass sowohl lokale als auch entfernte Änderungen (kollaborative Bearbeitung) möglich sind.

Es ist **nicht geeignet**

- um mit einer Datenbank zu synchronisieren, die kein direkter Ableger (beginnend mit einer Datenbankkopie oder Gramps XML-Export/-Import) der lokalen Datenbank ist,
- um zwei Datenbanken mit einer großen Anzahl von Änderungen auf beiden Seiten zu fusionieren, die manuelle Aufmerksamkeit für die Zusammenführung erfordern. Verwenden Sie zu diesem Zweck das hervorragende [Import Merge Tool](https://www.gramps-project.org/wiki/index.php/Import_Merge_Tool).

Die Betriebsprinzipien sind einfach:

- Es vergleicht die lokalen und entfernten Datenbanken.
- Wenn es Unterschiede gibt, überprüft es den Zeitstempel des neuesten identischen Objekts, nennen wir es **t**.
- Wenn ein Objekt in einer Datenbank existiert, das nach **t** geändert wurde, aber in der anderen nicht, wird es in beide synchronisiert (nehmen wir an, neues Objekt).
- Wenn ein Objekt zuletzt vor **t** in einer Datenbank geändert wurde, aber in der anderen fehlt, wird es in beiden gelöscht (nehmen wir an, gelöschtes Objekt).
- Wenn ein Objekt unterschiedlich ist, aber nur in einer Datenbank nach **t** geändert wurde, wird es in die andere synchronisiert (nehmen wir an, modifiziertes Objekt).
- Wenn ein Objekt unterschiedlich ist, aber in beiden Datenbanken nach **t** geändert wurde, werden sie zusammengeführt (nehmen wir an, konfliktierende Änderung).

Die Zeit der letzten erfolgreichen Synchronisierung wird ebenfalls aufgezeichnet, separat für jeden Server, und als **t** verwendet, wenn sie aktueller ist als das neueste identische Objekt.

Dieser Algorithmus ist einfach und robust, da er keine Verfolgung der Synchronisierungshistorie erfordert. Er funktioniert jedoch am besten, wenn Sie *häufig synchronisieren*.
