---
hide:
  - navigation
---

Hvis du støder på problemer eller har brug for hjælp med Gramps Web, så vælg en af de følgende muligheder.

[Forum :material-forum:](https://gramps.discourse.group/c/gramps-web/){ .md-button }
[Backend problemer :material-github:](https://github.com/gramps-project/gramps-web-api/issues){ .md-button }
[Frontend problemer :material-github:](https://github.com/gramps-project/gramps-web/issues){ .md-button }

Se nedenfor for nogle retningslinjer om, hvor du skal starte.

## Stille spørgsmål

Det officielle Gramps Discourse forum har en [separat kategori for Gramps Web](https://gramps.discourse.group/c/gramps-web/). Brug venligst denne til at stille eventuelle spørgsmål, du måtte have om Gramps Web, for eksempel

- Spørgsmål om brugen af Gramps Web
- Spørgsmål om konfigurationen af Gramps Web
- Fejlfinding af en deployment af Gramps Web
- Ideer til forbedringer af Gramps Web
- ...

## Rapportere problemer

Hvis du støder på et problem, som du mener er en fejl i Gramps Web, så rapporter det via Github.

Der er to separate Github-repositorier for koden, der bruges i Gramps Web, et til brugergrænsefladen (“frontend”) og et til serverkoden (“backend”):

- [Frontend problemer](https://github.com/gramps-project/gramps-web/issues)
- [Backend problemer](https://github.com/gramps-project/gramps-web-api/issues)

Hvis du er usikker på, hvor du skal indgive et problem, så bekymr dig ikke og vælg blot en af de to – vedligeholderne vil kunne overføre problemet, hvis det er nødvendigt.

I begge tilfælde, så inkluder venligst altid følgende oplysninger i din rapport:

- Oplysninger om din opsætning (f.eks. en docker-compose fil med følsomme værdier redigeret, eller om du bruger en hosted version, såsom Grampshub, eller et forudkonfigureret billede, såsom DigitalOcean)
- Versionsoplysninger. For at få disse, gå til fanen "Systeminformation" på indstillingssiden i Gramps Web og kopier/indsæt værdierne i boksen, som bør se nogenlunde således ud:

```
Gramps 5.1.6
Gramps Web API 1.5.1
Gramps.js 24.1.0
locale: en
multi-tree: false
task queue: true
```

## Forslå forbedringer

For generelle ideer og diskussioner om fremtidige forbedringer, er du velkommen til at åbne en diskussion i [forumet](https://gramps.discourse.group/c/gramps-web/). Du kan også tjekke issuesiderne (se links ovenfor) for at se, om en bestemt funktion allerede er planlagt eller under udvikling.

For specifikke forbedringer med et begrænset omfang, er du velkommen til direkte at åbne et issue med en funktionsanmodning i det relevante frontend eller backend Github-repositorium.
