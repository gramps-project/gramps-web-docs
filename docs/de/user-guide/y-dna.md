# Gramps Web für Y-DNA-Analysen verwenden

!!! note "Hinweis"
    Diese Funktion erfordert Gramps Web API Version 3.3.0 oder höher und Gramps Web Frontend Version 25.9.0 oder höher.

Die Y-DNA-Ansicht in Gramps Web kann Rohdaten zu Einzelnukleotid-Polymorphismen (SNPs) des Y-Chromosoms verwenden, um die wahrscheinlichste Y-DNA-Haplogruppe einer Person zu bestimmen und die abgeleiteten Vorfahren im menschlichen Y-Chromosomen-Stammbaum zusammen mit Zeitschätzungen anzuzeigen.

## So erhältst und speicherst du die Y-DNA-SNP-Daten

Um die Y-DNA-SNP-Daten zu erhalten, musst du einen Y-DNA-Test über einen Gentestdienst durchführen lassen. Das Ergebnis wird als eine Menge von Mutationen (SNPs) dargestellt, die jeweils durch eine Zeichenfolge (z. B. `R-BY44535`) und ein `+`- oder `-`-Zeichen gekennzeichnet sind, das angibt, ob die Mutation vorhanden oder nicht vorhanden ist. Gramps Web erwartet, dass die Zeichenfolge aller getesteten SNPs im Format `SNP1+, SNP2-, SNP3+,...` in einem Personenattribut des benutzerdefinierten Typs `Y-DNA` (Groß-/Kleinschreibung beachten) gespeichert wird. Du kannst dieses Attribut entweder manuell in Gramps Web oder Gramps Desktop erstellen oder zur Y-DNA-Ansicht in Gramps Web navigieren, auf die blaue Schaltfläche „Hinzufügen“ klicken, die Person auswählen, der du die Daten hinzufügen möchtest, und die SNP-Zeichenfolge einfügen. In jedem Fall werden die Daten als Personenattribut in deiner Gramps-Datenbank gespeichert.

[Weiter unten](#anweisungen-zum-erhalten-von-snp-daten-von-testdiensten) findest du Anweisungen dazu, wie du die SNP-Daten von verschiedenen Testdiensten erhältst.

## So funktioniert es

Sobald eine Person ein `Y-DNA`-Attribut mit den SNP-Daten besitzt, verwendet Gramps Web die Open-Source-Python-Bibliothek [yclade](https://github.com/DavidMStraub/yclade), um die wahrscheinlichste Position der Person im menschlichen Y-Chromosomen-Stammbaum zu bestimmen. Der Stammbaum wurde vom Projekt [YFull](https://www.yfull.com/) auf Grundlage von Zehntausenden Y-DNA-Tests erstellt. Beachte, dass Gramps Web eine lokale Kopie des YFull-Stammbaums verwendet, sodass keine Daten an Dritte gesendet werden.

Der Stammbaum wird von der Wurzel bis zu den Blättern durchlaufen. An jedem Knoten werden die mit diesem Knoten verbundenen SNPs mit den positiv und negativ getesteten SNPs der Person verglichen, und der entsprechende Zweig wird verfolgt.

Das Endergebnis ist eine Abfolge von Kladen von der Wurzel des Stammbaums (dem [„Adam“ des Y-Chromosoms](https://en.wikipedia.org/wiki/Y-chromosomal_Adam)) bis zur am weitesten abgeleiteten Klade, die mit den SNP-Daten der Person übereinstimmt. Für jede Klade wird ein geschätztes Alter angegeben, das auf dem Alter der Proben in der YFull-Datenbank basiert, die zu dieser Klade gehören.

Da Y-Chromosomen vom Vater an den Sohn vererbt werden, entspricht diese Abfolge einem Ausschnitt aus der patrilinearen Abstammung der Person.

## So interpretierst du die Ergebnisse

Die wichtigste Information ist die wahrscheinlichste Haplogruppe der Person, die oben auf der Seite angezeigt wird. Der Name ist mit der entsprechenden Seite auf der Website von [YFull](https://www.yfull.com/) verknüpft, die weitere Informationen enthält, beispielsweise das Herkunftsland der getesteten Proben, die zu dieser Haplogruppe gehören.

Im in Gramps Web angezeigten Stammbaum der patrilinearen Vorfahren ist das Feld direkt über der getesteten Person der jüngste gemeinsame Vorfahr (MRCA) aller getesteten Proben, die zur Haplogruppe der Person gehören. Das für diesen Vorfahren angezeigte Datum ist sein geschätztes ungefähres Geburtsdatum. Der Vorfahr über ihm ist der Vorfahr, bei dem die Mutation, die diese Haplogruppe definiert, erstmals aufgetreten ist.

Aufgrund der langsamen Mutationsrate von Y-Chromosomen kann der MRCA viele Hunderte Jahre zurückliegen. Bei seltenen Haplogruppen (d. h. Haplogruppen, für die bisher nur wenige Menschen getestet wurden) können es sogar Tausende von Jahren sein.

Zwischen dem MRCA und der getesteten Person zeigt das Diagramm die väterliche Linie, soweit sie in deinem Stammbaum dokumentiert ist: den Vater, dessen Vater und so weiter, vom ältesten zum jüngsten. Die gepunktete Linie über dem ältesten dokumentierten Vorfahren steht für die nicht dokumentierten Generationen und enthält eine Schätzung ihrer Anzahl. Es werden nur biologische Väter verfolgt – die Linie endet bei einem Adoptiv- oder Stiefvater, da dieser das Y-Chromosom nicht weitergegeben hat. Klicke auf eine Person in der Linie, um ihre Seite zu öffnen.

Das Symbol in jedem Kladenfeld öffnet diese Klade auf der Website von YFull.

## Private Y-DNA-Daten

Die Dialoge zum Hinzufügen und Bearbeiten von Y-DNA-Daten enthalten einen Schalter **Privat**. Private Y-DNA-Daten werden vor Benutzern verborgen, die keine privaten Datensätze anzeigen dürfen. Siehe [Private Datensätze](privacy.md).


## Anweisungen zum Erhalten von SNP-Daten von Testdiensten

### [YSEQ](https://www.yseq.net/)

Nachdem du dich bei „My Account“ angemeldet hast, gehe zu „My Results / View my Alleles“ und navigiere zum unteren Ende der Seite. Das Textfeld „ Allele list compact“ wurde speziell für Gramps Web hinzugefügt und hat genau das richtige Format, um die Daten in das Attribut `Y-DNA` einzufügen.
