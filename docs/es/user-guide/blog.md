# Usa el blog integrado

El blog está destinado a presentar historias sobre tu investigación de historia familiar.

En la base de datos de Gramps, las publicaciones del blog se representan como fuentes con una nota adjunta, que contiene el texto del blog y, opcionalmente, archivos multimedia para las imágenes de la publicación del blog. Gramps Web trata cada fuente con una etiqueta `Blog` como un artículo de blog.

## Agregar una publicación de blog

La forma más rápida de escribir una publicación es el formulario dedicado **Nueva Publicación de Blog** en Gramps Web. Ábrelo desde el botón azul **+** en la página del Blog, o desde el menú **Agregar** (icono de más) en la barra de aplicaciones superior eligiendo **Publicación de Blog**.

El formulario tiene campos para:

- **Título** – el título de la publicación (requerido)
- **Autor** – quién lo escribió
- **Contenido** – un editor de texto enriquecido para la publicación en sí
- **Medios** – uno o más objetos multimedia. El primero se convierte en la imagen de vista previa que se muestra encima del texto; todos ellos aparecen como una galería debajo.
- **Etiquetas** y un interruptor **privado**, como para cualquier otro objeto

Guardar el formulario crea la fuente subyacente, la nota y la etiqueta `Blog` para ti, como se describe [a continuación](#relación-entre-el-blog-y-las-fuentes).

### Agregar una publicación manualmente

También puedes crear una publicación construyendo los objetos subyacentes tú mismo. Esta es la única forma de hacerlo en Gramps Desktop ([sincronizado](../administration/sync.md) con Gramps Web), y los pasos son los mismos en ambas aplicaciones:

- Agrega una nueva fuente. El título de la fuente será el título de tu publicación de blog, el autor de la fuente será el autor de la publicación.
- Opcionalmente, asocia la fuente con un repositorio correspondiente a tu blog de Gramps Web.
- Agrega una nueva nota a la fuente. Escribe tu publicación de blog y copia el texto en la nota.
- Opcionalmente, agrega uno o más archivos multimedia a tu fuente. El primer archivo multimedia se tomará como la imagen de vista previa de la publicación que se muestra encima del texto. Todos los archivos multimedia se mostrarán debajo del texto como una galería.
- Agrega la etiqueta `Blog` a la fuente (créala si no existe).

## Relación entre el blog y las fuentes

Dado que las publicaciones del blog son solo fuentes, todos los artículos del blog también aparecen en la lista de fuentes y se muestran como fuentes en las búsquedas. En la vista de la fuente, hay un botón "mostrar en blog" que te llevará a la vista del blog para esa publicación. La URL de la publicación del blog también contiene el ID de Gramps de la fuente correspondiente, por lo que un artículo en `tudominio.com/blog/S0123` corresponde a la fuente en `tudominio.com/source/S0123`.

En la parte inferior de cada publicación del blog, hay un botón "detalles" que te llevará a la vista de la fuente.
