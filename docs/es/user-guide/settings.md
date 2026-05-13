# Configuración del usuario

La Configuración del usuario es accesible a través del ícono de usuario en la barra superior de la aplicación, luego **Configuración del usuario**. Los cambios tienen efecto inmediato a menos que se indique lo contrario.

## Información del usuario

Muestra tu **nombre de usuario** y el **rol de usuario** actual (por ejemplo, Invitado, Miembro, Editor). Estos son de solo lectura.

## Idioma

Selecciona el idioma para la interfaz web de Gramps. La configuración del idioma se almacena en el almacenamiento local del navegador y se aplica solo al dispositivo actual.

## Tema

Elige entre:

- **Sistema** – sigue la preferencia de luz/oscuridad del sistema operativo (predeterminado)
- **Claro** – siempre usa el tema claro
- **Oscuro** – siempre usa el tema oscuro

La configuración del tema se almacena en el almacenamiento local del navegador.

## Cambiar correo electrónico

Ingresa una nueva dirección de correo electrónico y haz clic en **Enviar** para actualizar la dirección asociada con tu cuenta. La dirección de correo electrónico se utiliza para restablecimientos de contraseña y (si está configurado) notificaciones.

## Cambiar contraseña

Ingresa tu contraseña actual y una nueva contraseña, luego haz clic en **Enviar**. Si has olvidado tu contraseña actual, utiliza el enlace **Olvidé mi contraseña** en la página de inicio de sesión.

## Preferencias del árbol genealógico

### Vista predeterminada del árbol genealógico

Establece qué tipo de gráfico se abre por defecto cuando navegas a la página del [Árbol Genealógico](tree.md). Las opciones son Árbol de Ancestros, Árbol de Descendientes, Gráfico de Reloj de Arena, Gráfico de Relaciones y Gráfico en Fan.

Esta preferencia se almacena en el almacenamiento local del navegador.

## Herramientas de desarrollador

### Token de API

Copia tu token de sesión actual al portapapeles. El token se puede usar para autenticar directamente contra la API REST, por ejemplo, en la interfaz Swagger interactiva servida por tu instancia de Gramps Web en `/api/swagger-ui`.

Haz clic en **Iniciar Swagger** para abrir la interfaz Swagger en una nueva pestaña con tu sesión ya disponible.

!!! nota
    El token de sesión tiene una vida corta. Cópialo inmediatamente antes de usarlo en Swagger, ya que puede expirar.
