# Limit CPU usage

In order to avoid high CPU (and therefore) RAM usage, it is possible to 
use the environment variable `GUNICORN_NUM_WORKERS`

The easiest was is to declare the variable in the `docker-compose.yml` file:

```
version: "3.7"
services:
  grampsweb:
    image: ghcr.io/gramps-project/grampsweb:latest
    restart: always
    ports:
      - "80:5000"  # host:docker
    environment:
      TREE: "Gramps Web"  # will create a new tree if not exists
      GUNICORN_NUM_WORKERS: 2
    volumes:
      - gramps_users:/app/users  # persist user database
      - gramps_index:/app/indexdir  # persist search index
      - gramps_thumb_cache:/app/thumbnail_cache  # persist thumbnails
      - gramps_secret:/app/secret  # persist flask secret
      - gramps_db:/root/.gramps/grampsdb  # persist Gramps database
      - gramps_media:/app/media  # persist media files
volumes:
  gramps_users:
  gramps_index:
  gramps_thumb_cache:
  gramps_secret:
  gramps_db:
  gramps_media:
```

Other was are possible, see [the docker documentation](https://docs.docker.com/compose/environment-variables/)

Using the declaration when calling the command:

	- docker compose --env-file ./env up

In this case, the `env` file would contain, as example, a single line: GUNICORN_NUM_WORKERS=2