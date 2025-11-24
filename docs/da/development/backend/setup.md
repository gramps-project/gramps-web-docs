# Backend udviklingsopsætning

Denne side opregner de trin, der kræves for at begynde at udvikle [Gramps Web API](https://github.com/gramps-project/gramps-web-api/), backend (serverkomponenten) af Gramps Web.


## Forudsætninger

Den anbefalede udviklingsopsætning bruger Visual Studio Code med devcontainers. Denne tilgang vil oprette et forudkonfigureret udviklingsmiljø med alle de værktøjer, du har brug for. For at komme i gang skal du bruge følgende ingredienser:

- [Docker](https://docs.docker.com/get-docker/)
- [Visual Studio Code](https://code.visualstudio.com/) med [Dev Containers-udvidelsen](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers) installeret
- [Git](https://git-scm.com)

Du kan bruge Linux, macOS eller Windows som dit operativsystem.


## Kom godt i gang

1. Åbn [Gramps Web API repository](https://github.com/gramps-project/gramps-web-api) og klik på "fork"
2. Klon dit forkede repository til din lokale maskine ved hjælp af Git
3. Åbn det klonede repository i Visual Studio Code. Når du bliver bedt om det, skal du vælge "Reopen in Container" eller manuelt åbne kommando paletten (Ctrl+Shift+P eller Cmd+Shift+P) og vælge "Dev Containers: Rebuild and Reopen in Container".
4. Vent på, at dev containeren bygger og starter. Dette kan tage et par minutter, især første gang.


## Opgaver

Hvis du kun ændrer backend-koden, behøver du ikke nødvendigvis at starte en webserver - enhedstest bruger en Flask testklient, der tillader simulering af anmodninger til API'en uden at have en kørende server.

Dog er det nyttigt at køre en server, hvis du

- vil prøve dine ændringer med rigtige HTTP-anmodninger (se [manuelle forespørgsler](queries.md)), 
- vil forudse virkningen af ændringer på den fulde Gramps Web-applikation, eller
- også vil foretage samtidige ændringer til frontend (se [frontend udviklingsopsætning](../frontend/setup.md)).

At køre serveren er forenklet i dev containeren ved hjælp af foruddefinerede opgaver. Du kan køre disse opgaver fra kommando paletten (Ctrl+Shift+P eller Cmd+Shift+P) ved at vælge "Tasks: Run Task" og derefter vælge en af følgende:
- "Serve Web API" - starter Flask udviklingsserveren på port 5555 med debug logging aktiveret
- "Start Celery worker" - starter en Celery worker til at behandle baggrundsopgaver.


## Fejlfinding

Fejlfinding kan nogle gange være udfordrende, især når man prøver at spore kompleks adfærd eller identificere subtile problemer. For at gøre dette lettere kan du fejlsøge både en kørende API-instans og individuelle testtilfælde direkte i Visual Studio Code.

### Fejlfinding af Gramps Web API

For at fejlsøge den kørende API:

1. Åbn Visual Studio Code og gå til **Kør og Fejlret** visningen.  
2. Vælg **"Web API"** konfigurationen fra dropdown-menuen.  
3. Start fejlfinding.  
4. Når du sender anmodninger til backend (enten manuelt eller gennem Gramps Web GUI), vil udførelsen pause ved enhver breakpoint, du har sat i koden.  
   Dette giver dig mulighed for at inspicere variabler, kontrolflow og andre runtime-detaljer.

### Fejlfinding af Testtilfælde

For at fejlsøge et specifikt testtilfælde:

1. Åbn testfilen, du vil fejlsøge (for eksempel `test_people.py`).  
2. I Visual Studio Code, åbn **Kør og Fejlret** visningen.  
3. Vælg **"Nuværende Testfil"** konfigurationen.  
4. Start fejlfinding - udførelsen stopper ved enhver breakpoint, der er sat inden for den testfil.  

Denne opsætning giver dig mulighed for at træde igennem testlogik, undersøge variabelværdier og bedre forstå testfejl eller uventede resultater.
