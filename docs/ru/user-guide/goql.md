# Фильтрация с использованием языка запросов объектов Gramps

[Представления списков объектов](lists.md) (люди, семьи, события и т. д.) и [список задач](tasks.md) имеют поле фильтра для выражений на [языке запросов объектов Gramps](https://github.com/DavidMStraub/gramps-object-query-language) (GOQL).

Чтобы использовать его, откройте панель фильтра, введите выражение в поле **GOQL** и нажмите Enter (или нажмите **Применить**). Список фильтруется по выражению, поверх любых других активных фильтров. Если выражение недействительно, поле помечается как ошибка.

Выражение всегда применяется к объектам списка, в котором вы находитесь: в списке людей `surname == 'Smith'` находит людей с фамилией Смит.

!!! примечание
    Поле GOQL требует Gramps Web API 3.24 или новее.

## Синтаксис

Выражение GOQL выглядит как условие в языке программирования Python. Вам не нужно знать Python, чтобы использовать его – примеры ниже охватывают большинство потребностей.

### Сравнения

Сравнение имеет форму `field operator value`, например `surname == 'Smith'`.

Оператор | Значение
---------|--------
`==` | равно
`!=` | не равно
`<`, `<=` | меньше, меньше или равно (раньше, меньше)
`>`, `>=` | больше, больше или равно (позже, больше)
`in [ ... ]` | является одним из перечисленных значений, например `surname in ['Meyer', 'Maier']`
`not in [ ... ]` | не является ни одним из перечисленных значений
`'text' in field` | поле содержит текст, например `'mill' in surname`
`is None` | поле пустое или не существует, например `death.date.sortval is None`

Текст помещается в одинарные или двойные кавычки (`'Smith'`), числа – без кавычек (`1850`). Сравнения могут быть связаны, например, `Date('1850') <= birth.date.sortval < Date('1900')`.

### Объединение условий

Условия могут быть объединены с помощью `and` и `or`, и инвертированы с помощью `not`. `and` имеет приоритет над `or`; используйте скобки для группировки условий:

```python
(gender == Person.MALE and surname == 'Smith') or given_name == 'Mary'
```

### Шаблоны текста

- `like(field, 'pattern')` соответствует шаблону, в котором `%` обозначает любой текст, а `_` – один символ, например, `like(given_name, 'J%')` для всех имен, начинающихся на "J".
- `regex(field, 'pattern')` соответствует [регулярному выражению](https://en.wikipedia.org/wiki/Regular_expression), например, `regex(surname, '^M[ae][iy]er$')`.

`like` и `'text' in field` игнорируют регистр (в SQLite это применяется только к буквам A–Z без акцентов). `regex` чувствителен к регистру.

### Поля

Поле – это название свойства объекта, например, `gender` или `gramps_id`, или путь к вложенному свойству, например, `primary_name.first_name` или `primary_name.surname_list[0].surname`. Квадратные скобки выбирают элемент списка по его позиции, начиная с 0. Доступные свойства – это свойства [модели данных Gramps](https://gramps-project.org/wiki/index.php/Gramps_Data_Model). Если поле не существует, сообщение об ошибке перечисляет существующие поля.

Доступно несколько сокращений:

- У людей есть `given_name` и `surname`, имя и фамилия основного имени.
- У людей есть `birth` и `death`, их события рождения и смерти, например, `birth.date.sortval` или `death.place.name.value`.
- У семей есть `father` и `mother`, например, `father.surname == 'Smith'`.
- У событий есть `place`, у цитат есть `source`, а у мест есть `enclosed_by`, окружающее место.

Эти поля могут быть связаны, например, `father.birth.place.name.value` в списке семей. Также можно сравнивать два поля друг с другом, например, `father.surname == mother.surname`.

### Списки связанных объектов

`any(collection, condition)` соответствует, если хотя бы один элемент коллекции соответствует условию, а `len(collection)` подсчитывает элементы. Без условия `any(collection)` соответствует, если коллекция не пуста. Коллекции:

- почти на каждом объекте: `notes`, `citations`, `media` и `tags`
- у людей: `events`, `families` (в качестве партнера), `parent_families` (в качестве ребенка) и `associations`
- у семей: `children`
- у всех объектов: `backlinks`, объекты, которые ссылаются на него, которые можно проверить по их типу с помощью `_class`, например, `any(backlinks, _class == 'Person')`

`any` и `len` также работают для списков, хранящихся в самом объекте, таких как `alternate_names` или `primary_name.surname_list`.

### Константы и типы

Фиксированные значения Gramps доступны как константы, такие как `Person.MALE`, `Person.FEMALE`, `Person.UNKNOWN`, или уровни уверенности от `Citation.CONF_VERY_LOW` до `Citation.CONF_VERY_HIGH`. Типы сравниваются по их `value` с константами, такими как `EventType.BIRTH`, `FamilyRelType.MARRIED`, `NameType.BIRTH`, `PlaceType.VILLAGE` или `RepositoryType.ARCHIVE`:

```python
type.value == EventType.BAPTISM
```

Пользовательские типы, которые вы ввели сами, не имеют своей константы.

### Даты

`Date('...')` преобразует дату, записанную в виде текста, в значение, которое можно сравнивать с `sortval` даты, например, `birth.date.sortval < Date('1800')`.

`sortval` – это единственная точка во времени и игнорирует тип и качество даты: "до 1800", "около 1800" и "1800" все имеют одинаковый `sortval`, а для диапазона или интервала это начало. Чтобы учитывать это, сравните `modifier` или `quality` даты с константами, такими как `Date.MOD_ABOUT`, `Date.MOD_BEFORE`, `Date.MOD_AFTER`, `Date.MOD_RANGE`, `Date.MOD_SPAN` или `Date.QUAL_ESTIMATED`:

```python
date.modifier == Date.MOD_ABOUT
```

## Примеры с комментариями

Список людей:

```python
gender == Person.FEMALE and like(given_name, 'Mar%')
```

Женщины, чье имя начинается на "Mar".

```python
Date('1850') <= birth.date.sortval < Date('1900')
```

Люди, родившиеся с 1850 по 1899 год.

```python
birth.place.name.value == death.place.name.value
```

Люди, которые родились и умерли в месте с одинаковым названием.

```python
not any(notes)
```

Люди без заметок.

```python
any(events, type.value == EventType.BURIAL)
```

Люди с событием захоронения.

```python
any(alternate_names, surname_list[0].surname == 'Meyer')
```

Люди с альтернативным именем с фамилией Мейер.

Список семей:

```python
len(children) > 10
```

Семьи с более чем 10 детьми.

```python
len(children, gender == Person.FEMALE) == 3
```

Семьи с тремя дочерьми.

```python
mother.death.date.sortval < father.death.date.sortval
```

Семьи, в которых мать умерла раньше отца.

Список событий:

```python
type.value == EventType.BAPTISM and place.name.value == 'Berlin'
```

Крещения в месте с названием Берлин.

Список цитат:

```python
confidence >= Citation.CONF_HIGH
```

Цитаты с высокой или очень высокой уверенностью.

Список заметок:

```python
'David' in text.string and private == True
```

Частные заметки, содержащие "David".

```python
not any(backlinks)
```

Заметки, которые не прикреплены к какому-либо объекту.

## Полное руководство

Для полного справочника по языку смотрите [документацию GOQL](https://github.com/DavidMStraub/gramps-object-query-language/blob/main/docs/where_expr.md).
