# Karte

Die Karten-Seite zeigt alle Orte in Ihrem Stammbaum als interaktive Marker auf einer geografischen Karte an. Sie ist über die Seitenleiste zugänglich.

## Ortsmarker

Nur Orte, die GPS-Koordinaten in der Gramps-Datenbank gespeichert haben, werden auf der Karte angezeigt. Orte ohne Koordinaten werden stillschweigend weggelassen. GPS-Koordinaten können auf der Detailseite des Ortes festgelegt werden (bearbeiten Sie den Ort und füllen Sie die Felder für Breite und Länge aus).

!!! tip
    Wenn viele Ihrer Orte auf der Karte fehlen, öffnen Sie eine Detailseite eines Ortes und überprüfen Sie, ob Breite und Länge festgelegt sind. Sie können Koordinaten direkt aus der Bearbeitungsansicht des Ortes hinzufügen oder korrigieren.

Jeder Ort mit Koordinaten wird als Marker angezeigt. Ein Klick auf einen Marker öffnet eine Zusammenfassungskarte, die den Ortsnamen sowie die verknüpften Ereignisse und Personen anzeigt. Klicken Sie auf den Ortsnamen in der Karte, um die vollständige Detailseite des Ortes zu öffnen.

## Suche

Das Suchfeld in der oberen linken Ecke der Karte sucht während Sie tippen und gruppiert die Ergebnisse unter drei Überschriften:

- **Orte** – Orte in Ihrem Stammbaum. Die Auswahl eines Ortes zentriert die Karte auf diesen und hebt seinen Marker hervor.
- **Personen** – Personen in Ihrem Stammbaum. Die Auswahl einer Person wechselt die Karte in die Personenansicht, die [unten](#following-a-person-across-the-map) beschrieben wird.
- **Extern** – Standorte von [OpenStreetMap](https://www.openstreetmap.org/), für überall auf der Welt. Die Auswahl eines externen Standorts zentriert und zoomt die Karte auf diesen Standort; es filtert oder ändert nicht die Orte Ihres Stammbaums.

Die externen Ergebnisse sind auch nützlich, wenn Sie Koordinaten zu einem Ort hinzufügen: Sie können den Standort hier nachschlagen, um zu sehen, wo er sich befindet, bevor Sie seine Breite und Länge eingeben.

## Eine Person über die Karte verfolgen

Die Auswahl einer Person – aus dem Suchfeld der Karte oder mit der Schaltfläche **In Karte öffnen** auf der Detailseite einer Person – zeigt die Orte, die mit den Ereignissen dieser Person verbunden sind, verbunden durch Linien in chronologischer Reihenfolge. Kleine Pfeile entlang jeder Linie zeigen die Reisrichtung an, sodass Sie das Leben einer Person von der Geburt bis zum Tod über die Karte verfolgen können.

Orte auf einer Detailseite des Ortes haben ebenfalls eine Schaltfläche **In Karte öffnen**, die die Karte zentriert auf diesen Ort öffnet.

## Zeitregler

Der Zeitregler am unteren Rand der Seite filtert, welche Ortsmarker basierend auf dem Jahr ihrer zugehörigen Ereignisse angezeigt werden:

- Ziehen Sie den Griff, um ein Jahr auszuwählen.
- Nur Orte, die mit Ereignissen verknüpft sind, die innerhalb des ausgewählten Zeitfensters liegen, werden angezeigt.
- Verwenden Sie dies, um nachzuvollziehen, wo Ihre Vorfahren zu einem bestimmten Zeitpunkt in der Geschichte lebten.

## Kartenebenen

Ein Schalter für die Ebenen (gestapelte Ebenen-Ikone, unten links) ermöglicht es Ihnen, zwischen zwei Basis-Karten zu wählen:

### Basis-Karte

Die Standardebene, betrieben von [OpenFreeMap](https://openfreemap.org) (Liberty-Stil für den Hellmodus, Dunkelstil für den Dunkelmodus). Dies ist eine moderne, allgemeine Karte, die sich gut zur Lokalisierung von Orten eignet.

### Historische Karte

Wechselt die Basis-Karte zu [OpenHistoricalMap](https://www.openhistoricalmap.org) (OHM), einem gemeinschaftlich betriebenen Projekt, das die Welt so kartiert, wie sie zu verschiedenen Zeitpunkten existierte – denken Sie daran als historisches Pendant zu OpenStreetMap.

Wenn die Ebene der historischen Karte aktiv ist, filtert der Zeitregler auch die Kartenausschnitte selbst: OHM rendert die Karte so, wie sie im ausgewählten Jahr erschien, sodass historische Grenzen, Ortsnamen und Merkmale anstelle der modernen angezeigt werden. Dies ermöglicht es, sowohl den Standort Ihres Vorfahren als auch den zeitgenössischen geografischen und politischen Kontext in einer einzigen Ansicht zu sehen.

!!! note
    Die Abdeckung von OpenHistoricalMap variiert je nach Region und Zeitraum. Gebiete oder Epochen mit spärlichen Beiträgen können begrenzte historische Details zeigen. Wenn Sie fehlende oder ungenaue historische Daten bemerken, ziehen Sie in Betracht, [zu OpenHistoricalMap beizutragen](https://www.openhistoricalmap.org) – es ist ein offenes Gemeinschaftsprojekt, das jeder bearbeiten kann.

## Benutzerdefinierte Kartenüberlagerungen

Zusätzlich zu den integrierten Basisebenen können Sie jedes gescannte historische Kartenbild – das in Gramps als **Medien**-Objekt gespeichert ist – in eine benutzerdefinierte Überlagerung verwandeln, die auf der Live-Karte positioniert ist. Dies ist nützlich für Scans alter Stadtpläne, Pfarrkarten oder Grundstückskarten, die Sie direkt mit moderner oder historischer Geografie vergleichen möchten.

### Georeferenzierung eines Bildes

1. Öffnen Sie das Medienobjekt für das gescannte Kartenbild und wechseln Sie in den Bearbeitungsmodus.
2. Öffnen Sie die Registerkarte "Karte" und klicken Sie auf **Koordinaten bearbeiten**. Dies öffnet einen Georeferenzierungsdialog mit dem Bild neben einer Karte.
3. Klicken Sie auf **Wählen Sie einen Punkt auf der Karte**, und klicken Sie dann auf den Standort auf der Karte, dem ein Punkt im Bild entsprechen soll. Das Bild wird auf der Karte zum ersten Mal platziert, sobald ein Punkt ausgewählt ist.
4. Verwenden Sie den **Skalieren**-Regler, um das Bild zu ändern, und den **Opazität**-Regler, um die Basiskarte während der Positionierung durchzusehen.
5. Klicken Sie auf **Bild ausrichten** und klicken Sie erneut auf die Karte, um das Bild zu verschieben, sodass der angeheftete Punkt genau übereinstimmt.
6. Wiederholen Sie die Schritte für Skalierung, Opazität und Ausrichtung, bis das Bild mit der zugrunde liegenden Geografie übereinstimmt, und speichern Sie dann.

Im Hintergrund werden die Eckkoordinaten des Bildes in einem `map:bounds`-Attribut des Medienobjekts gespeichert.

### Anzeigen von Überlagerungen auf der Karten-Seite

Sobald ein Medienobjekt auf diese Weise georeferenziert wurde, wird es automatisch als umschaltbare Ebene auf der Karten-Seite verfügbar. Öffnen Sie den Ebenenschalter (gestapelte Ebenen-Ikone, unten links), um jede Überlagerung unabhängig von der Basiskarte ein- oder auszublenden. Überlagerungen werden nach dem Titel des Medienobjekts aufgelistet.
