# Notificaciones

La campana en la barra superior de la aplicación abre las notificaciones. Un distintivo en la campana muestra el número de notificaciones no leídas. El menú lista las tareas en ejecución y las últimas notificaciones; **Mostrar todo** abre el registro completo de notificaciones. En pantallas pequeñas, la campana abre el registro directamente.

Las notificaciones son sobre:

- **Cambios por otros usuarios.** Cuando otros usuarios cambian el árbol mientras usas Gramps Web, una notificación indica quién cambió qué, por ejemplo, "Editar Persona" o "12 cambios". Haz clic en ella para abrir el cambio en el [historial de revisiones](revisions.md). Los cambios que no tienen un usuario de Gramps Web, como los cambios realizados directamente en una base de datos compartida con Gramps Desktop, se muestran sin un nombre. Esto solo está disponible para usuarios que pueden ver el historial de revisiones (miembros y superiores).
- **Tareas en segundo plano** – como importaciones y exportaciones, generación de informes, reconocimiento de texto OCR, actualizaciones de base de datos, eliminación o edición de muchos objetos, y reconstrucciones del índice de búsqueda – mostrando su estado (por ejemplo, pendiente, iniciado, en progreso) y notificándote cuando se completan o fallan.
- **Errores** que ocurrieron durante tu sesión – solicitudes de API fallidas, errores de tareas en segundo plano, fallos de guardado o errores a nivel de navegador.

Las exportaciones finalizadas y los archivos multimedia se pueden descargar desde su notificación, incluso después de haber salido de la [página de Exportación](../administration/export.md).

Algunas notificaciones incluyen detalles estructurados, como el mensaje de error de una tarea fallida. Hacer clic en tal entrada en el registro de notificaciones abre un diálogo con un desglose de los datos de error y un botón de **Copiar JSON**. Esto es útil al informar un error, ya que el JSON contiene la información exacta del error del servidor.

Usa **Borrar Todo** en el registro de notificaciones para descartar todas las notificaciones.

Las tareas que cambian todo el árbol, como una importación, una restauración, la eliminación de todos los objetos o la reconstrucción del índice de búsqueda, no pueden ejecutarse al mismo tiempo. Si inicias una mientras otra está en ejecución, un mensaje indica que otra tarea ya está en ejecución en este árbol, y la tarea en ejecución se muestra con su progreso.

!!! nota
    Las notificaciones se almacenan solo en memoria y se borran cuando recargas la página. Gramps Web verifica los cambios por otros usuarios solo mientras está abierto, por lo que los cambios realizados mientras estabas ausente no se reportan; consulta el [Historial de revisiones](revisions.md) para esos.
