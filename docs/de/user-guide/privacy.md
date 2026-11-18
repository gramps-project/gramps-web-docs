# Private Aufzeichnungen

Jeder Eintrag im Baum kann als privat markiert werden. Zusammen mit den [Benutzerrollen](../install_setup/users.md#user-roles) entscheidet dies, wer was sieht.

## Wer kann was sehen

Gramps Web ist niemals öffentlich zugänglich: Nur Benutzer mit einem Konto können etwas sehen. "Öffentlich" in Gramps bedeutet einfach "nicht privat", d.h. sichtbar für jeden angemeldeten Benutzer des Baums.

| Rolle | Öffentliche Aufzeichnungen | Private Aufzeichnungen |
|---|---|---|
| Gast | anzeigen | – |
| Mitglied | anzeigen | anzeigen |
| Mitwirkender | anzeigen, hinzufügen | anzeigen, hinzufügen |
| Redakteur, Eigentümer, Administrator | anzeigen, hinzufügen, bearbeiten, löschen | anzeigen, hinzufügen, bearbeiten, löschen |

Für Gäste existieren private Aufzeichnungen nicht: Sie werden aus Seiten, Listen, Suchergebnissen, Diagrammen, Berichten, Exporten und Antworten des KI-Assistenten ausgeschlossen. Dies wird durchgesetzt, wenn der Server die Datenbank liest, nicht durch das Verstecken von Inhalten in der App, sodass ein Gast auch auf keine andere Weise auf private Daten zugreifen kann.

Konten, die noch nicht genehmigt wurden (nach [Selbstregistrierung](registration.md)), können sich überhaupt nicht anmelden.

Wenn also Verwandte oder andere Personen mit einem Gastkonto bestimmte Informationen nicht sehen sollen, markieren Sie diese als privat. Wenn alle Benutzer eines Baums alles sehen dürfen, geben Sie ihnen die Rolle Mitglied (oder höher), und es ist nicht nötig, etwas als privat zu markieren.

## Lebende Personen sind nicht automatisch privat

Nichts wird automatisch privat gemacht – nicht einmal Personen, die noch leben. Daten lebender Personen sind für Gäste sichtbar, bis Sie sie als privat markieren. Dies gilt auch für importierte Bäume.

Um die Personen, die wahrscheinlich leben, in Gramps Web privat zu machen:

1. Öffnen Sie in der Personenliste den [erweiterten Filter](lists.md#advanced-filter) und fügen Sie die Bedingung "Personen wahrscheinlich lebend" hinzu (lassen Sie das Datum für heute leer). Wenden Sie den Filter an.
2. Klicken Sie auf **Auswählen**, aktivieren Sie das Kontrollkästchen im Header und wählen Sie **Alle auswählen**.
3. Wählen Sie die Aktion **Privatsphäre** und markieren Sie die Aufzeichnungen als privat.

"Voraussichtlich lebend" wird aus den Daten der Person und ihrer Verwandten geschätzt. Personen ohne verwertbare Daten gelten als lebend. Überprüfen Sie das Ergebnis und beachten Sie, dass die Schätzung sich ändern kann, wenn Sie Daten hinzufügen.

Das Markieren einer Person als privat verbirgt die Person, jedoch nicht ihre Ereignisse, Notizen, Medien oder Familien – siehe unten. Gramps Desktop bietet weitere Werkzeuge, um die Privatsphäre vieler verwandter Aufzeichnungen auf einmal festzulegen, die Sie mit dem [Sync-Addon](../administration/sync.md) verwenden können.

Personen, die später sterben, werden ebenfalls nicht automatisch öffentlich. Ob Sie das wünschen, liegt bei Ihnen – viele Forscher ziehen es vor, gesammelte Informationen eine Zeit lang privat zu halten.

## Lesen der Schloss-Symbole

Benutzer, die private Daten anzeigen können, sehen ein Schloss neben privaten Elementen. Es gibt zwei Arten:

- **Gefülltes Schloss** – der Eintrag selbst ist privat. Auf der Seite einer Person bedeutet beispielsweise ein gefülltes Schloss neben einem Ereignis, dass das Ereignis privat ist, und neben einem Kind, dass das Kind privat ist.
- **Umriss-Schloss** – nur der *Link* ist privat, nicht der Eintrag, auf den er verweist. Zum Beispiel kann der Link einer Person zu einem Ereignis privat sein, während das Ereignis selbst öffentlich ist. Das Ereignis wird dann von der Seite dieser Person verborgen, bleibt jedoch anderswo sichtbar, z.B. auf den Seiten anderer Teilnehmer oder in der Ereignisliste.

Wenn sowohl der Eintrag als auch sein Link privat sind, wird das gefüllte Schloss angezeigt.

Die gleiche Unterscheidung gilt für Kinder (das Kind oder der Link des Kindes zur Familie), Assoziationen, Repository-Links einer Quelle und Medien in einer Galerie. Namen, Attribute, Adressen und URLs gehören zu ihrem Eintrag und haben nur das gefüllte Schloss.

## Etwas privat machen

Sie benötigen Bearbeitungsrechte, um die Privatsphäre zu ändern.

- **Einen ganzen Eintrag**: Öffnen Sie seine Seite, gehen Sie in den Bearbeitungsmodus und klicken Sie auf die Schloss-Schaltfläche in der Symbolleiste.
- **Teil eines Eintrags** – ein alternativer Name, Attribut, Adresse, URL, Assoziation, Kinderlink oder Repository-Link: Öffnen Sie den Bearbeitungsdialog dieses Elements und aktivieren Sie den Schalter **Privat**. Der Hauptname hat keinen Schalter, da die Person sonst als "Privat" angezeigt würde.
- **Ein Ereignis von der Seite einer Person oder Familie**: Der Bearbeitungsdialog des Ereignisses hat einen Datenschalter für das Ereignis selbst. Wenn das Ereignis mit anderen Personen geteilt wird, kann es erst nach **Für alle bearbeiten** bearbeitet werden, da es für alle privat ist.
- **Ein Link einer Person zu einem Ereignis**: Öffnen Sie auf der Ereignisseite die Zeile des Teilnehmers im Bearbeitungsmodus. Der Datenschalter dort gilt nur für den Link dieses Teilnehmers, sodass das Ereignis für die anderen Teilnehmer sichtbar bleibt.
- **Ein Medienobjekt in einer Galerie**: Klicken Sie im Bearbeitungsmodus auf das Schloss in der Ecke der Kachel.
- **Viele Einträge auf einmal**: Wählen Sie sie in einer Liste aus und verwenden Sie die Aktion **Privatsphäre**, siehe [Listen](lists.md#tags-and-privacy).

Um zu überprüfen, welche Einträge in einer Liste privat sind, aktivieren Sie die **Privatsphäre**-Spalte im Spaltenauswähler der Liste.

## Dinge, die zu beachten sind

- Das Privatmachen eines Eintrags macht die Einträge, auf die er verweist, nicht privat. Wenn eine Person privat ist, sind ihre Ereignisse, die Familien, zu denen sie gehört, und die angehängten Notizen weiterhin sichtbar, es sei denn, sie sind selbst privat. Verwenden Sie den erweiterten Filter oder die **Privatsphäre**-Spalte, um verwandte Einträge zu überprüfen.
- Das Privatmachen einer Familie oder eines Ereignisses verbirgt es, jedoch nicht die darin enthaltenen Personen.
- [DNA-Übereinstimmungen und Y-DNA-Daten](dna-matches.md#private-matches) haben ihren eigenen **Privat**-Schalter in ihren Dialogen.
- Exporte und Medienarchive, die von einem Benutzer erstellt wurden, der keine privaten Daten anzeigen kann, enthalten keine privaten Aufzeichnungen oder Dateien.
- Privatsphäre ist ein Gramps-Feature, sodass in Gramps Desktop als privat markierte Aufzeichnungen auch in Gramps Web privat sind und umgekehrt.
