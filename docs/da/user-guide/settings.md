# Brugerindstillinger

Brugerindstillinger er tilgængelige via brugerikonet i den øverste app-bar, derefter **Brugerindstillinger**. Siden er organiseret i sammenklappelige sektioner. Ændringer træder i kraft med det samme, medmindre andet er angivet.

!!! note
    Ændringer i Brugerindstillinger påvirker kun din egen konto. Indstillinger, der påvirker alle brugere af træet, administreres i [Administrationsindstillinger](../administration/settings.md).

## Konto

Dækker dine profiloplysninger, legitimationsoplysninger og kontosikkerhed.

### Brugerinformation

Viser dit **brugernavn** og nuværende **brugerrolle** (f.eks. Gæst, Medlem, Redaktør). Disse er skrivebeskyttede.

### Skift e-mail

Indtast en ny e-mailadresse og klik på **Send** for at opdatere den adresse, der er knyttet til din konto. E-mailadressen bruges til nulstilling af adgangskoder og (hvis konfigureret) meddelelser.

### Skift adgangskode

Indtast din nuværende adgangskode og en ny adgangskode, og klik derefter på **Send**. Du forbliver logget ind på den aktuelle enhed, mens dine sessioner på andre enheder og browsere afsluttes inden for 15 minutter. Hvis du har glemt din nuværende adgangskode, skal du bruge linket **Glemt adgangskode** på login-siden i stedet.

Denne sektion er skjult, hvis serveren kun tillader login gennem en ekstern udbyder (se [OIDC-godkendelse](../install_setup/oidc.md)).

### Koblede loginmetoder

Hvis din server tilbyder single sign-on (se [OIDC-godkendelse](../install_setup/oidc.md)), kan du linke en konto fra en udbyder, såsom Google eller din organisations login, til din Gramps Web-konto. Du kan derefter logge ind med den udbyder og lande i din eksisterende konto, med din rolle og dine redigeringer. Denne sektion vises kun, når single sign-on er aktiveret, og serveren understøtter linking (Gramps Web API 3.24 og senere).

For at linke en konto skal du klikke på **Link med** og udbyderens navn, logge ind hos udbyderen, og du bliver taget tilbage til dine indstillinger. Hvis du ikke har logget ind for nylig, bliver du bedt om at logge ind igen først.

En udbyderkonto kan kun linkes til én Gramps Web-konto. Hvis du ser "Denne login er allerede linket til en anden konto", er den linket et andet sted, for eksempel til en konto, der blev oprettet, da du først loggede ind med den udbyder. En administrator kan slette den anden konto, hvorefter du kan linke den til din.

For at fjerne et link til en konto skal du klikke på **Fjern link**. Hvis det er din sidste koblede loginmetode, skal du også indtaste din adgangskode, så du stadig kan logge ind bagefter. Hvis din konto blev oprettet gennem single sign-on, og du aldrig har indstillet en adgangskode, skal du bruge **Glemt adgangskode** på login-siden for først at sætte en (dette kræver, at serveren kan sende e-mails). Hvis serveren kun tillader login gennem en udbyder, kan den sidste linkede konto ikke fjernes.

## Udseende

Kontroller visningspræferencer gemt på din enhed.

### Sprog

Vælg sproget for Gramps Web-grænsefladen. Sprogindstillingen gemmes i browserens lokale lager og gælder kun for den aktuelle enhed.

### Tema

Vælg mellem:

- **System** – følger operativsystemets lys/mørk præference (standard)
- **Lys** – brug altid lys tema
- **Mørk** – brug altid mørk tema

Temaindstillingen gemmes i browserens lokale lager.

### Præferencer for slægtstræ

#### Standard visning af slægtstræ

Indstiller, hvilken diagramtype der åbnes som standard, når du navigerer til siden [Slægtstræ](tree.md). Mulighederne er Forfædrediagram, Efterkommerdiagram, Timeglasdiagram, Forholddiagram og Fan-diagram.

Denne præference gemmes i browserens lokale lager.

## Udviklerværktøjer

### API-token

Kopierer dit nuværende sessionstoken til udklipsholderen. Tokenet kan bruges til at godkende direkte mod REST API'et, for eksempel i den interaktive Swagger UI, der serveres af din Gramps Web-instans på `/api/swagger-ui`.

Klik på **Start Swagger** for at åbne Swagger UI i en ny fane med din session allerede tilgængelig.

!!! note
    Sessionstokenet er kortvarigt. Kopier det straks, før du bruger det i Swagger, da det kan udløbe.
