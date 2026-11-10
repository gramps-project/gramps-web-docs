# Filtro usando a Linguagem de Consulta de Objetos Gramps

As [visualizações de lista de objetos](lists.md) (pessoas, famílias, eventos, ...) e a [lista de tarefas](tasks.md) têm um campo de filtro para expressões na [Linguagem de Consulta de Objetos Gramps](https://github.com/DavidMStraub/gramps-object-query-language) (GOQL).

Para usá-lo, abra o painel de filtro, digite uma expressão no campo **GOQL** e pressione Enter (ou clique em **Aplicar**). A lista é filtrada pela expressão, além de quaisquer outros filtros ativos. Se a expressão for inválida, o campo é marcado como um erro.

A expressão sempre se aplica aos objetos da lista em que você está: na lista de Pessoas, `surname == 'Smith'` encontra as pessoas com o sobrenome Smith.

!!! note
    O campo GOQL precisa da API Web do Gramps 3.24 ou mais recente.

## Sintaxe

Uma expressão GOQL se parece com uma condição na linguagem de programação Python. Você não precisa saber Python para usá-la – os exemplos abaixo cobrem a maioria das necessidades.

### Comparações

Uma comparação tem a forma `campo operador valor`, por exemplo `surname == 'Smith'`.

Operador | Significado
---------|--------
`==` | é igual a
`!=` | não é igual a
`<`, `<=` | é menor que, menor ou igual a (anterior, menor)
`>`, `>=` | é maior que, maior ou igual a (posterior, maior)
`in [ ... ]` | é um dos valores listados, por exemplo `surname in ['Meyer', 'Maier']`
`not in [ ... ]` | não é nenhum dos valores listados
`'texto' in campo` | o campo contém o texto, por exemplo `'mill' in surname`
`is None` | o campo está vazio ou não existe, por exemplo `death.date.sortval is None`

Texto vai entre aspas simples ou duplas (`'Smith'`), números não (`1850`). Comparações podem ser encadeadas, por exemplo `Date('1850') <= birth.date.sortval < Date('1900')`.

### Combinando condições

Condições podem ser combinadas com `and` e `or`, e invertidas com `not`. `and` tem precedência sobre `or`; use parênteses para agrupar condições:

```python
(gender == Person.MALE and surname == 'Smith') or given_name == 'Mary'
```

### Padrões de texto

- `like(field, 'pattern')` corresponde a um padrão em que `%` representa qualquer texto e `_` para um único caractere, por exemplo `like(given_name, 'J%')` para todos os nomes dados que começam com "J".
- `regex(field, 'pattern')` corresponde a uma [expressão regular](https://en.wikipedia.org/wiki/Regular_expression), por exemplo `regex(surname, '^M[ae][iy]er$')`.

`like` e `'texto' in campo` ignoram maiúsculas e minúsculas (no SQLite, isso se aplica apenas às letras A–Z sem acentos). `regex` é sensível a maiúsculas e minúsculas.

### Campos

Um campo é o nome de uma propriedade do objeto, como `gender` ou `gramps_id`, ou um caminho para uma propriedade aninhada, como `primary_name.first_name` ou `primary_name.surname_list[0].surname`. Os colchetes selecionam um elemento de uma lista pela sua posição, começando de 0. As propriedades disponíveis são aquelas do [modelo de dados do Gramps](https://gramps-project.org/wiki/index.php/Gramps_Data_Model). Se um campo não existir, a mensagem de erro lista os campos que existem.

Alguns atalhos estão disponíveis:

- Pessoas têm `given_name` e `surname`, o nome dado e sobrenome do nome principal.
- Pessoas têm `birth` e `death`, seus eventos de nascimento e morte, por exemplo `birth.date.sortval` ou `death.place.name.value`.
- Famílias têm `father` e `mother`, por exemplo `father.surname == 'Smith'`.
- Eventos têm `place`, citações têm `source`, e lugares têm `enclosed_by`, o lugar que envolve.

Esses podem ser encadeados, por exemplo `father.birth.place.name.value` na lista de Famílias. Dois campos também podem ser comparados entre si, por exemplo `father.surname == mother.surname`.

### Listas de objetos relacionados

`any(collection, condition)` corresponde se pelo menos um item de uma coleção atende à condição, e `len(collection)` conta os itens. Sem uma condição, `any(collection)` corresponde se a coleção não estiver vazia. As coleções são:

- em quase todos os objetos: `notes`, `citations`, `media`, e `tags`
- em pessoas: `events`, `families` (como parceiro), `parent_families` (como filho), e `associations`
- em famílias: `children`
- em todos os objetos: `backlinks`, os objetos que se referem a ele, que podem ser testados quanto ao seu tipo com `_class`, por exemplo `any(backlinks, _class == 'Person')`

`any` e `len` também funcionam para listas armazenadas no próprio objeto, como `alternate_names` ou `primary_name.surname_list`.

### Constantes e tipos

Valores fixos do Gramps estão disponíveis como constantes, como `Person.MALE`, `Person.FEMALE`, `Person.UNKNOWN`, ou os níveis de confiança `Citation.CONF_VERY_LOW` a `Citation.CONF_VERY_HIGH`. Tipos são comparados pelo seu `value` com constantes como `EventType.BIRTH`, `FamilyRelType.MARRIED`, `NameType.BIRTH`, `PlaceType.VILLAGE`, ou `RepositoryType.ARCHIVE`:

```python
type.value == EventType.BAPTISM
```

Tipos personalizados que você inseriu não têm uma constante própria.

### Datas

`Date('...')` transforma uma data escrita como texto em um valor que pode ser comparado com o `sortval` de uma data, por exemplo `birth.date.sortval < Date('1800')`.

O `sortval` é um único ponto no tempo e ignora o tipo e a qualidade de uma data: "antes de 1800", "cerca de 1800" e "1800" têm todos o mesmo `sortval`, e para um intervalo ou faixa é o início. Para levar isso em conta, compare o `modifier` ou `quality` da data com constantes como `Date.MOD_ABOUT`, `Date.MOD_BEFORE`, `Date.MOD_AFTER`, `Date.MOD_RANGE`, `Date.MOD_SPAN`, ou `Date.QUAL_ESTIMATED`:

```python
date.modifier == Date.MOD_ABOUT
```

## Exemplos comentados

Lista de pessoas:

```python
gender == Person.FEMALE and like(given_name, 'Mar%')
```

Mulheres cujo nome dado começa com "Mar".

```python
Date('1850') <= birth.date.sortval < Date('1900')
```

Pessoas nascidas de 1850 a 1899.

```python
birth.place.name.value == death.place.name.value
```

Pessoas que nasceram e morreram em um lugar com o mesmo nome.

```python
not any(notes)
```

Pessoas sem notas.

```python
any(events, type.value == EventType.BURIAL)
```

Pessoas com um evento de sepultamento.

```python
any(alternate_names, surname_list[0].surname == 'Meyer')
```

Pessoas com um nome alternativo com o sobrenome Meyer.

Lista de famílias:

```python
len(children) > 10
```

Famílias com mais de 10 filhos.

```python
len(children, gender == Person.FEMALE) == 3
```

Famílias com três filhas.

```python
mother.death.date.sortval < father.death.date.sortval
```

Famílias em que a mãe morreu antes do pai.

Lista de eventos:

```python
type.value == EventType.BAPTISM and place.name.value == 'Berlin'
```

Batismos em um lugar chamado Berlim.

Lista de citações:

```python
confidence >= Citation.CONF_HIGH
```

Citações com alta ou muito alta confiança.

Lista de notas:

```python
'David' in text.string and private == True
```

Notas privadas que contêm "David".

```python
not any(backlinks)
```

Notas que não estão anexadas a nenhum objeto.

## Referência completa

Para a referência completa da linguagem, veja a [documentação do GOQL](https://github.com/DavidMStraub/gramps-object-query-language/blob/main/docs/where_expr.md).
