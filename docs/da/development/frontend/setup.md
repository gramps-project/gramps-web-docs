# Frontend udviklingsopsætning

Denne side beskriver de trin, der er nødvendige for at komme i gang med frontend udvikling.

## Forudsætninger

Den anbefalede udviklingsopsætning bruger Visual Studio Code med devcontainers. Denne tilgang vil oprette et forudkonfigureret udviklingsmiljø med alle de værktøjer, du har brug for.

Se [Backend udviklingsopsætning](../backend/setup.md#prerequisites) for de nødvendige forudsætninger.

## Kom godt i gang

1. Åbn [Gramps Web frontend repository](https://github.com/gramps-project/gramps-web) og klik på "fork"
2. Klon dit forkede repository til din lokale maskine ved hjælp af Git
3. Åbn det klonede repository i Visual Studio Code. Når du bliver bedt om det, skal du vælge "Reopen in Container" eller manuelt åbne kommando paletten (Ctrl+Shift+P eller Cmd+Shift+P) og vælge "Dev Containers: Rebuild and Reopen in Container".
4. Vent på, at dev containeren bygger og starter. Dette kan tage et par minutter, især første gang.

## Kør frontend udviklingsserveren

For at køre frontend udviklingsserveren og forhåndsvise virkningen af dine ændringer i browseren, kan du bruge de foruddefinerede opgaver i dev containeren.

For at det kan fungere, skal du først starte en instans af [Gramps Web API backend](../backend/setup.md#tasks). Den nemmeste måde at gøre dette på er at bruge backend dev containeren og [køre "Serve Web API" opgaven](../backend/setup.md#tasks) i et separat VS Code vindue.

Når backend'en kører, kan du køre frontend udviklingsserveren ved at vælge "Tasks: Run Task" fra kommando paletten (Ctrl+Shift+P eller Cmd+Shift+P) og derefter vælge "Serve Gramps Web frontend".

Dette vil starte frontend udviklingsserveren på port 8001, som du kan tilgå i din browser på `http://localhost:8001`. Browseren vil automatisk genindlæse, når du foretager ændringer i frontend koden, så du kan se virkningen af dine ændringer med det samme.
