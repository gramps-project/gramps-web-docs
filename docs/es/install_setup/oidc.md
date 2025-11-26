# Autenticación OIDC

Gramps Web admite la autenticación OpenID Connect (OIDC), lo que permite a los usuarios iniciar sesión utilizando proveedores de identidad externos. Esto incluye tanto proveedores populares como Google, Microsoft y GitHub, así como proveedores OIDC personalizados como Keycloak, Authentik y otros.

## Descripción general

La autenticación OIDC te permite:

- Utilizar proveedores de identidad externos para la autenticación de usuarios
- Soportar múltiples proveedores de autenticación simultáneamente
- Mapear grupos/roles OIDC a roles de usuario de Gramps Web
- Implementar Single Sign-On (SSO) y Single Sign-Out
- Deshabilitar opcionalmente la autenticación local con nombre de usuario/contraseña

## Configuración

Para habilitar la autenticación OIDC, necesitas configurar los ajustes apropiados en tu archivo de configuración de Gramps Web o en las variables de entorno. Consulta la página de [Configuración del servidor](configuration.md#settings-for-oidc-authentication) para obtener una lista completa de los ajustes OIDC disponibles.

!!! info
    Al usar variables de entorno, recuerda anteponer cada nombre de ajuste con `GRAMPSWEB_` (por ejemplo, `GRAMPSWEB_OIDC_ENABLED`). Consulta [Archivo de configuración vs. variables de entorno](configuration.md#configuration-file-vs-environment-variables) para más detalles.

### Proveedores integrados

Gramps Web tiene soporte integrado para proveedores de identidad populares. Para utilizarlos, solo necesitas proporcionar el ID de cliente y el secreto de cliente:

- **Google**: `OIDC_GOOGLE_CLIENT_ID` y `OIDC_GOOGLE_CLIENT_SECRET`
- **Microsoft**: `OIDC_MICROSOFT_CLIENT_ID` y `OIDC_MICROSOFT_CLIENT_SECRET`
- **GitHub**: `OIDC_GITHUB_CLIENT_ID` y `OIDC_GITHUB_CLIENT_SECRET`

Puedes configurar múltiples proveedores simultáneamente. El sistema detectará automáticamente qué proveedores están disponibles según los valores de configuración.

### Proveedores OIDC personalizados

Para proveedores OIDC personalizados (como Keycloak, Authentik o cualquier proveedor estándar compatible con OIDC), utiliza estos ajustes:

Clave | Descripción
----|-------------
`OIDC_ENABLED` | Booleano, si habilitar la autenticación OIDC. Establecer en `True`.
`OIDC_ISSUER` | URL del emisor de tu proveedor
`OIDC_CLIENT_ID` | ID de cliente para tu proveedor OIDC
`OIDC_CLIENT_SECRET` | Secreto de cliente para tu proveedor OIDC
`OIDC_NAME` | Nombre de visualización personalizado (opcional, por defecto "OIDC")
`OIDC_SCOPES` | Alcances de OAuth (opcional, por defecto "openid email profile")

## URIs de redirección requeridas

Al configurar tu proveedor OIDC, debes registrar la siguiente URI de redirección:

**Para proveedores OIDC que soportan comodines: (por ejemplo, Authentik)**

- `https://your-gramps-backend.com/api/oidc/callback/*`

Donde `*` es un comodín regex. Dependiendo del intérprete regex de tu proveedor, esto también podría ser un `.*` o similar. Asegúrate de que el regex esté habilitado si tu proveedor lo requiere (por ejemplo, Authentik).

**Para proveedores OIDC que no soportan comodines: (por ejemplo, Authelia)**

- `https://your-gramps-backend.com/api/oidc/callback/?provider=custom`

## Mapeo de roles

Gramps Web puede mapear automáticamente grupos o roles OIDC de tu proveedor de identidad a roles de usuario de Gramps Web. Esto te permite gestionar los permisos de los usuarios de manera centralizada en tu proveedor de identidad.

### Configuración

Utiliza estos ajustes para configurar el mapeo de roles:

Clave | Descripción
----|-------------
`OIDC_ROLE_CLAIM` | El nombre del reclamo en el token OIDC que contiene los grupos/roles del usuario. Por defecto "groups"
`OIDC_GROUP_ADMIN` | El nombre del grupo/rol de tu proveedor OIDC que se mapea al rol "Admin" de Gramps
`OIDC_GROUP_OWNER` | El nombre del grupo/rol de tu proveedor OIDC que se mapea al rol "Owner" de Gramps
`OIDC_GROUP_EDITOR` | El nombre del grupo/rol de tu proveedor OIDC que se mapea al rol "Editor" de Gramps
`OIDC_GROUP_CONTRIBUTOR` | El nombre del grupo/rol de tu proveedor OIDC que se mapea al rol "Contributor" de Gramps
`OIDC_GROUP_MEMBER` | El nombre del grupo/rol de tu proveedor OIDC que se mapea al rol "Member" de Gramps
`OIDC_GROUP_GUEST` | El nombre del grupo/rol de tu proveedor OIDC que se mapea al rol "Guest" de Gramps

### Comportamiento del mapeo de roles

- Si no se configura el mapeo de roles (sin variables `OIDC_GROUP_*` establecidas), se preservan los roles de usuario existentes
- A los usuarios se les asigna el rol más alto al que tienen derecho según su pertenencia a grupos
- El mapeo de roles es sensible a mayúsculas y minúsculas por defecto (depende de tu proveedor OIDC)

## Cierre de sesión OIDC

Gramps Web admite el cierre de sesión Single Sign-Out (SSO) para proveedores OIDC. Cuando un usuario cierra sesión en Gramps Web después de autenticarse a través de OIDC, será redirigido automáticamente a la página de cierre de sesión del proveedor de identidad si el proveedor admite el `end_session_endpoint`.

### Cierre de sesión por canal de retroceso

Gramps Web implementa la especificación de Cierre de sesión por canal de retroceso de OpenID Connect. Esto permite a los proveedores de identidad notificar a Gramps Web cuando un usuario cierra sesión desde otra aplicación o desde el propio proveedor de identidad.

#### Configuración

Para configurar el cierre de sesión por canal de retroceso con tu proveedor de identidad:

1. **Registra el endpoint de cierre de sesión por canal de retroceso** en la configuración del cliente de tu proveedor de identidad:
   ```
   https://your-gramps-backend.com/api/oidc/backchannel-logout/
   ```

2. **Configura tu proveedor** para enviar notificaciones de cierre de sesión. Los pasos exactos dependen de tu proveedor:

   **Keycloak:**

   - En la configuración de tu cliente, navega a "Configuración"
   - Establece "URL de cierre de sesión por canal de retroceso" en `https://your-gramps-backend.com/api/oidc/backchannel-logout/`
   - Habilita "Se requiere sesión de cierre de sesión por canal de retroceso" si deseas un cierre de sesión basado en la sesión

   **Authentik:**

   - En la configuración de tu proveedor, agrega la URL de cierre de sesión por canal de retroceso
   - Asegúrate de que el proveedor esté configurado para enviar tokens de cierre de sesión

!!! warning "Expiración del token"
    Debido a la naturaleza sin estado de los tokens JWT, el cierre de sesión por canal de retroceso actualmente registra el evento de cierre de sesión pero no puede revocar inmediatamente los tokens JWT ya emitidos. Los tokens seguirán siendo válidos hasta que expiren (por defecto: 15 minutos para los tokens de acceso).

    Para una mayor seguridad, considera:

    - Reducir el tiempo de expiración del token JWT (`JWT_ACCESS_TOKEN_EXPIRES`)
    - Educar a los usuarios para que cierren sesión manualmente en Gramps Web al cerrar sesión en tu proveedor de identidad

!!! tip "Cómo funciona"
    Cuando un usuario cierra sesión en tu proveedor de identidad o en otra aplicación:

    1. El proveedor envía un `logout_token` JWT al endpoint de cierre de sesión por canal de retroceso de Gramps Web
    2. Gramps Web valida el token y registra el evento de cierre de sesión
    3. El JTI del token de cierre de sesión se agrega a una lista de bloqueo para prevenir ataques de repetición
    4. Cualquier nueva solicitud API con el JWT del usuario será denegada una vez que los tokens expiren

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
OIDC_AUTO_REDIRECT=True  # Opcional: redirigir automáticamente a la página de inicio de sesión SSO
OIDC_DISABLE_LOCAL_AUTH=True  # Opcional: deshabilitar el inicio de sesión con nombre de usuario/contraseña

# Opcional: Mapeo de roles de grupos OIDC a roles de Gramps
OIDC_ROLE_CLAIM="groups"  # o "roles" dependiendo de tu proveedor
OIDC_GROUP_ADMIN="gramps-admins"
OIDC_GROUP_EDITOR="gramps-editors"
OIDC_GROUP_MEMBER="gramps-members"

EMAIL_HOST="mail.example.com"
EMAIL_PORT=465
EMAIL_USE_TLS=True
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

# GitHub OAuth
OIDC_GITHUB_CLIENT_ID="tu-id-de-cliente-github"
OIDC_GITHUB_CLIENT_SECRET="tu-secreto-de-cliente-github"
```

### Authelia

Una guía de configuración OIDC hecha por la comunidad para Gramps Web está disponible en el [sitio web oficial de documentación de Authelia](https://www.authelia.com/integration/openid-connect/clients/gramps/).

### Keycloak

La mayor parte de la configuración para Keycloak puede dejarse en sus valores predeterminados (*Cliente → Crear cliente → Autenticación del cliente ACTIVADA*). Hay algunas excepciones:

1. **Alcance OpenID** – El alcance `openid` no está incluido por defecto en todas las versiones de Keycloak. Para evitar problemas, agrégalo manualmente: *Cliente → [Cliente Gramps] → Alcances de cliente → Agregar alcance → Nombre: `openid` → Establecer como predeterminado.*
2. **Roles** – Los roles pueden asignarse a nivel de cliente o globalmente por reino.

    * Si estás utilizando roles de cliente, establece la opción de configuración `OIDC_ROLE_CLAIM` en: `resource_access.[nombre-del-cliente-gramps].roles`
    * Para hacer que los roles sean visibles para Gramps, navega a *Alcances de cliente* (la sección de nivel superior, no bajo el cliente específico), luego: *Roles → Mapeadores → roles de cliente → Agregar a userinfo → ACTIVADO.*
