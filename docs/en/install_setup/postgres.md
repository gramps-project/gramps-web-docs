# Using a PostgreSQL database

By default, Gramps Web stores each family tree in its own SQLite database file. This needs no additional service, backups are as simple as copying files, and it works well for most installations, including ones [hosting multiple trees](multi-tree.md).

Alternatively, family trees can be hosted on a PostgreSQL server using the SharedPostgreSQL addon, which keeps all trees in a single database. This can make sense if you already run a PostgreSQL server and want to manage backups and monitoring there, or if you expect many users editing at the same time. PostgreSQL can also host the [user database](#using-a-postgresql-database-for-the-user-database) and the [search index](#using-a-postgresql-database-for-the-search-index), independently of where the family trees are stored.

!!! warning "PostgreSQL addon deprecated"
    The older PostgreSQL addon, which stores a single family tree per database, is deprecated and will no longer be supported in a future version of Gramps Web API. If you are using it, see [Moving a tree from the PostgreSQL addon to SharedPostgreSQL](#moving-a-tree-from-the-postgresql-addon-to-sharedpostgresql).

## Setting up the PostgreSQL server

The easiest option is to run the PostgreSQL server in a container on the same Docker host as Gramps Web, using Docker Compose.

Gramps needs locales installed on the PostgreSQL server to sort objects correctly in different languages, and the default PostgreSQL images do not include any. The [`gramps-postgres`](https://github.com/DavidMStraub/gramps-postgres-docker/) image adds them. To use it, add the following section to your `docker-compose.yml`:
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
and also add `postgres_data:` as key under the `volumes:` section of this YAML file. The image contains two databases, each with its own user and password: `gramps` for the genealogical data and `grampswebuser` for the Gramps Web user database.

If you use your own PostgreSQL server instead, create a database named `gramps` that the configured user can create tables in, and make sure the locales your users need are installed.

## Configuring Gramps Web

New family trees are created in the SharedPostgreSQL database when Gramps Web runs in [multi-tree mode](multi-tree.md) and the `NEW_DB_BACKEND` config option is set to `sharedpostgresql`. With the Docker Compose setup above, add the following under the `environment:` key of the `grampsweb` service in `docker-compose.yml`:

```yaml
      # enable multi-tree mode
      GRAMPSWEB_TREE: "*"
      GRAMPSWEB_MEDIA_PREFIX_TREE: true
      # create new trees in the SharedPostgreSQL database
      GRAMPSWEB_NEW_DB_BACKEND: sharedpostgresql
      # The host and port of the PostgreSQL server. The
      # host is the name of the PostgreSQL service above
      GRAMPSWEB_POSTGRES_HOST: postgres_gramps
      GRAMPSWEB_POSTGRES_PORT: 5432
      # The credentials must agree with the ones used for
      # the PostgreSQL container
      GRAMPSWEB_POSTGRES_USER: gramps
      GRAMPSWEB_POSTGRES_PASSWORD: postgres_password_gramps
```

See [Configuration](configuration.md) for a description of all these options. Note that host and port are saved with each tree when it is created, so changing them later only affects new trees.

## Creating a tree and importing data

To create a new tree, POST to the `/trees/` endpoint as described in [Setup for hosting multiple trees](multi-tree.md#create-a-new-tree). The response contains the ID of the new tree, which you need to [create the tree owner account](../administration/owner.md#multi-tree-setup-create-tree-owner-account).

Once the tree owner has logged in, they can [import](../administration/import.md) an existing family tree, e.g. a Gramps XML file exported from Gramps Desktop, via the web interface.

## Using a PostgreSQL database for the user database

The user database is usually an SQLite file, regardless of where the family trees are hosted. To use PostgreSQL instead, set the `USER_DB_URI` config option to a PostgreSQL database URL. With the `gramps-postgres` image above, use its `grampswebuser` database:
```
postgresql://grampswebuser:postgres_password_gramps_user@postgres_gramps:5432/grampswebuser
```

## Using a PostgreSQL database for the search index

The search index is also stored in SQLite by default. To use PostgreSQL instead, set the `SEARCH_INDEX_DB_URI` config option to a PostgreSQL database URL. With the `gramps-postgres` image above, you can use its `gramps` database, whether or not your family trees are hosted there as well:
```
postgresql://gramps:postgres_password_gramps@postgres_gramps:5432/gramps
```

## Moving a tree from the PostgreSQL addon to SharedPostgreSQL

Older installations may host their family tree with the PostgreSQL addon, which stores a single tree per database and is deprecated. To find out which addon a tree uses, look at the file `database.txt` in the tree's subdirectory of the Gramps database directory: it contains `postgresql` for the deprecated PostgreSQL addon and `sharedpostgresql` for SharedPostgreSQL.

To move a tree from the PostgreSQL addon to SharedPostgreSQL within the same installation, keeping your user accounts and media files:

1. [Back up your family tree](../administration/export.md#back-up-your-family-tree) as a Gramps XML (`.gramps`) file, using an account that can view private records.
2. Change your configuration as described in [Configuring Gramps Web](#configuring-gramps-web). You can keep using your existing `gramps-postgres` container.
3. [Create a new tree](multi-tree.md#create-a-new-tree) and note its tree ID.
4. Assign your existing user accounts to the new tree, as described in [Migrate existing user database](multi-tree.md#migrate-existing-user-database).
5. Move your media files to the location expected for the new tree, as described in [Migrate existing media files](multi-tree.md#migrate-existing-media-files).
6. Log in and [import](../administration/import.md) the Gramps XML file into the new tree.

Keep the Gramps XML file until you have checked that the new tree is complete.

If you are moving to a separate Gramps Web installation instead, follow the steps in [Move to a different Gramps Web instance](../administration/export.md#move-to-a-different-gramps-web-instance).

## Issues

In case of issues, please monitor the log output of Gramps Web and the PostgreSQL server. In the case of docker, this is achieved with

```
docker compose logs grampsweb
docker compose logs postgres_gramps
```

If you suspect there is an issue with Gramps Web (or the documentation), please file an issue [on Github](https://github.com/gramps-project/gramps-web-api/issues).
