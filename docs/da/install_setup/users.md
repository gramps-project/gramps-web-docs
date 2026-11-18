# Bruger system

Gramps Web er ikke beregnet til at blive eksponeret på internettet for offentlig adgang, men kun af autentificerede brugere. Bruger konti kan oprettes af webstedsejeren via kommandolinjen eller webgrænsefladen, eller ved selvregistrering og efterfølgende godkendelse af webstedsejeren.

## Brugerroller

Følgende brugerroller er i øjeblikket defineret.

Role | Role ID | Permissions
-----|---------|------------
Gæst | 0 | Se ikke-private objekter
Medlem | 1 | Gæst + se private objekter
Bidragyder* | 2 | Medlem + tilføje objekter
Redaktør | 3 | Bidragyder + redigere og slette objekter
Ejer | 4 | Redaktør + administrere brugere
Admin | 5 | Ejer + redigere andre træer i multi-træ opsætning

Om en post er privat, indstilles pr. post, se [Private poster](../user-guide/privacy.md). Intet er privat som standard, ikke engang levende mennesker.

\* Bemærk, at "Bidragyder" rollen i øjeblikket kun er delvist understøttet; f.eks. kan familieobjekter ikke tilføjes, da de indebærer en ændring af de underliggende Gramps personobjekter for familiemedlemmer. Det anbefales at bruge de andre roller, når det er muligt.

## Konfigurere hvem der kan bruge AI chat

Hvis du har [konfigureret AI chat](chat.md), vil du se en mulighed her for at vælge, hvilke brugergrupper der har lov til at bruge chatfunktionen.

## Administrere brugere

Der er to måder at administrere brugere på:

- Med ejerrettigheder ved hjælp af webgrænsefladen
- På kommandolinjen på serveren

Den ejerkonto, der kræves for først at få adgang til webappen, kan tilføjes i onboarding-guiden, der automatisk startes, når du får adgang til Gramps Web med en tom brugerdatabase.

### Administrere brugere på kommandolinjen

Når du bruger [Docker Compose](deployment.md), er den grundlæggende kommando

```bash
docker compose run grampsweb python3 -m gramps_webapi user COMMAND [ARGS]
```

`COMMAND` kan være `add`, `set-password` eller `delete`. Brug `--help` for `[ARGS]` for at vise syntaksen og mulige konfigurationsmuligheder.

`set-password NAME` sætter en ny adgangskode for en eksisterende bruger uden at skulle bruge den gamle, for eksempel når ingen længere kan logge ind, og e-mail ikke er opsat til nulstilling af adgangskoder (Gramps Web API 3.26+). Det beder om adgangskoden to gange uden at vise den, så adgangskoden ikke ender i shell-historikken. Alle brugerens sessioner afsluttes.

### Godkende selvregistrerede brugere

Når en bruger selvregistrerer sig, får de ikke straks adgang. En e-mail sendes til træejeren om den nye brugerregistrering, og brugeren sendes en e-mailanmodning om at bekræfte deres e-mailadresse. At bekræfte deres e-mailadresse ændrer deres rolle fra `unconfirmed` til `disabled`. Mens brugerkontoen er i en af disse to roller, kan brugeren ikke logge ind. Træejeren skal gennemgå brugerens anmodning og tildele brugeren en passende rolle, før de får lov til at logge ind.
