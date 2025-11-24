# Rajoita CPU- ja muistinkäyttöä

Suositellussa Docker-pohjaisessa asetuksessa Gramps Web käyttää [Gunicornia](https://gunicorn.org/) taustapalvelun tarjoamiseen ja [Celeryä](https://docs.celeryq.dev) taustatehtäviin. Molemmissa tapauksissa useita työntekijäprosesseja voidaan suorittaa rinnakkain, mikä tekee sovelluksesta käyttäjän näkökulmasta responsiivisemman. Kuitenkin työntekijöiden määrän lisääminen lisää myös käytetyn RAM-muistin määrää (jopa silloin, kun sovellus on käyttämättömänä) ja pyyntöjen käsittelyn salliminen rinnakkain voi johtaa korkeaan CPU-käyttöön (erityisesti silloin, kun monet käyttäjät käyttävät sovellusta samanaikaisesti). Sekä Gunicorn että Celery sallivat rinnakkaisten työntekijöiden määrän rajoittamisen.

## Hanki tietoa järjestelmästäsi

Linuxissa voit tarkistaa käytettävissä olevien ytimien määrän seuraavalla komennolla:

```bash
lscpu | grep CPU
```

Näet, kuinka paljon muistia ja swap-tilaa sinulla on käytettävissä, käytä

```bash
free -h
```


## Gunicorn-työntekijöiden määrän rajoittaminen

Helpoin tapa asettaa Gunicorn-työntekijöiden määrä käytettäessä oletus Gramps Web Docker -kuvaa on asettaa ympäristömuuttuja `GUNICORN_NUM_WORKERS`, esimerkiksi määrittämällä se `docker-compose.yml` -tiedostossa,
"environment"-osion alle.

```yaml
services:
  grampsweb:
    environment:
      GUNICORN_NUM_WORKERS: 2
```

Katso [Gunicornin dokumentaatiosta](https://docs.gunicorn.org/en/stable/design.html#how-many-workers) päättääksesi
ihanteellisesta työntekijöiden määrästä.



## Celery-työntekijöiden määrän rajoittaminen

Aseta Celery-työntekijöiden määrä mukauttamalla `concurrency`-asetusta Docker-compose-tiedostossa:

```yaml
  grampsweb_celery:
    command: celery -A gramps_webapi.celery worker --loglevel=INFO --concurrency=2
```

Katso [Celeryn dokumentaatiosta](https://docs.celeryq.dev/en/stable/userguide/workers.html#concurrency) päättääksesi
ihanteellisesta työntekijöiden määrästä.

!!! info
    Jos `concurrency`-lippua ei ole määritetty (mikä oli tilanne Gramps Web -dokumentaatiossa ennen v2.5.0), se
    oletusarvoisesti vastaa järjestelmän käytettävissä olevien CPU-ytimien määrää, mikä voi kuluttaa huomattavan määrän muistia.
