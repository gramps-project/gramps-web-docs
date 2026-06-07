# Notificaciones

**Notificaciones** es un elemento de la barra lateral con un ícono de campana. Cuando ocurren errores o se están ejecutando tareas en segundo plano, una insignia muestra el número de notificaciones no leídas. Haz clic en ella para abrir el registro de notificaciones.

El registro de notificaciones tiene dos propósitos:

- Es un registro de errores que ocurrieron durante tu sesión: solicitudes de API fallidas, errores de tareas en segundo plano, fallos de guardado o errores a nivel de navegador.
- Realiza un seguimiento del progreso de tareas en segundo plano de larga duración, como importaciones y exportaciones, generación de informes, reconocimiento de texto OCR, actualizaciones de base de datos y reconstrucciones de índices de búsqueda/semánticos, mostrando su estado (por ejemplo, pendiente, iniciado, en progreso) y notificándote cuando se completan o fallan.

Cada entrada muestra un mensaje corto, la fuente (Red, Tarea, Guardar o Navegador) y una marca de tiempo.

Algunas notificaciones incluyen detalles estructurados. Hacer clic en tal entrada abre un diálogo con un desglose de los datos del error y un botón de **Copiar JSON**. Esto es útil al informar un error, ya que el JSON contiene la información exacta del error del servidor.

Usa **Borrar Todo** para descartar todas las notificaciones.

!!! nota
    Las notificaciones se almacenan en memoria solamente y se eliminan cuando recargas la página.
