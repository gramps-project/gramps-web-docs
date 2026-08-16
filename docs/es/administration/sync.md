# Sincronizar Gramps Web y Gramps Desktop

*Gramps Web Sync* es un complemento para Gramps que permite sincronizar tu base de datos de Gramps en tu computadora de escritorio con Gramps Web, incluidos los archivos multimedia.

!!! warning
    Al igual que con cualquier herramienta de sincronización, no consideres esto como una herramienta de respaldo. Una eliminación accidental en un lado se propagará al otro lado. Asegúrate de crear copias de seguridad regulares (en formato XML de Gramps) de tu árbol genealógico.

!!! info
    La documentación se refiere a la última versión del complemento Gramps Web Sync. Utiliza el administrador de complementos de Gramps para actualizar el complemento a la última versión si es necesario.

!!! note "Qué cambió en la versión 1.5"
    La interfaz del complemento fue reescrita en la versión 1.5. El asistente paso a paso ha desaparecido, reemplazado por una única ventana, y los archivos multimedia ahora se confirman junto con los cambios de objeto en lugar de en una página separada después. Si estás buscando el selector de modo de sincronización, ahora se encuentra **por encima** de la lista de cambios en lugar de debajo. El modo de sincronización **merge** ha sido eliminado; consulta [Modo de sincronización](#sync-mode) a continuación.

## Instalación

El complemento requiere Gramps 6.0 ejecutándose en Python 3.10 o superior. Está disponible en Gramps Desktop y se puede instalar [de la manera habitual](https://www.gramps-project.org/wiki/index.php/5.2_Addons#Installing_Addons_in_Gramps).

!!! warning
    Asegúrate de utilizar la misma versión de Gramps en tu escritorio que la que se está ejecutando en tu servidor. Consulta la sección [Obtener ayuda](../help/help.md) para averiguar qué versión de Gramps está ejecutando tu servidor. La versión de Gramps tiene la forma `MAJOR.MINOR.PATCH`, y `MAJOR` y `MINOR` deben ser los mismos en web y escritorio.

### Requisitos del servidor

El complemento verifica dos cosas sobre tu servidor tan pronto como se conecta, y se niega a continuar si alguna de ellas no se cumple. Ambas verificaciones ocurren antes de que se descargue cualquier cosa.

- **Versión 3.x de la API de Gramps Web.** Esta versión del complemento, para Gramps 6.0, funciona con la API de Gramps Web 3. Un servidor más antiguo necesita ser actualizado; un servidor que ejecute una versión principal de API *más nueva* necesita una versión más nueva de Gramps, no un complemento más nuevo, porque cada línea de lanzamiento de Gramps se empareja con una versión de API. Puedes encontrar la versión de tu servidor en *Configuración ▸ Información de versión* en Gramps Web.
- **Una cola de tareas en segundo plano.** La sincronización envía sus cambios como una tarea en segundo plano. En un servidor sin una cola de tareas configurada, aplicar cambios se ejecutaría de forma sincrónica y se agotaría en cualquier árbol genealógico real, por lo que el complemento se niega a comenzar en lugar de fallar a medio camino.

También necesitas una cuenta con al menos privilegios de editor para aplicar cambios a la base de datos remota.

Paso opcional:

??? note inline end "Error del llavero de Gnome"
    Actualmente hay un [error en python keyring](https://github.com/jaraco/keyring/issues/496) que afecta a muchas configuraciones de escritorio de Gnome. Puede que necesites crear el archivo de configuración `~/.config/python_keyring/keyringrc.cfg` y editarlo para que se vea así:

        [backend]
        default-keyring=keyring.backends.SecretService.Keyring

- Instala `keyring` (por ejemplo, `sudo apt install python3-keyring` o `sudo dnf install python3-keyring`) para permitir almacenar la contraseña de la API de forma segura en el administrador de contraseñas de tu sistema.

Si no se puede usar el llavero, el complemento lo indica y continúa sin él: simplemente se te pedirá tu contraseña cada vez. En el paquete **Snap** de Gramps, el llavero del sistema está bloqueado por confinamiento hasta que conectes la interfaz una vez:

```bash
snap connect gramps:password-manager-service
```

El complemento muestra este comando exacto cuando detecta la situación.

## Uso

Una vez instalado, el complemento está disponible en Gramps bajo *Herramientas ▸ Procesamiento de árbol genealógico ▸ Gramps&nbsp;Web&nbsp;Sync*. Después de confirmar el diálogo de advertencia de que el historial de deshacer se descartará, se abre la ventana de sincronización.

**No se aplican cambios a tu árbol local ni al servidor hasta que los confirmes explícitamente.**

La ventana tiene una franja en la parte superior que nombra el árbol genealógico con el que estás sincronizando, la cuenta y la dirección a la que pertenece, y cuándo fue sincronizado por última vez. En la parte inferior, se muestra la versión del complemento y de la API Web del servidor, útil al informar de un problema.

### Conexión

Si has sincronizado este árbol genealógico antes y tu contraseña está almacenada, el complemento se conecta tan pronto como se abre y va directamente a comparar. De lo contrario, pide la URL base de tu instancia de Gramps Web (ejemplo: `https://mygrampsweb.com/`), tu nombre de usuario y tu contraseña.

La URL y el nombre de usuario se almacenan en texto plano en tu directorio de usuario de Gramps. La contraseña se almacena en el administrador de contraseñas de tu sistema solo si dejas marcada la opción **Recordar contraseña**; desmarcarla elimina cualquier contraseña ya almacenada para ese servidor.

!!! tip "Varios árboles genealógicos, varios servidores"
    Cada servidor con el que sincronizas se almacena por separado, junto con su propio registro de cuándo fue sincronizado por última vez. Alternar entre dos servidores ya no interrumpe ninguno.

    Cada entrada también registra **qué árbol genealógico local** fue sincronizado por última vez. El complemento solo se conecta por sí mismo cuando coincide con el árbol que tienes abierto; de lo contrario, muestra los detalles de conexión y espera a que presiones *Conectar*, con una advertencia si las credenciales almacenadas pertenecen a un árbol diferente. Esto es importante porque sincronizar un árbol contra un servidor que contiene un árbol *diferente* propondría eliminar el contenido de ambos.

Hay dos acciones disponibles mientras no se esté escribiendo:

- **Cambiar servidor…**, en la franja superior, regresa a los detalles de conexión para que puedas apuntar este árbol a un servidor diferente. Interrumpe una comparación en progreso en lugar de hacerte esperar a que termine.
- **Olvidar este servidor**, en el panel de conexión, elimina la dirección almacenada, el nombre de usuario y la contraseña, junto con el registro de cuándo este árbol fue sincronizado por última vez. La siguiente sincronización compara entonces los dos árboles desde cero.

Si ingresas una dirección que comienza con `http://` en lugar de `https://`, aparece una advertencia mientras escribes. Tu contraseña se enviaría en texto claro, así que úsala solo para pruebas locales.

### Revisando los cambios

El complemento compara las bases de datos local y remota y muestra lo que propone hacer. A diferencia de versiones anteriores, que enumeraban las diferencias en bruto entre los dos árboles, la lista ahora muestra las **acciones** que se llevarán a cabo, agrupadas por qué base de datos cambian:

```
▾ Cambiará en esta computadora (7 objetos)
    ▾ Agregar 3 objetos
        Persona   John Smith        I0123
    ▾ Actualizar 4 objetos
        …
▾ Cambiará en el servidor (5 objetos)
    …
```

Cada fila nombra el objeto, por lo que puedes saber quién o qué está afectado en lugar de solo ver un ID de Gramps.

Si algo va a ser eliminado, una advertencia sobre la lista dice cuántos objetos y en qué lado. Esto aparece cada vez que se involucran eliminaciones, incluso durante una sincronización bidireccional ordinaria que está propagando una eliminación que hiciste tú mismo.

Presiona **Aplicar** para llevar a cabo lo que describe la lista.

!!! warning "No edites mientras revisas"
    La ventana de sincronización no bloquea el resto de Gramps, por lo que puedes seguir trabajando mientras la lista está abierta. Si editas un objeto afectado, el complemento lo detecta cuando presionas Aplicar, se detiene sin cambiar nada y te pide que compares de nuevo. No se pierde nada, pero la comparación debe repetirse.

#### Modo de sincronización

El modo de sincronización se selecciona **por encima** de la lista de cambios. Cambiarlo reconstruye la lista, porque el modo decide lo que cada diferencia se convierte realmente.

- **Sincronización bidireccional** (el predeterminado) — los cambios de ambos lados se combinan. Los objetos editados en ambos lugares se fusionan.
- **Restablecer el servidor para que coincida con esta computadora** — el servidor se hace coincidir con esta computadora. Cualquier cosa cambiada solo en el servidor se descarta.
- **Restablecer esta computadora para que coincida con el servidor** — esta computadora se hace coincidir con el servidor. Cualquier cosa cambiada solo aquí se descarta.

!!! note
    El modo **merge** disponible en versiones anteriores ha sido eliminado. Se diferenciaba de la sincronización bidireccional solo en restaurar objetos eliminados en un lado en lugar de propagar la eliminación, lo cual no era una distinción que la interfaz pudiera explicar de manera útil. Si dependías de ello, usa la sincronización bidireccional y restaura cualquier cosa que desees conservar de una copia de seguridad.

### Archivos multimedia

Los archivos multimedia se manejan como parte de la misma confirmación, no como un paso separado. Si se necesitan transferir archivos, una casilla de verificación debajo de la lista ofrece moverlos:

```
[x] También transferir 12 archivos multimedia (4 para descargar, 8 para subir)
```

Desmárcala para sincronizar los cambios de objeto sin tocar los archivos.

Los archivos que faltan en *ambos* lados se enumeran por separado, porque no se puede hacer nada al respecto:

```
2 archivos multimedia faltan en ambos lados y no pueden ser transferidos.
```

Ten en cuenta las siguientes limitaciones de la sincronización de archivos multimedia:

- Si un archivo local tiene un checksum diferente al que se almacena en la base de datos de Gramps (esto puede suceder, por ejemplo, con archivos de Word cuando se editan después de ser añadidos a Gramps), la carga fallará con un mensaje de error.
- La herramienta no verifica la integridad de todos los archivos locales, por lo que si un archivo local existe bajo la ruta almacenada para el objeto multimedia, pero el archivo es diferente del archivo en el servidor, la herramienta no lo detectará. Usa el complemento Media Verify para detectar archivos con checksums incorrectos.

### Cuando algo sale mal

Si una sincronización falla a medio camino — una conexión caída, por ejemplo — el complemento informa lo que ya había aplicado y ofrece **Intentar de nuevo**, lo que reanuda en el paso que falló en lugar de comenzar de nuevo. La copia descargada del árbol remoto se conserva, por lo que volver a intentar no descarga y compara de nuevo.

Los detalles técnicos de la falla están disponibles detrás de un expander de *Detalles*, con un botón para copiarlos para un informe de error.

## Solución de problemas

### Registro de depuración

Si estás encontrando problemas con el complemento de sincronización, por favor inicia Gramps con el registro de depuración habilitado [iniciando Gramps desde la línea de comandos](https://gramps-project.org/wiki/index.php/Gramps_5.2_Wiki_Manual_-_Command_Line) con la siguiente opción:

```bash
gramps --debug grampswebsync
```

Esto imprimirá muchas declaraciones de registro útiles en la línea de comandos que te ayudarán a identificar la causa del problema.

### Credenciales del servidor

Si la conexión falla, verifica nuevamente la URL del servidor, tu nombre de usuario y contraseña.

### El complemento se niega a conectarse

Si el complemento informa que la versión de la API de Gramps Web del servidor es demasiado antigua o demasiado nueva, o que no se ha configurado ninguna cola de tareas en segundo plano, consulta [Requisitos del servidor](#server-requirements) arriba. Estas se verifican antes que nada, por lo que el mensaje nombra directamente el problema.

### Problemas de permisos

Si encuentras un error relacionado con permisos, verifica el rol de usuario de tu cuenta de usuario de Gramps Web. Solo puedes aplicar cambios a la base de datos remota si eres un usuario con rol de editor, propietario o administrador.

### Cambios inesperados en la base de datos

Si la herramienta de sincronización detecta cambios que crees que no ocurrieron, podría ser que haya inconsistencias en una de las bases de datos que engañan a Gramps para detectar una diferencia, o que la hora esté desincronizada entre tu computadora local y tu servidor.

Por favor, verifica que los relojes en ambas máquinas estén correctamente configurados (nota, la zona horaria no importa ya que la herramienta utiliza timestamps de Unix, que son agnósticos a la zona horaria).

También puedes ejecutar la herramienta de verificación y reparación en tu base de datos local y ver si esto ayuda.

Un método de fuerza bruta pero efectivo para asegurarte de que las inconsistencias en tu base de datos local no están causando falsos positivos es exportar tu base de datos a XML de Gramps y reimportarla en una nueva base de datos vacía. Esta es una operación sin pérdida, pero asegura que todos los datos se importen de manera consistente.

!!! tip
    Si el complemento propone un número alarmante de eliminaciones, verifica primero la franja superior: nombra el árbol genealógico en el servidor al que estás a punto de escribir. Sincronizar contra un servidor que contiene un árbol *diferente* produce exactamente este síntoma.

### Errores de tiempo de espera

La sincronización con el servidor es procesada por un trabajador en segundo plano, por lo que las sincronizaciones prolongadas no deberían agotar el tiempo. Un servidor sin una cola de tareas configurada se rechaza en el momento de la conexión por esta razón — consulta [Requisitos del servidor](#server-requirements).

Las solicitudes del complemento al servidor se agotan después de 60 segundos sin respuesta, por lo que un servidor inalcanzable informa un error de conexión en lugar de colgarse indefinidamente.

### Errores inesperados de archivos multimedia

Si la carga de un archivo multimedia falla, a menudo se debe a un desajuste en el checksum del archivo real en disco y el checksum en la base de datos local de Gramps. Esto sucede a menudo con archivos editables, como documentos de oficina, editados fuera de Gramps. Por favor, utiliza el complemento Gramps Media Verify para corregir los checksums de todos los archivos multimedia.

### Pide ayuda

Si todo lo anterior no ayuda, puedes pedir ayuda a la comunidad publicando en la [categoría Gramps Web del foro de Gramps](https://gramps.discourse.group/c/gramps-web/28). Asegúrate de proporcionar:

- la versión del complemento Gramps Web Sync (y utiliza la última versión lanzada, por favor) — se muestra en la parte inferior de la ventana de sincronización, junto a la versión de la API Web del servidor
- la versión de Gramps desktop que estás utilizando
- la salida del registro de depuración de Gramps, habilitada como se describe arriba
- la información de versión de Gramps Web (puedes encontrarla en Configuración/Información de versión)
- cualquier detalle que puedas proporcionar sobre tu instalación de Gramps Web (autoalojado, Grampshub, ...)
- la salida de los registros de tu servidor Gramps Web, si tienes acceso a ellos (cuando usas docker: `docker compose logs --tail 100 grampsweb` y `docker compose logs --tail 100 grampsweb-celery`)

## Antecedentes: cómo funciona el complemento

Si tienes curiosidad sobre cómo funciona realmente el complemento, puedes encontrar más detalles en esta sección.

El complemento está diseñado para mantener una base de datos local de Gramps sincronizada con una base de datos remota de Gramps Web, para permitir tanto cambios locales como remotos (edición colaborativa).

No es **adecuado**

- Para sincronizar con una base de datos que no sea un derivado directo (comenzando desde una copia de base de datos o exportación/importación de XML de Gramps) de la base de datos local
- Para fusionar dos bases de datos con un gran número de cambios en ambos lados que necesitan atención manual para la fusión. Usa la excelente [Import Merge Tool](https://www.gramps-project.org/wiki/index.php/Import_Merge_Tool) para este propósito.

Los principios de operación de la herramienta son muy simples:

- Compara las bases de datos local y remota
- Si hay diferencias, verifica la marca de tiempo del último objeto idéntico, llamémoslo **t**
- Si un objeto cambió más recientemente que **t** existe en una base de datos pero no en la otra, se sincroniza en ambas (asumir objeto nuevo)
- Si un objeto cambió la última vez antes de **t** está ausente en una base de datos, se elimina en ambas (asumir objeto eliminado)
- Si un objeto es diferente pero cambió después de **t** solo en una base de datos, se sincroniza con la otra (asumir objeto modificado)
- Si un objeto es diferente pero cambió después de **t** en ambas bases de datos, se fusionan (asumir modificación conflictiva)

El tiempo de la última sincronización exitosa también se registra, por separado para cada servidor, y se utiliza como **t** cuando es más reciente que el objeto idéntico más nuevo.

Este algoritmo es simple y robusto ya que no requiere rastrear el historial de sincronización. Sin embargo, funciona mejor cuando *sincronizas a menudo*.
