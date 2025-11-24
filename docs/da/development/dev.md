---
hide:
  - toc
---

# Gramps Web udvikling: oversigt

Gramps Web er en webapplikation, der består af to komponenter, som udvikles separat:

- **Gramps Web API** er et RESTful API skrevet i Python og baseret på Flask. Kildekoden er hostet på [github.com/gramps-project/gramps-web-api](https://github.com/gramps-project/gramps-web-api/). Det håndterer databaseadgang og genealogiske funktioner direkte ved at udnytte Gramps Python-biblioteket. Det fungerer som backend for Gramps Web. For udviklingsdokumentation, se [Backend](backend/index.md).
- **Gramps Web Frontend** er en Javascript webapplikation, der fungerer som frontend til Gramps Web. Kildekoden er hostet på [github.com/gramps-project/gramps-web](https://github.com/gramps-project/gramps-web/). For udviklingsdokumentation, se [Frontend](frontend/index.md).

En bemærkning om versionering: Gramps Web API og Gramps Web frontend versioneres uafhængigt. I øjeblikket har "Gramps Web" &ndash; den samlede applikation &ndash; ikke et separat versionsnummer. Begge projekter overholder [SemVer](https://semver.org/).

Hvis du ikke er en Python- eller Javascript-udvikler, men stadig gerne vil bidrage til Gramps Web, kan du tjekke [Contribute](../contribute/contribute.md).
