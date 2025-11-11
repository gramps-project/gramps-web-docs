# Verwendung von Gramps Web für Y-DNA-Analyse

!!! note "Hinweis"
    Diese Funktion erfordert die Gramps Web API-Version 3.3.0 oder höher und die Gramps Web-Frontend-Version 25.9.0 oder höher.

Die Y-DNA-Ansicht in Gramps Web kann rohe Y-Chromosom-Einzel-Nukleotid-Polymorphismus (SNP)-Daten verwenden, um die wahrscheinlichste Y-DNA-Haplogruppe einer Person zu bestimmen und die abgeleiteten Vorfahren im menschlichen Y-Chromosomenbaum zusammen mit Zeitabschätzungen anzuzeigen.

## So erhalten und speichern Sie die Y-DNA-SNP-Daten

Um die Y-DNA-SNP-Daten zu erhalten, müssen Sie einen Y-DNA-Test über einen genetischen Testdienst durchführen lassen. Das Ergebnis wird als eine Menge von Mutationen (SNPs) dargestellt, die jeweils durch eine Zeichenfolge (z. B. `R-BY44535`) und ein `+` oder `-` Zeichen gekennzeichnet sind, das angibt, ob die Mutation vorhanden oder abwesend ist. Gramps Web erwartet die Zeichenfolge aller getesteten SNPs im Format `SNP1+, SNP2-, SNP3+,...`, die in einem Personenattribut des benutzerdefinierten Typs `Y-DNA` (groß- und kleinschreibungssensitiv) gespeichert wird. Sie können dieses Attribut entweder manuell in Gramps Web oder Gramps Desktop erstellen oder zur Y-DNA-Ansicht in Gramps Web navigieren, auf die blaue Schaltfläche "Hinzufügen" klicken, die Person auswählen, zu der die Daten hinzugefügt werden sollen, und die SNP-Zeichenfolge einfügen. In jedem Fall werden die Daten als Personenattribut in Ihrer Gramps-Datenbank gespeichert.

[Siehe unten](#instructions-for-obtaining-snp-data-from-testing-services) für Anweisungen, wie Sie die SNP-Daten von verschiedenen Testdiensten erhalten können.

## So funktioniert es

Sobald eine Person ein `Y-DNA`-Attribut mit den SNP-Daten hat, verwendet Gramps Web die Open-Source [yclade](https://github.com/DavidMStraub/yclade) Python-Bibliothek, um die wahrscheinlichste Position der Person im menschlichen Y-Chromosomenbaum zu bestimmen. Der Baum wurde vom [YFull](https://www.yfull.com/) Projekt auf der Grundlage von Zehntausenden von Y-DNA-Tests erstellt. Beachten Sie, dass Gramps Web eine lokale Kopie des YFull-Baums verwendet, sodass keine Daten an Dritte gesendet werden.

Der Baum wird von der Wurzel zu den Blättern durchquert, und an jedem Knoten werden die SNPs, die mit diesem Knoten verbunden sind, mit den positiv und negativ getesteten SNPs der Person verglichen, und der entsprechende Zweig wird verfolgt.

Das Endergebnis ist eine Abfolge von Kladen von der Wurzel des Baums (dem [Y-chromosomalen "Adam"](https://en.wikipedia.org/wiki/Y-chromosomal_Adam)) bis zur am weitesten abgeleiteten Klade, die mit den SNP-Daten der Person übereinstimmt. Jede Klade hat ein geschätztes Alter, basierend auf den Altersdaten der Proben in der YFull-Datenbank, die zu dieser Klade gehören.

Da Y-Chromosomen von Vater zu Sohn vererbt werden, entspricht diese Abfolge einem Auszug aus der patrilinearen Abstammung der Person.

## So interpretieren Sie die Ergebnisse

Das wichtigste Informationsstück ist die wahrscheinlichste Haplogruppe der Person, die oben auf der Seite angezeigt wird. Der Name ist mit der entsprechenden Seite auf der [YFull](https://www.yfull.com/) Website verlinkt, die weitere Informationen enthält, wie z. B. das Herkunftsland der getesteten Proben, die zu dieser Haplogruppe gehören.

Im patrilinearen Ahnenbaum, der in Gramps Web angezeigt wird, ist das Feld direkt über der getesteten Person der letzte gemeinsame Vorfahr (MRCA) aller getesteten Proben, die zu der Haplogruppe der Person gehören. Das Datum, das für diesen Vorfahren angezeigt wird, ist sein geschätztes ungefähres Geburtsdatum. Der Vorfahr über ihm ist der Vorfahr, bei dem die Mutation, die diese Haplogruppe definiert, erstmals auftrat.

Aufgrund der langsamen Mutationsrate von Y-Chromosomen kann der MRCA viele Hunderte von Jahren in der Vergangenheit liegen. Bei seltenen Haplogruppen (d. h. Haplogruppen, bei denen bisher nur wenige Personen getestet wurden) kann es sogar Tausende von Jahren sein.

## Anweisungen zum Abrufen von SNP-Daten von Testdiensten

### [YSEQ](https://www.yseq.net/)

Sobald Sie sich bei "Mein Konto" angemeldet haben, gehen Sie zu "Meine Ergebnisse / Meine Allele anzeigen" und navigieren Sie zum Ende der Seite. Das Textfeld "Allele-Liste kompakt" wurde speziell für Gramps Web hinzugefügt und ist genau im richtigen Format, um in das `Y-DNA`-Attribut eingefügt zu werden.
