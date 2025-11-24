# Sincronizar Gramps Web y Gramps Desktop

*Gramps Web Sync* es un complemento para Gramps que permite sincronizar tu base de datos de Gramps en tu computadora de escritorio con Gramps Web, incluidos los archivos multimedia.

!!! warning
    Al igual que con cualquier herramienta de sincronización, no consideres esto como una herramienta de respaldo. Una eliminación accidental en un lado se propagará al otro lado. Asegúrate de crear copias de seguridad regulares (en formato XML de Gramps) de tu árbol genealógico.

!!! info
    La documentación se refiere a la última versión del complemento Gramps Web Sync. Utiliza el administrador de complementos de Gramps para actualizar el complemento a la última versión si es necesario.

## Instalación

El complemento requiere Gramps 6.0 ejecutándose en Python 3.10 o superior.  
Está disponible en Gramps Desktop y se puede instalar [de la manera habitual](https://www.gramps-project.org/wiki/index.php/5.2_Addons#Installing_Addons_in_Gramps).

!!! warn
    Asegúrate de usar la misma versión de Gramps en tu escritorio que la que se está ejecutando en tu servidor. Consulta la sección [Obtener ayuda](../help/help.md) para saber qué versión de Gramps está ejecutando tu servidor. La versión de Gramps tiene la forma `MAJOR.MINOR.PATCH`, y `MAJOR` y `MINOR` deben ser los mismos en web y escritorio.

Paso opcional:

??? note inline end "Error en el llavero de Gnome"
    Actualmente hay un [error en el llavero de python](https://github.com/jaraco/keyring/issues/496) que afecta a muchas configuraciones de escritorio de Gnome. Es posible que necesites crear el archivo de configuración `~/.config/python_keyring/keyringrc.cfg` y editarlo para que se vea así:

        [backend]
        default-keyring=keyring.backends.SecretService.Keyring

- Instala `keyring` (por ejemplo, `sudo apt install python3-keyring` o `sudo dnf install python3-keyring`) para permitir almacenar la contraseña de la API de forma segura en el administrador de contraseñas de tu sistema.

## Uso

Una vez instalado, el complemento está disponible en Gramps bajo *Herramientas > Procesamiento del árbol genealógico > Gramps&nbsp;Web&nbsp;Sync*. Una vez iniciado, y después de confirmar el diálogo de que el historial de deshacer se descartará, un asistente te guiará a través de los pasos de sincronización. Ten en cuenta que no se aplicarán cambios a tu árbol local ni al servidor hasta que los confirmes explícitamente.

### Paso 1: ingresar credenciales del servidor

La herramienta te pedirá la URL base (ejemplo: `https://mygrampsweb.com/`) de tu instancia de Gramps Web, tu nombre de usuario y contraseña. Necesitas una cuenta con al menos privilegios de editor para sincronizar cambios de vuelta a tu base de datos remota. El nombre de usuario y la URL se almacenarán en texto plano en tu directorio de usuario de Gramps, la contraseña solo se almacenará si `keyring` está instalado (ver arriba).

### Paso 2: revisar cambios

Después de confirmar tus credenciales, la herramienta compara las bases de datos local y remota y evalúa si hay alguna diferencia. Si las hay, muestra una lista de cambios de objetos (donde un objeto puede ser una persona, familia, evento, lugar, etc.) pertenecientes a una de las siguientes categorías:

- agregado localmente
- eliminado localmente
- modificado localmente
- agregado remotamente 
- eliminado remotamente
- modificado remotamente
- modificado simultáneamente (es decir, en ambos lados)

La herramienta utiliza marcas de tiempo para evaluar qué lado es más nuevo para cada objeto (ver "Antecedentes" a continuación si estás interesado en los detalles).

Si los cambios parecen ser los esperados, puedes hacer clic en "Aplicar" para aplicar los cambios necesarios a las bases de datos local y remota.

!!! tip "Avanzado: Modo de sincronización"
    Debajo de la lista de cambios, puedes seleccionar un modo de sincronización.
    
    El modo predeterminado, **sincronización bidireccional**, significa que aplicará cambios a ambos lados (local y remoto) replicando los cambios detectados (los objetos agregados localmente se agregarán en el lado remoto, etc.). Los objetos modificados en ambos lados se fusionarán y actualizarán también en ambos lados.

    La opción **restablecer remoto a local** asegurará que la base de datos remota de Gramps se vea exactamente como la local. Cualquier objeto detectado como "agregado remotamente" se eliminará nuevamente, los objetos detectados como "eliminados remotamente" se agregarán nuevamente, etc. *No se aplicarán cambios a la base de datos local de Gramps.*

    La opción **restablecer local a remoto** funciona de la manera opuesta y establece el estado local al de la base de datos remota. *No se aplicarán cambios a la base de datos remota.*

    Finalmente, la opción **fusionar** es similar a la sincronización bidireccional en que modifica ambas bases de datos, pero *no elimina ningún objeto*, sino que restaura todos los objetos eliminados en solo un lado.

### Paso 3: sincronizar archivos multimedia

*Después* de que las bases de datos han sido sincronizadas, la herramienta verifica si hay archivos multimedia nuevos o actualizados. Si encuentra alguno, muestra una lista y solicita confirmación para cargar/descargar los archivos necesarios.

Ten en cuenta las siguientes limitaciones de la sincronización de archivos multimedia:

- Si un archivo local tiene un checksum diferente al que se almacena en la base de datos de Gramps (esto puede suceder, por ejemplo, con archivos de Word cuando se editan después de ser agregados a Gramps), la carga fallará con un mensaje de error.
- La herramienta no verifica la integridad de todos los archivos locales, por lo que si un archivo local existe bajo la ruta almacenada para el objeto multimedia, pero el archivo es diferente del archivo en el servidor, la herramienta no lo detectará. Usa el complemento Media Verify para detectar archivos con checksums incorrectos.

## Solución de problemas

### Registro de depuración

Si estás encontrando problemas con el complemento Sync, por favor inicia Gramps con el registro de depuración habilitado [iniciando Gramps desde la línea de comandos](https://gramps-project.org/wiki/index.php/Gramps_5.2_Wiki_Manual_-_Command_Line) con la siguiente opción:

```bash
gramps --debug grampswebsync
```

Esto imprimirá muchas declaraciones de registro útiles en la línea de comandos que te ayudarán a identificar la causa del problema.

### Credenciales del servidor

Si el primer paso ya falla, verifica nuevamente la URL del servidor, tu nombre de usuario y contraseña.

### Problemas de permisos

Si encuentras un error relacionado con permisos, verifica el rol de usuario de tu cuenta de usuario de Gramps Web. Solo puedes aplicar cambios a la base de datos remota si eres un usuario con rol de editor, propietario o administrador.

### Cambios inesperados en la base de datos

Si la herramienta de sincronización detecta cambios que crees que no ocurrieron, podría ser que haya inconsistencias en una de las bases de datos que engañan a Gramps para detectar una diferencia, o que la hora esté desincronizada entre tu computadora local y tu servidor.

Por favor, verifica que los relojes en ambas máquinas estén correctamente configurados (ten en cuenta que la zona horaria no importa, ya que la herramienta utiliza marcas de tiempo de Unix, que son independientes de la zona horaria).

También puedes ejecutar la herramienta de verificación y reparación en tu base de datos local y ver si esto ayuda.

Un método de fuerza bruta pero efectivo para asegurarte de que las inconsistencias en tu base de datos local no estén causando falsos positivos es exportar tu base de datos a Gramps XML y reimportarla en una nueva base de datos vacía. Esta es una operación sin pérdida, pero asegura que todos los datos se importen de manera consistente.

### Errores de tiempo de espera

Si estás experimentando errores de tiempo de espera (por ejemplo, indicados por un error de estado HTTP 408 u otro mensaje de error que incluya la palabra "timeout"), es probable que se deba a un gran número de cambios que necesitan ser sincronizados al lado remoto en combinación con la configuración de tu servidor.

Para versiones del complemento de sincronización anteriores a v1.2.0 y versiones de la API de Gramps Web anteriores a v2.7.0 (ver la pestaña de información de versión en Gramps Web), la sincronización al lado del servidor se procesaba en una única solicitud que podría agotar el tiempo, dependiendo de la configuración del servidor, después de uno a, como máximo, unos pocos minutos. Para sincronizaciones grandes (como después de importar miles de objetos en la base de datos local o intentar sincronizar una base de datos local completa a una base de datos del lado del servidor vacía), esto puede ser demasiado corto.

Si estás utilizando el complemento de sincronización v1.2.0 o posterior y la API de Gramps Web v2.7.0 o posterior, la sincronización del lado del servidor se procesa mediante un trabajador en segundo plano y puede ejecutarse durante mucho tiempo (se mostrará una barra de progreso) y no deberían ocurrir errores de tiempo de espera.

### Errores inesperados de archivos multimedia

Si la carga de un archivo multimedia falla, a menudo se debe a una discrepancia en el checksum del archivo real en el disco y el checksum en la base de datos local de Gramps. Esto sucede a menudo con archivos editables, como documentos de oficina, editados fuera de Gramps. Por favor, utiliza el complemento Gramps Media Verify para corregir los checksums de todos los archivos multimedia.

### Pide ayuda

Si todo lo anterior no ayuda, puedes pedir ayuda a la comunidad publicando en la [categoría Gramps Web del foro de Gramps](https://gramps.discourse.group/c/gramps-web/28). Asegúrate de proporcionar:

- la versión del complemento Gramps Web Sync (y usa la última versión lanzada, por favor)
- la versión de Gramps desktop que estás utilizando
- la salida del registro de depuración de Gramps, habilitado como se describe arriba
- la información de versión de Gramps Web (puedes encontrarla en Configuración/Información de versión)
- cualquier detalle que puedas proporcionar sobre tu instalación de Gramps Web (autoalojado, Grampshub, ...)
- la salida de los registros de tu servidor Gramps Web, si tienes acceso a ellos (cuando uses docker: `docker compose logs --tail 100 grampsweb` y `docker compose logs --tail 100 grampsweb-celery`)

## Antecedentes: cómo funciona el complemento

Si tienes curiosidad sobre cómo funciona realmente el complemento, puedes encontrar más detalles en esta sección.

El complemento está destinado a mantener una base de datos local de Gramps en sincronía con una base de datos remota de Gramps Web, para permitir tanto cambios locales como remotos (edición colaborativa).

No es **adecuado**

- Para sincronizar con una base de datos que no sea un derivado directo (comenzando desde una copia de base de datos o exportación/importación de Gramps XML) de la base de datos local
- Para fusionar dos bases de datos con un gran número de cambios en ambos lados que necesiten atención manual para la fusión. Usa la excelente [Herramienta de Importación y Fusión](https://www.gramps-project.org/wiki/index.php/Import_Merge_Tool) para este propósito.

Los principios de operación de la herramienta son muy simples:

- Compara las bases de datos local y remota
- Si hay diferencias, verifica la marca de tiempo del último objeto idéntico, llamémoslo **t**
- Si un objeto cambió más recientemente que **t** existe en una base de datos pero no en la otra, se sincroniza a ambas (asumir objeto nuevo)
- Si un objeto cambió la última vez antes de **t** está ausente en una base de datos, se elimina en ambas (asumir objeto eliminado)
- Si un objeto es diferente pero cambió después de **t** solo en una base de datos, se sincroniza con la otra (asumir objeto modificado)
- Si un objeto es diferente pero cambió después de **t** en ambas bases de datos, se fusionan (asumir modificación en conflicto)

Este algoritmo es simple y robusto ya que no requiere rastrear el historial de sincronización. Sin embargo, funciona mejor cuando *sincronizas a menudo*.
