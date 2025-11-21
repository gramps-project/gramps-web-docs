# Crear una cuenta para el propietario del árbol

Antes de que puedas comenzar a usar Gramps Web, necesitas crear una cuenta para el propietario del árbol. Si no existe una cuenta de usuario para un árbol dado, se mostrará un formulario para crear una cuenta. El formulario depende de la configuración del servidor, que puede ser para un solo árbol o para múltiples árboles.

## Configuración de un solo árbol: crear cuenta de administrador

En un servidor con configuración de un solo árbol, cuando aún no existe ninguna cuenta de usuario, al abrir Gramps Web se muestra un formulario para crear una cuenta de administrador. El usuario administrador será tanto el propietario del árbol (único) como el administrador de la instalación. El formulario también permite configurar la configuración de correo electrónico necesaria para las notificaciones por correo electrónico (por ejemplo, restablecer la contraseña de un usuario). Si la configuración de correo electrónico ya se ha agregado a través de un archivo de configuración o variables de entorno en el servidor, esta parte del formulario se puede dejar vacía.

## Configuración de múltiples árboles: crear cuenta de administrador

En una configuración de múltiples árboles, se mostrará el mismo formulario para crear una cuenta de administrador si no existen usuarios *en ningún árbol*, es decir, cuando el servidor acaba de ser creado.

## Configuración de múltiples árboles: crear cuenta de propietario del árbol

En una configuración de múltiples árboles, cada usuario está vinculado a un solo árbol. Incluso si ya existen usuarios en otros árboles, se puede crear un propietario de árbol en la interfaz web si aún no existe un propietario *para este árbol*.

Sin embargo, el formulario de creación de propietario no se mostrará automáticamente en la página de inicio de Gramps Web, que es la misma para todos los árboles. En su lugar, se puede acceder a él en `https://my-gramps-instance/firstrun/my-tree-id`, donde `https://my-gramps-instance` es la dirección base de tu instalación de Gramps Web, y `my-tree-id` es el ID de tu árbol.

Un posible flujo de trabajo para un administrador del sitio para crear un nuevo árbol es:

- Crear un árbol a través de la API REST, obteniendo el ID del árbol nuevo
- Compartir el enlace al formulario de creación de propietario con el ID de árbol apropiado con el posible propietario del árbol

El formulario de creación de propietario del árbol es análogo al formulario de creación de administrador descrito anteriormente, excepto que no permite cambiar la configuración de correo electrónico (lo cual solo está permitido para administradores).
