# Stammbaum

Die Stammbaum-Seite ist über die Seitenleiste zugänglich und zeigt interaktive Diagramme, die sich auf eine ausgewählte Person konzentrieren. Fünf Diagrammtypen sind über Registerkarten am oberen Rand der Seite verfügbar.

## Auswahl der Startperson

Alle Diagramme beginnen mit der Person, die derzeit im Baum ausgewählt ist (angezeigt in der Symbolleiste). Die derzeit zentrierte Person ist mit einem Schlagschatten hervorgehoben. Verwenden Sie die **Hauptperson**-Schaltfläche, um zu Ihrer Hauptperson zurückzuspringen, oder die **Zurück**-Schaltfläche, um zur zuvor angezeigten Person zurückzukehren. Durch Klicken auf die Karte einer Person in einem Diagramm wird das Diagramm wieder auf diese Person zentriert.

Wenn keine Hauptperson festgelegt wurde, bietet die Seite eine **Hauptperson festlegen**-Schaltfläche, um direkt nach einer zu suchen und eine auszuwählen. Wenn der Baum noch keine Personen enthält, sehen Benutzer mit der Rolle Editor oder höher stattdessen eine **Neue Person**-Schaltfläche – die erste Person, die in einem leeren Baum erstellt wird, wird automatisch Ihre Hauptperson, sodass das Diagramm sofort angezeigt wird.

## Diagrammtypen

### Ahnenbaum

Ein Stammbaumdiagramm, das die Vorfahren der ausgewählten Person zeigt. Eltern erscheinen links (oder rechts, je nach Layout), Großeltern weiter außen und so weiter.

### Nachkommenbaum

Zeigt die Nachkommen der ausgewählten Person – Kinder, Enkelkinder und so weiter.

### Sanduhr-Diagramm

Kombiniert Vorfahren über und Nachkommen unter der ausgewählten Person in einer einzigen Ansicht.

### Beziehungsdiagramm

Zeigt den Beziehungsweg zwischen zwei Personen. Die ausgewählte Person ist ein Endpunkt; klicken Sie auf eine andere Person im Diagramm, um den zweiten Endpunkt festzulegen und den kürzesten Beziehungsweg zwischen ihnen anzuzeigen.

Jedes Paar wird durch einen kleinen Familienknoten zwischen den beiden Partnern verbunden. Fahren Sie mit der Maus darüber oder klicken oder tippen Sie darauf, um die Details der Familie zu sehen – wie das Heiratsdatum und den -ort sowie die Kinder – ohne das Diagramm zu verlassen. Die **Öffnen**-Schaltfläche in der Vorschau führt zur Seite der Familie. Der Knoten eines Paares, das nicht verheiratet ist, hat eine gestrichelte Umrandung.

!!! Hinweis
    Dieselbe Person kann mehr als einmal im Diagramm erscheinen – zum Beispiel, wenn jemand mehrmals verheiratet war und in mehreren Familieinheiten entlang des Pfades erscheint. Dies ist beabsichtigt, kein Fehler.

### Fächerdiagramm

Ein kreisförmiges Stammbaumdiagramm. Vorfahren strahlen von der ausgewählten Person in der Mitte nach außen.

Die **Farbe**-Schaltfläche in der Symbolleiste färbt die Segmente nach einem Merkmal jeder Person: der Anzahl der Ereignisse oder Notizen, Geburtsjahr, Sterbejahr, Alter, Nachname, Religion oder Vorfahrenhäufigkeit (wie oft eine Person im Diagramm erscheint). Die Färbung nach Nachname verwendet den Nachnamen der Geburtsnamen der Person oder den Hauptnamen, wenn kein Geburtsname vorhanden ist. Um die Färbung zu entfernen, löschen Sie den Chip, der die gewählte Farbe anzeigt.

## Zu Verwandten wechseln und Äste erweitern

Im Ahnenbaum und im Fächerdiagramm hat die ausgewählte Person eine Chevron-Schaltfläche, die ein Menü ihrer Kinder öffnet. Im Nachkommenbaum öffnet sie stattdessen ein Menü ihrer Eltern. Die Auswahl einer Person aus dem Menü zentriert das Diagramm auf diese Person.

Im Ahnenbaum, Nachkommenbaum und Sanduhr-Diagramm haben Personen am Rand des Diagramms, deren Eltern oder Kinder nicht angezeigt werden, einen Chevron auf der Seite, wo ihr Ast weitergeht. Ein Klick darauf fügt dieser Verzweigung eine weitere Generation hinzu, während die ausgewählte Person gleich bleibt. So können Sie beispielsweise alle Großeltern betrachten und dann nur eine Linie weiter zurückverfolgen. Erweiterte Äste werden zurückgesetzt, wenn Sie eine andere Person auswählen oder zu einem anderen Diagramm wechseln.

## Navigationssteuerungen

Alle Diagrammtypen teilen sich eine Symbolleiste mit den folgenden Schaltflächen:

- **Hauptperson** – zurück zu Ihrer Hauptperson springen
- **Zurück** – zurück zur zuvor zentrierten Person
- **Personendetails** – die vollständige Profilseite der derzeit zentrierten Person öffnen
- **Einstellungen** – ein Dialogfeld öffnen, um diagrammspezifische Anzeigeoptionen anzupassen (siehe unten)

Alle Diagramme unterstützen **Pan** (klicken und ziehen) und **Zoom** (Scrollrad oder Pinch).

## Diagrammeinstellungen

Das **Einstellungen**-Dialogfeld (Zahnrad-Symbol in der Symbolleiste) ermöglicht es Ihnen, die folgenden Optionen anzupassen, abhängig vom Diagrammtyp:

- **Maximale Ahnen-Generationen** – wie viele Generationen von Vorfahren angezeigt werden sollen
- **Maximale Nachkommen-Generationen** – wie viele Generationen von Nachkommen angezeigt werden sollen
- **Maximaler Grad der Trennung** – für das Beziehungsdiagramm, die maximale Pfadlänge, die gesucht werden soll. Hohe Werte können das Diagramm bei großen Bäumen langsam laden lassen.
- **Maximale Anzahl der angezeigten Bilder** – begrenzt die Profilfotos, die im Diagramm aus Leistungsgründen angezeigt werden
- **Namensanzeigeformat** – steuert, wie Namen auf Personenkarten angezeigt werden

Klicken Sie auf **Zurücksetzen**, um die Standardeinstellungen wiederherzustellen, oder auf **Schließen**, um Ihre Änderungen anzuwenden.

Die Einstellungen für Diagrammeinstellungen werden im lokalen Speicher des Browsers gespeichert, sodass sie über Sitzungen auf demselben Gerät hinweg bestehen bleiben.

## Standard-Diagrammtyp

Der Diagrammtyp, der angezeigt wird, wenn Sie die Stammbaum-Seite zum ersten Mal öffnen, kann in den [Benutzereinstellungen](settings.md) konfiguriert werden. Ihr gewählter Standard gilt auf all Ihren Geräten.

## Bearbeiten des Baums

Benutzer mit der Rolle Editor oder höher können Personen direkt aus dem Ahnenbaum hinzufügen und verknüpfen. Siehe [Bearbeiten des Stammbaums](tree-edit.md) für Details.
