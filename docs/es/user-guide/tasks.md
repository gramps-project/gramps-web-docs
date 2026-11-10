# Utilizar la gestión de tareas integrada

Gramps Web contiene una herramienta de gestión de tareas genealógicas integrada. Está destinada a permitir a los investigadores planificar y priorizar, pero también documentar sus tareas. Por esta razón, las tareas se representan como fuentes en la base de datos de Gramps. Después de completar una tarea, el contenido asociado puede servir como una fuente que documenta el proceso de investigación.

## Conceptos básicos de las tareas

Las tareas tienen las siguientes propiedades:

- Estado. Esto puede ser "Abierto", "En Progreso", "Bloqueado" o "Hecho"
- Prioridad. Esto puede ser "Baja", "Media" o "Alta"
- Etiquetas. Las etiquetas son etiquetas normales de Gramps de la fuente subyacente. (Tenga en cuenta que todas las tareas tienen además la etiqueta `ToDo` para identificarlas como tareas, pero esta etiqueta está oculta en la lista de tareas para evitar desorden.)
- Título. Se muestra en la lista de tareas
- Descripción. Un campo de texto enriquecido que se puede utilizar para describir el enunciado del problema, pero también documentar cualquier progreso realizado
- Medios. Cualquier archivo multimedia adjunto a la tarea

## Crear una tarea

Dado que las tareas son objetos normales de Gramps, pueden ser editadas o creadas por el mismo grupo de usuarios que puede editar o crear otros objetos (como personas o eventos).

Para crear una tarea, haga clic en el botón + en la página de la lista de tareas. Ingrese al menos un título y, opcionalmente, una prioridad, una descripción, archivos adjuntos y etiquetas. El estado siempre será "Abierto" al crear.

## La lista de tareas

La lista de tareas está ordenada por estado – las tareas hechas al final – y dentro de cada estado por prioridad, de mayor a menor.

Haga clic en una tarea para abrirla. Los usuarios con permisos de edición también pueden hacer clic en el ícono de estado de una tarea para cambiar su estado directamente en la lista, por ejemplo, para marcarla como hecha.

El botón **filtro** sobre la lista filtra las tareas por etiqueta, con una expresión [GOQL](goql.md), o con el [filtro avanzado](lists.md#advanced-filter).

## Editar una tarea

La página de la tarea no tiene un "modo de edición" separado como otros objetos de Gramps:

- Haga clic en el título para editarlo. Presione Enter, haga clic en ✓, o haga clic en otro lugar para guardar; presione Escape o haga clic en ✕ para cancelar.
- Los cambios en el estado y la prioridad se aplican de inmediato.
- Para editar la descripción o los archivos adjuntos, haga clic en el botón de editar junto al encabezado de la sección. La descripción se guarda con el botón "guardar" debajo de ella; la edición de archivos adjuntos termina con **Hecho**.
- El botón de bloqueo establece si la tarea es privada. La descripción de la tarea obtiene la misma privacidad.

Los usuarios sin permisos de edición ven el estado y la prioridad como texto, y las secciones sin contenido están ocultas.

Debajo del título, los editores ven dos botones más: **Editar Fuente** abre la fuente que representa la tarea, donde se pueden editar sus otras notas, citas y atributos. **Eliminar** elimina la tarea después de una confirmación y regresa a la lista de tareas; el mensaje que aparece tiene un botón de deshacer para restaurar la tarea.

## Cambio masivo de propiedades de tareas

Los usuarios con permisos de edición ven una casilla de verificación en cada fila de la lista de tareas. Seleccione tareas y use **Establecer Prioridad** o **Establecer Estado** sobre la lista para cambiar todas las tareas seleccionadas a la vez.

## Tareas en Gramps Desktop

Al agregar tareas a través de Gramps Web, tanto las fuentes como las notas tendrán la etiqueta `ToDo` adjunta a ellas, por lo que las tareas aparecerán en el [Gramplet de Notas por Hacer](https://gramps-project.org/wiki/index.php/Addon:ToDoNotesGramplet) de escritorio, así como en el [Informe de Tareas por Hacer](https://gramps-project.org/wiki/index.php/Addon:ToDoReport).

Para agregar o editar una tarea en Gramps Desktop, use las siguientes pautas:

- Agregue una fuente con la etiqueta `ToDo` y el título de la tarea como título
- Opcionalmente, agregue una nota a la fuente con la etiqueta `ToDo`, tipo "Por Hacer", y la descripción como texto
- Agregue un atributo "Estado" y configúrelo como "Abierto", "En Progreso", "Bloqueado" o "Hecho"
- Agregue un atributo "Prioridad" y configúrelo en 9 para baja, 5 para media o 1 para alta (estos valores contraintuitivos se toman de la especificación iCalendar)
