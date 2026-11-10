# Filtrare utilizzando il Gramps Object Query Language

Le [visualizzazioni dell'elenco degli oggetti](lists.md) (persone, famiglie, eventi, ...) e l'[elenco delle attività](tasks.md) hanno un campo di filtro per espressioni nel [Gramps Object Query Language](https://github.com/DavidMStraub/gramps-object-query-language) (GOQL).

Per utilizzarlo, apri il pannello di filtro, digita un'espressione nel campo **GOQL** e premi Invio (o fai clic su **Applica**). L'elenco è filtrato dall'espressione, oltre a qualsiasi altro filtro attivo. Se l'espressione è non valida, il campo è contrassegnato come errore.

L'espressione si applica sempre agli oggetti dell'elenco in cui ti trovi: nell'elenco Persone, `cognome == 'Smith'` trova le persone con il cognome Smith.

!!! nota
    Il campo GOQL richiede Gramps Web API 3.24 o versioni successive.

## Sintassi

Un'espressione GOQL assomiglia a una condizione nel linguaggio di programmazione Python. Non è necessario conoscere Python per utilizzarlo: gli esempi qui sotto coprono la maggior parte delle esigenze.

### Confronti

Un confronto ha la forma `campo operatore valore`, ad esempio `cognome == 'Smith'`.

Operatore | Significato
---------|--------
`==` | è uguale a
`!=` | non è uguale a
`<`, `<=` | è minore di, minore o uguale a (precedente, più piccolo)
`>`, `>=` | è maggiore di, maggiore o uguale a (successivo, più grande)
`in [ ... ]` | è uno dei valori elencati, ad es. `cognome in ['Meyer', 'Maier']`
`not in [ ... ]` | non è nessuno dei valori elencati
`'testo' in campo` | il campo contiene il testo, ad es. `'mill' in cognome`
`is None` | il campo è vuoto o non esiste, ad es. `death.date.sortval is None`

Il testo va tra virgolette singole o doppie (`'Smith'`), i numeri no (`1850`). I confronti possono essere concatenati, ad es. `Date('1850') <= birth.date.sortval < Date('1900')`.

### Combinare condizioni

Le condizioni possono essere combinate con `and` e `or`, e invertite con `not`. `and` ha la precedenza su `or`; usa le parentesi per raggruppare le condizioni:

```python
(gender == Person.MALE and cognome == 'Smith') or nome == 'Mary'
```

### Modelli di testo

- `like(campo, 'modello')` corrisponde a un modello in cui `%` sta per qualsiasi testo e `_` per un singolo carattere, ad es. `like(nome, 'J%')` per tutti i nomi che iniziano con "J".
- `regex(campo, 'modello')` corrisponde a una [espressione regolare](https://en.wikipedia.org/wiki/Regular_expression), ad es. `regex(cognome, '^M[ae][iy]er$')`.

`like` e `'testo' in campo` ignorano maiuscole e minuscole (su SQLite, questo si applica solo alle lettere A–Z senza accenti). `regex` è sensibile alle maiuscole.

### Campi

Un campo è il nome di una proprietà dell'oggetto, come `gender` o `gramps_id`, o un percorso a una proprietà annidata, come `primary_name.first_name` o `primary_name.surname_list[0].surname`. Le parentesi quadre selezionano un elemento di un elenco in base alla sua posizione, a partire da 0. Le proprietà disponibili sono quelle del [modello di dati di Gramps](https://gramps-project.org/wiki/index.php/Gramps_Data_Model). Se un campo non esiste, il messaggio di errore elenca i campi che esistono.

Sono disponibili alcuni scorciatoie:

- Le persone hanno `given_name` e `surname`, il nome e il cognome del nome principale.
- Le persone hanno `birth` e `death`, i loro eventi di nascita e morte, ad es. `birth.date.sortval` o `death.place.name.value`.
- Le famiglie hanno `father` e `mother`, ad es. `father.surname == 'Smith'`.
- Gli eventi hanno `place`, le citazioni hanno `source`, e i luoghi hanno `enclosed_by`, il luogo circostante.

Questi possono essere concatenati, ad es. `father.birth.place.name.value` nell'elenco delle Famiglie. Due campi possono anche essere confrontati tra loro, ad es. `father.surname == mother.surname`.

### Elenchi di oggetti correlati

`any(collezione, condizione)` corrisponde se almeno un elemento di una collezione soddisfa la condizione, e `len(collezione)` conta gli elementi. Senza una condizione, `any(collezione)` corrisponde se la collezione non è vuota. Le collezioni sono:

- su quasi ogni oggetto: `notes`, `citations`, `media`, e `tags`
- sulle persone: `events`, `families` (come partner), `parent_families` (come bambino), e `associations`
- sulle famiglie: `children`
- su tutti gli oggetti: `backlinks`, gli oggetti che si riferiscono ad esso, che possono essere testati per il loro tipo con `_class`, ad es. `any(backlinks, _class == 'Person')`

`any` e `len` funzionano anche per elenchi memorizzati nell'oggetto stesso, come `alternate_names` o `primary_name.surname_list`.

### Costanti e tipi

I valori fissi di Gramps sono disponibili come costanti, come `Person.MALE`, `Person.FEMALE`, `Person.UNKNOWN`, o i livelli di fiducia `Citation.CONF_VERY_LOW` a `Citation.CONF_VERY_HIGH`. I tipi sono confrontati dal loro `value` con costanti come `EventType.BIRTH`, `FamilyRelType.MARRIED`, `NameType.BIRTH`, `PlaceType.VILLAGE`, o `RepositoryType.ARCHIVE`:

```python
type.value == EventType.BAPTISM
```

I tipi personalizzati che hai inserito tu stesso non hanno una costante propria.

### Date

`Date('...')` trasforma una data scritta come testo in un valore che può essere confrontato con il `sortval` di una data, ad es. `birth.date.sortval < Date('1800')`.

Il `sortval` è un singolo punto nel tempo e ignora il tipo e la qualità di una data: "prima del 1800", "circa 1800" e "1800" hanno tutti lo stesso `sortval`, e per un intervallo o un periodo è l'inizio. Per tenerne conto, confronta il `modifier` o la `quality` della data con costanti come `Date.MOD_ABOUT`, `Date.MOD_BEFORE`, `Date.MOD_AFTER`, `Date.MOD_RANGE`, `Date.MOD_SPAN`, o `Date.QUAL_ESTIMATED`:

```python
date.modifier == Date.MOD_ABOUT
```

## Esempi commentati

Elenco delle persone:

```python
gender == Person.FEMALE and like(given_name, 'Mar%')
```

Donne il cui nome inizia con "Mar".

```python
Date('1850') <= birth.date.sortval < Date('1900')
```

Persone nate dal 1850 al 1899.

```python
birth.place.name.value == death.place.name.value
```

Persone nate e morte in un luogo con lo stesso nome.

```python
not any(notes)
```

Persone senza note.

```python
any(events, type.value == EventType.BURIAL)
```

Persone con un evento di sepoltura.

```python
any(alternate_names, surname_list[0].surname == 'Meyer')
```

Persone con un nome alternativo con il cognome Meyer.

Elenco delle famiglie:

```python
len(children) > 10
```

Famiglie con più di 10 figli.

```python
len(children, gender == Person.FEMALE) == 3
```

Famiglie con tre figlie.

```python
mother.death.date.sortval < father.death.date.sortval
```

Famiglie in cui la madre è morta prima del padre.

Elenco degli eventi:

```python
type.value == EventType.BAPTISM and place.name.value == 'Berlin'
```

Battesimi in un luogo chiamato Berlino.

Elenco delle citazioni:

```python
confidence >= Citation.CONF_HIGH
```

Citazioni con alta o altissima fiducia.

Elenco delle note:

```python
'David' in text.string and private == True
```

Note private che contengono "David".

```python
not any(backlinks)
```

Note che non sono collegate a nessun oggetto.

## Riferimento completo

Per il riferimento completo del linguaggio, vedere la [documentazione GOQL](https://github.com/DavidMStraub/gramps-object-query-language/blob/main/docs/where_expr.md).
