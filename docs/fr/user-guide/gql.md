# Filtrer en utilisant le Langage de Requête Gramps

Les vues de liste d'objets (personnes, familles, événements, ...) ont un mode de filtre avancé optionnel basé sur le [Langage de Requête Gramps](https://github.com/DavidMStraub/gramps-ql) (GQL).

Pour l'utiliser, tapez une requête en syntaxe GQL et appuyez sur entrée (ou cliquez sur le bouton "appliquer"). La vue sera filtrée par la requête. Si la requête est invalide, le cadre du champ de saisie devient rouge.

La syntaxe GQL est décrite ci-dessous, copiée de la documentation GQL.

## Syntaxe

Une requête GQL est une chaîne composée d'instructions de la forme `propriété opérateur valeur`, éventuellement combinées avec les mots-clés `et` et `ou` ainsi que des parenthèses.

### Propriétés

#### `class`

Filtre pour la classe d'objet Gramps et peut être l'un de `person`, `family`, `event`, `place`, `citation`, `source`, `repository`, `media`, ou `note`.

#### Propriétés d'objet

GQL prend en charge la requête de propriétés imbriquées des objets Gramps, par exemple `primary_name.date.calendar`. Voir ci-dessous pour une liste complète des propriétés – voir aussi [Modèle de Données Gramps](https://gramps-project.org/wiki/index.php/Gramps_Data_Model).

#### Éléments de liste par index

Les éléments individuels dans des propriétés de type liste peuvent être accessibles par index positionnel entre crochets. Cela peut être combiné avec des propriétés imbriquées, par exemple `primary_name.surname_list[0].surname`.

#### `length`

C'est une propriété spéciale qui retourne la longueur d'une propriété Gramps de type tableau, par exemple `media_list.length > 0` pour obtenir des objets avec des références médias.

#### `all`, `any`

Deux autres propriétés spéciales pour les propriétés Gramps de type tableau. `all` exige qu'une condition s'applique à tous les éléments de la liste, `any` exige qu'elle s'applique à au moins un élément. Les deux propriétés peuvent être combinées avec d'autres propriétés avant et après. Exemples : `media_list.any.citation_list.length > 0` pour retourner des objets avec des références médias qui ont des citations ; `media_list.all.citation_list.length = 0` pour retourner des objets où tous les objets médias n'ont pas de citations.

#### Index de tableau

Un index numérique de tableau peut être utilisé pour accéder à des éléments spécifiques d'une liste, par exemple `child_ref_list[0]` pour le premier enfant.

#### `get_person`, etc.

Alors que toutes les propriétés précédentes se réfèrent à un seul objet Gramps, il est également possible de filtrer sur différents objets référencés par l'objet initial. Par exemple, un événement a un gestionnaire de lieu dans sa propriété `place`. En utilisant la pseudo-propriété `get_place`, GQL passe aux propriétés de cet objet. Par exemple, il est possible de rechercher `class = event and place.get_place.name.value ~ York`. Cela peut également être combiné avec `any` ou `all`, par exemple `class = person and event_ref_list.any.ref.get_event.description ~ farmer`.

### Opérateurs

#### `=`, `!=`

Égalité ou inégalité. Exemples : `class = person`, `class != family`

#### `>`, `>=`, `<`, `<=`

Comparaison. Fonctionne pour les chaînes ainsi que pour les nombres. Exemples : `confidence <= 1`, `change > 1712477760 `, `gramps_id > "I2015"`

#### `~`, `!~`

Contient ou ne contient pas. Fonctionne pour les listes ainsi que pour les chaînes. Exemples : `gramps_id !~ F00`, `author ~ David`, `family_list ~ "3a16680f7d226e3ac3eefc8b57a"`

#### Pas d'opérateur/valeur

Si aucun opérateur et valeur n'est donné, la valeur est interprétée comme un booléen (vrai ou faux). Cela fonctionne pour tous les types de propriétés et les règles Python pour le casting en vrai/faux sont appliquées. Par exemple, la requête `private` retourne des objets privés ; `confidence` retourne des objets où la confiance est supérieure à 0 ; `media_list` retourne des objets avec au moins une référence média.

### Valeurs

Les valeurs peuvent être des nombres ou des chaînes. Si les nombres doivent être interprétés comme des chaînes ou si des caractères spéciaux comme = sont impliqués, entourez la valeur de guillemets. Exemples : `gramps_id = F0001`, mais `gramps_id = "0001"`.

## Exemples commentés

```sql
class = note and private and text.string ~ David
```

Toutes les notes privées qui contiennent la chaîne "David" dans leur texte


```sql
media_list.length >= 10
```

Tous les objets (de n'importe quelle classe) avec 10 références médias ou plus

```sql
class != person and media_list.any.rect
```

Tous les objets qui ne sont *pas* une personne mais ont une référence média qui fait partie d'une image. Ici, `media_list.any.rect` signifie que pour chacun des éléments de la liste des médias, il est vérifié si la propriété `rect` (rectangle) a une valeur véridique, ce qui signifie qu'il s'agit d'une liste non vide. (`media_list.any.rect.length > 0` aurait le même effet.)

```sql
class = family and child_ref_list.length > 10
```

Familles avec plus de 10 enfants.

```sql
class = event and date.modifier = 0 and date.dateval[2] > 2020
```

Événements où la date est une date normale (pas une plage, etc.) et l'année est après 2020.

```sql
note_list.any.get_note.text.string ~ "David"
```

Tous les objets avec au moins une note qui contient la chaîne "David" dans leur texte.


```sql
class = family and child_ref_list.all.ref.get_person.gender = 0 and child_ref_list.length = 3
```

Toutes les familles avec trois filles.


## Liste complète des Propriétés Gramps

Pour une liste complète des propriétés Gramps, voir la [documentation GQL](https://github.com/DavidMStraub/gramps-ql#full-list-of-gramps-properties).
