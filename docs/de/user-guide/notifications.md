# Benachrichtigungen

**Benachrichtigungen** ist ein Sidebar-Element mit einem Glockensymbol. Wenn Fehler aufgetreten sind oder Hintergrundaufgaben ausgeführt werden, zeigt ein Badge die Anzahl der ungelesenen Benachrichtigungen an. Klicken Sie darauf, um das Benachrichtigungsprotokoll zu öffnen.

Das Benachrichtigungsprotokoll dient zwei Zwecken:

- Es ist ein Protokoll der Fehler, die während Ihrer Sitzung aufgetreten sind – fehlgeschlagene API-Anfragen, Fehler bei Hintergrundaufgaben, Speicherfehler oder Fehler auf Browser-Ebene.
- Es verfolgt den Fortschritt von lang laufenden Hintergrundaufgaben – wie Importe und Exporte, das Erstellen von Berichten, OCR-Texterkennung, Datenbank-Upgrades und das Wiederherstellen von Such-/semantischen Indizes – und zeigt deren Status (z. B. ausstehend, gestartet, in Bearbeitung) an und benachrichtigt Sie, wenn sie abgeschlossen oder fehlgeschlagen sind.

Jeder Eintrag zeigt eine kurze Nachricht, die Quelle (Netzwerk, Aufgabe, Speicherung oder Browser) und einen Zeitstempel. Abgeschlossene Aufgaben lesen sich als "Aufgabe abgeschlossen" oder "Aufgabe fehlgeschlagen".

Einige Benachrichtigungen enthalten strukturierte Details, wie die Fehlermeldung einer fehlgeschlagenen Aufgabe. Ein Klick auf einen solchen Eintrag öffnet einen Dialog mit einer Aufschlüsselung der Fehlermeldungsdaten und einem **JSON kopieren**-Button. Dies ist nützlich, wenn Sie einen Fehler melden, da das JSON die genauen Fehlermeldungen vom Server enthält.

Verwenden Sie **Alle löschen**, um alle Benachrichtigungen zu entfernen.

Aufgaben, die den gesamten Baum ändern, wie ein Import, eine Wiederherstellung, das Löschen aller Objekte oder das Wiederherstellen des Suchindex, können nicht gleichzeitig ausgeführt werden. Wenn Sie eine starten, während eine andere läuft, wird eine Nachricht angezeigt, dass bereits eine andere Aufgabe auf diesem Baum ausgeführt wird, und die laufende Aufgabe wird mit ihrem Fortschritt angezeigt.

!!! Hinweis
    Benachrichtigungen werden nur im Speicher gespeichert und werden gelöscht, wenn Sie die Seite neu laden.
