# Búsqueda

La página de búsqueda es accesible haciendo clic en el ícono de la lupa en la barra superior de la aplicación, o presionando la tecla `s` [atajo de teclado](shortcuts.md).

## Búsqueda de texto completo

Escribe cualquier consulta en el campo de búsqueda y presiona Enter (o haz clic en el botón de búsqueda). Gramps Web busca en todos los tipos de objetos: personas, familias, eventos, lugares, fuentes, citas, repositorios, notas y medios, y devuelve resultados coincidentes clasificados por relevancia.

Los resultados muestran el tipo de objeto, el nombre y un breve resumen. Haz clic en cualquier resultado para abrir la página de detalles correspondiente.

## Sintaxis de búsqueda

- **Todas las palabras deben coincidir.** `Müller Berlin` encuentra objetos que contienen ambas palabras.
- **`or`** encuentra objetos que contienen cualquiera de las palabras, por ejemplo, `Meyer or Maier`. `and` también se puede escribir entre palabras, pero no hace ninguna diferencia.
- `or` se aplica a las palabras directamente adyacentes: `Meyer or Maier Berlin` significa "(Meyer or Maier) y Berlin". No se admiten paréntesis.
- **Comillas** coinciden con una frase, es decir, palabras en este orden: `"Johann Georg"`.
- **Carácter comodín:** un `*` al final coincide con cualquier final, por ejemplo, `Mey*` coincide con "Meyer", "Meyers", "Meyerhofer", etc. Esto también funciona para frases: `"Johann Georg"*`.
- `or` y `and` son reconocidos en cualquier caso. Para buscar una de estas palabras en sí misma, colócala entre comillas.
- No se pueden excluir palabras; no hay "no".

## Lo que encuentra la búsqueda

- Los acentos no necesitan coincidir: "Müller" también encuentra "Muller", y "muller" encuentra "Müller".
- Las familias y eventos también se encuentran por los nombres de sus personas, por ejemplo, "Müller" encuentra las familias y eventos de todos los que se llaman Müller. Estos resultados se clasifican por debajo de las coincidencias directas.
- Los tipos estándar se encuentran por sus nombres en el idioma de tu interfaz, por ejemplo, "Taufe" encuentra bautismos en la interfaz en alemán.
- Los guiones bajos separan palabras, por lo que "microfilm" encuentra un archivo de medios llamado `scanned_microfilm.png`.
- Los usuarios que no pueden ver registros privados no encuentran objetos a través de información privada, como una familia a través del nombre de un miembro privado.

## Filtrado por tipo de objeto

Debajo del campo de búsqueda, los botones de alternancia para cada tipo de objeto (Personas, Familias, Eventos, Lugares, …) te permiten restringir los resultados a uno o más tipos específicos. Por defecto, se buscan todos los tipos. Activar uno o más botones restringe los resultados solo a esos tipos.
