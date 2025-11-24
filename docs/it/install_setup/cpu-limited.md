# Limitare l'uso della CPU e della memoria

Nella configurazione consigliata basata su Docker, Gramps Web utilizza [Gunicorn](https://gunicorn.org/) per servire il
backend e [Celery](https://docs.celeryq.dev) per i compiti in background. In entrambi i casi, possono essere eseguiti
diversi processi worker in parallelo, il che rende l'applicazione più reattiva dal punto di vista dell'utente.
Tuttavia, aumentare il numero di worker aumenta anche la quantità di RAM utilizzata (anche quando l'applicazione è inattiva)
e consentire l'elaborazione delle richieste in parallelo può portare a un elevato utilizzo della CPU (in particolare
quando molti utenti utilizzano l'applicazione simultaneamente). Sia Gunicorn che Celery consentono di limitare il numero
di worker paralleli.

## Ottenere informazioni sul tuo sistema

Su Linux, puoi controllare il numero di core disponibili sul tuo sistema con il seguente comando:

```bash
lscpu | grep CPU
```

Per vedere quanta memoria e spazio di swap hai disponibile, usa

```bash
free -h
```

## Limitare il numero di worker di Gunicorn

Il modo più semplice per impostare il numero di worker di Gunicorn quando si utilizza l'immagine Docker predefinita di
Gramps Web è impostare la variabile di ambiente `GUNICORN_NUM_WORKERS`, ad esempio dichiarandola
nel file `docker-compose.yml`,
sotto la sezione "environment".

```yaml
services:
  grampsweb:
    environment:
      GUNICORN_NUM_WORKERS: 2
```

Consulta [la documentazione di Gunicorn](https://docs.gunicorn.org/en/stable/design.html#how-many-workers) per decidere
il numero ideale di worker.

## Limitare il numero di worker di Celery

Per impostare il numero di worker di Celery, adatta l'impostazione `concurrency` nel file Docker compose:

```yaml
  grampsweb_celery:
    command: celery -A gramps_webapi.celery worker --loglevel=INFO --concurrency=2
```

Consulta [la documentazione di Celery](https://docs.celeryq.dev/en/stable/userguide/workers.html#concurrency) per decidere
il numero ideale di worker.

!!! info
    Se il flag `concurrency` è omesso (cosa che è avvenuta nella documentazione di Gramps Web fino alla v2.5.0), esso
    predefinisce il numero di core CPU disponibili sul sistema, il che potrebbe consumare una quantità sostanziale di memoria.
