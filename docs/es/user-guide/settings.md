# Configuración del usuario

La Configuración del usuario es accesible a través del icono de usuario en la barra superior de la aplicación, luego **Configuración del usuario**. La página está organizada en secciones colapsables. Los cambios tienen efecto inmediato a menos que se indique lo contrario.

!!! note
    Los cambios en la Configuración del usuario solo afectan tu propia cuenta. Las configuraciones que afectan a todos los usuarios del árbol se gestionan en [Configuraciones de administración](../administration/settings.md).

## Cuenta

Cubre tu información de perfil, credenciales y seguridad de la cuenta.

### Información del usuario

Muestra tu **nombre de usuario** y **rol de usuario** actual (por ejemplo, Invitado, Miembro, Editor). Estos son de solo lectura.

### Cambiar correo electrónico

Ingresa una nueva dirección de correo electrónico y haz clic en **Enviar** para actualizar la dirección asociada con tu cuenta. La dirección de correo electrónico se utiliza para restablecimientos de contraseña y (si está configurado) notificaciones.

### Cambiar contraseña

Ingresa tu contraseña actual y una nueva contraseña, luego haz clic en **Enviar**. Si has olvidado tu contraseña actual, utiliza el enlace **Olvidé mi contraseña** en la página de inicio de sesión.

### Métodos de inicio de sesión vinculados

Si tu servidor ofrece inicio de sesión único (ver [autenticación OIDC](../install_setup/oidc.md)), puedes vincular una cuenta de un proveedor, como Google o el inicio de sesión de tu organización, a tu cuenta de Gramps Web. Luego puedes iniciar sesión con ese proveedor y acceder a tu cuenta existente, con tu rol y tus ediciones. Esta sección solo aparece cuando el inicio de sesión único está habilitado y el servidor admite vinculación (API de Gramps Web 3.24 y versiones posteriores).

Para vincular una cuenta, haz clic en **Vincular con** y el nombre del proveedor, inicia sesión en el proveedor, y serás llevado de vuelta a tu configuración. Si no has iniciado sesión recientemente, se te pedirá que inicies sesión nuevamente primero.

Una cuenta de proveedor solo puede estar vinculada a una cuenta de Gramps Web. Si ves "Este inicio de sesión ya está vinculado a otra cuenta", está vinculado en otro lugar, por ejemplo, a una cuenta que se creó cuando iniciaste sesión por primera vez con ese proveedor. Un administrador puede eliminar esa otra cuenta, después de lo cual podrás vincularla a la tuya.

Para desvincular una cuenta, haz clic en **Desvincular**. Si es tu último método de inicio de sesión vinculado, también necesitarás ingresar tu contraseña, para que aún puedas iniciar sesión después. Si tu cuenta fue creada a través de inicio de sesión único y nunca configuraste una contraseña, utiliza **Olvidé mi contraseña** en la página de inicio de sesión para establecer una primero (esto requiere que el servidor envíe correos electrónicos). Si el servidor solo permite iniciar sesión a través de un proveedor, la última cuenta vinculada no se puede desvincular.

## Apariencia

Controla las preferencias de visualización guardadas en tu dispositivo.

### Idioma

Selecciona el idioma para la interfaz de Gramps Web. La configuración de idioma se almacena en el almacenamiento local del navegador y se aplica solo al dispositivo actual.

### Tema

Elige entre:

- **Sistema** – sigue la preferencia de luz/oscuridad del sistema operativo (predeterminado)
- **Claro** – siempre usa el tema claro
- **Oscuro** – siempre usa el tema oscuro

La configuración del tema se almacena en el almacenamiento local del navegador.

### Preferencias del árbol genealógico

#### Vista predeterminada del árbol genealógico

Establece qué tipo de gráfico se abre por defecto cuando navegas a la página de [Árbol genealógico](tree.md). Las opciones son Árbol de Ancestros, Árbol de Descendientes, Gráfico de Reloj de Arena, Gráfico de Relaciones y Gráfico de Ventilador.

Esta preferencia se almacena en el almacenamiento local del navegador.

## Herramientas de desarrollador

### Token de API

Copia tu token de sesión actual al portapapeles. El token se puede usar para autenticar directamente contra la API REST, por ejemplo, en la interfaz Swagger interactiva servida por tu instancia de Gramps Web en `/api/swagger-ui`.

Haz clic en **Iniciar Swagger** para abrir la interfaz Swagger en una nueva pestaña con tu sesión ya disponible.

!!! note
    El token de sesión tiene una vida corta. Cópialo inmediatamente antes de usarlo en Swagger, ya que puede expirar.
