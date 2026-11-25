Es gibt zwei Möglichkeiten, eine neue Mediendatei (ein Bild, eine Audiodatei, ein Video oder eine andere Datei) hinzuzufügen. Außerdem können vorhandene Mediendateien beim Erstellen mit neuen Objekten verknüpft werden:

## Eine neue eigenständige Mediendatei hinzufügen

Um eine eigenständige Mediendatei hinzuzufügen, klicke in der oberen App-Leiste auf das Symbol + und wähle „Medienobjekt“ aus.

Klicke auf „Datei auswählen“, um eine Datei von deinem Computer auszuwählen. Auf einem Mobilgerät kannst du über diese Schaltfläche direkt ein Foto mit der Kamera deines Geräts aufnehmen.

Optional kannst du

- unter „Titel“ eine Beschreibung der Mediendatei eingeben
- ein Datum eingeben
- die Mediendatei als privat festlegen (dadurch ist sie nur für Benutzer mit ausreichender Berechtigung sichtbar)

Klicke auf „Hinzufügen“, um die Datei hochzuladen und das Medienobjekt zu erstellen.

## Eine neue Mediendatei hinzufügen und mit einem anderen Objekt verknüpfen

Die folgenden Objekttypen in Gramps können mit Medienobjekten verknüpft werden: Personen, Familien, Ereignisse, Orte, Quellen und Zitate.

Klicke in der Detailansicht eines beliebigen Objekts unten rechts auf die blaue Bearbeitungsschaltfläche (wenn du sie nicht siehst, hast du keine Bearbeitungsberechtigung). Klicke auf die Registerkarte „Galerie“ und anschließend auf die blaue Schaltfläche +.

Es wird ein Dialog geöffnet, der dieselben Felder wie im vorherigen Abschnitt enthält. Klicke auf „Speichern“, um die Datei hochzuladen, ein neues Medienobjekt hinzuzufügen und es mit dem angezeigten Objekt zu verknüpfen.

## Profilbilder

Das erste Bild in der Galerie einer Person wird als Profilbild verwendet. Im Bearbeitungsmodus ist es mit dem Hinweis „Profilbild“ gekennzeichnet. Um ein anderes Bild zu verwenden, verschiebe es mit den Pfeilschaltflächen auf den Miniaturansichten der Galerie an die erste Position oder ziehe es dorthin: Drücke mit der Maus auf die Miniaturansicht und verschiebe sie; auf einem Touchscreen drücke sie und halte sie gedrückt, bis sie aufgenommen wurde.
Wenn eine Person noch keine Medien hat, zeigt der Bearbeitungsmodus stattdessen den Platzhalter **Profilbild hinzufügen** an. Klicke darauf, um eine neue Mediendatei hochzuladen oder eine vorhandene auszuwählen.

## Vorhandene Mediendateien beim Erstellen eines Objekts verknüpfen

Wenn du eine neue Person, Familie, ein neues Ereignis, einen neuen Ort, eine neue Quelle oder ein neues Zitat erstellst, enthält das Formular einen Abschnitt „Medien“. Dort kannst du ein oder mehrere vorhandene Medienobjekte auswählen, die beim Speichern mit dem neuen Objekt verknüpft werden.

Wenn du eine Person zusammen mit ihren Geburts- und Sterbeereignissen erstellst, werden die ausgewählten Medienobjekte nur mit der Person, nicht mit den Ereignissen verknüpft.

## Medien durchsuchen

Die Medienansicht zeigt die Medienobjekte als Galerie von Miniaturansichten oder als Liste an. Die Auswahl wird in deinem Browser gespeichert. Wie die anderen [Listenansichten](lists.md) kann sie sortiert (auch nach Datum) und gefiltert werden. Außerdem kannst du Medien auswählen und gesammelt löschen.

Wenn du in der Galerie auf eine Kachel klickst, werden die Medien in der Lightbox geöffnet. Verwende die Pfeiltasten, wische oder klicke auf die Pfeilschaltflächen, um durch die gefilterten und sortierten Ergebnisse über mehrere Seiten hinweg zu blättern. Die Schaltfläche **Details** in der Lightbox öffnet die Seite des Medienobjekts. Wenn du in der Listenansicht auf eine Zeile klickst, wird die Seite des Medienobjekts direkt geöffnet.

Videos werden mit einer Miniaturansicht und einer Wiedergabeschaltfläche angezeigt. Audio- und Videodateien können auf der Seite des Medienobjekts, in der Lightbox, in [Blogbeiträgen](blog.md) und beim Einbetten in Notizen abgespielt werden.

## Texterkennung (OCR)

Wenn der Serveradministrator die OCR-Unterstützung aktiviert hat, wird unter dem Bild in der Detailansicht eines Medienobjekts die Schaltfläche „Texterkennung“ angezeigt.

Klicke auf „Texterkennung“, wähle die Sprache des im Bild angezeigten Textes aus und klicke anschließend auf „Ausführen“. Das Bild wird mit [Tesseract OCR](https://github.com/tesseract-ocr/tesseract) verarbeitet und der erkannte Text darunter angezeigt.

Wenn du über Bearbeitungsberechtigungen verfügst, klicke auf „Als Notiz speichern“, um eine neue Notiz (vom Typ „Transkript“) mit dem erkannten Text zu erstellen und sie mit dem Medienobjekt zu verknüpfen.

!!! tip
    Die Genauigkeit der OCR hängt stark von der Bildqualität und der ausgewählten Sprache ab. Wenn das Ergebnis falsch aussieht, versuche es mit einer anderen Sprache – bei historischen deutschen Dokumenten ist beispielsweise häufig die Frakturvariante statt einfachem Deutsch erforderlich.
