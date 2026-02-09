# Backend-Entwicklungssetup

Diese Seite listet die Schritte auf, die erforderlich sind, um mit der Entwicklung der [Gramps Web API](https://github.com/gramps-project/gramps-web-api/), dem Backend (Serverkomponente) von Gramps Web, zu beginnen.


## Voraussetzungen

Das empfohlene Entwicklungssetup verwendet Visual Studio Code mit Dev-Containern. Dieser Ansatz erstellt eine vorkonfigurierte Entwicklungsumgebung mit allen benötigten Tools. Um zu beginnen, benötigen Sie die folgenden Zutaten:

- [Docker](https://docs.docker.com/get-docker/)
- [Visual Studio Code](https://code.visualstudio.com/) mit der installierten [Dev Containers-Erweiterung](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers)
- [Git](https://git-scm.com)

Sie können Linux, macOS oder Windows als Betriebssystem verwenden.


## Erste Schritte

1. Öffnen Sie das [Gramps Web API-Repository](https://github.com/gramps-project/gramps-web-api) und klicken Sie auf "fork".
2. Klonen Sie Ihr geforktes Repository auf Ihren lokalen Rechner mit Git.
3. Öffnen Sie das geklonte Repository in Visual Studio Code. Wenn Sie dazu aufgefordert werden, wählen Sie "Im Container erneut öffnen" oder öffnen Sie manuell die Befehlspalette (Ctrl+Shift+P oder Cmd+Shift+P) und wählen Sie "Dev Containers: Neu aufbauen und im Container erneut öffnen".
4. Warten Sie, bis der Dev-Container gebaut und gestartet ist. Dies kann einige Minuten dauern, insbesondere beim ersten Mal.

    **Nachdem der Build des Dev-Containers erfolgreich war, gibt der Befehl zurück:**

    `Erfolgreich installiert gramps-webapi-x.x.x.`

    !!! info
        Um den Container in Visual Studio Code neu aufzubauen:

        - Wenn Sie sich im Container befinden, verwenden Sie den Befehl "Im Container neu aufbauen" in der Befehlspalette.

        - Wenn Sie sich in der Ordneransicht befinden (d. h. nicht im Container), verwenden Sie den Befehl "Neu aufbauen und im Container erneut öffnen" in der Befehlspalette.

## Aufgaben

Wenn Sie nur den Backend-Code ändern, müssen Sie nicht unbedingt einen Webserver starten - Unit-Tests verwenden einen Flask-Testclient, der es ermöglicht, Anfragen an die API zu simulieren, ohne einen laufenden Server zu benötigen.

Das Ausführen eines Servers ist jedoch nützlich, wenn Sie

- Ihre Änderungen mit echten HTTP-Anfragen ausprobieren möchten (siehe [manuelle Abfragen](queries.md)), 
- die Auswirkungen von Änderungen auf die gesamte Gramps Web-Anwendung vorab anzeigen möchten, oder
- auch gleichzeitig Änderungen am Frontend vornehmen möchten (siehe [Frontend-Entwicklungssetup](../frontend/setup.md)).

Das Ausführen des Servers wird im Dev-Container durch vordefinierte Aufgaben vereinfacht. Sie können diese Aufgaben über die Befehlspalette (Ctrl+Shift+P oder Cmd+Shift+P) ausführen, indem Sie "Aufgaben: Aufgabe ausführen" auswählen und dann eine der folgenden Optionen wählen:
- "Web API bereitstellen" - startet den Flask-Entwicklungsserver auf Port 5555 mit aktivierter Debug-Protokollierung
- "Celery-Worker starten" - startet einen Celery-Worker zur Verarbeitung von Hintergrundaufgaben.


## Debugging

Debugging kann manchmal herausfordernd sein, insbesondere wenn es darum geht, komplexes Verhalten nachzuvollziehen oder subtile Probleme zu identifizieren. Um dies zu erleichtern, können Sie sowohl eine laufende API-Instanz als auch einzelne Testfälle direkt in Visual Studio Code debuggen.

### Debugging der Gramps Web API

Um die laufende API zu debuggen:

1. Öffnen Sie Visual Studio Code und gehen Sie zur **Ausführen und Debuggen**-Ansicht.  
2. Wählen Sie die **"Web API"**-Konfiguration aus dem Dropdown-Menü.  
3. Starten Sie das Debugging.  
4. Wenn Sie Anfragen an das Backend senden (entweder manuell oder über die Gramps Web GUI), wird die Ausführung an allen Haltepunkten, die Sie im Code gesetzt haben, angehalten.  
   Dies ermöglicht es Ihnen, Variablen, den Kontrollfluss und andere Laufzeitdetails zu inspizieren.

### Debugging von Testfällen

Um einen bestimmten Testfall zu debuggen:

1. Öffnen Sie die Testdatei, die Sie debuggen möchten (zum Beispiel `test_people.py`).  
2. Öffnen Sie in Visual Studio Code die **Ausführen und Debuggen**-Ansicht.  
3. Wählen Sie die **"Aktuelle Testdatei"**-Konfiguration.  
4. Starten Sie das Debugging - die Ausführung wird an allen Haltepunkten, die innerhalb dieser Testdatei gesetzt wurden, angehalten.  

Dieses Setup ermöglicht es Ihnen, durch die Testlogik zu schrittweise zu gehen, Variablenwerte zu untersuchen und Testfehler oder unerwartete Ergebnisse besser zu verstehen.
