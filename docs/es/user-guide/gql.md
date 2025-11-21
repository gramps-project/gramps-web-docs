# Filtrar usando el Lenguaje de Consulta de Gramps

Las vistas de listas de objetos (personas, familias, eventos, ...) tienen un modo de filtro avanzado opcional basado en el [Lenguaje de Consulta de Gramps](https://github.com/DavidMStraub/gramps-ql) (GQL).

Para usarlo, escribe una consulta en sintaxis GQL y presiona enter (o haz clic en el botón "aplicar"). La vista se filtrará según la consulta. Si la consulta es inválida, el marco del campo de entrada se vuelve rojo.

La sintaxis de GQL se describe a continuación, copiada de la documentación de GQL.

## Sintaxis

Una consulta GQL es una cadena compuesta de declaraciones de la forma `propiedad operador valor`, combinadas opcionalmente con las palabras clave `and` y `or`, así como paréntesis.

### Propiedades

#### `class`

Filtra por la clase de objeto de Gramps y puede ser uno de `person`, `family`, `event`, `place`, `citation`, `source`, `repository`, `media`, o `note`.

#### Propiedades de objeto

GQL admite la consulta de propiedades anidadas de los objetos de Gramps, por ejemplo, `primary_name.date.calendar`. Consulta a continuación para obtener una lista completa de propiedades – consulta también el [Modelo de Datos de Gramps](https://gramps-project.org/wiki/index.php/Gramps_Data_Model).

#### Elementos de lista por índice

Los elementos individuales en propiedades similares a listas se pueden acceder por índice posicional en corchetes. Esto se puede combinar con propiedades anidadas, por ejemplo, `primary_name.surname_list[0].surname`.

#### `length`

Esta es una propiedad especial que devuelve la longitud de una propiedad de Gramps similar a un arreglo, por ejemplo, `media_list.length > 0` para obtener objetos con referencias de medios.

#### `all`, `any`

Dos propiedades especiales más para propiedades de Gramps similares a arreglos. `all` requiere que una condición se aplique a todos los elementos de la lista, `any` requiere que se aplique a al menos un elemento. Ambas propiedades se pueden combinar con otras propiedades antes y después. Ejemplos: `media_list.any.citation_list.length > 0` para devolver objetos con referencias de medios que tienen citas; `media_list.all.citation_list.length = 0` para devolver objetos donde todos los objetos de medios no tienen citas.

#### Índice de arreglo

Se puede usar un índice numérico de arreglo para acceder a elementos específicos de una lista, por ejemplo, `child_ref_list[0]` para el primer hijo.

#### `get_person`, etc.

Mientras que todas las propiedades anteriores se refieren a un solo objeto de Gramps, también es posible filtrar en diferentes objetos referidos por el objeto inicial. Por ejemplo, un evento tiene un manejador de lugar en su propiedad `place`. Usando la pseudo-propiedad `get_place`, GQL cambia a las propiedades de ese objeto. Por ejemplo, es posible buscar `class = event and place.get_place.name.value ~ York`. Esto también se puede combinar con `any` o `all`, por ejemplo, `class = person and event_ref_list.any.ref.get_event.description ~ farmer`.

### Operadores

#### `=`, `!=`

Igualdad o desigualdad. Ejemplos: `class = person`, `class != family`

#### `>`, `>=`, `<`, `<=`

Comparación. Funciona para cadenas así como para números. Ejemplos: `confidence <= 1`, `change > 1712477760`, `gramps_id > "I2015"`

#### `~`, `!~`

Contiene o no contiene. Funciona para listas así como para cadenas. Ejemplos: `gramps_id !~ F00`, `author ~ David`, `family_list ~ "3a16680f7d226e3ac3eefc8b57a"`

#### Sin operador/valor

Si no se proporciona un operador y un valor, el valor se interpreta como un booleano (verdadero o falso). Esto funciona para
todos los tipos de propiedades y se aplican las reglas de Python para convertir a verdadero/falso. Por ejemplo, la consulta `private` devuelve objetos privados; `confidence` devuelve objetos donde la confianza es mayor que 0; `media_list` devuelve objetos con al menos una referencia de medios.

### Valores

Los valores pueden ser números o cadenas. Si los números deben interpretarse como cadenas o si se involucran caracteres especiales como =, encierra el valor entre comillas. Ejemplos: `gramps_id = F0001`, pero `gramps_id = "0001"`.

## Ejemplos comentados

```sql
class = note and private and text.string ~ David
```

Todas las notas privadas que contienen la cadena "David" en su texto

```sql
media_list.length >= 10
```

Todos los objetos (de cualquier clase) con 10 o más referencias de medios

```sql
class != person and media_list.any.rect
```

Todos los objetos que *no* son una persona pero tienen una referencia de medios que es parte de una imagen. Aquí, `media_list.any.rect` significa que para cada uno de los elementos en la lista de medios, se verifica si la propiedad `rect` (rectángulo) tiene un valor verdadero, lo que significa que es una lista no vacía. (`media_list.any.rect.length > 0` tendría el mismo efecto.)

```sql
class = family and child_ref_list.length > 10
```

Familias con más de 10 hijos.

```sql
class = event and date.modifier = 0 and date.dateval[2] > 2020
```

Eventos donde la fecha es una fecha normal (no un rango, etc.) y el año es posterior a 2020.

```sql
note_list.any.get_note.text.string ~ "David"
```

Todos los objetos con al menos una nota que contiene la cadena "David" en su texto.

```sql
class = family and child_ref_list.all.ref.get_person.gender = 0 and child_ref_list.length = 3
```

Todas las familias con tres hijas.

## Lista completa de Propiedades de Gramps

Para una lista completa de propiedades de Gramps, consulta la [documentación de GQL](https://github.com/DavidMStraub/gramps-ql#full-list-of-gramps-properties).
