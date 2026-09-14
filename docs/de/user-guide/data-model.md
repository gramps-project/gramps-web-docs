# Wie Gramps Daten organisiert

Gramps Web speichert einen Stammbaum nicht als Diagramm, sondern als separate Objekte – Personen, Familien, Ereignisse, Orte, Quellen und so weiter – die miteinander verknüpft sind. Sobald Sie wissen, wie diese Objekte zusammenpassen, wird die Dateneingabe vorhersehbar: Alles, was Sie verknüpfen möchten, muss zuerst existieren.

Gramps Web verwendet dasselbe Datenmodell wie Gramps Desktop, sodass alles auf dieser Seite für beide gilt.

## Die Bausteine

| Objekt | Was es darstellt | Beispiele |
|---|---|---|
| Person | Eine Einzelperson | Sie, Ihre Großmutter |
| Familie | Ein Paar, deren Kinder oder beides | Ihre Eltern und deren Kinder |
| Ereignis | Etwas, das passiert ist, mit einem Datum und einem Ort | Geburt, Heirat, Volkszählung, Emigration |
| Ort | Ein geografischer Standort | Ein Dorf, eine Gemeinde, ein Land |
| Quelle | Ein Dokument oder eine Sammlung von Informationen | Ein Kirchenbuch, eine Volkszählung, ein Buch |
| Zitation | Ein spezifischer Verweis innerhalb einer Quelle | Seite 12, Eintrag 3 des Kirchenbuchs |
| Repository | Wo eine Quelle aufbewahrt wird | Ein Archiv, eine Bibliothek, eine Website |
| Notiz | Freitext | Eine Transkription, Forschungsanmerkungen |
| Medienobjekt | Eine Datei | Ein Foto, ein gescanntes Zertifikat |

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

## Geteilte Objekte: Orte und Quellen

Orte, Quellen, Zitationen, Repositories, Notizen und Medienobjekte existieren für sich und beliebig viele andere Objekte können auf dasselbe verweisen. Dies hat einige Konsequenzen:

- **Einmal erstellen, mehrfach auswählen.** Das Dorf, in dem zehn Ihrer Vorfahren geboren wurden, ist ein Ort, der in zehn Geburtenereignissen ausgewählt wird. Wenn Sie seinen Namen oder seine Koordinaten korrigieren, gilt die Korrektur überall.
- **Erstellen Sie es, bevor Sie es auswählen.** Formulare in Gramps Web wählen Orte und Quellen aus, die bereits existieren. Erstellen Sie zuerst einen neuen Ort oder eine neue Quelle mit der **+** (Hinzufügen) Schaltfläche in der oberen App-Leiste.
- **Orte sind geschachtelt.** Ein Ort kann von einem größeren umschlossen werden – ein Dorf von einem Landkreis, der Landkreis von einem Land – sodass Sie die gesamte Hierarchie nicht für jedes Dorf wiederholen müssen.
- **Quellen und Zitationen sind getrennt.** Eine Quelle ist das Kirchenbuch als Ganzes; eine Zitation ist der spezifische Eintrag, der eine Tatsache unterstützt, mit ihrer Seite, ihrem Datum und Ihrem Vertrauen in sie. Viele Zitationen können auf dieselbe Quelle verweisen.

Wenn Sie versehentlich denselben Ort oder dieselbe Quelle zweimal erstellt haben, können Sie [die Duplikate zusammenführen](lists.md#merge).

## Die Hauptperson

Die Hauptperson ist die Person, von der die Stammbaumdiagramme ausgehen, und der Standardstartpunkt für Berichte. Siehe [Erster Login](first-login.md), um zu erfahren, wie Sie sie festlegen.

!!! Hinweis "Anders als Gramps Desktop"
    In Gramps Desktop wird die Hauptperson in der Stammbaumdatenbank gespeichert, sodass sie für jeden, der diese Datenbank öffnet, dieselbe ist. Gramps Web verwendet dies nicht. Stattdessen wird die Hauptperson in Ihrem Browser gespeichert, separat für jeden Baum: Sie wird nicht mit anderen Benutzern geteilt und folgt Ihnen nicht zu einem anderen Browser oder Gerät. Nach dem Importieren eines Baums aus Gramps Desktop oder wenn Sie Gramps Web auf einem anderen Gerät verwenden, müssen Sie sie erneut festlegen.

## Eine empfohlene Reihenfolge

Beim manuellen Eingeben einer neuen Familie vermeidet diese Reihenfolge das Hin- und Herwechseln zwischen Formularen:

1. **Orte und Quellen.** Erstellen Sie die benötigten Orte und, falls Sie Quellen aufzeichnen, die Quelle, mit der Sie arbeiten.
2. **Personen.** Fügen Sie die Personen mit ihren Geburts- und Sterbedaten sowie -orten hinzu. Dies ist am schnellsten im Bearbeitungsmodus des Stammbaumdiagramms, das die Familien für Sie erstellt – siehe [Neuen Baum starten](start-tree.md) und [Familienbaum bearbeiten](tree-edit.md).
3. **Weitere Ereignisse.** Öffnen Sie eine Familie (zum Beispiel über den Reiter Beziehungen einer Person), um die Heirat hinzuzufügen, und die Seite einer Person, um andere Ereignisse hinzuzufügen.
4. **Zitationen.** Fügen Sie auf dem Reiter Quellenzitationen der Person, des Ereignisses oder eines anderen Objekts, das eine Quelle unterstützt, eine neue Zitation hinzu, wählen Sie die Quelle aus und geben Sie die Seite ein.
5. **Notizen und Medien.** Fügen Sie Transkriptionen, Fotos und Scans hinzu – siehe [Medien Dateien hinzufügen](media.md).

## Dateneingabe

Ein Datum wird als separate Felder für Jahr, Monat und Tag eingegeben, die auch mit einem Datumsauswähler ausgefüllt werden können. Lassen Sie die Teile weg, die Sie nicht wissen: Ein Jahr allein ist ein gültiges Datum.

Anstatt einen genauen Tag zu schätzen, beschreiben Sie, was Sie tatsächlich über den **Typ** des Datums wissen:

| Was Sie wissen | Typ | Beispiel |
|---|---|---|
| Das genaue Datum oder ein Teil davon | Regulär | 12. März 1850 oder nur 1850 |
| Ein ungefähres Datum | etwa | etwa 1850 |
| Eine Grenze | vor, nach | vor 1900 |
| Das Datum liegt irgendwo innerhalb eines Zeitraums | Bereich | zwischen 1850 und 1855 |
| Etwas dauerte einen Zeitraum | Zeitraum | von 1850 bis 1855 |
| Nur der Anfang oder das Ende eines Zeitraums | von, bis | von 1850 |

Das Feld **Qualität** dokumentiert, wie Sie zu einem Datum gekommen sind: "Geschätzt" für eine fundierte Schätzung, "Berechnet" für ein Datum, das aus anderen Informationen abgeleitet ist, wie z. B. einem Geburtsjahr, das aus einem Alter zum Zeitpunkt des Todes berechnet wurde.

!!! Warnung "Über und geschätzte Daten decken 50 Jahre in beide Richtungen ab"
    Wenn Gramps Daten vergleicht, behandelt es ein Datum des Typs "etwa" – und jedes Datum mit der Qualität "Geschätzt" – als einen Bereich, der von 50 Jahren vor bis 50 Jahren nach dem angegebenen Datum reicht. Zum Beispiel findet das Filtern der Personenliste nach Personen, die zwischen 1840 und 1860 geboren wurden, auch eine Person, die "etwa 1880" geboren wurde, da dieses Datum als von 1830 bis 1930 betrachtet wird. In ähnlicher Weise werden "vor" und "nach" als bis zu 50 Jahre vor oder nach dem Datum betrachtet.

    Dies kann zu überraschenden Ergebnissen führen, daher verwenden Sie "etwa" und "Geschätzt" nur, wenn Sie das Datum nicht eingrenzen können. Wenn Sie einen kürzeren Zeitraum kennen, ist ein Bereich wie "zwischen 1878 und 1882" präziser.

Das Feld **Kalender** ermöglicht es Ihnen, ein Datum im Kalender einzugeben, der im ursprünglichen Datensatz verwendet wurde, wie z. B. den Julianischen Kalender, anstatt es selbst zu konvertieren.
