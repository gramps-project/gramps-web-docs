# 限制 CPU 和内存使用

在推荐的基于 Docker 的设置中，Gramps Web 使用 [Gunicorn](https://gunicorn.org/) 来提供后端服务，并使用 [Celery](https://docs.celeryq.dev) 处理后台任务。在这两种情况下，可以并行运行多个工作进程，这使得应用程序在用户的角度上更加响应。然而，增加工作进程的数量也会增加使用的 RAM 量（即使在应用程序空闲时），并且允许请求并行处理可能导致高 CPU 使用率（尤其是在许多用户同时使用应用程序时）。Gunicorn 和 Celery 都允许限制并行工作进程的数量。

## 获取系统信息

在 Linux 上，您可以使用以下命令检查系统上可用的核心数量：

```bash
lscpu | grep CPU
```

要查看您可用的内存和交换空间，请使用

```bash
free -h
```

## 限制 Gunicorn 工作进程的数量

使用默认的 Gramps Web Docker 镜像时，设置 Gunicorn 工作进程数量的最简单方法是设置环境变量 `GUNICORN_NUM_WORKERS`，例如通过在 `docker-compose.yml` 文件中声明它，在 "environment" 下。

```yaml
services:
  grampsweb:
    environment:
      GUNICORN_NUM_WORKERS: 2
```

请参阅 [Gunicorn 文档](https://docs.gunicorn.org/en/stable/design.html#how-many-workers) 来决定理想的工作进程数量。

## 限制 Celery 工作进程的数量

要设置 Celery 工作进程的数量，请在 Docker compose 文件中调整 `concurrency` 设置：

```yaml
  grampsweb_celery:
    command: celery -A gramps_webapi.celery worker --loglevel=INFO --concurrency=2
```

请参阅 [Celery 文档](https://docs.celeryq.dev/en/stable/userguide/workers.html#concurrency) 来决定理想的工作进程数量。

!!! info
    如果省略 `concurrency` 标志（在 Gramps Web 文档 v2.5.0 之前的情况），则默认为系统上可用的 CPU 核心数量，这可能会消耗大量内存。
