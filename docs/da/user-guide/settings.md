# Brugerindstillinger

Brugerindstillinger er tilgængelige via brugerikonet i den øverste app-bar, derefter **Brugerindstillinger**. Ændringer træder i kraft med det samme, medmindre andet er angivet.

## Brugerinformation

Viser dit **brugernavn** og nuværende **brugerrolle** (f.eks. Gæst, Medlem, Redaktør). Disse er kun til læsning.

## Sprog

Vælg sproget til Gramps Web-grænsefladen. Sprogindstillingen gemmes i browserens lokale lager og gælder kun for den aktuelle enhed.

## Tema

Vælg mellem:

- **System** – følger operativsystemets lys/mørk præference (standard)
- **Lys** – brug altid lys tema
- **Mørk** – brug altid mørk tema

Temaindstillingen gemmes i browserens lokale lager.

## Skift e-mail

Indtast en ny e-mailadresse og klik på **Send** for at opdatere adressen, der er knyttet til din konto. E-mailadressen bruges til nulstilling af adgangskoder og (hvis konfigureret) meddelelser.

## Skift adgangskode

Indtast din nuværende adgangskode og en ny adgangskode, og klik derefter på **Send**. Hvis du har glemt din nuværende adgangskode, skal du i stedet bruge **Glemt adgangskode**-linket på login-siden.

## Præferencer for slægtstræ

### Standardvisning af slægtstræ

Indstiller hvilken diagramtype der åbnes som standard, når du navigerer til [Slægtstræ](tree.md) siden. Mulighederne er Forfadertræ, Efterkommertræ, Timeglasdiagram, Forholdsdiagram og Fan-diagram.

Denne præference gemmes i browserens lokale lager.

## Udviklerværktøjer

### API-token

Kopierer dit nuværende sessionstoken til udklipsholderen. Tokenet kan bruges til at autentificere direkte mod REST API'en, for eksempel i den interaktive Swagger UI, der serveres af din Gramps Web-instans på `/api/swagger-ui`.

Klik på **Start Swagger** for at åbne Swagger UI i en ny fane med din session allerede tilgængelig.

!!! note
    Sessionstokenet er kortvarigt. Kopier det straks før du bruger det i Swagger, da det kan udløbe.
