# Filtrar usando a Linguagem de Consulta Gramps

As visualizações de lista de objetos (pessoas, famílias, eventos, ...) têm um modo de filtro avançado opcional baseado na [Linguagem de Consulta Gramps](https://github.com/DavidMStraub/gramps-ql) (GQL).

Para usá-lo, digite uma consulta na sintaxe GQL e pressione enter (ou clique no botão "aplicar"). A visualização será filtrada pela consulta. Se a consulta for inválida, a moldura do campo de entrada ficará vermelha.

A sintaxe GQL é descrita abaixo, copiada da documentação GQL.

## Sintaxe

Uma consulta GQL é uma string composta por declarações da forma `propriedade operador valor`, opcionalmente combinadas com as palavras-chave `and` e `or`, bem como parênteses.

### Propriedades

#### `class`

Filtra pela classe de objeto Gramps e pode ser uma das seguintes: `person`, `family`, `event`, `place`, `citation`, `source`, `repository`, `media`, ou `note`.

#### Propriedades do objeto

O GQL suporta consultas a propriedades aninhadas de objetos Gramps, por exemplo, `primary_name.date.calendar`. Veja abaixo uma lista completa de propriedades – veja também o [Modelo de Dados Gramps](https://gramps-project.org/wiki/index.php/Gramps_Data_Model).

#### Elementos da lista por índice

Elementos individuais em propriedades semelhantes a listas podem ser acessados por índice posicional entre colchetes. Isso pode ser combinado com propriedades aninhadas, por exemplo, `primary_name.surname_list[0].surname`.

#### `length`

Esta é uma propriedade especial que retorna o comprimento de uma propriedade Gramps semelhante a um array, por exemplo, `media_list.length > 0` para obter objetos com referências de mídia.

#### `all`, `any`

Mais duas propriedades especiais para propriedades Gramps semelhantes a arrays. `all` requer que uma condição se aplique a todos os itens da lista, `any` requer que se aplique a pelo menos um item. Ambas as propriedades podem ser combinadas com outras propriedades antes e depois. Exemplos: `media_list.any.citation_list.length > 0` para retornar objetos com referências de mídia que têm citações; `media_list.all.citation_list.length = 0` para retornar objetos onde todos os objetos de mídia não têm citações.

#### Índice de array

Um índice numérico de array pode ser usado para acessar elementos específicos de uma lista, por exemplo, `child_ref_list[0]` para o primeiro filho.

#### `get_person`, etc.

Enquanto todas as propriedades anteriores se referem a um único objeto Gramps, também é possível filtrar diferentes objetos referidos pelo objeto inicial. Por exemplo, um evento tem um identificador de lugar em sua propriedade `place`. Usando a pseudo-propriedade `get_place`, o GQL muda para as propriedades desse objeto. Por exemplo, é possível buscar `class = event and place.get_place.name.value ~ York`. Isso também pode ser combinado com `any` ou `all`, por exemplo, `class = person and event_ref_list.any.ref.get_event.description ~ farmer`.

### Operadores

#### `=`, `!=`

Igualdade ou desigualdade. Exemplos: `class = person`, `class != family`

#### `>`, `>=`, `<`, `<=`

Comparação. Funciona para strings assim como para números. Exemplos: `confidence <= 1`, `change > 1712477760`, `gramps_id > "I2015"`

#### `~`, `!~`

Contém ou não contém. Funciona para listas assim como para strings. Exemplos: `gramps_id !~ F00`, `author ~ David`, `family_list ~ "3a16680f7d226e3ac3eefc8b57a"`

#### Sem operador/valor

Se nenhum operador e valor forem fornecidos, o valor é interpretado como um booleano (verdadeiro ou falso). Isso funciona para todos os tipos de propriedades e as regras do Python para conversão para verdadeiro/falso são aplicadas. Por exemplo, a consulta `private` retorna objetos privados; `confidence` retorna objetos onde a confiança é maior que 0; `media_list` retorna objetos com pelo menos uma referência de mídia.

### Valores

Os valores podem ser números ou strings. Se números devem ser interpretados como strings ou caracteres especiais como = estão envolvidos, coloque o valor entre aspas. Exemplos: `gramps_id = F0001`, mas `gramps_id = "0001"`.

## Exemplos comentados

```sql
class = note and private and text.string ~ David
```

Todas as notas privadas que contêm a string "David" em seu texto


```sql
media_list.length >= 10
```

Todos os objetos (de qualquer classe) com 10 ou mais referências de mídia

```sql
class != person and media_list.any.rect
```

Todos os objetos que *não* são uma pessoa, mas têm uma referência de mídia que é parte de uma imagem. Aqui, `media_list.any.rect` significa que para cada um dos itens na lista de mídia, é verificado se a propriedade `rect` (retângulo) tem um valor verdadeiro, significando que é uma lista não vazia. (`media_list.any.rect.length > 0` teria o mesmo efeito.)

```sql
class = family and child_ref_list.length > 10
```

Famílias com mais de 10 filhos.

```sql
class = event and date.modifier = 0 and date.dateval[2] > 2020
```

Eventos onde a data é uma data normal (não um intervalo etc.) e o ano é após 2020.

```sql
note_list.any.get_note.text.string ~ "David"
```

Todos os objetos com pelo menos uma nota que contém a string "David" em seu texto.


```sql
class = family and child_ref_list.all.ref.get_person.gender = 0 and child_ref_list.length = 3
```

Todas as famílias com três filhas.


## Lista completa de Propriedades do Gramps

Para uma lista completa de propriedades do Gramps, veja a [documentação GQL](https://github.com/DavidMStraub/gramps-ql#full-list-of-gramps-properties).
