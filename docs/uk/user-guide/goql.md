# Фільтрація за допомогою Мови Запитів Об'єктів Gramps

[Перегляди списків об'єктів](lists.md) (люди, родини, події тощо) та [список завдань](tasks.md) мають поле фільтрації для виразів у [Мові Запитів Об'єктів Gramps](https://github.com/DavidMStraub/gramps-object-query-language) (GOQL).

Щоб його використовувати, відкрийте панель фільтрації, введіть вираз у полі **GOQL** та натисніть Enter (або натисніть **Застосувати**). Список фільтрується за виразом, поверх будь-яких інших активних фільтрів. Якщо вираз є недійсним, поле позначається як помилка.

Вираз завжди застосовується до об'єктів списку, в якому ви знаходитесь: у списку людей `surname == 'Smith'` знаходить людей з прізвищем Сміт.

!!! note
    Поле GOQL потребує Gramps Web API 3.24 або новішої версії.

## Синтаксис

Вираз GOQL виглядає як умова в мові програмування Python. Вам не потрібно знати Python, щоб його використовувати – приклади нижче покривають більшість потреб.

### Порівняння

Порівняння має форму `поле оператор значення`, наприклад `surname == 'Smith'`.

Оператор | Значення
---------|--------
`==` | дорівнює
`!=` | не дорівнює
`<`, `<=` | менше ніж, менше або дорівнює (раніше, менше)
`>`, `>=` | більше ніж, більше або дорівнює (пізніше, більше)
`in [ ... ]` | є одним з перерахованих значень, наприклад `surname in ['Meyer', 'Maier']`
`not in [ ... ]` | не є жодним з перерахованих значень
`'text' in поле` | поле містить текст, наприклад `'mill' in surname`
`is None` | поле порожнє або не існує, наприклад `death.date.sortval is None`

Текст поміщається в одинарні або подвійні лапки (`'Smith'`), числа – без лапок (`1850`). Порівняння можуть бути з'єднані, наприклад `Date('1850') <= birth.date.sortval < Date('1900')`.

### Об'єднання умов

Умови можуть бути об'єднані за допомогою `and` та `or`, і інвертовані за допомогою `not`. `and` має пріоритет над `or`; використовуйте дужки для групування умов:

```python
(gender == Person.MALE and surname == 'Smith') or given_name == 'Mary'
```

### Шаблони тексту

- `like(field, 'pattern')` відповідає шаблону, в якому `%` означає будь-який текст, а `_` – один символ, наприклад `like(given_name, 'J%')` для всіх імен, що починаються на "J".
- `regex(field, 'pattern')` відповідає [регулярному виразу](https://en.wikipedia.org/wiki/Regular_expression), наприклад `regex(surname, '^M[ae][iy]er$')`.

`like` та `'text' in поле` ігнорують регістр (в SQLite це стосується лише літер A–Z без акцентів). `regex` чутливий до регістру.

### Поля

Поле – це назва властивості об'єкта, такої як `gender` або `gramps_id`, або шлях до вкладеної властивості, такої як `primary_name.first_name` або `primary_name.surname_list[0].surname`. Квадратні дужки вибирають елемент списку за його позицією, починаючи з 0. Доступні властивості – це властивості [моделі даних Gramps](https://gramps-project.org/wiki/index.php/Gramps_Data_Model). Якщо поле не існує, повідомлення про помилку перераховує поля, які існують.

Декілька скорочень доступні:

- У людей є `given_name` та `surname`, ім'я та прізвище основного імені.
- У людей є `birth` та `death`, їхні події народження та смерті, наприклад `birth.date.sortval` або `death.place.name.value`.
- У родин є `father` та `mother`, наприклад `father.surname == 'Smith'`.
- У подій є `place`, у цитат є `source`, а у місць є `enclosed_by`, місце, яке оточує.

Ці поля можуть бути з'єднані, наприклад `father.birth.place.name.value` у списку родин. Два поля також можуть бути порівняні між собою, наприклад `father.surname == mother.surname`.

### Списки пов'язаних об'єктів

`any(collection, condition)` відповідає, якщо принаймні один елемент колекції відповідає умові, а `len(collection)` підраховує елементи. Без умови `any(collection)` відповідає, якщо колекція не порожня. Колекції:

- майже на кожному об'єкті: `notes`, `citations`, `media` та `tags`
- у людей: `events`, `families` (як партнер), `parent_families` (як дитина) та `associations`
- у родин: `children`
- у всіх об'єктах: `backlinks`, об'єкти, які на них посилаються, які можна перевірити за їх типом за допомогою `_class`, наприклад `any(backlinks, _class == 'Person')`

`any` та `len` також працюють для списків, збережених в самому об'єкті, таких як `alternate_names` або `primary_name.surname_list`.

### Константи та типи

Фіксовані значення Gramps доступні як константи, такі як `Person.MALE`, `Person.FEMALE`, `Person.UNKNOWN`, або рівні впевненості `Citation.CONF_VERY_LOW` до `Citation.CONF_VERY_HIGH`. Типи порівнюються за їх `value` з константами, такими як `EventType.BIRTH`, `FamilyRelType.MARRIED`, `NameType.BIRTH`, `PlaceType.VILLAGE` або `RepositoryType.ARCHIVE`:

```python
type.value == EventType.BAPTISM
```

Користувацькі типи, які ви ввели самостійно, не мають власної константи.

### Дати

`Date('...')` перетворює дату, написану як текст, на значення, яке можна порівнювати з `sortval` дати, наприклад `birth.date.sortval < Date('1800')`.

`sortval` – це єдина точка в часі і ігнорує тип і якість дати: "до 1800", "близько 1800" та "1800" всі мають однаковий `sortval`, а для діапазону або проміжку це початок. Щоб врахувати це, порівняйте `modifier` або `quality` дати з константами, такими як `Date.MOD_ABOUT`, `Date.MOD_BEFORE`, `Date.MOD_AFTER`, `Date.MOD_RANGE`, `Date.MOD_SPAN` або `Date.QUAL_ESTIMATED`:

```python
date.modifier == Date.MOD_ABOUT
```

## Приклади з коментарями

Список людей:

```python
gender == Person.FEMALE and like(given_name, 'Mar%')
```

Жінки, чиє ім'я починається на "Mar".

```python
Date('1850') <= birth.date.sortval < Date('1900')
```

Люди, народжені з 1850 по 1899 рік.

```python
birth.place.name.value == death.place.name.value
```

Люди, які народилися і померли в місці з однаковою назвою.

```python
not any(notes)
```

Люди без нотаток.

```python
any(events, type.value == EventType.BURIAL)
```

Люди з подією поховання.

```python
any(alternate_names, surname_list[0].surname == 'Meyer')
```

Люди з альтернативним ім'ям з прізвищем Мейер.

Список родин:

```python
len(children) > 10
```

Родини з більше ніж 10 дітьми.

```python
len(children, gender == Person.FEMALE) == 3
```

Родини з трьома доньками.

```python
mother.death.date.sortval < father.death.date.sortval
```

Родини, в яких мати померла раніше батька.

Список подій:

```python
type.value == EventType.BAPTISM and place.name.value == 'Berlin'
```

Хрещення в місці з назвою Берлін.

Список цитат:

```python
confidence >= Citation.CONF_HIGH
```

Цитати з високим або дуже високим рівнем впевненості.

Список нотаток:

```python
'David' in text.string and private == True
```

Приватні нотатки, які містять "David".

```python
not any(backlinks)
```

Нотатки, які не прикріплені до жодного об'єкта.

## Повна довідка

Для повної довідки по мові дивіться [документацію GOQL](https://github.com/DavidMStraub/gramps-object-query-language/blob/main/docs/where_expr.md).
