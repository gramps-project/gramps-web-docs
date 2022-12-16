# Limit CPU usage

In order to avoid high CPU/RAM usage, it is possible to set the number of workers
using the environment variable `GUNICORN_NUM_WORKERS`.

Here, we will take a number of workers = 2. Adgust it according to your needs.
It may be a good idea to check the CPU/Threads available before choosing the value:

> lscpu | grep CPU

The easiest way is to declare the variable in the `docker-compose.yml` file,
under the "environment".

```
version: "3.7"
services:
  grampsweb:
    environment:
      GUNICORN_NUM_WORKERS: 2
```

Other ways are possible, for example by storing the variable in a file, 
and calling it in the startup command:

> docker compose --env-file ./env up

In this case, the `env` file would contain a single line: GUNICORN_NUM_WORKERS=2