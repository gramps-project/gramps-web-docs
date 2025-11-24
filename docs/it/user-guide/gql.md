# Filtro utilizzando il Linguaggio di Query di Gramps

Le visualizzazioni dell'elenco degli oggetti (persone, famiglie, eventi, ...) hanno una modalità di filtro avanzata opzionale basata sul [Linguaggio di Query di Gramps](https://github.com/DavidMStraub/gramps-ql) (GQL).

Per utilizzarlo, digita una query in sintassi GQL e premi invio (o fai clic sul pulsante "applica"). La visualizzazione sarà filtrata dalla query. Se la query non è valida, il bordo del campo di input diventa rosso.

La sintassi GQL è descritta di seguito, copiata dalla documentazione GQL.

## Sintassi

Una query GQL è una stringa composta da dichiarazioni della forma `proprietà operatore valore`, eventualmente combinata con le parole chiave `and` e `or` così come con le parentesi.

### Proprietà

#### `class`

Filtra per la classe di oggetti Gramps e può essere uno di `person`, `family`, `event`, `place`, `citation`, `source`, `repository`, `media`, o `note`.

#### Proprietà degli oggetti

GQL supporta la query delle proprietà annidate degli oggetti Gramps, ad esempio `primary_name.date.calendar`. Vedi di seguito per un elenco completo delle proprietà – vedi anche [Modello di Dati di Gramps](https://gramps-project.org/wiki/index.php/Gramps_Data_Model).

#### Elementi dell'elenco per indice

Gli elementi individuali nelle proprietà simili a un elenco possono essere accessibili tramite indice posizionale tra parentesi quadre. Questo può essere combinato con proprietà annidate, ad esempio `primary_name.surname_list[0].surname`.

#### `length`

Questa è una proprietà speciale che restituisce la lunghezza di una proprietà Gramps simile a un array, ad esempio `media_list.length > 0` per ottenere oggetti con riferimenti ai media.

#### `all`, `any`

Due ulteriori proprietà speciali per le proprietà Gramps simili a un array. `all` richiede che una condizione si applichi a tutti gli elementi dell'elenco, `any` richiede che si applichi ad almeno un elemento. Entrambe le proprietà possono essere combinate con altre proprietà prima e dopo. Esempi: `media_list.any.citation_list.length > 0` per restituire oggetti con riferimenti ai media che hanno citazioni; `media_list.all.citation_list.length = 0` per restituire oggetti in cui tutti gli oggetti media non hanno citazioni.

#### Indice dell'array

Un indice numerico dell'array può essere utilizzato per accedere a elementi specifici di un elenco, ad esempio `child_ref_list[0]` per il primo bambino.

#### `get_person`, ecc.

Mentre tutte le proprietà precedenti si riferiscono a un singolo oggetto Gramps, è anche possibile filtrare su oggetti diversi a cui si fa riferimento dall'oggetto iniziale. Ad esempio, un evento ha un handle di luogo nella sua proprietà `place`. Utilizzando la pseudo-proprietà `get_place`, GQL passa alle proprietà di quell'oggetto. Ad esempio, è possibile cercare `class = event and place.get_place.name.value ~ York`. Questo può anche essere combinato con `any` o `all`, ad esempio `class = person and event_ref_list.any.ref.get_event.description ~ farmer`.

### Operatori

#### `=`, `!=`

Uguaglianza o disuguaglianza. Esempi: `class = person`, `class != family`

#### `>`, `>=`, `<`, `<=`

Confronto. Funziona sia per stringhe che per numeri. Esempi: `confidence <= 1`, `change > 1712477760`, `gramps_id > "I2015"`

#### `~`, `!~`

Contiene o non contiene. Funziona per elenchi così come per stringhe. Esempi: `gramps_id !~ F00`, `author ~ David`, `family_list ~ "3a16680f7d226e3ac3eefc8b57a"`

#### Nessun operatore/valore

Se non viene fornito alcun operatore e valore, il valore è interpretato come booleano (true o false). Questo funziona per
tutti i tipi di proprietà e si applicano le regole di Python per il casting a true/false. Ad esempio, la query `private` restituisce oggetti privati; `confidence` restituisce oggetti in cui la fiducia è maggiore di 0; `media_list` restituisce oggetti con almeno un riferimento ai media.

### Valori

I valori possono essere numeri o stringhe. Se i numeri devono essere interpretati come stringhe o se sono coinvolti caratteri speciali come =, racchiudi il valore tra virgolette. Esempi: `gramps_id = F0001`, ma `gramps_id = "0001"`.

## Esempi commentati

```sql
class = note and private and text.string ~ David
```

Tutte le note private che contengono la stringa "David" nel loro testo


```sql
media_list.length >= 10
```

Tutti gli oggetti (di qualsiasi classe) con 10 o più riferimenti ai media

```sql
class != person and media_list.any.rect
```

Tutti gli oggetti che *non* sono una persona ma hanno un riferimento ai media che è parte di un'immagine. Qui, `media_list.any.rect` significa che per ciascuno degli elementi nell'elenco media, viene controllato se la proprietà `rect` (rettangolo) ha un valore veritiero, il che significa che è un elenco non vuoto. (`media_list.any.rect.length > 0` avrebbe lo stesso effetto.)

```sql
class = family and child_ref_list.length > 10
```

Famiglie con più di 10 figli.

```sql
class = event and date.modifier = 0 and date.dateval[2] > 2020
```

Eventi in cui la data è una data normale (non un intervallo ecc.) e l'anno è dopo il 2020.

```sql
note_list.any.get_note.text.string ~ "David"
```

Tutti gli oggetti con almeno una nota che contiene la stringa "David" nel loro testo.


```sql
class = family and child_ref_list.all.ref.get_person.gender = 0 and child_ref_list.length = 3
```

Tutte le famiglie con tre figlie.


## Elenco completo delle Proprietà di Gramps

Per un elenco completo delle proprietà di Gramps, vedere la [documentazione GQL](https://github.com/DavidMStraub/gramps-ql#full-list-of-gramps-properties).
