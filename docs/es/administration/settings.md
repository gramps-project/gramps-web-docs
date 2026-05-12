# Configuración de Administración

La página **Configuración > Administración** es accesible a través del ícono de usuario en la barra superior de la aplicación. Solo está disponible para usuarios con el rol de Propietario o Administrador y proporciona herramientas para gestionar la base de datos del árbol genealógico.

## Cuotas de uso

La parte superior de la página muestra el uso actual en relación con cualquier límite configurado:

- **Personas** — el número de objetos de persona en el árbol frente al máximo configurado (∞ si es ilimitado)
- **Almacenamiento de medios** — tamaño total de los archivos de medios subidos frente a la cuota de almacenamiento configurada (∞ si es ilimitado)

Las cuotas son establecidas por el administrador del servidor; consulte [Configuración del servidor](../install_setup/configuration.md) para más detalles.

## Importar datos

La sección de importación permite subir un archivo de árbol genealógico o un archivo de medios. Consulte [Importar datos](import.md) para obtener instrucciones completas.

## Estado de los archivos de medios

Esta sección muestra:

- El número total de objetos de medios en el árbol y si alguno carece de un checksum
- El número de objetos de medios cuyo archivo asociado falta en el servidor

Una marca de verificación verde indica que todo está en orden. Si se detectan problemas, se muestran enlaces a los objetos afectados. Los checksums faltantes suelen ocurrir cuando los datos se importaron desde un formato como GEDCOM que incluye referencias a medios pero no los archivos reales. Los archivos faltantes se pueden subir a través de la función de importar archivo de medios.

## Importar archivo de medios

Permite subir un archivo ZIP de archivos de medios para completar los archivos faltantes. Consulte [Importar datos](import.md) para obtener instrucciones completas.

## Gestionar índice de búsqueda

Gramps Web mantiene un índice de búsqueda de texto completo que normalmente se actualiza automáticamente cada vez que cambian los datos. El indicador de estado muestra cuántos objetos están actualmente indexados frente al conteo total de objetos.

Haga clic en **Actualizar índice de búsqueda** para activar una reconstrucción completa. Se muestra un indicador de progreso mientras la tarea se ejecuta en segundo plano. Esto generalmente solo es necesario después de una actualización del servidor.

### Índice de búsqueda semántica

Si el servidor tiene [búsqueda semántica (potenciada por IA) habilitada](../install_setup/configuration.md), aparece una sección adicional con dos acciones:

- **Regenerar índice de búsqueda semántica** — reconstruye todo el índice semántico desde cero. Esto es computacionalmente costoso y puede tardar mucho tiempo.
- **Actualizar índice de búsqueda semántica** — realiza una actualización incremental, añadiendo solo objetos que aún no están indexados. Más rápido que una reconstrucción completa.

## Nombre del árbol genealógico

!!! note
    Cambiar el nombre del árbol solo funciona en una [configuración de múltiples árboles](../install_setup/multi-tree.md) o cuando `TREE_ID` está explícitamente configurado en la [configuración del servidor](../install_setup/configuration.md). En una instalación predeterminada de un solo árbol sin `TREE_ID` configurado, esto generará un error.

Esto permite cambiar el nombre de la base de datos del árbol genealógico de Gramps subyacente. Ingrese un nuevo nombre y haga clic en **Renombrar** para aplicar.

## Comprobar y Reparar Base de Datos

Esta herramienta verifica la base de datos de Gramps en busca de inconsistencias internas y repara las que puede — análogo a la herramienta [Comprobar y Reparar Base de Datos](https://www.gramps-project.org/wiki/index.php/Gramps_5.2_Wiki_Manual_-_Tools#Check_and_Repair_Database) en Gramps Desktop.

Haga clic en **Comprobar y Reparar** y espere a que el indicador de progreso complete. El resultado se muestra debajo del botón:

- Si no se encontraron errores, se muestra un mensaje de confirmación.
- Si se encontraron errores, se muestra un resumen de las correcciones aplicadas.

Ejecute esta herramienta si encuentra errores inesperados o comportamientos que pueden ser causados por inconsistencias en la base de datos, como relaciones faltantes entre objetos.

## Zona de Peligro

!!! danger
    Las acciones en la Zona de Peligro son **irreversibles**. Haga una copia de seguridad antes de continuar.

### Eliminar todos los objetos

Elimina objetos del árbol genealógico. Hacer clic en **Eliminar** abre un diálogo donde puede elegir eliminar:

- **Todos los objetos** — limpia completamente el árbol
- **Tipos de objetos específicos** — por ejemplo, solo eventos o solo objetos de medios

Se le pedirá que se vuelva a autenticar (iniciar sesión nuevamente) para confirmar la acción. La eliminación se ejecuta como una tarea en segundo plano y se muestra un indicador de progreso.

!!! warning
    Eliminar solo un subconjunto de tipos de objetos (en lugar de todos los objetos a la vez) puede tardar mucho tiempo para árboles grandes, ya que el servidor debe verificar y actualizar todas las relaciones entre objetos.

!!! tip
    Use esto para comenzar de nuevo antes de importar un nuevo árbol, o para eliminar tipos de objetos específicos que se importaron incorrectamente.
