# Personalizar el árbol

Los propietarios y administradores del árbol pueden adaptar el nombre y la apariencia del árbol, así como su página de inicio, para todos los usuarios. Estas configuraciones se encuentran en las secciones de **Configuración del árbol** y **Personalización** de los [ajustes de administración](settings.md).

## Nombre del árbol genealógico

!!! note
    Cambiar el nombre del árbol solo funciona en una [configuración de múltiples árboles](../install_setup/multi-tree.md) o cuando `TREE_ID` está explícitamente configurado en la [configuración del servidor](../install_setup/configuration.md). En una instalación predeterminada de un solo árbol sin `TREE_ID` configurado, esto generará un error.

Esto permite cambiar el nombre de la base de datos subyacente del árbol genealógico de Gramps. Ingresa un nuevo nombre y haz clic en **Renombrar** para aplicar.

!!! tip
    Si solo deseas cambiar el nombre mostrado en la barra de la aplicación sin renombrar la base de datos, utiliza la configuración de [Título de la aplicación](#app-title) en su lugar.

## Información del investigador

Establece el nombre, la dirección y los detalles de contacto del investigador principal. Esta información se incrusta en las exportaciones (por ejemplo, archivos GEDCOM).

## Colores del tema

Establece un **color primario** y un **color de acento** personalizados para la interfaz web de Gramps. Estos colores se aplican a todos los usuarios de este árbol y entran en efecto inmediatamente después de guardar.

Utiliza los selectores de color para seleccionar colores, luego haz clic en **Guardar**. Haz clic en **Restablecer** para volver a los valores predeterminados.

## Título de la aplicación

Establece un título personalizado para la aplicación. Si se establece, esto reemplaza el nombre del árbol genealógico en la barra de título del navegador y en la barra superior de la aplicación.

Ingresa un título y haz clic en **Guardar**. Deja en blanco para usar el valor predeterminado (el nombre del árbol genealógico).

## Nota de la página de inicio

Selecciona un objeto **Nota** de Gramps para mostrar en la página de inicio del panel de control. El contenido de la nota se renderiza debajo de las columnas principales del panel de control y es visible para todos los usuarios con acceso al árbol.

Utiliza el selector de objetos para buscar y seleccionar una nota, luego guarda. Haz clic en **Eliminar** para borrar la nota actual de la página de inicio.

## Imagen de la página de inicio

Selecciona un objeto **Media** de Gramps para mostrar como una imagen en la página de inicio del panel de control. Cuando se combina con una nota de la página de inicio, la imagen aparece al lado del texto de la nota. Sin una nota, solo se muestra la imagen.

Utiliza el selector de objetos para buscar y seleccionar un objeto multimedia, luego guarda. Haz clic en **Eliminar** para borrar la imagen actual de la página de inicio.

## Configuraciones de exportación/importación

Las configuraciones a nivel de árbol (título de la aplicación, colores del tema, nota/imágen de la página de inicio, etc.) se pueden exportar como un archivo JSON para respaldo o para copiar a otra instancia de Gramps Web.

- Haz clic en **Exportar configuraciones** para descargar la configuración actual como un archivo JSON.
- Haz clic en **Importar configuraciones del árbol** para subir un archivo JSON exportado previamente y aplicar las configuraciones.
