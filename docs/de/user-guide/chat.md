# Verwendung von KI-Chat

!!! info
    Der KI-Chat erfordert die Gramps Web API-Version 2.5.0 oder höher und die Gramps Web-Version 24.10.0 oder höher. Die Gramps Web API-Version 3.6.0 führte Funktionen zum Aufrufen von Tools für intelligentere Interaktionen ein.



Die Chatansicht in Gramps Web (sofern in Ihrer Installation verfügbar) bietet Zugriff auf einen KI-Assistenten, der Fragen zu Ihrem Stammbaum beantworten kann.

!!! warning
    Da dies noch eine neue und sich entwickelnde Funktion ist, funktionieren einige Arten von Fragen gut, während andere es nicht tun. Außerdem kann der KI-Assistent, wie bei jedem KI-Assistenten, faktisch falsche Antworten geben, daher sollten Sie immer eine doppelte Überprüfung vornehmen.

## Wie es funktioniert

Um zu verstehen, welche Arten von Fragen der Assistent beantworten kann, ist es hilfreich zu verstehen, wie es im Hintergrund funktioniert:

1. Der Benutzer stellt eine Frage.
2. Der KI-Assistent kann mehrere Ansätze verwenden, um Antworten zu finden:
   - **Semantische Suche**: Gramps Web identifiziert Objekte in Ihrem Stammbaum, die wahrscheinlich relevante Informationen enthalten. Wenn Sie beispielsweise fragen: "Wie heißen die Kinder von John Doe?", werden Familien mit John Doe als Vater unter den besten Ergebnissen sein.
   - **Toolaufruf (Gramps Web API v3.6.0+)**: Der Assistent kann Ihre Datenbank direkt mit spezialisierten Tools abfragen, um Personen/Ereignisse/Familien/Orte nach bestimmten Kriterien zu suchen und zu filtern, Beziehungen zwischen Individuen zu berechnen und detaillierte Informationen abzurufen.
3. Gramps Web übermittelt die Frage zusammen mit den abgerufenen Informationen an ein großes Sprachmodell, um eine Antwort zu formulieren.
4. Die Antwort wird Ihnen angezeigt.

## Was Sie fragen können

Mit den Funktionen zum Aufrufen von Tools, die in der Gramps Web API-Version 3.6.0 eingeführt wurden, kann der KI-Assistent nun komplexere Fragen bearbeiten:

- **Familienbeziehungen**: "Wer sind die Großeltern von Jane Smith?" oder "Wie ist John Doe mit Mary Johnson verwandt?"
- **Gefilterte Suchen**: "Zeige mir alle Personen, die nach 1850 in London geboren wurden" oder "Welche Ereignisse fanden in Paris statt?"
- **Datumsbasierte Abfragen**: "Wer starb vor 1900?" oder "Liste die Ehen auf, die zwischen 1920 und 1950 stattfanden"
- **Ortsinformationen**: "Welche Orte gibt es in Frankreich?" oder "Erzähle mir von der St. Mary's Church"
- **Allgemeine Fragen**: "Wie heißen die Kinder von John Doe?" oder "Wann wurde Mary Smith geboren?"

## Tipps zum Stellen von Fragen

Um die besten Ergebnisse vom KI-Assistenten zu erhalten:

- **Seien Sie spezifisch**: Formulieren Sie Ihre Frage mit so vielen Details wie möglich, um Mehrdeutigkeiten zu vermeiden. Zum Beispiel ist "Wann heiratete John Smith, der 1850 in Boston geboren wurde?" besser als "Wann heiratete John Smith?"
- **Verwenden Sie richtige Namen**: Nennen Sie spezifische Namen, Orte und Daten, wenn relevant.
- **Fragen Sie eine Sache auf einmal**: Zerlegen Sie komplexe Fragen in einfachere Teile für bessere Ergebnisse.
- **Verwenden Sie Ihre Sprache**: Große Sprachmodelle sind mehrsprachig, sodass Sie Fragen in Ihrer eigenen Sprache stellen und Antworten in derselben Sprache erhalten können.

!!! tip
    Bitte teilen Sie Ihre Erfahrungen über Dinge, die funktionieren und nicht funktionieren, mit der Community.
