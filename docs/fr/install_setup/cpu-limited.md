# Limiter l'utilisation du CPU et de la mémoire

Dans la configuration recommandée basée sur Docker, Gramps Web utilise [Gunicorn](https://gunicorn.org/) pour servir le backend et [Celery](https://docs.celeryq.dev) pour les tâches en arrière-plan. Dans les deux cas, plusieurs processus de travail peuvent être exécutés en parallèle, ce qui rend l'application plus réactive du point de vue de l'utilisateur. Cependant, augmenter le nombre de travailleurs augmente également la quantité de RAM utilisée (même lorsque l'application est inactive) et permettre le traitement des requêtes en parallèle peut entraîner une forte utilisation du CPU (en particulier lorsque de nombreux utilisateurs utilisent l'application simultanément). Tant Gunicorn que Celery permettent de limiter le nombre de travailleurs parallèles.

## Obtenir des informations sur votre système

Sur Linux, vous pouvez vérifier le nombre de cœurs disponibles sur votre système avec la commande suivante :

```bash
lscpu | grep CPU
```

Pour voir combien de mémoire et d'espace d'échange vous avez disponible, utilisez

```bash
free -h
```


## Limiter le nombre de travailleurs Gunicorn

Le moyen le plus simple de définir le nombre de travailleurs Gunicorn lors de l'utilisation de l'image Docker par défaut de Gramps Web est de définir la variable d'environnement `GUNICORN_NUM_WORKERS`, par exemple en la déclarant dans le fichier `docker-compose.yml`, sous "environment".

```yaml
services:
  grampsweb:
    environment:
      GUNICORN_NUM_WORKERS: 2
```

Consultez [la documentation de Gunicorn](https://docs.gunicorn.org/en/stable/design.html#how-many-workers) pour décider du nombre idéal de travailleurs.



## Limiter le nombre de travailleurs Celery

Pour définir le nombre de travailleurs Celery, adaptez le paramètre `concurrency` dans le fichier Docker compose :

```yaml
  grampsweb_celery:
    command: celery -A gramps_webapi.celery worker --loglevel=INFO --concurrency=2
```

Consultez [la documentation de Celery](https://docs.celeryq.dev/en/stable/userguide/workers.html#concurrency) pour décider du nombre idéal de travailleurs.

!!! info
    Si le drapeau `concurrency` est omis (ce qui était le cas dans la documentation de Gramps Web jusqu'à la v2.5.0), il par défaut au nombre de cœurs CPU disponibles sur le système, ce qui pourrait consommer une quantité substantielle de mémoire.
