# Gestionar Usuarios

La interfaz de gestión de usuarios es accesible a través de **Configuración > Gestionar Usuarios** (el ícono de usuario en la barra superior de la aplicación). Solo está disponible para usuarios con el rol de Propietario o Administrador.

## Roles de usuario

Consulta [Sistema de usuarios](../install_setup/users.md) para una descripción completa de los roles de usuario disponibles y sus permisos.

## Ver y filtrar usuarios

La página de gestionar usuarios muestra una tabla de todas las cuentas de usuario registradas con las siguientes columnas:

- **Nombre de usuario** – el nombre de inicio de sesión
- **Nombre completo** – el nombre para mostrar
- **Correo electrónico** – la dirección de correo electrónico del usuario
- **Rol** – el rol asignado (Invitado, Miembro, Colaborador, Editor, Propietario o Administrador)
- **Fuente de la cuenta** – ya sea "Contraseña" (cuenta local) o el nombre de un proveedor de identidad externo (por ejemplo, al usar OIDC)

Utiliza el campo de búsqueda y el menú desplegable de roles en la parte superior de la tabla para filtrar la lista. Haz clic en el botón de limpiar filtros para restablecer todos los filtros.

## Editar un usuario

Haz clic en el ícono de editar (lápiz) en cualquier fila para abrir el diálogo de edición. Puedes cambiar:

- Nombre completo
- Dirección de correo electrónico
- Rol

Esta es la forma principal de **habilitar a un nuevo usuario auto-registrado**: cambia su rol de *deshabilitado* a cualquier rol activo (por ejemplo, Miembro o Editor).

Las direcciones de correo electrónico no tienen que ser únicas (desde la API web de Gramps 3.22), por lo que varias cuentas pueden compartir la misma dirección.

Deshabilitar a un usuario o cambiar su contraseña finaliza todas sus sesiones en un plazo de 15 minutos.

!!! nota
    Los propietarios no pueden editar, cambiar la contraseña de, o eliminar usuarios con un rol superior, como el administrador del sitio. Los usuarios con el mismo rol, como dos propietarios de un árbol, pueden gestionarse entre sí.

## Agregar un usuario manualmente

Haz clic en el ícono de **agregar usuario** (persona-agregar) encima de la tabla para crear una nueva cuenta de usuario directamente sin requerir auto-registro. Completa el nombre de usuario, nombre completo, dirección de correo electrónico, contraseña y rol en el diálogo y haz clic en **Guardar**.

## Eliminar un usuario

Haz clic en el ícono de eliminar (papelera) en cualquier fila y confirma en el diálogo. Esta acción no se puede deshacer.

!!! nota
    Para evitar que un árbol quede sin nadie que pueda administrarlo, no puedes bajar tu propio rol por debajo de Propietario o eliminar tu propia cuenta si eres el único Propietario o Administrador del árbol. Promociona a otro usuario a Propietario primero. Un administrador aún puede cambiar o eliminar al último propietario del árbol de otro usuario, ya que puede nombrar a uno nuevo.

## Exportar e importar cuentas de usuario

Estos botones son útiles al [migrar a una instancia diferente de Gramps Web](export.md).

- **Exportar detalles de usuario** (ícono de descarga) – descarga un archivo JSON que contiene todas las cuentas de usuario (sin contraseñas, ya que las contraseñas se almacenan en forma encriptada).
- **Importar cuentas de usuario** (ícono de grupo-agregar) – sube un archivo JSON previamente exportado para crear cuentas de usuario en bloque. Todos los usuarios importados necesitarán establecer una nueva contraseña a través del enlace "Olvidé mi contraseña", ya que las contraseñas no se pueden transferir.

## Enlace de registro (solo configuración de múltiples árboles)

En una configuración de múltiples árboles, el enlace de registro para nuevos usuarios se muestra en la parte superior de la página de gestionar usuarios. Puedes copiar este enlace y compartirlo con las personas que deseas invitar a registrarse en tu árbol.

!!! nota
    En una configuración de un solo árbol, hay un enlace genérico de "Registrar" en la página de inicio de sesión; el enlace de registro por árbol solo es necesario en instalaciones de múltiples árboles.

## Permisos de chat de IA

Si el chat de IA ha sido habilitado en el servidor, un menú desplegable en la parte superior de la página te permite controlar qué roles de usuario pueden utilizar la función de chat:

- Todos (incluidos los invitados)
- Miembro y superior
- Colaborador y superior
- Editor y superior
- Solo propietarios y administradores
- Nadie (deshabilitar chat para todos los usuarios)
