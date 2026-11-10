# Filter mit der Gramps Object Query Language verwenden

Die [Objektlistenansichten](lists.md) (Personen, Familien, Ereignisse, ...) und die [Aufgabenliste](tasks.md) haben ein Filterfeld für Ausdrücke in der [Gramps Object Query Language](https://github.com/DavidMStraub/gramps-object-query-language) (GOQL).

Um es zu verwenden, öffnen Sie das Filterpanel, geben Sie einen Ausdruck im **GOQL**-Feld ein und drücken Sie die Eingabetaste (oder klicken Sie auf **Anwenden**). Die Liste wird basierend auf dem Ausdruck gefiltert, zusätzlich zu allen anderen aktiven Filtern. Wenn der Ausdruck ungültig ist, wird das Feld als Fehler markiert.

Der Ausdruck gilt immer für die Objekte der Liste, in der Sie sich befinden: In der Personenliste findet `surname == 'Smith'` die Personen mit dem Nachnamen Smith.

!!! Hinweis
    Das GOQL-Feld benötigt die Gramps Web API 3.24 oder neuer.

## Syntax

Ein GOQL-Ausdruck sieht aus wie eine Bedingung in der Programmiersprache Python. Sie müssen Python nicht kennen, um es zu verwenden – die folgenden Beispiele decken die meisten Bedürfnisse ab.

### Vergleiche

Ein Vergleich hat die Form `field operator value`, zum Beispiel `surname == 'Smith'`.

Operator | Bedeutung
---------|--------
`==` | ist gleich
`!=` | ist nicht gleich
`<`, `<=` | ist kleiner als, kleiner oder gleich (früher, kleiner)
`>`, `>=` | ist größer als, größer oder gleich (später, größer)
`in [ ... ]` | ist einer der aufgelisteten Werte, z.B. `surname in ['Meyer', 'Maier']`
`not in [ ... ]` | ist keiner der aufgelisteten Werte
`'text' in field` | das Feld enthält den Text, z.B. `'mill' in surname`
`is None` | das Feld ist leer oder existiert nicht, z.B. `death.date.sortval is None`

Text wird in einfachen oder doppelten Anführungszeichen angegeben (`'Smith'`), Zahlen nicht (`1850`). Vergleiche können verkettet werden, z.B. `Date('1850') <= birth.date.sortval < Date('1900')`.

### Bedingungen kombinieren

Bedingungen können mit `and` und `or` kombiniert und mit `not` invertiert werden. `and` hat Vorrang vor `or`; verwenden Sie Klammern, um Bedingungen zu gruppieren:

```python
(gender == Person.MALE and surname == 'Smith') or given_name == 'Mary'
```

### Textmuster

- `like(field, 'pattern')` entspricht einem Muster, bei dem `%` für beliebigen Text und `_` für ein einzelnes Zeichen steht, z.B. `like(given_name, 'J%')` für alle Vornamen, die mit "J" beginnen.
- `regex(field, 'pattern')` entspricht einem [regulären Ausdruck](https://de.wikipedia.org/wiki/Regulärer_Ausdruck), z.B. `regex(surname, '^M[ae][iy]er$')`.

`like` und `'text' in field` ignorieren Groß- und Kleinschreibung (in SQLite gilt dies nur für die Buchstaben A–Z ohne Akzentzeichen). `regex` ist groß- und kleinschreibungssensitiv.

### Felder

Ein Feld ist der Name einer Eigenschaft des Objekts, wie `gender` oder `gramps_id`, oder ein Pfad zu einer verschachtelten Eigenschaft, wie `primary_name.first_name` oder `primary_name.surname_list[0].surname`. Die eckigen Klammern wählen ein Element einer Liste nach seiner Position aus, beginnend bei 0. Die verfügbaren Eigenschaften sind die des [Gramps-Datenmodells](https://gramps-project.org/wiki/index.php/Gramps_Data_Model). Wenn ein Feld nicht existiert, listet die Fehlermeldung die vorhandenen Felder auf.

Einige Abkürzungen sind verfügbar:

- Personen haben `given_name` und `surname`, den Vornamen und Nachnamen des Hauptnamens.
- Personen haben `birth` und `death`, ihre Geburts- und Sterbeereignisse, z.B. `birth.date.sortval` oder `death.place.name.value`.
- Familien haben `father` und `mother`, z.B. `father.surname == 'Smith'`.
- Ereignisse haben `place`, Zitationen haben `source`, und Orte haben `enclosed_by`, den umschließenden Ort.

Diese können verkettet werden, z.B. `father.birth.place.name.value` in der Familienliste. Zwei Felder können auch miteinander verglichen werden, z.B. `father.surname == mother.surname`.

### Listen verwandter Objekte

`any(collection, condition)` entspricht, wenn mindestens ein Element einer Sammlung die Bedingung erfüllt, und `len(collection)` zählt die Elemente. Ohne eine Bedingung entspricht `any(collection)`, wenn die Sammlung nicht leer ist. Sammlungen sind:

- auf fast jedem Objekt: `notes`, `citations`, `media` und `tags`
- bei Personen: `events`, `families` (als Partner), `parent_families` (als Kind) und `associations`
- bei Familien: `children`
- bei allen Objekten: `backlinks`, die Objekte, die darauf verweisen, die mit `_class` auf ihren Typ getestet werden können, z.B. `any(backlinks, _class == 'Person')`

`any` und `len` funktionieren auch für Listen, die im Objekt selbst gespeichert sind, wie `alternate_names` oder `primary_name.surname_list`.

### Konstanten und Typen

Feste Werte von Gramps sind als Konstanten verfügbar, wie `Person.MALE`, `Person.FEMALE`, `Person.UNKNOWN` oder die Vertrauensstufen `Citation.CONF_VERY_LOW` bis `Citation.CONF_VERY_HIGH`. Typen werden durch ihren `value` mit Konstanten wie `EventType.BIRTH`, `FamilyRelType.MARRIED`, `NameType.BIRTH`, `PlaceType.VILLAGE` oder `RepositoryType.ARCHIVE` verglichen:

```python
type.value == EventType.BAPTISM
```

Benutzerdefinierte Typen, die Sie selbst eingegeben haben, haben keine eigene Konstante.

### Daten

`Date('...')` wandelt ein als Text geschriebenes Datum in einen Wert um, der mit dem `sortval` eines Datums verglichen werden kann, z.B. `birth.date.sortval < Date('1800')`.

Der `sortval` ist ein einzelner Zeitpunkt und ignoriert den Typ und die Qualität eines Datums: "vor 1800", "um 1800" und "1800" haben alle denselben `sortval`, und für einen Bereich oder eine Spanne ist es der Beginn. Um diese zu berücksichtigen, vergleichen Sie den `modifier` oder die `quality` des Datums mit Konstanten wie `Date.MOD_ABOUT`, `Date.MOD_BEFORE`, `Date.MOD_AFTER`, `Date.MOD_RANGE`, `Date.MOD_SPAN` oder `Date.QUAL_ESTIMATED`:

```python
date.modifier == Date.MOD_ABOUT
```

## Kommentierte Beispiele

Personenliste:

```python
gender == Person.FEMALE and like(given_name, 'Mar%')
```

Frauen, deren Vorname mit "Mar" beginnt.

```python
Date('1850') <= birth.date.sortval < Date('1900')
```

Personen, die zwischen 1850 und 1899 geboren wurden.

```python
birth.place.name.value == death.place.name.value
```

Personen, die an einem Ort mit demselben Namen geboren und gestorben sind.

```python
not any(notes)
```

Personen ohne Notizen.

```python
any(events, type.value == EventType.BURIAL)
```

Personen mit einem Begräbnisereignis.

```python
any(alternate_names, surname_list[0].surname == 'Meyer')
```

Personen mit einem alternativen Namen mit dem Nachnamen Meyer.

Familienliste:

```python
len(children) > 10
```

Familien mit mehr als 10 Kindern.

```python
len(children, gender == Person.FEMALE) == 3
```

Familien mit drei Töchtern.

```python
mother.death.date.sortval < father.death.date.sortval
```

Familien, in denen die Mutter vor dem Vater gestorben ist.

Ereignisliste:

```python
type.value == EventType.BAPTISM and place.name.value == 'Berlin'
```

Taufen an einem Ort namens Berlin.

Zitationsliste:

```python
confidence >= Citation.CONF_HIGH
```

Zitationen mit hoher oder sehr hoher Zuverlässigkeit.

Notizenliste:

```python
'David' in text.string and private == True
```

Private Notizen, die "David" enthalten.

```python
not any(backlinks)
```

Notizen, die an kein Objekt angehängt sind.

## Vollständige Referenz

Für die vollständige Sprachreferenz siehe die [GOQL-Dokumentation](https://github.com/DavidMStraub/gramps-object-query-language/blob/main/docs/where_expr.md).
