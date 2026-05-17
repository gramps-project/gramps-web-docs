# Configuración del Usuario

La Configuración del Usuario es accesible a través del ícono de usuario en la barra superior de la aplicación, luego **Configuración del Usuario**. La página está organizada en secciones colapsables. Los cambios tienen efecto inmediato a menos que se indique lo contrario.

!!! note
    Los cambios en la Configuración del Usuario solo afectan tu propia cuenta. Las configuraciones que afectan a todos los usuarios del árbol se gestionan en [Configuración de Administración](../administration/settings.md).

## Cuenta

Cubre tu información de perfil, credenciales y seguridad de la cuenta.

### Información del usuario

Muestra tu **nombre de usuario** y el **rol de usuario** actual (por ejemplo, Invitado, Miembro, Editor). Estos son de solo lectura.

### Cambiar correo electrónico

Ingresa una nueva dirección de correo electrónico y haz clic en **Enviar** para actualizar la dirección asociada con tu cuenta. La dirección de correo electrónico se utiliza para restablecimientos de contraseña y (si está configurado) notificaciones.

### Cambiar contraseña

Ingresa tu contraseña actual y una nueva contraseña, luego haz clic en **Enviar**. Si has olvidado tu contraseña actual, utiliza el enlace **Olvidé mi contraseña** en la página de inicio de sesión.

## Apariencia

Controla las preferencias de visualización guardadas en tu dispositivo.

### Idioma

Selecciona el idioma para la interfaz web de Gramps. La configuración de idioma se almacena en el almacenamiento local del navegador y se aplica solo al dispositivo actual.

### Tema

Elige entre:

- **Sistema** – sigue la preferencia de luz/oscuridad del sistema operativo (predeterminado)
- **Claro** – siempre usa el tema claro
- **Oscuro** – siempre usa el tema oscuro

La configuración del tema se almacena en el almacenamiento local del navegador.

### Preferencias del árbol genealógico

#### Vista predeterminada del árbol genealógico

Establece qué tipo de gráfico se abre por defecto cuando navegas a la página de [Árbol Genealógico](tree.md). Las opciones son Árbol de Ancestros, Árbol de Descendientes, Gráfico de Reloj de Arena, Gráfico de Relaciones y Gráfico de Ventilador.

Esta preferencia se almacena en el almacenamiento local del navegador.

## Herramientas de desarrollador

### Token de API

Copia tu token de sesión actual al portapapeles. El token se puede usar para autenticar directamente contra la API REST, por ejemplo, en la interfaz Swagger interactiva servida por tu instancia de Gramps Web en `/api/swagger-ui`.

Haz clic en **Iniciar Swagger** para abrir la interfaz Swagger en una nueva pestaña con tu sesión ya disponible.

!!! note
    El token de sesión tiene una vida útil corta. Cópialo inmediatamente antes de usarlo en Swagger, ya que puede expirar.
