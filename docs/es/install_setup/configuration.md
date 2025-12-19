# Configuración del Servidor

Usando la imagen de Docker predeterminada, toda la configuración necesaria se puede realizar desde el navegador. Sin embargo, dependiendo del despliegue, puede ser necesario personalizar la configuración del servidor.

Esta página enumera todos los métodos para cambiar la configuración y todas las opciones de configuración existentes.


## Archivo de configuración vs. variables de entorno

Para la configuración, puedes usar un archivo de configuración o variables de entorno.

Cuando utilizas la [configuración basada en Docker Compose](deployment.md), puedes incluir un archivo de configuración añadiendo el siguiente elemento de lista bajo la clave `volumes:` en el bloque `grampsweb:`:

```yaml
      - /ruta/a/config.cfg:/app/config/config.cfg
```
donde `/ruta/a/config.cfg` es la ruta al archivo de configuración en el sistema de archivos de tu servidor (el lado derecho se refiere a la ruta en el contenedor y no debe ser cambiado).

Al usar variables de entorno,

- prefija cada nombre de configuración con `GRAMPSWEB_` para obtener el nombre de la variable de entorno
- Usa dobles guiones bajos para configuraciones de diccionario anidadas, por ejemplo `GRAMPSWEB_THUMBNAIL_CACHE_CONFIG__CACHE_DEFAULT_TIMEOUT` establecerá el valor de la opción de configuración `THUMBNAIL_CACHE_CONFIG['CACHE_DEFAULT_TIMEOUT']`

Ten en cuenta que las opciones de configuración establecidas a través del entorno tienen prioridad sobre las que están en el archivo de configuración. Si ambas están presentes, la variable de entorno "gana".

## Configuraciones de configuración existentes
Las siguientes opciones de configuración existen.

### Configuraciones requeridas

Clave | Descripción
----|-------------
`TREE` | El nombre de la base de datos del árbol genealógico a utilizar. Muestra los árboles disponibles con `gramps -l`. Si no existe un árbol con este nombre, se creará uno nuevo vacío.
`SECRET_KEY` | La clave secreta para flask. La clave no debe ser compartida públicamente. Cambiarla invalidará todos los tokens de acceso.
`USER_DB_URI` | La URL de la base de datos de usuarios. Se permite cualquier URL compatible con SQLAlchemy.

!!! info
    Puedes generar una clave secreta segura, por ejemplo, con el comando

    ```
    python3 -c "import secrets;print(secrets.token_urlsafe(32))"
    ```

### Configuraciones opcionales

Clave | Descripción
----|-------------
`MEDIA_BASE_DIR` | Ruta a usar como directorio base para archivos multimedia, sobrescribiendo el directorio base de medios establecido en Gramps. Al usar [S3](s3.md), debe tener la forma `s3://<bucket_name>`
`SEARCH_INDEX_DB_URI` | URL de la base de datos para el índice de búsqueda. Solo se permiten `sqlite` o `postgresql` como backends. Por defecto es `sqlite:///indexdir/search_index.db`, creando un archivo SQLite en la carpeta `indexdir` relativa a la ruta donde se ejecuta el script
`STATIC_PATH` | Ruta para servir archivos estáticos (por ejemplo, un frontend web estático)
`BASE_URL` | URL base donde se puede acceder a la API (por ejemplo, `https://mygramps.mydomain.com/`). Esto es necesario, por ejemplo, para construir enlaces correctos de restablecimiento de contraseña
`CORS_ORIGINS` | Orígenes desde los cuales se permiten solicitudes CORS. Por defecto, todos están deshabilitados. Usa `"*"` para permitir solicitudes de cualquier dominio.
`EMAIL_HOST` | Host del servidor SMTP (por ejemplo, para enviar correos electrónicos de restablecimiento de contraseña)
`EMAIL_PORT` | Puerto del servidor SMTP. por defecto es 465
`EMAIL_HOST_USER` | Nombre de usuario del servidor SMTP
`EMAIL_HOST_PASSWORD` | Contraseña del servidor SMTP
`EMAIL_USE_TLS` | **Obsoleto** (usa `EMAIL_USE_SSL` o `EMAIL_USE_STARTTLS` en su lugar). Booleano, si se debe usar TLS para enviar correos electrónicos. Por defecto es `True`. Al usar STARTTLS, establece esto en `False` y usa un puerto diferente de 25.
`EMAIL_USE_SSL` | Booleano, si se debe usar SSL/TLS implícito para SMTP (v3.6.0+). Por defecto es `True` si `EMAIL_USE_TLS` no se establece explícitamente. Típicamente se usa con el puerto 465.
`EMAIL_USE_STARTTLS` | Booleano, si se debe usar STARTTLS explícito para SMTP (v3.6.0+). Por defecto es `False`. Típicamente se usa con el puerto 587 o 25.
`DEFAULT_FROM_EMAIL` | Dirección "De" para correos electrónicos automatizados
`THUMBNAIL_CACHE_CONFIG` | Diccionario con configuraciones para la caché de miniaturas. Consulta [Flask-Caching](https://flask-caching.readthedocs.io/en/latest/) para posibles configuraciones.
`REQUEST_CACHE_CONFIG` | Diccionario con configuraciones para la caché de solicitudes. Consulta [Flask-Caching](https://flask-caching.readthedocs.io/en/latest/) para posibles configuraciones.
`PERSISTENT_CACHE_CONFIG` | Diccionario con configuraciones para la caché persistente, utilizada por ejemplo para telemetría. Consulta [Flask-Caching](https://flask-caching.readthedocs.io/en/latest/) para posibles configuraciones.
`CELERY_CONFIG` | Configuraciones para la cola de tareas en segundo plano de Celery. Consulta [Celery](https://docs.celeryq.dev/en/stable/userguide/configuration.html) para posibles configuraciones.
`REPORT_DIR` | Directorio temporal donde se almacenará la salida de los informes de Gramps
`EXPORT_DIR` | Directorio temporal donde se almacenará la salida de la exportación de la base de datos de Gramps
`REGISTRATION_DISABLED` | Si `True`, deshabilita el registro de nuevos usuarios (por defecto `False`)
`DISABLE_TELEMETRY` | Si `True`, deshabilita la telemetría de estadísticas (por defecto `False`). Consulta [telemetría](telemetry.md) para más detalles.


!!! info
    Al usar variables de entorno para la configuración, las opciones booleanas como `EMAIL_USE_TLS` deben ser la cadena `true` o `false` (sensible a mayúsculas y minúsculas!).


### Configuraciones solo para la base de datos backend de PostgreSQL

Esto es necesario si has configurado tu base de datos de Gramps para trabajar con el [complemento de PostgreSQL](https://gramps-project.org/wiki/index.php/Addon:PostgreSQL).

Clave | Descripción
----|-------------
`POSTGRES_USER` | El nombre de usuario para la conexión a la base de datos
`POSTGRES_PASSWORD` | La contraseña para el usuario de la base de datos


### Configuraciones relevantes para alojar múltiples árboles

Las siguientes configuraciones son relevantes al [alojar múltiples árboles](multi-tree.md).


Clave | Descripción
----|-------------
`MEDIA_PREFIX_TREE` | Booleano, si se debe usar una subcarpeta separada para los archivos multimedia de cada árbol. Por defecto es `False`, pero se recomienda encarecidamente usar `True` en una configuración de múltiples árboles
`NEW_DB_BACKEND` | El backend de base de datos a utilizar para los árboles genealógicos recién creados. Debe ser uno de `sqlite`, `postgresql` o `sharedpostgresql`. Por defecto es `sqlite`.
`POSTGRES_HOST` | El nombre del host del servidor PostgreSQL utilizado para crear nuevos árboles cuando se utiliza una configuración de múltiples árboles con el backend SharedPostgreSQL
`POSTGRES_PORT` | El puerto del servidor PostgreSQL utilizado para crear nuevos árboles cuando se utiliza una configuración de múltiples árboles con el backend SharedPostgreSQL


### Configuraciones para autenticación OIDC

Estas configuraciones son necesarias si deseas usar autenticación OpenID Connect (OIDC) con proveedores externos. Para instrucciones de configuración detalladas y ejemplos, consulta [Autenticación OIDC](oidc.md).

Clave | Descripción
----|-------------
`OIDC_ENABLED` | Booleano, si se debe habilitar la autenticación OIDC. Por defecto es `False`.
`OIDC_ISSUER` | URL del emisor del proveedor OIDC (para proveedores OIDC personalizados)
`OIDC_CLIENT_ID` | ID de cliente OAuth (para proveedores OIDC personalizados)
`OIDC_CLIENT_SECRET` | Secreto de cliente OAuth (para proveedores OIDC personalizados)
`OIDC_NAME` | Nombre de visualización personalizado para el proveedor. Por defecto es "OIDC"
`OIDC_SCOPES` | Alcances de OAuth. Por defecto es "openid email profile"
`OIDC_USERNAME_CLAIM` | La reclamación a usar para el nombre de usuario. Por defecto es "preferred_username"
`OIDC_OPENID_CONFIG_URL` | Opcional: URL al endpoint de configuración de OpenID Connect (si no se utiliza el estándar `/.well-known/openid-configuration`)
`OIDC_DISABLE_LOCAL_AUTH` | Booleano, si se debe deshabilitar la autenticación local de nombre de usuario/contraseña. Por defecto es `False`
`OIDC_AUTO_REDIRECT` | Booleano, si se debe redirigir automáticamente a OIDC cuando solo se configura un proveedor. Por defecto es `False`

#### Proveedores OIDC integrados

Para proveedores integrados (Google, Microsoft, GitHub), usa estas configuraciones:

Clave | Descripción
----|-------------
`OIDC_GOOGLE_CLIENT_ID` | ID de cliente para Google OAuth
`OIDC_GOOGLE_CLIENT_SECRET` | Secreto de cliente para Google OAuth
`OIDC_MICROSOFT_CLIENT_ID` | ID de cliente para Microsoft OAuth
`OIDC_MICROSOFT_CLIENT_SECRET` | Secreto de cliente para Microsoft OAuth
`OIDC_GITHUB_CLIENT_ID` | ID de cliente para GitHub OAuth
`OIDC_GITHUB_CLIENT_SECRET` | Secreto de cliente para GitHub OAuth

#### Mapeo de Roles OIDC

Estas configuraciones te permiten mapear grupos/roles OIDC de tu proveedor de identidad a roles de usuario de Gramps Web:

Clave | Descripción
----|-------------
`OIDC_ROLE_CLAIM` | El nombre de la reclamación en el token OIDC que contiene los grupos/roles del usuario. Por defecto es "groups"
`OIDC_GROUP_ADMIN` | El nombre del grupo/rol de tu proveedor OIDC que se mapea al rol "Admin" de Gramps
`OIDC_GROUP_OWNER` | El nombre del grupo/rol de tu proveedor OIDC que se mapea al rol "Owner" de Gramps
`OIDC_GROUP_EDITOR` | El nombre del grupo/rol de tu proveedor OIDC que se mapea al rol "Editor" de Gramps
`OIDC_GROUP_CONTRIBUTOR` | El nombre del grupo/rol de tu proveedor OIDC que se mapea al rol "Contributor" de Gramps
`OIDC_GROUP_MEMBER` | El nombre del grupo/rol de tu proveedor OIDC que se mapea al rol "Member" de Gramps
`OIDC_GROUP_GUEST` | El nombre del grupo/rol de tu proveedor OIDC que se mapea al rol "Guest" de Gramps

### Configuraciones solo para funciones de IA

Estas configuraciones son necesarias si deseas usar funciones impulsadas por IA como chat o búsqueda semántica.

Clave | Descripción
----|-------------
`LLM_BASE_URL` | URL base para la API de chat compatible con OpenAI. Por defecto es `None`, lo que utiliza la API de OpenAI.
`LLM_MODEL` | El modelo a usar para la API de chat compatible con OpenAI. Si no se establece (el valor por defecto), el chat está deshabilitado. A partir de la v3.6.0, el asistente de IA utiliza Pydantic AI con capacidades de llamada a herramientas.
`VECTOR_EMBEDDING_MODEL` | El modelo de [Sentence Transformers](https://sbert.net/) a utilizar para embeddings de vectores de búsqueda semántica. Si no se establece (el valor por defecto), la búsqueda semántica y el chat están deshabilitados.
`LLM_MAX_CONTEXT_LENGTH` | Límite de caracteres para el contexto del árbol genealógico proporcionado al LLM. Por defecto es 50000.
`LLM_SYSTEM_PROMPT` | Prompt del sistema personalizado para el asistente de chat LLM (v3.6.0+). Si no se establece, utiliza el prompt optimizado para genealogía por defecto.


## Ejemplo de archivo de configuración

Un archivo de configuración mínimo para producción podría verse así:
```python
TREE="Mi Árbol Genealógico"
BASE_URL="https://mitree.ejemplo.com"
SECRET_KEY="..."  # tu clave secreta
USER_DB_URI="sqlite:////ruta/a/usuarios.sqlite"
EMAIL_HOST="mail.ejemplo.com"
EMAIL_PORT=465
EMAIL_USE_SSL=True  # Usar SSL implícito para el puerto 465
EMAIL_HOST_USER="gramps@ejemplo.com"
EMAIL_HOST_PASSWORD="..." # tu contraseña SMTP
DEFAULT_FROM_EMAIL="gramps@ejemplo.com"
