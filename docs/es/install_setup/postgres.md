# Uso de una base de datos PostgreSQL

Por defecto, Gramps Web almacena cada árbol genealógico en su propio archivo de base de datos SQLite. Esto no necesita ningún servicio adicional, las copias de seguridad son tan simples como copiar archivos, y funciona bien para la mayoría de las instalaciones, incluidas las que [albergan múltiples árboles](multi-tree.md).

Alternativamente, los árboles genealógicos pueden ser alojados en un servidor PostgreSQL utilizando el complemento SharedPostgreSQL, que mantiene todos los árboles en una sola base de datos. Esto puede tener sentido si ya estás ejecutando un servidor PostgreSQL y deseas gestionar las copias de seguridad y la monitorización allí, o si esperas que muchos usuarios editen al mismo tiempo. PostgreSQL también puede albergar la [base de datos de usuarios](#using-a-postgresql-database-for-the-user-database) y el [índice de búsqueda](#using-a-postgresql-database-for-the-search-index), independientemente de dónde se almacenen los árboles genealógicos.

!!! warning "Complemento de PostgreSQL obsoleto"
    El antiguo complemento de PostgreSQL, que almacena un solo árbol genealógico por base de datos, está obsoleto y no será compatible en una versión futura de la API de Gramps Web. Si lo estás utilizando, consulta [Mover un árbol del complemento de PostgreSQL a SharedPostgreSQL](#moving-a-tree-from-the-postgresql-addon-to-sharedpostgresql).

## Configurando el servidor PostgreSQL

La opción más fácil es ejecutar el servidor PostgreSQL en un contenedor en el mismo host de Docker que Gramps Web, utilizando Docker Compose.

Gramps necesita locales instalados en el servidor PostgreSQL para ordenar objetos correctamente en diferentes idiomas, y las imágenes predeterminadas de PostgreSQL no incluyen ninguna. La imagen [`gramps-postgres`](https://github.com/DavidMStraub/gramps-postgres-docker/) las añade. Para usarla, agrega la siguiente sección a tu `docker-compose.yml`:
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
y también agrega `postgres_data:` como clave bajo la sección `volumes:` de este archivo YAML. La imagen contiene dos bases de datos, cada una con su propio usuario y contraseña: `gramps` para los datos genealógicos y `grampswebuser` para la base de datos de usuarios de Gramps Web.

Si utilizas tu propio servidor PostgreSQL en su lugar, crea una base de datos llamada `gramps` en la que el usuario configurado pueda crear tablas, y asegúrate de que las locales que necesitan tus usuarios estén instaladas.

## Configurando Gramps Web

Nuevos árboles genealógicos se crean en la base de datos SharedPostgreSQL cuando Gramps Web se ejecuta en [modo multi-árbol](multi-tree.md) y la opción de configuración `NEW_DB_BACKEND` está establecida en `sharedpostgresql`. Con la configuración de Docker Compose anterior, agrega lo siguiente bajo la clave `environment:` del servicio `grampsweb` en `docker-compose.yml`:

```yaml
      # habilitar modo multi-árbol
      GRAMPSWEB_TREE: "*"
      GRAMPSWEB_MEDIA_PREFIX_TREE: true
      # crear nuevos árboles en la base de datos SharedPostgreSQL
      GRAMPSWEB_NEW_DB_BACKEND: sharedpostgresql
      # El host y el puerto del servidor PostgreSQL. El
      # host es el nombre del servicio de PostgreSQL arriba
      GRAMPSWEB_POSTGRES_HOST: postgres_gramps
      GRAMPSWEB_POSTGRES_PORT: 5432
      # Las credenciales deben coincidir con las utilizadas para
      # el contenedor de PostgreSQL
      GRAMPSWEB_POSTGRES_USER: gramps
      GRAMPSWEB_POSTGRES_PASSWORD: postgres_password_gramps
```

Consulta [Configuración](configuration.md) para una descripción de todas estas opciones. Ten en cuenta que el host y el puerto se guardan con cada árbol cuando se crea, por lo que cambiarlos más tarde solo afecta a los nuevos árboles.

## Creando un árbol e importando datos

Para crear un nuevo árbol, realiza un POST al endpoint `/trees/` como se describe en [Configuración para alojar múltiples árboles](multi-tree.md#create-a-new-tree). La respuesta contiene el ID del nuevo árbol, que necesitas para [crear la cuenta del propietario del árbol](../administration/owner.md#multi-tree-setup-create-tree-owner-account).

Una vez que el propietario del árbol haya iniciado sesión, puede [importar](../administration/import.md) un árbol genealógico existente, por ejemplo, un archivo XML de Gramps exportado desde Gramps Desktop, a través de la interfaz web.

## Usando una base de datos PostgreSQL para la base de datos de usuarios

La base de datos de usuarios suele ser un archivo SQLite, independientemente de dónde se alojen los árboles genealógicos. Para usar PostgreSQL en su lugar, establece la opción de configuración `USER_DB_URI` a una URL de base de datos PostgreSQL. Con la imagen `gramps-postgres` anterior, utiliza su base de datos `grampswebuser`:
```
postgresql://grampswebuser:postgres_password_gramps_user@postgres_gramps:5432/grampswebuser
```

## Usando una base de datos PostgreSQL para el índice de búsqueda

El índice de búsqueda también se almacena en SQLite por defecto. Para usar PostgreSQL en su lugar, establece la opción de configuración `SEARCH_INDEX_DB_URI` a una URL de base de datos PostgreSQL. Con la imagen `gramps-postgres` anterior, puedes usar su base de datos `gramps`, ya sea que tus árboles genealógicos estén alojados allí o no:
```
postgresql://gramps:postgres_password_gramps@postgres_gramps:5432/gramps
```

## Moviendo un árbol del complemento de PostgreSQL a SharedPostgreSQL

Las instalaciones más antiguas pueden alojar su árbol genealógico con el complemento de PostgreSQL, que almacena un solo árbol por base de datos y está obsoleto. Para averiguar qué complemento utiliza un árbol, mira el archivo `database.txt` en el subdirectorio del árbol en el directorio de la base de datos de Gramps: contiene `postgresql` para el complemento de PostgreSQL obsoleto y `sharedpostgresql` para SharedPostgreSQL.

Para mover un árbol del complemento de PostgreSQL a SharedPostgreSQL dentro de la misma instalación, manteniendo tus cuentas de usuario y archivos multimedia:

1. [Haz una copia de seguridad de tu árbol genealógico](../administration/export.md#back-up-your-family-tree) como un archivo XML de Gramps (`.gramps`), utilizando una cuenta que pueda ver registros privados.
2. Cambia tu configuración como se describe en [Configurando Gramps Web](#configuring-gramps-web). Puedes seguir utilizando tu contenedor `gramps-postgres` existente.
3. [Crea un nuevo árbol](multi-tree.md#create-a-new-tree) y anota su ID de árbol.
4. Asigna tus cuentas de usuario existentes al nuevo árbol, como se describe en [Migrar base de datos de usuarios existente](multi-tree.md#migrate-existing-user-database).
5. Mueve tus archivos multimedia a la ubicación esperada para el nuevo árbol, como se describe en [Migrar archivos multimedia existentes](multi-tree.md#migrate-existing-media-files).
6. Inicia sesión e [importa](../administration/import.md) el archivo XML de Gramps en el nuevo árbol.

Mantén el archivo XML de Gramps hasta que hayas verificado que el nuevo árbol está completo.

Si te estás moviendo a una instalación separada de Gramps Web, sigue los pasos en [Mover a una instancia diferente de Gramps Web](../administration/export.md#move-to-a-different-gramps-web-instance).

## Problemas

En caso de problemas, por favor monitorea la salida del registro de Gramps Web y del servidor PostgreSQL. En el caso de Docker, esto se logra con

```
docker compose logs grampsweb
docker compose logs postgres_gramps
```

Si sospechas que hay un problema con Gramps Web (o la documentación), por favor reporta un problema [en Github](https://github.com/gramps-project/gramps-web-api/issues).
