# Configuración de Administración

La página de **Configuración > Administración** es accesible a través del icono de usuario en la barra superior de la aplicación. Solo está disponible para usuarios con el rol de Propietario o Administrador y proporciona herramientas para gestionar la base de datos del árbol genealógico.

La página está organizada en secciones colapsables. Haz clic en el encabezado de una sección para expandirla.

## Datos

Cubre cuotas de uso, importación de datos y gestión de archivos multimedia.

### Cuotas de uso

La parte superior de la sección muestra el uso actual en relación con los límites configurados:

- **Personas** – el número de objetos de persona en el árbol frente al máximo configurado (∞ si es ilimitado)
- **Almacenamiento multimedia** – tamaño total de los archivos multimedia subidos frente a la cuota de almacenamiento configurada (∞ si es ilimitado)

Las cuotas son establecidas por el administrador del servidor; consulta [Configuración del servidor](../install_setup/configuration.md) para más detalles.

### Importar datos

La sección de importación te permite subir un archivo de árbol genealógico o un archivo de medios. Consulta [Importar datos](import.md) para obtener instrucciones completas.

### Estado de archivos multimedia

Esta sección muestra:

- El número total de objetos multimedia en el árbol y si alguno carece de una suma de verificación
- El número de objetos multimedia cuyo archivo asociado falta en el servidor

Una marca de verificación verde indica que todo está en orden. Si se detectan problemas, se muestran enlaces a los objetos afectados. Las sumas de verificación faltantes suelen ocurrir cuando los datos se importaron desde un formato como GEDCOM que incluye referencias multimedia pero no los archivos reales. Los archivos faltantes se pueden subir a través de la función de importar archivo multimedia.

### Importar archivo multimedia

Permite subir un archivo ZIP de archivos multimedia para completar los archivos faltantes. Consulta [Importar datos](import.md) para obtener instrucciones completas.

## Índice de búsqueda

### Gestionar índice de búsqueda

Gramps Web mantiene un índice de búsqueda de texto completo que normalmente se actualiza automáticamente cada vez que cambian los datos. El indicador de estado muestra cuántos objetos están actualmente indexados frente al recuento total de objetos.

Haz clic en **Actualizar índice de búsqueda** para desencadenar una reconstrucción completa. Se muestra un indicador de progreso mientras la tarea se ejecuta en segundo plano. Esto generalmente solo es necesario después de una actualización del servidor.

### Índice de búsqueda semántica

!!! warning "Obsoleto"
    La búsqueda semántica está obsoleta y se eliminará en la API de Gramps Web 3.25, junto con esta sección. El chat de IA no la necesita ya que la API de Gramps Web 3.24.

Si el servidor tiene [búsqueda semántica (potenciada por IA) habilitada](../install_setup/chat.md#semantic-search-deprecated), aparece una sección adicional con dos acciones:

- **Regenerar índice de búsqueda semántica** – reconstruye todo el índice semántico desde cero. Esto es computacionalmente costoso y puede llevar mucho tiempo.
- **Actualizar índice de búsqueda semántica** – realiza una actualización incremental, agregando solo objetos que aún no están indexados. Más rápido que una reconstrucción completa.

## Configuración del árbol

### Nombre del árbol genealógico

!!! note
    Cambiar el nombre del árbol solo funciona en una [configuración de múltiples árboles](../install_setup/multi-tree.md) o cuando `TREE_ID` está explícitamente configurado en la [configuración del servidor](../install_setup/configuration.md). En una instalación predeterminada de un solo árbol sin `TREE_ID` configurado, esto generará un error.

Esto permite cambiar el nombre de la base de datos del árbol genealógico de Gramps subyacente. Ingresa un nuevo nombre y haz clic en **Renombrar** para aplicar.

!!! tip
    Si solo deseas cambiar el nombre que se muestra en la barra de la aplicación sin renombrar la base de datos, utiliza la configuración de [Título de la aplicación](#app-title) en su lugar.

### Información del investigador

Establece el nombre, dirección y detalles de contacto del investigador principal. Esta información se incrusta en las exportaciones (por ejemplo, archivos GEDCOM).

## Personalización

### Colores del tema

Establece un **color primario** y un **color de acento** personalizados para la interfaz de Gramps Web. Estos colores se aplican a todos los usuarios de este árbol y entran en efecto inmediatamente después de guardar.

Utiliza los selectores de color para seleccionar colores, luego haz clic en **Guardar**. Haz clic en **Restablecer** para volver a los valores predeterminados.

### Título de la aplicación

Establece un título personalizado para la aplicación. Si se establece, esto anula el nombre del árbol genealógico en la barra de título del navegador y en la barra superior de la aplicación.

Ingresa un título y haz clic en **Guardar**. Deja en blanco para usar el valor predeterminado (el nombre del árbol genealógico).

### Nota de la página de inicio

Selecciona un objeto **Nota** de Gramps para mostrar en la página de inicio del panel de control. El contenido de la nota se renderiza debajo de las columnas principales del panel de control y es visible para todos los usuarios con acceso al árbol.

Utiliza el selector de objetos para buscar y seleccionar una nota, luego guarda. Haz clic en **Eliminar** para borrar la nota actual de la página de inicio.

### Imagen de la página de inicio

Selecciona un objeto **Media** de Gramps para mostrar como una imagen en la página de inicio del panel de control. Cuando se combina con una nota de la página de inicio, la imagen aparece junto al texto de la nota. Sin una nota, solo se muestra la imagen.

Utiliza el selector de objetos para buscar y seleccionar un objeto multimedia, luego guarda. Haz clic en **Eliminar** para borrar la imagen actual de la página de inicio.

### Configuración de exportación/importación

Las configuraciones a nivel de árbol (título de la aplicación, colores del tema, nota/imágen de la página de inicio, etc.) se pueden exportar como un archivo JSON para respaldo o para copiar a otra instancia de Gramps Web.

- Haz clic en **Exportar configuraciones** para descargar la configuración actual como un archivo JSON.
- Haz clic en **Importar configuraciones del árbol** para subir un archivo JSON exportado previamente y aplicar las configuraciones.

## Procesamiento del árbol genealógico

### Comprobar y reparar la base de datos

Esta herramienta verifica la base de datos de Gramps en busca de inconsistencias internas y repara las que puede – análogo a la herramienta [Comprobar y reparar base de datos](https://www.gramps-project.org/wiki/index.php/Gramps_5.2_Wiki_Manual_-_Tools#Check_and_Repair_Database) en Gramps Desktop.

Haz clic en **Comprobar y reparar** y espera a que el indicador de progreso se complete. El resultado se muestra debajo del botón:

- Si no se encontraron errores, se muestra un mensaje de confirmación.
- Si se encontraron errores, se muestra un resumen de las correcciones aplicadas.

Ejecuta esta herramienta si encuentras errores o comportamientos inesperados que pueden ser causados por inconsistencias en la base de datos, como relaciones faltantes entre objetos.

### Verificar los datos

Mientras que [Comprobar y reparar base de datos](#check-and-repair-database) busca inconsistencias *técnicas*, esta herramienta busca datos *implausibles* – análogo a la herramienta [Verificar los datos](https://gramps-project.org/wiki/index.php/Gramps_5.0_Wiki_Manual_-_Tools#Verify_the_Data) en Gramps Desktop. Informa sobre cosas que no son imposibles, pero son lo suficientemente improbables como para merecer una segunda revisión, como una madre de 12 años o una persona que vivió hasta los 130.

Bajo **Opciones** puedes ajustar los umbrales que utilizan las pruebas – edad máxima, edad mínima y máxima para casarse o tener hijos, número máximo de hijos, y así sucesivamente – así como si estimar fechas faltantes o inexactas y si informar fechas inválidas como el 31 de febrero.

Haz clic en **Verificar los datos** para comenzar. La verificación se ejecuta como una tarea en segundo plano, y los hallazgos se enumeran luego bajo **Resultados de verificación de datos**. Esta herramienta no cambia nada: solo informa lo que encuentra.

!!! note
    Un hallazgo no es prueba de un error. Las vidas largas y las grandes diferencias de edad ocurren, así que trata los resultados como una lista de cosas a verificar en lugar de una lista de cosas a corregir.

## Etiquetas

### Gestionar etiquetas

Crea, renombra, recolorea y elimina [etiquetas](../user-guide/tags.md) para el árbol genealógico. Las etiquetas se almacenan en la base de datos de Gramps, se comparten entre todos los usuarios y son totalmente compatibles con Gramps Desktop.

Haz clic en **Nueva etiqueta** para crear una etiqueta. Utiliza los controles junto a una etiqueta existente para renombrarla (icono de lápiz), cambiar su color (selector de color) o eliminarla (icono de eliminar).

!!! note
    Eliminar una etiqueta la quita de todos los objetos a los que se aplicó.

Consulta [Etiquetas](../user-guide/tags.md) para ver cómo se utilizan las etiquetas en Gramps Web, incluidas las etiquetas especiales `Blog` y `ToDo`.

## Copias de seguridad

Una copia de seguridad contiene los datos del árbol genealógico, incluidos registros privados, la configuración del árbol y los usuarios del árbol. Los archivos multimedia no están incluidos; consulta [Haz una copia de seguridad de tus archivos multimedia](export.md#back-up-your-media-files).

### Copias de seguridad almacenadas

Si el administrador del servidor ha configurado un directorio de copias de seguridad (`BACKUP_DIR`, consulta [Configuración del servidor](../install_setup/configuration.md)), las copias de seguridad se pueden almacenar en el servidor. De lo contrario, la sección muestra un aviso de que no se ha configurado el almacenamiento de copias de seguridad, y solo está disponible la restauración desde un archivo subido.

Haz clic en **Hacer copia de seguridad...** para crear una copia de seguridad. Se crea como una tarea en segundo plano y luego aparece en la lista de copias de seguridad almacenadas, con su fecha, el número de personas y su tamaño. El servidor mantiene solo las copias de seguridad más recientes (cinco por defecto) y elimina automáticamente las más antiguas. También se limita el número de copias de seguridad que se pueden crear por día.

Para cada copia de seguridad almacenada, puedes:

- **Descargar** como un archivo `.tar`, por ejemplo, para mantener una copia en otro lugar.
- **Restaurar** como se describe a continuación.
- **Eliminar** después de confirmar.

Una copia de seguridad realizada con una versión más nueva de Gramps Web que la que se está ejecutando en el servidor está marcada con un icono de advertencia y no se puede restaurar.

### Restaurar desde la copia de seguridad

Restaura el árbol desde una copia de seguridad almacenada o desde un archivo subido. Para restaurar una copia de seguridad almacenada, haz clic en el botón de restaurar junto a ella. Para restaurar desde un archivo, selecciona una copia de seguridad de Gramps Web (`.tar`) o un archivo XML de Gramps (`.gramps`) y haz clic en **Restaurar**.

!!! danger
    Restaurar los datos es un reemplazo destructivo, no una fusión. Cualquier objeto existente que no esté presente en la copia de seguridad se eliminará.

Para una copia de seguridad de Gramps Web, se muestra un diálogo que indica cuándo se realizó la copia de seguridad, para qué árbol y con qué versión, y te permite elegir qué partes restaurar:

- **Datos** – los objetos del árbol genealógico
- **Configuración del árbol** – la configuración de esta página, como colores del tema, título de la aplicación y nota de la página de inicio
- **Usuarios** – los usuarios del árbol

Haz clic en **Vista previa** para ver qué cambiaría la restauración. Un archivo XML de Gramps solo contiene datos, por lo que para dicho archivo la vista previa comienza de inmediato. Se te pedirá que te autentiques nuevamente si tu sesión no es lo suficientemente reciente. La vista previa se ejecuta como una tarea en segundo plano y, una vez completada, abre un diálogo que resume los cambios por tipo de objeto (personas, familias, eventos, lugares, citas, fuentes, repositorios, objetos multimedia, notas, etiquetas), y para la configuración del árbol y los usuarios si se seleccionaron:

- **Agregar** – objetos presentes en la copia de seguridad pero faltantes en el árbol actual
- **Actualizar** – objetos presentes en ambos que difieren
- **Eliminar** – objetos en el árbol actual que están ausentes de la copia de seguridad
- **Sin cambios** – objetos idénticos en ambos

Si algún objeto se eliminaría, el diálogo advierte cuántos. Revisa el resumen y luego haz clic en **Restaurar** para aplicar los cambios, o **Cancelar** para abortar.

Después de la restauración, se enumeran los usuarios que se agregaron desde la copia de seguridad. Reciben una contraseña aleatoria, por lo que deben restablecer su contraseña antes de poder iniciar sesión. Los usuarios que ya existen en el servidor nunca se cambian. También se enumeran los objetos multimedia cuyos archivos faltan en el servidor; súbelos a través de [Importar archivo multimedia](#import-media-archive).

!!! note
    Restaurar datos solo restaura datos de objetos y referencias multimedia. Los archivos multimedia binarios en sí mismos y los metadatos del árbol (persona predeterminada, marcadores, grupos de nombres) no se ven afectados.

!!! tip
    Utiliza esto para retroceder un árbol a una copia de seguridad conocida como buena, por ejemplo, después de una mala importación o una edición masiva no deseada.

## Zona de Peligro

!!! danger
    Las acciones en la Zona de Peligro son **irreversibles**. Haz una [copia de seguridad](#backups) antes de continuar.

### Eliminar todos los objetos

Elimina objetos del árbol genealógico. Hacer clic en **Eliminar** abre un diálogo donde puedes elegir eliminar:

- **Todos los objetos** – limpia completamente el árbol
- **Tipos de objetos específicos** – por ejemplo, solo eventos o solo objetos multimedia

Se te pedirá que te autentiques nuevamente (iniciar sesión de nuevo) para confirmar la acción. La eliminación se ejecuta como una tarea en segundo plano y se muestra un indicador de progreso.

!!! warning
    Eliminar solo un subconjunto de tipos de objetos (en lugar de todos los objetos a la vez) puede llevar mucho tiempo para árboles grandes, ya que el servidor debe verificar y actualizar todas las relaciones entre objetos.

!!! tip
    Utiliza esto para empezar de nuevo antes de importar un nuevo árbol, o para eliminar tipos de objetos específicos que se importaron incorrectamente.
