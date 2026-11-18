# Verwendung des KI-Assistenten

Die **Assistent**-Ansicht in Gramps Web (sofern in Ihrer Installation aktiviert) bietet Zugriff auf einen KI-Assistenten, der Fragen zu Ihrem Stammbaum beantwortet.

!!! warning
    Wie bei jedem KI-Assistenten können die Antworten falsch sein. Verwenden Sie die Links in der Antwort, um die Aufzeichnungen zu überprüfen, auf denen sie basieren.

## So funktioniert es

Der Assistent kennt Ihren Baum im Voraus nicht. Um eine Frage zu beantworten, sucht ein großes Sprachmodell die benötigten Aufzeichnungen, ähnlich wie Sie es selbst tun würden:

- es durchsucht den Baum mit der [Volltextsuche](search.md),
- es filtert Personen, Ereignisse und Familien nach Kriterien wie Namen, Daten, Orten oder der Anzahl der Kinder,
- es findet Vorfahren, Nachkommen und andere Verwandte einer Person sowie deren Beziehung,
- es liest vollständige Aufzeichnungen von Personen, Familien, Ereignissen, Orten und Notizen.

Anschließend beantwortet es die Fragen basierend auf den gefundenen Aufzeichnungen und gibt Links zu diesen an. Während es arbeitet, werden die verwendeten Werkzeuge angezeigt, sodass Sie folgen können. Fragen, die länger dauern, laufen im Hintergrund – Sie können weg navigieren und zurückkommen.

Der Assistent antwortet nur auf Basis Ihres Baums, nicht aus dem allgemeinen Wissen des Sprachmodells – selbst über bekannte Personen. Wenn der Baum etwas nicht verzeichnet, sagt er das und erwähnt verwandte Informationen, die er gefunden hat, beispielsweise in einer Notiz. Er sieht nur das, was Sie sehen dürfen: Links zu privaten Aufzeichnungen werden als Klartext für Benutzer angezeigt, die sie nicht einsehen können.

Folgefragen behalten den Kontext früherer Fragen im selben Gespräch, sodass Sie nach einer Frage zu einer Person fragen können: "Und wann ist er gestorben?"

## Was Sie fragen können

- **Fakten über Personen**: "Wann wurde Mary Smith geboren?" oder "Wie heißen die Kinder von John Doe?"
- **Verwandte**: "Wer sind die Großeltern von Jane Smith?" oder "Welche Nachkommen von Johann Meyer sind nach Amerika ausgewandert?"
- **Suchen mit Kriterien**: "Wer wurde nach 1850 in London geboren?", "Liste der Ehen zwischen 1920 und 1950" oder "Welche Paare hatten fünf oder mehr Kinder?"
- **Orte**: "Welche Ereignisse fanden in Paris statt?" oder "Wer wurde in Dänemark geboren?" – Orte innerhalb eines größeren Ortes sind eingeschlossen.
- **Notizen**: "Was sagen die Notizen über den Hof der Familie Meyer?"

Fragen, die den gesamten Baum auf einmal benötigen, wie "Was ist der häufigste Vorname?", funktionieren weniger gut, da der Assistent nur eine begrenzte Anzahl von Aufzeichnungen pro Abfrage sieht.

## Fragen zu Bildern

Wenn der Serveradministrator dies aktiviert hat, hat die Eingabeaufforderung eine Schaltfläche zum Anhängen von Bildern. Sie können auch ein Bild einfügen oder Bilddateien in die Eingabeaufforderung ziehen. Bis zu vier Bilder können einer Frage angehängt werden, zum Beispiel ein Scan eines Kirchenbuchs, um zu fragen: "Wer wird in diesem Eintrag erwähnt, und sind sie in meinem Baum?"

Die Bilder werden nur mit der Frage gesendet, an die sie angehängt sind. Folgefragen können sich auf das beziehen, was der Assistent darüber gesagt hat, jedoch nicht auf die Bilder selbst, sodass Sie sie bei Bedarf erneut anhängen müssen. Wenn Ihr Baum eine Begrenzung für die Nutzung der KI hat, zählt jedes Bild wie eine zusätzliche Frage.

## Den Assistenten Änderungen an Ihrem Baum vornehmen lassen

Wenn der Serveradministrator dies aktiviert hat, können Redakteure, Eigentümer und Administratoren den Assistenten bitten, den Baum zu ändern, zum Beispiel "Fügen Sie eine Taufe am 3. Mai 1802 in St. Mary's zu Johann Meyer hinzu" oder "Korrigieren Sie das Geburtsjahr von Anna Smith, es sollte 1871 sein".

Der Assistent ändert niemals etwas von sich aus. Er antwortet mit einer **Vorgeschlagenen Änderungen**-Karte, die jede Aufzeichnung auflistet, die er hinzufügen, bearbeiten oder löschen würde, wobei die alten Werte durchgestrichen und die neuen Werte hervorgehoben sind. Nichts passiert, bis Sie auf **Übernehmen** klicken. Die Änderungen werden dann in einem Schritt vorgenommen, den Sie wie jede andere Bearbeitung rückgängig machen können, aus der Nachricht, die erscheint, oder in der [Versionsgeschichte](revisions.md).

Überprüfen Sie einen Vorschlag sorgfältig, bevor Sie ihn anwenden – insbesondere, dass der Assistent die richtige Person ausgewählt hat und dass er keinen neuen Datensatz (wie einen Ort oder eine Quelle) hinzugefügt hat, der bereits in Ihrem Baum unter einem leicht anderen Namen existiert. Wenn ein Vorschlag nicht ganz richtig ist, sagen Sie, was geändert werden soll, und der Assistent schlägt erneut vor.

Sobald ein Vorschlag angewendet wurde, können ältere Vorschläge im selben Gespräch nicht mehr angewendet werden, da sie für den Baum gemacht wurden, wie er zuvor war. Dasselbe passiert, wenn einer der betroffenen Datensätze inzwischen geändert wurde.

## Tipps zum Stellen von Fragen

- **Nennen Sie die Personen.** Der Assistent weiß nicht, wer Sie sind oder wer Ihre Hauptperson ist, also fragen Sie statt "meiner Großmutter" nach "der Großmutter von Anna Smith (geboren 1950)". Sie können auch Gramps-IDs verwenden, z.B. "die Kinder von I0042".
- **Seien Sie spezifisch**, wenn Namen häufig sind: "Wann hat der John Smith, der 1850 in Boston geboren wurde, geheiratet?" ist besser als "Wann hat John Smith geheiratet?"
- **Verwenden Sie Ihre Sprache.** Sie können in Ihrer eigenen Sprache fragen und Antworten in derselben Sprache erhalten.
- **Fragen Sie anders erneut**, wenn eine Antwort unvollständig aussieht – zum Beispiel, indem Sie den Ort oder den Zeitraum nennen, an dem Sie interessiert sind.

!!! tip
    Bitte teilen Sie Ihre Erfahrungen über Dinge, die funktionieren und nicht funktionieren, mit der Gemeinschaft.
