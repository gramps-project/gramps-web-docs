# Frontend-Entwicklungssetup

Diese Seite beschreibt die Schritte, die erforderlich sind, um mit der Frontend-Entwicklung zu beginnen.

## Voraussetzungen

Das empfohlene Entwicklungssetup verwendet Visual Studio Code mit Dev-Containern. Dieser Ansatz erstellt eine vorkonfigurierte Entwicklungsumgebung mit allen benötigten Tools.

Siehe [Backend-Entwicklungssetup](../backend/setup.md#prerequisites) für die erforderlichen Voraussetzungen.

## Erste Schritte

1. Öffnen Sie das [Gramps Web-Frontend-Repository](https://github.com/gramps-project/gramps-web) und klicken Sie auf "fork".
2. Klonen Sie Ihr geforktes Repository auf Ihren lokalen Computer mit Git.
3. Öffnen Sie das geklonte Repository in Visual Studio Code. Wenn Sie dazu aufgefordert werden, wählen Sie "Im Container erneut öffnen" oder öffnen Sie manuell die Befehls-Palette (Ctrl+Shift+P oder Cmd+Shift+P) und wählen Sie "Dev-Container: Neu erstellen und im Container erneut öffnen".
4. Warten Sie, bis der Dev-Container erstellt und gestartet ist. Dies kann einige Minuten dauern, insbesondere beim ersten Mal.

## Ausführen des Frontend-Entwicklungsservers

Um den Frontend-Entwicklungsserver auszuführen und die Auswirkungen Ihrer Änderungen im Browser anzuzeigen, können Sie die vordefinierten Aufgaben im Dev-Container verwenden.

Damit dies funktioniert, müssen Sie zunächst eine Instanz des [Gramps Web API-Backends](../backend/setup.md#tasks) starten. Der einfachste Weg, dies zu tun, ist die Verwendung des Backend-Dev-Containers und [die Aufgabe "Web-API bereitstellen" auszuführen](../backend/setup.md#tasks) in einem separaten VS Code-Fenster.

Sobald das Backend läuft, können Sie den Frontend-Entwicklungsserver starten, indem Sie "Aufgaben: Aufgabe ausführen" aus der Befehls-Palette (Ctrl+Shift+P oder Cmd+Shift+P) auswählen und dann "Gramps Web-Frontend bereitstellen" wählen.

Dies startet den Frontend-Entwicklungsserver auf Port 8001, den Sie in Ihrem Browser unter `http://localhost:8001` erreichen können. Der Browser wird automatisch neu geladen, wenn Sie Änderungen am Frontend-Code vornehmen, sodass Sie die Auswirkungen Ihrer Änderungen sofort sehen können.
