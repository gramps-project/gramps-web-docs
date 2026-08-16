# Synkroniser Gramps Web og Gramps Desktop

*Gramps Web Sync* er et addon til Gramps, der gør det muligt at synkronisere din Gramps-database på din desktopcomputer med Gramps Web, inklusive mediefiler.

!!! warning
    Som med ethvert synkroniseringsværktøj, bør du ikke betragte dette som et backup-værktøj. En utilsigtet sletning på den ene side vil blive videreført til den anden side. Sørg for at lave regelmæssige backups (i Gramps XML-format) af dit slægtstræ.

!!! info
    Dokumentationen henviser til den nyeste version af Gramps Web Sync Addon. Brug venligst Gramps addon-manageren til at opdatere addon til den nyeste version, hvis det er nødvendigt.

!!! note "Hvad er ændret i version 1.5"
    Addonens interface blev omskrevet i version 1.5. Trin-for-trin guiden er væk, erstattet af et enkelt vindue, og mediefiler bekræftes nu sammen med objektændringerne i stedet for på en separat side bagefter. Hvis du leder efter synkroniseringsmodevælgeren, sidder den nu **over** listen over ændringer i stedet for under den. **Sammenflet** synkroniseringsmode er blevet fjernet; se [Synkroniseringsmode](#sync-mode) nedenfor.

## Installation

Addon kræver Gramps 6.0, der kører på Python 3.10 eller nyere. Den er tilgængelig i Gramps Desktop og kan installeres [på den sædvanlige måde](https://www.gramps-project.org/wiki/index.php/5.2_Addons#Installing_Addons_in_Gramps).

!!! warning
    Sørg for at bruge den samme version af Gramps på din desktop som den, der kører på din server. Se sektionen [Få hjælp](../help/help.md) for hvordan du finder ud af, hvilken Gramps-version din server kører. Gramps-versionen har formen `MAJOR.MINOR.PATCH`, og `MAJOR` og `MINOR` skal være de samme på web og desktop.

### Serverkrav

Addon tjekker to ting om din server, så snart den opretter forbindelse, og nægter at fortsætte, hvis nogen af dem ikke er opfyldt. Begge tjek sker, før noget downloades.

- **Gramps Web API version 3.x.** Denne version af addon, til Gramps 6.0, fungerer med Gramps Web API 3. En ældre server skal opdateres; en server, der kører en *nyere* API major version, har brug for en nyere version af Gramps, ikke en nyere addon, fordi hver Gramps-udgivelseslinje parres med én API-version. Du kan finde versionen af din server under *Indstillinger ▸ Versionsinfo* i Gramps Web.
- **En baggrundsopgavekø.** Synkronisering indsender sine ændringer som en baggrundsopgave. På en server uden en konfigureret opgavekø ville anvendelse af ændringer køre synkront og timeout på ethvert reelt slægtstræ, så addon nægter at starte i stedet for at fejle halvvejs igennem.

Du har også brug for en konto med mindst redaktørrettigheder for at anvende ændringer på den fjerne database.

Valgfrit trin:

??? note inline end "Gnome keyring fejl"
    Der er i øjeblikket en [fejl i python keyring](https://github.com/jaraco/keyring/issues/496), der påvirker mange Gnome desktop-konfigurationer. Du skal muligvis oprette konfigurationsfilen `~/.config/python_keyring/keyringrc.cfg` og redigere den til at se sådan ud:

        [backend]
        default-keyring=keyring.backends.SecretService.Keyring

- Installer `keyring` (f.eks. `sudo apt install python3-keyring` eller `sudo dnf install python3-keyring`) for at tillade sikker opbevaring af API-adgangskoden i dit systems password manager.

Hvis keyring ikke kan bruges, siger addon det og fortsætter uden det — du vil blot blive bedt om din adgangskode hver gang. På Gramps **Snap**-pakken er systemkeyringen blokeret af confinement, indtil du forbinder grænsefladen én gang:

```bash
snap connect gramps:password-manager-service
```

Addon viser denne præcise kommando, når den opdager situationen.

## Brug

Når den er installeret, er addon tilgængelig i Gramps under *Værktøjer ▸ Behandling af slægtstræ ▸ Gramps&nbsp;Web&nbsp;Sync*. Efter at have bekræftet dialogadvarslen om, at fortrydelseshistorikken vil blive kasseret, åbnes synkroniseringsvinduet.

**Ingen ændringer anvendes på dit lokale træ eller på serveren, før du eksplicit bekræfter dem.**

Vinduet har en stribe langs toppen, der navngiver det slægtstræ, du synkroniserer med, den konto og adresse, det tilhører, og hvornår det sidst blev synkroniseret. Nederst vises versionen af addon og serverens Web API — nyttigt når du rapporterer et problem.

### Oprettelse af forbindelse

Hvis du har synkroniseret dette slægtstræ før, og din adgangskode er gemt, opretter addon forbindelse, så snart den åbner, og går direkte til sammenligning. Ellers beder den om basis-URL'en til din Gramps Web-instans (eksempel: `https://mygrampsweb.com/`), dit brugernavn og din adgangskode.

URL'en og brugernavnet gemmes i klar tekst i din Gramps-brugerbibliotek. Adgangskoden gemmes i din systems password manager, kun hvis du lader **Husk adgangskode** være markeret; hvis du fjerner markeringen, fjernes enhver adgangskode, der allerede er gemt for den server.

!!! tip "Flere slægtstræer, flere servere"
    Hver server, du synkroniserer med, gemmes separat, sammen med sin egen optegnelse over, hvornår den sidst blev synkroniseret. At skifte mellem to servere forstyrrer ikke længere nogen af dem.

    Hver post registrerer også **hvilket lokalt slægtstræ** det sidst blev synkroniseret fra. Addon opretter kun forbindelse af sig selv, når det matcher det træ, du har åbent; ellers viser det forbindelsesoplysningerne og venter på, at du trykker på *Opret forbindelse*, med en advarsel hvis de gemte legitimationsoplysninger tilhører et andet træ. Dette er vigtigt, fordi synkronisering af et træ mod en server, der holder et *forskelligt* træ, ville foreslå at slette indholdet af begge.

To handlinger er tilgængelige, mens der ikke skrives noget:

- **Skift server…**, på den øverste stribe, vender tilbage til forbindelsesoplysningerne, så du kan pege dette træ mod en anden server. Det afbryder en sammenligning i gang i stedet for at få dig til at vente på, at den afsluttes.
- **Glem denne server**, på forbindelsespanelet, fjerner den den gemte adresse, brugernavn og adgangskode, sammen med optegnelsen over, hvornår dette træ sidst blev synkroniseret. Den næste synkronisering sammenligner derefter de to træer fra bunden.

Hvis du indtaster en adresse, der begynder med `http://` i stedet for `https://`, vises en advarsel, mens du skriver. Din adgangskode ville blive sendt i klar tekst, så brug den kun til lokal testning.

### Gennemgang af ændringerne

Addon sammenligner de lokale og fjerne databaser og viser, hvad den foreslår at gøre. I modsætning til tidligere versioner, der listede de rå forskelle mellem de to træer, viser listen nu de **handlinger**, der vil blive udført, grupperet efter hvilken database de ændrer:

```
▾ Vil ændre på denne computer (7 objekter)
    ▾ Tilføj 3 objekter
        Person   John Smith        I0123
    ▾ Opdater 4 objekter
        …
▾ Vil ændre på serveren (5 objekter)
    …
```

Hver række navngiver objektet, så du kan se, hvem eller hvad der er berørt i stedet for kun at se et Gramps ID.

Hvis noget skal slettes, siger en advarsel over listen, hvor mange objekter og på hvilken side. Dette vises, når der er involveret sletninger, inklusive under en almindelig tovejs synkronisering, der viderefører en sletning, du selv har foretaget.

Tryk på **Anvend** for at udføre det, listen beskriver.

!!! warning "Rediger ikke mens du gennemgår"
    Synkroniseringsvinduet blokerer ikke resten af Gramps, så du kan fortsætte med at arbejde, mens listen er åben. Hvis du redigerer et berørt objekt, opdager addon det, når du trykker på Anvend, stopper uden at ændre noget og beder dig om at sammenligne igen. Intet går tabt, men sammenligningen skal gentages.

#### Synkroniseringsmode

Synkroniseringsmode vælges **over** listen over ændringer. Ændring af det genopbygger listen, fordi mode bestemmer, hvad hver forskel faktisk bliver.

- **Tovejs synkronisering** (standard) — ændringer fra begge sider kombineres. Objekter redigeret begge steder flettes.
- **Nulstil serveren til at matche denne computer** — serveren gøres til at matche denne computer. Alt, der kun er ændret på serveren, kasseres.
- **Nulstil denne computer til at matche serveren** — denne computer gøres til at matche serveren. Alt, der kun er ændret her, kasseres.

!!! note
    **Sammenflet** mode, der var tilgængelig i tidligere versioner, er blevet fjernet. Den adskilte sig fra tovejs synkronisering kun ved at gendanne objekter, der blev slettet på den ene side i stedet for at videreføre sletningen, hvilket ikke var en forskel, som grænsefladen kunne forklare nyttigt. Hvis du stolede på det, skal du bruge tovejs synkronisering og gendanne alt, du ønsker at beholde fra en backup.

### Mediefiler

Mediefiler håndteres som en del af den samme bekræftelse, ikke som et separat trin. Hvis der er filer, der skal overføres, tilbyder en afkrydsningsfelt under listen at flytte dem:

```
[x] Overfør også 12 mediefiler (4 til download, 8 til upload)
```

Fjern markeringen for at synkronisere objektændringerne uden at røre ved filerne.

Filer, der mangler på *begge* sider, listes separat, fordi der ikke kan gøres noget ved dem:

```
2 mediefiler mangler på begge sider og kan ikke overføres.
```

Bemærk følgende begrænsninger ved mediefil-synkronisering:

- Hvis en lokal fil har en anden checksum end den, der er gemt i Gramps-databasen (dette kan ske f.eks. for Word-filer, når de redigeres efter at være tilføjet til Gramps), vil uploaden fejle med en fejlmeddelelse.
- Værktøjet tjekker ikke integriteten af alle lokale filer, så hvis en lokal fil eksisterer under den sti, der er gemt for medieobjektet, men filen er forskellig fra filen på serveren, vil værktøjet ikke opdage det. Brug Media Verify Addon til at opdage filer med forkerte checksums.

### Når noget går galt

Hvis en synkronisering fejler halvvejs — en tabt forbindelse, for eksempel — rapporterer addon, hvad den allerede har anvendt, og tilbyder **Prøv igen**, som genoptager ved det trin, der fejlede i stedet for at starte forfra. Den downloadede kopi af det fjerne træ opbevares, så genforsøg ikke downloader og sammenligner det en anden gang.

Tekniske detaljer om fejlen er tilgængelige bag en *Detaljer* udvidelse, med en knap til at kopiere dem til en fejlrapport.

## Fejlfinding

### Debug logging

Hvis du oplever problemer med Sync Addon, skal du starte Gramps med debug logging aktiveret ved at [starte Gramps fra kommandolinjen](https://gramps-project.org/wiki/index.php/Gramps_5.2_Wiki_Manual_-_Command_Line) med følgende mulighed:

```bash
gramps --debug grampswebsync
```

Dette vil udskrive mange nyttige logningsudtalelser til kommandolinjen, der vil hjælpe dig med at identificere årsagen til problemet.

### Serverlegitimationsoplysninger

Hvis forbindelsen fejler, skal du dobbelttjekke serverens URL, dit brugernavn og din adgangskode.

### Addon nægter at oprette forbindelse

Hvis addon rapporterer, at serverens Gramps Web API-version er for gammel eller for ny, eller at der ikke er konfigureret nogen baggrundsopgavekø, se [Serverkrav](#server-requirements) ovenfor. Disse tjekkes før noget andet, så meddelelsen navngiver problemet direkte.

### Problemer med tilladelser

Hvis du støder på en fejl, der involverer tilladelser, skal du tjekke brugerrollen for din Gramps Web-brugerkonto. Du kan kun anvende ændringer på den fjerne database, hvis du er en bruger med rollen redaktør, ejer eller administrator.

### Uventede databaseændringer

Hvis synkroniseringsværktøjet opdager ændringer, som du mener ikke skete, kan det være, at der er uoverensstemmelser i en af databaserne, der narre Gramps til at opdage en forskel, eller at tiden er ude af synk mellem din lokale computer og din server.

Tjek venligst, at urene på begge maskiner er korrekt indstillet (bemærk, tidszonen betyder ikke noget, da værktøjet bruger Unix-tidsstempler, som er tidszoneagnostiske).

Du kan også køre tjek & reparer værktøjet på din lokale database og se, om dette hjælper.

En bruteforce, men effektiv metode til at sikre, at uoverensstemmelser i din lokale database ikke forårsager falske positiver, er at eksportere din database til Gramps XML og reimportere den i en ny, tom database. Dette er en tabsfri operation, men sikrer, at alle data importeres konsekvent.

!!! tip
    Hvis addon foreslår et alarmerende antal sletninger, skal du tjekke den øverste stribe først: den navngiver det slægtstræ på serveren, du er ved at skrive til. At synkronisere mod en server, der holder et *forskelligt* træ, producerer præcis dette symptom.

### Timeout-fejl

Synkronisering til serveren behandles af en baggrundsarbejder, så langvarige synkroniseringer bør ikke timeout. En server uden en konfigureret opgavekø nægtes ved forbindelsestidspunktet af denne grund — se [Serverkrav](#server-requirements).

Anmodninger fra addon til serveren timeout efter 60 sekunder uden et svar, så en utilgængelig server rapporterer en forbindelsesfejl i stedet for at hænge uendeligt.

### Uventede mediefil-fejl

Hvis upload af en mediefil fejler, skyldes det ofte en mismatch i checksummen af den faktiske fil på disk og checksummen i den lokale Gramps-database. Dette sker ofte med redigerbare filer, som kontor dokumenter, der redigeres uden for Gramps. Brug venligst Gramps Media Verify Addon til at korrigere checksummene for alle mediefiler.

### Bed om hjælp

Hvis alt det ovenstående ikke hjælper, kan du bede fællesskabet om hjælp ved at poste i [Gramps Web-kategorien på Gramps-forummet](https://gramps.discourse.group/c/gramps-web/28). Sørg venligst for at give:

- versionen af Gramps Web Sync addon (og brug venligst den senest udgivne version) — den vises nederst i synkroniseringsvinduet, ved siden af serverens Web API-version
- versionen af Gramps desktop, du bruger
- output fra Gramps debug logging, aktiveret som beskrevet ovenfor
- versionsinfo for Gramps Web (du kan finde den under Indstillinger/Versionsinfo)
- eventuelle detaljer, du kan give om din Gramps Web-installation (selvhostet, Grampshub, ...)
- output fra dine Gramps Web serverlogs, hvis du har adgang til dem (når du bruger docker: `docker compose logs --tail 100 grampsweb` og `docker compose logs --tail 100 grampsweb-celery`)

## Baggrund: hvordan addon fungerer

Hvis du er nysgerrig efter, hvordan addon faktisk fungerer, kan du finde lidt flere detaljer i denne sektion.

Addon er beregnet til at holde en lokal Gramps-database synkroniseret med en fjern Gramps Web-database, for at tillade både lokale og fjerne ændringer (samarbejdende redigering).

Det er **ikke egnet**

- Til at synkronisere med en database, der ikke er direkte afledt (startende fra en databasekopi eller Gramps XML eksport/import) af den lokale database
- Til at flette to databaser med et stort antal ændringer på begge sider, der kræver manuel opmærksomhed til sammenfletning. Brug det fremragende [Import Merge Tool](https://www.gramps-project.org/wiki/index.php/Import_Merge_Tool) til dette formål.

Principperne for værktøjets drift er meget enkle:

- Det sammenligner de lokale og fjerne databaser
- Hvis der er nogen forskelle, tjekker det tidsstemplet for det seneste identiske objekt, lad os kalde det **t**
- Hvis et objekt ændrede sig mere for nylig end **t** findes i den ene database, men ikke den anden, synkroniseres det til begge (antag nyt objekt)
- Hvis et objekt ændrede sig sidste gang før **t** er fraværende i den ene database, slettes det i begge (antag slettet objekt)
- Hvis et objekt er forskelligt, men ændret efter **t** kun i den ene database, synkroniseres det til den anden (antag modificeret objekt)
- Hvis et objekt er forskelligt, men ændret efter **t** i begge databaser, flettes de (antag konfliktende ændring)

Tiden for den sidste succesfulde synkronisering registreres også, separat for hver server, og bruges som **t**, når den er mere aktuel end det nyeste identiske objekt.

Denne algoritme er simpel og robust, da den ikke kræver sporing af synkroniseringshistorik. Dog fungerer den bedst, når du *synkroniserer ofte*.
