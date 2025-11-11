# Verwendung von KI-Chat

!!! info
    Der KI-Chat erfordert die Gramps Web API-Version 2.5.0 oder höher und die Gramps Web-Version 24.10.0 oder höher.


Die Chatansicht in Gramps Web (sofern in Ihrer Installation verfügbar) bietet Zugriff auf einen KI-Assistenten, der Fragen zu Ihrem Stammbaum beantworten kann.

!!! warning
    Da dies noch eine neue und sich entwickelnde Funktion ist, funktionieren einige Arten von Fragen gut, während andere es nicht tun. Außerdem kann der KI-Assistent, wie bei jedem KI-Tool, faktisch falsche Antworten geben, daher sollten Sie immer eine doppelte Überprüfung vornehmen.

## Wie es funktioniert

Um zu verstehen, welche Arten von Fragen der Assistent beantworten kann, ist es hilfreich zu verstehen, wie es im Hintergrund funktioniert:

1. Der Benutzer stellt eine Frage.
2. Gramps Web identifiziert eine Anzahl von (z. B. zehn) Gramps-Objekten, die höchstwahrscheinlich die Informationen enthalten, die die Frage beantworten. Zu diesem Zweck verwendet es eine Technik namens "semantische Suche". Wenn Sie beispielsweise fragen "Wie heißen die Kinder von John Doe?", und eine Familie mit John Doe als Vater existiert, wird sie wahrscheinlich unter den obersten Ergebnissen sein.
3. Gramps Web übergibt die Benutzerfrage zusammen mit den abgerufenen Kontextinformationen an ein großes Sprachmodell ("Chatbot") und bittet es, die richtige Antwort zu extrahieren.
4. Die Antwort wird dem Benutzer angezeigt.

## Wie man eine Frage stellt

Aufgrund der Funktionsweise des Chats ist es (derzeit) nicht möglich, dass der KI-Assistent Fragen zu spezifischen Beziehungen außer Eltern oder Kindern beantwortet, es sei denn, diese Informationen sind als Text in einer Notiz enthalten.

Da jede Antwort auf einer begrenzten Anzahl von obersten Ergebnissen der semantischen Suche basiert, kann sie auch keine Fragen zu Statistiken beantworten ("Wie viele Personen in meiner Datenbank ...").

Um Mehrdeutigkeiten und Missverständnisse zu vermeiden, ist es hilfreich, die Frage so detailliert wie möglich zu formulieren.

Beachten Sie, dass große Sprachmodelle mehrsprachig sind, sodass Sie in Ihrer eigenen Sprache mit ihm sprechen können und es in derselben Sprache antwortet.

!!! tip
    Bitte teilen Sie Ihre Erfahrungen über Dinge, die funktionieren und nicht funktionieren, mit der Community.
