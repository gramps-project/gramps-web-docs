# Wie Gramps Daten organisiert

Gramps Web speichert einen Stammbaum nicht als Diagramm, sondern als separate Objekte – Personen, Familien, Ereignisse, Orte, Quellen und so weiter –, die miteinander verknüpft sind. Sobald du weißt, wie diese Objekte zusammenpassen, wird die Dateneingabe vorhersehbar: Alles, womit du eine Verknüpfung herstellen möchtest, muss zuerst vorhanden sein.

Gramps Web verwendet dasselbe Datenmodell wie Gramps Desktop, daher gilt alles auf dieser Seite für beide.

## Die Bausteine

| Objekt | Was es darstellt | Beispiele |
|---|---|---|
| Person | Eine einzelne Person | Du, deine Großmutter |
| Familie | Ein Paar, dessen Kinder oder beides | Deine Eltern und ihre Kinder |
| Ereignis | Etwas, das geschehen ist, mit einem Datum und einem Ort | Geburt, Heirat, Volkszählung, Auswanderung |
| Ort | Ein geografischer Ort | Ein Dorf, eine Pfarrei, ein Land |
| Quelle | Ein Dokument oder eine Informationssammlung | Ein Kirchenbuch, eine Volkszählung, ein Buch |
| Beleg | Eine bestimmte Referenz innerhalb einer Quelle | Seite 12, Eintrag 3 des Kirchenbuchs |
| Aufbewahrungsort | Wo eine Quelle aufbewahrt wird | Ein Archiv, eine Bibliothek, eine Website |
| Notiz | Freier Text | Eine Transkription, Forschungsnotizen |
| Medienobjekt | Eine Datei | Ein Foto, eine gescannte Urkunde |

Jeder Objekttyp hat seine eigene Liste in Gramps Web, siehe [Listen](lists.md).

## Personen und Familien

Eltern und Kinder sind nicht direkt miteinander verknüpft, sondern über eine **Familie**. Eine Familie hat bis zu zwei Partner und beliebig viele Kinder:

- Deine Eltern und du sind über die Familie verknüpft, in der du ein Kind bist.
- Deine Geschwister sind die anderen Kinder derselben Familie.
- Du und dein Ehepartner bildet eine weitere Familie, in der ihr gemeinsam mit euren Kindern Partner seid.

Eine Person kann in einer Familie Kind und in mehreren Familien Partner sein. Jedes Kind hat zu jedem seiner Eltern eine Beziehung, etwa leiblich, adoptiert oder Stiefkind, und jede Familie hat einen Beziehungstyp, etwa verheiratet oder eingetragene Lebenspartnerschaft.

Deshalb bedeutet „Eltern hinzufügen“ zu einer Person, die Person als Kind zu einer Familie hinzuzufügen – was das [Stammbaumdiagramm](tree-edit.md) in einem Schritt für dich erledigt.

## Ereignisse

Eine Geburt, ein Tod oder eine Heirat ist kein Feld einer Person, sondern ein **eigenständiges Ereignis** mit einem Typ, einem Datum, einem Ort und einer Beschreibung. Personen werden über eine **Rolle** mit einem Ereignis verknüpft: Die Person, deren Geburt es ist, hat die Rolle „Primär“, während eine andere Person mit demselben Ereignis beispielsweise als Zeuge verknüpft sein kann.

Ereignisse, die ein Paar betreffen, etwa eine Heirat, gehören zur Familie und nicht zu einem der beiden Partner. Ein Ereignis kann auch von mehreren Personen gemeinsam verwendet werden – zum Beispiel ein Volkszählungseintrag, der einen ganzen Haushalt aufführt –, anstatt einmal pro Person eingegeben zu werden.

Das wirkt sich auf die Bearbeitung aus. Das Ereignis selbst – sein Typ, Datum, Ort und seine Beschreibung – ist für alle damit verknüpften Personen gleich. Wenn du ein gemeinsames Ereignis auf der Seite einer Person bearbeitest, änderst du es daher für alle. Der Bearbeitungsdialog listet deshalb zuerst die anderen Teilnehmer auf, und die Felder werden erst nach **Für alle bearbeiten** bearbeitbar. Was zur Verknüpfung einer Person mit dem Ereignis gehört – die Rolle sowie Belege, Notizen und Attribute, die nur für diese Person gelten –, wird auf der Seite des Ereignisses im Bearbeitungsmodus im Tab **Teilnehmer** bearbeitet. Dort kannst du auch Teilnehmer hinzufügen und entfernen. Die Rolle eines Paten und die Notiz „mit Handzeichen unterschrieben“ gehören beispielsweise zur Verknüpfung des Paten mit der Taufe und nicht zur Taufe selbst.

## Gemeinsame Objekte: Orte und Quellen

Orte, Quellen, Belege, Aufbewahrungsorte, Notizen und Medienobjekte existieren unabhängig voneinander, und beliebig viele andere Objekte können auf dasselbe Objekt verweisen. Das hat einige Konsequenzen:

- **Einmal erstellen, oft auswählen.** Das Dorf, in dem zehn deiner Vorfahren geboren wurden, ist ein einziger Ort, der in zehn Geburtsereignissen ausgewählt wird. Wenn du seinen Namen oder seine Koordinaten korrigierst, gilt die Korrektur überall.
- **Vor dem Auswählen erstellen.** Formulare in Gramps Web wählen Orte und Quellen aus, die bereits vorhanden sind. Erstelle zuerst einen neuen Ort oder eine neue Quelle über die Schaltfläche **+** (Hinzufügen) in der oberen App-Leiste.
- **Orte sind verschachtelt.** Ein Ort kann von einem größeren Ort umfasst sein – ein Dorf von einem Landkreis, der Landkreis von einem Land –, sodass du die gesamte Hierarchie nicht für jedes Dorf wiederholen musst.
- **Quellen und Belege sind getrennt.** Eine Quelle ist das Kirchenbuch als Ganzes; ein Beleg ist der konkrete Eintrag, der eine Tatsache stützt, mit seiner Seite, seinem Datum und deiner Einschätzung seiner Zuverlässigkeit. Viele Belege können auf dieselbe Quelle verweisen.

Wenn du versehentlich denselben Ort oder dieselbe Quelle zweimal erstellt hast, kannst du die [Duplikate zusammenführen](lists.md#merge).

## Die Seite eines Objekts bearbeiten

Klicke auf der Seite einer Quelle, eines Aufbewahrungsorts oder eines Medienobjekts im Bearbeitungsmodus auf den Titel, um ihn zu ändern (bei einem Medienobjekt die Beschreibung). Drücke die Eingabetaste, klicke auf ✓ oder klicke an eine andere Stelle, um zu speichern; drücke die Esc-Taste oder klicke auf ✕, um abzubrechen.

Die meisten Listen auf der Seite eines Objekts behalten die von dir festgelegte Reihenfolge bei, beispielsweise die Ereignisse, Namen, Attribute, Adressen, Belege oder die Kinder einer Familie. Wähle im Bearbeitungsmodus eine Zeile aus und verschiebe sie mit den Schaltflächen nach oben und unten oder ziehe sie an ihre neue Position: Mit der Maus drückst du auf die Zeile und verschiebst sie; auf einem Touchscreen drückst du auf die Zeile und hältst sie gedrückt, bis du sie aufgenommen hast. Drücke beim Ziehen die Esc-Taste, um abzubrechen. Medien in der Galerie können auf dieselbe Weise neu angeordnet werden, siehe [Profilbilder](media.md#profile-pictures).

## Die Hauptperson

Die Hauptperson ist die Person, mit der die Stammbaumdiagramme beginnen und die als standardmäßiger Ausgangspunkt für Berichte dient. Siehe [Erste Anmeldung](first-login.md), um zu erfahren, wie du sie festlegst.

!!! note "Anders als in Gramps Desktop"
    In Gramps Desktop wird die Hauptperson in der Stammbaumdatenbank gespeichert und ist daher für alle Personen gleich, die diese Datenbank öffnen. Gramps Web verwendet sie nicht. Stattdessen wird die Hauptperson in deinem Browser für jeden Stammbaum separat gespeichert: Sie wird nicht mit anderen Benutzern geteilt und nicht auf einen anderen Browser oder ein anderes Gerät übertragen. Nach dem Importieren eines Stammbaums aus Gramps Desktop oder wenn du Gramps Web auf einem anderen Gerät verwendest, musst du sie erneut festlegen.

## Eine empfohlene Reihenfolge

Wenn du eine neue Familie von Hand eingibst, vermeidest du mit dieser Reihenfolge, ständig zwischen Formularen hin- und herzuwechseln:

1. **Orte und Quellen.** Erstelle die benötigten Orte und, falls du Quellen dokumentierst, die Quelle, aus der du arbeitest.
2. **Personen.** Füge die Personen mit ihren Geburts- und Sterbedaten sowie den entsprechenden Orten hinzu. Am schnellsten geht das im Bearbeitungsmodus des Stammbaumdiagramms, das die Familien für dich erstellt – siehe [Einen neuen Stammbaum beginnen](start-tree.md) und [Den Stammbaum bearbeiten](tree-edit.md).
3. **Weitere Ereignisse.** Öffne eine Familie (beispielsweise über den Tab „Beziehungen“ einer Person), um die Heirat hinzuzufügen, und die Seite einer Person, um weitere Ereignisse hinzuzufügen.
4. **Belege.** Füge im Tab „Quellenbelege“ der Person, des Ereignisses oder eines anderen Objekts, das eine Quelle stützt, einen neuen Beleg hinzu, wähle die Quelle aus und gib die Seite ein.
5. **Notizen und Medien.** Füge Transkriptionen, Fotos und Scans hinzu – siehe [Mediendateien hinzufügen](media.md).

## Daten eingeben

Ein Datum wird in separaten Feldern für Jahr, Monat und Tag eingegeben, die auch mithilfe einer Datumsauswahl ausgefüllt werden können. Lass die Teile weg, die du nicht kennst: Ein Jahr allein ist ein gültiges Datum.
Anstatt einen genauen Tag zu vermuten, beschreibe, was du tatsächlich weißt, indem du den Typ des Datums mit den Chips über den Feldern auswählst. Ein Hinweis unter den Chips erklärt den ausgewählten Typ:

| Was du weißt | Typ | Beispiel |
|---|---|---|
| Das genaue Datum oder einen Teil davon | Regulär | 12. März 1850 oder nur 1850 |
| Ein ungefähres Datum | Ungefähr | ungefähr 1850 |
| Eine Grenze | Vor, Nach | vor 1900 |
| Das Datum liegt innerhalb eines Zeitraums | Zeitraum | zwischen 1850 und 1855 (Felder „Frühestes“ und „Spätestes“) |
| Etwas dauerte einen Zeitraum | Zeitspanne | von 1850 bis 1855 |

Bei einer Zeitspanne kann eines der beiden Daten („Von“ und „Bis“) leer gelassen werden, sodass „ab 1850“ oder „bis 1855“ eine Zeitspanne mit nur einem Datum ist.

Die Felder **Qualität** und **Kalender** befinden sich unter **Weitere Optionen**. Dieser Bereich wird automatisch geöffnet, wenn ein Datum eines der beiden Felder verwendet. Die Qualität dokumentiert, wie du zu einem Datum gelangt bist: „Geschätzt“ für eine begründete Vermutung, „Berechnet“ für ein aus anderen Informationen abgeleitetes Datum, beispielsweise ein aus dem Alter beim Tod berechnetes Geburtsjahr.

!!! warning "Ungefähre und geschätzte Daten decken 50 Jahre in beide Richtungen ab"
    Beim Vergleichen von Daten behandelt Gramps ein Datum des Typs „ungefähr“ – und jedes Datum mit der Qualität „Geschätzt“ – als einen Zeitraum, der sich 50 Jahre vor bis 50 Jahre nach dem angegebenen Datum erstreckt. Wenn du beispielsweise die Personenliste nach Personen filterst, die zwischen 1840 und 1860 geboren wurden, wird auch eine Person gefunden, die „ungefähr 1880“ geboren wurde, da dieses Datum den Zeitraum von 1830 bis 1930 abdeckt. Ebenso werden „vor“ und „nach“ so behandelt, als würden sie sich bis zu 50 Jahre vor beziehungsweise nach dem Datum erstrecken.

    Dies kann zu überraschenden Ergebnissen führen. Verwende „ungefähr“ und „Geschätzt“ daher nur, wenn du das Datum nicht genauer eingrenzen kannst. Wenn du einen kürzeren Zeitraum kennst, ist ein Zeitraum wie „zwischen 1878 und 1882“ präziser.

Mit dem Kalender kannst du ein Datum in dem Kalender eingeben, der im ursprünglichen Eintrag verwendet wurde, etwa im Julianischen Kalender, anstatt es selbst umzurechnen.
