# Frontend-Entwicklungsumgebung

Diese Seite beschreibt die erforderlichen Schritte, um mit der Frontend-Entwicklung zu beginnen.

## Voraussetzungen

Für die empfohlene Entwicklungsumgebung wird Visual Studio Code mit Dev-Containern verwendet. Dieser Ansatz erstellt eine vorkonfigurierte Entwicklungsumgebung mit allen benötigten Tools.

Weitere Informationen zu den erforderlichen Voraussetzungen findest du unter [Backend-Entwicklungsumgebung](../backend/setup.md#prerequisites).

## Erste Schritte

1. Öffne das [Gramps-Web-Frontend-Repository](https://github.com/gramps-project/gramps-web) und klicke auf „fork“
2. Klone dein geforktes Repository mithilfe von Git auf deinen lokalen Rechner
3. Öffne das geklonte Repository in Visual Studio Code. Wähle bei entsprechender Aufforderung „Reopen in Container“ aus oder öffne manuell die Befehlspalette (Strg+Umschalt+P oder Cmd+Umschalt+P) und wähle „Dev Containers: Rebuild and Reopen in Container“ aus.
4. Warte, bis der Dev-Container erstellt und gestartet wurde. Dies kann einige Minuten dauern, insbesondere beim ersten Mal.


## Ausführen des Frontend-Entwicklungsservers

Um den Frontend-Entwicklungsserver auszuführen und die Auswirkungen deiner Änderungen im Browser anzuzeigen, kannst du die vordefinierten Aufgaben im Dev-Container verwenden.

Damit dies funktioniert, musst du zunächst eine Instanz des [Gramps-Web-API-Backends](../backend/setup.md#tasks) starten. Am einfachsten geht das, indem du den Backend-Dev-Container verwendest und die Aufgabe [„Serve Web API“ ausführen](../backend/setup.md#tasks) in einem separaten VS-Code-Fenster startest.

Sobald das Backend ausgeführt wird, kannst du den Frontend-Entwicklungsserver starten, indem du in der Befehlspalette (Strg+Umschalt+P oder Cmd+Umschalt+P) „Tasks: Run Task“ auswählst und anschließend „Serve Gramps Web frontend“ wählst.

Dadurch wird der Frontend-Entwicklungsserver auf Port 8001 gestartet. Du kannst ihn in deinem Browser unter `http://localhost:8001` aufrufen. Der Browser wird automatisch neu geladen, wenn du Änderungen am Frontend-Code vornimmst, sodass du die Auswirkungen deiner Änderungen sofort sehen kannst.
