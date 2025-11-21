# 使用 Gramps 查询语言进行过滤

对象列表视图（人员、家庭、事件等）具有基于 [Gramps 查询语言](https://github.com/DavidMStraub/gramps-ql) (GQL) 的可选高级过滤模式。

要使用它，请输入 GQL 语法的查询并按回车键（或点击“应用”按钮）。视图将根据查询进行过滤。如果查询无效，输入框的边框将变为红色。

GQL 语法如下所述，复制自 GQL 文档。

## 语法

GQL 查询是由 `property operator value` 形式的语句组成的字符串，可以选择性地与关键字 `and` 和 `or` 以及括号结合使用。

### 属性

#### `class`

过滤 Gramps 对象类，可以是 `person`、`family`、`event`、`place`、`citation`、`source`、`repository`、`media` 或 `note` 之一。

#### 对象属性

GQL 支持查询 Gramps 对象的嵌套属性，例如 `primary_name.date.calendar`。请参见下面的完整属性列表 - 另请参见 [Gramps 数据模型](https://gramps-project.org/wiki/index.php/Gramps_Data_Model)。

#### 按索引列出元素

可以通过方括号中的位置索引访问列表属性中的单个元素。这可以与嵌套属性结合使用，例如 `primary_name.surname_list[0].surname`。

#### `length`

这是一个特殊属性，返回类似数组的 Gramps 属性的长度，例如 `media_list.length > 0` 以获取具有媒体引用的对象。

#### `all`, `any`

两个更多的特殊属性用于类似数组的 Gramps 属性。`all` 要求条件适用于列表中的所有项，`any` 要求条件适用于至少一项。这两个属性可以与其他属性结合使用。示例：`media_list.any.citation_list.length > 0` 返回具有引用的媒体引用的对象；`media_list.all.citation_list.length = 0` 返回所有媒体对象没有引用的对象。

#### 数组索引

可以使用数字数组索引访问列表的特定元素，例如 `child_ref_list[0]` 表示第一个孩子。

#### `get_person` 等

虽然所有前面的属性都指的是单个 Gramps 对象，但也可以对初始对象所引用的不同对象进行过滤。例如，一个事件在其 `place` 属性中有一个地点句柄。使用 `get_place` 伪属性，GQL 切换到该对象的属性。例如，可以搜索 `class = event and place.get_place.name.value ~ York`。这也可以与 `any` 或 `all` 结合使用，例如 `class = person and event_ref_list.any.ref.get_event.description ~ farmer`。

### 运算符

#### `=`, `!=`

相等或不相等。示例：`class = person`，`class != family`

#### `>`, `>=`, `<`, `<=`

比较。适用于字符串和数字。示例：`confidence <= 1`，`change > 1712477760`，`gramps_id > "I2015"`

#### `~`, `!~`

包含或不包含。适用于列表和字符串。示例：`gramps_id !~ F00`，`author ~ David`，`family_list ~ "3a16680f7d226e3ac3eefc8b57a"`

#### 无运算符/值

如果未给出运算符和值，则该值被解释为布尔值（真或假）。这适用于所有类型的属性，并应用 Python 的真/假转换规则。例如，查询 `private` 返回私有对象；`confidence` 返回置信度大于 0 的对象；`media_list` 返回至少有一个媒体引用的对象。

### 值

值可以是数字或字符串。如果数字应被解释为字符串或涉及特殊字符如 =，请将值放在字符串中。示例：`gramps_id = F0001`，但 `gramps_id = "0001"`。

## 注释示例

```sql
class = note and private and text.string ~ David
```

所有包含字符串 "David" 的私有笔记


```sql
media_list.length >= 10
```

所有具有 10 个或更多媒体引用的对象（任何类）

```sql
class != person and media_list.any.rect
```

所有 *不是* 人员但具有作为图像一部分的媒体引用的对象。在这里，`media_list.any.rect` 意味着检查媒体列表中的每个项的 `rect`（矩形）属性是否具有真实值，意味着它是一个非空列表。（`media_list.any.rect.length > 0` 将具有相同的效果。）

```sql
class = family and child_ref_list.length > 10
```

有超过 10 个孩子的家庭。

```sql
class = event and date.modifier = 0 and date.dateval[2] > 2020
```

日期为正常日期（不是范围等）且年份在 2020 年之后的事件。

```sql
note_list.any.get_note.text.string ~ "David"
```

所有具有至少一个包含字符串 "David" 的笔记的对象。


```sql
class = family and child_ref_list.all.ref.get_person.gender = 0 and child_ref_list.length = 3
```

所有有三个女儿的家庭。


## Gramps 属性完整列表

有关 Gramps 属性的完整列表，请参见 [GQL 文档](https://github.com/DavidMStraub/gramps-ql#full-list-of-gramps-properties)。
