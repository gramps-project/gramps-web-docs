# Sikkerhedskopiering og gendannelse

Træejere kan oprette, downloade og gendanne sikkerhedskopier af træet i sektionen **Sikkerhedskopier** i [Administrationsindstillinger](settings.md).

En sikkerhedskopi indeholder data om familietræet, herunder private optegnelser, træindstillinger og brugerne af træet. Mediefiler er ikke inkluderet; se [Sikkerhedskopier dine mediefiler](export.md#back-up-your-media-files).

## Gemte sikkerhedskopier

Hvis serveradministratoren har angivet en sikkerhedskopimappe (`BACKUP_DIR`, se [Serverkonfiguration](../install_setup/configuration.md)), kan sikkerhedskopier gemmes på serveren. Ellers viser sektionen en meddelelse om, at opbevaring af sikkerhedskopier ikke er konfigureret, og at kun gendannelse fra en uploadet fil er tilgængelig.

Klik på **Lav sikkerhedskopi...** for at oprette en sikkerhedskopi. Den oprettes som en baggrundsopgave og vises derefter i listen over gemte sikkerhedskopier, med sin dato, antallet af personer og sin størrelse. Serveren opbevarer kun de nyeste sikkerhedskopier (fem som standard) og sletter automatisk ældre. Antallet af sikkerhedskopier, der kan oprettes pr. dag, er også begrænset.

For hver gemt sikkerhedskopi kan du:

- **Downloade** den som en `.tar` fil, for eksempel for at opbevare en kopi et andet sted.
- **Gendanne** den, som beskrevet nedenfor.
- **Slette** den, efter bekræftelse.

En sikkerhedskopi lavet med en nyere version af Gramps Web end den, der kører på serveren, er markeret med et advarselsikon og kan ikke gendannes.

## Gendan fra sikkerhedskopi

Gendanner træet fra en gemt sikkerhedskopi eller fra en uploadet fil. For at gendanne en gemt sikkerhedskopi skal du klikke på gendannelsesknappen ved siden af den. For at gendanne fra en fil skal du vælge en Gramps Web-sikkerhedskopi (`.tar`) eller en Gramps XML-fil (`.gramps`) og klikke på **Gendan**.

!!! danger
    Gendannelse af data er en destruktiv erstatning, ikke en sammenlægning. Enhver eksisterende genstand, der ikke er til stede i sikkerhedskopien, slettes.

For en Gramps Web-sikkerhedskopi vises en dialogboks, der viser, hvornår sikkerhedskopien blev lavet, for hvilket træ, og med hvilken version, og lader dig vælge, hvilke dele der skal gendannes:

- **Data** – objekterne i familietræet
- **Træindstillinger** – indstillingerne for administrationssiden, såsom tema farver, app titel og note på startsiden
- **Brugere** – brugerne af træet

Klik på **Forhåndsvisning** for at se, hvad gendannelsen ville ændre. En Gramps XML-fil indeholder kun data, så for en sådan fil starter forhåndsvisningen straks. Du vil blive bedt om at genautentificere, hvis din session ikke er frisk nok. Forhåndsvisningen kører som en baggrundsopgave og åbner, når den er færdig, en dialogboks, der opsummerer ændringerne pr. objekttype (personer, familier, begivenheder, steder, citater, kilder, opbevaringssteder, medieobjekter, noter, tags), og for træindstillinger og brugere, hvis valgt:

- **Tilføj** – objekter til stede i sikkerhedskopien, men mangler i det nuværende træ
- **Opdater** – objekter til stede i begge, der adskiller sig
- **Slet** – objekter i det nuværende træ, der er fraværende fra sikkerhedskopien
- **Uændret** – objekter identiske i begge

Hvis nogen objekter ville blive slettet, advarer dialogboksen om, hvor mange. Gennemgå opsummeringen, og klik derefter på **Gendan** for at anvende ændringerne, eller **Annuller** for at afbryde.

Efter gendannelsen listes brugere, der blev tilføjet fra sikkerhedskopien. De får et tilfældigt kodeord, så de skal nulstille deres kodeord, før de kan logge ind. Brugere, der allerede findes på serveren, ændres aldrig. Medieobjekter, hvis filer mangler på serveren, listes også; upload dem via [Importér mediefiler](import-media.md).

!!! note
    Gendannelse af data gendanner kun objektdata og mediereferencer. Binære mediefiler selv og træmetadata (standardperson, bogmærker, navnegrupper) påvirkes ikke.

!!! tip
    Brug dette til at rulle et træ tilbage til en kendt god sikkerhedskopi, for eksempel efter en dårlig import eller en uønsket masseændring.

## Gramps XML som sikkerhedskopi

Hvis opbevaring af sikkerhedskopier ikke er tilgængelig, eller du kun ønsker at opbevare en kopi af familietrædataene, [eksporter](export.md) træet som Gramps XML. En sådan fil kan også gendannes via [Gendan fra sikkerhedskopi](#restore-from-backup).

Bemærk, at hvis din Gramps Web-bruger ikke har tilladelse til at se private optegnelser, vil eksporten ikke være en fuld sikkerhedskopi, da den ikke vil indeholde nogen private optegnelser.
