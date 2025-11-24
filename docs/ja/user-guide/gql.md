# Grampsクエリ言語を使用したフィルタリング

オブジェクトリストビュー（人、家族、イベントなど）は、[Grampsクエリ言語](https://github.com/DavidMStraub/gramps-ql)（GQL）に基づくオプションの高度なフィルターモードを持っています。

これを使用するには、GQL構文でクエリを入力し、Enterキーを押すか、「適用」ボタンをクリックします。ビューはクエリによってフィルタリングされます。クエリが無効な場合、入力フィールドの枠が赤くなります。

GQL構文は以下に説明されており、GQLドキュメントからコピーされています。

## 構文

GQLクエリは、`property operator value`の形式のステートメントで構成された文字列であり、オプションで`and`および`or`というキーワードや括弧で組み合わせることができます。

### プロパティ

#### `class`

Grampsオブジェクトクラスをフィルタリングし、`person`、`family`、`event`、`place`、`citation`、`source`、`repository`、`media`、または`note`のいずれかになります。

#### オブジェクトプロパティ

GQLは、Grampsオブジェクトのネストされたプロパティをクエリすることをサポートしています。例：`primary_name.date.calendar`。プロパティの完全なリストについては、下記を参照してください。また、[Grampsデータモデル](https://gramps-project.org/wiki/index.php/Gramps_Data_Model)も参照してください。

#### インデックスによるリスト要素

リストのようなプロパティ内の個々の要素には、角括弧内の位置インデックスでアクセスできます。これはネストされたプロパティと組み合わせることができます。例：`primary_name.surname_list[0].surname`。

#### `length`

これは特別なプロパティで、配列のようなGrampsプロパティの長さを返します。例：`media_list.length > 0`は、メディア参照を持つオブジェクトを取得します。

#### `all`, `any`

配列のようなGrampsプロパティに対するもう2つの特別なプロパティです。`all`はリストのすべてのアイテムに条件が適用されることを要求し、`any`は少なくとも1つのアイテムに適用されることを要求します。両方のプロパティは、前後の他のプロパティと組み合わせることができます。例：`media_list.any.citation_list.length > 0`は、引用を持つメディア参照を持つオブジェクトを返します；`media_list.all.citation_list.length = 0`は、すべてのメディアオブジェクトが引用を持たないオブジェクトを返します。

#### 配列インデックス

数値の配列インデックスを使用してリストの特定の要素にアクセスできます。例：`child_ref_list[0]`は最初の子供を指します。

#### `get_person`など

前述のすべてのプロパティは単一のGrampsオブジェクトを参照しますが、初期オブジェクトによって参照される異なるオブジェクトでフィルタリングすることも可能です。たとえば、イベントにはその`place`プロパティに場所ハンドルがあります。`get_place`擬似プロパティを使用すると、GQLはそのオブジェクトのプロパティに切り替わります。たとえば、`class = event and place.get_place.name.value ~ York`を検索することが可能です。これは`any`や`all`と組み合わせることもできます。例：`class = person and event_ref_list.any.ref.get_event.description ~ farmer`。

### 演算子

#### `=`, `!=`

等しいまたは等しくない。例：`class = person`、`class != family`

#### `>`, `>=`, `<`, `<=`

比較。文字列および数値に対して機能します。例：`confidence <= 1`、`change > 1712477760`、`gramps_id > "I2015"`

#### `~`, `!~`

含むまたは含まない。リストおよび文字列に対して機能します。例：`gramps_id !~ F00`、`author ~ David`、`family_list ~ "3a16680f7d226e3ac3eefc8b57a"`

#### 演算子/値なし

演算子と値が指定されていない場合、値はブール値（trueまたはfalse）として解釈されます。これはすべてのタイプのプロパティに対して機能し、Pythonの真偽値へのキャストルールが適用されます。たとえば、クエリ`private`はプライベートオブジェクトを返します；`confidence`は信頼度が0より大きいオブジェクトを返します；`media_list`は少なくとも1つのメディア参照を持つオブジェクトを返します。

### 値

値は数値または文字列です。数値を文字列として解釈する必要がある場合や、`=`のような特殊文字が関与する場合は、値を文字列で囲みます。例：`gramps_id = F0001`、ただし`gramps_id = "0001"`。

## コメント付きの例

```sql
class = note and private and text.string ~ David
```

テキストに「David」という文字列を含むすべてのプライベートノート


```sql
media_list.length >= 10
```

メディア参照が10以上のすべてのオブジェクト（任意のクラス）


```sql
class != person and media_list.any.rect
```

人ではないが、画像の一部としてメディア参照を持つすべてのオブジェクト。ここで、`media_list.any.rect`は、メディアリスト内の各アイテムについて、`rect`（長方形）プロパティが真の値を持つかどうかをチェックします。つまり、空でないリストです。(`media_list.any.rect.length > 0`も同じ効果があります。)

```sql
class = family and child_ref_list.length > 10
```

10人以上の子供を持つ家族。

```sql
class = event and date.modifier = 0 and date.dateval[2] > 2020
```

日付が通常の日付（範囲などではなく）で、年が2020年以降のイベント。

```sql
note_list.any.get_note.text.string ~ "David"
```

テキストに「David」という文字列を含むノートを少なくとも1つ持つすべてのオブジェクト。


```sql
class = family and child_ref_list.all.ref.get_person.gender = 0 and child_ref_list.length = 3
```

3人の娘を持つすべての家族。


## Grampsプロパティの完全なリスト

Grampsプロパティの完全なリストについては、[GQLドキュメント](https://github.com/DavidMStraub/gramps-ql#full-list-of-gramps-properties)を参照してください。
