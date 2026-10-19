Es gibt zwei Möglichkeiten, eine neue Mediendatei (ein Bild, eine Audiodatei, eine Videodatei oder eine andere Datei) hinzuzufügen, und vorhandene Mediendateien können beim Erstellen neuer Objekte verknüpft werden:

## Fügen Sie eine neue eigenständige Mediendatei hinzu

Um eine eigenständige Mediendatei hinzuzufügen, klicken Sie auf das +-Symbol in der oberen App-Leiste und wählen Sie "Medienobjekt".

Klicken Sie auf "Datei auswählen", um eine Datei von Ihrem Computer auszuwählen. Auf einem mobilen Gerät haben Sie die Möglichkeit, direkt ein Foto mit der Kamera Ihres Geräts aufzunehmen, wenn Sie diese Schaltfläche drücken.

Optional können Sie

- eine Beschreibung der Mediendatei unter "Titel" eingeben
- ein Datum eingeben
- die Mediendatei als privat festlegen (was sie nur für Benutzer mit ausreichenden Berechtigungen sichtbar macht)

Klicken Sie auf "Hinzufügen", um die Datei hochzuladen und das Medienobjekt zu erstellen.

## Fügen Sie eine neue Mediendatei hinzu und verknüpfen Sie sie mit einem anderen Objekt

Die folgenden Objekttypen in Gramps können mit Medienobjekten verknüpft werden: Personen, Familien, Ereignisse, Orte, Quellen und Zitationen.

In der Detailansicht eines beliebigen Objekts klicken Sie auf die blaue Schaltfläche "Bearbeiten" in der unteren rechten Ecke (wenn Sie sie nicht sehen, hat Ihr Benutzer keine Bearbeitungsberechtigungen). Klicken Sie auf die Registerkarte "Galerie" und klicken Sie auf die blaue +-Schaltfläche.

Ein Dialogfeld öffnet sich, das die gleichen Felder wie im vorherigen Abschnitt beschrieben anbietet. Klicken Sie auf "Speichern", um die Datei hochzuladen, ein neues Medienobjekt hinzuzufügen und es mit dem betrachteten Objekt zu verknüpfen.

## Verknüpfen Sie vorhandene Mediendateien beim Erstellen eines Objekts

Wenn Sie eine neue Person, Familie, ein Ereignis, einen Ort, eine Quelle oder eine Zitation erstellen, hat das Formular einen Abschnitt "Medien". Dort können Sie ein oder mehrere vorhandene Medienobjekte auswählen, die beim Speichern mit dem neuen Objekt verknüpft werden.

Wenn Sie eine Person zusammen mit ihren Geburts- und Sterbeereignissen erstellen, werden die ausgewählten Medienobjekte nur mit der Person verknüpft, nicht mit den Ereignissen.

## Texterkennung (OCR)

Wenn der Serveradministrator die OCR-Unterstützung aktiviert hat, erscheint unter dem Bild in der Detailansicht eines Medienobjekts eine Schaltfläche "Texterkennung".

Klicken Sie auf "Texterkennung", wählen Sie die Sprache des im Bild angezeigten Textes aus und klicken Sie dann auf "Ausführen". Das Bild wird mit [Tesseract OCR](https://github.com/tesseract-ocr/tesseract) verarbeitet und der erkannte Text wird darunter angezeigt.

Wenn Ihr Benutzer über Bearbeitungsberechtigungen verfügt, klicken Sie auf "Als Notiz speichern", um eine neue Notiz (vom Typ "Transkript") mit dem erkannten Text zu erstellen und sie mit dem Medienobjekt zu verknüpfen.

!!! tip
    Die OCR-Genauigkeit hängt stark von der Bildqualität und der ausgewählten Sprache ab. Wenn das Ergebnis falsch aussieht, versuchen Sie eine andere Sprache – zum Beispiel benötigen historische deutsche Dokumente oft die Fraktur-Variante anstelle von einfachem Deutsch.
