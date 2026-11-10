# Grampsオブジェクトクエリ言語を使用したフィルタリング

[オブジェクトリストビュー](lists.md)（人物、家族、イベントなど）および[タスクリスト](tasks.md)には、[Grampsオブジェクトクエリ言語](https://github.com/DavidMStraub/gramps-object-query-language)（GOQL）の式用のフィルターフィールドがあります。

使用するには、フィルターパネルを開き、**GOQL**フィールドに式を入力してEnterを押すか（または**適用**をクリックします）。リストは、他のアクティブなフィルターの上に式によってフィルタリングされます。式が無効な場合、フィールドはエラーとしてマークされます。

式は常に、現在いるリストのオブジェクトに適用されます：人物リストでは、`surname == 'Smith'`は姓がSmithの人物を見つけます。

!!! note
    GOQLフィールドにはGramps Web API 3.24以降が必要です。

## 構文

GOQL式は、Pythonプログラミング言語の条件のように見えます。使用するためにPythonを知っている必要はありません – 以下の例はほとんどのニーズをカバーしています。

### 比較

比較は`field operator value`の形式を持ちます。例えば、`surname == 'Smith'`です。

Operator | 意味
---------|--------
`==` | 等しい
`!=` | 等しくない
`<`, `<=` | より小さい、以下（早い、小さい）
`>`, `>=` | より大きい、以上（遅い、大きい）
`in [ ... ]` | リストされた値の1つである、例えば`surname in ['Meyer', 'Maier']`
`not in [ ... ]` | リストされた値のいずれでもない
`'text' in field` | フィールドにテキストが含まれている、例えば`'mill' in surname`
`is None` | フィールドが空であるか存在しない、例えば`death.date.sortval is None`

テキストはシングルまたはダブルクォートで囲みます（`'Smith'`）、数字はそのまま使用します（`1850`）。比較は連鎖させることができ、例えば`Date('1850') <= birth.date.sortval < Date('1900')`のようにします。

### 条件の組み合わせ

条件は`and`および`or`で組み合わせることができ、`not`で反転させることができます。`and`は`or`よりも優先されます；条件をグループ化するために括弧を使用してください：

```python
(gender == Person.MALE and surname == 'Smith') or given_name == 'Mary'
```

### テキストパターン

- `like(field, 'pattern')`は、`%`が任意のテキストを、`_`が単一の文字を表すパターンと一致します。例えば、`like(given_name, 'J%')`は「J」で始まるすべての名前に一致します。
- `regex(field, 'pattern')`は、[正規表現](https://en.wikipedia.org/wiki/Regular_expression)と一致します。例えば、`regex(surname, '^M[ae][iy]er$')`です。

`like`および`'text' in field`は大文字と小文字を無視します（SQLiteでは、これはアクセントのないA–Zの文字にのみ適用されます）。`regex`は大文字と小文字を区別します。

### フィールド

フィールドは、`gender`や`gramps_id`のようなオブジェクトのプロパティの名前、または`primary_name.first_name`や`primary_name.surname_list[0].surname`のようなネストされたプロパティへのパスです。角括弧は、0から始まる位置でリストの要素を選択します。利用可能なプロパティは、[Grampsデータモデル](https://gramps-project.org/wiki/index.php/Gramps_Data_Model)のものです。フィールドが存在しない場合、エラーメッセージには存在するフィールドがリストされます。

いくつかのショートカットが利用可能です：

- 人物には`given_name`と`surname`があり、これは主な名前の名と姓です。
- 人物には`birth`と`death`があり、これはそれぞれの出生イベントと死亡イベントです。例えば、`birth.date.sortval`や`death.place.name.value`です。
- 家族には`father`と`mother`があり、例えば`father.surname == 'Smith'`です。
- イベントには`place`、引用には`source`、場所には`enclosed_by`があり、これは囲まれた場所を指します。

これらは連鎖させることができ、例えば家族リストでは`father.birth.place.name.value`のようにします。また、2つのフィールドを互いに比較することもできます。例えば、`father.surname == mother.surname`です。

### 関連オブジェクトのリスト

`any(collection, condition)`は、コレクションの少なくとも1つのアイテムが条件を満たす場合に一致し、`len(collection)`はアイテムの数をカウントします。条件なしで`any(collection)`は、コレクションが空でない場合に一致します。コレクションは次の通りです：

- ほとんどすべてのオブジェクトに：`notes`、`citations`、`media`、および`tags`
- 人物に：`events`、`families`（パートナーとして）、`parent_families`（子供として）、および`associations`
- 家族に：`children`
- すべてのオブジェクトに：`backlinks`、それを参照するオブジェクトで、`_class`でその型をテストできます。例えば、`any(backlinks, _class == 'Person')`です。

`any`および`len`は、`alternate_names`や`primary_name.surname_list`のように、オブジェクト自体に保存されているリストにも適用されます。

### 定数と型

Grampsの固定値は定数として利用可能で、例えば`Person.MALE`、`Person.FEMALE`、`Person.UNKNOWN`、または信頼レベル`Citation.CONF_VERY_LOW`から`Citation.CONF_VERY_HIGH`までです。型は、`EventType.BIRTH`、`FamilyRelType.MARRIED`、`NameType.BIRTH`、`PlaceType.VILLAGE`、または`RepositoryType.ARCHIVE`のような定数とその`value`で比較されます：

```python
type.value == EventType.BAPTISM
```

自分で入力したカスタム型には独自の定数はありません。

### 日付

`Date('...')`は、テキストとして書かれた日付を、日付の`sortval`と比較できる値に変換します。例えば、`birth.date.sortval < Date('1800')`です。

`sortval`は単一の時点であり、日付の型や品質を無視します：「1800年前」、「1800年頃」、「1800年」はすべて同じ`sortval`を持ち、範囲やスパンの場合は開始点です。これらを考慮するために、日付の`modifier`や`quality`を、`Date.MOD_ABOUT`、`Date.MOD_BEFORE`、`Date.MOD_AFTER`、`Date.MOD_RANGE`、`Date.MOD_SPAN`、または`Date.QUAL_ESTIMATED`のような定数と比較します：

```python
date.modifier == Date.MOD_ABOUT
```

## コメント付きの例

人物リスト：

```python
gender == Person.FEMALE and like(given_name, 'Mar%')
```

名が「Mar」で始まる女性。

```python
Date('1850') <= birth.date.sortval < Date('1900')
```

1850年から1899年の間に生まれた人物。

```python
birth.place.name.value == death.place.name.value
```

同じ名前の場所で生まれ、亡くなった人物。

```python
not any(notes)
```

メモがない人物。

```python
any(events, type.value == EventType.BURIAL)
```

埋葬イベントを持つ人物。

```python
any(alternate_names, surname_list[0].surname == 'Meyer')
```

姓がMeyerの別名を持つ人物。

家族リスト：

```python
len(children) > 10
```

10人以上の子供を持つ家族。

```python
len(children, gender == Person.FEMALE) == 3
```

3人の娘を持つ家族。

```python
mother.death.date.sortval < father.death.date.sortval
```

母親が父親より先に亡くなった家族。

イベントリスト：

```python
type.value == EventType.BAPTISM and place.name.value == 'Berlin'
```

ベルリンという場所での洗礼。

引用リスト：

```python
confidence >= Citation.CONF_HIGH
```

高いまたは非常に高い信頼性のある引用。

メモリスト：

```python
'David' in text.string and private == True
```

「David」を含むプライベートメモ。

```python
not any(backlinks)
```

どのオブジェクトにも添付されていないメモ。

## 完全なリファレンス

完全な言語リファレンスについては、[GOQLドキュメント](https://github.com/DavidMStraub/gramps-object-query-language/blob/main/docs/where_expr.md)を参照してください。
