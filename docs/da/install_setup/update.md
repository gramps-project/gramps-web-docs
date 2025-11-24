# Opdater Gramps Web

Hvis du bruger en af installationsmetoderne baseret på Docker Compose, er det enkelt at opdatere Gramps Web til den nyeste version. I den mappe, hvor din `docker-compose.yml` er placeret, skal du køre følgende kommandoer

```bash
docker compose pull
docker compose up -d
```

For mindre versionsspring af [Gramps Web API](https://github.com/gramps-project/gramps-web-api) er dette alt, hvad der er nødvendigt. Følg dog [udgivelsesnoterne for Gramps Web API](https://github.com/gramps-project/gramps-web-api/releases), da der kan være breaking changes, der kræver yderligere opmærksomhed eller konfigurationsændringer.

Bemærk, at det standard `grampsweb:latest` docker-billede altid kombinerer den nyeste version af API'et med den nyeste version af frontend'en. Hvis du ønsker at opgradere de to komponenter separat - hvilket er muligt - er der brug for en mere involveret opsætning end beskrevet her.
