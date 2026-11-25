# Private Datensätze

Jeder Datensatz im Stammbaum kann als privat markiert werden. Zusammen mit den [Benutzerrollen](../install_setup/users.md#user-roles) wird dadurch festgelegt, wer was sehen kann.

## Wer kann was sehen?

Gramps Web ist niemals öffentlich zugänglich: Nur Benutzer mit einem Konto können überhaupt etwas sehen. „Öffentlich“ bedeutet in Gramps einfach „nicht privat“, also für jeden angemeldeten Benutzer des Stammbaums sichtbar.

| Rolle | Öffentliche Datensätze | Private Datensätze |
|---|---|---|
| Gast | anzeigen | – |
| Mitglied | anzeigen | anzeigen |
| Beitragender | anzeigen, hinzufügen | anzeigen, hinzufügen |
| Bearbeiter, Eigentümer, Administrator | anzeigen, hinzufügen, bearbeiten, löschen | anzeigen, hinzufügen, bearbeiten, löschen |

Für Gäste existieren private Datensätze nicht: Sie werden aus Seiten, Listen, Suchergebnissen, Diagrammen, Berichten, Exporten und Antworten des KI-Assistenten ausgeschlossen. Dies wird beim Lesen der Datenbank durch den Server erzwungen und nicht dadurch, dass Dinge in der App ausgeblendet werden. Ein Gast kann daher auch auf keinem anderen Weg an private Daten gelangen.

Konten, die noch nicht genehmigt wurden (nach der [Selbstregistrierung](registration.md)), können sich überhaupt nicht anmelden.

Wenn Verwandte oder andere Personen mit einem Gastkonto bestimmte Informationen nicht sehen sollen, markiere sie als privat. Wenn alle Benutzer eines Stammbaums alles sehen dürfen, gib ihnen die Rolle „Mitglied“ (oder eine höhere Rolle); dann müssen keine Datensätze als privat markiert werden.

## Lebende Personen sind nicht automatisch privat

Nichts wird automatisch privat gemacht – auch nicht Personen, die noch leben. Die Daten lebender Personen sind für Gäste sichtbar, bis du sie als privat markierst. Dies gilt auch für importierte Stammbäume.

So machst du die wahrscheinlich noch lebenden Personen in Gramps Web privat:

1. Öffne in der Personenliste den [erweiterten Filter](lists.md#advanced-filter) und füge die Bedingung „Wahrscheinlich lebende Personen“ hinzu (lasse das Datum für den heutigen Tag leer). Wende den Filter an.
2. Klicke auf **Auswählen**, aktiviere das Kontrollkästchen in der Kopfzeile und wähle **Alle auswählen**.
3. Wähle die Aktion **Privatsphäre** und markiere die Datensätze als privat.

„Wahrscheinlich lebend“ wird anhand der Daten der Person und ihrer Verwandten geschätzt. Personen ohne verwertbare Datumsangaben werden als lebend betrachtet. Überprüfe das Ergebnis und beachte, dass sich die Schätzung ändern kann, wenn du weitere Daten hinzufügst.

Wenn du eine Person als privat markierst, wird die Person ausgeblendet, nicht jedoch ihre Ereignisse, Notizen, Medien oder Familien – siehe unten. Gramps Desktop bietet weitere Werkzeuge, um die Privatsphäre vieler zugehöriger Datensätze gleichzeitig festzulegen. Du kannst diese mit dem [Sync-Addon](../administration/sync.md) verwenden.

Personen, die später sterben, werden ebenfalls nicht automatisch öffentlich. Ob du das möchtest, bleibt dir überlassen – viele Forscher ziehen es vor, gesammelte Informationen eine Zeit lang privat zu halten.

## Die Schlosssymbole verstehen

Benutzer, die private Daten anzeigen dürfen, sehen neben privaten Einträgen ein Schloss. Es gibt zwei Arten:

- **Ausgefülltes Schloss** – der Datensatz selbst ist privat. Auf der Seite einer Person bedeutet beispielsweise ein ausgefülltes Schloss neben einem Ereignis, dass das Ereignis privat ist, und neben einem Kind, dass das Kind privat ist.
- **Umrissschloss** – nur der *Link* ist privat, nicht der Datensatz, auf den er verweist. Beispielsweise kann der Link einer Person zu einem Ereignis privat sein, während das Ereignis selbst öffentlich ist. Das Ereignis wird dann auf der Seite dieser Person ausgeblendet, bleibt aber an anderer Stelle sichtbar, etwa auf den Seiten anderer Teilnehmer oder in der Ereignisliste.

Wenn sowohl der Datensatz als auch sein Link privat sind, wird das ausgefüllte Schloss angezeigt.

Dieselbe Unterscheidung gilt für Kinder (das Kind oder der Link des Kindes zur Familie), Zuordnungen, Repository-Links einer Quelle und Medien in einer Galerie. Namen, Attribute, Adressen und URLs gehören zu ihrem Datensatz und haben nur das ausgefüllte Schloss.

## Etwas privat machen

Um die Privatsphäre zu ändern, benötigst du Bearbeitungsrechte.

- **Ein vollständiger Datensatz**: Öffne seine Seite, wechsle in den Bearbeitungsmodus und klicke in der Werkzeugleiste auf die Schaltfläche mit dem Schloss.
- **Teil eines Datensatzes** – ein alternativer Name, ein Attribut, eine Adresse, eine URL, eine Zuordnung, ein Link zu einem Kind oder ein Repository-Link: Öffne den Bearbeitungsdialog dieses Elements und aktiviere den Schalter **Privat**. Für den primären Namen gibt es keinen Schalter, da die Person andernfalls als „Privat“ angezeigt würde.
- **Ein Ereignis auf der Seite einer Person oder Familie**: Im Bearbeitungsdialog des Ereignisses gibt es einen Schalter für die Privatsphäre des Ereignisses selbst. Wenn das Ereignis mit anderen Personen geteilt wird, kann es erst nach **Für alle bearbeiten** bearbeitet werden, da es für alle diese Personen privat ist.
- **Der Link einer Person zu einem Ereignis**: Öffne auf der Ereignisseite die Zeile des Teilnehmers im Bearbeitungsmodus. Der dortige Schalter für die Privatsphäre gilt nur für den Link dieses Teilnehmers, sodass das Ereignis für die anderen Teilnehmer sichtbar bleibt.
- **Ein Medienobjekt in einer Galerie**: Klicke im Bearbeitungsmodus auf das Schloss in der Ecke der Kachel.
- **Viele Datensätze auf einmal**: Wähle sie in einer Liste aus und verwende die Aktion **Privatsphäre**; siehe [Listen](lists.md#tags-and-privacy).

Um zu prüfen, welche Datensätze in einer Liste privat sind, aktiviere die Spalte **Privatsphäre** in der Spaltenauswahl der Liste.

## Was du beachten solltest

- Wenn du einen Datensatz privat machst, werden die Datensätze, auf die er verweist, nicht ebenfalls privat. Wenn eine Person privat ist, bleiben ihre Ereignisse, die Familien, denen sie angehört, und die an sie angehängten Notizen sichtbar, sofern sie nicht selbst privat sind. Verwende den erweiterten Filter oder die Spalte **Privatsphäre**, um zugehörige Datensätze zu überprüfen.
- Wenn du eine Familie oder ein Ereignis privat machst, wird es ausgeblendet, nicht jedoch die darin enthaltenen Personen.
- [DNA-Matches und Y-DNA-Daten](dna-matches.md#private-matches) verfügen in ihren Dialogen über einen eigenen Schalter **Privat**.
- Von einem Benutzer erstellte Exporte und Medienarchive, der private Daten nicht anzeigen darf, enthalten keine privaten Datensätze oder Dateien.
- Privatsphäre ist eine Gramps-Funktion. Daher sind in Gramps Desktop als privat markierte Datensätze auch in Gramps Web privat und umgekehrt.
