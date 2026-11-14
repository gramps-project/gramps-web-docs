# Copia de seguridad y restauración

Los propietarios del árbol pueden crear, descargar y restaurar copias de seguridad del árbol en la sección de **Copias de seguridad** de la [Configuración de administración](settings.md).

Una copia de seguridad contiene los datos del árbol genealógico, incluidos los registros privados, la configuración del árbol y los usuarios del árbol. Los archivos multimedia no están incluidos; consulte [Hacer copia de seguridad de sus archivos multimedia](export.md#back-up-your-media-files).

## Copias de seguridad almacenadas

Si el administrador del servidor ha configurado un directorio de copias de seguridad (`BACKUP_DIR`, consulte [Configuración del servidor](../install_setup/configuration.md)), las copias de seguridad se pueden almacenar en el servidor. De lo contrario, la sección muestra un aviso de que el almacenamiento de copias de seguridad no está configurado, y solo se puede restaurar desde un archivo subido.

Haga clic en **Hacer copia de seguridad...** para crear una copia de seguridad. Se crea como una tarea en segundo plano y luego aparece en la lista de copias de seguridad almacenadas, con su fecha, el número de personas y su tamaño. El servidor mantiene solo las copias de seguridad más recientes (cinco por defecto) y elimina automáticamente las más antiguas. También hay un límite en el número de copias de seguridad que se pueden crear por día.

Para cada copia de seguridad almacenada, puede:

- **Descargar**la como un archivo `.tar`, por ejemplo, para mantener una copia en otro lugar.
- **Restaurarla**, como se describe a continuación.
- **Eliminarla**, después de confirmar.

Una copia de seguridad hecha con una versión más nueva de Gramps Web que la que se ejecuta en el servidor está marcada con un ícono de advertencia y no se puede restaurar.

## Restaurar desde la copia de seguridad

Restaura el árbol desde una copia de seguridad almacenada o desde un archivo subido. Para restaurar una copia de seguridad almacenada, haga clic en el botón de restauración junto a ella. Para restaurar desde un archivo, seleccione una copia de seguridad de Gramps Web (`.tar`) o un archivo XML de Gramps (`.gramps`) y haga clic en **Restaurar**.

!!! danger
    Restaurar los datos es un reemplazo destructivo, no una fusión. Cualquier objeto existente que no esté presente en la copia de seguridad se eliminará.

Para una copia de seguridad de Gramps Web, se muestra un diálogo que indica cuándo se hizo la copia de seguridad, para qué árbol y con qué versión, y le permite elegir qué partes restaurar:

- **Datos** – los objetos del árbol genealógico
- **Configuración del árbol** – la configuración de la página de administración, como colores del tema, título de la aplicación y nota de la página de inicio
- **Usuarios** – los usuarios del árbol

Haga clic en **Vista previa** para ver qué cambiaría la restauración. Un archivo XML de Gramps solo contiene datos, por lo que para tal archivo la vista previa comienza de inmediato. Se le pedirá que se vuelva a autenticar si su sesión no es lo suficientemente reciente. La vista previa se ejecuta como una tarea en segundo plano y, una vez completada, abre un diálogo que resume los cambios por tipo de objeto (personas, familias, eventos, lugares, citas, fuentes, repositorios, objetos multimedia, notas, etiquetas), y para la configuración del árbol y los usuarios si se seleccionaron:

- **Agregar** – objetos presentes en la copia de seguridad pero que faltan en el árbol actual
- **Actualizar** – objetos presentes en ambos que difieren
- **Eliminar** – objetos en el árbol actual que están ausentes en la copia de seguridad
- **Sin cambios** – objetos idénticos en ambos

Si se eliminaran objetos, el diálogo advierte cuántos. Revise el resumen y luego haga clic en **Restaurar** para aplicar los cambios, o **Cancelar** para abortar.

Después de la restauración, se enumeran los usuarios que se añadieron desde la copia de seguridad. Obtienen una contraseña aleatoria, por lo que deben restablecer su contraseña antes de poder iniciar sesión. Los usuarios que ya existen en el servidor nunca se modifican. Los objetos multimedia cuyos archivos faltan en el servidor también se enumeran; cárguelos a través de [Importar archivos multimedia](import-media.md).

!!! note
    Restaurar datos solo restaura datos de objetos y referencias multimedia. Los archivos multimedia binarios en sí y los metadatos del árbol (persona predeterminada, marcadores, grupos de nombres) no se ven afectados.

!!! tip
    Use esto para retroceder un árbol a una copia de seguridad conocida y buena, por ejemplo, después de una mala importación o una edición masiva no deseada.

## Gramps XML como copia de seguridad

Si no está disponible el almacenamiento de copias de seguridad, o si solo desea mantener una copia de los datos del árbol genealógico, [exporte](export.md) el árbol como XML de Gramps. Tal archivo se puede restaurar a través de [Restaurar desde la copia de seguridad](#restore-from-backup) también.

Tenga en cuenta que si su usuario de Gramps Web no tiene permiso para ver registros privados, la exportación no será una copia de seguridad completa, ya que no contendrá ningún registro privado.
