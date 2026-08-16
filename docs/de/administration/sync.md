# Synchronisieren von Gramps Web und Gramps Desktop

*Gramps Web Sync* ist ein Addon für Gramps, das es ermöglicht, Ihre Gramps-Datenbank auf Ihrem Desktop-Computer mit Gramps Web zu synchronisieren, einschließlich Mediendateien.

!!! warning
    Wie bei jedem Synchronisierungstool sollten Sie dies nicht als Backup-Tool betrachten. Eine versehentliche Löschung auf einer Seite wird auf die andere Seite übertragen. Stellen Sie sicher, dass Sie regelmäßige Backups (im Gramps XML-Format) Ihres Stammbaums erstellen.

!!! info
    Die Dokumentation bezieht sich auf die neueste Version des Gramps Web Sync-Addons. Bitte verwenden Sie den Gramps-Addon-Manager, um das Addon bei Bedarf auf die neueste Version zu aktualisieren.

!!! note "Was sich in Version 1.5 geändert hat"
    Die Benutzeroberfläche des Addons wurde in Version 1.5 neu geschrieben. Der Schritt-für-Schritt-Assistent ist verschwunden und wurde durch ein einzelnes Fenster ersetzt. Mediendateien werden nun zusammen mit den Objektänderungen bestätigt, anstatt auf einer separaten Seite danach. Wenn Sie nach dem Synchronisierungsmodus-Selector suchen, befindet er sich jetzt **oberhalb** der Liste der Änderungen anstatt darunter. Der **Merge**-Synchronisierungsmodus wurde entfernt; siehe [Synchronisierungsmodus](#sync-mode) unten.

## Installation

Das Addon erfordert Gramps 6.0, das auf Python 3.10 oder neuer läuft. Es ist in Gramps Desktop verfügbar und kann [auf die übliche Weise](https://www.gramps-project.org/wiki/index.php/5.2_Addons#Installing_Addons_in_Gramps) installiert werden.

!!! warning
    Bitte stellen Sie sicher, dass Sie die gleiche Version von Gramps auf Ihrem Desktop verwenden wie die, die auf Ihrem Server läuft. Siehe den Abschnitt [Hilfe erhalten](../help/help.md), um herauszufinden, welche Gramps-Version Ihr Server verwendet. Die Gramps-Version hat die Form `MAJOR.MINOR.PATCH`, und `MAJOR` und `MINOR` müssen sowohl im Web als auch auf dem Desktop gleich sein.

### Serveranforderungen

Das Addon überprüft zwei Dinge über Ihren Server, sobald es sich verbindet, und weigert sich fortzufahren, wenn eines davon nicht erfüllt ist. Beide Überprüfungen erfolgen, bevor irgendetwas heruntergeladen wird.

- **Gramps Web API Version 3.x.** Diese Version des Addons, für Gramps 6.0, funktioniert mit Gramps Web API 3. Ein älterer Server muss aktualisiert werden; ein Server, der eine *neuere* API-Hauptversion ausführt, benötigt eine neuere Version von Gramps, nicht ein neueres Addon, da jede Gramps-Version mit einer API-Version gepaart ist. Sie finden die Version Ihres Servers unter *Einstellungen ▸ Versionsinfo* in Gramps Web.
- **Eine Hintergrundaufgabenwarteschlange.** Die Synchronisierung reicht ihre Änderungen als Hintergrundaufgabe ein. Auf einem Server ohne konfigurierte Aufgabenwarteschlange würde das Anwenden von Änderungen synchron ablaufen und bei einem echten Stammbaum zeitlich auslaufen, sodass das Addon sich weigert zu starten, anstatt während des Vorgangs zu scheitern.

Sie benötigen außerdem ein Konto mit mindestens Bearbeitungsrechten, um Änderungen an der entfernten Datenbank anzuwenden.

Optionaler Schritt:

??? note inline end "Gnome Keyring Bug"
    Derzeit gibt es einen [Bug im Python Keyring](https://github.com/jaraco/keyring/issues/496), der viele Gnome-Desktop-Konfigurationen betrifft. Sie müssen möglicherweise die Konfigurationsdatei `~/.config/python_keyring/keyringrc.cfg` erstellen und sie so bearbeiten:

        [backend]
        default-keyring=keyring.backends.SecretService.Keyring

- Installieren Sie `keyring` (z. B. `sudo apt install python3-keyring` oder `sudo dnf install python3-keyring`), um das sichere Speichern des API-Passworts im Passwortmanager Ihres Systems zu ermöglichen.

Wenn der Keyring nicht verwendet werden kann, sagt das Addon dies und fährt ohne ihn fort – Sie werden einfach jedes Mal nach Ihrem Passwort gefragt. Bei dem Gramps **Snap**-Paket wird der System-Keyring durch die Einschränkung blockiert, bis Sie die Schnittstelle einmal verbinden:

```bash
snap connect gramps:password-manager-service
```

Das Addon zeigt diesen genauen Befehl an, wenn es die Situation erkennt.

## Verwendung

Sobald es installiert ist, ist das Addon in Gramps unter *Werkzeuge ▸ Stammbaumverarbeitung ▸ Gramps&nbsp;Web&nbsp;Sync* verfügbar. Nach der Bestätigung des Dialogwarnhinweises, dass die Rückgängig-Historie verworfen wird, öffnet sich das Synchronisierungsfenster.

**Es werden keine Änderungen an Ihrem lokalen Baum oder am Server angewendet, bis Sie diese ausdrücklich bestätigen.**

Das Fenster hat einen Streifen oben, der den Stammbaum benennt, mit dem Sie synchronisieren, das Konto und die Adresse, zu der es gehört, und wann es zuletzt synchronisiert wurde. Unten werden die Version des Addons und der Web-API des Servers angezeigt – nützlich, wenn Sie ein Problem melden.

### Verbindung herstellen

Wenn Sie diesen Stammbaum zuvor synchronisiert haben und Ihr Passwort gespeichert ist, verbindet sich das Addon, sobald es geöffnet wird, und geht direkt zum Vergleichen über. Andernfalls fragt es nach der Basis-URL Ihrer Gramps Web-Instanz (Beispiel: `https://mygrampsweb.com/`), Ihrem Benutzernamen und Ihrem Passwort.

Die URL und der Benutzername werden im Klartext in Ihrem Gramps-Benutzerdirectory gespeichert. Das Passwort wird nur in Ihrem System-Passwortmanager gespeichert, wenn Sie **Passwort merken** aktiviert lassen; das Deaktivieren entfernt jedes Passwort, das bereits für diesen Server gespeichert ist.

!!! tip "Mehrere Stammäume, mehrere Server"
    Jeder Server, mit dem Sie synchronisieren, wird separat gespeichert, zusammen mit seinem eigenen Protokoll, wann er zuletzt synchronisiert wurde. Das Wechseln zwischen zwei Servern stört keinen von beiden mehr.

    Jeder Eintrag protokolliert auch **welchen lokalen Stammbaum** er zuletzt synchronisiert hat. Das Addon verbindet sich nur von selbst, wenn dies mit dem Baum übereinstimmt, den Sie geöffnet haben; andernfalls zeigt es die Verbindungsdetails an und wartet darauf, dass Sie auf *Verbinden* drücken, mit einer Warnung, wenn die gespeicherten Anmeldeinformationen zu einem anderen Baum gehören. Dies ist wichtig, da das Synchronisieren eines Baums gegen einen Server, der einen *anderen* Baum enthält, vorschlagen würde, den Inhalt beider zu löschen.

Es stehen zwei Aktionen zur Verfügung, während nichts geschrieben wird:

- **Server ändern…**, im oberen Streifen, kehrt zu den Verbindungsdetails zurück, damit Sie diesen Baum auf einen anderen Server verweisen können. Es unterbricht einen laufenden Vergleich, anstatt Sie warten zu lassen, bis er abgeschlossen ist.
- **Diesen Server vergessen**, im Verbindungsbereich, entfernt die gespeicherte Adresse, den Benutzernamen und das Passwort sowie den Protokolleintrag, wann dieser Baum zuletzt synchronisiert wurde. Die nächste Synchronisierung vergleicht dann die beiden Bäume von Grund auf neu.

Wenn Sie eine Adresse eingeben, die mit `http://` anstelle von `https://` beginnt, erscheint beim Tippen eine Warnung. Ihr Passwort würde im Klartext gesendet, verwenden Sie es daher nur für lokale Tests.

### Änderungen überprüfen

Das Addon vergleicht die lokalen und entfernten Datenbanken und zeigt an, was es vorschlägt zu tun. Im Gegensatz zu früheren Versionen, die die rohen Unterschiede zwischen den beiden Bäumen auflisteten, zeigt die Liste jetzt die **Aktionen** an, die durchgeführt werden, gruppiert nach welcher Datenbank sie geändert werden:

```
▾ Wird auf diesem Computer geändert (7 Objekte)
    ▾ 3 Objekte hinzufügen
        Person   John Smith        I0123
    ▾ 4 Objekte aktualisieren
        …
▾ Wird auf dem Server geändert (5 Objekte)
    …
```

Jede Zeile benennt das Objekt, sodass Sie erkennen können, wer oder was betroffen ist, anstatt nur eine Gramps-ID zu sehen.

Wenn etwas gelöscht werden soll, sagt eine Warnung über der Liste, wie viele Objekte betroffen sind und auf welcher Seite. Dies erscheint immer, wenn Löschungen beteiligt sind, einschließlich während einer gewöhnlichen bidirektionalen Synchronisierung, die eine Löschung propagiert, die Sie selbst vorgenommen haben.

Drücken Sie **Übernehmen**, um das auszuführen, was die Liste beschreibt.

!!! warning "Nicht bearbeiten während der Überprüfung"
    Das Synchronisierungsfenster blockiert den Rest von Gramps nicht, sodass Sie weiterarbeiten können, während die Liste geöffnet ist. Wenn Sie jedoch ein betroffenes Objekt bearbeiten, erkennt das Addon dies, wenn Sie auf Übernehmen drücken, stoppt ohne Änderungen vorzunehmen und bittet Sie, erneut zu vergleichen. Nichts geht verloren, aber der Vergleich muss wiederholt werden.

#### Synchronisierungsmodus

Der Synchronisierungsmodus wird **oberhalb** der Liste der Änderungen ausgewählt. Eine Änderung baut die Liste neu auf, da der Modus entscheidet, was jeder Unterschied tatsächlich wird.

- **Bidirektionale Synchronisierung** (Standard) – Änderungen von beiden Seiten werden kombiniert. Objekte, die an beiden Orten bearbeitet wurden, werden zusammengeführt.
- **Server zurücksetzen, um mit diesem Computer übereinzustimmen** – der Server wird so eingestellt, dass er mit diesem Computer übereinstimmt. Alles, was nur auf dem Server geändert wurde, wird verworfen.
- **Diesen Computer zurücksetzen, um mit dem Server übereinzustimmen** – dieser Computer wird so eingestellt, dass er mit dem Server übereinstimmt. Alles, was nur hier geändert wurde, wird verworfen.

!!! note
    Der in früheren Versionen verfügbare **Merge**-Modus wurde entfernt. Er unterschied sich von der bidirektionalen Synchronisierung nur darin, dass Objekte, die auf einer Seite gelöscht wurden, wiederhergestellt wurden, anstatt die Löschung zu propagieren, was eine Unterscheidung war, die die Benutzeroberfläche nicht sinnvoll erklären konnte. Wenn Sie darauf angewiesen waren, verwenden Sie die bidirektionale Synchronisierung und stellen Sie alles wieder her, was Sie aus einem Backup behalten möchten.

### Mediendateien

Mediendateien werden als Teil derselben Bestätigung behandelt, nicht als separater Schritt. Wenn Dateien übertragen werden müssen, bietet ein Kontrollkästchen unter der Liste an, sie zu verschieben:

```
[x] Auch 12 Mediendateien übertragen (4 zum Herunterladen, 8 zum Hochladen)
```

Deaktivieren Sie es, um die Objektänderungen zu synchronisieren, ohne die Dateien zu berühren.

Dateien, die auf *beiden* Seiten fehlen, werden separat aufgelistet, da nichts mit ihnen getan werden kann:

```
2 Mediendateien fehlen auf beiden Seiten und können nicht übertragen werden.
```

Beachten Sie die folgenden Einschränkungen der Mediendatei-Synchronisierung:

- Wenn eine lokale Datei eine andere Prüfziffer hat als die, die in der Gramps-Datenbank gespeichert ist (dies kann z. B. bei Word-Dateien passieren, die nach dem Hinzufügen zu Gramps bearbeitet wurden), schlägt der Upload mit einer Fehlermeldung fehl.
- Das Tool überprüft nicht die Integrität aller lokalen Dateien, sodass, wenn eine lokale Datei unter dem Pfad existiert, der für das Medienobjekt gespeichert ist, die Datei jedoch von der Datei auf dem Server abweicht, das Tool dies nicht erkennt. Verwenden Sie das Media Verify Addon, um Dateien mit falschen Prüfziffern zu erkennen.

### Wenn etwas schiefgeht

Wenn eine Synchronisierung teilweise fehlschlägt – z. B. aufgrund einer unterbrochenen Verbindung – berichtet das Addon, was es bereits angewendet hat, und bietet **Erneut versuchen** an, was an dem Schritt fortsetzt, der fehlgeschlagen ist, anstatt von vorne zu beginnen. Die heruntergeladene Kopie des entfernten Baums wird aufbewahrt, sodass ein erneuter Versuch nicht erneut heruntergeladen und verglichen wird.

Technische Details des Fehlers sind hinter einem *Details*-Erweiterer verfügbar, mit einer Schaltfläche, um sie für einen Bug-Report zu kopieren.

## Fehlersuche

### Debug-Protokollierung

Wenn Sie Probleme mit dem Sync-Addon haben, starten Sie Gramps bitte mit aktivierter Debug-Protokollierung, indem Sie [Gramps von der Kommandozeile aus starten](https://gramps-project.org/wiki/index.php/Gramps_5.2_Wiki_Manual_-_Command_Line) mit der folgenden Option:

```bash
gramps --debug grampswebsync
```

Dies wird viele hilfreiche Protokollierungsanweisungen in die Kommandozeile drucken, die Ihnen helfen, die Ursache des Problems zu identifizieren.

### Serveranmeldeinformationen

Wenn die Verbindung fehlschlägt, überprüfen Sie bitte die Server-URL, Ihren Benutzernamen und Ihr Passwort.

### Das Addon weigert sich zu verbinden

Wenn das Addon meldet, dass die Gramps Web API-Version des Servers zu alt oder zu neu ist oder dass keine Hintergrundaufgabenwarteschlange konfiguriert ist, siehe [Serveranforderungen](#serveranforderungen) oben. Diese werden überprüft, bevor etwas anderes geschieht, sodass die Nachricht das Problem direkt benennt.

### Berechtigungsprobleme

Wenn Sie auf einen Fehler stoßen, der Berechtigungen betrifft, überprüfen Sie bitte die Benutzerrolle Ihres Gramps Web-Benutzerkontos. Sie können nur Änderungen an der entfernten Datenbank anwenden, wenn Sie ein Benutzer mit der Rolle Bearbeiter, Eigentümer oder Administrator sind.

### Unerwartete Datenbankänderungen

Wenn das Synchronisierungstool Änderungen erkennt, von denen Sie glauben, dass sie nicht stattgefunden haben, könnte es sein, dass es Inkonsistenzen in einer der Datenbanken gibt, die Gramps dazu bringen, einen Unterschied zu erkennen, oder dass die Zeit zwischen Ihrem lokalen Computer und Ihrem Server nicht synchronisiert ist.

Bitte überprüfen Sie, ob die Uhren auf beiden Maschinen korrekt eingestellt sind (beachten Sie, die Zeitzone spielt keine Rolle, da das Tool Unix-Zeitstempel verwendet, die zeitzonenunabhängig sind).

Sie können auch das Überprüfungs- und Reparaturtool auf Ihrer lokalen Datenbank ausführen und sehen, ob dies hilft.

Eine brutale, aber effektive Methode, um sicherzustellen, dass Inkonsistenzen in Ihrer lokalen Datenbank keine falschen Positiven verursachen, besteht darin, Ihre Datenbank in Gramps XML zu exportieren und in eine neue, leere Datenbank zu importieren. Dies ist ein verlustfreier Vorgang, stellt jedoch sicher, dass alle Daten konsistent importiert werden.

!!! tip
    Wenn das Addon eine alarmierende Anzahl von Löschungen vorschlägt, überprüfen Sie zuerst den oberen Streifen: Er benennt den Stammbaum auf dem Server, in den Sie schreiben möchten. Das Synchronisieren gegen einen Server, der einen *anderen* Baum enthält, produziert genau dieses Symptom.

### Timeout-Fehler

Die Synchronisierung mit dem Server wird von einem Hintergrundarbeiter verarbeitet, sodass lang laufende Synchronisierungen nicht zeitlich auslaufen sollten. Ein Server ohne konfigurierte Aufgabenwarteschlange wird aus diesem Grund bei der Verbindungsherstellung abgelehnt – siehe [Serveranforderungen](#serveranforderungen).

Anfragen des Addons an den Server laufen nach 60 Sekunden ohne Antwort ab, sodass ein unerreichbarer Server einen Verbindungsfehler meldet, anstatt unendlich zu hängen.

### Unerwartete Fehler bei Mediendateien

Wenn das Hochladen einer Mediendatei fehlschlägt, liegt dies oft an einer Abweichung in der Prüfziffer der tatsächlichen Datei auf der Festplatte und der Prüfziffer in der lokalen Gramps-Datenbank. Dies geschieht häufig mit bearbeitbaren Dateien, wie z. B. Bürodokumenten, die außerhalb von Gramps bearbeitet wurden. Bitte verwenden Sie das Gramps Media Verify Addon, um die Prüfziffern aller Mediendateien zu korrigieren.

### Hilfe anfordern

Wenn all dies nicht hilft, können Sie die Community um Hilfe bitten, indem Sie im [Gramps Web-Bereich des Gramps-Forums](https://gramps.discourse.group/c/gramps-web/28) posten. Bitte stellen Sie sicher, dass Sie Folgendes angeben:

- die Version des Gramps Web Sync-Addons (und verwenden Sie bitte die neueste veröffentlichte Version) – sie wird am Ende des Synchronisierungsfensters angezeigt, neben der Web-API-Version des Servers
- die Version von Gramps Desktop, die Sie verwenden
- die Ausgabe der Gramps-Debug-Protokollierung, die wie oben beschrieben aktiviert wurde
- die Versionsinfo von Gramps Web (Sie finden sie unter Einstellungen/Versionsinfo)
- alle Details, die Sie zu Ihrer Gramps Web-Installation bereitstellen können (selbst gehostet, Grampshub, ...)
- die Ausgabe Ihrer Gramps Web-Serverprotokolle, wenn Sie Zugriff darauf haben (bei Verwendung von Docker: `docker compose logs --tail 100 grampsweb` und `docker compose logs --tail 100 grampsweb-celery`)

## Hintergrund: wie das Addon funktioniert

Wenn Sie neugierig sind, wie das Addon tatsächlich funktioniert, finden Sie in diesem Abschnitt einige weitere Details.

Das Addon soll eine lokale Gramps-Datenbank mit einer entfernten Gramps Web-Datenbank synchron halten, um sowohl lokale als auch entfernte Änderungen zu ermöglichen (kollaborative Bearbeitung).

Es ist **nicht geeignet**

- Um mit einer Datenbank zu synchronisieren, die nicht direkt abgeleitet ist (beginnend mit einer Datenbankkopie oder Gramps XML-Export/Import) von der lokalen Datenbank
- Um zwei Datenbanken mit einer großen Anzahl von Änderungen auf beiden Seiten zu verschmelzen, die manuelle Aufmerksamkeit für das Zusammenführen benötigen. Verwenden Sie zu diesem Zweck das hervorragende [Import Merge Tool](https://www.gramps-project.org/wiki/index.php/Import_Merge_Tool).

Die Betriebsprinzipien des Tools sind sehr einfach:

- Es vergleicht die lokalen und entfernten Datenbanken
- Wenn es Unterschiede gibt, überprüft es den Zeitstempel des letzten identischen Objekts, nennen wir es **t**
- Wenn ein Objekt in einer Datenbank existiert, das nach **t** geändert wurde, aber nicht in der anderen, wird es in beide synchronisiert (nehmen wir an, neues Objekt)
- Wenn ein Objekt das letzte Mal vor **t** geändert wurde und in einer Datenbank fehlt, wird es in beiden gelöscht (nehmen wir an, gelöschtes Objekt)
- Wenn ein Objekt unterschiedlich ist, aber nach **t** nur in einer Datenbank geändert wurde, wird es in die andere synchronisiert (nehmen wir an, modifiziertes Objekt)
- Wenn ein Objekt unterschiedlich ist, aber nach **t** in beiden Datenbanken geändert wurde, werden sie zusammengeführt (nehmen wir an, widersprüchliche Änderung)

Die Zeit der letzten erfolgreichen Synchronisierung wird ebenfalls aufgezeichnet, separat für jeden Server, und als **t** verwendet, wenn sie aktueller ist als das neueste identische Objekt.

Dieser Algorithmus ist einfach und robust, da er keine Verfolgung der Synchronisierungshistorie erfordert. Er funktioniert jedoch am besten, wenn Sie *häufig synchronisieren*.
