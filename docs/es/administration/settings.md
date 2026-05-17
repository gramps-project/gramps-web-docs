# Configuración de Administración

La página de **Configuración > Administración** es accesible a través del ícono de usuario en la barra superior de la aplicación. Solo está disponible para usuarios con el rol de Propietario o Administrador y proporciona herramientas para gestionar la base de datos del árbol genealógico.

La página está organizada en secciones colapsables. Haz clic en el encabezado de una sección para expandirla.

## Datos

Cubre cuotas de uso, importación de datos y gestión de archivos multimedia.

### Cuotas de uso

La parte superior de la sección muestra el uso actual en relación con cualquier límite configurado:

- **Personas** – el número de objetos persona en el árbol frente al máximo configurado (∞ si es ilimitado)
- **Almacenamiento multimedia** – tamaño total de los archivos multimedia subidos frente a la cuota de almacenamiento configurada (∞ si es ilimitado)

Las cuotas son establecidas por el administrador del servidor; consulta [Configuración del servidor](../install_setup/configuration.md) para más detalles.

### Importar datos

La sección de importación te permite subir un archivo de árbol genealógico o un archivo de medios. Consulta [Importar datos](import.md) para obtener instrucciones completas.

### Estado de archivos multimedia

Esta sección muestra:

- El número total de objetos multimedia en el árbol y si alguno carece de un checksum
- El número de objetos multimedia cuyo archivo asociado falta en el servidor

Una marca de verificación verde indica que todo está en orden. Si se detectan problemas, se muestran enlaces a los objetos afectados. Los checksums faltantes suelen ocurrir cuando los datos se importaron desde un formato como GEDCOM que incluye referencias multimedia pero no los archivos reales. Los archivos faltantes se pueden subir a través de la función de importar archivo multimedia.

### Importar archivo multimedia

Permite subir un archivo ZIP de archivos multimedia para completar los archivos faltantes. Consulta [Importar datos](import.md) para obtener instrucciones completas.

## Índice de búsqueda

### Gestionar índice de búsqueda

Gramps Web mantiene un índice de búsqueda de texto completo que normalmente se actualiza automáticamente cada vez que los datos cambian. El indicador de estado muestra cuántos objetos están actualmente indexados frente al recuento total de objetos.

Haz clic en **Actualizar índice de búsqueda** para activar una reconstrucción completa. Se muestra un indicador de progreso mientras la tarea se ejecuta en segundo plano. Esto generalmente solo es necesario después de una actualización del servidor.

### Índice de búsqueda semántica

Si el servidor tiene [búsqueda semántica (potenciada por IA) habilitada](../install_setup/configuration.md), aparece una sección adicional con dos acciones:

- **Regenerar índice de búsqueda semántica** – reconstruye todo el índice semántico desde cero. Esto es computacionalmente costoso y puede tardar mucho tiempo.
- **Actualizar índice de búsqueda semántica** – realiza una actualización incremental, añadiendo solo objetos que aún no están indexados. Más rápido que una reconstrucción completa.

## Configuración del árbol

### Nombre del árbol genealógico

!!! note
    Cambiar el nombre del árbol solo funciona en una [configuración de múltiples árboles](../install_setup/multi-tree.md) o cuando `TREE_ID` está explícitamente configurado en la [configuración del servidor](../install_setup/configuration.md). En una instalación predeterminada de un solo árbol sin `TREE_ID` configurado, esto generará un error.

Esto permite cambiar el nombre de la base de datos del árbol genealógico de Gramps subyacente. Ingresa un nuevo nombre y haz clic en **Renombrar** para aplicar.

!!! tip
    Si solo deseas cambiar el nombre mostrado en la barra de la aplicación sin renombrar la base de datos, utiliza la configuración de [Título de la aplicación](#app-title) en su lugar.

### Información del investigador

Establece el nombre, la dirección y los detalles de contacto del investigador principal. Esta información se incrusta en las exportaciones (por ejemplo, archivos GEDCOM).

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

Esta herramienta verifica la base de datos de Gramps en busca de inconsistencias internas y corrige las que puede – análogo a la herramienta [Comprobar y reparar base de datos](https://www.gramps-project.org/wiki/index.php/Gramps_5.2_Wiki_Manual_-_Tools#Check_and_Repair_Database) en Gramps Desktop.

Haz clic en **Comprobar y reparar** y espera a que el indicador de progreso se complete. El resultado se muestra debajo del botón:

- Si no se encontraron errores, se muestra un mensaje de confirmación.
- Si se encontraron errores, se muestra un resumen de las correcciones aplicadas.

Ejecuta esta herramienta si encuentras errores inesperados o comportamientos que pueden ser causados por inconsistencias en la base de datos, como relaciones faltantes entre objetos.

## Zona de peligro

!!! danger
    Las acciones en la Zona de peligro son **irreversibles**. Haz una copia de seguridad antes de proceder.

### Eliminar todos los objetos

Elimina objetos del árbol genealógico. Hacer clic en **Eliminar** abre un diálogo donde puedes elegir eliminar:

- **Todos los objetos** – limpia completamente el árbol
- **Tipos de objetos específicos** – por ejemplo, solo eventos o solo objetos multimedia

Se te pedirá que te autentiques nuevamente para confirmar la acción. La eliminación se ejecuta como una tarea en segundo plano y se muestra un indicador de progreso.

!!! warning
    Eliminar solo un subconjunto de tipos de objetos (en lugar de todos los objetos a la vez) puede tardar mucho tiempo para árboles grandes, ya que el servidor debe verificar y actualizar todas las relaciones entre objetos.

!!! tip
    Utiliza esto para comenzar de nuevo antes de importar un nuevo árbol, o para eliminar tipos de objetos específicos que se importaron incorrectamente.
