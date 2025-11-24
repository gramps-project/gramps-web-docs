# Begræns CPU- og hukommelsesforbrug

I den anbefalede docker-baserede opsætning bruger Gramps Web [Gunicorn](https://gunicorn.org/) til at servere
backend og [Celery](https://docs.celeryq.dev) til baggrundsopgaver. I begge tilfælde kan flere arbejdere
køre parallelt, hvilket gør applikationen mere responsiv fra et brugerperspektiv.
Dog øger en stigning i antallet af arbejdere også mængden af RAM, der bruges (selv når applikationen er inaktiv)
og tillader behandling af anmodninger parallelt kan føre til høj CPU-brug (især når mange brugere
bruger applikationen samtidig). Både Gunicorn og Celery tillader at begrænse antallet af parallelle arbejdere.

## Få information om dit system

På Linux kan du tjekke antallet af kerner, der er tilgængelige på dit system med følgende kommando:

```bash
lscpu | grep CPU
```

For at se hvor meget hukommelse og swap-plads du har til rådighed, brug

```bash
free -h
```


## Begrænsning af antallet af Gunicorn-arbejdere

Den nemmeste måde at indstille antallet af Gunicorn-arbejdere, når du bruger det standard Gramps Web
docker-billede, er at sætte miljøvariablen `GUNICORN_NUM_WORKERS`, f.eks. ved at erklære den
i `docker-compose.yml` filen,
under "environment".

```yaml
services:
  grampsweb:
    environment:
      GUNICORN_NUM_WORKERS: 2
```

Se [Gunicorn-dokumentationen](https://docs.gunicorn.org/en/stable/design.html#how-many-workers) for at beslutte
om det ideelle antal arbejdere.



## Begrænsning af antallet af Celery-arbejdere

For at indstille antallet af Celery-arbejdere, tilpas `concurrency` indstillingen i Docker compose-filen:

```yaml
  grampsweb_celery:
    command: celery -A gramps_webapi.celery worker --loglevel=INFO --concurrency=2
```

Se [Celery-dokumentationen](https://docs.celeryq.dev/en/stable/userguide/workers.html#concurrency) for at beslutte
om det ideelle antal arbejdere.

!!! info
    Hvis `concurrency` flaget udelades (hvilket var tilfældet i Gramps Web-dokumentationen indtil v2.5.0), 
    defaultes det til antallet af CPU-kerner, der er tilgængelige på systemet, hvilket kan forbruge en betydelig mængde hukommelse.
