# Mapa

La página del Mapa muestra todos los lugares en tu árbol familiar como marcadores interactivos en un mapa geográfico. Es accesible desde la barra lateral.

## Marcadores de lugar

Solo se muestran en el mapa los lugares que tienen coordenadas GPS almacenadas en la base de datos de Gramps. Los lugares sin coordenadas se omiten silenciosamente. Las coordenadas GPS se pueden establecer en la página de detalles del lugar (edita el lugar y completa los campos de latitud y longitud).

!!! tip
    Si muchos de tus lugares faltan en el mapa, abre una página de detalles del lugar y verifica si se han establecido la latitud y la longitud. Puedes agregar o corregir coordenadas directamente desde la vista de edición del lugar.

Cada lugar con coordenadas se muestra como un marcador. Hacer clic en un marcador abre una tarjeta de resumen que muestra el nombre del lugar y sus eventos y personas vinculados. Haz clic en el nombre del lugar en la tarjeta para abrir la página completa de detalles del lugar.

## Búsqueda

El cuadro de búsqueda en la esquina superior izquierda del mapa busca mientras escribes y agrupa los resultados bajo tres encabezados:

- **Lugares** – lugares en tu árbol familiar. Seleccionar uno centra el mapa en él y resalta su marcador.
- **Personas** – personas en tu árbol familiar. Seleccionar uno cambia el mapa a la vista de la persona descrita [a continuación](#siguiendo-a-una-persona-a-través-del-mapa).
- **Externo** – ubicaciones de [OpenStreetMap](https://www.openstreetmap.org/), para cualquier lugar del mundo. Seleccionar uno simplemente centra y hace zoom en el mapa a esa ubicación; no filtra ni cambia los lugares de tu árbol.

Los resultados externos también son útiles al agregar coordenadas a un lugar: puedes buscar la ubicación aquí para ver dónde está antes de ingresar su latitud y longitud.

## Siguiendo a una persona a través del mapa

Seleccionar una persona – desde el cuadro de búsqueda del mapa, o con el botón **Abrir en el mapa** en la página de detalles de una persona – muestra los lugares conectados a los eventos de esa persona, unidos por líneas en orden cronológico. Flechas pequeñas a lo largo de cada línea indican la dirección del viaje, para que puedas seguir la vida de una persona desde su nacimiento hasta su muerte a través del mapa.

Los lugares en una página de detalles del lugar también tienen un botón **Abrir en el mapa**, que abre el mapa centrado en ese lugar.

## Control deslizante de tiempo

El control deslizante de tiempo en la parte inferior de la página filtra qué marcadores de lugar se muestran según el año de sus eventos asociados:

- Arrastra el control para seleccionar un año.
- Solo se muestran los lugares vinculados a eventos que caen dentro de la ventana de tiempo seleccionada.
- Usa esto para rastrear dónde vivieron tus antepasados en un momento particular de la historia.

## Capas del mapa

Un botón de cambio de capa (ícono de capas apiladas, en la esquina inferior izquierda) te permite elegir entre dos mapas base:

### Mapa Base

La capa predeterminada, impulsada por [OpenFreeMap](https://openfreemap.org) (estilo Liberty para modo claro, estilo oscuro para modo oscuro). Este es un mapa moderno de propósito general adecuado para localizar lugares.

### Mapa Histórico

Cambia el mapa base a [OpenHistoricalMap](https://www.openhistoricalmap.org) (OHM), un proyecto impulsado por la comunidad que mapea el mundo tal como existió en diferentes momentos en el tiempo – piénsalo como un contraparte histórica de OpenStreetMap.

Cuando la capa del Mapa Histórico está activa, el control deslizante de tiempo también filtra los propios mosaicos del mapa: OHM renderiza el mapa tal como apareció en el año seleccionado, por lo que se muestran fronteras históricas, nombres de lugares y características en lugar de las modernas. Esto hace posible ver tanto la ubicación de tu ancestro como el contexto geográfico y político contemporáneo en una sola vista.

!!! note
    La cobertura de OpenHistoricalMap varía según la región y el período. Las áreas o épocas con contribuciones escasas pueden mostrar detalles históricos limitados. Si notas datos históricos faltantes o inexactos, considera [contribuir a OpenHistoricalMap](https://www.openhistoricalmap.org) – es un proyecto comunitario abierto que cualquiera puede editar.

## Superposiciones de mapa personalizadas

Además de las capas base integradas, puedes convertir cualquier imagen de mapa histórico escaneada – almacenada en Gramps como un objeto **Media** – en una superposición personalizada posicionada en el mapa en vivo. Esto es útil para escaneos de antiguos planos de ciudades, mapas parroquiales o mapas de propiedades que deseas comparar directamente con la geografía moderna o histórica.

### Georreferenciando una imagen

1. Abre el objeto multimedia para la imagen del mapa escaneado y cambia a modo de edición.
2. Abre la pestaña "Mapa" y haz clic en **Editar coordenadas**. Esto abre un diálogo de georreferenciación con la imagen junto a un mapa.
3. Haz clic en **Seleccionar un punto en el mapa**, luego haz clic en la ubicación del mapa a la que debería corresponder un punto en la imagen. La imagen se coloca en el mapa por primera vez tan pronto como se selecciona un punto.
4. Usa el control deslizante de **Escala** para redimensionar la imagen y el control deslizante de **Opacidad** para ver el mapa base a través de ella mientras posicionas.
5. Haz clic en **Alinear la imagen** y haz clic en el mapa nuevamente para mover la imagen de modo que el punto fijado se alinee con precisión.
6. Repite los pasos de escala, opacidad y alineación hasta que la imagen coincida con la geografía subyacente, luego guarda.

Detrás de escena, esto almacena las coordenadas de las esquinas de la imagen en un atributo `map:bounds` en el objeto multimedia.

### Visualizando superposiciones en la página del Mapa

Una vez que un objeto multimedia ha sido georreferenciado de esta manera, se vuelve automáticamente disponible como una capa conmutable en la página del Mapa. Abre el cambiador de capas (ícono de capas apiladas, en la esquina inferior izquierda) para mostrar u ocultar cada superposición independientemente del mapa base. Las superposiciones se enumeran por el título del objeto multimedia.
