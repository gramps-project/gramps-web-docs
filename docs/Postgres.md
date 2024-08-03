# Using a PostgreSQL database

By default, Gramps uses a file-based SQLite database to store the family tree. This works perfectly fine for Gramps Web and is recommended for most users. However, starting with Gramps Web API version 0.3.0, also a PostgreSQL server with a single family tree per database is supported, powered by the [Gramps PostgreSQL Addon](https://gramps-project.org/wiki/index.php/Addon:PostgreSQL). Since [version 1.0.0](https://github.com/gramps-project/gramps-web-api/releases/tag/v1.0.0), also the SharedPostgreSQL Addon is supported, which allows hosting multiple family trees in a single database, which is particularly useful when used together with Gramps Web API [multi-tree support](https://www.grampsweb.org/multi-tree/).

## Setting up the PostgreSQL server

If you want to set up a new database for use with the PostgreSQLAddon, you can follow the [instructions in the Gramps Wiki](https://gramps-project.org/wiki/index.php/Addon:PostgreSQL) to set up the server.

Alternatively, you can also use Docker Compose to run the PostgreSQL server in a container on the same docker host as Gramps Web.

Using a dockerized PostgreSQL with Gramps is only complicated by the fact the the default PostgreSQL images do not have any locales installed, which are however needed by Gramps for localized collation of objects. The easiest option is to use the `gramps-postgres` image released in [this repository](https://github.com/DavidMStraub/gramps-postgres-docker/). To use it, add the following section to your `docker-compose.yml`:
```yaml
  postgres_gramps:
    image: ghcr.io/davidmstraub/gramps-postgres:latest
    restart: unless-stopped
    environment:
      POSTGRES_USER: gramps
      POSTGRES_PASSWORD: your_postgres_password
    volumes:
      - postgres_data:/var/lib/postgresql/data
```
and also add `postgres_data:` as key under the `volumes:` section of this YAML file.

## Importing a Gramps family tree

Again, if you have set up the PostgreSQL server yourself, you can follow the [instructions in the Gramps Wiki](https://gramps-project.org/wiki/index.php/Addon:PostgreSQL) to import a family tree into the database.

Alternatively, if you have followed the Docker Compose instructions above, you can use the following command to import a Gramps XML file located on your docker host:

```bash
docker-compose run --entrypoint "" grampsweb \
    gramps -C postgres \
    -i /root/.gramps/grampsdb/my_tree.gramps \
    --config=database.backend:postgresql \
    --config=database.host:postgres_gramps \
    --config=database.port:5432 \
    --username=postgres --password=your_postgres_password
```

## Configuring Web API for use with the database

To configure Web API for use with the PostgreSQL database, add the following under the `environment:` key of the `grampsweb` service in `docker-compose.yml`:

```yaml
      # the PostgreSQL addon assumes the tree name to be
      # equal to the database name and here the default 
      # database name of the PostgreSQL image is used
      TREE: postgres
      # The credentials must agree with the ones used for
      # the PostgreSQL container
      POSTGRES_USER: gramps
      POSTGRES_PASSWORD: your_postgres_password
```


## Issues

In case of issues, please monitor the log output of Gramps Web and the PostgreSQL server. In the case of docker, this is achieved with

```
docker-compose logs grampsweb
docker-compose logs postgres_grampsweb
```

If you suspect there is an issue with Gramps Web (or the documentation), please file an issue [on Github](https://github.com/gramps-project/gramps-web-api/issues).