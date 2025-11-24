# Uso de una base de datos PostgreSQL

Por defecto, Gramps utiliza una base de datos SQLite basada en archivos para almacenar el árbol genealógico. Esto funciona perfectamente bien para Gramps Web y se recomienda para la mayoría de los usuarios. Sin embargo, a partir de la versión 0.3.0 de la API de Gramps Web, también se admite un servidor PostgreSQL con un solo árbol genealógico por base de datos, impulsado por el [Complemento de PostgreSQL de Gramps](https://gramps-project.org/wiki/index.php/Addon:PostgreSQL). Desde la [versión 1.0.0](https://github.com/gramps-project/gramps-web-api/releases/tag/v1.0.0), también se admite el Complemento SharedPostgreSQL, que permite alojar múltiples árboles genealógicos en una sola base de datos, lo cual es particularmente útil cuando se utiliza junto con el [soporte para múltiples árboles](multi-tree.md) de la API de Gramps Web.

## Configuración del servidor PostgreSQL

Si deseas configurar una nueva base de datos para usar con el Complemento PostgreSQL, puedes seguir las [instrucciones en la Wiki de Gramps](https://gramps-project.org/wiki/index.php/Addon:PostgreSQL) para configurar el servidor.

Alternativamente, también puedes usar Docker Compose para ejecutar el servidor PostgreSQL en un contenedor en el mismo host de Docker que Gramps Web.

Usar un PostgreSQL dockerizado con Gramps solo se complica por el hecho de que las imágenes predeterminadas de PostgreSQL no tienen locales instalados, que son necesarios para la colación localizada de objetos por parte de Gramps. La opción más fácil es usar la imagen `gramps-postgres` publicada en [este repositorio](https://github.com/DavidMStraub/gramps-postgres-docker/). Para usarla, agrega la siguiente sección a tu `docker-compose.yml`:
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
y también agrega `postgres_data:` como clave bajo la sección `volumes:` de este archivo YAML. Esta imagen contiene una base de datos separada para los datos genealógicos de Gramps y para la base de datos de usuarios de Gramps; cada una puede tener contraseñas separadas.

## Importando un árbol genealógico de Gramps

Nuevamente, si has configurado el servidor PostgreSQL tú mismo, puedes seguir las [instrucciones en la Wiki de Gramps](https://gramps-project.org/wiki/index.php/Addon:PostgreSQL) para importar un árbol genealógico en la base de datos.

Alternativamente, si has seguido las instrucciones de Docker Compose anteriores, puedes usar el siguiente comando para importar un archivo XML de Gramps ubicado en tu host de Docker:

```bash
docker compose run --entrypoint "" grampsweb \
    gramps -C postgres \
    -i /root/.gramps/grampsdb/my_tree.gramps \
    --config=database.path:/root/.gramps/grampsdb \
    --config=database.backend:postgresql \
    --config=database.host:postgres_gramps \
    --config=database.port:5432 \
    --username=gramps --password=postgres_password_gramps
```

## Configurando la API Web para su uso con la base de datos

Para configurar la API Web para su uso con la base de datos PostgreSQL, agrega lo siguiente bajo la clave `environment:` del servicio `grampsweb` en `docker-compose.yml`:

```yaml
      # el complemento de PostgreSQL asume que el nombre del árbol es
      # igual al nombre de la base de datos y aquí se utiliza el nombre
      # de base de datos predeterminado de la imagen de PostgreSQL
      TREE: postgres
      # Las credenciales deben coincidir con las utilizadas para
      # el contenedor de PostgreSQL
      POSTGRES_USER: gramps
      POSTGRES_PASSWORD: postgres_password_gramps
```

## Uso de una base de datos PostgreSQL compartida en una instalación de múltiples árboles

Al usar una [configuración de múltiples árboles](multi-tree.md), el complemento SharedPostgreSQL es una opción conveniente para alojar todos los árboles, también los recién creados a través de la API, en una sola base de datos PostgreSQL sin comprometer la privacidad o la seguridad.

Para lograr esto, configura un contenedor basado en la imagen `gramps-postgres` como se describió anteriormente y simplemente establece la opción de configuración `NEW_DB_BACKEND` a `sharedpostgresql`, por ejemplo, a través de la variable de entorno `GRAMPSWEB_NEW_DB_BACKEND`.

## Uso de una base de datos PostgreSQL para la base de datos de usuarios

Independientemente de qué backend de base de datos se utilice para los datos genealógicos, la base de datos de usuarios puede ser alojada en una base de datos PostgreSQL proporcionando una URL de base de datos apropiada. La imagen de Docker `gramps-postgres` mencionada anteriormente contiene una base de datos separada `grampswebuser` que se puede usar para este propósito. En ese caso, el valor apropiado para la opción de configuración `USER_DB_URI` sería
```
postgresql://grampswebuser:postgres_password_gramps_user@postgres_gramps:5432/grampswebuser
```

## Uso de una base de datos PostgreSQL para el índice de búsqueda

Desde la versión 2.4.0 de la API de Gramps Web, el índice de búsqueda se aloja ya sea en una base de datos SQLite (la predeterminada) o en una base de datos PostgreSQL. También para este propósito, se puede usar la imagen `gramps-postgres`. Para el índice de búsqueda, podemos usar la base de datos `gramps` proporcionada por la imagen, independientemente de si estamos alojando nuestros datos genealógicos en PostgreSQL o no (el índice de búsqueda y los datos genealógicos pueden coexistir en la misma base de datos). Esto se puede lograr, en el ejemplo anterior, configurando la opción de configuración `SEARCH_INDEX_DB_URI` a
```
postgresql://gramps:postgres_password_gramps@postgres_gramps:5432/gramps
```

## Problemas

En caso de problemas, por favor monitorea la salida de registro de Gramps Web y del servidor PostgreSQL. En el caso de Docker, esto se logra con

```
docker compose logs grampsweb
docker compose logs postgres_grampsweb
```

Si sospechas que hay un problema con Gramps Web (o la documentación), por favor informa un problema [en Github](https://github.com/gramps-project/gramps-web-api/issues).
