# Arbeiten mit DNA-Übereinstimmungen

DNA-Übereinstimmungen sind DNA-Segmente, die zwischen zwei Individuen übereinstimmen, identifiziert durch das Vorhandensein von Markern, den sogenannten SNPs (die Abkürzung für Einzelne Nukleotid-Polymorphismen, ausgesprochen „snips“).

Um diese Daten zu erhalten, benötigen Sie Zugang zu einem DNA-Test, der in einer Übereinstimmungsdatenbank hochgeladen wurde, die es ermöglicht, DNA-Segment-Übereinstimmungsdaten anzuzeigen (z. B. MyHeritage, Gedmatch, FamilytreeDNA). Gramps Web führt die Übereinstimmung selbst nicht durch, da es nur Zugriff auf die Daten hat, die Sie hochladen.

## Eingabe von DNA-Übereinstimmungsdaten

Um DNA-Übereinstimmungsdaten einzugeben, benötigen Sie [Bearbeitungsberechtigungen](../install_setup/users.md), da die Daten als Notiz in der Gramps-Datenbank gespeichert werden. Die DNA-Ansicht, die über das Hauptmenü zugänglich ist, bietet eine bequeme Möglichkeit, diese Daten im richtigen Format einzugeben.

Um eine neue Übereinstimmung einzugeben, klicken Sie auf die Schaltfläche + in der unteren rechten Ecke. Wählen Sie im sich öffnenden Dialog die beiden Individuen aus. Beachten Sie, dass die „Erste Person“ und die „Zweite Person“ unterschiedlich behandelt werden: Die Übereinstimmung wird als Assoziation von der ersten zur zweiten Person gespeichert. Nur die erste Person kann für die DNA-Übereinstimmungsansicht und den Chromosomenbrowser ausgewählt werden. Typischerweise ist die erste Person diejenige, deren DNA-Test Ihnen vorliegt, und die zweite Person ist ein entfernterer Verwandter.

Wenn die zweite Person nicht in der Datenbank vorhanden ist, müssen Sie sie zuerst erstellen, indem Sie die Schaltfläche „Person erstellen“ in der oberen rechten Ecke der Benutzeroberfläche verwenden. Nachdem Sie die Person erstellt haben, können Sie zur DNA-Übereinstimmungsansicht zurückkehren und die neu erstellte Person auswählen.

Fügen Sie als Nächstes die Rohdaten in das Textfeld ein. Die Daten sollten eine durch Kommas oder Tabs getrennte Tabelle von Übereinstimmungen enthalten, die typischerweise die Chromosomennummer, die Start- und Endposition der Übereinstimmung, die Anzahl der SNPs in der Übereinstimmung und die Länge der Übereinstimmung in Centimorgans (cM) enthalten. Sie können auch eine Datei mit den Übereinstimmungsdaten in das Textfeld ziehen und ablegen.

Ein minimales Beispiel für eine solche Tabelle ist:

```csv
Chromosom,Startposition,Endposition,Centimorgans,SNPs
6,6358001,18115715,19.6,7424
7,150135758,154205894,10.9,2816
```

Wenn das Format gültig ist, wird eine Vorschau unter dem Textfeld als Tabelle angezeigt.

Klicken Sie schließlich auf die Schaltfläche „Speichern“, um die Übereinstimmung in der Datenbank zu speichern.

## Anzeigen von DNA-Übereinstimmungsdaten

Die DNA-Übereinstimmungsansicht hat ein Dropdown-Menü, das es ermöglicht, jede Person in der Datenbank auszuwählen, die eine zugehörige DNA-Übereinstimmung hat. Sobald eine Person ausgewählt ist, werden ihre Übereinstimmungen in einer Tabelle aufgelistet: der Name der Übereinstimmung, ihre Beziehung zur ausgewählten Person, die Gesamtlänge der gemeinsamen DNA in Centimorgans (cM), die Anzahl der gemeinsamen Segmente und die Länge des größten dieser Segmente.

Für Übereinstimmungen, die bereits im Baum platziert sind, zeigt die Beziehungsspalte die im Baum aufgezeichnete Beziehung an (automatisch aus der Gramps-Datenbank ermittelt). Für Übereinstimmungen, die nicht mit der ausgewählten Person im Baum verwandt sind, wird die Beziehung geschätzt, die auf der gemeinsamen DNA basiert, gekennzeichnet mit "≈".

Ein Klick auf eine Übereinstimmung öffnet ihre Seite, mit einer Zusammenfassung der gemeinsamen DNA, der [Beziehungsschätzung](#relationship-estimate), einem Diagramm der Beziehung im Baum und der Liste der Segmente. Jedes Segment zeigt an, ob es auf der väterlichen oder mütterlichen Seite ist. Die Seite kann entweder manuell eingegeben werden (indem ein `P` für väterlich oder `M` für mütterlich in einer Spalte namens `Seite` in den Rohdaten angegeben wird) oder automatisch vom letzten gemeinsamen Vorfahren bestimmt werden. Die Schaltfläche zum Herunterladen neben den Segmenten speichert sie als CSV-Datei im Format, das der Übereinstimmungsdialog akzeptiert.

## Beziehungsschätzung

Gemeinsame DNA ist kein Beweis für eine spezifische Beziehung: Die Menge an DNA, die zwei Verwandte teilen, variiert stark, und verschiedene Beziehungen überschneiden sich. Gramps Web zeigt daher eine Reihe möglicher Beziehungen mit ihren Wahrscheinlichkeiten an, die aus der Anzahl und Länge der gemeinsamen Segmente berechnet werden (benötigt Gramps Web API 3.26 oder neuer).

Beziehungen werden nach ihrem *Grad* gruppiert:

- **Eltern oder Kind** und **Vollgeschwister** werden einzeln angezeigt.
- **Verwandter 2. Grades** umfasst Halbgeschwister, Großeltern und Enkelkinder sowie Tanten, Onkel, Nichten und Neffen.
- **Verwandter 3. Grades** umfasst Cousins ersten Grades, Urgroßeltern, Großtanten und Großonkel sowie Halbtanten und -onkel.
- Jeder weitere Grad ist etwa eine Generation weiter entfernt, z. B. sind Cousins ersten Grades einmal entfernt Grad 4 und Cousins zweiten Grades Grad 5. Grad 9 und darüber hinaus werden als "9+" gruppiert.

Beziehungen mit demselben Grad teilen im Durchschnitt etwa die gleiche Menge an DNA, sodass DNA allein sie nicht unterscheiden kann. Verwenden Sie die Alter der Personen, um zwischen ihnen zu entscheiden – ein 30-jähriger Verwandter 2. Grades eines 60-Jährigen ist wahrscheinlicher eine Nichte als ein Großelternteil.

Die Schätzung ist am zuverlässigsten für nahe Verwandte. Bei entfernten Beziehungen teilen Übereinstimmungen nur wenige Segmente, und die Wahrscheinlichkeiten verteilen sich über mehrere Grade.

### Überprüfung des Baums gegen die DNA

Wenn die Übereinstimmung im Baum platziert ist, überprüft Gramps Web, ob die gemeinsame DNA zur dort aufgezeichneten Beziehung passt. Wenn die DNA für diese Beziehung sehr unwahrscheinlich ist, wird ein Warnsymbol in der Übereinstimmungstabelle und eine Warnung auf der Übereinstimmungsseite angezeigt. Die Zahl in Klammern, z. B. "1 : 500", vergleicht, wie wahrscheinlich die DNA für die aufgezeichnete Beziehung ist, mit wie wahrscheinlich sie für die wahrscheinlichste Beziehung ist.

Eine Warnung ist ein Grund, genauer hinzusehen, kein Beweis für einen Fehler. Häufige Ursachen sind:

- ein Fehler im Baum, wie z. B. ein falscher Elternteil,
- eine fälschlicherweise zugeordnete Elternschaft, z. B. eine unbekannte Adoption oder ein anderer biologischer Vater,
- unvollständige Übereinstimmungsdaten, zum Beispiel wenn nur Segmente über einem hohen Schwellenwert vom Testdienst kopiert wurden,
- Beziehungen über mehr als eine Linie, z. B. Personen, die sowohl über ihre Mutter als auch über ihren Vater verwandt sind („Pedigree-Kollaps“), die mehr DNA teilen als erwartet.

Beziehungen, die nicht durch Geburt entstanden sind, wie durch eine Adoption, werden nicht überprüft.

## Bearbeiten einer Übereinstimmung

Um eine Übereinstimmung zu bearbeiten, öffnen Sie ihre Seite und klicken Sie auf die Schaltfläche Bearbeiten oder drücken Sie `e`. Beachten Sie, dass Sie die Rohdaten ändern können, jedoch nicht die mit der Übereinstimmung verbundenen Individuen – Sie müssen die Übereinstimmung löschen und eine neue erstellen, wenn Sie die Individuen ändern möchten.

## Private Übereinstimmungen

Die Dialoge zum Hinzufügen und Bearbeiten einer Übereinstimmung haben einen **Privat**-Schalter. Eine private Übereinstimmung, einschließlich ihrer Segmente, ist für Benutzer, die keine privaten Datensätze anzeigen können, verborgen. Private Übereinstimmungen sind für alle anderen mit einem Schloss gekennzeichnet. Siehe [Private Datensätze](privacy.md) für weitere Informationen zur Privatsphäre.

## Arbeiten mit Übereinstimmungsdaten in Gramps Desktop

Die DNA-Übereinstimmungsdaten werden als Notiz in der Gramps-Datenbank gespeichert. Das Format ist kompatibel mit dem 
[DNA Segment Map Addon](https://gramps-project.org/wiki/index.php/Addon:DNASegmentMapGramplet)
verfügbar für Gramps Desktop. Die Wiki-Seite enthält weitere Details dazu, wie die Daten abgerufen, interpretiert und in Gramps eingegeben werden.

!!! info
    Gramps Web API v2.8.0 führte einige Änderungen ein, um ein breiteres Spektrum an Roh-DNA-Übereinstimmungsdaten zu akzeptieren, die im Gramps Desktop Addon noch nicht verfügbar sind. Das Gramps Desktop Addon wird in Zukunft aktualisiert, um die gleichen Formate zu unterstützen.
