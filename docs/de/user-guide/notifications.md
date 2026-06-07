# Benachrichtigungen

**Benachrichtigungen** ist ein Sidebar-Element mit einem Glockensymbol. Wenn Fehler aufgetreten sind oder Hintergrundaufgaben ausgeführt werden, zeigt ein Badge die Anzahl der ungelesenen Benachrichtigungen an. Klicken Sie darauf, um das Benachrichtigungsprotokoll zu öffnen.

Das Benachrichtigungsprotokoll dient zwei Zwecken:

- Es ist ein Protokoll von Fehlern, die während Ihrer Sitzung aufgetreten sind – fehlgeschlagene API-Anfragen, Fehler bei Hintergrundaufgaben, Speicherfehler oder Fehler auf Browser-Ebene.
- Es verfolgt den Fortschritt von lang laufenden Hintergrundaufgaben – wie Importe und Exporte, das Erstellen von Berichten, OCR-Texterkennung, Datenbank-Upgrades und den Wiederaufbau von Such-/semantischen Indizes – und zeigt deren Zustand (z. B. ausstehend, gestartet, in Bearbeitung) an und benachrichtigt Sie, wenn sie abgeschlossen oder fehlgeschlagen sind.

Jeder Eintrag zeigt eine kurze Nachricht, die Quelle (Netzwerk, Aufgabe, Speicherung oder Browser) und einen Zeitstempel.

Einige Benachrichtigungen enthalten strukturierte Details. Ein Klick auf einen solchen Eintrag öffnet einen Dialog mit einer Aufschlüsselung der Fehlermeldungen und einem **JSON kopieren**-Button. Dies ist nützlich, wenn Sie einen Fehler melden, da das JSON die genauen Fehlermeldungen vom Server enthält.

Verwenden Sie **Alle löschen**, um alle Benachrichtigungen zu entfernen.

!!! Hinweis
    Benachrichtigungen werden nur im Speicher gespeichert und werden gelöscht, wenn Sie die Seite neu laden.
