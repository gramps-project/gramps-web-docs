# Filtrar usando el Lenguaje de Consulta de Objetos de Gramps

Las [vistas de lista de objetos](lists.md) (personas, familias, eventos, ...) y la [lista de tareas](tasks.md) tienen un campo de filtro para expresiones en el [Lenguaje de Consulta de Objetos de Gramps](https://github.com/DavidMStraub/gramps-object-query-language) (GOQL).

Para usarlo, abre el panel de filtro, escribe una expresión en el campo **GOQL** y presiona Enter (o haz clic en **Aplicar**). La lista se filtra según la expresión, además de cualquier otro filtro activo. Si la expresión es inválida, el campo se marca como un error.

La expresión siempre se aplica a los objetos de la lista en la que te encuentras: en la lista de Personas, `surname == 'Smith'` encuentra a las personas con el apellido Smith.

!!! nota
    El campo GOQL necesita la API Web de Gramps 3.24 o superior.

## Sintaxis

Una expresión GOQL se parece a una condición en el lenguaje de programación Python. No necesitas conocer Python para usarlo; los ejemplos a continuación cubren la mayoría de las necesidades.

### Comparaciones

Una comparación tiene la forma `campo operador valor`, por ejemplo `surname == 'Smith'`.

Operador | Significado
---------|--------
`==` | es igual a
`!=` | no es igual a
`<`, `<=` | es menor que, menor o igual a (anterior, más pequeño)
`>`, `>=` | es mayor que, mayor o igual a (posterior, más grande)
`in [ ... ]` | es uno de los valores listados, p. ej. `surname in ['Meyer', 'Maier']`
`not in [ ... ]` | no es ninguno de los valores listados
`'texto' in campo` | el campo contiene el texto, p. ej. `'mill' in surname`
`is None` | el campo está vacío o no existe, p. ej. `death.date.sortval is None`

El texto va entre comillas simples o dobles (`'Smith'`), los números no (`1850`). Las comparaciones se pueden encadenar, p. ej. `Date('1850') <= birth.date.sortval < Date('1900')`.

### Combinando condiciones

Las condiciones se pueden combinar con `and` y `or`, e invertir con `not`. `and` tiene prioridad sobre `or`; usa paréntesis para agrupar condiciones:

```python
(gender == Person.MALE and surname == 'Smith') or given_name == 'Mary'
```

### Patrones de texto

- `like(field, 'pattern')` coincide con un patrón en el que `%` representa cualquier texto y `_` para un solo carácter, p. ej. `like(given_name, 'J%')` para todos los nombres de pila que comienzan con "J".
- `regex(field, 'pattern')` coincide con una [expresión regular](https://es.wikipedia.org/wiki/Expresi%C3%B3n_regular), p. ej. `regex(surname, '^M[ae][iy]er$')`.

`like` y `'texto' in campo` ignoran mayúsculas y minúsculas (en SQLite, esto solo se aplica a las letras A–Z sin acentos). `regex` es sensible a mayúsculas.

### Campos

Un campo es el nombre de una propiedad del objeto, como `gender` o `gramps_id`, o una ruta a una propiedad anidada, como `primary_name.first_name` o `primary_name.surname_list[0].surname`. Los corchetes cuadrados seleccionan un elemento de una lista por su posición, comenzando desde 0. Las propiedades disponibles son las del [modelo de datos de Gramps](https://gramps-project.org/wiki/index.php/Gramps_Data_Model). Si un campo no existe, el mensaje de error lista los campos que sí existen.

Hay algunos atajos disponibles:

- Las personas tienen `given_name` y `surname`, el nombre y apellido del nombre principal.
- Las personas tienen `birth` y `death`, sus eventos de nacimiento y muerte, p. ej. `birth.date.sortval` o `death.place.name.value`.
- Las familias tienen `father` y `mother`, p. ej. `father.surname == 'Smith'`.
- Los eventos tienen `place`, las citas tienen `source`, y los lugares tienen `enclosed_by`, el lugar que los rodea.

Estos se pueden encadenar, p. ej. `father.birth.place.name.value` en la lista de Familias. También se pueden comparar dos campos entre sí, p. ej. `father.surname == mother.surname`.

### Listas de objetos relacionados

`any(collection, condition)` coincide si al menos un elemento de una colección cumple con la condición, y `len(collection)` cuenta los elementos. Sin una condición, `any(collection)` coincide si la colección no está vacía. Las colecciones son:

- en casi todos los objetos: `notes`, `citations`, `media`, y `tags`
- en personas: `events`, `families` (como pareja), `parent_families` (como hijo), y `associations`
- en familias: `children`
- en todos los objetos: `backlinks`, los objetos que se refieren a él, que se pueden probar por su tipo con `_class`, p. ej. `any(backlinks, _class == 'Person')`

`any` y `len` también funcionan para listas almacenadas en el propio objeto, como `alternate_names` o `primary_name.surname_list`.

### Constantes y tipos

Los valores fijos de Gramps están disponibles como constantes, como `Person.MALE`, `Person.FEMALE`, `Person.UNKNOWN`, o los niveles de confianza `Citation.CONF_VERY_LOW` a `Citation.CONF_VERY_HIGH`. Los tipos se comparan por su `value` con constantes como `EventType.BIRTH`, `FamilyRelType.MARRIED`, `NameType.BIRTH`, `PlaceType.VILLAGE`, o `RepositoryType.ARCHIVE`:

```python
type.value == EventType.BAPTISM
```

Los tipos personalizados que has ingresado tú mismo no tienen una constante propia.

### Fechas

`Date('...')` convierte una fecha escrita como texto en un valor que se puede comparar con el `sortval` de una fecha, p. ej. `birth.date.sortval < Date('1800')`.

El `sortval` es un único punto en el tiempo e ignora el tipo y la calidad de una fecha: "antes de 1800", "alrededor de 1800" y "1800" tienen el mismo `sortval`, y para un rango o intervalo es el inicio. Para tener en cuenta estos aspectos, compara el `modifier` o `quality` de la fecha con constantes como `Date.MOD_ABOUT`, `Date.MOD_BEFORE`, `Date.MOD_AFTER`, `Date.MOD_RANGE`, `Date.MOD_SPAN`, o `Date.QUAL_ESTIMATED`:

```python
date.modifier == Date.MOD_ABOUT
```

## Ejemplos comentados

Lista de personas:

```python
gender == Person.FEMALE and like(given_name, 'Mar%')
```

Mujeres cuyo nombre comienza con "Mar".

```python
Date('1850') <= birth.date.sortval < Date('1900')
```

Personas nacidas entre 1850 y 1899.

```python
birth.place.name.value == death.place.name.value
```

Personas que nacieron y murieron en un lugar con el mismo nombre.

```python
not any(notes)
```

Personas sin notas.

```python
any(events, type.value == EventType.BURIAL)
```

Personas con un evento de entierro.

```python
any(alternate_names, surname_list[0].surname == 'Meyer')
```

Personas con un nombre alternativo con el apellido Meyer.

Lista de familias:

```python
len(children) > 10
```

Familias con más de 10 hijos.

```python
len(children, gender == Person.FEMALE) == 3
```

Familias con tres hijas.

```python
mother.death.date.sortval < father.death.date.sortval
```

Familias en las que la madre murió antes que el padre.

Lista de eventos:

```python
type.value == EventType.BAPTISM and place.name.value == 'Berlin'
```

Bautismos en un lugar llamado Berlín.

Lista de citas:

```python
confidence >= Citation.CONF_HIGH
```

Citas con una confianza alta o muy alta.

Lista de notas:

```python
'David' in text.string and private == True
```

Notas privadas que contienen "David".

```python
not any(backlinks)
```

Notas que no están adjuntas a ningún objeto.

## Referencia completa

Para la referencia completa del lenguaje, consulta la [documentación de GOQL](https://github.com/DavidMStraub/gramps-object-query-language/blob/main/docs/where_expr.md).
