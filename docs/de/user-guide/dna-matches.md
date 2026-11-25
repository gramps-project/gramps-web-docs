# Mit DNA-Übereinstimmungen arbeiten

DNA-Übereinstimmungen sind DNA-Segmente, die bei zwei Personen übereinstimmen. Sie werden anhand des Vorhandenseins von Markern identifiziert, den sogenannten SNPs (die Abkürzung für „single nucleotide polymorphisms“, ausgesprochen „snips“).

Um diese Daten zu erhalten, benötigst du Zugriff auf einen DNA-Test, der in eine Übereinstimmungsdatenbank hochgeladen wurde, in der DNA-Segment-Übereinstimmungsdaten angezeigt werden können (z. B. MyHeritage, Gedmatch, FamilytreeDNA). Gramps Web führt die Übereinstimmungssuche nicht selbst durch, da es nur Zugriff auf die von dir hochgeladenen Daten hat.

## Eingeben von DNA-Übereinstimmungsdaten

Um DNA-Übereinstimmungsdaten einzugeben, benötigst du [Bearbeitungsberechtigungen](../install_setup/users.md), da die Daten als Notiz in der Gramps-Datenbank gespeichert werden. Die über das Hauptmenü erreichbare DNA-Ansicht bietet eine bequeme Möglichkeit, diese Daten im richtigen Format einzugeben.

Um eine neue Übereinstimmung einzugeben, klicke unten rechts auf die Schaltfläche +. Wähle im daraufhin geöffneten Dialog die beiden Personen aus. Beachte, dass „Erste Person“ und „Zweite Person“ unterschiedlich behandelt werden: Die Übereinstimmung wird als Zuordnung von der ersten zur zweiten Person gespeichert. Nur die erste Person kann in der DNA-Übereinstimmungsansicht und im Chromosomenbrowser ausgewählt werden. Typischerweise ist die erste Person diejenige, auf deren DNA-Test du Zugriff hast, und die zweite Person ist ein entfernterer Verwandter.

Wenn sich die zweite Person nicht in der Datenbank befindet, musst du sie zuerst über die Schaltfläche „Person erstellen“ in der oberen rechten Ecke der Benutzeroberfläche anlegen. Sobald du die Person erstellt hast, kannst du zur DNA-Übereinstimmungsansicht zurückkehren und die neu erstellte Person auswählen.

Füge als Nächstes die Rohdaten in das Textfeld ein. Bei den Daten sollte es sich um eine durch Kommas oder Tabulatoren getrennte Tabelle mit Übereinstimmungen handeln, die normalerweise die Chromosomennummer, die Start- und Endposition der Übereinstimmung, die Anzahl der SNPs in der Übereinstimmung und die Länge der Übereinstimmung in Zentimorgan (cM) enthält. Du kannst auch eine Datei mit den Übereinstimmungsdaten per Drag-and-Drop in das Textfeld ziehen.

Ein minimales Beispiel für eine solche Tabelle ist:

```csv
Chromosome,Start Location,End Location,Centimorgans,SNPs
6,6358001,18115715,19.6,7424
7,150135758,154205894,10.9,2816
```

Wenn das Format gültig ist, wird unter dem Textfeld eine Vorschau als Tabelle angezeigt. 

Klicke abschließend auf die Schaltfläche „Speichern“, um die Übereinstimmung in der Datenbank zu speichern.

## Anzeigen von DNA-Übereinstimmungsdaten

Die DNA-Übereinstimmungsansicht verfügt über ein Dropdown-Menü, in dem du jede Person in der Datenbank auswählen kannst, der eine DNA-Übereinstimmung zugeordnet ist. Sobald eine Person ausgewählt wurde, werden ihre Übereinstimmungen in einer Tabelle aufgelistet: der Name der Übereinstimmung, die Beziehung zur ausgewählten Person, die Gesamtlänge der gemeinsamen DNA in Zentimorgan (cM), die Anzahl der gemeinsamen Segmente und die Länge des größten dieser Segmente.

Bei Übereinstimmungen, die bereits im Stammbaum platziert sind, zeigt die Beziehungsspalte die im Stammbaum aufgezeichnete Beziehung an (automatisch anhand der Gramps-Datenbank bestimmt). Bei Übereinstimmungen mit Personen, die im Stammbaum nicht mit der ausgewählten Person verwandt sind, wird die anhand der gemeinsamen DNA geschätzte Beziehung mit dem Zeichen „≈“ angezeigt.

Wenn du auf eine Übereinstimmung klickst, wird deren Seite mit einer Zusammenfassung der gemeinsamen DNA, der [Beziehungsschätzung](#relationship-estimate), einem Diagramm der Beziehung im Stammbaum und der Liste der Segmente geöffnet. Für jedes Segment wird angezeigt, ob es auf der väterlichen oder mütterlichen Seite liegt. Die Seite kann entweder manuell eingegeben werden (indem in einer Spalte namens `Side` in den Rohdaten ein `P` für väterlich oder ein `M` für mütterlich angegeben wird) oder anhand des jüngsten gemeinsamen Vorfahren automatisch bestimmt werden. Über die Download-Schaltfläche neben den Segmenten werden diese als CSV-Datei in dem vom Übereinstimmungsdialog akzeptierten Format gespeichert.

## Beziehungsschätzung

Gemeinsame DNA ist kein Beweis für eine bestimmte Beziehung: Die Menge der DNA, die zwei Verwandte gemeinsam haben, variiert stark, und verschiedene Beziehungen überschneiden sich. Gramps Web zeigt daher eine Reihe möglicher Beziehungen mit ihren Wahrscheinlichkeiten an, die anhand der Anzahl und Länge der gemeinsamen Segmente berechnet werden (erfordert Gramps Web API 3.26 oder neuer).

Beziehungen werden nach ihrem *Grad* gruppiert:

- **Elternteil oder Kind** und **Vollgeschwister** werden jeweils einzeln angezeigt.
- **Verwandte des 2. Grades** umfassen Halbgeschwister, Großeltern und Enkelkinder sowie Tanten, Onkel, Nichten und Neffen.
- **Verwandte des 3. Grades** umfassen Cousins und Cousinen ersten Grades, Urgroßeltern, Großtanten und Großonkel sowie Halbgeschwister der Eltern.
- Jeder weitere Grad bedeutet ungefähr eine Generation mehr Abstand. Cousins und Cousinen ersten Grades, die einmal entfernt sind, haben beispielsweise den 4. Grad, und Cousins und Cousinen zweiten Grades haben den 5. Grad. Der 9. Grad und darüber hinaus werden als „9+“ zusammengefasst.

Beziehungen mit demselben Grad haben im Durchschnitt ungefähr die gleiche Menge gemeinsamer DNA, daher können sie allein anhand der DNA nicht voneinander unterschieden werden. Verwende das Alter der Personen, um zwischen ihnen zu entscheiden – eine 30-jährige verwandte Person 2. Grades einer 60-jährigen Person ist wahrscheinlich eher eine Nichte als ein Großelternteil.

Die Schätzung ist bei nahen Verwandten am zuverlässigsten. Bei entfernten Beziehungen haben Übereinstimmungen nur wenige gemeinsame Segmente, und die Wahrscheinlichkeiten verteilen sich auf mehrere Grade.

### Abgleich des Stammbaums mit der DNA

Wenn die Übereinstimmung im Stammbaum platziert ist, prüft Gramps Web, ob die gemeinsame DNA zur dort aufgezeichneten Beziehung passt. Wenn die DNA für diese Beziehung sehr unwahrscheinlich ist, wird in der Übereinstimmungstabelle ein Warnsymbol und auf der Seite der Übereinstimmung eine Warnung angezeigt. Die Zahl in Klammern, z. B. „1 : 500“, vergleicht, wie wahrscheinlich die DNA für die aufgezeichnete Beziehung ist und wie wahrscheinlich sie für die wahrscheinlichste Beziehung ist.

Eine Warnung ist ein Grund für eine genauere Prüfung, aber kein Beweis für einen Fehler. Häufige Ursachen sind:

- ein Fehler im Stammbaum, z. B. ein falsches Elternteil,
- eine falsch zugeordnete Abstammung, z. B. eine unbekannte Adoption oder ein anderer biologischer Vater,
- unvollständige Übereinstimmungsdaten, beispielsweise wenn vom Testdienst nur Segmente oberhalb eines hohen Schwellenwerts kopiert wurden,
- Beziehungen über mehr als eine Linie, z. B. Personen, die sowohl über ihre Mutter als auch über ihren Vater verwandt sind („Ahnenverlust“), wodurch sie mehr DNA gemeinsam haben als erwartet.

Beziehungen, die nicht auf biologischer Abstammung beruhen, beispielsweise durch eine Adoption, werden nicht geprüft.

## Bearbeiten einer Übereinstimmung

Um eine Übereinstimmung zu bearbeiten, öffne ihre Seite und klicke auf die Bearbeitungsschaltfläche oder drücke `e`. Beachte, dass du die Rohdaten ändern kannst, nicht jedoch die der Übereinstimmung zugeordneten Personen – wenn du die Personen ändern möchtest, musst du die Übereinstimmung löschen und eine neue erstellen.

## Private Übereinstimmungen

Die Dialoge zum Hinzufügen und Bearbeiten einer Übereinstimmung enthalten einen Schalter **Privat**. Eine private Übereinstimmung einschließlich ihrer Segmente wird vor Benutzern verborgen, die keine privaten Datensätze anzeigen können. Private Übereinstimmungen sind für alle anderen mit einem Schloss gekennzeichnet. Weitere Informationen zum Datenschutz findest du unter [Private Datensätze](privacy.md).

## Arbeiten mit Übereinstimmungsdaten in Gramps Desktop

Die DNA-Übereinstimmungsdaten werden als Notiz in der Gramps-Datenbank gespeichert. Das Format ist kompatibel mit dem für Gramps Desktop verfügbaren 
[DNA Segment Map Addon](https://gramps-project.org/wiki/index.php/Addon:DNASegmentMapGramplet).
Die Wiki-Seite enthält weitere Informationen darüber, wie du die Daten erhältst, wie du sie interpretierst und wie du die Daten in Gramps eingibst.

!!! info
    Gramps Web API v2.8.0 führte einige Änderungen ein, um einen größeren Bereich von DNA-Übereinstimmungsrohdaten zu akzeptieren. Diese Funktion ist im Gramps-Desktop-Addon noch nicht verfügbar. Das Gramps-Desktop-Addon wird künftig aktualisiert, um dieselben Formate zu unterstützen.
