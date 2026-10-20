# Karte

Die Karten-Seite zeigt alle Orte in Ihrem Stammbaum als interaktive Marker auf einer geografischen Karte an. Sie ist über die Seitenleiste zugänglich.

## Ortsmarker

Nur Orte, die GPS-Koordinaten in der Gramps-Datenbank gespeichert haben, werden auf der Karte angezeigt. Orte ohne Koordinaten werden stillschweigend weggelassen. GPS-Koordinaten können auf der Detailseite des Ortes festgelegt werden (bearbeiten Sie den Ort und füllen Sie die Felder für Breiten- und Längengrad aus).

!!! tip
    Wenn viele Ihrer Orte auf der Karte fehlen, öffnen Sie eine Detailseite des Ortes und überprüfen Sie, ob Breiten- und Längengrad festgelegt sind. Sie können Koordinaten direkt aus der Bearbeitungsansicht des Ortes hinzufügen oder korrigieren.

Jeder Ort mit Koordinaten wird als Marker angezeigt. Ein Klick auf einen Marker öffnet eine Zusammenfassungs-Karte, die den Ortsnamen sowie die verknüpften Ereignisse und Personen anzeigt. Klicken Sie auf den Ortsnamen in der Karte, um die vollständige Detailseite des Ortes zu öffnen.

## Suche

Das Suchfeld in der oberen linken Ecke der Karte sucht, während Sie tippen, und gruppiert die Ergebnisse unter drei Überschriften:

- **Orte** – Orte in Ihrem Stammbaum. Die Auswahl eines Ortes zentriert die Karte auf diesen und hebt seinen Marker hervor.
- **Personen** – Personen in Ihrem Stammbaum. Die Auswahl einer Person wechselt die Karte in die Personenansicht, die [unten](#following-a-person-across-the-map) beschrieben ist.
- **Extern** – Standorte von [OpenStreetMap](https://www.openstreetmap.org/), für überall auf der Welt. Die Auswahl eines externen Standorts zoomt einfach auf diese Position; es filtert oder ändert nicht die Orte in Ihrem Stammbaum.

Die externen Ergebnisse sind auch nützlich, wenn Sie Koordinaten zu einem Ort hinzufügen: Sie können den Standort hier nachschlagen, um zu sehen, wo er sich befindet, bevor Sie seinen Breiten- und Längengrad eingeben.

## Eine Person über die Karte verfolgen

Die Auswahl einer Person – aus dem Suchfeld der Karte oder mit der Schaltfläche **In Karte öffnen** auf der Detailseite einer Person – zeigt die Orte, die mit den Ereignissen dieser Person verbunden sind, verbunden durch Linien in chronologischer Reihenfolge. Kleine Pfeile entlang jeder Linie zeigen die Reisrichtung an, sodass Sie das Leben einer Person von der Geburt bis zum Tod über die Karte verfolgen können.

Orte auf einer Detailseite des Ortes haben ebenfalls eine Schaltfläche **In Karte öffnen**, die die Karte auf diesen Ort zentriert.

## Zeitregler

Der Zeitregler am unteren Rand der Seite filtert, welche Ortsmarker basierend auf dem Jahr ihrer zugehörigen Ereignisse angezeigt werden:

- Ziehen Sie den Regler, um ein Jahr auszuwählen.
- Nur Orte, die mit Ereignissen verknüpft sind, die innerhalb des ausgewählten Zeitfensters liegen, werden angezeigt.
- Verwenden Sie dies, um nachzuvollziehen, wo Ihre Vorfahren zu einem bestimmten Zeitpunkt in der Geschichte lebten.

## Kartenebenen

Eine Schaltfläche zum Wechseln der Ebenen (gestapelte Ebenen-Ikone, unten links) ermöglicht es Ihnen, zwischen zwei Grundkarten zu wählen. Darunter listet sie Ihre eigenen Kartenebenen unter "Ihre Karten" (siehe [Benutzerdefinierte Kartenüberlagerungen](#custom-map-overlays) und [Karten-Dateien von Orten](#map-files-of-places)) sowie die [Wikidata-Gebäude](#wikidata-buildings)-Ebene unter "Extern", die jeweils ein- und ausgeschaltet werden kann.

Die Beschriftungen beider Grundkarten werden in der Sprache angezeigt, die Sie in Gramps Web ausgewählt haben, wobei die Kartendaten in dieser Sprache einen Namen haben, und in der lokalen Bezeichnung ansonsten.

### Grundkarte

Die Standardebene, betrieben von [OpenFreeMap](https://openfreemap.org) (Liberty-Stil für den hellen Modus, dunkler Stil für den dunklen Modus). Dies ist eine moderne, allgemeine Karte, die sich gut zur Lokalisierung von Orten eignet.

### Historische Karte

Wechselt die Grundkarte zu [OpenHistoricalMap](https://www.openhistoricalmap.org) (OHM), einem gemeinschaftlich betriebenen Projekt, das die Welt so kartiert, wie sie zu verschiedenen Zeitpunkten existierte – denken Sie daran als ein historisches Pendant zu OpenStreetMap.

Wenn die historische Kartenebene aktiv ist, filtert der Zeitregler auch die Kartenkacheln selbst: OHM rendert die Karte so, wie sie im ausgewählten Jahr erschien, sodass historische Grenzen, Ortsnamen und Merkmale angezeigt werden, anstelle der modernen. Dies ermöglicht es, sowohl den Standort Ihres Vorfahren als auch den zeitgenössischen geografischen und politischen Kontext in einer einzigen Ansicht zu sehen.

!!! note
    Die Abdeckung von OpenHistoricalMap variiert je nach Region und Zeitraum. Gebiete oder Epochen mit spärlichen Beiträgen können begrenzte historische Details zeigen. Wenn Sie fehlende oder ungenaue historische Daten bemerken, ziehen Sie in Betracht, [zu OpenHistoricalMap beizutragen](https://www.openhistoricalmap.org) – es ist ein offenes Gemeinschaftsprojekt, das jeder bearbeiten kann.

## Benutzerdefinierte Kartenüberlagerungen

Neben den integrierten Grundebenen können Sie jedes gescannte historische Kartenbild – das in Gramps als **Medien**-Objekt gespeichert ist – in eine benutzerdefinierte Überlagerung umwandeln, die auf der Live-Karte positioniert ist. Dies ist nützlich für Scans alter Stadtpläne, Pfarrkarten oder Grundstückskarten, die Sie direkt mit moderner oder historischer Geografie vergleichen möchten.

### Georeferenzierung eines Bildes

1. Öffnen Sie das Medienobjekt für das gescannte Kartenbild und wechseln Sie in den Bearbeitungsmodus.
2. Öffnen Sie die Registerkarte "Karte" und klicken Sie auf **Koordinaten bearbeiten**. Dies öffnet einen Georeferenzierungsdialog mit dem Bild neben einer Karte.
3. Klicken Sie auf **Wählen Sie einen Punkt auf der Karte**, und klicken Sie dann auf den Standort auf der Karte, der einem Punkt auf dem Bild entsprechen soll. Das Bild wird auf der Karte zum ersten Mal platziert, sobald ein Punkt ausgewählt ist.
4. Verwenden Sie den **Skalieren**-Regler, um das Bild zu ändern, und den **Transparenz**-Regler, um die Grundkarte während der Positionierung durchsehen zu können.
5. Klicken Sie auf **Bild ausrichten** und klicken Sie erneut auf die Karte, um das Bild so zu verschieben, dass der fixierte Punkt genau übereinstimmt.
6. Wiederholen Sie die Schritte für Skalierung, Transparenz und Ausrichtung, bis das Bild mit der zugrunde liegenden Geografie übereinstimmt, und speichern Sie es.

Im Hintergrund werden die Eckkoordinaten des Bildes in einem `map:bounds`-Attribut im Medienobjekt gespeichert.

### Anzeigen von Überlagerungen auf der Karten-Seite

Sobald ein Medienobjekt auf diese Weise georeferenziert wurde, steht es automatisch als umschaltbare Ebene auf der Karten-Seite zur Verfügung. Öffnen Sie den Ebenenwechsel (gestapelte Ebenen-Ikone, unten links), um jede Überlagerung unabhängig von der Grundkarte ein- oder auszublenden. Überlagerungen werden nach dem Titel des Medienobjekts aufgelistet.

## Karten-Dateien von Orten

Orte können Karten-Dateien als Medienobjekte angehängt haben – zum Beispiel die Grenzen einer Pfarrei, eines Stadtteils oder eines Anwesens oder eine Route. Unterstützt werden KML (`.kml`), GeoJSON (`.geojson`) und GPX (`.gpx`) Dateien.

Wenn Sie einen Ort auf der Karte auswählen, werden seine Karten-Dateien über der Karte gezeichnet, wobei die Farben verwendet werden, die in der Datei gespeichert sind, wo sie vorhanden sind. Dies funktioniert auch für Orte ohne Koordinaten: Die Karte zoomt dann auf das Gebiet, das von den Dateien abgedeckt wird. Während der Ort ausgewählt ist, werden seine Dateien im Ebenenwechsel unter "Ihre Karten" aufgelistet, wo Sie jede von ihnen ausschalten können.

Um eine Karten-Datei zu einem Ort hinzuzufügen, fügen Sie sie wie jede andere [Medien-Datei](media.md) zur Galerie des Ortes hinzu.

## Wikidata-Gebäude

Die "Wikidata-Gebäude"-Ebene zeigt Gebäude an, die in [Wikidata](https://www.wikidata.org/) erfasst sind, wie Kirchen, Höfe oder Stadthäuser. Sie ist standardmäßig deaktiviert und kann im Ebenenwechsel unter "Extern" aktiviert werden. Gebäude werden nur angezeigt, wenn die Karte weit genug hereingezoomt ist. Wenn der Zeitregler aktiv ist, werden nur Gebäude angezeigt, die zu dem ausgewählten Zeitpunkt existierten.

Klicken Sie auf ein Gebäude, um seine Details aus Wikidata zu sehen, wie z.B. wann es gebaut oder abgerissen wurde, seine Adressen, Bewohner und Eigentümer.

### Speichern eines Gebäudes als Ort

Benutzer, die Objekte hinzufügen können, sehen eine Schaltfläche **Als Ort speichern** in den Details des Gebäudes. Sie öffnet das Formular für einen neuen Ort, das mit dem Namen des Gebäudes in Ihrer Sprache, einem Ortstyp (`Hof` für Höfe, sonst `Gebäude`), seinen Koordinaten und einem Link zum Wikidata-Element vorausgefüllt ist. Vervollständigen Sie das Formular, indem Sie beispielsweise den umschließenden Ort auswählen, und speichern Sie es.

Wenn sich ein Ort in Ihrem Stammbaum am gleichen Standort wie das Gebäude befindet, lautet die Schaltfläche stattdessen **Gespeicherten Ort öffnen** und zeigt diesen Ort an.

!!! info
    Der Serveradministrator kann die Wikidata-Gebäude-Ebene mit der `mapWikidata`-Option der [Frontend-Konfiguration](../install_setup/frontend-config.md) entfernen.
