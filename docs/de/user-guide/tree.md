# Familienbaum

Die Seite „Familienbaum“ ist über die Seitenleiste erreichbar und zeigt interaktive Diagramme, die auf eine ausgewählte Person zentriert sind. Über Tabs am oberen Rand der Seite stehen fünf Diagrammtypen zur Verfügung.

## Auswählen der Ausgangsperson

Alle Diagramme beginnen mit der Person, die aktuell im Stammbaum ausgewählt ist (in der Werkzeugleiste angezeigt). Die derzeit zentrierte Person wird mit einem Schlagschatten hervorgehoben. Verwende die Schaltfläche **Hauptperson**, um zu deiner Hauptperson zurückzuspringen, oder die Schaltfläche **Zurück**, um zur zuvor angezeigten Person zurückzukehren. Wenn du im Diagramm auf die Karte einer Person klickst, wird das Diagramm auf diese Person zentriert.

Wenn noch keine Hauptperson festgelegt wurde, bietet die Seite eine Schaltfläche **Hauptperson festlegen**, mit der du direkt nach einer Person suchen und sie auswählen kannst. Wenn der Stammbaum noch keine Personen enthält, sehen Benutzer mit der Rolle „Bearbeiter“ oder höher stattdessen eine Schaltfläche **Neue Person**. Die erste in einem leeren Stammbaum erstellte Person wird automatisch deine Hauptperson, sodass das Diagramm sofort angezeigt wird.

## Diagrammtypen

### Vorfahrendiagramm

Ein Ahnentafel-Diagramm, das die Vorfahren der ausgewählten Person zeigt. Die Eltern erscheinen links (oder je nach Layout rechts), die Großeltern weiter außen usw.

### Nachfahrendiagramm

Zeigt die Nachkommen der ausgewählten Person – Kinder, Enkelkinder usw.

### Sanduhrdiagramm

Kombiniert die Vorfahren oberhalb und die Nachkommen unterhalb der ausgewählten Person in einer einzigen Ansicht.

### Beziehungsdiagramm

Zeigt den Beziehungspfad zwischen zwei Personen. Die ausgewählte Person ist ein Endpunkt. Klicke auf eine beliebige andere Person im Diagramm, um den zweiten Endpunkt festzulegen und den kürzesten Beziehungspfad zwischen ihnen anzuzeigen.

Jedes Paar ist durch einen kleinen Familienknoten zwischen den beiden Partnern verbunden. Bewege den Mauszeiger darüber oder klicke bzw. tippe darauf, um die Details der Familie zu sehen – etwa Heiratsdatum und -ort sowie die Kinder – ohne das Diagramm zu verlassen. Die Schaltfläche **Öffnen** in der Vorschau führt zur Seite der Familie. Der Knoten eines nicht verheirateten Paares hat eine gestrichelte Umrandung.

!!! note
    Dieselbe Person kann im Diagramm mehr als einmal erscheinen – beispielsweise wenn jemand mehrfach verheiratet war und entlang des Pfads in mehreren Familieneinheiten erscheint. Das ist beabsichtigt und kein Fehler.

### Fächergrafik

Ein kreisförmiges Ahnentafel-Diagramm. Die Vorfahren strahlen von der ausgewählten Person in der Mitte nach außen.

Die Schaltfläche **Farbe** in der Werkzeugleiste färbt die Segmente anhand einer Eigenschaft jeder Person: der Anzahl der Ereignisse oder Notizen, des Geburtsjahrs, des Todesjahrs, des Alters, des Nachnamens, der Religion oder der Vorfahrenhäufigkeit (wie oft eine Person im Diagramm erscheint). Bei der Färbung nach Nachnamen wird der Nachname des Geburtsnamens der Person verwendet oder, wenn kein Geburtsname vorhanden ist, der Nachname des primären Namens. Um die Färbung zu entfernen, entferne das Etikett, das die ausgewählte Farbe anzeigt.

## Zu Verwandten wechseln und Zweige erweitern

Im Vorfahrendiagramm und in der Fächergrafik verfügt die ausgewählte Person über eine Chevron-Schaltfläche, die ein Menü mit ihren Kindern öffnet. Im Nachfahrendiagramm öffnet sie stattdessen ein Menü mit ihren Eltern. Wenn du eine Person aus dem Menü auswählst, wird das Diagramm auf diese Person zentriert.

Im Vorfahrendiagramm, Nachfahrendiagramm und Sanduhrdiagramm haben Personen am Rand des Diagramms, deren Eltern oder Kinder nicht angezeigt werden, auf der Seite, auf der ihr Zweig fortgesetzt wird, ein Chevron. Wenn du darauf klickst, wird diesem Zweig eine weitere Generation hinzugefügt, während die ausgewählte Person unverändert bleibt. So kannst du beispielsweise alle Großeltern anzeigen und anschließend nur einer Linie weiter zurück folgen. Erweiterte Zweige werden zurückgesetzt, wenn du eine andere Person auswählst oder zu einem anderen Diagramm wechselst.

## Navigationssteuerelemente

Alle Diagrammtypen verfügen über eine Werkzeugleiste mit den folgenden Schaltflächen:

- **Hauptperson** – zu deiner Hauptperson zurückspringen
- **Zurück** – zur zuvor zentrierten Person zurückkehren
- **Personendetails** – die vollständige Profilseite der derzeit zentrierten Person öffnen
- **Einstellungen** – einen Dialog öffnen, um diagrammspezifische Anzeigeoptionen anzupassen (siehe unten)

Alle Diagramme unterstützen **Verschieben** (klicken und ziehen) und **Zoomen** (Mausrad oder Auf- und Zuziehen).

## Diagrammeinstellungen

Der Dialog **Einstellungen** (Zahnradsymbol in der Werkzeugleiste) ermöglicht dir, abhängig vom Diagrammtyp, die folgenden Optionen anzupassen:

- **Maximale Vorfahrengenerationen** – wie viele Generationen von Vorfahren angezeigt werden
- **Maximale Nachfahrengenerationen** – wie viele Generationen von Nachkommen angezeigt werden
- **Maximaler Verwandtschaftsgrad** – für das Beziehungsdiagramm die maximale Länge des zu suchenden Pfads. Hohe Werte können dazu führen, dass das Diagramm bei großen Stammbäumen langsam geladen wird.
- **Maximale Anzahl angezeigter Bilder** – begrenzt die im Diagramm angezeigten Profilfotos, um die Leistung zu verbessern
- **Namensanzeigeformat** – legt fest, wie Namen auf Personenkarten angezeigt werden

Klicke auf **Zurücksetzen**, um die Standardeinstellungen wiederherzustellen, oder auf **Schließen**, um deine Änderungen anzuwenden.

Die Einstellungen für Diagramme werden im lokalen Speicher des Browsers gespeichert und bleiben daher sitzungsübergreifend auf demselben Gerät erhalten.

## Standarddiagrammtyp

Der Diagrammtyp, der beim ersten Öffnen der Seite „Familienbaum“ angezeigt wird, kann in den [Benutzereinstellungen](settings.md) konfiguriert werden. Deine gewählte Standardeinstellung gilt auf allen deinen Geräten.

## Bearbeiten des Stammbaums

Benutzer mit der Rolle „Bearbeiter“ oder höher können Personen direkt über das Vorfahrendiagramm hinzufügen und verknüpfen. Einzelheiten findest du unter [Bearbeiten des Stammbaums](tree-edit.md).
