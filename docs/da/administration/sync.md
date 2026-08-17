# Synkroniser Gramps Web og Gramps Desktop

*Gramps Web Sync* er et addon til Gramps, der synkroniserer Gramps-databasen på din desktop-computer med Gramps Web, inklusive mediefiler. Ændringer foretaget på den ene side overføres til den anden, så du kan arbejde lokalt og på nettet med det samme slægtstræ.

Som ethvert synkroniseringsværktøj er det ikke en backup: hvis du sletter noget på den ene side, vil det også blive slettet på den anden side. Sørg for at tage regelmæssige backups af dit slægtstræ i Gramps XML-format.

## Installation

Addonet kræver Gramps 6.0, der kører på Python 3.10 eller nyere. Det er tilgængeligt i Gramps Desktop og kan installeres [på den sædvanlige måde](https://www.gramps-project.org/wiki/index.php/5.2_Addons#Installing_Addons_in_Gramps). Denne dokumentation beskriver den nyeste version af addonet; brug Gramps addon manager til at opdatere det, hvis det er nødvendigt.

Din desktop og din server skal køre den samme version af Gramps. Versionen har formen `MAJOR.MINOR.PATCH`, og `MAJOR` og `MINOR` skal matche. Se [Få hjælp](../help/help.md) for at finde ud af, hvilken Gramps-version din server kører.

### Serverkrav

Addonet tjekker to ting om din server, så snart det opretter forbindelse, før noget downloades, og stopper med en besked, hvis nogen af dem ikke er opfyldt:

- **Gramps Web API version 3.x.** Denne version af addonet, til Gramps 6.0, fungerer med Gramps Web API 3. En ældre server skal opdateres; en server, der kører en *nyere* API-hovedversion, har brug for en nyere version af Gramps, ikke et nyere addon, fordi hver Gramps-udgivelseslinje parres med én API-version. Du kan finde versionen af din server under *Indstillinger ▸ Versionsinfo* i Gramps Web.
- **En baggrundsopgavekø.** Ændringer anvendes på serveren som en baggrundsopgave. Uden en opgavekø ville dette køre synkront og timeout på ethvert rigtigt slægtstræ.

For at anvende ændringer på den fjerntliggende database skal du have en konto med rollen redaktør, ejer eller administrator.

### Opbevaring af dit kodeord (valgfrit)

Installer `keyring` (f.eks. `sudo apt install python3-keyring` eller `sudo dnf install python3-keyring`) for at gemme API-kodeordet i dit systems password manager. Hvis keyring ikke kan bruges, siger addonet det og fortsætter uden det – du vil simpelthen blive bedt om dit kodeord hver gang.

På Gramps **Snap**-pakken er systemkeyringen blokeret af indelukning, indtil du forbinder grænsefladen én gang. Addonet viser denne kommando, når det opdager situationen:

```bash
snap connect gramps:password-manager-service
```

På mange Gnome desktop-konfigurationer betyder en [fejl i python keyring](https://github.com/jaraco/keyring/issues/496), at du skal oprette konfigurationsfilen `~/.config/python_keyring/keyringrc.cfg` med følgende indhold:

```ini
[backend]
default-keyring=keyring.backends.SecretService.Keyring
```

## Brug

Addonet er tilgængeligt i Gramps under *Værktøjer ▸ Behandling af slægtstræ ▸ Gramps&nbsp;Web&nbsp;Sync*. Efter at have bekræftet dialogadvarslen om, at fortrydelseshistorikken vil blive kasseret, åbnes synkroniseringsvinduet. Ingen ændringer anvendes på dit lokale træ eller på serveren, før du eksplicit bekræfter dem.

En bjælke øverst i vinduet navngiver det slægtstræ, du synkroniserer med, den konto og adresse, det tilhører, og hvornår det sidst blev synkroniseret. I bunden vises versionen af addonet og serverens Web API, hvilket er nyttigt, når du rapporterer et problem.

### Oprettelse af forbindelse

Hvis du har synkroniseret dette slægtstræ før, og dit kodeord er gemt, opretter addonet forbindelse, så snart det åbner, og går direkte til sammenligning. Ellers beder det om basis-URL'en til din Gramps Web-instans (eksempel: `https://mygrampsweb.com/`), dit brugernavn og dit kodeord.

URL'en og brugernavnet gemmes i klartekst i din Gramps-brugermappe. Kodeordet gemmes i din systems password manager, kun hvis du lader **Husk kodeord** være markeret; hvis du fjerner markeringen, fjernes ethvert kodeord, der allerede er gemt for den server. Hvis du indtaster en adresse, der begynder med `http://` i stedet for `https://`, advarer addonet dig, mens du skriver, fordi dit kodeord ville blive sendt i klartekst.

Hver server, du synkroniserer med, gemmes separat, sammen med sin egen post om, hvornår den sidst blev synkroniseret, så du kan skifte mellem to servere uden at forstyrre nogen af dem. Hver post registrerer også, hvilket lokalt slægtstræ det sidst blev synkroniseret fra. Addonet opretter kun forbindelse af sig selv, når det matcher det træ, du har åbent; ellers viser det forbindelsesoplysningerne og venter på, at du trykker på *Opret forbindelse*.

To handlinger er tilgængelige, mens der ikke skrives noget:

- **Skift server…**, på den øverste bjælke, vender tilbage til forbindelsesoplysningerne, så du kan pege dette træ mod en anden server. Det afbryder en sammenligning, der er i gang, i stedet for at få dig til at vente på, at den afsluttes.
- **Glem denne server**, på forbindelsespanelet, fjerner den gemte adresse, brugernavn og kodeord, sammen med posten om, hvornår dette træ sidst blev synkroniseret. Den næste synkronisering sammenligner derefter de to træer fra bunden.

### Gennemgang af ændringerne

Addonet sammenligner de lokale og fjerntliggende databaser og viser de handlinger, det foreslår at udføre, grupperet efter hvilken database de ændrer:

```
▾ Vil ændre på denne computer (7 objekter)
    ▾ Tilføj 3 objekter
        Person   John Smith        I0123
    ▾ Opdater 4 objekter
        …
▾ Vil ændre på serveren (5 objekter)
    …
```

Hver række navngiver objektet, så du kan se, hvem eller hvad der er påvirket i stedet for kun at se et Gramps ID. Hvis noget skal slettes, siger en note over listen, hvor mange objekter og på hvilken side.

Tryk på **Anvend** for at udføre, hvad listen beskriver.

Synkroniseringsvinduet blokerer ikke resten af Gramps, så du kan fortsætte med at arbejde, mens listen er åben. Hvis du redigerer et påvirket objekt i mellemtiden, bemærker addonet det, når du trykker på Anvend, stopper uden at ændre noget og beder dig om at sammenligne igen.

#### Synkroniseringsmetode

Synkroniseringsmetoden vælges over listen over ændringer. Ændring af den genopbygger listen, fordi metoden bestemmer, hvad hver forskel bliver.

- **Bidirektionel synkronisering** (standard) – ændringer fra begge sider kombineres. Objekter redigeret begge steder flettes.
- **Nulstil serveren til at matche denne computer** – serveren gøres til at matche denne computer. Alt, der kun er ændret på serveren, kasseres.
- **Nulstil denne computer til at matche serveren** – denne computer gøres til at matche serveren. Alt, der kun er ændret her, kasseres.

**Flet**-metoden, der var tilgængelig i versioner før 1.5, er blevet fjernet. Den adskilte sig fra bidirektionel synkronisering kun ved at gendanne objekter, der blev slettet på den ene side i stedet for at propagere sletningen. Hvis du stolede på den, skal du bruge bidirektionel synkronisering og gendanne alt, hvad du ønsker at bevare fra en backup.

### Mediefiler

Mediefiler håndteres som en del af den samme bekræftelse, ikke som et separat trin. Hvis der er nogen filer, der skal overføres, tilbyder en afkrydsningsfelt under listen at flytte dem:

```
[x] Overfør også 12 mediefiler (4 til download, 8 til upload)
```

Fjern markeringen for at synkronisere objektændringerne uden at røre ved filerne.

Filer, der mangler på *begge* sider, listes separat, fordi der ikke kan gøres noget ved dem:

```
2 mediefiler mangler på begge sider og kan ikke overføres.
```

Synkronisering af mediefiler har to begrænsninger:

- Hvis en lokal fil har en anden checksum end den, der er gemt i Gramps-databasen (dette kan ske f.eks. for Word-filer, der er redigeret efter at være tilføjet til Gramps), vil uploaden fejle med en fejlmeddelelse.
- Værktøjet verificerer ikke integriteten af alle lokale filer. Hvis en fil findes under den sti, der er gemt for medieobjektet, men adskiller sig fra filen på serveren, vil værktøjet ikke opdage det. Brug Media Verify Addon til at finde filer med forkerte checksums.

### Hvis en synkronisering fejler

Hvis en synkronisering fejler delvist – en mistet forbindelse, for eksempel – rapporterer addonet, hvad det allerede har anvendt, og tilbyder **Prøv igen**, som genoptager ved det trin, der fejlede, i stedet for at starte forfra. Den downloadede kopi af det fjerntliggende træ opbevares, så genforsøg ikke downloader og sammenligner det en gang til.

Tekniske detaljer om fejlen er tilgængelige bag en *Detaljer* udvidelse, med en knap til at kopiere dem til en fejlrapport.

## Fejlfinding

**Uventede ændringer.** Hvis addonet foreslår et alarmerende antal sletninger, skal du først tjekke den øverste bjælke: den navngiver det slægtstræ på serveren, du er ved at skrive til. At synkronisere et træ mod en server, der har et *forskelligt* træ, giver præcis dette symptom.

Ellers kan forskelle, du ikke forventede, komme fra inkonsistenser i en af databaserne eller fra ure, der ikke er synkroniseret mellem din computer og din server. Tjek, at begge ure er korrekt indstillet (tidens zone betyder ikke noget, da værktøjet bruger Unix-tidsstempler) og kør kontrol- og reparationsværktøjet på din lokale database. Som en sidste udvej, eksportér din lokale database til Gramps XML og importer den igen i en ny, tom database. Dette er en tabsfri operation, men sikrer, at alle data gemmes konsekvent.

**Mediefilfejl.** En mislykket upload skyldes ofte en mismatch mellem checksummen af filen på disken og checksummen i den lokale Gramps-database, hvilket sker med redigerbare filer som kontordokumenter, der er redigeret uden for Gramps. Brug Gramps Media Verify Addon til at rette checksummene.

**Tilladelsesfejl.** Tjek rollen for din Gramps Web-brugerkonto: kun redaktører, ejere og administratorer kan anvende ændringer på den fjerntliggende database.

### Bed om hjælp

Hvis ingen af ovenstående hjælper, bed om hjælp fra fællesskabet ved at poste i [Gramps Web-kategorien i Gramps-forummet](https://gramps.discourse.group/c/gramps-web/28). Angiv venligst:

- versionen af Gramps Web Sync-addonet, vist nederst i synkroniseringsvinduet ved siden af serverens Web API-version (og brug venligst den nyeste udgivne version)
- versionen af Gramps desktop, du bruger
- versionsinfoen for Gramps Web, som findes under *Indstillinger ▸ Versionsinfo*
- eventuelle detaljer om din Gramps Web-installation (selvhostet, Grampshub, ...)
- output fra dine Gramps Web-serverlogs, hvis du har adgang til dem (når du bruger Docker: `docker compose logs --tail 100 grampsweb` og `docker compose logs --tail 100 grampsweb-celery`)

Hvis du bliver bedt om en debug-log, skal du starte Gramps [fra kommandolinjen](https://gramps-project.org/wiki/index.php/Gramps_5.2_Wiki_Manual_-_Command_Line) med debug-logning aktiveret og genskabe problemet:

```bash
gramps --debug grampswebsync
```

## Baggrund: hvordan addonet fungerer

Addonet er designet til at holde en lokal Gramps-database synkroniseret med en fjerntliggende Gramps Web-database, hvilket muliggør både lokale og fjerntliggende ændringer (samarbejdende redigering).

Det er **ikke egnet**

- til at synkronisere med en database, der ikke er en direkte afledning (startende fra en databasekopi eller Gramps XML eksport/import) af den lokale database,
- til at flette to databaser med et stort antal ændringer på begge sider, der kræver manuel opmærksomhed til fletning. Brug det fremragende [Import Merge Tool](https://www.gramps-project.org/wiki/index.php/Import_Merge_Tool) til dette formål.

Driftsprincipperne er enkle:

- Det sammenligner de lokale og fjerntliggende databaser.
- Hvis der er nogen forskelle, tjekker det tidsstemplet for det seneste identiske objekt, lad os kalde det **t**.
- Hvis et objekt ændrede sig mere for nylig end **t** findes i den ene database, men ikke den anden, synkroniseres det til begge (antag nyt objekt).
- Hvis et objekt ændrede sig sidste gang før **t** er fraværende i den ene database, slettes det i begge (antag slettet objekt).
- Hvis et objekt er forskelligt, men ændret efter **t** kun i den ene database, synkroniser det til den anden (antag ændret objekt).
- Hvis et objekt er forskelligt, men ændret efter **t** i begge databaser, flettes de (antag konfliktende ændring).

Tidspunktet for den sidste vellykkede synkronisering registreres også, separat for hver server, og bruges som **t**, når det er nyere end det nyeste identiske objekt.

Denne algoritme er enkel og robust, da den ikke kræver sporing af synkroniseringshistorik. Den fungerer dog bedst, når du *synkroniserer ofte*.
