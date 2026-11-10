# 使用 Gramps 对象查询语言进行过滤

[对象列表视图](lists.md)（人员、家庭、事件等）和[任务列表](tasks.md)都有一个用于表达式的过滤字段，使用[Gramps 对象查询语言](https://github.com/DavidMStraub/gramps-object-query-language)（GOQL）。

要使用它，请打开过滤面板，在 **GOQL** 字段中输入表达式并按 Enter（或单击 **应用**）。列表将根据该表达式进行过滤，叠加在任何其他活动过滤器之上。如果表达式无效，该字段将标记为错误。

该表达式始终适用于您所在列表的对象：在人员列表中，`surname == 'Smith'` 查找姓氏为 Smith 的人员。

!!! note
    GOQL 字段需要 Gramps Web API 3.24 或更高版本。

## 语法

GOQL 表达式看起来像 Python 编程语言中的条件。您不需要了解 Python 就可以使用它——下面的示例涵盖了大多数需求。

### 比较

比较的形式为 `field operator value`，例如 `surname == 'Smith'`。

操作符 | 意义
---------|--------
`==` | 等于
`!=` | 不等于
`<`, `<=` | 小于，小于或等于（较早，较小）
`>`, `>=` | 大于，大于或等于（较晚，较大）
`in [ ... ]` | 是列出值之一，例如 `surname in ['Meyer', 'Maier']`
`not in [ ... ]` | 不是列出值之一
`'text' in field` | 字段包含文本，例如 `'mill' in surname`
`is None` | 字段为空或不存在，例如 `death.date.sortval is None`

文本用单引号或双引号括起来（`'Smith'`），数字则不需要（`1850`）。比较可以链接，例如 `Date('1850') <= birth.date.sortval < Date('1900')`。

### 组合条件

条件可以使用 `and` 和 `or` 组合，并使用 `not` 进行反转。`and` 的优先级高于 `or`；使用括号来分组条件：

```python
(gender == Person.MALE and surname == 'Smith') or given_name == 'Mary'
```

### 文本模式

- `like(field, 'pattern')` 匹配一个模式，其中 `%` 代表任何文本，`_` 代表单个字符，例如 `like(given_name, 'J%')` 用于所有以 "J" 开头的名字。
- `regex(field, 'pattern')` 匹配一个[正则表达式](https://en.wikipedia.org/wiki/Regular_expression)，例如 `regex(surname, '^M[ae][iy]er$')`。

`like` 和 `'text' in field` 忽略大小写（在 SQLite 上，这仅适用于不带重音的字母 A–Z）。`regex` 是区分大小写的。

### 字段

字段是对象属性的名称，如 `gender` 或 `gramps_id`，或嵌套属性的路径，如 `primary_name.first_name` 或 `primary_name.surname_list[0].surname`。方括号通过位置选择列表中的元素，从 0 开始。可用的属性是[Gramps 数据模型](https://gramps-project.org/wiki/index.php/Gramps_Data_Model)中的属性。如果字段不存在，错误消息将列出存在的字段。

有一些快捷方式可用：

- 人员有 `given_name` 和 `surname`，即主要名称的名字和姓氏。
- 人员有 `birth` 和 `death`，即他们的出生和死亡事件，例如 `birth.date.sortval` 或 `death.place.name.value`。
- 家庭有 `father` 和 `mother`，例如 `father.surname == 'Smith'`。
- 事件有 `place`，引用有 `source`，地点有 `enclosed_by`，即包围地点。

这些可以链接，例如在家庭列表中使用 `father.birth.place.name.value`。两个字段也可以相互比较，例如 `father.surname == mother.surname`。

### 相关对象列表

`any(collection, condition)` 如果集合中的至少一个项目满足条件，则匹配，`len(collection)` 计算项目数量。没有条件时，`any(collection)` 如果集合不为空则匹配。集合包括：

- 几乎每个对象都有的：`notes`、`citations`、`media` 和 `tags`
- 人员：`events`、`families`（作为伴侣）、`parent_families`（作为子女）和 `associations`
- 家庭：`children`
- 所有对象：`backlinks`，指向它的对象，可以通过 `_class` 测试其类型，例如 `any(backlinks, _class == 'Person')`

`any` 和 `len` 也适用于存储在对象本身中的列表，例如 `alternate_names` 或 `primary_name.surname_list`。

### 常量和类型

Gramps 的固定值作为常量可用，例如 `Person.MALE`、`Person.FEMALE`、`Person.UNKNOWN`，或置信度级别 `Citation.CONF_VERY_LOW` 到 `Citation.CONF_VERY_HIGH`。类型通过其 `value` 与常量进行比较，例如 `EventType.BIRTH`、`FamilyRelType.MARRIED`、`NameType.BIRTH`、`PlaceType.VILLAGE` 或 `RepositoryType.ARCHIVE`：

```python
type.value == EventType.BAPTISM
```

您自己输入的自定义类型没有自己的常量。

### 日期

`Date('...')` 将以文本形式书写的日期转换为可以与日期的 `sortval` 进行比较的值，例如 `birth.date.sortval < Date('1800')`。

`sortval` 是一个时间点，忽略日期的类型和质量：“1800 年之前”、“约 1800 年”和“1800 年”都具有相同的 `sortval`，对于范围或跨度，它是开始。要考虑这些因素，可以将日期的 `modifier` 或 `quality` 与常量进行比较，例如 `Date.MOD_ABOUT`、`Date.MOD_BEFORE`、`Date.MOD_AFTER`、`Date.MOD_RANGE`、`Date.MOD_SPAN` 或 `Date.QUAL_ESTIMATED`：

```python
date.modifier == Date.MOD_ABOUT
```

## 注释示例

人员列表：

```python
gender == Person.FEMALE and like(given_name, 'Mar%')
```

名字以 "Mar" 开头的女性。

```python
Date('1850') <= birth.date.sortval < Date('1900')
```

1850 年至 1899 年出生的人。

```python
birth.place.name.value == death.place.name.value
```

在同一地点出生和去世的人。

```python
not any(notes)
```

没有备注的人。

```python
any(events, type.value == EventType.BURIAL)
```

有埋葬事件的人。

```python
any(alternate_names, surname_list[0].surname == 'Meyer')
```

有替代名称且姓氏为 Meyer 的人。

家庭列表：

```python
len(children) > 10
```

有超过 10 个孩子的家庭。

```python
len(children, gender == Person.FEMALE) == 3
```

有三个女儿的家庭。

```python
mother.death.date.sortval < father.death.date.sortval
```

母亲在父亲之前去世的家庭。

事件列表：

```python
type.value == EventType.BAPTISM and place.name.value == 'Berlin'
```

在名为柏林的地方的洗礼。

引用列表：

```python
confidence >= Citation.CONF_HIGH
```

置信度高或非常高的引用。

备注列表：

```python
'David' in text.string and private == True
```

包含 "David" 的私人备注。

```python
not any(backlinks)
```

未附加到任何对象的备注。

## 完整参考

有关完整的语言参考，请参见[GOQL 文档](https://github.com/DavidMStraub/gramps-object-query-language/blob/main/docs/where_expr.md)。
