# Wie Gramps Daten organisiert

Gramps Web speichert einen Stammbaum nicht als Diagramm, sondern als separate Objekte – Personen, Familien, Ereignisse, Orte, Quellen usw. – die miteinander verknüpft sind. Sobald Sie wissen, wie diese Objekte zusammenpassen, wird die Dateneingabe vorhersehbar: Alles, was Sie verknüpfen möchten, muss zuerst existieren.

Gramps Web verwendet dasselbe Datenmodell wie Gramps Desktop, sodass alles auf dieser Seite für beide gilt.

## Die Bausteine

| Objekt | Was es darstellt | Beispiele |
|---|---|---|
| Person | Eine Einzelperson | Sie, Ihre Großmutter |
| Familie | Ein Paar, deren Kinder oder beides | Ihre Eltern und deren Kinder |
| Ereignis | Etwas, das passiert ist, mit einem Datum und einem Ort | Geburt, Heirat, Volkszählung, Auswanderung |
| Ort | Ein geografischer Standort | Ein Dorf, eine Gemeinde, ein Land |
| Quelle | Ein Dokument oder eine Sammlung von Informationen | Ein Kirchenbuch, eine Volkszählung, ein Buch |
| Zitation | Ein spezifischer Verweis innerhalb einer Quelle | Seite 12, Eintrag 3 des Kirchenbuchs |
| Archiv | Wo eine Quelle aufbewahrt wird | Ein Archiv, eine Bibliothek, eine Website |
| Notiz | Freier Text | Eine Transkription, Forschungsanmerkungen |
| Mediendatei | Eine Datei | Ein Foto, ein gescanntes Zertifikat |

Jeder Objekttyp hat seine eigene Liste in Gramps Web, siehe [Listen](lists.md).

## Personen und Familien

Eltern und Kinder sind nicht direkt miteinander verknüpft, sondern durch eine **Familie**. Eine Familie hat bis zu zwei Partner und beliebig viele Kinder:

- Ihre Eltern und Sie sind durch die Familie verbunden, in der Sie ein Kind sind.
- Ihre Geschwister sind die anderen Kinder derselben Familie.
- Sie und Ihr Ehepartner bilden eine andere Familie, in der Sie ein Partner sind, zusammen mit Ihren Kindern.

Eine Person kann in einer Familie ein Kind und in mehreren anderen Familien ein Partner sein. Jedes Kind hat eine Beziehung zu jedem der Elternteile, wie Geburt, Adoption oder Stiefkind, und jede Familie hat einen Beziehungstyp, wie verheiratet oder eingetragene Partnerschaft.

Deshalb bedeutet "Eltern hinzufügen" zu einer Person, die Person als Kind zu einer Familie hinzuzufügen – was das [Baumdiagramm](tree-edit.md) für Sie in einem Schritt erledigt.

## Ereignisse

Eine Geburt, ein Tod oder eine Heirat ist kein Feld einer Person, sondern ein **Ereignis** für sich, mit einem Typ, einem Datum, einem Ort und einer Beschreibung. Personen sind mit einem Ereignis durch eine **Rolle** verknüpft: Die Person, deren Geburt es ist, hat die Rolle "Primär", während jemand anderes mit demselben Ereignis als Zeuge verknüpft sein kann.

Ereignisse, die ein Paar betreffen, wie eine Heirat, gehören zur Familie und nicht zu einem der Partner. Ein Ereignis kann auch von mehreren Personen geteilt werden – zum Beispiel ein Volkszählungsdatensatz, der einen ganzen Haushalt auflistet – anstatt einmal pro Person eingegeben zu werden.

Dies hat Auswirkungen auf die Bearbeitung. Das Ereignis selbst – sein Typ, Datum, Ort und Beschreibung – ist für alle, die damit verknüpft sind, dasselbe, sodass die Bearbeitung eines gemeinsamen Ereignisses von der Seite einer Person aus es für alle ändert. Der Bearbeitungsdialog listet daher zuerst die anderen Teilnehmer auf, und die Felder werden erst nach **Für alle bearbeiten** bearbeitbar. Was zu einer Personens Verknüpfung mit dem Ereignis gehört – die Rolle sowie Zitationen, Notizen und Attribute, die nur für diese Person gelten – wird auf der Seite des Ereignisses im Tab **Teilnehmer** im Bearbeitungsmodus bearbeitet. Dort können Sie auch Teilnehmer hinzufügen und entfernen. Zum Beispiel gehört die Rolle eines Paten und die Notiz "mit einem Zeichen unterschrieben" zur Verknüpfung des Paten zur Taufe, nicht zur Taufe selbst.

## Geteilte Objekte: Orte und Quellen

Orte, Quellen, Zitationen, Archive, Notizen und Mediendateien existieren für sich und beliebig viele andere Objekte können auf dasselbe verweisen. Dies hat einige Konsequenzen:

- **Einmal erstellen, mehrfach auswählen.** Das Dorf, in dem zehn Ihrer Vorfahren geboren wurden, ist ein Ort, der in zehn Geburtsereignissen ausgewählt wird. Wenn Sie seinen Namen oder seine Koordinaten korrigieren, gilt die Korrektur überall.
- **Erstellen Sie es, bevor Sie es auswählen.** Formulare in Gramps Web wählen Orte und Quellen aus, die bereits existieren. Erstellen Sie zuerst einen neuen Ort oder eine neue Quelle mit der **+** (Hinzufügen) Schaltfläche in der oberen App-Leiste.
- **Orte sind geschachtelt.** Ein Ort kann von einem größeren umschlossen werden – ein Dorf von einem Landkreis, der Landkreis von einem Land – sodass Sie die gesamte Hierarchie nicht für jedes Dorf wiederholen müssen.
- **Quellen und Zitationen sind getrennt.** Eine Quelle ist das Kirchenbuch als Ganzes; eine Zitation ist der spezifische Eintrag, der eine Tatsache unterstützt, mit ihrer Seite, ihrem Datum und Ihrem Vertrauen in sie. Viele Zitationen können auf dieselbe Quelle verweisen.

Wenn Sie versehentlich denselben Ort oder dieselbe Quelle zweimal erstellt haben, können Sie [die Duplikate zusammenführen](lists.md#merge).

## Bearbeiten der Seite eines Objekts

Auf der Seite einer Quelle, eines Archivs oder einer Mediendatei klicken Sie im Bearbeitungsmodus auf den Titel, um ihn zu ändern (bei einer Mediendatei deren Beschreibung). Drücken Sie Enter, klicken Sie auf ✓ oder klicken Sie anderswo, um zu speichern; drücken Sie Escape oder klicken Sie auf ✕, um abzubrechen.

Die meisten Listen auf der Seite eines Objekts behalten die Reihenfolge, die Sie ihnen geben, zum Beispiel die Ereignisse, Namen, Attribute, Adressen, Zitationen oder die Kinder einer Familie. Im Bearbeitungsmodus wählen Sie eine Zeile aus und bewegen sie mit den Auf- und Ab-Tasten oder ziehen sie an ihre neue Position: Mit der Maus drücken Sie die Zeile und bewegen sie; auf einem Touchscreen drücken und halten Sie die Zeile, bis sie aufgehoben wird. Drücken Sie Escape während des Ziehens, um abzubrechen. Medien in der Galerie können auf die gleiche Weise neu angeordnet werden, siehe [Profilbilder](media.md#profile-pictures).

## Die Hauptperson

Die Hauptperson ist die Person, von der die Stammbaumdiagramme ausgehen, und der standardmäßige Ausgangspunkt für Berichte. Siehe [Erster Login](first-login.md), um zu erfahren, wie Sie sie festlegen.

!!! Hinweis "Anders als bei Gramps Desktop"
    In Gramps Desktop wird die Hauptperson in der Stammbaumdatenbank gespeichert, sodass sie für jeden, der diese Datenbank öffnet, dieselbe ist. Gramps Web verwendet dies nicht. Stattdessen wird die Hauptperson in Ihrem Browser gespeichert, separat für jeden Baum: Sie wird nicht mit anderen Benutzern geteilt und folgt Ihnen nicht zu einem anderen Browser oder Gerät. Nach dem Importieren eines Baums aus Gramps Desktop oder wenn Sie Gramps Web auf einem anderen Gerät verwenden, müssen Sie sie erneut festlegen.

## Eine empfohlene Reihenfolge

Beim manuellen Eingeben einer neuen Familie vermeidet diese Reihenfolge das Hin- und Herwechseln zwischen Formularen:

1. **Orte und Quellen.** Erstellen Sie die benötigten Orte und, falls Sie Quellen aufzeichnen, die Quelle, mit der Sie arbeiten.
2. **Personen.** Fügen Sie die Personen mit ihren Geburts- und Sterbedaten sowie -orten hinzu. Dies ist im Bearbeitungsmodus des Stammbaumdiagramms am schnellsten, das die Familien für Sie erstellt – siehe [Neuen Baum starten](start-tree.md) und [Stammbaum bearbeiten](tree-edit.md).
3. **Weitere Ereignisse.** Öffnen Sie eine Familie (zum Beispiel über den Tab Beziehungen einer Person), um die Heirat hinzuzufügen, und die Seite einer Person, um andere Ereignisse hinzuzufügen.
4. **Zitationen.** Fügen Sie im Tab Quellenzitationen der Person, des Ereignisses oder eines anderen Objekts, das eine Quelle unterstützt, eine neue Zitation hinzu, wählen Sie die Quelle aus und geben Sie die Seite ein.
5. **Notizen und Medien.** Fügen Sie Transkriptionen, Fotos und Scans hinzu – siehe [Medien Dateien hinzufügen](media.md).

## Dateneingabe

Ein Datum wird als separate Felder für Jahr, Monat und Tag eingegeben, die auch mit einem Datumsauswähler ausgefüllt werden können. Lassen Sie die Teile weg, die Sie nicht wissen: Ein Jahr allein ist ein gültiges Datum. Anstatt einen genauen Tag zu raten, beschreiben Sie, was Sie tatsächlich wissen, indem Sie den Typ des Datums mit den Chips über den Feldern auswählen. Ein Hinweis unter den Chips erklärt den ausgewählten Typ:

| Was Sie wissen | Typ | Beispiel |
|---|---|---|
| Das genaue Datum oder ein Teil davon | Regulär | 12. März 1850 oder nur 1850 |
| Ein ungefähres Datum | Ungefähr | etwa 1850 |
| Eine Grenze | Vor, Nach | vor 1900 |
| Das Datum liegt irgendwo innerhalb eines Zeitraums | Bereich | zwischen 1850 und 1855 (Felder "Frühestes" und "Spätestes") |
| Etwas dauerte über einen Zeitraum | Zeitraum | von 1850 bis 1855 |

Für einen Zeitraum kann eines der beiden Daten ("Von" und "Bis") leer gelassen werden, sodass "von 1850" oder "bis 1855" ein Zeitraum mit nur einem Datum ist.

Die Felder **Qualität** und **Kalender** befinden sich unter **Weitere Optionen**, die sich von selbst öffnen, wenn ein Datum eines von beiden verwendet. Die Qualität dokumentiert, wie Sie zu einem Datum gekommen sind: "Geschätzt" für eine fundierte Schätzung, "Berechnet" für ein Datum, das aus anderen Informationen abgeleitet wurde, wie einem Geburtsjahr, das aus einem Alter bei Tod berechnet wurde.

!!! Warnung "Über und geschätzte Daten decken 50 Jahre in beide Richtungen ab"
    Wenn Gramps Daten vergleicht, behandelt es ein Datum des Typs "ungefähr" – und jedes Datum mit der Qualität "Geschätzt" – als einen Bereich, der von 50 Jahren vor bis 50 Jahren nach dem angegebenen Datum reicht. Zum Beispiel findet das Filtern der Personenliste nach Personen, die zwischen 1840 und 1860 geboren wurden, auch eine Person, die "ungefähr 1880" geboren wurde, da dieses Datum als von 1830 bis 1930 betrachtet wird. Ebenso werden "vor" und "nach" so interpretiert, dass sie bis zu 50 Jahre vor oder nach dem Datum reichen.

    Dies kann zu überraschenden Ergebnissen führen, daher verwenden Sie "ungefähr" und "Geschätzt" nur, wenn Sie das Datum nicht eingrenzen können. Wenn Sie einen kürzeren Zeitraum kennen, ist ein Bereich wie "zwischen 1878 und 1882" präziser.

Der Kalender ermöglicht es Ihnen, ein Datum im Kalender einzugeben, der im ursprünglichen Dokument verwendet wurde, wie dem Julianischen Kalender, anstatt es selbst zu konvertieren.
