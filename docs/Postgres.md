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
      POSTGRES_PASSWORD: postgres_password_admin
      POSTGRES_PASSWORD_GRAMPS: postgres_password_gramps
      POSTGRES_PASSWORD_GRAMPS_USER: postgres_password_gramps_user
    volumes:
      - postgres_data:/var/lib/postgresql/data
```
and also add `postgres_data:` as key under the `volumes:` section of this YAML file. This image contains a separate database for Gramps genealogical data and for the Gramps user database; they each can have separate passwords.

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
    --username=gramps --password=postgres_password_gramps
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
      POSTGRES_PASSWORD: postgres_password_gramps
```

## Using a shared PostgreSQL database in a multi-tree installation

When using a [multi-tree setup](https://www.grampsweb.org/multi-tree/), the SharedPostgreSQL addon is a convenient option to host all trees, also newly created ones via the API, in a single PostgreSQL database without compromising privacy or security.

To achieve this, set up a container based on the `gramps-postgres` image as described above and simply set the config option `NEW_DB_BACKEND` to `sharedpostgresql`, e.g. via the `GRAMPSWEB_NEW_DB_BACKEND` environment variable.

## Using a PostgreSQL database for the user database

Independently of which database backend is used for the genealogical data, the user database can be hosted in a PostgreSQL database by providing an appropriate database URL. The `gramps-postgres` docker image mentioned above contains a separate database `grampswebuser` that can be used for this purpose. In that case, the appropriate value for the `USER_DB_URI` config option would be
```
postgresql://grampswebuser:postgres_password_gramps_user@postgres_gramps:5432/grampswebuser
```

## Using a PostgreSQL database for the search index

Since Gramps Web API version 2.4.0, the search index is hosted either in an SQLite database (the default) or a PostgreSQL database. Also for this purpose, the `gramps-postgres` image can be used. For the search index, we can use the `gramps` database provided by the image, regardless of whether we are hosting our genealogical data in PostgreSQL or not (the search index and genealogical data can coexist in the same database). This can be achieved, in the above example, by setting the `SEARCH_INDEX_DB_URI` config option to
```
postgresql://gramps:postgres_password_gramps@postgres_gramps:5432/gramps
```


## Issues

In case of issues, please monitor the log output of Gramps Web and the PostgreSQL server. In the case of docker, this is achieved with

```
docker-compose logs grampsweb
docker-compose logs postgres_grampsweb
```

If you suspect there is an issue with Gramps Web (or the documentation), please file an issue [on Github](https://github.com/gramps-project/gramps-web-api/issues).