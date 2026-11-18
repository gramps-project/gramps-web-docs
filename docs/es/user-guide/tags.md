# Etiquetas

Las etiquetas son etiquetas que se pueden aplicar a cualquier objeto en la base de datos de Gramps: personas, familias, eventos, lugares, fuentes, citas, repositorios, notas y medios. Son útiles para agrupar y filtrar objetos. Las etiquetas se almacenan en la base de datos del árbol genealógico de Gramps y se comparten entre todos los usuarios; también son completamente compatibles con las etiquetas creadas en Gramps Desktop.

## Gestión de etiquetas

Las etiquetas se gestionan desde la sección **Etiquetas** de [Configuración de Administración](../administration/settings.md#tags), que solo está disponible para usuarios con el rol de Propietario o Administrador. Muestra todas las etiquetas existentes y te permite:

- **Crear** una nueva etiqueta utilizando el botón **Nueva Etiqueta**
- **Renombrar** una etiqueta utilizando el ícono de editar (lápiz)
- **Cambiar el color** de una etiqueta utilizando el selector de color
- **Eliminar** una etiqueta utilizando el ícono de eliminar

!!! nota
    Eliminar una etiqueta la quita de todos los objetos a los que se aplicó.

## Aplicando etiquetas a objetos

Las etiquetas se pueden aplicar o eliminar de un objeto en su página de detalles cuando está en modo de edición. Para etiquetar muchos objetos a la vez, selecciónalos en una lista y utiliza la acción **Agregar Etiqueta** o **Eliminar Etiqueta**, consulta [Listas](lists.md#tags-and-privacy).

Las etiquetas se muestran en la columna **Etiquetas** de las listas, y en los resultados de búsqueda, marcadores e historial. Si una lista no muestra la columna, actívala en el selector de columnas.

## Filtrando por etiqueta

Todas las [páginas de lista de objetos](lists.md) (Personas, Familias, Eventos, Lugares, Fuentes, Citas, Repositorios, Notas, Medios) incluyen un filtro de etiquetas. Úsalo para mostrar solo los objetos que tienen una etiqueta específica aplicada.

## Etiquetas especiales

Dos etiquetas tienen un significado especial en Gramps Web:

- **`Blog`** – cualquier fuente etiquetada como `Blog` se trata como una entrada de blog y aparece en la vista de [Blog](blog.md)
- **`ToDo`** – cualquier nota etiquetada como `ToDo` se trata como una tarea de investigación y aparece en la vista de [Tareas](tasks.md)

Estas etiquetas se crean automáticamente cuando usas por primera vez las funciones de Blog o Tareas. Renombrarlas o eliminarlas romperá la función correspondiente.
