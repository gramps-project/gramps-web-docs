# Índice de búsqueda

La sección de **Índice de búsqueda** en la [Configuración de administración](settings.md) muestra el estado del índice de búsqueda de texto completo y te permite reconstruirlo.

## Administrar índice de búsqueda

Gramps Web mantiene un índice de búsqueda de texto completo que normalmente se actualiza automáticamente cada vez que los datos cambian. El indicador de estado muestra cuántos objetos están actualmente indexados frente al conteo total de objetos.

Haz clic en **Actualizar índice de búsqueda** para iniciar una reconstrucción completa. Se muestra un indicador de progreso mientras la tarea se ejecuta en segundo plano. Esto rara vez es necesario.

Si un árbol aún no tiene índice de búsqueda, por ejemplo, después de una actualización del servidor que cambió el formato del índice, Gramps Web lo construye en segundo plano la primera vez que se abre el árbol. Mientras se está construyendo, la sección muestra "El índice de búsqueda se está construyendo." en lugar de los conteos, **Actualizar índice de búsqueda** está deshabilitado y los resultados de búsqueda pueden ser incompletos. La construcción aparece en [Notificaciones](../user-guide/notifications.md) como la tarea "Actualizar índice de búsqueda".
