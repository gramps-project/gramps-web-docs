# Filtrer en utilisant le Gramps Object Query Language

Les [vues de liste d'objets](lists.md) (personnes, familles, événements, ...) et la [liste des tâches](tasks.md) ont un champ de filtre pour les expressions dans le [Gramps Object Query Language](https://github.com/DavidMStraub/gramps-object-query-language) (GOQL).

Pour l'utiliser, ouvrez le panneau de filtre, tapez une expression dans le champ **GOQL** et appuyez sur Entrée (ou cliquez sur **Appliquer**). La liste est filtrée par l'expression, en plus de tous les autres filtres actifs. Si l'expression est invalide, le champ est marqué comme une erreur.

L'expression s'applique toujours aux objets de la liste dans laquelle vous vous trouvez : dans la liste des personnes, `surname == 'Smith'` trouve les personnes portant le nom de famille Smith.

!!! note
    Le champ GOQL nécessite l'API Web Gramps 3.24 ou plus récent.

## Syntaxe

Une expression GOQL ressemble à une condition dans le langage de programmation Python. Vous n'avez pas besoin de connaître Python pour l'utiliser – les exemples ci-dessous couvrent la plupart des besoins.

### Comparaisons

Une comparaison a la forme `champ opérateur valeur`, par exemple `surname == 'Smith'`.

Opérateur | Signification
---------|--------
`==` | est égal à
`!=` | n'est pas égal à
`<`, `<=` | est inférieur à, inférieur ou égal à (plus tôt, plus petit)
`>`, `>=` | est supérieur à, supérieur ou égal à (plus tard, plus grand)
`in [ ... ]` | est l'une des valeurs listées, par exemple `surname in ['Meyer', 'Maier']`
`not in [ ... ]` | n'est aucune des valeurs listées
`'text' in field` | le champ contient le texte, par exemple `'mill' in surname`
`is None` | le champ est vide ou n'existe pas, par exemple `death.date.sortval is None`

Le texte doit être entre guillemets simples ou doubles (`'Smith'`), les nombres ne le sont pas (`1850`). Les comparaisons peuvent être enchaînées, par exemple `Date('1850') <= birth.date.sortval < Date('1900')`.

### Combinaison de conditions

Les conditions peuvent être combinées avec `and` et `or`, et inversées avec `not`. `and` a la priorité sur `or` ; utilisez des parenthèses pour regrouper les conditions :

```python
(gender == Person.MALE and surname == 'Smith') or given_name == 'Mary'
```

### Modèles de texte

- `like(field, 'pattern')` correspond à un modèle dans lequel `%` représente n'importe quel texte et `_` pour un seul caractère, par exemple `like(given_name, 'J%')` pour tous les prénoms commençant par "J".
- `regex(field, 'pattern')` correspond à une [expression régulière](https://en.wikipedia.org/wiki/Regular_expression), par exemple `regex(surname, '^M[ae][iy]er$')`.

`like` et `'text' in field` ignorent la casse (sur SQLite, cela ne s'applique qu'aux lettres A–Z sans accents). `regex` est sensible à la casse.

### Champs

Un champ est le nom d'une propriété de l'objet, comme `gender` ou `gramps_id`, ou un chemin vers une propriété imbriquée, comme `primary_name.first_name` ou `primary_name.surname_list[0].surname`. Les crochets sélectionnent un élément d'une liste par sa position, en commençant à 0. Les propriétés disponibles sont celles du [modèle de données Gramps](https://gramps-project.org/wiki/index.php/Gramps_Data_Model). Si un champ n'existe pas, le message d'erreur liste les champs qui existent.

Quelques raccourcis sont disponibles :

- Les personnes ont `given_name` et `surname`, le prénom et le nom de famille du nom principal.
- Les personnes ont `birth` et `death`, leurs événements de naissance et de décès, par exemple `birth.date.sortval` ou `death.place.name.value`.
- Les familles ont `father` et `mother`, par exemple `father.surname == 'Smith'`.
- Les événements ont `place`, les citations ont `source`, et les lieux ont `enclosed_by`, le lieu englobant.

Ceci peut être enchaîné, par exemple `father.birth.place.name.value` dans la liste des familles. Deux champs peuvent également être comparés entre eux, par exemple `father.surname == mother.surname`.

### Listes d'objets associés

`any(collection, condition)` correspond si au moins un élément d'une collection répond à la condition, et `len(collection)` compte les éléments. Sans condition, `any(collection)` correspond si la collection n'est pas vide. Les collections sont :

- sur presque tous les objets : `notes`, `citations`, `media`, et `tags`
- sur les personnes : `events`, `families` (en tant que partenaire), `parent_families` (en tant qu'enfant), et `associations`
- sur les familles : `children`
- sur tous les objets : `backlinks`, les objets qui y font référence, qui peuvent être testés pour leur type avec `_class`, par exemple `any(backlinks, _class == 'Person')`

`any` et `len` fonctionnent également pour les listes stockées dans l'objet lui-même, telles que `alternate_names` ou `primary_name.surname_list`.

### Constantes et types

Les valeurs fixes de Gramps sont disponibles en tant que constantes, telles que `Person.MALE`, `Person.FEMALE`, `Person.UNKNOWN`, ou les niveaux de confiance `Citation.CONF_VERY_LOW` à `Citation.CONF_VERY_HIGH`. Les types sont comparés par leur `value` avec des constantes telles que `EventType.BIRTH`, `FamilyRelType.MARRIED`, `NameType.BIRTH`, `PlaceType.VILLAGE`, ou `RepositoryType.ARCHIVE` :

```python
type.value == EventType.BAPTISM
```

Les types personnalisés que vous avez saisis vous-même n'ont pas de constante propre.

### Dates

`Date('...')` transforme une date écrite sous forme de texte en une valeur qui peut être comparée avec le `sortval` d'une date, par exemple `birth.date.sortval < Date('1800')`.

Le `sortval` est un point unique dans le temps et ignore le type et la qualité d'une date : "avant 1800", "environ 1800" et "1800" ont tous le même `sortval`, et pour une plage ou un intervalle, c'est le début. Pour en tenir compte, comparez le `modifier` ou la `quality` de la date avec des constantes telles que `Date.MOD_ABOUT`, `Date.MOD_BEFORE`, `Date.MOD_AFTER`, `Date.MOD_RANGE`, `Date.MOD_SPAN`, ou `Date.QUAL_ESTIMATED` :

```python
date.modifier == Date.MOD_ABOUT
```

## Exemples commentés

Liste des personnes :

```python
gender == Person.FEMALE and like(given_name, 'Mar%')
```

Femmes dont le prénom commence par "Mar".

```python
Date('1850') <= birth.date.sortval < Date('1900')
```

Personnes nées entre 1850 et 1899.

```python
birth.place.name.value == death.place.name.value
```

Personnes nées et décédées dans un lieu portant le même nom.

```python
not any(notes)
```

Personnes sans notes.

```python
any(events, type.value == EventType.BURIAL)
```

Personnes ayant un événement d'inhumation.

```python
any(alternate_names, surname_list[0].surname == 'Meyer')
```

Personnes ayant un nom alternatif avec le nom de famille Meyer.

Liste des familles :

```python
len(children) > 10
```

Familles avec plus de 10 enfants.

```python
len(children, gender == Person.FEMALE) == 3
```

Familles avec trois filles.

```python
mother.death.date.sortval < father.death.date.sortval
```

Familles dans lesquelles la mère est décédée avant le père.

Liste des événements :

```python
type.value == EventType.BAPTISM and place.name.value == 'Berlin'
```

Baptêmes dans un lieu nommé Berlin.

Liste des citations :

```python
confidence >= Citation.CONF_HIGH
```

Citations avec une confiance élevée ou très élevée.

Liste des notes :

```python
'David' in text.string and private == True
```

Notes privées contenant "David".

```python
not any(backlinks)
```

Notes qui ne sont attachées à aucun objet.

## Référence complète

Pour la référence complète du langage, consultez la [documentation GOQL](https://github.com/DavidMStraub/gramps-object-query-language/blob/main/docs/where_expr.md).
