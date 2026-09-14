# Historial de Revisiones

La vista del historial de revisiones muestra todas las ediciones que se han realizado en el árbol genealógico.

La vista de lista muestra las ediciones agrupadas por "transacciones". Una transacción es un grupo de una o más adiciones, eliminaciones o cambios a objetos de Gramps. Por ejemplo, agregar una nueva familia con dos personas existentes como padre y madre genera una transacción con un objeto de familia añadido y dos objetos de persona modificados (porque contienen el enlace al nuevo objeto de familia).

Hacer clic en una transacción abre la vista de detalles de la transacción. Contiene la lista de adiciones, eliminaciones y actualizaciones individuales por objeto de Gramps.

Seleccionar un cambio individual abre una vista de la representación JSON en bruto del objeto de Gramps con adiciones y eliminaciones resaltadas en verde y rojo, respectivamente. Un botón sobre la diferencia te lleva directamente a la página del propio objeto.

## Revisiones de un solo objeto

Para ver el historial de una persona, familia, evento u otro objeto en particular, abre su página y cambia a la pestaña **Revisiones**. Enumera cada cambio realizado en ese objeto, el más nuevo primero, con el tipo de cambio (agregado, actualizado o eliminado), el usuario que lo realizó y cuándo. Hacer clic en una entrada abre la transacción a la que pertenece, donde puedes inspeccionar la diferencia o deshacerla.

Haz clic en **Mostrar más** para cargar entradas más antiguas; para objetos con un historial muy largo, solo se muestran las revisiones más recientes. Para objetos que se cambiaron por última vez antes de que se registrara el historial de revisiones, la pestaña solo muestra la hora del último cambio.

!!! nota
    La pestaña Revisiones es visible para miembros y superiores y requiere la versión 3.22 o posterior de la API Web de Gramps.

## Deshaciendo una revisión

En la página de detalles de la transacción, un botón **Deshacer** te permite revertir esa transacción. Hacer clic en él verifica si el deshacer se puede realizar de manera limpia.

**Deshacer limpio** – si ninguno de los objetos afectados por la transacción ha sido modificado desde entonces, el deshacer puede proceder sin riesgo. Se muestra un cuadro de diálogo de confirmación y hacer clic en **Deshacer** revierte la transacción.

**Se requiere forzar** – si uno o más objetos afectados han sido modificados por una transacción posterior, un deshacer limpio no es posible. El cuadro de diálogo advierte que forzar el deshacer puede resultar en inconsistencias de datos, ya que los cambios posteriores que dependen de los objetos en cuestión se conservarán tal como están, aunque los objetos subyacentes estén siendo revertidos. Puedes cancelar o hacer clic en **Forzar deshacer** para proceder de todos modos.

En ambos casos, el deshacer se ejecuta como una tarea en segundo plano y se muestra un indicador de progreso.
