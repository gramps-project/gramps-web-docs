# Sincronizar Gramps Web y Gramps Desktop

*Gramps Web Sync* es un complemento para Gramps que sincroniza la base de datos de Gramps en tu computadora de escritorio con Gramps Web, incluidos los archivos multimedia. Los cambios realizados en cualquiera de los lados se trasladan al otro, por lo que puedes trabajar localmente y en la web en el mismo árbol genealógico.

Como cualquier herramienta de sincronización, no es una copia de seguridad: si eliminas algo en un lado, también se eliminará en el otro lado. Mantén copias de seguridad regulares de tu árbol genealógico en formato XML de Gramps.

## Instalación

El complemento requiere Gramps 6.0 ejecutándose en Python 3.10 o superior. Está disponible en Gramps Desktop y se puede instalar [de la manera habitual](https://www.gramps-project.org/wiki/index.php/5.2_Addons#Installing_Addons_in_Gramps). Esta documentación describe la última versión del complemento; usa el administrador de complementos de Gramps para actualizarlo si es necesario.

Tu computadora de escritorio y tu servidor deben ejecutar la misma versión de Gramps. La versión tiene la forma `MAJOR.MINOR.PATCH`, y `MAJOR` y `MINOR` deben coincidir. Consulta [Obtener ayuda](../help/help.md) para saber qué versión de Gramps está ejecutando tu servidor.

### Requisitos del servidor

El complemento verifica dos cosas sobre tu servidor tan pronto como se conecta, antes de que se descargue cualquier cosa, y se detiene con un mensaje si alguna de ellas no se cumple:

- **Versión de la API de Gramps Web 3.x.** Esta versión del complemento, para Gramps 6.0, funciona con la API de Gramps Web 3. Un servidor más antiguo necesita ser actualizado; un servidor que ejecute una versión principal de API *más nueva* necesita una versión más nueva de Gramps, no un complemento más nuevo, porque cada línea de lanzamiento de Gramps se empareja con una versión de API. Puedes encontrar la versión de tu servidor en *Configuración ▸ Información de versión* en Gramps Web.
- **Una cola de tareas en segundo plano.** Los cambios se aplican en el servidor como una tarea en segundo plano. Sin una cola de tareas, esto se ejecutaría de manera sincrónica y se agotaría en cualquier árbol genealógico real.

Para aplicar cambios a la base de datos remota, necesitas una cuenta con el rol de editor, propietario o administrador.

### Almacenamiento de tu contraseña (opcional)

Instala `keyring` (por ejemplo, `sudo apt install python3-keyring` o `sudo dnf install python3-keyring`) para almacenar la contraseña de la API en el administrador de contraseñas de tu sistema. Si no se puede usar el keyring, el complemento lo indicará y continuará sin él; simplemente se te pedirá tu contraseña cada vez.

En el paquete **Snap** de Gramps, el keyring del sistema está bloqueado por confinamiento hasta que conectes la interfaz una vez. El complemento muestra este comando cuando detecta la situación:

```bash
snap connect gramps:password-manager-service
```

En muchas configuraciones de escritorio de Gnome, un [error en python keyring](https://github.com/jaraco/keyring/issues/496) significa que debes crear el archivo de configuración `~/.config/python_keyring/keyringrc.cfg` con el siguiente contenido:

```ini
[backend]
default-keyring=keyring.backends.SecretService.Keyring
```

## Uso

El complemento está disponible en Gramps bajo *Herramientas ▸ Procesamiento de Árbol Genealógico ▸ Gramps&nbsp;Web&nbsp;Sync*. Después de confirmar el aviso del diálogo de que el historial de deshacer se descartará, se abre la ventana de sincronización. No se aplican cambios a tu árbol local ni al servidor hasta que los confirmes explícitamente.

Una franja en la parte superior de la ventana nombra el árbol genealógico con el que estás sincronizando, la cuenta y la dirección a la que pertenece, y cuándo fue la última sincronización. En la parte inferior, se muestra la versión del complemento y de la API Web del servidor, lo cual es útil al informar un problema.

### Conectando

Si has sincronizado este árbol genealógico antes y tu contraseña está almacenada, el complemento se conecta tan pronto como se abre y va directamente a comparar. De lo contrario, solicita la URL base de tu instancia de Gramps Web (ejemplo: `https://mygrampsweb.com/`), tu nombre de usuario y tu contraseña.

La URL y el nombre de usuario se almacenan en texto plano en tu directorio de usuario de Gramps. La contraseña se almacena en el administrador de contraseñas de tu sistema solo si dejas marcada la opción **Recordar contraseña**; desmarcarla elimina cualquier contraseña ya almacenada para ese servidor. Si ingresas una dirección que comienza con `http://` en lugar de `https://`, el complemento te advertirá mientras escribes, porque tu contraseña se enviaría en texto claro.

Cada servidor con el que sincronizas se almacena por separado, junto con su propio registro de cuándo fue la última sincronización, por lo que puedes alternar entre dos servidores sin alterar ninguno. Cada entrada también registra qué árbol genealógico local fue sincronizado por última vez. El complemento solo se conecta por sí mismo cuando coincide con el árbol que tienes abierto; de lo contrario, muestra los detalles de conexión y espera a que presiones *Conectar*.

Dos acciones están disponibles mientras no se esté escribiendo nada:

- **Cambiar servidor…**, en la franja superior, regresa a los detalles de conexión para que puedas apuntar este árbol a un servidor diferente. Interrumpe una comparación en progreso en lugar de hacerte esperar a que termine.
- **Olvidar este servidor**, en el panel de conexión, elimina la dirección almacenada, el nombre de usuario y la contraseña, junto con el registro de cuándo este árbol se sincronizó por última vez. La próxima sincronización comparará entonces los dos árboles desde cero.

### Revisando los cambios

El complemento compara las bases de datos local y remota y muestra las acciones que propone llevar a cabo, agrupadas por qué base de datos cambian:

```
▾ Cambiará en esta computadora (7 objetos)
    ▾ Agregar 3 objetos
        Persona   John Smith        I0123
    ▾ Actualizar 4 objetos
        …
▾ Cambiará en el servidor (5 objetos)
    …
```

Cada fila nombra el objeto, por lo que puedes saber quién o qué se ve afectado en lugar de solo ver un ID de Gramps. Si algo va a ser eliminado, una nota sobre la lista dice cuántos objetos y en qué lado.

Presiona **Aplicar** para llevar a cabo lo que describe la lista.

La ventana de sincronización no bloquea el resto de Gramps, por lo que puedes seguir trabajando mientras la lista está abierta. Si editas un objeto afectado en el ínterin, el complemento lo notará cuando presiones Aplicar, se detendrá sin cambiar nada y te pedirá que compares nuevamente.

#### Modo de sincronización

El modo de sincronización se selecciona sobre la lista de cambios. Cambiarlo reconstruye la lista, porque el modo decide qué se convierte cada diferencia.

- **Sincronización bidireccional** (el predeterminado) – los cambios de ambos lados se combinan. Los objetos editados en ambos lugares se fusionan.
- **Restablecer el servidor para que coincida con esta computadora** – el servidor se hace coincidir con esta computadora. Cualquier cosa cambiada solo en el servidor se descarta.
- **Restablecer esta computadora para que coincida con el servidor** – esta computadora se hace coincidir con el servidor. Cualquier cosa cambiada solo aquí se descarta.

El modo **fusionar** disponible en versiones anteriores a 1.5 ha sido eliminado. Se diferenciaba de la sincronización bidireccional solo en restaurar objetos eliminados en un lado en lugar de propagar la eliminación. Si dependías de él, usa la sincronización bidireccional y restaura cualquier cosa que desees conservar de una copia de seguridad.

### Archivos multimedia

Los archivos multimedia se manejan como parte de la misma confirmación, no como un paso separado. Si se necesitan transferir archivos, una casilla de verificación debajo de la lista ofrece moverlos:

```
[x] También transferir 12 archivos multimedia (4 para descargar, 8 para cargar)
```

Desmarca esta opción para sincronizar los cambios de objeto sin tocar los archivos.

Los archivos que faltan en *ambos* lados se enumeran por separado, porque no se puede hacer nada al respecto:

```
2 archivos multimedia faltan en ambos lados y no se pueden transferir.
```

La sincronización de archivos multimedia tiene dos limitaciones:

- Si un archivo local tiene un checksum diferente al que está almacenado en la base de datos de Gramps (esto puede suceder, por ejemplo, con archivos de Word editados después de ser añadidos a Gramps), la carga fallará con un mensaje de error.
- La herramienta no verifica la integridad de todos los archivos locales. Si un archivo existe bajo la ruta almacenada para el objeto multimedia pero difiere del archivo en el servidor, la herramienta no lo detectará. Usa el complemento Media Verify para encontrar archivos con checksums incorrectos.

### Si una sincronización falla

Si una sincronización falla a mitad de camino – una conexión caída, por ejemplo – el complemento informa lo que ya había aplicado y ofrece **Intentar de nuevo**, lo que reanuda en el paso que falló en lugar de comenzar de nuevo. La copia descargada del árbol remoto se mantiene, por lo que volver a intentar no descarga y compara nuevamente.

Los detalles técnicos de la falla están disponibles detrás de un expander de *Detalles*, con un botón para copiarlos para un informe de error.

## Solución de problemas

**Cambios inesperados.** Si el complemento propone un número alarmante de eliminaciones, verifica primero la franja superior: nombra el árbol genealógico en el servidor al que estás a punto de escribir. Sincronizar un árbol contra un servidor que tiene un árbol *diferente* produce exactamente este síntoma.

De lo contrario, las diferencias que no esperabas pueden provenir de inconsistencias en una de las bases de datos, o de relojes que están desincronizados entre tu computadora y tu servidor. Verifica que ambos relojes estén correctamente configurados (la zona horaria no importa, ya que la herramienta utiliza marcas de tiempo de Unix) y ejecuta la herramienta de verificación y reparación en tu base de datos local. Como último recurso, exporta tu base de datos local a Gramps XML y reimportala en una nueva base de datos vacía. Esta es una operación sin pérdida, pero asegura que todos los datos se almacenen de manera consistente.

**Errores de archivos multimedia.** Una carga fallida a menudo es causada por un desajuste entre el checksum del archivo en disco y el checksum en la base de datos local de Gramps, lo que ocurre con archivos editables como documentos de oficina editados fuera de Gramps. Usa el complemento Gramps Media Verify para corregir los checksums.

**Errores de permisos.** Verifica el rol de tu cuenta de usuario de Gramps Web: solo los editores, propietarios y administradores pueden aplicar cambios a la base de datos remota.

### Pide ayuda

Si nada de lo anterior ayuda, pregunta a la comunidad publicando en la [categoría Gramps Web del foro de Gramps](https://gramps.discourse.group/c/gramps-web/28). Por favor proporciona:

- la versión del complemento Gramps Web Sync, que se muestra en la parte inferior de la ventana de sincronización junto a la versión de la API Web del servidor (y por favor usa la última versión lanzada)
- la versión de Gramps desktop que estás usando
- la información de versión de Gramps Web, que se encuentra en *Configuración ▸ Información de versión*
- cualquier detalle sobre tu instalación de Gramps Web (autoalojada, Grampshub, ...)
- la salida de los registros de tu servidor Gramps Web, si tienes acceso a ellos (cuando usas Docker: `docker compose logs --tail 100 grampsweb` y `docker compose logs --tail 100 grampsweb-celery`)

Si se te pide un registro de depuración, inicia Gramps [desde la línea de comandos](https://gramps-project.org/wiki/index.php/Gramps_5.2_Wiki_Manual_-_Command_Line) con el registro de depuración habilitado y reproduce el problema:

```bash
gramps --debug grampswebsync
```

## Antecedentes: cómo funciona el complemento

El complemento está diseñado para mantener una base de datos local de Gramps sincronizada con una base de datos remota de Gramps Web, permitiendo tanto cambios locales como remotos (edición colaborativa).

No es **adecuado**

- para sincronizar con una base de datos que no sea un derivado directo (comenzando desde una copia de base de datos o exportación/importación de Gramps XML) de la base de datos local,
- para fusionar dos bases de datos con un gran número de cambios en ambos lados que necesitan atención manual para la fusión. Usa la excelente [Herramienta de Importación y Fusión](https://www.gramps-project.org/wiki/index.php/Import_Merge_Tool) para este propósito.

Los principios de operación son simples:

- Compara las bases de datos local y remota.
- Si hay diferencias, verifica la marca de tiempo del último objeto idéntico, llamémoslo **t**.
- Si un objeto cambió más recientemente que **t** existe en una base de datos pero no en la otra, se sincroniza en ambas (asumir objeto nuevo).
- Si un objeto cambió la última vez antes de **t** está ausente en una base de datos, se elimina en ambas (asumir objeto eliminado).
- Si un objeto es diferente pero cambió después de **t** solo en una base de datos, se sincroniza con la otra (asumir objeto modificado).
- Si un objeto es diferente pero cambió después de **t** en ambas bases de datos, se fusionan (asumir modificación en conflicto).

El tiempo de la última sincronización exitosa también se registra, por separado para cada servidor, y se utiliza como **t** cuando es más reciente que el objeto idéntico más nuevo.

Este algoritmo es simple y robusto ya que no requiere rastrear el historial de sincronización. Sin embargo, funciona mejor cuando *sincronizas a menudo*.
