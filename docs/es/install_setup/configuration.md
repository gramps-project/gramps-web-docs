# Configuración del Servidor

Usando la imagen de Docker por defecto, toda la configuración necesaria se puede realizar desde el navegador. Sin embargo, dependiendo del despliegue, puede ser necesario personalizar la configuración del servidor.

Esta página enumera todos los métodos para cambiar la configuración y todas las opciones de configuración existentes.


## Archivo de configuración vs. variables de entorno

Para los ajustes, puedes usar un archivo de configuración o variables de entorno.

Cuando usas la [configuración basada en Docker Compose](deployment.md), puedes incluir un archivo de configuración añadiendo el siguiente elemento de lista bajo la clave `volumes:` en el bloque `grampsweb:`:

```yaml
      - /path/to/config.cfg:/app/config/config.cfg
```
donde `/path/to/config.cfg` es la ruta al archivo de configuración en el sistema de archivos de tu servidor (el lado derecho se refiere a la ruta en el contenedor y no debe ser cambiado).

Al usar variables de entorno,

- prefija cada nombre de ajuste con `GRAMPSWEB_` para obtener el nombre de la variable de entorno
- Usa dobles guiones bajos para los ajustes de diccionario anidados, por ejemplo, `GRAMPSWEB_THUMBNAIL_CACHE_CONFIG__CACHE_DEFAULT_TIMEOUT` establecerá el valor de la opción de configuración `THUMBNAIL_CACHE_CONFIG['CACHE_DEFAULT_TIMEOUT']`

Ten en cuenta que las opciones de configuración establecidas a través del entorno tienen prioridad sobre las que están en el archivo de configuración. Si ambas están presentes, la variable de entorno "gana".

!!! warning "Las variables de entorno sin prefijo están en desuso"
    Por razones históricas, un puñado de ajustes – `TREE`, `SECRET_KEY`, `USER_DB_URI`, `POSTGRES_USER`, `POSTGRES_PASSWORD`, `MEDIA_BASE_DIR`, `SEARCH_INDEX_DIR`, `EMAIL_HOST`, `EMAIL_PORT`, `EMAIL_HOST_USER`, `EMAIL_HOST_PASSWORD`, `DEFAULT_FROM_EMAIL`, `BASE_URL`, y `STATIC_PATH` – aún pueden ser establecidos a través de una variable de entorno *sin* el prefijo `GRAMPSWEB_`. Esto está en desuso, registra una advertencia al inicio y dejará de funcionar en una futura versión. Siempre usa la forma con prefijo, por ejemplo, `GRAMPSWEB_TREE` en lugar de `TREE`.

    Ten en cuenta que esto solo concierne a las variables de entorno. En un archivo de configuración, los nombres de los ajustes siempre se utilizan sin prefijo.

!!! tip "Verificando opciones en desuso"
    Las opciones de configuración en desuso de las que tu servidor aún depende – como las variables de entorno sin prefijo, `SEARCH_INDEX_DIR`, o `EMAIL_USE_TLS` – se registran como advertencias al inicio. Desde Gramps Web API 3.22, también se enumeran, junto con su reemplazo y la versión en la que se eliminará el soporte, en la parte superior de la página de **Información del Sistema** (accesible a través del ícono de usuario en la barra de la aplicación superior) cuando estás conectado como administrador.

    Los ajustes de correo electrónico y la URL base que el asistente de primera ejecución de versiones anteriores almacenó en la base de datos también se enumeran allí. Establece en tu configuración los valores almacenados; la advertencia desaparece una vez que coinciden.

## Ajustes de configuración existentes
Las siguientes opciones de configuración existen.

### Ajustes requeridos

Clave | Descripción
----|-------------
`TREE` | El nombre de la base de datos del árbol genealógico a usar. Muestra los árboles disponibles con `gramps -l`. Si un árbol con este nombre no existe, se creará uno nuevo vacío.
`SECRET_KEY` | La clave secreta para flask. La clave secreta no debe ser compartida públicamente. Cambiarla invalidará todos los tokens de acceso.
`USER_DB_URI` | La URL de la base de datos de usuarios. Se permite cualquier URL compatible con SQLAlchemy.

!!! info
    Puedes generar una clave secreta segura, por ejemplo, con el comando

    ```
    python3 -c "import secrets;print(secrets.token_urlsafe(32))"
    ```

### Ajustes opcionales

Clave | Descripción
----|-------------
`MEDIA_BASE_DIR` | Ruta a usar como directorio base para archivos multimedia, sobrescribiendo el directorio base de medios establecido en Gramps. Al usar [S3](s3.md), debe tener la forma `s3://<bucket_name>`
`TREE_ID` | El nombre del directorio de la base de datos del árbol genealógico a usar en modo de un solo árbol (cuando `TREE` no está configurado como `*`). Cuando se establece, el servidor identifica el árbol por su nombre de directorio en lugar de su nombre de visualización, lo que es más robusto ante cambios de nombre. Requerido si deseas renombrar el árbol a través de la API. El nombre del directorio se puede encontrar a través de `GET /api/trees/-` (el campo `id`).
`SEARCH_INDEX_DB_URI` | URL de la base de datos para el índice de búsqueda. Solo se permiten `sqlite` o `postgresql` como backends. Por defecto, se establece en `sqlite:///indexdir/search_index.db`, creando un archivo SQLite en la carpeta `indexdir` relativa a la ruta donde se ejecuta el script.
`SEARCH_INDEX_DIR` | **En desuso** (usa `SEARCH_INDEX_DB_URI` en su lugar). Directorio que contiene el índice de búsqueda. Si se establece mientras `SEARCH_INDEX_DB_URI` está sin establecer, la URL del índice de búsqueda se deriva como `sqlite:///<SEARCH_INDEX_DIR>/search_index.db`.
`STATIC_PATH` | Ruta para servir archivos estáticos (por ejemplo, un frontend web estático)
`BASE_URL` | URL base donde se puede alcanzar la API (por ejemplo, `https://mygramps.mydomain.com/`). Esto es necesario, por ejemplo, para construir enlaces de restablecimiento de contraseña correctos. Web Push también requiere una URL HTTPS accesible públicamente; el valor por defecto `http://localhost/` desactiva Web Push. Al configurar este ajuste a través del entorno, usa `GRAMPSWEB_BASE_URL`.
`CORS_ORIGINS` | Orígenes desde los cuales se permiten solicitudes CORS. Por defecto, todas están deshabilitadas. Usa `"*"` para permitir solicitudes de cualquier dominio.
`EMAIL_HOST` | Host del servidor SMTP (por ejemplo, para enviar correos electrónicos de restablecimiento de contraseña)
`EMAIL_PORT` | Puerto del servidor SMTP. por defecto es 465
`EMAIL_HOST_USER` | Nombre de usuario del servidor SMTP
`EMAIL_HOST_PASSWORD` | Contraseña del servidor SMTP
`EMAIL_USE_TLS` | **En desuso** (usa `EMAIL_USE_SSL` o `EMAIL_USE_STARTTLS` en su lugar). Booleano, si se debe usar TLS para enviar correos electrónicos. Por defecto es `True`. Al usar STARTTLS, establece esto en `False` y usa un puerto diferente de 25.
`EMAIL_USE_SSL` | Booleano, si se debe usar SSL/TLS implícito para SMTP (v3.6.0+). Por defecto es `True` si `EMAIL_USE_TLS` no se establece explícitamente. Típicamente se usa con el puerto 465.
`EMAIL_USE_STARTTLS` | Booleano, si se debe usar STARTTLS explícito para SMTP (v3.6.0+). Por defecto es `False`. Típicamente se usa con el puerto 587 o 25.
`DEFAULT_FROM_EMAIL` | Dirección "De" para correos electrónicos automatizados
`THUMBNAIL_CACHE_CONFIG` | Diccionario con ajustes para la caché de miniaturas. Consulta [Flask-Caching](https://flask-caching.readthedocs.io/en/latest/) para posibles ajustes.
`REQUEST_CACHE_CONFIG` | Diccionario con ajustes para la caché de solicitudes. Consulta [Flask-Caching](https://flask-caching.readthedocs.io/en/latest/) para posibles ajustes.
`PERSISTENT_CACHE_CONFIG` | Diccionario con ajustes para la caché persistente, utilizada, por ejemplo, para telemetría. Consulta [Flask-Caching](https://flask-caching.readthedocs.io/en/latest/) para posibles ajustes.
`CELERY_CONFIG` | Ajustes para la cola de tareas en segundo plano de Celery. Consulta [Celery](https://docs.celeryq.dev/en/stable/userguide/configuration.html) para posibles ajustes.
`REPORT_DIR` | Directorio temporal donde se almacenará la salida de los informes de Gramps
`EXPORT_DIR` | Directorio temporal donde se almacenará la salida de la exportación de la base de datos de Gramps
`BACKUP_DIR` | Directorio donde se almacenan [copias de seguridad](../administration/backups.md), en un subdirectorio por árbol (v3.24.0+). Si no se establece (el valor por defecto), las copias de seguridad no se pueden almacenar en el servidor, pero aún se pueden restaurar desde un archivo subido. Usa una ubicación persistente, por ejemplo, un volumen de Docker, y preferiblemente una que esté respaldada o sincronizada en otro lugar.
`BACKUP_KEEP` | Número de copias de seguridad almacenadas por árbol; las más antiguas se eliminan cuando se crea una nueva copia de seguridad (v3.24.0+). Por defecto es `5`
`RATE_LIMIT_BACKUP` | Límite de tasa para crear copias de seguridad, por árbol (v3.24.0+). Por defecto es `"10 por día"`
`RATE_LIMIT_MEDIA_ARCHIVE` | Límite de tasa para crear archivos multimedia en la página de Exportación. Por defecto es `"1 por hora"`
`REGISTRATION_DISABLED` | Si `True`, no se permite el registro de nuevos usuarios (por defecto `False`). Desde Gramps Web API 3.26, la página de inicio de sesión también oculta su enlace de registro.
`PROXY_FIX_X_FOR` | Número de proxies inversos de confianza frente a Gramps Web (v3.26.0+). Establecer en `1` detrás de un solo proxy inverso para que los límites de tasa se apliquen por cliente en lugar de a todos los usuarios juntos. Por defecto es `0`. Solo configúralo si el servidor es accesible exclusivamente a través de estos proxies.
`DISABLE_TELEMETRY` | Si `True`, desactiva la telemetría de estadísticas (por defecto `False`). Consulta [telemetría](telemetry.md) para más detalles.
`PILLOW_MAX_IMAGE_PIXELS` | Establece el parámetro PIL.Image.MAX_IMAGE_PIXELS, que indica el número de píxeles que la imagen procesada puede contener. Consulta [docs](https://pillow.readthedocs.io/en/stable/reference/Image.html#PIL.Image.MAX_IMAGE_PIXELS) para más detalles.
`MAX_THUMBNAIL_FILE_BYTES` | Establece un tamaño máximo de archivo duro para miniaturas. Por defecto es `50 * 1024 * 1024` (50 MB). Aumentarlo puede aumentar considerablemente el uso de memoria y puede llevar a fallos por falta de memoria o pérdida de datos si archivos grandes se descomprimen en memoria.


!!! info
    Al usar variables de entorno para la configuración, las opciones booleanas como `EMAIL_USE_SSL` deben ser ya sea la cadena `true` o `false` (¡sensible a mayúsculas!).


### Ajustes para bases de datos PostgreSQL

Estos ajustes son requeridos si tus árboles genealógicos están alojados en una [base de datos PostgreSQL](postgres.md) usando el complemento SharedPostgreSQL.

Clave | Descripción
----|-------------
`POSTGRES_USER` | El nombre de usuario para la conexión a la base de datos
`POSTGRES_PASSWORD` | La contraseña para el usuario de la base de datos


### Ajustes relevantes para alojar múltiples árboles

Los siguientes ajustes son relevantes al [alojar múltiples árboles](multi-tree.md).


Clave | Descripción
----|-------------
`MEDIA_PREFIX_TREE` | Booleano, si se debe usar o no una subcarpeta separada para los archivos multimedia de cada árbol. Por defecto es `False`, pero se recomienda encarecidamente usar `True` en una configuración de múltiples árboles.
`NEW_DB_BACKEND` | El backend de base de datos a usar para los árboles genealógicos recién creados. Debe ser uno de `sqlite` o `sharedpostgresql`. Por defecto es `sqlite`. El valor `postgresql` aún se acepta pero está en desuso, ya que el backend de PostgreSQL será eliminado en Gramps Web API 4.0.
`POSTGRES_HOST` | El nombre del host del servidor PostgreSQL utilizado para crear nuevos árboles al usar una configuración de múltiples árboles con el backend SharedPostgreSQL.
`POSTGRES_PORT` | El puerto del servidor PostgreSQL utilizado para crear nuevos árboles al usar una configuración de múltiples árboles con el backend SharedPostgreSQL.


### Ajustes para autenticación OIDC

Estos ajustes son necesarios si deseas usar autenticación OpenID Connect (OIDC) con proveedores externos. Para instrucciones detalladas de configuración y ejemplos, consulta [Autenticación OIDC](oidc.md).

Clave | Descripción
----|-------------
`OIDC_ENABLED` | Booleano, si se debe habilitar la autenticación OIDC. Por defecto es `False`.
`OIDC_ISSUER` | URL del emisor del proveedor OIDC (para proveedores OIDC personalizados)
`OIDC_CLIENT_ID` | ID de cliente OAuth (para proveedores OIDC personalizados)
`OIDC_CLIENT_SECRET` | Secreto de cliente OAuth (para proveedores OIDC personalizados)
`OIDC_NAME` | Nombre de visualización personalizado para el proveedor. Por defecto es "OIDC"
`OIDC_SCOPES` | Alcances de OAuth. Por defecto es "openid email profile"
`OIDC_USERNAME_CLAIM` | La reclamación a usar para el nombre de usuario. Por defecto es "preferred_username"
`OIDC_OPENID_CONFIG_URL` | Opcional: URL al punto de configuración de OpenID Connect (si no se usa el estándar `/.well-known/openid-configuration`)
`OIDC_PKCE` | Booleano, si se debe usar PKCE. Si no se establece, se usa PKCE cuando el documento de descubrimiento del proveedor lista `S256`. Consulta [PKCE](oidc.md#pkce)
`OIDC_DISABLE_LOCAL_AUTH` | Booleano, si se debe deshabilitar la autenticación local de nombre de usuario/contraseña. Por defecto es `False`
`OIDC_AUTO_REDIRECT` | Booleano, si se debe redirigir automáticamente a OIDC cuando solo se configura un proveedor. Por defecto es `False`
`OIDC_ALLOWED_REDIRECT_URIS` | Lista de URIs `https` en las que las aplicaciones nativas pueden recibir el resultado del inicio de sesión (v3.26.0+), establecida como una lista JSON en una variable de entorno. Vacía por defecto. Solo necesaria si la documentación de una aplicación nativa lo solicita. Consulta [Aplicaciones nativas](oidc.md#native-apps)

#### Proveedores OIDC integrados

Para proveedores integrados (Google, Microsoft), usa estos ajustes:

Clave | Descripción
----|-------------
`OIDC_GOOGLE_CLIENT_ID` | ID de cliente para Google OAuth
`OIDC_GOOGLE_CLIENT_SECRET` | Secreto de cliente para Google OAuth
`OIDC_MICROSOFT_CLIENT_ID` | ID de cliente para Microsoft OAuth
`OIDC_MICROSOFT_CLIENT_SECRET` | Secreto de cliente para Microsoft OAuth
`OIDC_GOOGLE_PKCE` | Booleano, ajuste PKCE para Google, consulta [PKCE](oidc.md#pkce)
`OIDC_MICROSOFT_PKCE` | Booleano, ajuste PKCE para Microsoft, consulta [PKCE](oidc.md#pkce)

#### Mapeo de Roles OIDC

Estos ajustes te permiten mapear grupos/roles OIDC de tu proveedor de identidad a roles de usuario de Gramps Web:

Clave | Descripción
----|-------------
`OIDC_ROLE_CLAIM` | El nombre de la reclamación en el token OIDC que contiene los grupos/roles del usuario. Por defecto es "groups"
`OIDC_GROUP_ADMIN` | El nombre del grupo/rol de tu proveedor OIDC que se mapea al rol "Admin" de Gramps
`OIDC_GROUP_OWNER` | El nombre del grupo/rol de tu proveedor OIDC que se mapea al rol "Owner" de Gramps
`OIDC_GROUP_EDITOR` | El nombre del grupo/rol de tu proveedor OIDC que se mapea al rol "Editor" de Gramps
`OIDC_GROUP_CONTRIBUTOR` | El nombre del grupo/rol de tu proveedor OIDC que se mapea al rol "Contributor" de Gramps
`OIDC_GROUP_MEMBER` | El nombre del grupo/rol de tu proveedor OIDC que se mapea al rol "Member" de Gramps
`OIDC_GROUP_GUEST` | El nombre del grupo/rol de tu proveedor OIDC que se mapea al rol "Guest" de Gramps

### Ajustes solo para funciones de IA

Estos ajustes son necesarios si deseas usar chat de IA. Consulta [Configurando chat de IA](chat.md) para más detalles.

!!! note
    Los ajustes `VECTOR_EMBEDDING_MODEL`, `VECTOR_EMBEDDING_BASE_URL` y `VECTOR_EMBEDDING_API_KEY` para búsqueda semántica son ignorados desde Gramps Web API 3.25, que eliminó la búsqueda semántica. El chat de IA solo necesita `LLM_MODEL`.

Clave | Descripción
----|-------------
`LLM_BASE_URL` | URL base para la API de chat compatible con OpenAI. Por defecto es `None`, lo que usa la API de OpenAI.
`LLM_MODEL` | El modelo a usar para la API de chat compatible con OpenAI. Si no se establece (el valor por defecto), el chat está deshabilitado. A partir de v3.6.0, el asistente de IA usa Pydantic AI con capacidades de llamada a herramientas.
`LLM_MAX_OUTPUT_TOKENS` | Número máximo de tokens que el modelo puede generar en una sola respuesta. Sin establecer por defecto, dejando el límite al servidor del modelo. Útil para servidores de modelos sin un límite propio, donde una respuesta podría continuar indefinidamente.
`LLM_MAX_CONTEXT_LENGTH` | Límite de caracteres para el contexto del árbol genealógico proporcionado al LLM. Por defecto es 50000.
`LLM_SYSTEM_PROMPT` | Aviso de sistema personalizado para el asistente de chat LLM (v3.6.0+). Si no se establece, usa el aviso optimizado para genealogía por defecto.
`LLM_VISION` | Booleano, si los usuarios pueden adjuntar imágenes a sus preguntas (v3.26.0+). Solo habilítalo si el modelo acepta imágenes. Por defecto es `False`. Consulta [Imágenes en preguntas](chat.md#images-in-questions)
`LLM_ALLOW_WRITE_PROPOSALS` | Booleano, si el asistente puede proponer cambios al árbol para que los usuarios los revisen y apliquen (v3.26.0+). Por defecto es `False`. Consulta [Permitiendo que el asistente proponga cambios](chat.md#letting-the-assistant-propose-changes)


## Ejemplo de archivo de configuración

Un archivo de configuración mínimo para producción podría verse así:
```python
TREE="Mi Árbol Genealógico"
BASE_URL="https://mitree.ejemplo.com"
SECRET_KEY="..."  # tu clave secreta
USER_DB_URI="sqlite:////path/to/users.sqlite"
EMAIL_HOST="mail.ejemplo.com"
EMAIL_PORT=465
EMAIL_USE_SSL=True  # Usar SSL implícito para el puerto 465
EMAIL_HOST_USER="gramps@ejemplo.com"
EMAIL_HOST_PASSWORD="..." # tu contraseña SMTP
DEFAULT_FROM_EMAIL="gramps@ejemplo.com"
