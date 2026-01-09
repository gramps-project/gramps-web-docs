# Utilizar la gestión de tareas integrada

Gramps Web contiene una herramienta de gestión de tareas genealógicas integrada. Está diseñada para permitir a los investigadores planificar y priorizar, pero también documentar sus tareas. Por esta razón, las tareas se representan como fuentes en la base de datos de Gramps. Después de completar una tarea, el contenido asociado puede servir como una fuente que documenta el proceso de investigación.

## Conceptos básicos de las tareas

Las tareas tienen las siguientes propiedades:

- Estado. Puede ser "Abierto", "En Progreso", "Bloqueado" o "Hecho"
- Prioridad. Puede ser "Baja", "Media" o "Alta"
- Etiquetas. Las etiquetas son etiquetas normales de Gramps de la fuente subyacente. (Tenga en cuenta que todas las tareas además tienen la etiqueta `ToDo` para identificarlas como tareas, pero esta etiqueta está oculta en la lista de tareas para evitar desorden.)
- Título. Se muestra en la lista de tareas
- Descripción. Un campo de texto enriquecido que se puede utilizar para describir el enunciado del problema, pero también documentar cualquier progreso realizado
- Medios. Cualquier archivo de medios adjunto a la tarea

## Crear una tarea

Dado que las tareas son objetos normales de Gramps, pueden ser editadas o creadas por el mismo grupo de usuarios que puede editar o crear otros objetos (como personas o eventos).

Para crear una tarea, haga clic en el botón + en la página de la lista de tareas. Ingrese al menos un título. El estado siempre será "Abierto" al crear.

## Editar una tarea

Para editar cualquier detalle de la tarea, haga clic en ella en la lista de tareas.

La página de detalles de la tarea no tiene un "modo de edición" separado como otros objetos de Gramps. Los cambios en el título, estado y prioridad se aplican inmediatamente. Los cambios en la descripción de texto enriquecido requieren hacer clic en el botón "guardar" debajo de ella.

## Cambio masivo de propiedades de tareas

La prioridad y el estado de las tareas se pueden cambiar en masa utilizando las casillas de verificación en la lista de tareas para la selección y los botones apropiados sobre la lista de tareas.

## Tareas en Gramps Desktop

Al agregar tareas a través de Gramps Web, tanto las fuentes como las notas tendrán la etiqueta `ToDo` adjunta, por lo que las tareas aparecerán en el [Gramplet de Notas por Hacer](https://gramps-project.org/wiki/index.php/Addon:ToDoNotesGramplet) de escritorio, así como en el [Informe de Tareas por Hacer](https://gramps-project.org/wiki/index.php/Addon:ToDoReport).

Para agregar o editar una tarea en Gramps Desktop, utilice las siguientes pautas

- Agregue una fuente con la etiqueta `ToDo` y el título de la tarea como título
- Opcionalmente, agregue una nota a la fuente con la etiqueta `ToDo`, tipo "Por Hacer", y la descripción como texto
- Agregue un atributo "Estado" y configúrelo como "Abierto", "En Progreso", "Bloqueado" o "Hecho"
- Agregue un atributo "Prioridad" y configúrelo en 9 para baja, 5 para media o 1 para alta (estos valores contraintuitivos se toman de la especificación de iCalendar)
