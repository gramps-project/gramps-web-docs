# Uso de Gramps Web para el Análisis de Y-DNA

!!! note "Nota"
    Esta función requiere Gramps Web API versión 3.3.0 o posterior y Gramps Web frontend versión 25.9.0 o posterior.

La vista de Y-DNA en Gramps Web puede utilizar datos crudos de polimorfismos de un solo nucleótido (SNP) del cromosoma Y para determinar el haplogrupo Y-DNA más probable de una persona y mostrar los ancestros derivados en el árbol del cromosoma Y humano junto con estimaciones de tiempo.

## Cómo obtener y almacenar los datos SNP de Y-DNA

Para obtener los datos SNP de Y-DNA, necesitas realizar una prueba de Y-DNA a través de un servicio de pruebas genéticas. El resultado se representa como un conjunto de mutaciones (SNPs), cada una identificada por una cadena (por ejemplo, `R-BY44535`) y un signo `+` o `-` que indica si la mutación está presente o ausente. Gramps Web espera la cadena de todos los SNPs probados en el formato `SNP1+, SNP2-, SNP3+,...` para ser almacenada en un atributo de persona de tipo personalizado `Y-DNA` (sensible a mayúsculas). Puedes crear manualmente este atributo en Gramps Web o Gramps Desktop, o navegar a la vista de Y-DNA en Gramps Web y hacer clic en el botón azul "Agregar", seleccionar la persona a la que deseas añadir los datos y pegar la cadena de SNP. En cualquier caso, los datos se almacenarán como un atributo de persona en tu base de datos de Gramps.

[Consulta a continuación](#instrucciones-para-obtener-datos-snp-de-servicios-de-pruebas) para obtener instrucciones sobre cómo obtener los datos SNP de varios servicios de pruebas.

## Cómo funciona

Una vez que una persona tiene un atributo `Y-DNA` que contiene los datos SNP, Gramps Web utilizará la biblioteca Python de código abierto [yclade](https://github.com/DavidMStraub/yclade) para determinar la posición más probable de la persona en el árbol del cromosoma Y humano. El árbol ha sido creado por el proyecto [YFull](https://www.yfull.com/) basado en decenas de miles de pruebas de Y-DNA. Ten en cuenta que Gramps Web utiliza una copia local del árbol de YFull, por lo que no se envían datos a ningún tercero.

El árbol se recorre desde la raíz hasta las hojas, y en cada nodo, los SNPs asociados con ese nodo se comparan con los SNPs positivos y negativos probados de la persona, y se sigue la rama apropiada.

El resultado final es una sucesión de clados desde la raíz del árbol (el [“Adán” cromosómico Y](https://es.wikipedia.org/wiki/Ad%C3%A1n_cromos%C3%B3mico_Y)) hasta el clado más derivado que es consistente con los datos SNP de la persona. Cada clado tiene una edad estimada basada en las edades de las muestras en la base de datos de YFull que pertenecen a ese clado.

Dado que los cromosomas Y se heredan de padre a hijo, esta sucesión corresponde a un extracto de la ascendencia patrilineal de la persona.

## Cómo interpretar los resultados

La pieza de información más importante es el haplogrupo más probable de la persona, mostrado en la parte superior de la página. El nombre está vinculado a la página correspondiente en el sitio web de [YFull](https://www.yfull.com/), que contiene más información, como el país de origen de las muestras probadas pertenecientes a ese haplogrupo.

En el árbol de ancestros patrilineales mostrado en Gramps Web, la caja directamente encima de la persona probada es el ancestro común más reciente (MRCA) de todas las muestras probadas pertenecientes al haplogrupo de la persona. La fecha mostrada para este ancestro es su fecha de nacimiento aproximada estimada. El ancestro encima de él es el ancestro donde la mutación que define este haplogrupo apareció por primera vez.

Debido a la lenta tasa de mutación de los cromosomas Y, el MRCA puede estar muchos cientos de años en el pasado. Para haplogrupos raros (es decir, haplogrupos donde pocas personas han sido probadas hasta ahora), puede incluso ser miles de años.


## Instrucciones para obtener datos SNP de servicios de pruebas

### [YSEQ](https://www.yseq.net/)

Una vez que hayas iniciado sesión en "Mi Cuenta", ve a "Mis Resultados / Ver mis Alelos" y navega hasta la parte inferior de la página. El campo de texto "Lista de alelos compacta" se ha añadido específicamente para Gramps Web y está en el formato exacto para pegar en el atributo `Y-DNA`.
