# Karte

Die Karten-Seite zeigt alle Orte in Ihrem Stammbaum als interaktive Marker auf einer geografischen Karte an. Sie ist über die Seitenleiste zugänglich.

## Ort Marker

Nur Orte, die GPS-Koordinaten in der Gramps-Datenbank gespeichert haben, werden auf der Karte angezeigt. Orte ohne Koordinaten werden stillschweigend weggelassen. GPS-Koordinaten können auf der Detailseite des Ortes festgelegt werden (bearbeiten Sie den Ort und füllen Sie die Felder für Breite und Länge aus).

!!! tip
    Wenn viele Ihrer Orte auf der Karte fehlen, öffnen Sie eine Detailseite des Ortes und überprüfen Sie, ob Breite und Länge festgelegt sind. Sie können Koordinaten direkt aus der Bearbeitungsansicht des Ortes hinzufügen oder korrigieren.

Jeder Ort mit Koordinaten wird als Marker angezeigt. Ein Klick auf einen Marker öffnet eine Zusammenfassungs-Karte, die den Ortsnamen sowie die verknüpften Ereignisse und Personen anzeigt. Klicken Sie auf den Ortsnamen in der Karte, um die vollständige Detailseite des Ortes zu öffnen.

## Suche

Das Suchfeld in der oberen linken Ecke der Karte ermöglicht es Ihnen, zu jedem Ort der Welt nach Namen zu springen. Dies filtert nicht die Orte im Stammbaum – es schwenkt und zoomt einfach die Karte auf den gesuchten Ort.

## Zeitregler

Der Zeitregler am unteren Rand der Seite filtert, welche Ort Marker basierend auf dem Jahr ihrer zugehörigen Ereignisse angezeigt werden:

- Ziehen Sie den Griff, um ein Jahr auszuwählen.
- Nur Orte, die mit Ereignissen verknüpft sind, die innerhalb des ausgewählten Zeitfensters liegen, werden angezeigt.
- Nutzen Sie dies, um nachzuvollziehen, wo Ihre Vorfahren zu einem bestimmten Zeitpunkt in der Geschichte lebten.

## Kartenebenen

Ein Schalter für die Ebenen (gestapelte Ebenen-Ikone, unten links) ermöglicht es Ihnen, zwischen zwei Basiskarten zu wählen:

### Basiskarte

Die Standardebene, betrieben von [OpenFreeMap](https://openfreemap.org) (Liberty-Stil für den Hellmodus, Dunkelstil für den Dunkelmodus). Dies ist eine moderne, allgemeine Karte, die sich gut zur Lokalisierung von Orten eignet.

### Historische Karte

Wechselt die Basiskarte zu [OpenHistoricalMap](https://www.openhistoricalmap.org) (OHM), einem gemeinschaftlich betriebenen Projekt, das die Welt so kartiert, wie sie zu verschiedenen Zeitpunkten existierte – denken Sie daran als ein historisches Pendant zu OpenStreetMap.

Wenn die Ebene der historischen Karte aktiv ist, filtert der Zeitregler auch die Kartenteile selbst: OHM rendert die Karte so, wie sie im ausgewählten Jahr erschien, sodass historische Grenzen, Ortsnamen und Merkmale anstelle der modernen angezeigt werden. Dies ermöglicht es, sowohl den Standort Ihrer Vorfahren als auch den zeitgenössischen geografischen und politischen Kontext in einer einzigen Ansicht zu sehen.

!!! note
    Die Abdeckung von OpenHistoricalMap variiert je nach Region und Zeitraum. Gebiete oder Epochen mit spärlichen Beiträgen können begrenzte historische Details zeigen. Wenn Sie fehlende oder ungenaue historische Daten bemerken, ziehen Sie in Betracht, [zu OpenHistoricalMap beizutragen](https://www.openhistoricalmap.org) – es ist ein offenes Gemeinschaftsprojekt, das jeder bearbeiten kann.

## Benutzerdefinierte Kartenüberlagerungen

Zusätzlich zu den integrierten Basisebenen können Sie jedes gescannte historische Kartenbild – das in Gramps als **Medien**-Objekt gespeichert ist – in eine benutzerdefinierte Überlagerung umwandeln, die auf der Live-Karte positioniert wird. Dies ist nützlich für Scans alter Stadtpläne, Pfarrkarten oder Grundstückskarten, die Sie direkt mit moderner oder historischer Geografie vergleichen möchten.

### Georeferenzierung eines Bildes

1. Öffnen Sie das Medienobjekt für das gescannte Kartenbild und wechseln Sie in den Bearbeitungsmodus.
2. Öffnen Sie die Registerkarte "Karte" und klicken Sie auf **Koordinaten bearbeiten**. Dies öffnet einen Georeferenzierungsdialog mit dem Bild neben einer Karte.
3. Klicken Sie auf **Wählen Sie einen Punkt auf der Karte**, und klicken Sie dann auf den Ort auf der Karte, dem ein Punkt auf dem Bild entsprechen soll. Das Bild wird zum ersten Mal auf der Karte platziert, sobald ein Punkt ausgewählt ist.
4. Verwenden Sie den **Skalieren**-Regler, um das Bild zu skalieren, und den **Transparenz**-Regler, um die Basiskarte während der Positionierung durchzusehen.
5. Klicken Sie auf **Bild ausrichten** und klicken Sie erneut auf die Karte, um das Bild so zu verschieben, dass der angeheftete Punkt genau ausgerichtet ist.
6. Wiederholen Sie die Schritte für Skalierung, Transparenz und Ausrichtung, bis das Bild mit der zugrunde liegenden Geografie übereinstimmt, und speichern Sie dann.

Im Hintergrund werden die Eckkoordinaten des Bildes in einem `map:bounds`-Attribut des Medienobjekts gespeichert.

### Anzeigen von Überlagerungen auf der Karten-Seite

Sobald ein Medienobjekt auf diese Weise georeferenziert wurde, wird es automatisch als umschaltbare Ebene auf der Karten-Seite verfügbar. Öffnen Sie den Ebenen-Schalter (gestapelte Ebenen-Ikone, unten links), um jede Überlagerung unabhängig von der Basiskarte ein- oder auszublenden. Überlagerungen werden nach dem Titel des Medienobjekts aufgelistet.
