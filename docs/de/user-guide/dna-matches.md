# Arbeiten mit DNA-Matches

DNA-Matches sind DNA-Segmente, die zwischen zwei Individuen übereinstimmen, identifiziert durch das Vorhandensein von Markern, den sogenannten SNPs (die Abkürzung für Einzelne Nukleotid-Polymorphismen, ausgesprochen „snips“).

Um diese Daten zu erhalten, benötigen Sie Zugang zu einem DNA-Test, der in eine Matching-Datenbank hochgeladen wurde, die es ermöglicht, DNA-Segment-Match-Daten anzuzeigen (z. B. MyHeritage, Gedmatch, FamilytreeDNA). Gramps Web führt das Matching nicht selbst durch, da es nur Zugriff auf die Daten hat, die Sie hochladen.

## Eingabe von DNA-Match-Daten

Um DNA-Match-Daten einzugeben, benötigen Sie [Bearbeitungsberechtigungen](../install_setup/users.md), da die Daten als Notiz in der Gramps-Datenbank gespeichert werden. Die DNA-Ansicht, die über das Hauptmenü zugänglich ist, bietet eine bequeme Möglichkeit, diese Daten im richtigen Format einzugeben.

Um ein neues Match einzugeben, klicken Sie auf die Schaltfläche + in der unteren rechten Ecke. Wählen Sie im sich öffnenden Dialog die beiden Personen aus. Beachten Sie, dass die „Erste Person“ und die „Zweite Person“ unterschiedlich behandelt werden: Das Match wird als Assoziation von der ersten zur zweiten Person gespeichert. Nur die erste Person kann für die DNA-Match-Ansicht und den Chromosomen-Browser ausgewählt werden. Typischerweise ist die erste Person diejenige, deren DNA-Test Ihnen vorliegt, und die zweite Person ist ein entfernterer Verwandter.

Wenn die zweite Person nicht in der Datenbank vorhanden ist, müssen Sie sie zuerst erstellen, indem Sie die Schaltfläche „Person erstellen“ in der oberen rechten Ecke der Benutzeroberfläche verwenden. Nachdem Sie die Person erstellt haben, können Sie zur DNA-Match-Ansicht zurückkehren und die neu erstellte Person auswählen.

Fügen Sie als Nächstes die Rohdaten in das Textfeld ein. Die Daten sollten eine durch Kommas oder Tabs getrennte Tabelle von Matches sein, die typischerweise die Chromosomennummer, die Start- und Endposition des Matches, die Anzahl der SNPs im Match und die Länge des Matches in Centimorgans (cM) enthalten. Sie können auch eine Datei mit den Match-Daten in das Textfeld ziehen und ablegen.

Ein minimales Beispiel für eine solche Tabelle ist:

```csv
Chromosom,Startposition,Endposition,Centimorgans,SNPs
6,6358001,18115715,19.6,7424
7,150135758,154205894,10.9,2816
```

Wenn das Format gültig ist, wird eine Vorschau unter dem Textfeld als Tabelle angezeigt.

Klicken Sie schließlich auf die Schaltfläche „Speichern“, um das Match in der Datenbank zu speichern.

## Anzeigen von DNA-Match-Daten

Die DNA-Match-Ansicht hat ein Dropdown-Menü, das es ermöglicht, jede Person in der Datenbank auszuwählen, die ein zugehöriges DNA-Match hat. Sobald eine Person ausgewählt ist, werden die DNA-Match-Daten in einer Tabelle unter dem Dropdown-Menü angezeigt. Sie zeigt den Namen der Person, mit der das Match verbunden ist, die Beziehung zur im Dropdown-Menü ausgewählten Person (automatisch aus der Gramps-Datenbank ermittelt), die Gesamtlänge der gemeinsamen DNA in Centimorgans (cM), die Anzahl der gemeinsamen Segmente und die Länge des größten dieser Segmente.

Wenn Sie auf ein einzelnes Match klicken, öffnet sich eine Detailseite, die alle Segmente anzeigt und ob das Match auf der mütterlichen oder väterlichen Seite liegt. Diese Informationen können entweder manuell eingegeben werden (indem ein `P` für väterlich oder `M` für mütterlich in einer Spalte namens `Seite` in den Rohdaten angegeben wird) oder automatisch von Gramps basierend auf dem letzten gemeinsamen Vorfahren ermittelt werden.

## Bearbeiten eines Matches

Sie können ein Match bearbeiten, indem Sie auf die Bleistiftschaltfläche in der unteren rechten Ecke der Match-Detailansicht klicken. Dies öffnet einen ähnlichen Dialog wie beim Erstellen eines neuen Matches, jedoch mit vorausgefüllten Daten. Beachten Sie, dass Sie die Rohdaten ändern können, jedoch nicht die mit dem Match verbundenen Personen – Sie müssen das Match löschen und ein neues erstellen, wenn Sie die Personen ändern möchten.

## Arbeiten mit Match-Daten in Gramps Desktop

Die DNA-Match-Daten werden als Notiz in der Gramps-Datenbank gespeichert. Das Format ist kompatibel mit dem 
[DNA Segment Map Addon](https://gramps-project.org/wiki/index.php/Addon:DNASegmentMapGramplet)
verfügbar für Gramps Desktop. Die Wiki-Seite enthält weitere Details dazu, wie die Daten beschafft, interpretiert und in Gramps eingegeben werden.

!!! info
    Die Gramps Web API v2.8.0 führte einige Änderungen ein, um ein breiteres Spektrum an Roh-DNA-Match-Daten zu akzeptieren, die im Gramps Desktop Addon noch nicht verfügbar sind. Das Gramps Desktop Addon wird in Zukunft aktualisiert, um die gleichen Formate zu unterstützen.
