# Notificaciones

**Notificaciones** es un elemento de la barra lateral con un ícono de campana. Cuando han ocurrido errores o se están ejecutando tareas en segundo plano, un distintivo muestra el número de notificaciones no leídas. Haz clic en él para abrir el registro de notificaciones.

El registro de notificaciones tiene dos propósitos:

- Es un registro de errores que ocurrieron durante tu sesión: solicitudes de API fallidas, errores de tareas en segundo plano, fallos de guardado o errores a nivel de navegador.
- Realiza un seguimiento del progreso de tareas en segundo plano de larga duración, como importaciones y exportaciones, generación de informes, reconocimiento de texto OCR, actualizaciones de base de datos, eliminación de muchos objetos y reconstrucciones de índice de búsqueda, mostrando su estado (por ejemplo, pendiente, iniciado, en progreso) y notificándote cuando se completan o fallan.

Cada entrada muestra un mensaje corto, la fuente (Red, Tarea, Guardar o Navegador) y una marca de tiempo. Las tareas finalizadas indican "Tarea completada" o "Tarea fallida".

Algunas notificaciones incluyen detalles estructurados, como el mensaje de error de una tarea fallida. Hacer clic en tal entrada abre un diálogo con un desglose de los datos de error y un botón de **Copiar JSON**. Esto es útil al reportar un error, ya que el JSON contiene la información exacta del error del servidor.

Utiliza **Borrar todo** para descartar todas las notificaciones.

Las tareas que cambian todo el árbol, como una importación, una restauración, la eliminación de todos los objetos o la reconstrucción del índice de búsqueda, no pueden ejecutarse al mismo tiempo. Si inicias una mientras otra está en ejecución, un mensaje indica que otra tarea ya se está ejecutando en este árbol, y la tarea en ejecución se muestra con su progreso.

!!! nota
    Las notificaciones se almacenan en memoria únicamente y se borran cuando recargas la página.
