---
hide:
  - toc
  - navigation
---

# Funktioner

Gramps Web er en webapp til samarbejdende slægtsforskning. Den er bygget på [Gramps](https://gramps-project.org/), det open-source slægtsforskningsprogram, og arbejder med de samme data. Du kan køre den på din egen server eller bruge en hostingudbyder.

[Prøv demoen](#demo){ .md-button .md-button--primary } [Kom i gang](../install_setup/setup.md){ .md-button }

## Udforsk dit slægtstræ { .feature-group }

![Fan diagram, der viser syv generationer af forfædre](screenshots/fan.png){ align=right width="400"}

### Interaktive slægtstræ grafer

Naviger dit slægtstræ som et forfædret træ, efterkommertræ, timeglasgraf, relationsgraf eller fandiagram, med interaktive grafik af høj kvalitet og et konfigurerbart antal generationer.

Hold musen over enhver person for at se et forhåndsvisningskort med deres nøgleoplysninger, og spring direkte fra diagrammet til den fulde detaljeside.

<div style="clear:both;"></div>

---

![Tidslinje for familiens begivenheder mellem 1940'erne og 1970'erne](screenshots/timeline.png){ align=left width="400"}

### Kronologisk tidslinje

Se hver begivenhed i dit slægtstræ præsenteret på en horisontal, zoombar tidslinje. Rul og zoom gennem århundrederne, og filtrer derefter ned til en enkelt person – eller til alle deres forfædre eller efterkommere – eller til alt, hvad der skete ét sted.

Se [Tidslinje](../user-guide/timeline.md).

<div style="clear:both;"></div>

---

![Kort over London med et valgt sted, der viser dets foto og begivenheder](screenshots/map.png){ align=right width="400"}

### Interaktivt kort

Vis alle steder i dit træ på et interaktivt, søgbart kort. Søg efter nye steder direkte på OpenStreetMap, når du opretter et sted, plot folk i din database geografisk, og spor en enkelt persons liv ved at forbinde deres begivenheder med linjer på kortet.

<div style="clear:both;"></div>

---

![London på OpenHistoricalMap-laget, med tidsglideren indstillet til 1707](screenshots/ohm.png){ align=left width="400"}

### Historiske kort

Forvandl et historisk kort gemt som et medieobjekt i Gramps til et tilpasset kortoverlæg.

Du kan også skifte til de historiske vektorkort fra [OpenHistoricalMap](https://www.openhistoricalmap.org/) projektet. Brug tidsglideren til at rulle gennem udviklingen af stederne i din familiehistorie og vis de steder, hvor forfædre levede eller begivenheder fandt sted.

<div style="clear:both;"></div>

---

![Søgeresultater for "Albert" på tværs af personer, begivenheder og medier](screenshots/search.png){ align=right width="400"}

### Find alt

Den fuldtekst søgemaskine dækker alle Gramps objekt typer, inklusive indholdet af tekstnoter, og understøtter jokertegn og logiske operatorer.

For præcise forespørgsler tilbyder objektlistevisninger en avanceret filtertilstand baseret på [Gramps Object Query Language](../user-guide/goql.md), sammen med hurtige filtre efter tekst, tag og privatliv.

Fra enhver persons side åbner [Ekstern Søgning](../user-guide/external-search.md) en forudfyldt søgning på FamilySearch, Ancestry, CompGen og andre sider – og du kan tilføje dine egne.

<div style="clear:both;"></div>

## Byg og forsk { .feature-group }

![Forfædret træ i redigeringstilstand med dialogen til at tilføje et familiemedlem](screenshots/tree-edit.png){ align=left width="400"}

### Byg dit træ direkte i diagrammet

Skift trævisningen til redigeringstilstand og udvid dit slægtstræ uden at forlade diagrammet. Hver personkort får en **+** knap til at tilføje en far, mor, barn eller ægtefælle – enten ved at linke til nogen, der allerede er i din database, eller ved at oprette en helt ny person på stedet. Hver ændring gemmes straks.

Se [Redigering af slægtstræet](../user-guide/tree-edit.md).

<div style="clear:both;"></div>

---

![AI-assistenten, der læser en fødselsattest og foreslår nye optegnelser](screenshots/chat.png){ align=right width="400"}

### Integreret AI-assistent

Stil spørgsmål om dit slægtstræ på dit eget sprog, og få svar baseret på dine data.

Assistenten søger ikke bare: den forespørger direkte i din database med et sæt værktøjer, filtrerer personer, begivenheder, familier og steder, og beregner relationer mellem individer. Du kan se, hvilke værktøjer den bruger, mens den bygger et svar, og længere spørgsmål kører som baggrundsopgaver, så du kan navigere væk og komme tilbage.

Assistenten er valgfri og skal [opsættes af serveradministratoren](../install_setup/chat.md) med en AI-modeludbyder.

<div style="clear:both;"></div>

---

![Kromosombrowser, der viser de delte DNA-segmenter af elleve matches](screenshots/dna.png){ align=left width="400"}

### DNA-matches, kromosombrowser & Y-DNA

Upload DNA-matchdata fra din DNA-testudbyder, gem det sammen med dit slægtstræ, og se dine matches i en interaktiv kromosombrowser.

Rå Y-kromosom SNP-data kan bruges til at bestemme en persons mest sandsynlige [Y-DNA haplogruppe](../user-guide/y-dna.md) og vise deres patrilineære forfædre i det menneskelige Y-kromosomtræ, med tidsestimater. Analysen kører helt på din egen server – ingen data sendes til nogen tredjepart.

<div style="clear:both;"></div>

---

![Maleri med to personer tagget og de andre registrerede ansigtstræk omridset](screenshots/tag.png){ align=right width="400"}

### Tag personer i fotos med automatiseret ansigtsgenkendelse

Identificer forfædre i gamle familie fotos sammen med dine slægtninge. Ansigtstræk registreres automatisk, så tagging af en person tager to klik.

<div style="clear:both;"></div>

---

![Liste over forskningsopgaver med status, prioritet og tags](screenshots/tasks.png){ align=left width="400"}

### Integreret opgavestyringsapp

Gramps Web leveres med en integreret opgavestyringsapp til at organisere og planlægge din slægtsforskning. Giv hver opgave en status, en prioritet og tags, dokumenter din fremgang i en rig tekstbeskrivelse, og vedhæft de medier, du har indsamlet undervejs.

Opgaverne gemmes som kilder i Gramps-databasen, så de udgør en del af dine slægtsdata og kan tilgås og redigeres i Gramps Desktop også.

<div style="clear:both;"></div>

---

![Blogindlæg om at identificere personerne i et familiefoto](screenshots/blog.png){ align=right width="400"}

### Slægtsforskningsblog inkluderet

Sammenfat din forskning i form af bloghistorier med billeder, og del dem med dine slægtninge. En dedikeret editor gør det enkelt at skrive et nyt indlæg. Alle data gemmes i Gramps-databasen.

<div style="clear:both;"></div>

## Arbejd sammen { .feature-group }

![Liste over personer i slægtstræet](screenshots/list.png){ align=left width="400"}

### Privatlivsniveauer & brugeradgang

Du kan [markere optegnelser som private](../user-guide/privacy.md) – ned til et enkelt navn, begivenhedslink eller DNA-match – og kontrollere, hvilke brugere der har tilladelse til at se private optegnelser. Private optegnelser filtreres ud på databaseniveau for maksimal sikkerhed. Derudover kan du kontrollere, hvad brugere kan tilføje og redigere.

Brugere kan logge ind med en adgangskode eller gennem en ekstern identitetsudbyder ved hjælp af [OpenID Connect](../install_setup/oidc.md) – Google og Microsoft fra starten, plus tilpassede udbydere som Keycloak, Authentik og Authelia.

<div style="clear:both;"></div>

---

![En revision, der viser de ændrede felter i en personoptegnelse](screenshots/revisions.png){ align=right width="400"}

### Fuld revisionshistorik – med fortryd

Hver redigering af dit slægtstræ registreres. Gennemse den komplette historie grupperet efter transaktion, dyk ned i enhver individuel ændring for at se præcis hvilke felter der blev tilføjet, fjernet eller ændret, og fortryd en transaktion, hvis det viser sig at være en fejl. Hver objekts side har også sin egen revisionsfane, der viser, hvem der ændrede det og hvornår.

Se [Revisionshistorik](../user-guide/revisions.md).

<div style="clear:both;"></div>

---

![Gramps Desktop's værktøjsmenu med Gramps Web Sync-indgangen](screenshots/sync.png){ align=left width="300"}

### Fuld integration med Gramps Desktop

Gramps Web bruger den samme datamodel og database som [Gramps Desktop](https://gramps-project.org/). Du kan gennemse og redigere alle de samme [optegnelsestyper](https://gramps-project.org/wiki/index.php/Gramps_Data_Model): personer, familier, begivenheder, steder, arkiver, kilder, citater, medieobjekter og noter.

Med [Gramps Web Sync-tilføjelsen](../administration/sync.md) til Gramps Desktop kan du synkronisere dine data i begge retninger, så du kan fortsætte med at arbejde i Gramps Desktop og i Gramps Web side om side.

<div style="clear:both;"></div>

## Rapporter og dataeksport { .feature-group }

![Forfædre rapport genereret som en PDF](screenshots/report.png){ align=right width="400"}

### Generer udskrivbare rapporter

Gramps Web er bygget på den samme kerne som Gramps Desktop, så du kan generere næsten alle de [rapporter](https://gramps-project.org/wiki/index.php/Gramps_6.0_Wiki_Manual_-_Reports), som desktopappen understøtter direkte fra browseren, inklusive relationsgrafer eller bograpporter som PDF.

<div style="clear:both;"></div>

---

![Eksportside med listen over tilgængelige filformater](screenshots/export.png){ align=left width="300"}

### Ingen låsning – dataimport og eksport

Importer data i forskellige formater, herunder Gramps XML og GEDCOM, og download alle dine data når som helst – slægtstrædata, mediefiler og brugerkonti – til sikkerhedskopier eller for at flytte til en anden server.

Import kan forudses som en tørkørsel, før noget skrives, og en komplet sikkerhedskopi kan gendannes tilbage til træet.

<div style="clear:both;"></div>

## Brug det overalt { .feature-group }

![Den samme persons side på en computer og på en telefon](screenshots/mobile.png){ align=right width="400"}

### Fungerer på enhver enhed

Brug Gramps Web på enhver enhed med en webbrowser: upload fotos, opret eller rediger optegnelser, eller vis dit slægtstræ for slægtninge ved næste familietræf.

Gramps Web er en progressiv webapp: installer den på din startskærm eller desktop, og den opfører sig som en native app. På desktop får [tastaturgenveje](../user-guide/shortcuts.md) dig hvor som helst med et par tastetryk – tryk `?` for at se dem alle.

<div style="clear:both;"></div>

---

![Sprogvalgmenu](screenshots/lang.png){ align=left width="300"}

### Fuldstændig internationaliseret

Brug grænsefladen på et hvilket som helst af mere end 50 sprog oversat af Gramps-fællesskabet.

<div style="clear:both;"></div>

## Og mere

- **Notifikationer og baggrundsopgaver** – importer, eksporter, rapporter og indeksopbygninger kører i baggrunden, med fremskridt og fejl samlet ét sted
- **Tags, bogmærker og historie** – organiser objekter med farvekodede tags og kom tilbage til det, du arbejdede på
- **Masse redigering** – vælg flere objekter i listevisningerne for at slette dem på én gang, eller slå dublerede objekter sammen
- **Tilpassede listevisninger** – vælg, hvilke kolonner der skal vises, og filtrer efter tekst, tag eller privatliv
- **Tekstgenkendelse (OCR)** – udtræk tekst fra scannede dokumenter i dit mediegalleri
- **Datavalidering** – tjek dit træ for usandsynlige datoer og andre dataproblemer
- **Kalendere** – indtast datoer i den gregorianske, julianske, hebraiske, franske republikanske, persiske, islamiske eller svenske kalender
- **Gør det til dit eget** – giv dit site sit eget navn, tema farver og tekst og billede til startsiden

## Demo

For at logge ind på demoen, brug et af følgende brugernavn/adgangskode-par. Hver repræsenterer en af brugerrollerne i Gramps Web.

`owner / owner` <br>
`editor / editor` <br>
`contributor / contributor` <br>
`member / member`

Demoen nulstilles hver anden time, så eventuelle ændringer, du foretager, er midlertidige.

[Gå til Demo Login](https://demo.grampsweb.org/){ .md-button .md-button--primary target="_blank"}

### Tak

Demoen støttes venligt af DigitalOcean.

<a href="https://www.digitalocean.com/?refcode=b1d13ebe86ac&utm_campaign=Referral_Invite&utm_medium=Referral_Program&utm_source=badge"><img src="https://web-platforms.sfo2.cdn.digitaloceanspaces.com/WWW/Badge%202.svg" alt="DigitalOcean Referral Badge" /></a>
