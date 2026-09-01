# Tags

Tags er etiketter, der kan anvendes på ethvert objekt i Gramps-databasen – personer, familier, begivenheder, steder, kilder, citater, arkiver, noter og medier. De er nyttige til at gruppere og filtrere objekter. Tags opbevares i Gramps-familietrædatabasen og deles blandt alle brugere; de er også fuldt kompatible med tags oprettet i Gramps Desktop.

## Håndtering af tags

Tags administreres fra **Tags** sektionen i [Administrationsindstillinger](../administration/settings.md#tags), som kun er tilgængelig for brugere med ejer- eller administratorrolle. Den viser alle eksisterende tags og giver dig mulighed for at:

- **Oprette** et nyt tag ved hjælp af **Nyt Tag** knappen
- **Omdøbe** et tag ved hjælp af redigerings (blyant) ikonet
- **Ændre farven** på et tag ved hjælp af farvevælgeren
- **Slette** et tag ved hjælp af slette ikonet

!!! note
    Sletning af et tag fjerner det fra alle objekter, det blev anvendt på.

## Anvendelse af tags på objekter

Tags kan anvendes på eller fjernes fra et objekt på dets detaljeside, når man er i redigeringstilstand.

## Filtrering efter tag

Alle [objektliste sider](lists.md) (Personer, Familier, Begivenheder, Steder, Kilder, Citater, Arkiver, Noter, Medier) inkluderer et tagfilter. Brug det til kun at vise objekter, der har et specifikt tag anvendt.

## Specielle tags

To tags har en særlig betydning i Gramps Web:

- **`Blog`** – enhver kilde mærket `Blog` behandles som et blogindlæg og vises i [Blog](blog.md) visningen
- **`ToDo`** – enhver note mærket `ToDo` behandles som en forskningsopgave og vises i [Opgaver](tasks.md) visningen

Disse tags oprettes automatisk, når du første gang bruger Blog- eller Opgavefunktionerne. Omdøbning eller sletning af dem vil bryde den tilsvarende funktion.
