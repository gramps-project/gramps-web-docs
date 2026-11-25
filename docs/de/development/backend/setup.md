# Backend-Entwicklungsumgebung

Diese Seite listet die Schritte auf, die erforderlich sind, um mit der Entwicklung der [Gramps Web API](https://github.com/gramps-project/gramps-web-api), des Backends (Serverkomponente) von Gramps Web, zu beginnen.


## Voraussetzungen

Die empfohlene Entwicklungsumgebung verwendet Visual Studio Code mit Dev-Containern. Dieser Ansatz erstellt eine vorkonfigurierte Entwicklungsumgebung mit allen benötigten Tools. Für den Einstieg benötigst du Folgendes:

- [Docker](https://docs.docker.com/get-docker/)
- [Visual Studio Code](https://code.visualstudio.com/) mit installierter [Dev-Containers-Erweiterung](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers)
- [Git](https://git-scm.com)

Du kannst Linux, macOS oder Windows als Betriebssystem verwenden.


## Erste Schritte

1. Öffne das [Gramps-Web-API-Repository](https://github.com/gramps-project/gramps-web-api) und klicke auf „fork“
2. Klone dein geforktes Repository mit Git auf deinen lokalen Rechner
3. Öffne das geklonte Repository in Visual Studio Code. Wähle bei entsprechender Aufforderung „Reopen in Container“ aus oder öffne manuell die Befehlspalette (Ctrl+Shift+P oder Cmd+Shift+P) und wähle „Dev Containers: Rebuild and Reopen in Container“ aus.
4. Warte, bis der Dev-Container erstellt und gestartet wurde. Dies kann einige Minuten dauern, insbesondere beim ersten Mal.

    **Nach erfolgreichem Erstellen des Dev-Containers wird der folgende Befehl ausgegeben:**

    `Successfully installed gramps-webapi-x.x.x.`

    !!! info
        So erstellst du den Container in Visual Studio Code neu:

        - Wenn du dich im Container befindest, verwende den Palettenbefehl „Rebuild in container“.

        - Wenn du dich in der Ordneransicht befindest (d. h. nicht im Container), verwende den Palettenbefehl „Rebuild and Reopen in Container“.

## Aufgaben

Wenn du nur den Backend-Code änderst, musst du nicht unbedingt einen Webserver starten – bei Unit-Tests wird ein Flask-Testclient verwendet, mit dem sich Anfragen an die API simulieren lassen, ohne dass ein laufender Server erforderlich ist.

Das Ausführen eines Servers ist jedoch hilfreich, wenn du

- deine Änderungen mit echten HTTP-Anfragen ausprobieren möchtest (siehe [manuelle Abfragen](queries.md)), 
- die Auswirkungen von Änderungen auf die vollständige Gramps-Web-Anwendung überprüfen möchtest oder
- gleichzeitig Änderungen am Frontend vornehmen möchtest (siehe [Frontend-Entwicklungsumgebung](../frontend/setup.md)).

Das Ausführen des Servers wird im Dev-Container durch vordefinierte Aufgaben vereinfacht. Du kannst diese Aufgaben über die Befehlspalette (Ctrl+Shift+P oder Cmd+Shift+P) ausführen, indem du „Tasks: Run Task“ auswählst und anschließend eine der folgenden Aufgaben auswählst:
- „Serve Web API“ – startet den Flask-Entwicklungsserver auf Port 5555 mit aktivierter Debug-Protokollierung
- „Start Celery worker“ – startet einen Celery-Worker zur Verarbeitung von Hintergrundaufgaben.


## Debugging

Das Debuggen kann manchmal herausfordernd sein, insbesondere beim Nachverfolgen komplexer Abläufe oder beim Erkennen schwer zu ermittelnder Probleme. Um dies zu erleichtern, kannst du sowohl eine laufende API-Instanz als auch einzelne Testfälle direkt in Visual Studio Code debuggen.

### Debuggen der Gramps Web API

So debuggst du die laufende API:

1. Öffne Visual Studio Code und wechsle zur Ansicht **Run and Debug**.  
2. Wähle im Dropdown-Menü die Konfiguration **„Web API“** aus.  
3. Starte das Debugging.  
4. Wenn du Anfragen an das Backend sendest (entweder manuell oder über die Gramps-Web-GUI), wird die Ausführung an allen Breakpoints angehalten, die du im Code gesetzt hast.  
   Dadurch kannst du Variablen, den Kontrollfluss und andere Laufzeitdetails untersuchen.

### Debuggen von Testfällen

So debuggst du einen bestimmten Testfall:

1. Öffne die Testdatei, die du debuggen möchtest (zum Beispiel `test_people.py`).  
2. Öffne in Visual Studio Code die Ansicht **Run and Debug**.  
3. Wähle die Konfiguration **„Current Test File“** aus.  
4. Starte das Debugging – die Ausführung wird an allen Breakpoints angehalten, die in dieser Testdatei gesetzt wurden.  

Mit dieser Einrichtung kannst du die Testlogik schrittweise durchlaufen, Variablenwerte untersuchen und Testfehler oder unerwartete Ergebnisse besser verstehen.
