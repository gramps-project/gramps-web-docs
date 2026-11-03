Es gibt zwei Möglichkeiten, eine neue Mediendatei (ein Bild, eine Audiodatei, eine Videodatei oder eine andere Datei) hinzuzufügen, und vorhandene Mediendateien können beim Erstellen neuer Objekte verknüpft werden:

## Fügen Sie eine neue eigenständige Mediendatei hinzu

Um eine eigenständige Mediendatei hinzuzufügen, klicken Sie auf das +-Symbol in der oberen App-Leiste und wählen Sie "Medienobjekt".

Klicken Sie auf "Datei auswählen", um eine Datei von Ihrem Computer auszuwählen. Auf einem mobilen Gerät haben Sie die Möglichkeit, direkt ein Foto mit der Kamera Ihres Geräts aufzunehmen, wenn Sie diese Schaltfläche drücken.

Optional können Sie:

- eine Beschreibung der Mediendatei unter "Titel" eingeben
- ein Datum eingeben
- die Mediendatei als privat festlegen (was sie nur für Benutzer mit ausreichenden Berechtigungen sichtbar macht)

Klicken Sie auf "Hinzufügen", um die Datei hochzuladen und das Medienobjekt zu erstellen.

## Fügen Sie eine neue Mediendatei hinzu und verknüpfen Sie sie mit einem anderen Objekt

Die folgenden Objekttypen in Gramps können mit Medienobjekten verbunden werden: Personen, Familien, Ereignisse, Orte, Quellen und Zitationen.

In der Detailansicht eines beliebigen Objekts klicken Sie auf die blaue Schaltfläche "Bearbeiten" in der unteren rechten Ecke (wenn Sie sie nicht sehen, hat Ihr Benutzer keine Bearbeitungsberechtigungen). Klicken Sie auf die Registerkarte "Galerie" und klicken Sie auf die blaue +-Schaltfläche.

Ein Dialogfeld öffnet sich, das die gleichen Felder wie im vorherigen Abschnitt beschrieben anbietet. Klicken Sie auf "Speichern", um die Datei hochzuladen, ein neues Medienobjekt hinzuzufügen und es mit dem angezeigten Objekt zu verknüpfen.

## Profilbilder

Das erste Bild in der Galerie einer Person wird als Profilbild verwendet. Im Bearbeitungsmodus ist es mit einem "Profilbild"-Abzeichen gekennzeichnet. Um ein anderes Bild zu verwenden, verschieben Sie es mit den Pfeiltasten auf den ersten Platz in den Miniaturansichten der Galerie.

Wenn eine Person noch keine Medien hat, zeigt der Bearbeitungsmodus stattdessen einen **Profilbild hinzufügen** Platzhalter an. Klicken Sie darauf, um eine neue Mediendatei hochzuladen oder eine vorhandene auszuwählen.

## Verknüpfen Sie vorhandene Mediendateien beim Erstellen eines Objekts

Wenn Sie eine neue Person, Familie, Ereignis, Ort, Quelle oder Zitation erstellen, enthält das Formular einen Abschnitt "Medien". Dort können Sie ein oder mehrere vorhandene Medienobjekte auswählen, die beim Speichern mit dem neuen Objekt verknüpft werden.

Wenn Sie eine Person zusammen mit ihren Geburts- und Sterbeereignissen erstellen, sind die ausgewählten Medienobjekte nur mit der Person verknüpft, nicht mit den Ereignissen.

## Medien durchsuchen

Die Medienansicht zeigt die Medienobjekte als Galerie von Miniaturansichten oder als Liste; die Wahl wird in Ihrem Browser gespeichert. Wie die anderen [Listenansichten](lists.md) kann sie sortiert (einschließlich nach Datum), gefiltert und verwendet werden, um Medien in großen Mengen auszuwählen und zu löschen.

Ein Klick auf ein Feld in der Galerie öffnet das Medium im Lightbox. Verwenden Sie die Pfeiltasten, wischen Sie oder klicken Sie auf die Pfeiltasten, um durch die gefilterten und sortierten Ergebnisse über Seiten hinweg zu blättern. Die Schaltfläche **Details** in der Lightbox öffnet die Seite des Medienobjekts. Ein Klick auf eine Zeile im Listenlayout öffnet die Seite des Medienobjekts direkt.

Videos werden mit einer Miniaturansicht und einer Wiedergabetaste angezeigt. Audio- und Videodateien können auf der Seite des Medienobjekts, in der Lightbox, in [Blogbeiträgen](blog.md) und beim Einbetten in Notizen abgespielt werden.

## Texterkennung (OCR)

Wenn der Serveradministrator die OCR-Unterstützung aktiviert hat, erscheint unter dem Bild in der Detailansicht eines Medienobjekts eine Schaltfläche "Texterkennung".

Klicken Sie auf "Texterkennung", wählen Sie die Sprache des im Bild angezeigten Textes aus und klicken Sie dann auf "Ausführen". Das Bild wird mit [Tesseract OCR](https://github.com/tesseract-ocr/tesseract) verarbeitet und der erkannte Text wird darunter angezeigt.

Wenn Ihr Benutzer über Bearbeitungsberechtigungen verfügt, klicken Sie auf "Als Notiz speichern", um eine neue Notiz (vom Typ "Transkript") mit dem erkannten Text zu erstellen und sie mit dem Medienobjekt zu verknüpfen.

!!! tip
    Die Genauigkeit der OCR hängt stark von der Bildqualität und der ausgewählten Sprache ab. Wenn das Ergebnis falsch aussieht, versuchen Sie eine andere Sprache – zum Beispiel benötigen historische deutsche Dokumente oft die Fraktur-Variante anstelle von normalem Deutsch.
