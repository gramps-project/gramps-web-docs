# Karte

Die Karten-Seite zeigt alle Orte in Ihrem Stammbaum als interaktive Marker auf einer geografischen Karte an. Sie ist über die Seitenleiste zugänglich.

## Ortsmarker

Nur Orte, die GPS-Koordinaten in der Gramps-Datenbank gespeichert haben, werden auf der Karte angezeigt. Orte ohne Koordinaten werden stillschweigend weggelassen. GPS-Koordinaten können auf der Detailseite des Ortes festgelegt werden (bearbeiten Sie den Ort und füllen Sie die Felder für Breiten- und Längengrad aus).

!!! tip
    Wenn viele Ihrer Orte auf der Karte fehlen, öffnen Sie eine Detailseite des Ortes und überprüfen Sie, ob Breiten- und Längengrad gesetzt sind. Sie können Koordinaten direkt aus der Bearbeitungsansicht des Ortes hinzufügen oder korrigieren.

Jeder Ort mit Koordinaten wird als Marker angezeigt. Ein Klick auf einen Marker öffnet eine Zusammenfassungs-Karte, die den Ortsnamen sowie die verknüpften Ereignisse und Personen anzeigt. Klicken Sie auf den Ortsnamen in der Karte, um die vollständige Detailseite des Ortes zu öffnen.

## Suche

Das Suchfeld in der oberen linken Ecke der Karte ermöglicht es Ihnen, zu jedem Ort der Welt nach Namen zu springen. Dies filtert nicht die Orte des Stammbaums – es schwenkt und zoomt einfach die Karte auf den gesuchten Ort.

## Zeitregler

Der Zeitregler am unteren Ende der Seite filtert, welche Ortsmarker basierend auf dem Jahr ihrer zugehörigen Ereignisse angezeigt werden:

- Ziehen Sie den Griff, um ein Jahr auszuwählen.
- Nur Orte, die mit Ereignissen verknüpft sind, die innerhalb des ausgewählten Zeitfensters liegen, werden angezeigt.
- Nutzen Sie dies, um nachzuvollziehen, wo Ihre Vorfahren zu einem bestimmten Zeitpunkt in der Geschichte lebten.

## Kartenebenen

Ein Schalter für die Ebenen (Symbol für gestapelte Ebenen, unten links) ermöglicht es Ihnen, zwischen zwei Basis-Karten zu wählen:

### Basis-Karte

Die Standardebene, betrieben von [OpenFreeMap](https://openfreemap.org) (Liberty-Stil für den Hellmodus, Dunkelstil für den Dunkelmodus). Dies ist eine moderne, allgemeine Karte, die sich gut zur Lokalisierung von Orten eignet.

### Historische Karte

Wechselt die Basis-Karte zu [OpenHistoricalMap](https://www.openhistoricalmap.org) (OHM), einem gemeinschaftsgetriebenen Projekt, das die Welt so kartiert, wie sie zu verschiedenen Zeitpunkten existierte – denken Sie daran als ein historisches Pendant zu OpenStreetMap.

Wenn die historische Kartenebene aktiv ist, filtert der Zeitregler auch die Kartenausschnitte selbst: OHM rendert die Karte so, wie sie im ausgewählten Jahr erschien, sodass historische Grenzen, Ortsnamen und Merkmale anstelle der modernen angezeigt werden. Dies ermöglicht es, sowohl den Standort Ihrer Vorfahren als auch den zeitgenössischen geografischen und politischen Kontext in einer einzigen Ansicht zu sehen.

!!! note
    Die Abdeckung von OpenHistoricalMap variiert je nach Region und Zeitraum. Gebiete oder Epochen mit spärlichen Beiträgen können begrenzte historische Details zeigen. Wenn Sie fehlende oder ungenaue historische Daten bemerken, ziehen Sie in Betracht, [zu OpenHistoricalMap beizutragen](https://www.openhistoricalmap.org) – es ist ein offenes Gemeinschaftsprojekt, das von jedem bearbeitet werden kann.
