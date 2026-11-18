# Verwendung von Gramps Web für Y-DNA-Analyse

!!! note "Hinweis"
    Diese Funktion erfordert Gramps Web API Version 3.3.0 oder höher und Gramps Web Frontend Version 25.9.0 oder höher.

Die Y-DNA-Ansicht in Gramps Web kann rohe Y-Chromosom-Einzel-Nukleotid-Polymorphismus (SNP) Daten verwenden, um die wahrscheinlichste Y-DNA-Haplogruppe einer Person zu bestimmen und die abgeleiteten Vorfahren im menschlichen Y-Chromosomenbaum zusammen mit Zeitabschätzungen anzuzeigen.

## So erhalten und speichern Sie die Y-DNA-SNP-Daten

Um die Y-DNA-SNP-Daten zu erhalten, müssen Sie einen Y-DNA-Test über einen genetischen Testdienst durchführen lassen. Das Ergebnis wird als eine Menge von Mutationen (SNPs) dargestellt, die jeweils durch eine Zeichenfolge (z. B. `R-BY44535`) und ein `+` oder `-` Zeichen gekennzeichnet sind, das angibt, ob die Mutation vorhanden oder abwesend ist. Gramps Web erwartet die Zeichenfolge aller getesteten SNPs im Format `SNP1+, SNP2-, SNP3+,...`, die in einem Personenattribut des benutzerdefinierten Typs `Y-DNA` (groß- und kleinschreibungsempfindlich) gespeichert wird. Sie können dieses Attribut entweder manuell in Gramps Web oder Gramps Desktop erstellen oder zur Y-DNA-Ansicht in Gramps Web navigieren und auf die blaue Schaltfläche "Hinzufügen" klicken, die Person auswählen, zu der die Daten hinzugefügt werden sollen, und die SNP-Zeichenfolge einfügen. In jedem Fall werden die Daten als Personenattribut in Ihrer Gramps-Datenbank gespeichert.

[Siehe unten](#anweisungen-zum-erhalten-von-snp-daten-von-testdiensten) für Anweisungen, wie Sie die SNP-Daten von verschiedenen Testdiensten erhalten können.

## So funktioniert es

Sobald eine Person ein `Y-DNA`-Attribut mit den SNP-Daten hat, verwendet Gramps Web die Open-Source [yclade](https://github.com/DavidMStraub/yclade) Python-Bibliothek, um die wahrscheinlichste Position der Person im menschlichen Y-Chromosomenbaum zu bestimmen. Der Baum wurde vom [YFull](https://www.yfull.com/) Projekt basierend auf Zehntausenden von Y-DNA-Tests erstellt. Beachten Sie, dass Gramps Web eine lokale Kopie des YFull-Baums verwendet, sodass keine Daten an Dritte gesendet werden.

Der Baum wird von der Wurzel zu den Blättern durchquert, und an jedem Knoten werden die mit diesem Knoten verbundenen SNPs mit den positiv und negativ getesteten SNPs der Person verglichen, und der entsprechende Zweig wird verfolgt.

Das Endergebnis ist eine Abfolge von Kladen von der Wurzel des Baumes (dem [Y-chromosomalen "Adam"](https://de.wikipedia.org/wiki/Y-chromosomaler_Adam)) bis zur am weitesten abgeleiteten Klade, die mit den SNP-Daten der Person übereinstimmt. Jede Klade hat ein geschätztes Alter, das auf den Altersangaben der Proben in der YFull-Datenbank basiert, die zu dieser Klade gehören.

Da Y-Chromosomen von Vater zu Sohn vererbt werden, entspricht diese Abfolge einem Auszug aus der patrilinearen Abstammung der Person.

## So interpretieren Sie die Ergebnisse

Das wichtigste Stück Information ist die wahrscheinlichste Haplogruppe der Person, die oben auf der Seite angezeigt wird. Der Name ist mit der entsprechenden Seite auf der [YFull](https://www.yfull.com/) Website verlinkt, die weitere Informationen enthält, wie z. B. das Herkunftsland der getesteten Proben, die zu dieser Haplogruppe gehören.

Im patrilinearen Ahnenbaum, der in Gramps Web angezeigt wird, ist das Feld direkt über der getesteten Person der letzte gemeinsame Vorfahr (MRCA) aller getesteten Proben, die zu der Haplogruppe der Person gehören. Das Datum, das für diesen Vorfahren angezeigt wird, ist sein geschätztes ungefähres Geburtsdatum. Der Vorfahr über ihm ist der Vorfahr, bei dem die Mutation, die diese Haplogruppe definiert, erstmals auftrat.

Aufgrund der langsamen Mutationsrate von Y-Chromosomen kann der MRCA viele Hundert Jahre in der Vergangenheit liegen. Bei seltenen Haplogruppen (d. h. Haplogruppen, bei denen bisher nur wenige Personen getestet wurden) kann es sogar Tausende von Jahren sein.

Zwischen dem MRCA und der getesteten Person zeigt das Diagramm die väterliche Linie, soweit sie in Ihrem Baum dokumentiert ist: den Vater, seinen Vater und so weiter, der älteste zuerst. Die gestrichelte Linie über dem ältesten dokumentierten Vorfahren steht für die Generationen, die nicht dokumentiert sind, mit einer Schätzung ihrer Anzahl. Nur biologische Väter werden verfolgt – die Linie endet bei einem Adoptivvater oder Stiefvater, da sie das Y-Chromosom nicht weitergegeben haben. Klicken Sie auf eine Person in der Linie, um ihre Seite zu öffnen.

Das Symbol auf jedem Kladenfeld öffnet diese Klade auf der YFull-Website.

## Private Y-DNA-Daten

Die Dialoge zum Hinzufügen und Bearbeiten von Y-DNA-Daten haben einen **Privat**-Schalter. Private Y-DNA-Daten sind für Benutzer, die keine privaten Datensätze einsehen können, verborgen. Siehe [Private Datensätze](privacy.md).

## Anweisungen zum Erhalten von SNP-Daten von Testdiensten

### [YSEQ](https://www.yseq.net/)

Sobald Sie sich bei "Mein Konto" angemeldet haben, gehen Sie zu "Meine Ergebnisse / Meine Allele anzeigen" und navigieren Sie zum Ende der Seite. Das Textfeld "Allelliste kompakt" wurde speziell für Gramps Web hinzugefügt und ist genau im richtigen Format, um in das `Y-DNA`-Attribut eingefügt zu werden.
