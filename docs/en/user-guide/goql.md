# Filter using the Gramps Object Query Language

The [object list views](lists.md) (people, families, events, ...) and the [task list](tasks.md) have a filter field for expressions in the [Gramps Object Query Language](https://github.com/DavidMStraub/gramps-object-query-language) (GOQL).

To use it, open the filter panel, type an expression in the **GOQL** field and press Enter (or click **Apply**). The list is filtered by the expression, on top of any other active filters. If the expression is invalid, the field is marked as an error.

The expression always applies to the objects of the list you are in: in the People list, `surname == 'Smith'` finds the people with the surname Smith.

!!! note
    The GOQL field needs Gramps Web API 3.24 or newer.

## Syntax

A GOQL expression looks like a condition in the Python programming language. You don't need to know Python to use it – the examples below cover most needs.

### Comparisons

A comparison has the form `field operator value`, for example `surname == 'Smith'`.

Operator | Meaning
---------|--------
`==` | is equal to
`!=` | is not equal to
`<`, `<=` | is less than, less than or equal to (earlier, smaller)
`>`, `>=` | is greater than, greater than or equal to (later, bigger)
`in [ ... ]` | is one of the listed values, e.g. `surname in ['Meyer', 'Maier']`
`not in [ ... ]` | is none of the listed values
`'text' in field` | the field contains the text, e.g. `'mill' in surname`
`is None` | the field is empty or does not exist, e.g. `death.date.sortval is None`

Text goes in single or double quotes (`'Smith'`), numbers don't (`1850`). Comparisons can be chained, e.g. `Date('1850') <= birth.date.sortval < Date('1900')`.

### Combining conditions

Conditions can be combined with `and` and `or`, and inverted with `not`. `and` takes precedence over `or`; use parentheses to group conditions:

```python
(gender == Person.MALE and surname == 'Smith') or given_name == 'Mary'
```

### Text patterns

- `like(field, 'pattern')` matches a pattern in which `%` stands for any text and `_` for a single character, e.g. `like(given_name, 'J%')` for all given names starting with "J".
- `regex(field, 'pattern')` matches a [regular expression](https://en.wikipedia.org/wiki/Regular_expression), e.g. `regex(surname, '^M[ae][iy]er$')`.

`like` and `'text' in field` ignore upper and lower case (on SQLite, this only applies to the letters A–Z without accents). `regex` is case-sensitive.

### Fields

A field is the name of a property of the object, like `gender` or `gramps_id`, or a path to a nested property, like `primary_name.first_name` or `primary_name.surname_list[0].surname`. The square brackets select an element of a list by its position, starting from 0. The available properties are those of the [Gramps data model](https://gramps-project.org/wiki/index.php/Gramps_Data_Model). If a field does not exist, the error message lists the fields that do.

A few shortcuts are available:

- People have `given_name` and `surname`, the given name and surname of the primary name.
- People have `birth` and `death`, their birth and death events, e.g. `birth.date.sortval` or `death.place.name.value`.
- Families have `father` and `mother`, e.g. `father.surname == 'Smith'`.
- Events have `place`, citations have `source`, and places have `enclosed_by`, the enclosing place.

These can be chained, e.g. `father.birth.place.name.value` in the Families list. Two fields can also be compared with each other, e.g. `father.surname == mother.surname`.

### Lists of related objects

`any(collection, condition)` matches if at least one item of a collection meets the condition, and `len(collection)` counts the items. Without a condition, `any(collection)` matches if the collection is not empty. Collections are:

- on almost every object: `notes`, `citations`, `media`, and `tags`
- on people: `events`, `families` (as a partner), `parent_families` (as a child), and `associations`
- on families: `children`
- on all objects: `backlinks`, the objects that refer to it, which can be tested for their type with `_class`, e.g. `any(backlinks, _class == 'Person')`

`any` and `len` also work for lists stored in the object itself, such as `alternate_names` or `primary_name.surname_list`.

### Constants and types

Fixed values of Gramps are available as constants, such as `Person.MALE`, `Person.FEMALE`, `Person.UNKNOWN`, or the confidence levels `Citation.CONF_VERY_LOW` to `Citation.CONF_VERY_HIGH`. Types are compared by their `value` with constants such as `EventType.BIRTH`, `FamilyRelType.MARRIED`, `NameType.BIRTH`, `PlaceType.VILLAGE`, or `RepositoryType.ARCHIVE`:

```python
type.value == EventType.BAPTISM
```

Custom types that you have entered yourself have no constant of their own.

### Dates

`Date('...')` turns a date written as text into a value that can be compared with the `sortval` of a date, e.g. `birth.date.sortval < Date('1800')`.

The `sortval` is a single point in time and ignores the type and quality of a date: "before 1800", "about 1800" and "1800" all have the same `sortval`, and for a range or span it is the start. To take these into account, compare the `modifier` or `quality` of the date with constants such as `Date.MOD_ABOUT`, `Date.MOD_BEFORE`, `Date.MOD_AFTER`, `Date.MOD_RANGE`, `Date.MOD_SPAN`, or `Date.QUAL_ESTIMATED`:

```python
date.modifier == Date.MOD_ABOUT
```

## Commented examples

People list:

```python
gender == Person.FEMALE and like(given_name, 'Mar%')
```

Women whose given name starts with "Mar".

```python
Date('1850') <= birth.date.sortval < Date('1900')
```

People born from 1850 to 1899.

```python
birth.place.name.value == death.place.name.value
```

People who were born and died in a place with the same name.

```python
not any(notes)
```

People without notes.

```python
any(events, type.value == EventType.BURIAL)
```

People with a burial event.

```python
any(alternate_names, surname_list[0].surname == 'Meyer')
```

People with an alternate name with the surname Meyer.

Families list:

```python
len(children) > 10
```

Families with more than 10 children.

```python
len(children, gender == Person.FEMALE) == 3
```

Families with three daughters.

```python
mother.death.date.sortval < father.death.date.sortval
```

Families in which the mother died before the father.

Events list:

```python
type.value == EventType.BAPTISM and place.name.value == 'Berlin'
```

Baptisms in a place named Berlin.

Citations list:

```python
confidence >= Citation.CONF_HIGH
```

Citations with a high or very high confidence.

Notes list:

```python
'David' in text.string and private == True
```

Private notes that contain "David".

```python
not any(backlinks)
```

Notes that are not attached to any object.

## Full reference

For the full language reference, see the [GOQL documentation](https://github.com/DavidMStraub/gramps-object-query-language/blob/main/docs/where_expr.md).
