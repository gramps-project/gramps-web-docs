# Usa el blog integrado

El blog está destinado a presentar historias sobre tu investigación de historia familiar.

En la base de datos de Gramps, las entradas del blog se representan como fuentes con una nota adjunta, que contiene el texto del blog y, opcionalmente, archivos multimedia para las imágenes de la entrada del blog. Gramps Web trata cada fuente con una etiqueta `Blog` como un artículo de blog.

## Agregar una entrada de blog

Para agregar una entrada de blog, puedes usar Gramps Web o Gramps Desktop ([sincronizado](../administration/sync.md) con Gramps Web), los pasos son los mismos en ambos casos:

- Agrega una nueva fuente. El título de la fuente será el título de tu entrada de blog, el autor de la fuente será el autor de la entrada.
- Opcionalmente, asocia la fuente con un repositorio correspondiente a tu blog de Gramps Web.
- Agrega una nueva nota a la fuente. Escribe tu entrada de blog y copia el texto en la nota.
- Opcionalmente, agrega uno o más archivos multimedia a tu fuente. El primer archivo multimedia se tomará como la imagen de vista previa de la entrada que se muestra sobre el texto. Todos los archivos multimedia se mostrarán debajo del texto como una galería.
- Agrega la etiqueta `Blog` a la fuente (créala si no existe).

## Relación entre el blog y las fuentes

Dado que las entradas del blog son solo fuentes, todos los artículos del blog también aparecen en la lista de fuentes y se muestran como fuentes en las búsquedas. En la vista de la fuente, hay un botón "mostrar en blog" que te llevará a la vista del blog para esa entrada. La URL de la entrada del blog también contiene el ID de Gramps de la fuente correspondiente, por lo que un artículo en `yourdomain.com/blog/S0123` corresponde a la fuente en `yourdomain.com/source/S0123`.

En la parte inferior de cada entrada del blog, hay un botón "detalles" que te llevará a la vista de la fuente.
