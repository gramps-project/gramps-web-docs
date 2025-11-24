## Realiza una copia de seguridad de tu árbol genealógico

Para crear una copia de seguridad de tu árbol genealógico, abre la página de Exportación en Gramps Web y selecciona el formato XML de Gramps.

Hacer clic en "exportar" generará el archivo y comenzará la descarga una vez que esté listo.

Ten en cuenta que si tu usuario de Gramps Web no tiene permiso para ver registros privados, la exportación no será una copia de seguridad completa, ya que no contendrá ningún registro privado.

## Comparte tu árbol genealógico con usuarios de otros programas de genealogía

Cuando compartir datos genealógicos como Gramps XML no es una opción, también puedes exportar un archivo GEDCOM. Ten en cuenta que esto no es adecuado como una copia de seguridad de tu árbol de Gramps Web.

## Realiza una copia de seguridad de tus archivos multimedia

Para realizar una copia de seguridad de tus archivos multimedia, puedes crear y descargar un archivo ZIP de todos los archivos multimedia en la página de Exportación.

Ten en cuenta que, especialmente para árboles grandes, esto puede ser una operación costosa para el servidor y solo debe hacerse si es absolutamente necesario.

Una mejor opción para realizar copias de seguridad de tus archivos multimedia de manera regular es usar el [complemento Gramps Web Sync](sync.md) (que en sí mismo no es una solución de copia de seguridad) y crear copias de seguridad incrementales en tu computadora local.

En ambos casos, si tu usuario de Gramps Web no tiene permiso para ver registros privados, la exportación no contendrá archivos de objetos multimedia privados.

## Moverse a una instancia diferente de Gramps Web

Gramps Web no te ata a un proveedor específico y siempre puedes moverte a una instancia diferente de Gramps Web sin perder ningún dato y sin tener acceso directo a ninguno de los servidores.

Para lograr una migración completa, sigue estos pasos (suponiendo que tienes permisos de propietario del árbol):

1. Ve a la página de Exportación y exporta tu árbol como un archivo XML de Gramps (`.gramps`). Si usas el [complemento Sync](sync.md), también puedes generar la exportación en Gramps de escritorio.
2. En la página de Exportación, genera y descarga un archivo de medios. Si usas el [complemento Sync](sync.md), también puedes simplemente comprimir tu carpeta de medios de Gramps local.
3. Ve a Configuración > Administración > Gestionar usuarios y haz clic en el botón "Exportar detalles del usuario". Se descargará un archivo JSON.
4. En la nueva instancia de Gramps Web, abre la página de Importación. Importa el archivo `.gramps` exportado en el paso 1.
5. En la página de Importación de la nueva instancia de Gramps Web, sube el archivo de medios (ZIP).
6. Ve a Configuración > Administración > Gestionar usuarios de la nueva instancia de Gramps Web. Haz clic en el botón "Importar cuentas de usuario" y sube el archivo JSON descargado en el paso 3.

Ten en cuenta que, aunque tus cuentas de usuario serán migradas, todos tus usuarios necesitarán establecer nuevas contraseñas utilizando el enlace "olvidé mi contraseña", ya que las contraseñas se almacenan en forma encriptada y no se pueden exportar.
