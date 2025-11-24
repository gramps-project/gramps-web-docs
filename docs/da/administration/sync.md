# Synkroniser Gramps Web og Gramps Desktop

*Gramps Web Sync* er et addon til Gramps, der gør det muligt at synkronisere din Gramps-database på din desktopcomputer med Gramps Web, inklusive mediefiler.

!!! warning
    Som med ethvert synkroniseringsværktøj, skal du ikke betragte dette som et backup-værktøj. En utilsigtet sletning på den ene side vil blive videreført til den anden side. Sørg for at lave regelmæssige backups (i Gramps XML-format) af dit slægtstræ.

!!! info
    Dokumentationen henviser til den nyeste version af Gramps Web Sync Addon. Brug venligst Gramps addon manager til at opdatere addon til den nyeste version, hvis det er nødvendigt.

## Installation

Addonen kræver Gramps 6.0, der kører på Python 3.10 eller nyere. 
Den er tilgængelig i Gramps Desktop og kan installeres [på den sædvanlige måde](https://www.gramps-project.org/wiki/index.php/5.2_Addons#Installing_Addons_in_Gramps).

!!! warn
    Sørg venligst for at bruge den samme version af Gramps på din desktop som den, der kører på din server. Se sektionen [Få hjælp](../help/help.md) for hvordan du finder ud af, hvilken Gramps-version din server kører. Gramps-versionen har formen `MAJOR.MINOR.PATCH`, og `MAJOR` og `MINOR` skal være de samme på web og desktop.

Valgfrit trin:

??? note inline end "Gnome keyring bug"
    Der er i øjeblikket en [bug i python keyring](https://github.com/jaraco/keyring/issues/496), der påvirker mange Gnome desktop-konfigurationer. Du skal muligvis oprette konfigurationsfilen `~/.config/python_keyring/keyringrc.cfg` og redigere den, så den ser sådan ud:

        [backend]
        default-keyring=keyring.backends.SecretService.Keyring

- Installer `keyring` (f.eks. `sudo apt install python3-keyring` eller `sudo dnf install python3-keyring`) for at tillade sikker opbevaring af API-adgangskoden i dit systems password manager.

## Brug

Når den er installeret, er addonen tilgængelig i Gramps under *Værktøjer > Behandling af slægtstræ > Gramps&nbsp;Web&nbsp;Sync*. Når den er startet, og efter at have bekræftet dialogen om, at fortrydelseshistorikken vil blive forkastet, vil en guide føre dig gennem synkroniseringstrinene. Bemærk, at der ikke vil blive anvendt ændringer på dit lokale træ eller på serveren, før du eksplicit bekræfter dem.

### Trin 1: indtast serveroplysninger

Værktøjet vil spørge dig om basis-URL'en (eksempel: `https://mygrampsweb.com/`) for din Gramps Web-instans, dit brugernavn og adgangskode. Du har brug for en konto med mindst redaktørrettigheder for at synkronisere ændringer tilbage til din eksterne database. Brugernavnet og URL'en vil blive gemt i klar tekst i din Gramps-brugermappe, adgangskoden vil kun blive gemt, hvis `keyring` er installeret (se ovenfor).

### Trin 2: gennemgå ændringer

Efter at have bekræftet dine legitimationsoplysninger, sammenligner værktøjet de lokale og eksterne databaser og vurderer, om der er nogen forskelle. Hvis der er, viser det en liste over objektændringer (hvor et objekt kan være en person, familie, begivenhed, sted osv.), der tilhører en af følgende kategorier:

- tilføjet lokalt
- slettet lokalt
- ændret lokalt
- tilføjet eksternt 
- slettet eksternt
- ændret eksternt
- ændret samtidigt (dvs. på begge sider)

Værktøjet bruger tidsstempler til at vurdere, hvilken side der er nyere for hvert objekt (se "Baggrund" nedenfor, hvis du er interesseret i detaljerne).

Hvis ændringerne ser ud som forventet, kan du klikke på "Anvend" for at anvende de nødvendige ændringer på de lokale og eksterne databaser.

!!! tip "Avanceret: Synkroniseringsmetode"
    Under listen over ændringer kan du vælge en synkroniseringsmetode.
    
    Standard, **bidirektionel synkronisering**, betyder, at det vil anvende ændringer på begge sider (lokalt og eksternt) ved at replikere de registrerede ændringer (objekter, der er tilføjet lokalt, vil blive tilføjet på den eksterne side osv.). Objekter, der er ændret på begge sider, vil også blive flettet og opdateret på begge sider.

    Muligheden **nulstil ekstern til lokal** vil derimod sikre, at den eksterne Gramps-database ser præcist ud som den lokale. Eventuelle objekter, der er registreret som "tilføjet eksternt", vil blive slettet igen, objekter, der er registreret som "slettet eksternt", vil blive tilføjet igen osv. *Ingen ændringer vil blive anvendt på den lokale Gramps-database.*

    Muligheden **nulstil lokal til ekstern** fungerer på den modsatte måde og sætter den lokale tilstand til den for den eksterne database. *Ingen ændringer vil blive anvendt på den eksterne database.*

    Endelig er muligheden **flet** ligesom bidirektionel synkronisering, idet den ændrer begge databaser, men den *sletter ikke nogen objekter*, men gendanner i stedet alle objekter, der kun er slettet på den ene side.

### Trin 3: synkroniser mediefiler

*Efter* at databaserne er blevet synkroniseret, kontrollerer værktøjet for eventuelle nye eller opdaterede mediefiler. Hvis det finder nogen, viser det en liste og beder om bekræftelse på at uploade/download de nødvendige filer.

Bemærk følgende begrænsninger ved mediefil-synkroniseringen:

- Hvis en lokal fil har en anden checksum end den, der er gemt i Gramps-databasen (dette kan ske f.eks. for Word-filer, når de redigeres efter at være tilføjet til Gramps), vil uploaden mislykkes med en fejlmeddelelse.
- Værktøjet kontrollerer ikke integriteten af alle lokale filer, så hvis en lokal fil findes under den sti, der er gemt for medieobjektet, men filen er forskellig fra filen på serveren, vil værktøjet ikke opdage det. Brug Media Verify Addon til at opdage filer med forkerte checksums.

## Fejlfinding

### Debug-logning

Hvis du oplever problemer med Sync Addon, skal du starte Gramps med debug-logning aktiveret ved [at starte Gramps fra kommandolinjen](https://gramps-project.org/wiki/index.php/Gramps_5.2_Wiki_Manual_-_Command_Line) med følgende mulighed:

```bash
gramps --debug grampswebsync
```

Dette vil udskrive mange nyttige logningsudtalelser til kommandolinjen, der vil hjælpe dig med at identificere årsagen til problemet.

### Serveroplysninger

Hvis det første trin allerede mislykkes, skal du dobbelttjekke server-URL'en, dit brugernavn og adgangskode.

### Tilladelsesproblemer

Hvis du støder på en fejl, der involverer tilladelser, skal du kontrollere brugerrollen for din Gramps Web-brugerkonto. Du kan kun anvende ændringer på den eksterne database, hvis du er en bruger med rollen redaktør, ejer eller administrator.

### Uventede databaseændringer

Hvis synkroniseringsværktøjet registrerer ændringer, som du mener ikke er sket, kan det være, at der er inkonsistenser i en af databaserne, der får Gramps til at registrere en forskel, eller at tiden er ude af synk mellem din lokale computer og din server.

Kontroller venligst, at klokken på begge maskiner er korrekt indstillet (bemærk, tidszonen betyder ikke noget, da værktøjet bruger Unix-tidsstempler, som er tidszoneagnostiske).

Du kan også køre kontrol- og reparationsværktøjet på din lokale database og se, om dette hjælper.

En bruteforce-metode, men effektiv metode til at sikre, at inkonsistenser i din lokale database ikke forårsager falske positiver, er at eksportere din database til Gramps XML og importere den igen i en ny, tom database. Dette er en tabsfri operation, men sikrer, at alle data importeres konsistent.

### Timeout-fejl

Hvis du oplever timeout-fejl (f.eks. angivet ved en HTTP-status 408-fejl eller en anden fejlmeddelelse, der inkluderer ordet "timeout"), skyldes det sandsynligvis et stort antal ændringer, der skal synkroniseres til den eksterne side i kombination med din serveropsætning.

For versioner af synkroniseringsaddon tidligere end v1.2.0 og versioner af Gramps Web API tidligere end v2.7.0 (se versionsinfo-fanen i Gramps Web), blev synkronisering til serversiden behandlet i en enkelt anmodning, der ville timeout, afhængigt af serverkonfigurationen, efter en til højst et par minutter. For store synkroniseringer (såsom efter import af tusindvis af objekter i den lokale database eller forsøg på at synkronisere et fuldt lokalt database til en tom server-side database) kan dette være for kort.

Hvis du bruger synkroniseringsaddon v1.2.0 eller senere og Gramps Web API v2.7.0 eller senere, behandles synkronisering på serversiden af en baggrundsarbejder og kan køre i meget lang tid (en statuslinje vil blive vist), og timeout-fejl bør ikke forekomme.

### Uventede mediefil-fejl

Hvis upload af en mediefil mislykkes, skyldes det ofte en mismatch i checksummen af den faktiske fil på disken og checksummen i den lokale Gramps-database. Dette sker ofte med redigerbare filer, som kontor dokumenter, der er redigeret uden for Gramps. Brug venligst Gramps Media Verify Addon til at korrigere checksummene for alle mediefiler.

### Bed om hjælp

Hvis alt det ovenstående ikke hjælper, kan du bede fællesskabet om hjælp ved at poste i [Gramps Web-kategorien på Gramps-forummet](https://gramps.discourse.group/c/gramps-web/28). Sørg venligst for at give:

- versionen af Gramps Web Sync-addon (og brug venligst den senest udgivne version)
- versionen af Gramps desktop, du bruger
- output fra Gramps debug-logning, aktiveret som beskrevet ovenfor
- versionsinfo for Gramps Web (du kan finde den under Indstillinger/Versionsinfo)
- eventuelle detaljer, du kan give om din Gramps Web-installation (selvhostet, Grampshub, ...)
- output fra dine Gramps Web-serverlogs, hvis du har adgang til dem (når du bruger docker: `docker compose logs --tail 100 grampsweb` og `docker compose logs --tail 100 grampsweb-celery`)

## Baggrund: hvordan addonen fungerer

Hvis du er nysgerrig efter, hvordan addonen faktisk fungerer, kan du finde nogle flere detaljer i denne sektion.

Addonen er beregnet til at holde en lokal Gramps-database synkroniseret med en ekstern Gramps Web-database, for at tillade både lokale og eksterne ændringer (samarbejdende redigering).

Den er **ikke egnet**

- Til at synkronisere med en database, der ikke er en direkte afledt (startende fra en databasekopi eller Gramps XML eksport/import) af den lokale database
- Til at flette to databaser med et stort antal ændringer på begge sider, der kræver manuel opmærksomhed for at flette. Brug det fremragende [Import Merge Tool](https://www.gramps-project.org/wiki/index.php/Import_Merge_Tool) til dette formål.

Driftsprincipperne for værktøjet er meget enkle:

- Det sammenligner de lokale og eksterne databaser
- Hvis der er nogen forskelle, kontrollerer det tidsstemplet for det seneste identiske objekt, lad os kalde det **t**
- Hvis et objekt ændrede sig mere for nylig end **t** findes i en database, men ikke den anden, synkroniseres det til begge (antag nyt objekt)
- Hvis et objekt ændrede sig sidste gang før **t** er fraværende i en database, slettes det i begge (antag slettet objekt)
- Hvis et objekt er forskelligt, men ændret efter **t** kun i en database, synkroniseres det til den anden (antag ændret objekt)
- Hvis et objekt er forskelligt, men ændret efter **t** i begge databaser, flettes de (antag konfliktende ændring)

Denne algoritme er simpel og robust, da den ikke kræver sporing af synkroniseringshistorik. Men den fungerer bedst, når du *synkroniserer ofte*.
