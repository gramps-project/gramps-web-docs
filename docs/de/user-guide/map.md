# Karte

Die Seite „Karte“ zeigt alle Orte in deinem Stammbaum als interaktive Markierungen auf einer geografischen Karte an. Sie ist über die Seitenleiste erreichbar.

## Ortsmarkierungen

Nur Orte, für die GPS-Koordinaten in der Gramps-Datenbank gespeichert sind, werden auf der Karte angezeigt. Orte ohne Koordinaten werden stillschweigend ausgelassen. GPS-Koordinaten können auf der Ortsdetailseite festgelegt werden (bearbeite den Ort und fülle die Felder für Breitengrad und Längengrad aus).

!!! tip
    Wenn viele deiner Orte auf der Karte fehlen, öffne eine Ortsdetailseite und prüfe, ob Breitengrad und Längengrad festgelegt sind. Du kannst Koordinaten direkt in der Bearbeitungsansicht des Ortes hinzufügen oder korrigieren.

Jeder Ort mit Koordinaten wird als Markierung angezeigt. Wenn du auf eine Markierung klickst, wird eine Zusammenfassungskarte mit dem Ortsnamen und den zugehörigen Ereignissen und Personen geöffnet. Klicke auf den Ortsnamen in der Karte, um die vollständige Ortsdetailseite zu öffnen.

## Suche

Das Suchfeld in der oberen linken Ecke der Karte sucht während der Eingabe und gruppiert die Ergebnisse unter drei Überschriften:

- **Orte** – Orte in deinem Stammbaum. Wenn du einen auswählst, wird die Karte dorthin verschoben und seine Markierung hervorgehoben.
- **Personen** – Personen in deinem Stammbaum. Wenn du eine auswählst, wechselt die Karte in die weiter unten beschriebene Personenansicht [hier](#following-a-person-across-the-map).
- **Extern** – Orte aus [OpenStreetMap](https://www.openstreetmap.org/) für jeden beliebigen Ort auf der Welt. Wenn du einen auswählst, wird die Karte einfach auf diesen Ort verschoben und dorthin gezoomt; die Orte deines Stammbaums werden dadurch weder gefiltert noch geändert.

Die externen Ergebnisse sind auch beim Hinzufügen von Koordinaten zu einem Ort hilfreich: Du kannst den Ort hier nachschlagen, um zu sehen, wo er sich befindet, bevor du seinen Breiten- und Längengrad eingibst.

## Einer Person auf der Karte folgen

Wenn du eine Person auswählst – über das Suchfeld der Karte oder mit der Schaltfläche **In Karte öffnen** auf der Detailseite einer Person –, werden die mit den Ereignissen dieser Person verbundenen Orte angezeigt – einschließlich der Ereignisse ihrer Familien, etwa Eheschließungen –, die in chronologischer Reihenfolge durch Linien verbunden sind. Kleine Pfeile entlang jeder Linie zeigen die Bewegungsrichtung an, sodass du dem Leben einer Person von der Geburt bis zum Tod auf der Karte folgen kannst.

Orte auf einer Ortsdetailseite haben ebenfalls eine Schaltfläche **In Karte öffnen**, die die Karte öffnet und auf diesen Ort zentriert.

## Zeitschieberegler

Der Zeitschieberegler am unteren Seitenrand filtert die angezeigten Ortsmarkierungen anhand des Jahres ihrer zugehörigen Ereignisse:

- Ziehe den Schieberegler, um ein Jahr auszuwählen.
- Es werden nur Orte angezeigt, die mit Ereignissen verknüpft sind, die in das ausgewählte Zeitfenster fallen.
- Nutze diese Funktion, um nachzuverfolgen, wo deine Vorfahren zu einem bestimmten Zeitpunkt in der Geschichte lebten.

## Kartenebenen

Mit einer Schaltfläche zum Wechseln der Ebenen (Symbol mit übereinanderliegenden Ebenen, unten links) kannst du zwischen zwei Basiskarten wählen. Darunter werden deine eigenen Kartenebenen unter „Deine Karten“ (siehe [Benutzerdefinierte Kartenüberlagerungen](#custom-map-overlays) und [Kartendateien von Orten](#map-files-of-places)) sowie die Ebene [Wikidata-Gebäude](#wikidata-buildings) unter „Extern“ aufgelistet. Jede dieser Ebenen kann ein- und ausgeschaltet werden.

Die Bezeichnungen beider Basiskarten werden in der von dir in Gramps Web ausgewählten Sprache angezeigt, sofern die Kartendaten einen Namen in dieser Sprache haben, andernfalls in der lokalen Bezeichnung.

### Basiskarte

Die Standardebene wird von [OpenFreeMap](https://openfreemap.org) bereitgestellt (Liberty-Stil im hellen Modus, dunkler Stil im dunklen Modus). Es handelt sich um eine moderne Karte für allgemeine Zwecke, die sich zum Auffinden von Orten eignet.

### Historische Karte

Wechselt die Basiskarte zu [OpenHistoricalMap](https://www.openhistoricalmap.org) (OHM), einem von der Gemeinschaft getragenen Projekt, das die Welt so kartiert, wie sie zu verschiedenen Zeitpunkten existierte – stell dir das als historisches Gegenstück zu OpenStreetMap vor.

Wenn die Ebene „Historische Karte“ aktiv ist, filtert der Zeitschieberegler auch die Kartenkacheln selbst: OHM stellt die Karte so dar, wie sie im ausgewählten Jahr aussah. Dadurch werden historische Grenzen, Ortsnamen und Merkmale anstelle der modernen angezeigt. So kannst du sowohl den Aufenthaltsort deiner Vorfahren als auch den zeitgenössischen geografischen und politischen Kontext in einer einzigen Ansicht sehen.

!!! note
    Die Abdeckung von OpenHistoricalMap variiert je nach Region und Zeitraum. In Gebieten oder Epochen mit wenigen Beiträgen werden möglicherweise nur wenige historische Details angezeigt. Wenn dir fehlende oder ungenaue historische Daten auffallen, erwäge, zu [OpenHistoricalMap beizutragen](https://www.openhistoricalmap.org) – es handelt sich um ein offenes Gemeinschaftsprojekt, das von allen bearbeitet werden kann.

## Benutzerdefinierte Kartenüberlagerungen

Zusätzlich zu den integrierten Basisebenen kannst du jedes gescannte historische Kartenbild – das in Gramps als **Medien**-Objekt gespeichert ist – in eine benutzerdefinierte Überlagerung umwandeln, die auf der Live-Karte positioniert wird. Das ist nützlich für Scans alter Stadtpläne, Pfarrkarten oder Grundstückskarten, die du direkt mit der modernen oder historischen Geografie vergleichen möchtest.

### Georeferenzierung eines Bildes

1. Öffne das Medienobjekt des gescannten Kartenbildes und wechsle in den Bearbeitungsmodus.
2. Öffne die Registerkarte „Karte“ und klicke auf **Koordinaten bearbeiten**. Dadurch wird ein Georeferenzierungsdialog geöffnet, in dem das Bild neben einer Karte angezeigt wird.
3. Klicke auf **Einen Punkt auf der Karte auswählen** und anschließend auf den Ort auf der Karte, dem ein Punkt auf dem Bild entsprechen soll. Sobald ein Punkt ausgewählt ist, wird das Bild zum ersten Mal auf der Karte platziert.
4. Verwende den Schieberegler **Skalierung**, um die Größe des Bildes anzupassen, und den Schieberegler **Deckkraft**, um beim Positionieren die Basiskarte durch das Bild hindurchzusehen.
5. Klicke auf **Bild ausrichten** und anschließend erneut auf die Karte, um das Bild zu verschieben, sodass der markierte Punkt genau übereinstimmt.
6. Wiederhole die Schritte zur Skalierung, Deckkraft und Ausrichtung, bis das Bild mit der zugrunde liegenden Geografie übereinstimmt, und speichere anschließend.

Im Hintergrund werden dabei die Koordinaten der Bildecken in einem `map:bounds`-Attribut des Medienobjekts gespeichert.

### Überlagerungen auf der Kartenseite anzeigen

Sobald ein Medienobjekt auf diese Weise georeferenziert wurde, steht es auf der Kartenseite automatisch als ein- und ausschaltbare Ebene zur Verfügung. Öffne den Ebenenwechsler (Symbol mit übereinanderliegenden Ebenen, unten links), um jede Überlagerung unabhängig von der Basiskarte ein- oder auszublenden. Die Überlagerungen werden nach dem Titel des Medienobjekts aufgelistet.

Unter dem Namen jeder Überlagerung befindet sich ein Schieberegler für die Deckkraft, sodass du die Basiskarte durch das Bild hindurchsehen kannst.

## Kartendateien von Orten

An Orte können Kartendateien als Medienobjekte angehängt werden – zum Beispiel die Grenzen einer Gemeinde, eines Bezirks oder eines Landguts oder eine Route. Unterstützt werden KML-Dateien (`.kml`), GeoJSON-Dateien (`.geojson`) und GPX-Dateien (`.gpx`).

Wenn du einen Ort auf der Karte auswählst, werden seine Kartendateien über der Karte angezeigt, wobei die in der Datei gespeicherten Farben verwendet werden, sofern vorhanden. Dies funktioniert auch für Orte ohne Koordinaten: Die Karte zoomt dann auf das von den Dateien abgedeckte Gebiet. Solange der Ort ausgewählt ist, werden seine Dateien im Ebenenwechsler unter „Deine Karten“ aufgelistet, wo du jede einzelne ausblenden kannst.

Um eine Kartendatei zu einem Ort hinzuzufügen, füge sie wie jede andere [Mediendatei](media.md) zur Galerie des Ortes hinzu.

## Wikidata-Gebäude

Die Ebene „Wikidata-Gebäude“ zeigt in [Wikidata](https://www.wikidata.org/) erfasste Gebäude an, etwa Kirchen, Bauernhöfe oder Stadthäuser. Sie ist standardmäßig ausgeschaltet und kann im Ebenenwechsler unter „Extern“ eingeschaltet werden. Gebäude werden nur angezeigt, wenn die Karte weit genug vergrößert ist. Wenn der Zeitschieberegler aktiv ist, werden nur Gebäude angezeigt, die zum ausgewählten Zeitpunkt existierten.

Klicke auf ein Gebäude, um seine Details aus Wikidata anzuzeigen, etwa wann es gebaut oder abgerissen wurde sowie seine Adressen, Bewohner und Eigentümer.

### Ein Gebäude als Ort speichern

Benutzer, die Objekte hinzufügen können, sehen in den Gebäudedetails eine Schaltfläche **Als Ort speichern**. Sie öffnet das Formular für einen neuen Ort, in dem der Gebäudename in deiner Sprache, ein Ortstyp (`Farm` für Bauernhöfe, andernfalls `Building`), die Koordinaten und ein Link zum Wikidata-Element vorausgefüllt sind. Vervollständige das Formular, indem du beispielsweise den übergeordneten Ort auswählst, und speichere es.

Wenn sich ein Ort in deinem Stammbaum am selben Standort wie das Gebäude befindet, lautet die Schaltfläche stattdessen **Gespeicherten Ort öffnen** und zeigt diesen Ort an.

!!! info
    Der Serveradministrator kann die Ebene „Wikidata-Gebäude“ mit der Option `mapWikidata` der [Frontend-Konfiguration](../install_setup/frontend-config.md) entfernen.
