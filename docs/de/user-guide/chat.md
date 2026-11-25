# Den KI-Assistenten verwenden

Die Ansicht **Assistent** in Gramps Web (falls sie in deiner Installation aktiviert ist) bietet Zugriff auf einen KI-Assistenten, der Fragen zu deinem Stammbaum beantwortet.

!!! warning
    Wie bei jedem KI-Assistenten können Antworten falsch sein. Verwende die Links in der Antwort, um die Datensätze zu überprüfen, auf denen sie basiert.

## Funktionsweise

Der Assistent kennt deinen Stammbaum nicht im Voraus. Um eine Frage zu beantworten, sucht ein großes Sprachmodell die benötigten Datensätze heraus, ähnlich wie du selbst:

- es durchsucht den Stammbaum mit der [Volltextsuche](search.md),
- es filtert Personen, Ereignisse und Familien nach Kriterien wie Namen, Daten, Orten oder der Anzahl der Kinder,
- es findet Vorfahren, Nachkommen und andere Verwandte einer Person sowie deren Verwandtschaftsbeziehung,
- es liest vollständige Datensätze von Personen, Familien, Ereignissen, Orten und Notizen.

Anschließend beantwortet es die Frage anhand der gefundenen Datensätze und fügt Links zu ihnen hinzu. Während der Bearbeitung werden die verwendeten Werkzeuge angezeigt, sodass du den Vorgang verfolgen kannst. Fragen, deren Beantwortung länger dauert, werden im Hintergrund ausgeführt – du kannst zu einer anderen Ansicht wechseln und später zurückkehren.

Der Assistent antwortet ausschließlich anhand deines Stammbaums und nicht anhand des Allgemeinwissens des Sprachmodells – auch nicht bei bekannten Personen. Wenn im Stammbaum etwas nicht erfasst ist, weist er darauf hin und nennt verwandte Informationen, die er beispielsweise in einer Notiz gefunden hat. Er sieht nur, was du sehen darfst: Links zu privaten Datensätzen werden für Benutzer, die sie nicht anzeigen dürfen, als einfacher Text dargestellt.

Nachfragen behalten den Kontext früherer Fragen in derselben Unterhaltung bei. Du kannst also nach einer Frage zu einer Person fragen: „Und wann ist er gestorben?“

## Was du fragen kannst

- **Fakten zu Personen**: „Wann wurde Mary Smith geboren?“ oder „Wie heißen die Kinder von John Doe?“
- **Verwandte**: „Wer sind die Großeltern von Jane Smith?“ oder „Welche Nachkommen von Johann Meyer sind nach Amerika ausgewandert?“
- **Suchen mit Kriterien**: „Wer wurde nach 1850 in London geboren?“, „Liste die Eheschließungen zwischen 1920 und 1950 auf“ oder „Welche Paare hatten fünf oder mehr Kinder?“
- **Orte**: „Welche Ereignisse fanden in Paris statt?“ oder „Wer wurde in Dänemark geboren?“ – Orte innerhalb eines größeren Ortes werden einbezogen.
- **Notizen**: „Was sagen die Notizen über den Bauernhof der Familie Meyer aus?“

Fragen, die den gesamten Stammbaum auf einmal benötigen, wie „Was ist der häufigste Vorname?“, funktionieren weniger gut, da der Assistent pro Suche nur eine begrenzte Anzahl von Datensätzen sieht.

## Fragen zu Bildern stellen

Wenn der Serveradministrator dies aktiviert hat, enthält das Eingabefeld eine Schaltfläche zum Anhängen von Bildern. Du kannst auch ein Bild einfügen oder Bilddateien auf das Eingabefeld ziehen. An eine Frage können bis zu vier Bilder angehängt werden, beispielsweise ein Scan eines Kirchenbuchs, um zu fragen: „Wer wird in diesem Eintrag erwähnt und befindet sich die Person in meinem Stammbaum?“

Die Bilder werden nur zusammen mit der Frage gesendet, an die sie angehängt sind. Nachfragen können sich auf die Aussagen des Assistenten zu den Bildern beziehen, nicht jedoch auf die Bilder selbst. Hänge sie daher bei Bedarf erneut an. Wenn dein Stammbaum eine Beschränkung für die KI-Nutzung hat, zählt jedes Bild wie eine zusätzliche Frage.

## Den Assistenten Änderungen an deinem Stammbaum vornehmen lassen

Wenn der Serveradministrator dies aktiviert hat, können Bearbeiter, Eigentümer und Administratoren den Assistenten auffordern, den Stammbaum zu ändern, beispielsweise mit „Füge für Johann Meyer eine Taufe am 3. Mai 1802 in St. Mary's hinzu“ oder „Korrigiere das Geburtsjahr von Anna Smith, es sollte 1871 sein“.

Der Assistent nimmt niemals selbstständig Änderungen vor. Er antwortet mit einer Karte **Vorgeschlagene Änderungen**, in der jeder Datensatz aufgeführt ist, den er hinzufügen, bearbeiten oder löschen würde. Die alten Werte sind durchgestrichen und die neuen Werte hervorgehoben. Es geschieht nichts, bis du auf **Anwenden** klickst. Die Änderungen werden dann in einem Schritt vorgenommen. Du kannst sie wie jede andere Bearbeitung rückgängig machen – entweder über die daraufhin angezeigte Nachricht oder in der [Änderungshistorie](revisions.md).

Prüfe einen Vorschlag sorgfältig, bevor du ihn anwendest – insbesondere, ob der Assistent die richtige Person ausgewählt hat und ob er keinen neuen Datensatz (beispielsweise einen Ort oder eine Quelle) hinzugefügt hat, der bereits unter einem leicht abweichenden Namen in deinem Stammbaum existiert. Wenn ein Vorschlag nicht ganz richtig ist, teile dem Assistenten mit, was geändert werden soll, und er erstellt einen neuen Vorschlag.

Sobald ein Vorschlag angewendet wurde, können ältere Vorschläge in derselben Unterhaltung nicht mehr angewendet werden, da sie für den Stand des Stammbaums erstellt wurden, der davor bestand. Dasselbe geschieht, wenn einer der betroffenen Datensätze inzwischen geändert wurde.

## Tipps zum Stellen von Fragen

- **Nenne die Personen.** Der Assistent weiß nicht, wer du bist oder wer deine Hauptperson ist. Frage daher statt nach „meiner Großmutter“ beispielsweise nach „der Großmutter von Anna Smith (geboren 1950)“. Du kannst auch Gramps-IDs verwenden, z. B. „die Kinder von I0042“.
- **Sei bei häufigen Namen genau**: „Wann hat der 1850 in Boston geborene John Smith geheiratet?“ ist besser als „Wann hat John Smith geheiratet?“
- **Verwende deine Sprache.** Du kannst in deiner eigenen Sprache fragen und erhältst die Antworten in derselben Sprache.
- **Frage auf andere Weise erneut**, wenn eine Antwort unvollständig wirkt – beispielsweise indem du den Ort oder den Zeitraum nennst, für den du dich interessierst.

!!! tip
    Bitte teile deine Erfahrungen zu Dingen, die mit der Community funktionieren oder nicht funktionieren.
