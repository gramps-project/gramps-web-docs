# Trabajando con coincidencias de ADN

Las coincidencias de ADN son segmentos de ADN que coinciden entre dos individuos, identificados por la presencia de marcadores, los llamados SNPs (el acrónimo de polimorfismos de un solo nucleótido, pronunciado “snips”).

Para obtener estos datos, necesitas acceso a una prueba de ADN que esté subida a una base de datos de coincidencias que permita ver los datos de coincidencia de segmentos de ADN (por ejemplo, MyHeritage, Gedmatch, FamilytreeDNA). Gramps Web no realiza la coincidencia en sí, ya que solo tiene acceso a los datos que subes.

## Ingresando datos de coincidencias de ADN

Para ingresar datos de coincidencias de ADN, necesitas [permisos de edición](../install_setup/users.md) ya que los datos se almacenan como una nota en la base de datos de Gramps. La vista de ADN, accesible desde el menú principal, proporciona una forma conveniente de ingresar estos datos en el formato correcto.

Para ingresar una nueva coincidencia, haz clic en el botón + en la esquina inferior derecha. En el diálogo que se abre, selecciona a los dos individuos. Ten en cuenta que la “Primera persona” y la “Segunda persona” se tratan de manera diferente: la coincidencia se almacena como una asociación de la primera a la segunda persona. Solo la primera persona será seleccionable para la vista de coincidencias de ADN y el navegador de cromosomas. Típicamente, la primera persona es aquella cuya prueba de ADN tienes acceso y la segunda persona es un pariente más distante.

Si la segunda persona no está en la base de datos, necesitas crearla primero utilizando el botón “Crear persona” en la esquina superior derecha de la interfaz de usuario. Una vez que hayas creado a la persona, puedes regresar a la vista de coincidencias de ADN y seleccionar a la persona recién creada.

A continuación, pega los datos en bruto en el campo de texto. Los datos deben ser una tabla de coincidencias separada por comas o tabulaciones, que típicamente contenga el número de cromosoma, la posición de inicio y fin de la coincidencia, el número de SNPs en la coincidencia y la longitud de la coincidencia en unidades de centimorganes (cM). También puedes arrastrar y soltar un archivo con los datos de coincidencia en el campo de texto.

Un ejemplo mínimo de tal tabla es:

```csv
Cromosoma,Ubicación de inicio,Ubicación de fin,Centimorganes,SNPs
6,6358001,18115715,19.6,7424
7,150135758,154205894,10.9,2816
```

Si el formato es válido, se muestra una vista previa debajo del campo de texto como una tabla.

Finalmente, haz clic en el botón “Guardar” para almacenar la coincidencia en la base de datos.

## Visualizando datos de coincidencias de ADN

La vista de coincidencias de ADN tiene un menú desplegable que permite seleccionar a cada persona en la base de datos que tiene una coincidencia de ADN asociada. Una vez que se selecciona a una persona, los datos de coincidencias de ADN se muestran en una tabla debajo del menú desplegable. Muestra el nombre de la persona con la que está asociada la coincidencia, la relación con la persona seleccionada en el menú desplegable (determinado automáticamente desde la base de datos de Gramps), la longitud total de ADN compartido en centimorganes (cM), el número de segmentos compartidos y la longitud del más grande de estos segmentos.

Cuando haces clic en una coincidencia individual, se abre una página de detalles que muestra todos los segmentos y si la coincidencia es del lado materno o paterno. Esta información puede ser ingresada manualmente (proporcionando una `P` para paterno o `M` para materno en una columna llamada `Lado` en los datos en bruto) o determinada automáticamente por Gramps en función del ancestro común más reciente.

## Editando una coincidencia

Puedes editar una coincidencia haciendo clic en el botón de lápiz en la esquina inferior derecha en la vista de detalles de la coincidencia. Esto abre un diálogo similar al de cuando creas una nueva coincidencia, pero con los datos prellenados. Ten en cuenta que puedes cambiar los datos en bruto, pero no los individuos asociados con la coincidencia; necesitas eliminar la coincidencia y crear una nueva si deseas cambiar a los individuos.

## Trabajando con datos de coincidencias en Gramps Desktop

Los datos de coincidencias de ADN se almacenan como una nota en la base de datos de Gramps. El formato es compatible con el 
[Complemento de Mapa de Segmentos de ADN](https://gramps-project.org/wiki/index.php/Addon:DNASegmentMapGramplet)
disponible para Gramps Desktop. Su página de wiki contiene más detalles sobre cómo obtener los datos, cómo interpretarlos y cómo ingresar los datos en Gramps.

!!! info
    La API de Gramps Web v2.8.0 introdujo algunos cambios para aceptar un rango más amplio de datos de coincidencias de ADN en bruto, que aún no están disponibles en el Complemento de Gramps Desktop. El Complemento de Gramps Desktop se actualizará en el futuro para soportar los mismos formatos también.
