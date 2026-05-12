# Gestionar Usuarios

La interfaz de gestión de usuarios es accesible a través de **Configuración > Gestionar Usuarios** (el ícono de usuario en la barra superior de la aplicación). Solo está disponible para usuarios con el rol de Propietario o Administrador.

## Roles de usuario

Consulta [Sistema de usuarios](../install_setup/users.md) para una descripción completa de los roles de usuario disponibles y sus permisos.

## Ver y filtrar usuarios

La página de gestionar usuarios muestra una tabla de todas las cuentas de usuario registradas con las siguientes columnas:

- **Nombre de usuario** — el nombre de inicio de sesión
- **Nombre completo** — el nombre para mostrar
- **Correo electrónico** — la dirección de correo electrónico del usuario
- **Rol** — el rol asignado (Invitado, Miembro, Contribuyente, Editor, Propietario o Administrador)
- **Fuente de la cuenta** — ya sea "Contraseña" (cuenta local) o el nombre de un proveedor de identidad externo (por ejemplo, al usar OIDC)

Utiliza el campo de búsqueda y el menú desplegable de roles en la parte superior de la tabla para filtrar la lista. Haz clic en el botón de limpiar filtro para restablecer todos los filtros.

## Editar un usuario

Haz clic en el ícono de editar (lápiz) en cualquier fila para abrir el diálogo de edición. Puedes cambiar el:

- Nombre completo
- Dirección de correo electrónico
- Rol

Esta es la forma principal de **habilitar a un nuevo usuario registrado por sí mismo**: cambia su rol de *deshabilitado* a cualquier rol activo (por ejemplo, Miembro o Editor).

## Agregar un usuario manualmente

Haz clic en el ícono de **agregar usuario** (persona-agregar) sobre la tabla para crear una nueva cuenta de usuario directamente sin requerir auto-registro. Completa el nombre de usuario, nombre completo, dirección de correo electrónico, contraseña y rol en el diálogo y haz clic en **Guardar**.

## Eliminar un usuario

Haz clic en el ícono de eliminar (basura) en cualquier fila y confirma en el diálogo. Esta acción no se puede deshacer.

## Exportar e importar cuentas de usuario

Estos botones son útiles al [migrar a una instancia diferente de Gramps Web](export.md).

- **Exportar detalles del usuario** (ícono de descarga) — descarga un archivo JSON que contiene todas las cuentas de usuario (sin contraseñas, ya que las contraseñas se almacenan en forma encriptada).
- **Importar cuentas de usuario** (ícono de grupo-agregar) — sube un archivo JSON previamente exportado para crear cuentas de usuario en masa. Todos los usuarios importados deberán establecer una nueva contraseña a través del enlace "Olvidé mi contraseña", ya que las contraseñas no se pueden transferir.

## Enlace de registro (solo configuración de múltiples árboles)

En una configuración de múltiples árboles, el enlace de registro para nuevos usuarios se muestra en la parte superior de la página de gestionar usuarios. Puedes copiar este enlace y compartirlo con las personas que deseas invitar a registrarse en tu árbol.

!!! nota
    En una configuración de un solo árbol, hay un enlace genérico de "Registrar" en la página de inicio de sesión; el enlace de registro por árbol solo es necesario en instalaciones de múltiples árboles.

## Permisos de chat de IA

Si el chat de IA ha sido habilitado en el servidor, un menú desplegable en la parte superior de la página te permite controlar qué roles de usuario pueden usar la función de chat:

- Todos (incluidos los invitados)
- Miembro y superior
- Contribuyente y superior
- Editor y superior
- Solo propietarios y administradores
- Nadie (desactivar el chat para todos los usuarios)
