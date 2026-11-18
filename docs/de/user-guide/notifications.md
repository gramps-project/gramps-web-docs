# Benachrichtigungen

Die Glocke in der oberen App-Leiste öffnet die Benachrichtigungen. Ein Badge auf der Glocke zeigt die Anzahl der ungelesenen Benachrichtigungen an. Das Menü listet laufende Aufgaben und die neuesten Benachrichtigungen auf; **Alle anzeigen** öffnet das vollständige Benachrichtigungsprotokoll. Auf kleinen Bildschirmen öffnet die Glocke das Protokoll direkt.

Benachrichtigungen beziehen sich auf:

- **Änderungen durch andere Benutzer.** Wenn andere Benutzer den Baum ändern, während Sie Gramps Web verwenden, zeigt eine Benachrichtigung an, wer was geändert hat, z.B. "Person bearbeiten" oder "12 Änderungen". Klicken Sie darauf, um die Änderung im [Änderungsverlauf](revisions.md) zu öffnen. Änderungen, die keinen Gramps Web-Benutzer haben, wie Änderungen, die direkt an einer gemeinsamen Datenbank mit Gramps Desktop vorgenommen wurden, werden ohne Namen angezeigt. Dies ist nur für Benutzer verfügbar, die den Änderungsverlauf sehen können (Mitglieder und höher).
- **Hintergrundaufgaben** – wie Importe und Exporte, das Erstellen von Berichten, OCR-Texterkennung, Datenbank-Upgrades, das Löschen oder Bearbeiten vieler Objekte und das Wiederherstellen des Suchindex – die ihren Status anzeigen (z.B. ausstehend, gestartet, in Bearbeitung) und Sie benachrichtigen, wenn sie abgeschlossen sind oder fehlschlagen.
- **Fehler**, die während Ihrer Sitzung aufgetreten sind – fehlgeschlagene API-Anfragen, Fehler bei Hintergrundaufgaben, Speicherfehler oder Fehler auf Browser-Ebene.

Abgeschlossene Exporte und Medienarchive können über ihre Benachrichtigung heruntergeladen werden, auch nachdem Sie die [Exportseite](../administration/export.md) verlassen haben.

Einige Benachrichtigungen enthalten strukturierte Details, wie die Fehlermeldung einer fehlgeschlagenen Aufgabe. Das Klicken auf einen solchen Eintrag im Benachrichtigungsprotokoll öffnet einen Dialog mit einer Aufschlüsselung der Fehlermeldungsdaten und einem **JSON kopieren**-Button. Dies ist nützlich, wenn Sie einen Fehler melden, da das JSON die genauen Fehlermeldungen vom Server enthält.

Verwenden Sie **Alle löschen** im Benachrichtigungsprotokoll, um alle Benachrichtigungen zu verwerfen.

Aufgaben, die den gesamten Baum ändern, wie ein Import, eine Wiederherstellung, das Löschen aller Objekte oder das Wiederherstellen des Suchindex, können nicht gleichzeitig ausgeführt werden. Wenn Sie eine starten, während eine andere läuft, wird eine Nachricht angezeigt, dass bereits eine andere Aufgabe auf diesem Baum ausgeführt wird, und die laufende Aufgabe wird mit ihrem Fortschritt angezeigt.

!!! Hinweis
    Benachrichtigungen werden nur im Speicher gespeichert und werden gelöscht, wenn Sie die Seite neu laden. Gramps Web überprüft Änderungen durch andere Benutzer nur, während es geöffnet ist, sodass Änderungen, die während Ihrer Abwesenheit vorgenommen wurden, nicht gemeldet werden; siehe [Änderungsverlauf](revisions.md) für diese.
