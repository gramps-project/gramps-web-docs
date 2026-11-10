# Árbol Genealógico

La página del Árbol Genealógico es accesible desde la barra lateral y muestra gráficos interactivos centrados en una persona seleccionada. Hay cinco tipos de gráficos disponibles a través de pestañas en la parte superior de la página.

## Seleccionando la persona inicial

Todos los gráficos comienzan desde la persona actualmente seleccionada en el árbol (mostrada en la barra de herramientas). La persona actualmente centrada está resaltada con una sombra. Usa el botón **Persona de Inicio** para volver a tu persona de inicio, o el botón **Atrás** para regresar a la persona vista anteriormente. Hacer clic en la tarjeta de una persona en cualquier gráfico re-centra el gráfico en esa persona.

Si no se ha establecido una persona de inicio, la página ofrece un botón **Establecer Persona de Inicio** para buscar y seleccionar una directamente. Si el árbol no contiene ninguna persona aún, los usuarios con el rol de Editor o superior verán en su lugar un botón **Nueva Persona** – la primera persona creada en un árbol vacío se convierte automáticamente en tu persona de inicio, por lo que el gráfico se muestra de inmediato.

## Tipos de gráficos

### Árbol de Ancestros

Un gráfico de pedigrí que muestra los ancestros de la persona seleccionada. Los padres aparecen a la izquierda (o a la derecha, dependiendo del diseño), los abuelos más alejados, y así sucesivamente.

### Árbol de Descendientes

Muestra los descendientes de la persona seleccionada: hijos, nietos, y así sucesivamente.

### Gráfico de Reloj de Arena

Combina ancestros arriba y descendientes abajo de la persona seleccionada en una sola vista.

### Gráfico de Relaciones

Muestra el camino de relación entre dos personas. La persona seleccionada es un extremo; haz clic en cualquier otra persona en el gráfico para establecer el segundo extremo y mostrar el camino de relación más corto entre ellas.

!!! nota
    La misma persona puede aparecer más de una vez en el gráfico – por ejemplo, cuando alguien ha estado casado varias veces y aparece en varias unidades familiares a lo largo del camino. Esto es intencional, no un error.

### Gráfico de Ventilador

Un gráfico de pedigrí circular. Los ancestros irradian hacia afuera desde la persona seleccionada en el centro.

El botón **Color** en la barra de herramientas colorea los segmentos según una propiedad de cada persona: el número de eventos o notas, año de nacimiento, año de fallecimiento, edad, apellido, religión o frecuencia de ancestro (qué tan a menudo aparece una persona en el gráfico). Colorear por apellido utiliza el apellido del nombre de nacimiento de la persona, o del nombre principal si no hay nombre de nacimiento. Para eliminar el coloreado, despeja el chip que muestra el color elegido.

## Moviendo a familiares y expandiendo ramas

En el Árbol de Ancestros y el Gráfico de Ventilador, la persona seleccionada tiene un botón de chevrón que abre un menú de sus hijos. En el Árbol de Descendientes, abre un menú de sus padres en su lugar. Elegir una persona del menú centra el gráfico en ella.

En el Árbol de Ancestros, el Árbol de Descendientes y el Gráfico de Reloj de Arena, las personas en el borde del gráfico cuyas padres o hijos no se muestran tienen un chevrón en el lado donde su rama continúa. Hacer clic en él agrega una generación más a esa rama, mientras que la persona seleccionada permanece igual. De esta manera, puedes, por ejemplo, ver a todos los abuelos y luego seguir solo una línea más atrás. Las ramas expandidas se restablecen cuando seleccionas otra persona o cambias a un gráfico diferente.

## Controles de navegación

Todos los tipos de gráficos comparten una barra de herramientas con los siguientes botones:

- **Persona de Inicio** – volver a tu persona de inicio
- **Atrás** – regresar a la persona centrada anteriormente
- **Detalles de la Persona** – abrir la página de perfil completo de la persona actualmente centrada
- **Preferencias** – abrir un diálogo para ajustar las opciones de visualización específicas del gráfico (ver abajo)

Todos los gráficos soportan **pan** (clic y arrastrar) y **zoom** (rueda de desplazamiento o pellizcar).

## Preferencias del gráfico

El diálogo de **Preferencias** (icono de engranaje en la barra de herramientas) te permite ajustar las siguientes opciones, dependiendo del tipo de gráfico:

- **Máx. Generaciones de Ancestros** – cuántas generaciones de ancestros mostrar
- **Máx. Generaciones de Descendientes** – cuántas generaciones de descendientes mostrar
- **Máx. Grado de Separación** – para el Gráfico de Relaciones, la longitud máxima del camino a buscar, hasta 6
- **Máx. Número de Imágenes mostradas** – limita las fotos de perfil mostradas en el gráfico para mejorar el rendimiento
- **Formato de Visualización del Nombre** – controla cómo se muestran los nombres en las tarjetas de las personas

Haz clic en **Restablecer** para restaurar los valores predeterminados, o **Cerrar** para aplicar tus cambios.

Las configuraciones de preferencias del gráfico se almacenan en el almacenamiento local del navegador, por lo que persisten entre sesiones en el mismo dispositivo.

## Tipo de gráfico predeterminado

El tipo de gráfico mostrado cuando abres por primera vez la página del Árbol Genealógico se puede configurar en [Configuraciones del Usuario](settings.md). Tu predeterminado elegido se aplica en todos tus dispositivos.

## Editando el árbol

Los usuarios con el rol de Editor o superior pueden agregar y vincular personas directamente desde el Árbol de Ancestros. Consulta [Editando el árbol genealógico](tree-edit.md) para más detalles.
