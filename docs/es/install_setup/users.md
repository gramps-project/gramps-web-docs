# Sistema de usuarios

Gramps Web no está destinado a ser expuesto a Internet para acceso público, sino solo por usuarios autenticados. Las cuentas de usuario pueden ser creadas por el propietario del sitio a través de la línea de comandos o la interfaz web, o mediante auto-registro y posterior aprobación por parte del propietario del sitio.

## Roles de usuario

Los siguientes roles de usuario están actualmente definidos.

Rol | ID de rol | Permisos
-----|---------|------------
Invitado | 0 | Ver objetos no privados
Miembro | 1 | Invitado + ver objetos privados
Contribuyente* | 2 | Miembro + agregar objetos
Editor | 3 | Contribuyente + editar y eliminar objetos
Propietario | 4 | Editor + gestionar usuarios
Administrador | 5 | Propietario + editar otros árboles en configuración de múltiples árboles

Si un registro es privado se establece por registro, ver [Registros privados](../user-guide/privacy.md). Nada es privado por defecto, ni siquiera las personas vivas.

\* Tenga en cuenta que el rol de "Contribuyente" actualmente solo está parcialmente soportado; por ejemplo, los objetos familiares no pueden ser añadidos ya que implican una modificación de los objetos de persona subyacentes de los miembros de la familia. Se recomienda utilizar los otros roles siempre que sea posible.

## Configurando quién puede usar el chat de IA

Si ha [configurado el chat de IA](chat.md), verá una opción aquí para elegir qué grupos de usuarios pueden usar la función de chat.

## Gestión de usuarios

Hay dos formas de gestionar usuarios:

- Con permisos de propietario utilizando la interfaz web
- En la línea de comandos en el servidor

La cuenta de propietario requerida para acceder primero a la aplicación web puede ser añadida en el asistente de incorporación que se lanza automáticamente al acceder a Gramps Web con una base de datos de usuarios vacía.

### Gestión de usuarios en la línea de comandos

Al usar [Docker Compose](deployment.md), el comando básico es

```bash
docker compose run grampsweb python3 -m gramps_webapi user COMMAND [ARGS]
```

El `COMMAND` puede ser `add`, `set-password` o `delete`. Use `--help` para `[ARGS]` para mostrar la sintaxis y las posibles opciones de configuración.

`set-password NAME` establece una nueva contraseña para un usuario existente sin necesidad de la antigua, por ejemplo, cuando nadie puede iniciar sesión y el correo electrónico no está configurado para restablecimientos de contraseña (Gramps Web API 3.26+). Se solicita la contraseña dos veces sin mostrarla, por lo que la contraseña no termina en el historial de la shell. Todas las sesiones del usuario se terminan.

### Aprobando usuarios auto-registrados

Cuando un usuario se auto-registra, no se le concede acceso inmediato. Se envía un correo electrónico al propietario del árbol sobre el nuevo registro de usuario y se envía un correo electrónico al usuario solicitando que confirme su dirección de correo electrónico. Confirmar exitosamente su dirección de correo electrónico cambia su rol de `unconfirmed` a `disabled`. Mientras la cuenta de usuario esté en cualquiera de esos dos roles, el usuario no puede iniciar sesión. El propietario del árbol debe revisar la solicitud del usuario y asignarle un rol apropiado antes de que se le permita iniciar sesión.
