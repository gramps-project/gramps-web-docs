# Benachrichtigungen

Das Glockensymbol in der oberen App-Leiste öffnet die Benachrichtigungen. Ein Abzeichen an der Glocke zeigt die Anzahl der ungelesenen Benachrichtigungen an. Das Menü listet laufende Aufgaben und die neuesten Benachrichtigungen auf; **Alle anzeigen** öffnet das vollständige Benachrichtigungsprotokoll. Auf kleinen Bildschirmen öffnet die Glocke das Protokoll direkt.

Benachrichtigungen informieren über:

- **Änderungen durch andere Benutzer.** Wenn andere Benutzer den Stammbaum ändern, während du Gramps Web verwendest, informiert dich eine Benachrichtigung darüber, wer was geändert hat, z. B. „Person bearbeiten“ oder „12 Änderungen“. Klicke darauf, um die Änderung im [Änderungsverlauf](revisions.md) zu öffnen. Änderungen ohne Gramps-Web-Benutzer, z. B. Änderungen, die direkt an einer freigegebenen Datenbank mit Gramps Desktop vorgenommen wurden, werden ohne Namen angezeigt. Dies ist nur für Benutzer verfügbar, die den Änderungsverlauf sehen können (Mitglieder und höher).
- **Hintergrundaufgaben** – z. B. Importe und Exporte, das Erstellen von Berichten, OCR-Texterkennung, Datenbankaktualisierungen, das Löschen oder Bearbeiten vieler Objekte sowie die Neuerstellung von Suchindizes – zeigen ihren Status an (z. B. ausstehend, gestartet, in Bearbeitung) und benachrichtigen dich, wenn sie abgeschlossen sind oder fehlschlagen.
- **Fehler**, die während deiner Sitzung aufgetreten sind – fehlgeschlagene API-Anfragen, Fehler bei Hintergrundaufgaben, Fehler beim Speichern oder Fehler auf Browserebene.

Abgeschlossene Exporte und Medienarchive können über ihre Benachrichtigung heruntergeladen werden, auch nachdem du die [Exportseite](../administration/export.md) verlassen hast.

Einige Benachrichtigungen enthalten strukturierte Details, z. B. die Fehlermeldung einer fehlgeschlagenen Aufgabe. Wenn du auf einen solchen Eintrag im Benachrichtigungsprotokoll klickst, wird ein Dialog mit einer Aufschlüsselung der Fehlerdaten und einer Schaltfläche **JSON kopieren** geöffnet. Dies ist hilfreich, wenn du einen Fehler meldest, da das JSON die genauen Fehlerinformationen vom Server enthält.

Verwende **Alle löschen** im Benachrichtigungsprotokoll, um alle Benachrichtigungen zu verwerfen.

Aufgaben, die den gesamten Stammbaum ändern, z. B. ein Import, eine Wiederherstellung, das Löschen aller Objekte oder die Neuerstellung des Suchindex, können nicht gleichzeitig ausgeführt werden. Wenn du eine startest, während eine andere läuft, wird eine Meldung angezeigt, dass bereits eine andere Aufgabe für diesen Stammbaum ausgeführt wird; die laufende Aufgabe wird mit ihrem Fortschritt angezeigt.

!!! note
    Benachrichtigungen werden nur im Arbeitsspeicher gespeichert und beim Neuladen der Seite gelöscht. Gramps Web prüft nur auf Änderungen durch andere Benutzer, solange es geöffnet ist. Daher werden Änderungen, die während deiner Abwesenheit vorgenommen wurden, nicht gemeldet; siehe [Änderungsverlauf](revisions.md).
