# Limitar o uso de CPU e memória

Na configuração recomendada baseada em docker, o Gramps Web usa [Gunicorn](https://gunicorn.org/) para servir o
backend e [Celery](https://docs.celeryq.dev) para tarefas em segundo plano. Em ambos os casos, vários processos
de trabalho podem ser executados em paralelo, o que torna a aplicação mais responsiva do ponto de vista do usuário.
No entanto, aumentar o número de trabalhadores também aumenta a quantidade de RAM utilizada (mesmo quando a aplicação está ociosa)
e permitir que as solicitações sejam processadas em paralelo pode levar a um alto uso de CPU (em particular quando muitos usuários
estão usando a aplicação simultaneamente). Tanto o Gunicorn quanto o Celery permitem limitar o número de trabalhadores paralelos.

## Obter informações sobre seu sistema

No Linux, você pode verificar o número de núcleos disponíveis em seu sistema com o seguinte comando:

```bash
lscpu | grep CPU
```

Para ver quanto de memória e espaço de swap você tem disponível, use

```bash
free -h
```


## Limitando o número de trabalhadores do Gunicorn

A maneira mais fácil de definir o número de trabalhadores do Gunicorn ao usar a imagem docker padrão do Gramps Web
é definir a variável de ambiente `GUNICORN_NUM_WORKERS`, por exemplo, declarando-a
no arquivo `docker-compose.yml`,
sob "environment".

```yaml
services:
  grampsweb:
    environment:
      GUNICORN_NUM_WORKERS: 2
```

Consulte [a documentação do Gunicorn](https://docs.gunicorn.org/en/stable/design.html#how-many-workers) para decidir
sobre o número ideal de trabalhadores.



## Limitando o número de trabalhadores do Celery

Para definir o número de trabalhadores do Celery, adapte a configuração `concurrency` no arquivo Docker compose:

```yaml
  grampsweb_celery:
    command: celery -A gramps_webapi.celery worker --loglevel=INFO --concurrency=2
```

Consulte [a documentação do Celery](https://docs.celeryq.dev/en/stable/userguide/workers.html#concurrency) para decidir
sobre o número ideal de trabalhadores.

!!! info
    Se a flag `concurrency` for omitida (o que era o caso na documentação do Gramps Web até a v2.5.0), ela
    assume o número de núcleos de CPU disponíveis no sistema, o que pode consumir uma quantidade substancial de memória.
