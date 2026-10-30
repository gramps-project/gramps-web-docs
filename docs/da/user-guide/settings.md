# Brugerindstillinger

Brugerindstillinger er tilgængelige via brugerikonet i den øverste app-bar, derefter **Brugerindstillinger**. Siden er organiseret i sammenklappelige sektioner. Ændringer træder i kraft med det samme, medmindre andet er angivet.

!!! note
    Ændringer i brugerindstillinger påvirker kun din egen konto. Indstillinger, der påvirker alle brugere af træet, administreres i [Administrationsindstillinger](../administration/settings.md).

## Konto

Dækker dine profiloplysninger, legitimationsoplysninger og kontosikkerhed.

### Brugeroplysninger

Viser dit **brugernavn** og nuværende **brugerrolle** (f.eks. Gæst, Medlem, Redaktør). Disse er kun til læsning.

### Skift e-mail

Indtast en ny e-mailadresse og klik på **Send** for at opdatere den adresse, der er knyttet til din konto. E-mailadressen bruges til nulstilling af adgangskoder og (hvis konfigureret) meddelelser.

### Skift adgangskode

Indtast din nuværende adgangskode og en ny adgangskode, og klik derefter på **Send**. Hvis du har glemt din nuværende adgangskode, skal du bruge **Glemt adgangskode**-linket på login-siden i stedet.

### Koblede loginmetoder

Hvis din server tilbyder single sign-on (se [OIDC-godkendelse](../install_setup/oidc.md)), kan du knytte en konto fra en udbyder, såsom Google eller din organisations login, til din Gramps Web-konto. Du kan derefter logge ind med den udbyder og lande i din eksisterende konto, med din rolle og dine redigeringer. Denne sektion vises kun, når single sign-on er aktiveret, og serveren understøtter linking (Gramps Web API 3.24 og senere).

For at knytte en konto skal du klikke på **Knyt med** og udbyderens navn, logge ind hos udbyderen, og du bliver derefter ført tilbage til dine indstillinger. Hvis du ikke har logget ind for nylig, bliver du bedt om at logge ind igen først.

En udbyderkonto kan kun knyttes til én Gramps Web-konto. Hvis du ser "Denne login er allerede knyttet til en anden konto", er den knyttet et andet sted, for eksempel til en konto, der blev oprettet, da du først loggede ind med den udbyder. En administrator kan slette den anden konto, hvorefter du kan knytte den til din.

For at afkoble en konto skal du klikke på **Afkobl**. Hvis det er din sidste knyttede loginmetode, skal du også indtaste din adgangskode, så du stadig kan logge ind bagefter. Hvis din konto blev oprettet gennem single sign-on, og du aldrig har indstillet en adgangskode, skal du bruge **Glemt adgangskode** på login-siden for først at indstille en (dette kræver, at serveren sender e-mails). Hvis serveren kun tillader login gennem en udbyder, kan den sidste knyttede konto ikke afkobles.

## Udseende

Kontrollerer visningspræferencer gemt på din enhed.

### Sprog

Vælg sproget til Gramps Web-grænsefladen. Sprogindstillingen gemmes i browserens lokale lager og gælder kun for den aktuelle enhed.

### Tema

Vælg mellem:

- **System** – følger operativsystemets lys/mørk præference (standard)
- **Lys** – brug altid det lyse tema
- **Mørk** – brug altid det mørke tema

Temaindstillingen gemmes i browserens lokale lager.

### Familietræ præferencer

#### Standard familietræ visning

Indstiller, hvilken diagramtype der åbnes som standard, når du navigerer til [Familietræ](tree.md) siden. Mulighederne er Forfædretræ, Efterkommertræ, Timeglasdiagram, Forholdsdiagram og Fan-diagram.

Denne præference gemmes i browserens lokale lager.

## Udviklerværktøjer

### API-token

Kopierer dit nuværende sessionstoken til udklipsholderen. Tokenet kan bruges til at godkende direkte mod REST API'en, for eksempel i den interaktive Swagger UI, der serveres af din Gramps Web-instans på `/api/swagger-ui`.

Klik på **Start Swagger** for at åbne Swagger UI i en ny fane med din session allerede tilgængelig.

!!! note
    Sessionstokenet er kortvarigt. Kopier det straks, før du bruger det i Swagger, da det kan udløbe.
