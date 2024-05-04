# Filter using the Gramps Query Language

The object list views (people, families, events, ...) have an optional advanced filter mode based on the [Gramps Query Language](https://github.com/DavidMStraub/gramps-ql) (GQL).

To use it, type a query in GQL syntax and press enter (or hit the "apply" button). The view will be filtered by the query. If the query is invalid, the input field's frame turns red.

The GQL syntax is described below, copied from the GQL documentation.

## Syntax

A GQL query is a string composed of statements of the form `property operator value`, optionally combined with the keywords `and` and `or` as well as parentheses.

### Properties

#### `class`

Filters for the Gramps object class and can be one of `person`, `family`, `event`, `place`, `citation`, `source`, `repository`, `media`, or `note`.

#### Object properties

GQL supports querying nested properties of Gramps objects, e.g. `primary_name.date.calendar`. See below for a full list of properties – see also [Gramps Data Model](https://gramps-project.org/wiki/index.php/Gramps_Data_Model).

#### List elements by index

Individual elements in list-like properties can be accessed by positional index in square brackets. This can be combined with nested properties, e.g. `primary_name.surname_list[0].surname`.

#### `length`

This is a special property that returns the length of an array-like Gramps property, e.g. `media_list.length > 0` to get objects with media references.

#### `all`, `any`

Two more special properties for array-like Gramps properties. `all` requires a condition to apply to all items of the list, `any` requires it to apply to at least one item. Both properties can be combined with other properties before and after. Examples: `media_list.any.citation_list.length > 0` to return objects with media references that have citations; `media_list.all.citation_list.length = 0` to return objects where all media objects do not have citations.

#### Array index

A numerical array index can be used to access specific elements of a list, e.g. `child_ref_list[0]` for the first child.

#### `get_person`, etc.

While all the preceding properties refer to a single Gramps object, it is also possible to filter on different objects referred to by the initial object. For instance, an event has a place handle in its `place` property. Using the `get_place` pseudo-property, GQL switches to the properties of that object. For instance, it is possible to search for `class = event and place.get_place.name.value ~ York`. This can also be combined with `any` or `all`, e.g. `class = person and event_ref_list.any.ref.get_event.description ~ farmer`.

### Operators

#### `=`, `!=`

Equality or inequality. Examples: `class = person`, `class != family`

#### `>`, `>=`, `<`, `<=`

Comparison. Works for strings as well as numbers. Examples: `confidence <= 1`, `change > 1712477760 `, `gramps_id > "I2015"`

#### `~`, `!~`

Contains or does not contain. Works for lists as well as strings. Examples: `gramps_id !~ F00`, `author ~ David`, `family_list ~ "3a16680f7d226e3ac3eefc8b57a"`

#### No operator/value

If no operator and value is given, the value is interpreted as a boolean (true or false). This works for
all types of properties and Python rules for casting to true/false are applied. For instance, the query `private` returns private objects; `confidence` returns objects where confidence is greater than 0; `media_list` returns objects with at least one media reference.

### Values

Values can be numbers or strings. If numbers should be interpreted as strings or special characters like = are involved, enclose the value in strings. Examples: `gramps_id = F0001`, but `gramps_id = "0001"`.

## Commented examples

```sql
class = note and private and text.string ~ David
```

All private notes that contain the string "David" in their text


```sql
media_list.length >= 10
```

All objects (of any class) with 10 or more media references

```sql
class != person and media_list.any.rect
```

All objects that are *not* a person but have a media reference that is part of an image. Here, `media_list.any.rect` means that for each of the items in the media list, it is checked whether the `rect` (rectangle) property has a truthy value, meaning it is a non-empty list. (`media_list.any.rect.length > 0` would have the same effect.)

```sql
class = family and child_ref_list.length > 10
```

Families with more than 10 children.

```sql
class = event and date.modifier = 0 and date.dateval[2] > 2020
```

Events where the date is a normal date (not a range etc.) and the year is after 2020.

```sql
note_list.any.get_note.text.string ~ "David"
```

All objects with at least one note that contains the string "David" in their text.


```sql
class = family and child_ref_list.all.ref.get_person.gender = 0 and child_ref_list.length = 3
```

All families with three daughters.


## Full list of Gramps Properties

For a full list of Gramps properties, see the [GQL documentation](https://github.com/DavidMStraub/gramps-ql#full-list-of-gramps-properties).