# Filtrer ved hjælp af Gramps Query Language

Objektlistevisningerne (personer, familier, begivenheder, ...) har en valgfri avanceret filtertilstand baseret på [Gramps Query Language](https://github.com/DavidMStraub/gramps-ql) (GQL).

For at bruge det skal du skrive en forespørgsel i GQL-syntaks og trykke på enter (eller klikke på "anvend" knappen). Visningen vil blive filtreret efter forespørgslen. Hvis forespørgslen er ugyldig, bliver inputfeltets ramme rød.

GQL-syntaksen er beskrevet nedenfor, kopieret fra GQL-dokumentationen.

## Syntaks

En GQL-forespørgsel er en streng sammensat af udsagn af formen `property operator value`, eventuelt kombineret med nøgleordene `and` og `or` samt parenteser.

### Egenskaber

#### `class`

Filtrerer for Gramps objektklasse og kan være en af `person`, `family`, `event`, `place`, `citation`, `source`, `repository`, `media` eller `note`.

#### Objekt egenskaber

GQL understøtter forespørgsler på indlejrede egenskaber af Gramps objekter, f.eks. `primary_name.date.calendar`. Se nedenfor for en fuld liste over egenskaber – se også [Gramps Data Model](https://gramps-project.org/wiki/index.php/Gramps_Data_Model).

#### Listeelementer efter indeks

Individuelle elementer i liste-lignende egenskaber kan tilgås ved positionsindeks i firkantede parenteser. Dette kan kombineres med indlejrede egenskaber, f.eks. `primary_name.surname_list[0].surname`.

#### `length`

Dette er en særlig egenskab, der returnerer længden af en array-lignende Gramps egenskab, f.eks. `media_list.length > 0` for at få objekter med mediereferencer.

#### `all`, `any`

To flere særlige egenskaber for array-lignende Gramps egenskaber. `all` kræver, at en betingelse gælder for alle elementer i listen, `any` kræver, at den gælder for mindst ét element. Begge egenskaber kan kombineres med andre egenskaber før og efter. Eksempler: `media_list.any.citation_list.length > 0` for at returnere objekter med mediereferencer, der har citater; `media_list.all.citation_list.length = 0` for at returnere objekter, hvor alle medieobjekter ikke har citater.

#### Array indeks

Et numerisk array indeks kan bruges til at tilgå specifikke elementer i en liste, f.eks. `child_ref_list[0]` for det første barn.

#### `get_person`, osv.

Mens alle de foregående egenskaber refererer til et enkelt Gramps objekt, er det også muligt at filtrere på forskellige objekter, der refereres til af det oprindelige objekt. For eksempel har en begivenhed et sted-håndtag i sin `place` egenskab. Ved at bruge den pseudo-egenskab `get_place` skifter GQL til egenskaberne for det objekt. For eksempel er det muligt at søge efter `class = event and place.get_place.name.value ~ York`. Dette kan også kombineres med `any` eller `all`, f.eks. `class = person and event_ref_list.any.ref.get_event.description ~ farmer`.

### Operatører

#### `=`, `!=`

Lighed eller ulighed. Eksempler: `class = person`, `class != family`

#### `>`, `>=`, `<`, `<=`

Sammenligning. Fungerer for strenge såvel som tal. Eksempler: `confidence <= 1`, `change > 1712477760 `, `gramps_id > "I2015"`

#### `~`, `!~`

Indeholder eller indeholder ikke. Fungerer for lister såvel som strenge. Eksempler: `gramps_id !~ F00`, `author ~ David`, `family_list ~ "3a16680f7d226e3ac3eefc8b57a"`

#### Ingen operator/værdi

Hvis ingen operator og værdi gives, tolkes værdien som en boolesk (true eller false). Dette fungerer for alle typer egenskaber, og Python-regler for casting til true/false anvendes. For eksempel returnerer forespørgslen `private` private objekter; `confidence` returnerer objekter, hvor tilliden er større end 0; `media_list` returnerer objekter med mindst én mediereference.

### Værdier

Værdier kan være tal eller strenge. Hvis tal skal tolkes som strenge, eller hvis specielle tegn som = er involveret, skal værdien indkapsles i strenge. Eksempler: `gramps_id = F0001`, men `gramps_id = "0001"`.

## Kommenterede eksempler

```sql
class = note and private and text.string ~ David
```

Alle private noter, der indeholder strengen "David" i deres tekst


```sql
media_list.length >= 10
```

Alle objekter (af enhver klasse) med 10 eller flere mediereferencer

```sql
class != person and media_list.any.rect
```

Alle objekter, der *ikke* er en person, men har en mediereference, der er en del af et billede. Her betyder `media_list.any.rect`, at der for hvert af elementerne i medielisten kontrolleres, om `rect` (rektangel) egenskaben har en sand værdi, hvilket betyder, at det er en ikke-tom liste. (`media_list.any.rect.length > 0` ville have samme effekt.)

```sql
class = family and child_ref_list.length > 10
```

Familier med mere end 10 børn.

```sql
class = event and date.modifier = 0 and date.dateval[2] > 2020
```

Begivenheder, hvor datoen er en normal dato (ikke et interval osv.) og året er efter 2020.

```sql
note_list.any.get_note.text.string ~ "David"
```

Alle objekter med mindst én note, der indeholder strengen "David" i deres tekst.


```sql
class = family and child_ref_list.all.ref.get_person.gender = 0 and child_ref_list.length = 3
```

Alle familier med tre døtre.


## Fuld liste over Gramps Egenskaber

For en fuld liste over Gramps egenskaber, se [GQL dokumentationen](https://github.com/DavidMStraub/gramps-ql#full-list-of-gramps-properties).
