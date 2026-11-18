# Tags

Tags er etiketter, der kan anvendes på ethvert objekt i Gramps-databasen – personer, familier, begivenheder, steder, kilder, citater, arkiver, noter og medier. De er nyttige til at gruppere og filtrere objekter. Tags gemmes i Gramps familie træ database og deles mellem alle brugere; de er også fuldt kompatible med tags, der er oprettet i Gramps Desktop.

## Håndtering af tags

Tags administreres fra **Tags** sektionen i [Administration Settings](../administration/settings.md#tags), som kun er tilgængelig for brugere med ejer- eller administratorrolle. Den viser alle eksisterende tags og giver dig mulighed for at:

- **Oprette** et nyt tag ved at bruge **New Tag** knappen
- **Omnavngive** et tag ved at bruge redigerings (blyant) ikonet
- **Ændre farven** på et tag ved at bruge farvevælgeren
- **Slette** et tag ved at bruge slette ikonet

!!! note
    Sletning af et tag fjerner det fra alle objekter, det blev anvendt på.

## Anvendelse af tags på objekter

Tags kan anvendes på eller fjernes fra et objekt på dets detaljeside, når det er i redigeringstilstand. For at tagge mange objekter på én gang, vælg dem i en liste og brug **Add Tag** eller **Remove Tag** handlingen, se [Lists](lists.md#tags-and-privacy).

Tags vises i **Tags** kolonnen i listerne, og i søgeresultater, bogmærker og historik. Hvis en liste ikke viser kolonnen, kan du aktivere den i kolonnevælgeren.

## Filtrering efter tag

Alle [objektliste sider](lists.md) (Personer, Familier, Begivenheder, Steder, Kilder, Citater, Arkiver, Noter, Medier) inkluderer et tagfilter. Brug det til kun at vise objekter, der har et specifikt tag anvendt.

## Specielle tags

To tags har en særlig betydning i Gramps Web:

- **`Blog`** – enhver kilde, der er tagget `Blog`, behandles som et blogindlæg og vises i [Blog](blog.md) visningen
- **`ToDo`** – enhver note, der er tagget `ToDo`, behandles som en forskningsopgave og vises i [Tasks](tasks.md) visningen

Disse tags oprettes automatisk, når du første gang bruger Blog- eller Opgavefunktionerne. Omnavngivning eller sletning af dem vil bryde den tilsvarende funktion.
