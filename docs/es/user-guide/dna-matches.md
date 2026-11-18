# Trabajando con coincidencias de ADN

Las coincidencias de ADN son segmentos de ADN que coinciden entre dos individuos, identificados por la presencia de marcadores, los llamados SNPs (el acrónimo de polimorfismos de un solo nucleótido, pronunciado “snips”).

Para obtener estos datos, necesitas acceso a una prueba de ADN que esté subida a una base de datos de coincidencias que permita ver los datos de coincidencias de segmentos de ADN (por ejemplo, MyHeritage, Gedmatch, FamilytreeDNA). Gramps Web no realiza la coincidencia en sí, ya que solo tiene acceso a los datos que subes.

## Ingresando datos de coincidencias de ADN

Para ingresar datos de coincidencias de ADN, necesitas [permisos de edición](../install_setup/users.md) ya que los datos se almacenan como una nota en la base de datos de Gramps. La vista de ADN, accesible desde el menú principal, proporciona una forma conveniente de ingresar estos datos en el formato correcto.

Para ingresar una nueva coincidencia, haz clic en el botón + en la esquina inferior derecha. En el diálogo que se abre, selecciona a los dos individuos. Ten en cuenta que la “Primera persona” y la “Segunda persona” se tratan de manera diferente: la coincidencia se almacena como una asociación de la primera a la segunda persona. Solo la primera persona será seleccionable para la vista de coincidencias de ADN y el navegador de cromosomas. Típicamente, la primera persona es aquella cuya prueba de ADN tienes acceso y la segunda persona es un pariente más distante.

Si la segunda persona no está en la base de datos, necesitas crearla primero utilizando el botón “Crear persona” en la esquina superior derecha de la interfaz de usuario. Una vez que hayas creado a la persona, puedes volver a la vista de coincidencias de ADN y seleccionar a la persona recién creada.

A continuación, pega los datos en bruto en el campo de texto. Los datos deben ser una tabla de coincidencias separada por comas o tabulaciones, que típicamente contenga el número de cromosoma, la posición de inicio y fin de la coincidencia, el número de SNPs en la coincidencia y la longitud de la coincidencia en unidades de centimorganes (cM). También puedes arrastrar y soltar un archivo con los datos de coincidencias en el campo de texto.

Un ejemplo mínimo de tal tabla es:

```csv
Cromosoma,Ubicación de inicio,Ubicación de fin,Centimorganes,SNPs
6,6358001,18115715,19.6,7424
7,150135758,154205894,10.9,2816
```

Si el formato es válido, se muestra una vista previa debajo del campo de texto como una tabla.

Finalmente, haz clic en el botón “Guardar” para almacenar la coincidencia en la base de datos.

## Visualizando datos de coincidencias de ADN

La vista de coincidencias de ADN tiene un menú desplegable que permite seleccionar a cada persona en la base de datos que tiene una coincidencia de ADN asociada. Una vez que se selecciona a una persona, sus coincidencias se enumeran en una tabla: el nombre de la coincidencia, su relación con la persona seleccionada, la longitud total de ADN compartido en centimorganes (cM), el número de segmentos compartidos y la longitud del más grande de estos segmentos.

Para las coincidencias que ya están colocadas en el árbol, la columna de relación muestra la relación registrada en el árbol (determinada automáticamente a partir de la base de datos de Gramps). Para las coincidencias que no están relacionadas con la persona seleccionada en el árbol, muestra la relación estimada a partir del ADN compartido, marcada con "≈".

Hacer clic en una coincidencia abre su página, con un resumen del ADN compartido, la [estimación de relación](#relationship-estimate), un gráfico de la relación en el árbol y la lista de segmentos. Cada segmento muestra si está en el lado paterno o materno. El lado puede ser ingresado manualmente (proporcionando una `P` para paterno o `M` para materno en una columna llamada `Lado` en los datos en bruto) o determinado automáticamente a partir del ancestro común más reciente. El botón de descarga junto a los segmentos los guarda como un archivo CSV en el formato que acepta el diálogo de coincidencias.

## Estimación de relación

El ADN compartido no es prueba de una relación específica: la cantidad de ADN que comparten dos parientes varía mucho, y diferentes relaciones se superponen. Por lo tanto, Gramps Web muestra un rango de relaciones posibles con sus probabilidades, calculadas a partir del número y las longitudes de los segmentos compartidos (requiere Gramps Web API 3.26 o más reciente).

Las relaciones se agrupan por su *grado*:

- **Padre o hijo** y **Hermano completo** se muestran por separado.
- **Pariente de grado 2** incluye medios hermanos, abuelos y nietos, y tías, tíos, sobrinas y sobrinos.
- **Pariente de grado 3** incluye primos hermanos, bisabuelos, tías y tíos abuelos, y medios tíos y tías.
- Cada grado adicional está aproximadamente a una generación más de distancia, por ejemplo, primos hermanos una vez removidos son grado 4 y primos segundos son grado 5. El grado 9 y más allá se agrupan como "9+".

Las relaciones con el mismo grado comparten aproximadamente la misma cantidad de ADN en promedio, por lo que el ADN por sí solo no puede diferenciarlas. Usa las edades de las personas para decidir entre ellas: un pariente de grado 2 de 30 años de edad de un individuo de 60 años es más probable que sea un sobrino que un abuelo.

La estimación es más confiable para parientes cercanos. Para relaciones distantes, las coincidencias comparten solo unos pocos segmentos, y las probabilidades se distribuyen en varios grados.

### Verificando el árbol contra el ADN

Si la coincidencia está colocada en el árbol, Gramps Web verifica si el ADN compartido se ajusta a la relación registrada allí. Si el ADN es muy poco probable para esa relación, se muestra un ícono de advertencia en la tabla de coincidencias y una advertencia en la página de coincidencia. El número entre paréntesis, por ejemplo, "1 : 500", compara cuán probable es el ADN para la relación registrada con cuán probable es para la relación más probable.

Una advertencia es una razón para mirar más de cerca, no prueba de un error. Las causas comunes son:

- un error en el árbol, como un padre equivocado,
- una paternidad mal atribuida, por ejemplo, una adopción desconocida o un padre biológico diferente,
- datos de coincidencias incompletos, por ejemplo, si solo se copiaron segmentos por encima de un umbral alto del servicio de pruebas,
- relaciones a través de más de una línea, por ejemplo, personas relacionadas a través de su madre y padre ("colapso de pedigrí"), que comparten más ADN de lo esperado.

Las relaciones que no son por nacimiento, como a través de una adopción, no se verifican.

## Editando una coincidencia

Para editar una coincidencia, abre su página y haz clic en el botón de editar, o presiona `e`. Ten en cuenta que puedes cambiar los datos en bruto, pero no los individuos asociados con la coincidencia; necesitas eliminar la coincidencia y crear una nueva si deseas cambiar a los individuos.

## Coincidencias privadas

Los diálogos para agregar y editar una coincidencia tienen un interruptor de **Privado**. Una coincidencia privada, incluidos sus segmentos, está oculta para los usuarios que no pueden ver registros privados. Las coincidencias privadas están marcadas con un candado para todos los demás. Consulta [Registros privados](privacy.md) para más información sobre la privacidad.

## Trabajando con datos de coincidencias en Gramps Desktop

Los datos de coincidencias de ADN se almacenan como una nota en la base de datos de Gramps. El formato es compatible con el 
[Complemento de Mapa de Segmentos de ADN](https://gramps-project.org/wiki/index.php/Addon:DNASegmentMapGramplet)
disponible para Gramps Desktop. Su página de wiki contiene más detalles sobre cómo obtener los datos, cómo interpretarlos y cómo ingresar los datos en Gramps.

!!! info
    La API de Gramps Web v2.8.0 introdujo algunos cambios para aceptar una gama más amplia de datos de coincidencias de ADN en bruto, que aún no están disponibles en el Complemento de Gramps Desktop. El Complemento de Gramps Desktop se actualizará en el futuro para admitir los mismos formatos también.
