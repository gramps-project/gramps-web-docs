# Listas

Cada tipo de objeto en Gramps Web tiene una vista de lista: Personas, Familias, Eventos, Lugares, Fuentes, Citas, Repositorios, Notas y Medios. Todos funcionan de la misma manera y comparten las mismas herramientas para ordenar, filtrar y editar en masa.

## Ordenar y paginar

Haz clic en el encabezado de una columna para ordenar por esa columna; haz clic nuevamente para invertir el orden. El ordenamiento se realiza en el servidor, por lo que se aplica a toda la lista, no solo a la página que estás viendo.

Las listas largas se dividen en páginas. Usa los controles de paginación en la parte inferior para moverte entre ellas.

En pantallas estrechas, la tabla cambia automáticamente a un diseño compacto, por lo que las vistas de lista siguen siendo utilizables en un teléfono.

## Elegir columnas

Haz clic en el ícono de engranaje sobre la lista para abrir el diálogo de **Columnas**. Marca o desmarca una columna para mostrarla u ocultarla. **Restablecer** restaura la selección predeterminada para esa lista.

Al menos una columna debe permanecer visible, por lo que la última columna restante no puede ser desmarcada.

Tu selección de columnas se recuerda por tipo de objeto y por árbol genealógico. Se almacena en tu navegador, por lo que no es visible para otros usuarios, pero tampoco te sigue a otro navegador o dispositivo.

## Filtrar

Haz clic en el botón de **filtro** para abrir el panel de filtro. Ofrece tres formas de filtrar, que se pueden combinar:

- **Filtros predefinidos** en secciones colapsables que dependen del tipo de objeto. Para personas, por ejemplo, puedes filtrar por año de nacimiento, año de fallecimiento, varias propiedades de la persona, el número de asociaciones, etiquetas y si un objeto es privado o público.
- **Filtro avanzado**: un generador de condiciones para filtros que los predefinidos no pueden expresar, descrito [a continuación](#filtro-avanzado).
- **GQL**: un campo de texto para una consulta en el [Gramps Query Language](gql.md). Escribe la consulta y presiona Enter o haz clic en **Aplicar**. Si la consulta es inválida, el marco del campo se vuelve rojo. Una consulta se aplica además de los otros filtros.

Los filtros activos se muestran como chips sobre la lista. Elimina un solo filtro haciendo clic en el botón de borrar del chip, o usa **Eliminar todos los filtros** para eliminarlos todos de una vez.

### Filtro avanzado

Haz clic en **Filtro avanzado** en la parte inferior del panel de filtro para abrir el generador de condiciones. Sus condiciones son las reglas de filtro conocidas de Gramps Desktop, como "Personas con el &lt;nombre&gt;" o "Antepasados de &lt;persona&gt;".

- Haz clic en **Agregar condición** para elegir una regla. Las reglas están agrupadas en categorías y se pueden buscar por nombre o descripción.
- Completa los parámetros de la regla. Cada parámetro tiene una entrada correspondiente, por ejemplo, un campo de fecha, un selector de etiquetas o un selector de objetos para una persona o lugar.
- Elige cómo se combinan las condiciones de un grupo: **Todas las condiciones**, **Cualquier condición**, o – a través del menú junto a ellas – **Exactamente una condición**.
- Haz clic en **Agregar grupo** para añadir un grupo de condiciones dentro de otro grupo, con su propia forma de combinarlas.
- Selecciona **No** en una condición o grupo para invertirlo.

Haz clic en **Aplicar** para filtrar la lista.

Los filtros predefinidos que están activos cuando abres el generador aparecen allí como condiciones. Si el filtro que construyes se puede expresar con los filtros predefinidos, se muestra con ellos después de aplicar. De lo contrario, se muestra como un solo chip de **Filtro avanzado**, y el panel de filtro ofrece un botón de **Editar** para reabrir el generador.

!!! nota
    Las reglas que se refieren a filtros personalizados guardados en Gramps Desktop no están disponibles en el generador. Las reglas se muestran en tu idioma con Gramps Web API 3.24 o posterior.

## Seleccionar objetos y actuar sobre ellos en masa

Los usuarios con permisos de edición ven un botón de **Seleccionar** junto al botón de filtro. Haz clic en él para entrar en modo de selección, lo que añade una casilla de verificación a cada fila.

Marca los objetos que desees, y aparece una barra de herramientas que muestra cuántos están seleccionados, junto con un menú desplegable de **Acción** y un botón de **Aplicar**.

### Eliminar

Selecciona uno o más objetos, elige **Eliminar** y haz clic en **Aplicar**. Un cuadro de confirmación te pide que confirmes, advirtiendo que la acción no se puede deshacer.

!!! consejo
    Las eliminaciones se registran en el [historial de revisiones](revisions.md) como cualquier otro cambio, por lo que una eliminación masiva errónea se puede revertir deshaciendo la transacción correspondiente.

### Fusionar

Selecciona **exactamente dos** objetos, elige **Fusionar** y haz clic en **Aplicar**. Un cuadro de diálogo pregunta cuál de los dos debe proporcionar los datos primarios para el objeto fusionado; haz clic en el que deseas mantener como primario. Los datos del otro objeto se fusionan en él y las referencias se actualizan.

La fusión está disponible para personas, familias, eventos, lugares, fuentes y citas. No está disponible para repositorios, notas y objetos multimedia.

Si eliges una acción sin una selección válida – por ejemplo, una fusión con solo un objeto seleccionado – un cuadro de diálogo explica lo que se requiere.
