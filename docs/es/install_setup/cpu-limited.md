# Limitar el uso de CPU y memoria

En la configuración recomendada basada en Docker, Gramps Web utiliza [Gunicorn](https://gunicorn.org/) para servir el
backend y [Celery](https://docs.celeryq.dev) para tareas en segundo plano. En ambos casos, se pueden ejecutar varios procesos de trabajo en paralelo, lo que hace que la aplicación sea más receptiva desde la perspectiva del usuario. Sin embargo, aumentar el número de trabajadores también incrementa la cantidad de RAM utilizada (incluso cuando la aplicación está inactiva) y permitir que las solicitudes se procesen en paralelo puede llevar a un alto uso de CPU (en particular cuando muchos usuarios están utilizando la aplicación simultáneamente). Tanto Gunicorn como Celery permiten limitar el número de trabajadores en paralelo.

## Obtener información sobre su sistema

En Linux, puede verificar el número de núcleos disponibles en su sistema con el siguiente comando:

```bash
lscpu | grep CPU
```

Para ver cuánta memoria y espacio de intercambio tiene disponible, use

```bash
free -h
```


## Limitar el número de trabajadores de Gunicorn

La forma más sencilla de establecer el número de trabajadores de Gunicorn al usar la imagen de Docker predeterminada de Gramps Web es configurar la variable de entorno `GUNICORN_NUM_WORKERS`, por ejemplo, declarándola en el archivo `docker-compose.yml`, bajo "environment".

```yaml
services:
  grampsweb:
    environment:
      GUNICORN_NUM_WORKERS: 2
```

Consulte [la documentación de Gunicorn](https://docs.gunicorn.org/en/stable/design.html#how-many-workers) para decidir
sobre el número ideal de trabajadores.



## Limitar el número de trabajadores de Celery

Para establecer el número de trabajadores de Celery, adapte la configuración de `concurrency` en el archivo de Docker compose:

```yaml
  grampsweb_celery:
    command: celery -A gramps_webapi.celery worker --loglevel=INFO --concurrency=2
```

Consulte [la documentación de Celery](https://docs.celeryq.dev/en/stable/userguide/workers.html#concurrency) para decidir
sobre el número ideal de trabajadores.

!!! info
    Si se omite la opción `concurrency` (que fue el caso en la documentación de Gramps Web hasta la v2.5.0), 
    se establece de forma predeterminada en el número de núcleos de CPU disponibles en el sistema, lo que podría consumir una cantidad sustancial de memoria.
