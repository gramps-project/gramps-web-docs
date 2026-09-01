# Listas

Cada tipo de objeto en Gramps Web tiene una vista de lista: Personas, Familias, Eventos, Lugares, Fuentes, Citas, Repositorios, Notas y Medios. Todos funcionan de la misma manera y comparten las mismas herramientas para ordenar, filtrar y editar en masa.

## Ordenar y paginar

Haz clic en el encabezado de una columna para ordenar por esa columna; haz clic nuevamente para invertir el orden. El ordenamiento se realiza en el servidor, por lo que se aplica a toda la lista, no solo a la página que estás viendo.

Las listas largas se dividen en páginas. Usa los controles de paginación en la parte inferior para moverte entre ellas.

En pantallas estrechas, la tabla cambia automáticamente a un diseño compacto, por lo que las vistas de lista siguen siendo utilizables en un teléfono.

## Elegir columnas

Haz clic en el ícono de engranaje sobre la lista para abrir el diálogo de **Columnas**. Marca o desmarca una columna para mostrarla u ocultarla. **Restablecer** restaura la selección predeterminada para esa lista.

Al menos una columna debe permanecer visible, por lo que la última columna restante no se puede desmarcar.

Tu selección de columnas se recuerda por tipo de objeto y por árbol genealógico. Se almacena en tu navegador, por lo que no es visible para otros usuarios, pero tampoco te sigue a otro navegador o dispositivo.

## Filtrar

Haz clic en el botón de **filtrar** para abrir el panel de filtros. Un interruptor de píldora en la parte superior del panel cambia entre dos modos:

- **simple** – un conjunto de filtros predefinidos que dependen del tipo de objeto. Para personas, por ejemplo, puedes filtrar por año de nacimiento, año de fallecimiento, varias propiedades de la persona, el número de asociaciones, etiquetas y si un objeto es privado o público.
- **GQL** – un único campo de texto para una consulta avanzada en el [Lenguaje de Consulta de Gramps](gql.md). Escribe la consulta y presiona Enter o haz clic en **Aplicar**. Si la consulta es inválida, el marco del campo se vuelve rojo.

Los filtros activos se muestran como chips sobre la lista. Elimina un solo filtro haciendo clic en el botón de borrar del chip, o usa **Limpiar todos los filtros** para eliminarlos todos a la vez.

!!! nota
    Los dos modos son alternativos, no aditivos: una consulta GQL reemplaza los filtros simples, y volver al modo simple elimina la consulta.

## Seleccionar objetos y actuar sobre ellos en masa

Los usuarios con permisos de edición ven un botón de **Seleccionar** junto al botón de filtro. Haz clic en él para entrar en modo de selección, lo que añade una casilla de verificación a cada fila.

Marca los objetos que deseas, y aparece una barra de herramientas que muestra cuántos están seleccionados, junto con un menú desplegable de **Acción** y un botón de **Aplicar**.

### Eliminar

Selecciona uno o más objetos, elige **Eliminar** y haz clic en **Aplicar**. Un cuadro de confirmación te pide que confirmes, advirtiendo que la acción no se puede deshacer.

!!! consejo
    Las eliminaciones se registran en el [historial de revisiones](revisions.md) como cualquier otro cambio, por lo que una eliminación masiva errónea puede revertirse deshaciendo la transacción correspondiente.

### Fusionar

Selecciona **exactamente dos** objetos, elige **Fusionar** y haz clic en **Aplicar**. Un cuadro de diálogo pregunta cuál de los dos debe proporcionar los datos primarios para el objeto fusionado; haz clic en el que deseas mantener como primario. Los datos del otro objeto se fusionan en él y las referencias se actualizan.

La fusión está disponible para personas, familias, eventos, lugares, fuentes y citas. No está disponible para repositorios, notas y objetos multimedia.

Si eliges una acción sin una selección válida, por ejemplo, una fusión con solo un objeto seleccionado, un cuadro de diálogo explica lo que se requiere.
