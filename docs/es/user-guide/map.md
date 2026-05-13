# Mapa

La página del Mapa muestra todos los lugares en tu árbol genealógico como marcadores interactivos en un mapa geográfico. Es accesible desde la barra lateral.

## Marcadores de lugar

Solo se muestran en el mapa los lugares que tienen coordenadas GPS almacenadas en la base de datos de Gramps. Los lugares sin coordenadas se omiten silenciosamente. Las coordenadas GPS se pueden establecer en la página de detalles del lugar (edita el lugar y completa los campos de latitud y longitud).

!!! tip
    Si muchos de tus lugares faltan en el mapa, abre la página de detalles de un lugar y verifica si la latitud y la longitud están establecidas. Puedes agregar o corregir coordenadas directamente desde la vista de edición del lugar.

Cada lugar con coordenadas se muestra como un marcador. Hacer clic en un marcador abre una tarjeta de resumen que muestra el nombre del lugar y sus eventos y personas vinculados. Haz clic en el nombre del lugar en la tarjeta para abrir la página completa de detalles del lugar.

## Búsqueda

El cuadro de búsqueda en la esquina superior izquierda del mapa te permite saltar a cualquier ubicación en el mundo por nombre. Esto no filtra los lugares del árbol; simplemente desplaza y hace zoom en el mapa a la ubicación buscada.

## Control deslizante de tiempo

El control deslizante de tiempo en la parte inferior de la página filtra qué marcadores de lugar se muestran según el año de sus eventos asociados:

- Arrastra el control para seleccionar un año.
- Solo se muestran los lugares vinculados a eventos que caen dentro de la ventana de tiempo seleccionada.
- Utiliza esto para rastrear dónde vivieron tus antepasados en un momento particular de la historia.

## Capas del mapa

Un botón de cambio de capa (icono de capas apiladas, en la parte inferior izquierda) te permite elegir entre dos mapas base:

### Mapa Base

La capa predeterminada, impulsada por [OpenFreeMap](https://openfreemap.org) (estilo Liberty para modo claro, estilo oscuro para modo oscuro). Este es un mapa moderno de propósito general adecuado para localizar lugares.

### Mapa Histórico

Cambia el mapa base a [OpenHistoricalMap](https://www.openhistoricalmap.org) (OHM), un proyecto impulsado por la comunidad que mapea el mundo tal como existía en diferentes momentos en el tiempo; piénsalo como un contraparte histórica de OpenStreetMap.

Cuando la capa del Mapa Histórico está activa, el control deslizante de tiempo también filtra los propios mosaicos del mapa: OHM renderiza el mapa tal como aparecía en el año seleccionado, por lo que se muestran fronteras históricas, nombres de lugares y características en lugar de las modernas. Esto hace posible ver tanto la ubicación de tu ancestro como el contexto geográfico y político contemporáneo en una sola vista.

!!! note
    La cobertura de OpenHistoricalMap varía según la región y el período. Las áreas o épocas con contribuciones escasas pueden mostrar detalles históricos limitados. Si notas datos históricos faltantes o inexactos, considera [contribuir a OpenHistoricalMap](https://www.openhistoricalmap.org) – es un proyecto comunitario abierto que cualquiera puede editar.
