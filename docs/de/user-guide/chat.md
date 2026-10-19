# Verwendung des KI-Assistenten

!!! info
    Der KI-Assistent erfordert die Gramps Web API-Version 2.5.0 oder höher und die Gramps Web-Version 24.10.0 oder höher. Die Gramps Web API-Version 3.6.0 führte Funktionen zum Aufrufen von Tools für intelligentere Interaktionen ein.

Die **Assistent**-Ansicht in Gramps Web (sofern in Ihrer Installation verfügbar, in älteren Versionen als "Chat" bezeichnet) bietet Zugang zu einem KI-Assistenten, der Fragen zu Ihrem Stammbaum beantworten kann.

!!! warning
    Da dies noch eine neue und sich entwickelnde Funktion ist, funktionieren einige Arten von Fragen gut, während andere es nicht tun. Außerdem kann der KI-Assistent, wie bei jedem KI-Assistenten, faktisch falsche Antworten geben, daher sollten Sie immer doppelt überprüfen.

## Wie es funktioniert

Um zu verstehen, welche Arten von Fragen der Assistent beantworten kann, ist es hilfreich zu verstehen, wie er im Hintergrund funktioniert:

1. Der Benutzer stellt eine Frage.
2. Der Assistent fragt direkt Ihre Datenbank mit spezialisierten Tools ab: Er durchsucht den Stammbaum mit der [Volltextsuche](search.md), filtert Personen/Ereignisse/Familien/Orte nach bestimmten Kriterien, berechnet Beziehungen zwischen Individuen und sucht vollständige Datensätze, einschließlich ihrer Notizen.
3. Ein großes Sprachmodell formuliert eine Antwort basierend auf den gefundenen Datensätzen.
4. Die Antwort wird Ihnen angezeigt, mit Links zu den Datensätzen, auf denen sie basiert.

Auf Servern, die eine Gramps Web API-Version älter als 3.24 ausführen, stützte sich der Assistent auch auf semantische Suche, die schrittweise eingestellt wird.

Während der Assistent arbeitet, zeigen Indikatoren an, welche Tools er derzeit verwendet (z. B. Personen suchen, Beziehungen nachschlagen), sodass Sie ihm folgen können, während er seine Antwort erstellt. Länger laufende Fragen werden als Hintergrundaufgaben verarbeitet – Sie können navigieren und zurückkommen, und der Fortschritt wird auch in [Benachrichtigungen](notifications.md) angezeigt. Antworten sind im Markdown-Format (Listen, Hervorhebungen, Links usw.) formatiert, um das Lesen zu erleichtern.

## Was Sie fragen können

Mit den in der Gramps Web API-Version 3.6.0 eingeführten Funktionen zum Aufrufen von Tools kann der KI-Assistent jetzt komplexere Fragen bearbeiten:

- **Familienbeziehungen**: "Wer sind die Großeltern von Jane Smith?" oder "Wie ist John Doe mit Mary Johnson verwandt?"
- **Gefilterte Suchen**: "Zeige mir alle Personen, die nach 1850 in London geboren wurden" oder "Welche Ereignisse fanden in Paris statt?"
- **Datumsbasierte Abfragen**: "Wer starb vor 1900?" oder "Liste der Ehen, die zwischen 1920 und 1950 stattfanden"
- **Ortsinformationen**: "Welche Orte gibt es in Frankreich?" oder "Erzählen Sie mir von der St. Mary's Church"
- **Allgemeine Fragen**: "Wie heißen die Kinder von John Doe?" oder "Wann wurde Mary Smith geboren?"

## Tipps zum Stellen von Fragen

Um die besten Ergebnisse vom KI-Assistenten zu erhalten:

- **Seien Sie spezifisch**: Formulieren Sie Ihre Frage mit so vielen Details wie möglich, um Mehrdeutigkeiten zu vermeiden. Zum Beispiel ist "Wann hat John Smith, geboren 1850 in Boston, geheiratet?" besser als "Wann hat John Smith geheiratet?"
- **Verwenden Sie Eigennamen**: Nennen Sie spezifische Namen, Orte und Daten, wenn relevant.
- **Fragen Sie eine Sache auf einmal**: Zerlegen Sie komplexe Fragen in einfachere Teile für bessere Ergebnisse.
- **Verwenden Sie Ihre Sprache**: Große Sprachmodelle sind mehrsprachig, sodass Sie Fragen in Ihrer eigenen Sprache stellen und Antworten in derselben Sprache erhalten können.

!!! tip
    Bitte teilen Sie Ihre Erfahrungen über Dinge, die funktionieren und nicht funktionieren, mit der Community.
