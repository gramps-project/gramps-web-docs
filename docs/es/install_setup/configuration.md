# Configuración del servidor

Con la imagen de Docker predeterminada, toda la configuración necesaria se puede realizar desde el navegador. Sin embargo, dependiendo del despliegue, puede ser necesario personalizar la configuración del servidor.

Esta página enumera todos los métodos para cambiar la configuración y todas las opciones de configuración existentes.


## Archivo de configuración frente a variables de entorno

Para la configuración, puedes usar un archivo de configuración o variables de entorno.

Cuando usas la [configuración basada en Docker Compose](deployment.md), puedes incluir un archivo de configuración añadiendo el siguiente elemento de lista bajo la clave `volumes:` en el bloque `grampsweb:`:

```yaml
      - /path/to/config.cfg:/app/config/config.cfg
```
donde `/path/to/config.cfg` es la ruta al archivo de configuración en el sistema de archivos de tu servidor (el lado derecho hace referencia a la ruta dentro del contenedor y no debe cambiarse).

Al usar variables de entorno:

- antepone `GRAMPSWEB_` a cada nombre de configuración para obtener el nombre de la variable de entorno
- usa dos guiones bajos para las opciones de configuración de diccionarios anidados; por ejemplo, `GRAMPSWEB_THUMBNAIL_CACHE_CONFIG__CACHE_DEFAULT_TIMEOUT` establecerá el valor de la opción de configuración `THUMBNAIL_CACHE_CONFIG['CACHE_DEFAULT_TIMEOUT']`

Ten en cuenta que las opciones de configuración establecidas mediante el entorno tienen prioridad sobre las del archivo de configuración. Si están presentes ambas, la variable de entorno «gana».

!!! warning "Las variables de entorno sin prefijo están obsoletas"
    Por razones históricas, todavía se pueden establecer algunos valores de configuración —`TREE`, `SECRET_KEY`, `USER_DB_URI`, `POSTGRES_USER`, `POSTGRES_PASSWORD`, `MEDIA_BASE_DIR`, `SEARCH_INDEX_DIR`, `EMAIL_HOST`, `EMAIL_PORT`, `EMAIL_HOST_USER`, `EMAIL_HOST_PASSWORD`, `DEFAULT_FROM_EMAIL`, `BASE_URL` y `STATIC_PATH`— mediante una variable de entorno *sin* el prefijo `GRAMPSWEB_`. Esto está obsoleto, registra una advertencia al iniciar y dejará de funcionar en una versión futura. Usa siempre la forma con prefijo; por ejemplo, `GRAMPSWEB_TREE` en lugar de `TREE`.

    Ten en cuenta que esto solo afecta a las variables de entorno. En un archivo de configuración, los nombres de las opciones siempre se usan sin prefijo.

!!! tip "Comprobar las opciones obsoletas"
    Las opciones de configuración obsoletas de las que tu servidor todavía depende —como las variables de entorno sin prefijo, `SEARCH_INDEX_DIR` o `EMAIL_USE_TLS`— se registran como advertencias al iniciar. Desde Gramps Web API 3.22, también aparecen, junto con su sustituto y la versión en la que se eliminará la compatibilidad, en la parte superior de la página **Información del sistema** (accesible mediante el icono de usuario de la barra superior de la aplicación) cuando hayas iniciado sesión como administrador.

    Allí también aparecen la configuración del correo electrónico y la URL base que el asistente de primera ejecución de versiones anteriores almacenaba en la base de datos. Establécelas en tu configuración con los valores almacenados; la advertencia desaparecerá cuando coincidan.

## Opciones de configuración existentes
Existen las siguientes opciones de configuración.

### Opciones obligatorias

Clave | Descripción
----|-------------
`TREE` | El nombre de la base de datos del árbol genealógico que se utilizará. Muestra los árboles disponibles con `gramps -l`. Si no existe un árbol con este nombre, se creará uno nuevo vacío.
`SECRET_KEY` | La clave secreta de Flask. El secreto no debe compartirse públicamente. Cambiarla invalidará todos los tokens de acceso.
`USER_DB_URI` | La URL de la base de datos de usuarios. Se permite cualquier URL compatible con SQLAlchemy.

!!! info
    Puedes generar una clave secreta segura, por ejemplo, con el comando

    ```
    python3 -c "import secrets;print(secrets.token_urlsafe(32))"
    ```

### Opciones opcionales

Clave | Descripción
----|-------------
`MEDIA_BASE_DIR` | Ruta que se utilizará como directorio base para los archivos multimedia, reemplazando el directorio base de medios establecido en Gramps. Al usar [S3](s3.md), debe tener el formato `s3://<bucket_name>`
`TREE_ID` | Nombre del directorio de la base de datos del árbol genealógico que se utilizará en el modo de árbol único (cuando `TREE` no está establecido en `*`). Cuando se establece, el servidor identifica el árbol por su nombre de directorio en lugar de su nombre mostrado, lo que ofrece mayor resistencia a los cambios de nombre. Es obligatorio si quieres cambiar el nombre del árbol mediante la API. El nombre del directorio se puede encontrar mediante `GET /api/trees/-` (el campo `id`).
`SEARCH_INDEX_DB_URI` | URL de la base de datos para el índice de búsqueda. Solo se permiten `sqlite` o `postgresql` como backends. El valor predeterminado es `sqlite:///indexdir/search_index.db`, que crea un archivo SQLite en la carpeta `indexdir`, relativa a la ruta desde la que se ejecuta el script
`SEARCH_INDEX_DIR` | **Obsoleto** (usa `SEARCH_INDEX_DB_URI` en su lugar). Directorio que contiene el índice de búsqueda. Si se establece mientras `SEARCH_INDEX_DB_URI` no está definido, la URL del índice de búsqueda se deriva como `sqlite:///<SEARCH_INDEX_DIR>/search_index.db`.
`STATIC_PATH` | Ruta desde la que se servirán los archivos estáticos (por ejemplo, un frontend web estático)
`BASE_URL` | URL base desde la que se puede acceder a la API (por ejemplo, `https://mygramps.mydomain.com/`). Es necesaria, por ejemplo, para crear enlaces correctos de restablecimiento de contraseña. Web Push también requiere una URL HTTPS accesible públicamente; el valor predeterminado `http://localhost/` desactiva Web Push. Al configurar esta opción mediante el entorno, usa `GRAMPSWEB_BASE_URL`.
`CORS_ORIGINS` | Orígenes desde los que se permiten solicitudes CORS. De forma predeterminada, todos están bloqueados. Usa `"*"` para permitir solicitudes desde cualquier dominio.
`EMAIL_HOST` | Host del servidor SMTP (por ejemplo, para enviar correos electrónicos de restablecimiento de contraseña)
`EMAIL_PORT` | Puerto del servidor SMTP. El valor predeterminado es 465
`EMAIL_HOST_USER` | Nombre de usuario del servidor SMTP
`EMAIL_HOST_PASSWORD` | Contraseña del servidor SMTP
`EMAIL_USE_TLS` | **Obsoleto** (usa `EMAIL_USE_SSL` o `EMAIL_USE_STARTTLS` en su lugar). Booleano que indica si se debe usar TLS para enviar correos electrónicos. El valor predeterminado es `True`. Al usar STARTTLS, establece este valor en `False` y usa un puerto distinto de 25.
`EMAIL_USE_SSL` | Booleano que indica si se debe usar SSL/TLS implícito para SMTP (v3.6.0+). El valor predeterminado es `True` si `EMAIL_USE_TLS` no se establece explícitamente. Normalmente se usa con el puerto 465.
`EMAIL_USE_STARTTLS` | Booleano que indica si se debe usar STARTTLS explícito para SMTP (v3.6.0+). El valor predeterminado es `False`. Normalmente se usa con el puerto 587 o 25.
`DEFAULT_FROM_EMAIL` | Dirección «De» para los correos electrónicos automatizados
`THUMBNAIL_CACHE_CONFIG` | Diccionario con las opciones de configuración de la caché de miniaturas. Consulta [Flask-Caching](https://flask-caching.readthedocs.io/en/latest/) para conocer las opciones disponibles.
`REQUEST_CACHE_CONFIG` | Diccionario con las opciones de configuración de la caché de solicitudes. Consulta [Flask-Caching](https://flask-caching.readthedocs.io/en/latest/) para conocer las opciones disponibles.
`PERSISTENT_CACHE_CONFIG` | Diccionario con las opciones de configuración de la caché persistente, utilizada, por ejemplo, para la telemetría. Consulta [Flask-Caching](https://flask-caching.readthedocs.io/en/latest/) para conocer las opciones disponibles.
`CELERY_CONFIG` | Opciones de configuración de la cola de tareas en segundo plano de Celery. Consulta [Celery](https://docs.celeryq.dev/en/stable/userguide/configuration.html) para conocer las opciones disponibles.
`REPORT_DIR` | Directorio temporal donde se almacenará el resultado de ejecutar informes de Gramps
`EXPORT_DIR` | Directorio temporal donde se almacenará el resultado de exportar la base de datos de Gramps
`BACKUP_DIR` | Directorio donde se almacenan las [copias de seguridad](../administration/backups.md), en un subdirectorio por árbol (v3.24.0+). Si no se establece (valor predeterminado), no se pueden almacenar copias de seguridad en el servidor, aunque sí se pueden restaurar desde un archivo cargado. Usa una ubicación persistente, como un volumen de Docker, y preferiblemente una que también tenga su propia copia de seguridad o esté sincronizada en otro lugar.
`BACKUP_KEEP` | Número de copias de seguridad almacenadas que se conservan por árbol; las más antiguas se eliminan cuando se crea una nueva copia de seguridad (v3.24.0+). El valor predeterminado es `5`
`RATE_LIMIT_BACKUP` | Límite de frecuencia para crear copias de seguridad, por árbol (v3.24.0+). El valor predeterminado es `"10 per day"`
`RATE_LIMIT_MEDIA_ARCHIVE` | Límite de frecuencia para crear archivos multimedia en la página de Exportación. El valor predeterminado es `"1 per hour"`
`REGISTRATION_DISABLED` | Si es `True`, impide el registro de nuevos usuarios (valor predeterminado `False`). Desde Gramps Web API 3.26, la página de inicio de sesión también oculta su enlace de registro.
`PROXY_FIX_X_FOR` | Número de proxies inversos de confianza situados delante de Gramps Web (v3.26.0+). Establécelo en `1` detrás de un único proxy inverso para que los límites de frecuencia se apliquen por cliente en lugar de a todos los usuarios conjuntamente. El valor predeterminado es `0`. Establécelo únicamente si se puede acceder al servidor exclusivamente a través de estos proxies.
`DISABLE_TELEMETRY` | Si es `True`, desactiva la telemetría de estadísticas (valor predeterminado `False`). Consulta [telemetría](telemetry.md) para obtener más información.
`PILLOW_MAX_IMAGE_PIXELS` | Establece el parámetro `PIL.Image.MAX_IMAGE_PIXELS`, que indica el número de píxeles que puede contener la imagen procesada. Consulta la [documentación](https://pillow.readthedocs.io/en/stable/reference/Image.html#PIL.Image.MAX_IMAGE_PIXELS) para obtener más información.
`MAX_THUMBNAIL_FILE_BYTES` | Establece un tamaño máximo estricto para los archivos de miniaturas. El valor predeterminado es `50 * 1024 * 1024` (50 MB). Aumentarlo puede incrementar considerablemente el uso de memoria y provocar fallos por falta de memoria o pérdida de datos si se descomprimen archivos grandes en memoria.


!!! info
    Al usar variables de entorno para la configuración, las opciones booleanas como `EMAIL_USE_SSL` deben ser exactamente la cadena `true` o `false` (distinguiendo mayúsculas y minúsculas).


### Opciones para bases de datos PostgreSQL

Estas opciones son obligatorias si tus árboles genealógicos están alojados en una [base de datos PostgreSQL](postgres.md) mediante el complemento SharedPostgreSQL.

Clave | Descripción
----|-------------
`POSTGRES_USER` | Nombre de usuario para la conexión a la base de datos
`POSTGRES_PASSWORD` | Contraseña del usuario de la base de datos


### Opciones relevantes para alojar varios árboles

Las siguientes opciones son relevantes al [alojar varios árboles](multi-tree.md).


Clave | Descripción
----|-------------
`MEDIA_PREFIX_TREE` | Booleano que indica si se debe usar una subcarpeta independiente para los archivos multimedia de cada árbol. El valor predeterminado es `False`, pero se recomienda encarecidamente usar `True` en una configuración con varios árboles
`NEW_DB_BACKEND` | Backend de base de datos que se utilizará para los árboles genealógicos nuevos. Debe ser `sqlite` o `sharedpostgresql`. El valor predeterminado es `sqlite`. El valor `postgresql` todavía se acepta, pero está obsoleto, ya que el backend de PostgreSQL se eliminará en Gramps Web API 4.0.
`POSTGRES_HOST` | Nombre del host del servidor PostgreSQL utilizado para crear árboles nuevos al usar una configuración con varios árboles y el backend SharedPostgreSQL
`POSTGRES_PORT` | Puerto del servidor PostgreSQL utilizado para crear árboles nuevos al usar una configuración con varios árboles y el backend SharedPostgreSQL


### Opciones para la autenticación OIDC

Estas opciones son necesarias si quieres usar la autenticación OpenID Connect (OIDC) con proveedores externos. Para obtener instrucciones detalladas de configuración y ejemplos, consulta [Autenticación OIDC](oidc.md).

Clave | Descripción
----|-------------
`OIDC_ENABLED` | Booleano que indica si se debe habilitar la autenticación OIDC. El valor predeterminado es `False`.
`OIDC_ISSUER` | URL del emisor del proveedor OIDC (para proveedores OIDC personalizados)
`OIDC_CLIENT_ID` | ID de cliente de OAuth (para proveedores OIDC personalizados)
`OIDC_CLIENT_SECRET` | Secreto del cliente de OAuth (para proveedores OIDC personalizados)
`OIDC_NAME` | Nombre de visualización personalizado para el proveedor. El valor predeterminado es «OIDC»
`OIDC_SCOPES` | Ámbitos de OAuth. El valor predeterminado es «openid email profile»
`OIDC_USERNAME_CLAIM` | Afirmación que se utilizará para el nombre de usuario. El valor predeterminado es «preferred_username»
`OIDC_OPENID_CONFIG_URL` | Opcional: URL del endpoint de configuración de OpenID Connect (si no se usa `/.well-known/openid-configuration` estándar)
`OIDC_PKCE` | Booleano que indica si se debe usar PKCE. Si no se establece, se usa PKCE cuando el documento de descubrimiento del proveedor incluye `S256`. Consulta [PKCE](oidc.md#pkce)
`OIDC_DISABLE_LOCAL_AUTH` | Booleano que indica si se debe desactivar la autenticación local mediante nombre de usuario y contraseña. El valor predeterminado es `False`
`OIDC_AUTO_REDIRECT` | Booleano que indica si se debe redirigir automáticamente a OIDC cuando solo hay un proveedor configurado. El valor predeterminado es `False`
`OIDC_ALLOWED_REDIRECT_URIS` | Lista de URI `https` en las que las aplicaciones nativas pueden recibir el resultado del inicio de sesión (v3.26.0+), establecida como una lista JSON en una variable de entorno. Vacía de forma predeterminada. Solo es necesaria si la documentación de una aplicación nativa la solicita. Consulta [Aplicaciones nativas](oidc.md#native-apps)

#### Proveedores OIDC integrados

Para los proveedores integrados (Google, Microsoft), usa estas opciones:

Clave | Descripción
----|-------------
`OIDC_GOOGLE_CLIENT_ID` | ID de cliente para OAuth de Google
`OIDC_GOOGLE_CLIENT_SECRET` | Secreto del cliente para OAuth de Google
`OIDC_MICROSOFT_CLIENT_ID` | ID de cliente para OAuth de Microsoft
`OIDC_MICROSOFT_CLIENT_SECRET` | Secreto del cliente para OAuth de Microsoft
`OIDC_GOOGLE_PKCE` | Booleano, configuración de PKCE para Google; consulta [PKCE](oidc.md#pkce)
`OIDC_MICROSOFT_PKCE` | Booleano, configuración de PKCE para Microsoft; consulta [PKCE](oidc.md#pkce)

#### Asignación de roles OIDC

Estas opciones permiten asignar grupos/roles OIDC de tu proveedor de identidad a roles de usuario de Gramps Web:

Clave | Descripción
----|-------------
`OIDC_ROLE_CLAIM` | Nombre de la afirmación en el token OIDC que contiene los grupos/roles del usuario. El valor predeterminado es «groups»
`OIDC_GROUP_ADMIN` | Nombre del grupo/rol de tu proveedor OIDC que se asigna al rol «Admin» de Gramps
`OIDC_GROUP_OWNER` | Nombre del grupo/rol de tu proveedor OIDC que se asigna al rol «Owner» de Gramps
`OIDC_GROUP_EDITOR` | Nombre del grupo/rol de tu proveedor OIDC que se asigna al rol «Editor» de Gramps
`OIDC_GROUP_CONTRIBUTOR` | Nombre del grupo/rol de tu proveedor OIDC que se asigna al rol «Contributor» de Gramps
`OIDC_GROUP_MEMBER` | Nombre del grupo/rol de tu proveedor OIDC que se asigna al rol «Member» de Gramps
`OIDC_GROUP_GUEST` | Nombre del grupo/rol de tu proveedor OIDC que se asigna al rol «Guest» de Gramps

### Opciones solo para las funciones de IA

Estas opciones son necesarias si quieres usar el chat de IA. Consulta [Configurar el chat de IA](chat.md) para obtener más información.

!!! note
    Las opciones `VECTOR_EMBEDDING_MODEL`, `VECTOR_EMBEDDING_BASE_URL` y `VECTOR_EMBEDDING_API_KEY` para la búsqueda semántica se ignoran desde Gramps Web API 3.25, que eliminó la búsqueda semántica. El chat de IA solo necesita `LLM_MODEL`.

Clave | Descripción
----|-------------
`LLM_BASE_URL` | URL base de la API de chat compatible con OpenAI. El valor predeterminado es `None`, que usa la API de OpenAI.
`LLM_MODEL` | Modelo que se utilizará para la API de chat compatible con OpenAI. Si no se establece (valor predeterminado), el chat se desactiva. Desde la v3.6.0, el asistente de IA usa Pydantic AI con capacidades de llamada a herramientas.
`LLM_MAX_OUTPUT_TOKENS` | Número máximo de tokens que el modelo puede generar en una sola respuesta. No se establece de forma predeterminada, por lo que el límite queda a cargo del servidor del modelo. Es útil para servidores de modelos que no tienen un límite propio, donde de otro modo una respuesta podría continuar indefinidamente.
`LLM_MAX_CONTEXT_LENGTH` | Límite de caracteres para el contexto del árbol genealógico proporcionado al LLM. El valor predeterminado es 50000.
`LLM_SYSTEM_PROMPT` | Prompt del sistema personalizado para el asistente de chat LLM (v3.6.0+). Si no se establece, se usa el prompt predeterminado optimizado para genealogía.
`LLM_VISION` | Booleano que indica si los usuarios pueden adjuntar imágenes a sus preguntas (v3.26.0+). Habilítalo únicamente si el modelo acepta imágenes. El valor predeterminado es `False`. Consulta [Imágenes en las preguntas](chat.md#images-in-questions)
`LLM_ALLOW_WRITE_PROPOSALS` | Booleano que indica si el asistente puede proponer cambios en el árbol para que los usuarios los revisen y apliquen (v3.26.0+). El valor predeterminado es `False`. Consulta [Permitir que el asistente proponga cambios](chat.md#letting-the-assistant-propose-changes)


## Ejemplo de archivo de configuración

Un archivo de configuración mínimo para producción podría tener este aspecto:
```python
TREE="My Family Tree"
BASE_URL="https://mytree.example.com"
SECRET_KEY="..."  # your secret key
USER_DB_URI="sqlite:////path/to/users.sqlite"
EMAIL_HOST="mail.example.com"
EMAIL_PORT=465
EMAIL_USE_SSL=True  # Use implicit SSL for port 465
EMAIL_HOST_USER="gramps@example.com"
EMAIL_HOST_PASSWORD="..." # your SMTP password
DEFAULT_FROM_EMAIL="gramps@example.com"
```
