# Autenticación OIDC

Gramps Web admite la autenticación OpenID Connect (OIDC), lo que permite a los usuarios iniciar sesión utilizando proveedores de identidad externos. Esto incluye los proveedores integrados Google y Microsoft, así como proveedores OIDC personalizados como Keycloak, Authentik y Authelia.

!!! warning "GitHub como proveedor OIDC ya no es compatible"
    Si tienes `OIDC_GITHUB_CLIENT_ID` / `OIDC_GITHUB_CLIENT_SECRET` configurados de una versión anterior, elimínalos; ahora son ignorados, y los usuarios que anteriormente iniciaron sesión a través de GitHub ya no pueden iniciar sesión de esa manera. GitHub es un proveedor de OAuth 2.0, no un proveedor de OpenID Connect, y nunca devolvió el reclamo del que Gramps Web depende para la identidad, por lo que nunca fue completamente confiable.

## Descripción general

La autenticación OIDC te permite:

- Usar proveedores de identidad externos para la autenticación de usuarios
- Soportar múltiples proveedores de autenticación simultáneamente
- Mapear grupos/roles OIDC a roles de usuario de Gramps Web
- Implementar inicio de sesión único (SSO) y cierre de sesión único
- Deshabilitar opcionalmente la autenticación local con nombre de usuario/contraseña

## Configuración

Para habilitar la autenticación OIDC, necesitas configurar los ajustes apropiados en tu archivo de configuración de Gramps Web o en variables de entorno. Consulta la página de [Configuración del servidor](configuration.md#settings-for-oidc-authentication) para obtener una lista completa de los ajustes OIDC disponibles.

!!! info
    Al usar variables de entorno, recuerda anteponer cada nombre de ajuste con `GRAMPSWEB_` (por ejemplo, `GRAMPSWEB_OIDC_ENABLED`). Consulta [Archivo de configuración vs. variables de entorno](configuration.md#configuration-file-vs-environment-variables) para más detalles.

### Proveedores integrados

Gramps Web tiene soporte integrado para proveedores de identidad populares. Para usarlos, solo necesitas proporcionar el ID de cliente y el secreto del cliente:

- **Google**: `OIDC_GOOGLE_CLIENT_ID` y `OIDC_GOOGLE_CLIENT_SECRET`
- **Microsoft**: `OIDC_MICROSOFT_CLIENT_ID` y `OIDC_MICROSOFT_CLIENT_SECRET`

Puedes configurar múltiples proveedores simultáneamente. El sistema detectará automáticamente qué proveedores están disponibles según los valores de configuración.

!!! tip "Microsoft: implementaciones de inquilino único"
    El proveedor integrado de Microsoft utiliza el punto final multi-inquilino `/common` y acepta inicios de sesión de cualquier cuenta de Microsoft por diseño. Si solo deseas permitir usuarios de tu propio inquilino, utiliza el [proveedor OIDC personalizado](#custom-oidc-providers) con la URL del emisor específica de tu inquilino, lo que mantiene la validación del emisor activa y restringe los inicios de sesión a ese inquilino.

### Proveedores OIDC personalizados

Para proveedores OIDC personalizados (como Keycloak, Authentik, Authelia o un inquilino de Microsoft Entra de inquilino único), utiliza estos ajustes:

Clave | Descripción
----|-------------
`OIDC_ENABLED` | Booleano, si habilitar la autenticación OIDC. Establecer en `True`.
`OIDC_ISSUER` | URL del emisor de tu proveedor. La búsqueda de descubrimiento se obtiene de `<issuer>/.well-known/openid-configuration`.
`OIDC_CLIENT_ID` | ID de cliente para tu proveedor OIDC
`OIDC_CLIENT_SECRET` | Secreto de cliente para tu proveedor OIDC
`OIDC_NAME` | Nombre de visualización personalizado (opcional, por defecto "OIDC")
`OIDC_SCOPES` | Alcances de OAuth (opcional, por defecto "openid email profile")
`OIDC_USERNAME_CLAIM` | Reclamo utilizado para generar el nombre de usuario (opcional, por defecto "preferred_username")

### Configuraciones de múltiples árboles

En un servidor de múltiples árboles, el árbol al que el usuario está iniciando sesión debe ser conocido antes de que Gramps Web redirija al proveedor de identidad, por lo que el inicio de sesión comienza con:

```
GET /api/oidc/login/?provider=<id>&tree=<tree_id>
```

`tree` es obligatorio en configuraciones de múltiples árboles; omitirlo o pasar el ID de un árbol que no existe falla el inicio de sesión. En un servidor de un solo árbol, `tree` es opcional, pero si se proporciona, debe coincidir con el `TREE` configurado.

Una identidad OIDC está vinculada a exactamente una cuenta de Gramps Web, que a su vez pertenece a exactamente un árbol; iniciar sesión contra un árbol diferente falla en lugar de mover la cuenta. No hay forma de vincular una única identidad en el proveedor a cuentas en varios árboles; los usuarios que necesitan acceso a múltiples árboles necesitan identidades separadas en el proveedor (por ejemplo, nombres de usuario o cuentas distintas).

!!! warning
    Una cuenta de administrador del sitio sin árbol asociado (ver [creando una cuenta de administrador](../administration/owner.md)) no puede iniciar sesión a través de OIDC, ya que el inicio de sesión OIDC siempre requiere un árbol. Tales cuentas deben ser creadas y autenticadas con un nombre de usuario/contraseña local en su lugar.

## URIs de redirección requeridos

Al configurar tu proveedor OIDC, debes registrar la siguiente URI de redirección:

**Para proveedores OIDC que admiten comodines: (por ejemplo, Authentik)**

- `https://your-gramps-backend.com/api/oidc/callback/*`

Donde `*` es un comodín regex. Dependiendo del intérprete regex de tu proveedor, esto también podría ser un `.*` o similar. Asegúrate de que el regex esté habilitado si tu proveedor lo requiere (por ejemplo, Authentik).

**Para proveedores OIDC que no admiten comodines: (por ejemplo, Authelia)**

- `https://your-gramps-backend.com/api/oidc/callback/custom`

El árbol nunca es parte de la URI de redirección, incluso en servidores de múltiples árboles; viaja por separado en la sesión, ya que los proveedores requieren que la URI de redirección coincida exactamente con la registrada.

## Mapeo de roles

Gramps Web puede mapear automáticamente grupos o roles OIDC de tu proveedor de identidad a roles de usuario de Gramps Web. Esto te permite gestionar permisos de usuario de manera centralizada en tu proveedor de identidad. El mapeo de roles funciona de la misma manera para todos los proveedores, ya sean integrados o personalizados.

### Configuración

Utiliza estos ajustes para configurar el mapeo de roles:

Clave | Descripción
----|-------------
`OIDC_ROLE_CLAIM` | El nombre del reclamo en el token OIDC que contiene los grupos/roles del usuario. Por defecto es "groups". Se admiten rutas con puntos, por ejemplo, `realm_access.roles`.
`OIDC_GROUP_ADMIN` | El nombre del grupo/rol de tu proveedor OIDC que se mapea al rol "Admin" de Gramps
`OIDC_GROUP_OWNER` | El nombre del grupo/rol de tu proveedor OIDC que se mapea al rol "Owner" de Gramps
`OIDC_GROUP_EDITOR` | El nombre del grupo/rol de tu proveedor OIDC que se mapea al rol "Editor" de Gramps
`OIDC_GROUP_CONTRIBUTOR` | El nombre del grupo/rol de tu proveedor OIDC que se mapea al rol "Contributor" de Gramps
`OIDC_GROUP_MEMBER` | El nombre del grupo/rol de tu proveedor OIDC que se mapea al rol "Member" de Gramps
`OIDC_GROUP_GUEST` | El nombre del grupo/rol de tu proveedor OIDC que se mapea al rol "Guest" de Gramps

### Comportamiento del mapeo de roles

Si no se configura ningún ajuste `OIDC_GROUP_*`, el mapeo de roles está desactivado y los roles se gestionan manualmente en Gramps Web; las nuevas cuentas OIDC se crean deshabilitadas y necesitan ser aprobadas por un propietario o administrador existente (ver [Primer inicio de sesión y arranque](#first-login-and-bootstrapping) a continuación).

Una vez que el mapeo de roles está configurado, en cada inicio de sesión:

- Si el reclamo de rol está presente y el usuario pertenece a un grupo mapeado, recibe el rol correspondiente.
- Si el reclamo de rol está presente pero el usuario no pertenece a ningún grupo mapeado, su rol se establece como deshabilitado. Este es un valor predeterminado de fallo cerrado, no un error; Gramps Web no puede inferir un rol para un grupo que no reconoce.
- Si el reclamo de rol está ausente del token por completo, el rol existente permanece sin cambios; una nueva cuenta aún se predetermina como deshabilitada.

!!! warning "Google no envía un reclamo de grupos"
    Los tokens de Google nunca incluyen un reclamo de `groups`, por lo que con el mapeo de roles habilitado, los inicios de sesión de Google caen bajo "reclamo ausente" arriba: los usuarios existentes mantienen su rol, pero los nuevos usuarios de Google se crean deshabilitados y necesitan aprobación manual. Ten esto en cuenta antes de habilitar el mapeo de roles solo para otro proveedor; no desactiva, por sí mismo, a los usuarios existentes de Google.

Microsoft Entra devuelve roles de aplicación y membresías de grupo solo en el token de ID, no desde el punto final de información del usuario. Gramps Web fusiona los reclamos del token de ID en la respuesta de información del usuario para que `OIDC_ROLE_CLAIM` funcione de la misma manera que para otros proveedores; donde ambos contienen un reclamo, el valor de información del usuario tiene prioridad.

## Primer inicio de sesión y arranque

Las nuevas cuentas creadas a través de OIDC comienzan deshabilitadas a menos que el mapeo de roles les asigne un rol (ver arriba). En una instancia completamente nueva, nadie puede aprobar una cuenta deshabilitada, y si `OIDC_DISABLE_LOCAL_AUTH` también está habilitado, no hay inicio de sesión por contraseña al que recurrir.

!!! warning "Configura un grupo de propietario/admin antes del primer inicio de sesión"
    Antes de que alguien inicie sesión a través de OIDC por primera vez, establece `OIDC_GROUP_OWNER` (o `OIDC_GROUP_ADMIN`) y asegúrate de que el primer usuario pertenezca a ese grupo en el proveedor. De lo contrario, la instancia no puede ser iniciada a través de OIDC en absoluto.

## Cuentas y nombres de usuario

Las cuentas creadas a través de OIDC obtienen un nombre de usuario generado, asignado una vez en la creación de la cuenta y nunca cambiado en inicios de sesión posteriores:

- Proveedores integrados: `<provider>_<claim value>`, por ejemplo, `microsoft_alice@contoso.com`
- Proveedor personalizado: el valor de reclamo puro, por ejemplo, `alice`

Se añade un sufijo numérico en caso de colisión. No hay forma de renombrar el nombre de usuario de una cuenta creada por OIDC después; el nombre completo y la dirección de correo electrónico, en cambio, se actualizan en cada inicio de sesión.

Un inicio de sesión OIDC nunca se adjunta a una cuenta local existente que comparta su dirección de correo electrónico; esto es deliberado, ya que vincular cuentas por correo electrónico es un vector de toma de control de cuentas. Un usuario que ya tiene una cuenta local obtiene una segunda cuenta separada la primera vez que inicia sesión a través de OIDC.

Las direcciones de correo electrónico del proveedor solo se almacenan si el proveedor las marca como verificadas (o omite completamente el reclamo `email_verified`) y si la dirección no está ya utilizada por otra cuenta; de lo contrario, el inicio de sesión procede sin almacenar una dirección de correo electrónico.

## Cierre de sesión OIDC

Gramps Web admite el cierre de sesión único (SSO) para proveedores OIDC. `GET /api/oidc/logout/` busca el `end_session_endpoint` del proveedor y lo devuelve como `logout_url` en la respuesta; es el frontend de Gramps Web el que navega el navegador allí para terminar realmente la sesión en el proveedor de identidad. `logout_url` es `null` cuando el proveedor no tiene `end_session_endpoint`.

!!! warning "Los tokens no se revocan al cerrar sesión"
    Cerrar sesión solo termina la sesión del navegador; actualmente no hay forma de revocar un token de Gramps Web que ya ha sido emitido. Los tokens permanecen válidos hasta que expiran (`JWT_ACCESS_TOKEN_EXPIRES`, por defecto 15 minutos para tokens de acceso), independientemente de si el usuario ha cerrado sesión en Gramps Web o en el proveedor de identidad.

## Ejemplos de configuraciones

### Proveedor OIDC personalizado (Keycloak)

```python
TREE="Mi Árbol Familiar"
BASE_URL="https://mytree.example.com"
SECRET_KEY="..."  # tu clave secreta
USER_DB_URI="sqlite:////path/to/users.sqlite"

# Configuración OIDC personalizada
OIDC_ENABLED=True
OIDC_ISSUER="https://auth.example.com/realms/myrealm"
OIDC_CLIENT_ID="gramps-web"
OIDC_CLIENT_SECRET="tu-secreto-de-cliente"
OIDC_NAME="SSO Familiar"
OIDC_SCOPES="openid email profile"
OIDC_AUTO_REDIRECT=True  # Opcional: redirigir automáticamente al inicio de sesión SSO
OIDC_DISABLE_LOCAL_AUTH=True  # Opcional: deshabilitar el inicio de sesión con nombre de usuario/contraseña

# Opcional: Mapeo de roles de grupos OIDC a roles de Gramps
OIDC_ROLE_CLAIM="groups"  # o "roles" dependiendo de tu proveedor
OIDC_GROUP_ADMIN="gramps-admins"
OIDC_GROUP_EDITOR="gramps-editors"
OIDC_GROUP_MEMBER="gramps-members"

EMAIL_HOST="mail.example.com"
EMAIL_PORT=465
EMAIL_USE_SSL=True  # Usar SSL implícito para el puerto 465
EMAIL_HOST_USER="gramps@example.com"
EMAIL_HOST_PASSWORD="..." # tu contraseña SMTP
DEFAULT_FROM_EMAIL="gramps@example.com"
```

### Proveedor integrado (Google)

```python
TREE="Mi Árbol Familiar"
BASE_URL="https://mytree.example.com"
SECRET_KEY="..."  # tu clave secreta
USER_DB_URI="sqlite:////path/to/users.sqlite"

# Google OAuth
OIDC_GOOGLE_CLIENT_ID="tu-id-de-cliente-google"
OIDC_GOOGLE_CLIENT_SECRET="tu-secreto-de-cliente-google"
```

### Múltiples proveedores

Puedes habilitar múltiples proveedores OIDC simultáneamente:

```python
TREE="Mi Árbol Familiar"
BASE_URL="https://mytree.example.com"
SECRET_KEY="..."  # tu clave secreta
USER_DB_URI="sqlite:////path/to/users.sqlite"

# Proveedor personalizado
OIDC_ENABLED=True
OIDC_ISSUER="https://auth.example.com/realms/myrealm"
OIDC_CLIENT_ID="gramps-web"
OIDC_CLIENT_SECRET="tu-secreto-de-cliente"
OIDC_NAME="SSO de la Empresa"

# Google OAuth
OIDC_GOOGLE_CLIENT_ID="tu-id-de-cliente-google"
OIDC_GOOGLE_CLIENT_SECRET="tu-secreto-de-cliente-google"

# Microsoft OAuth
OIDC_MICROSOFT_CLIENT_ID="tu-id-de-cliente-microsoft"
OIDC_MICROSOFT_CLIENT_SECRET="tu-secreto-de-cliente-microsoft"
```

### Authelia

Una guía de configuración OIDC hecha por la comunidad para Gramps Web está disponible en el [sitio web oficial de documentación de Authelia](https://www.authelia.com/integration/openid-connect/clients/gramps/).

### Keycloak

La mayor parte de la configuración para Keycloak puede dejarse en sus valores predeterminados (*Cliente → Crear cliente → Autenticación de cliente ACTIVADA*). Hay algunas excepciones:

1. **Alcance OpenID** – El alcance `openid` no está incluido por defecto en todas las versiones de Keycloak. Para evitar problemas, agrégalo manualmente: *Cliente → [Cliente Gramps] → Alcances de cliente → Agregar alcance → Nombre: `openid` → Establecer como predeterminado.*
2. **Roles** – Los roles pueden asignarse ya sea a nivel de cliente o globalmente por reino.

    * Si estás usando roles de cliente, establece la opción de configuración `OIDC_ROLE_CLAIM` en: `resource_access.[nombre-del-cliente-gramps].roles`
    * Para hacer que los roles sean visibles para Gramps, navega a *Alcances de cliente* (la sección de nivel superior, no bajo el cliente específico), luego: *Roles → Mapeadores → roles de cliente → Agregar a información del usuario → ACTIVADO.*
