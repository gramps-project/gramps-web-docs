# Limit CPU and memory usage

In the recommended docker-based setup, Gramps Web uses [Gunicorn](https://gunicorn.org/) to serve the
backend and [Celery](https://docs.celeryq.dev) for background tasks. In both cases, several worker
processes can be run in parallel, which makes the application more responsive from a user perspective.
However, increasing the number of workers also increase the amount of RAM used (even when the application is idle)
and allowing requests to be processed in parallel can lead to high CPU usage (in particular when many users
are using the application simultaneously). Both Gunicorn and Celery allow to limit the number of parallel workers.

## Get information about your system

On Linux, you can check the number of cores available on your system with the following command:

```bash
lscpu | grep CPU
```

To see how much memory and swap space you have available, use

```bash
free -h
```


## Limiting the number of Gunicorn workers

The easiest way to set the number of Gunicorn workers when using the default Gramps Web
docker image is to set the environment variable `GUNICORN_NUM_WORKERS`, e.g. by declaring it
in the `docker-compose.yml` file,
under the "environment".

```yaml
services:
  grampsweb:
    environment:
      GUNICORN_NUM_WORKERS: 2
```

See [the Gunicorn documentation](https://docs.gunicorn.org/en/stable/design.html#how-many-workers) to decide
about the ideal number of workers.



## Limiting the number of Celery workers

To set the number of Celery workers, adapt the `concurrency` setting in the Docker compose file:

```yaml
  grampsweb_celery:
    command: celery -A gramps_webapi.celery worker --loglevel=INFO --concurrency=2
```

See [the Celery documentation](https://docs.celeryq.dev/en/stable/userguide/workers.html#concurrency) to decide
about the ideal number of workers.

!!! info
    If the `concurrency` flag is omitted (which was the case in the Gramps Web documentation until v2.5.0), it
    defaults to the number of CPU cores available on the system, which might consume a substantial amount of memory.