## Realiza una copia de seguridad de tu árbol genealógico

Los propietarios del árbol pueden crear, descargar y restaurar copias de seguridad completas del árbol, incluidos sus ajustes y usuarios, en la sección de [Copias de seguridad](settings.md#backups) de la configuración de Administración.

Alternativamente, para crear una copia de seguridad solo de los datos del árbol genealógico, abre la página de Exportar en Gramps Web y selecciona el formato XML de Gramps.

Al hacer clic en "exportar", se generará el archivo y comenzará la descarga una vez que esté listo.

Ten en cuenta que si tu usuario de Gramps Web no tiene permiso para ver registros privados, la exportación no será una copia de seguridad completa, ya que no contendrá ningún registro privado.

Este archivo XML de Gramps se puede utilizar más tarde para restaurar el árbol a este estado exacto a través de [Restaurar desde la copia de seguridad](settings.md#restore-from-backup).

## Comparte tu árbol genealógico con usuarios de otros programas de genealogía

Cuando compartir datos genealógicos como Gramps XML no es una opción, también puedes exportar un archivo GEDCOM. Ten en cuenta que esto no es adecuado como una copia de seguridad de tu árbol de Gramps Web.

## Realiza una copia de seguridad de tus archivos multimedia

Para realizar una copia de seguridad de tus archivos multimedia, puedes crear y descargar un archivo ZIP de todos los archivos multimedia en la página de Exportar.

Ten en cuenta que, especialmente para árboles grandes, esto puede ser una operación costosa para el servidor y solo debe hacerse si es absolutamente necesario. Por esta razón, el número de archivos multimedia que se pueden crear está limitado (por defecto a uno por hora). Si alcanzas el límite, el mensaje de error lo indicará.

Una mejor opción para realizar copias de seguridad de tus archivos multimedia de manera regular es utilizar el [complemento de sincronización de Gramps Web](sync.md) (que en sí mismo no es una solución de copia de seguridad) y crear copias de seguridad incrementales en tu computadora local.

En ambos casos, si tu usuario de Gramps Web no tiene permiso para ver registros privados, la exportación no contendrá archivos de objetos multimedia privados.

## Moverse a una instancia diferente de Gramps Web

Gramps Web no te obliga a quedarte con un proveedor específico y siempre puedes moverte a una instancia diferente de Gramps Web sin perder ningún dato y sin tener acceso directo a ninguno de los servidores.

Para lograr una migración completa, sigue estos pasos (suponiendo que tienes permisos de propietario del árbol):

1. Ve a la página de Exportar y exporta tu árbol como un archivo XML de Gramps (`.gramps`). Si utilizas el [complemento de sincronización](sync.md), también puedes generar la exportación en Gramps de escritorio.
2. En la página de Exportar, genera y descarga un archivo multimedia. Si utilizas el [complemento de sincronización](sync.md), también puedes simplemente comprimir tu carpeta multimedia local de Gramps en un ZIP.
3. Ve a Configuración > Administración > Administrar usuarios y haz clic en el botón "Exportar detalles del usuario". Se descargará un archivo JSON.
4. En la nueva instancia de Gramps Web, abre la página de Importar. Importa el archivo `.gramps` exportado en el paso 1.
5. En la página de Importar de la nueva instancia de Gramps Web, sube el archivo multimedia (ZIP).
6. Ve a Configuración > Administración > Administrar usuarios de la nueva instancia de Gramps Web. Haz clic en el botón "Importar cuentas de usuario" y sube el archivo JSON descargado en el paso 3.

Ten en cuenta que, aunque tus cuentas de usuario serán migradas, todos tus usuarios necesitarán establecer nuevas contraseñas utilizando el enlace "olvidé mi contraseña", ya que las contraseñas se almacenan en forma encriptada y no se pueden exportar.
