# Notificaciones

**Notificaciones** es un elemento de la barra lateral con un ícono de campana. Cuando ocurren errores o se están ejecutando tareas en segundo plano, una insignia muestra el número de notificaciones no leídas. Haz clic en ella para abrir el registro de notificaciones.

El registro de notificaciones tiene dos propósitos:

- Es un registro de errores que ocurrieron durante tu sesión: solicitudes de API fallidas, errores de tareas en segundo plano, fallos de guardado o errores a nivel de navegador.
- Realiza un seguimiento del progreso de tareas en segundo plano de larga duración, como importaciones y exportaciones, generación de informes, reconocimiento de texto OCR, actualizaciones de bases de datos y reconstrucciones de índices de búsqueda/semánticos, mostrando su estado (por ejemplo, pendiente, iniciado, en progreso) y notificándote cuando se completan o fallan.

Cada entrada muestra un mensaje corto, la fuente (Red, Tarea, Guardar o Navegador) y una marca de tiempo. Las tareas finalizadas indican "Tarea completada" o "Tarea fallida".

Algunas notificaciones incluyen detalles estructurados, como el mensaje de error de una tarea fallida. Hacer clic en tal entrada abre un diálogo con un desglose de los datos de error y un botón de **Copiar JSON**. Esto es útil al informar un error, ya que el JSON contiene la información exacta del error del servidor.

Utiliza **Limpiar todo** para descartar todas las notificaciones.

Las tareas que cambian todo el árbol, como una importación, una restauración, la eliminación de todos los objetos o la reconstrucción del índice de búsqueda, no pueden ejecutarse al mismo tiempo. Si inicias una mientras otra se está ejecutando, un mensaje indica que otra tarea ya se está ejecutando en este árbol, y la tarea en ejecución se muestra con su progreso.

!!! nota
    Las notificaciones se almacenan solo en memoria y se borran cuando recargas la página.
