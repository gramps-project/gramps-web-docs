# Filtrering ved hjælp af Gramps Object Query Language

De [objektlistevisninger](lists.md) (personer, familier, begivenheder, ...) og [opgavelisten](tasks.md) har et filterfelt til udtryk i [Gramps Object Query Language](https://github.com/DavidMStraub/gramps-object-query-language) (GOQL).

For at bruge det, åbn filterpanelet, skriv et udtryk i **GOQL**-feltet og tryk på Enter (eller klik på **Anvend**). Listen filtreres efter udtrykket, oven på eventuelle andre aktive filtre. Hvis udtrykket er ugyldigt, markeres feltet som en fejl.

Udtrykket gælder altid for objekterne i den liste, du er i: i Personer-listen finder `surname == 'Smith'` personer med efternavnet Smith.

!!! note
    GOQL-feltet kræver Gramps Web API 3.24 eller nyere.

## Syntaks

Et GOQL-udtryk ligner en betingelse i programmeringssproget Python. Du behøver ikke at kende Python for at bruge det – eksemplerne nedenfor dækker de fleste behov.

### Sammenligninger

En sammenligning har formen `felt operator værdi`, for eksempel `surname == 'Smith'`.

Operator | Betydning
---------|--------
`==` | er lig med
`!=` | er ikke lig med
`<`, `<=` | er mindre end, mindre end eller lig med (tidligere, mindre)
`>`, `>=` | er større end, større end eller lig med (senere, større)
`in [ ... ]` | er en af de listede værdier, f.eks. `surname in ['Meyer', 'Maier']`
`not in [ ... ]` | er ingen af de listede værdier
`'text' in felt` | feltet indeholder teksten, f.eks. `'mill' in surname`
`is None` | feltet er tomt eller eksisterer ikke, f.eks. `death.date.sortval is None`

Tekst skal være i enkle eller dobbelte citationstegn (`'Smith'`), tal skal ikke (`1850`). Sammenligninger kan kædes sammen, f.eks. `Date('1850') <= birth.date.sortval < Date('1900')`.

### Kombinering af betingelser

Betingelser kan kombineres med `and` og `or`, og inverteres med `not`. `and` har højere prioritet end `or`; brug parenteser til at gruppere betingelser:

```python
(gender == Person.MALE and surname == 'Smith') or given_name == 'Mary'
```

### Tekstmønstre

- `like(field, 'pattern')` matcher et mønster, hvor `%` står for enhver tekst og `_` for et enkelt tegn, f.eks. `like(given_name, 'J%')` for alle fornavne, der starter med "J".
- `regex(field, 'pattern')` matcher et [regulært udtryk](https://en.wikipedia.org/wiki/Regular_expression), f.eks. `regex(surname, '^M[ae][iy]er$')`.

`like` og `'text' in field` ignorerer store og små bogstaver (på SQLite gælder dette kun for bogstaverne A–Z uden accenter). `regex` er skelnen mellem store og små bogstaver.

### Felter

Et felt er navnet på en egenskab ved objektet, som `gender` eller `gramps_id`, eller en sti til en indlejret egenskab, som `primary_name.first_name` eller `primary_name.surname_list[0].surname`. De firkantede parenteser vælger et element fra en liste efter dets position, der starter fra 0. De tilgængelige egenskaber er dem fra [Gramps datamodel](https://gramps-project.org/wiki/index.php/Gramps_Data_Model). Hvis et felt ikke eksisterer, opregner fejlmeddelelsen de felter, der gør.

Nogle genveje er tilgængelige:

- Personer har `given_name` og `surname`, fornavnet og efternavnet på det primære navn.
- Personer har `birth` og `death`, deres fødsels- og dødsbegivenheder, f.eks. `birth.date.sortval` eller `death.place.name.value`.
- Familier har `father` og `mother`, f.eks. `father.surname == 'Smith'`.
- Begivenheder har `place`, citater har `source`, og steder har `enclosed_by`, det indkapslende sted.

Disse kan kædes sammen, f.eks. `father.birth.place.name.value` i Familier-listen. To felter kan også sammenlignes med hinanden, f.eks. `father.surname == mother.surname`.

### Lister over relaterede objekter

`any(collection, condition)` matcher, hvis mindst ét element i en samling opfylder betingelsen, og `len(collection)` tæller elementerne. Uden en betingelse matcher `any(collection)`, hvis samlingen ikke er tom. Samlinger er:

- på næsten hvert objekt: `notes`, `citations`, `media`, og `tags`
- på personer: `events`, `families` (som partner), `parent_families` (som barn), og `associations`
- på familier: `children`
- på alle objekter: `backlinks`, de objekter, der henviser til det, som kan testes for deres type med `_class`, f.eks. `any(backlinks, _class == 'Person')`

`any` og `len` fungerer også for lister, der er gemt i objektet selv, såsom `alternate_names` eller `primary_name.surname_list`.

### Konstanter og typer

Faste værdier fra Gramps er tilgængelige som konstanter, såsom `Person.MALE`, `Person.FEMALE`, `Person.UNKNOWN`, eller tillidsniveauerne `Citation.CONF_VERY_LOW` til `Citation.CONF_VERY_HIGH`. Typer sammenlignes efter deres `value` med konstanter som `EventType.BIRTH`, `FamilyRelType.MARRIED`, `NameType.BIRTH`, `PlaceType.VILLAGE`, eller `RepositoryType.ARCHIVE`:

```python
type.value == EventType.BAPTISM
```

Brugerdefinerede typer, som du selv har indtastet, har ikke en konstant af deres egen.

### Datoer

`Date('...')` omdanner en dato skrevet som tekst til en værdi, der kan sammenlignes med `sortval` af en dato, f.eks. `birth.date.sortval < Date('1800')`.

`sortval` er et enkelt tidspunkt og ignorerer typen og kvaliteten af en dato: "før 1800", "omkring 1800" og "1800" har alle den samme `sortval`, og for et interval eller spænd er det starten. For at tage disse i betragtning, sammenlign `modifier` eller `quality` af datoen med konstanter som `Date.MOD_ABOUT`, `Date.MOD_BEFORE`, `Date.MOD_AFTER`, `Date.MOD_RANGE`, `Date.MOD_SPAN`, eller `Date.QUAL_ESTIMATED`:

```python
date.modifier == Date.MOD_ABOUT
```

## Kommenterede eksempler

Personer liste:

```python
gender == Person.FEMALE and like(given_name, 'Mar%')
```

Kvinder hvis fornavn starter med "Mar".

```python
Date('1850') <= birth.date.sortval < Date('1900')
```

Personer født fra 1850 til 1899.

```python
birth.place.name.value == death.place.name.value
```

Personer der blev født og døde i et sted med samme navn.

```python
not any(notes)
```

Personer uden noter.

```python
any(events, type.value == EventType.BURIAL)
```

Personer med en begravelsesbegivenhed.

```python
any(alternate_names, surname_list[0].surname == 'Meyer')
```

Personer med et alternativt navn med efternavnet Meyer.

Familier liste:

```python
len(children) > 10
```

Familier med mere end 10 børn.

```python
len(children, gender == Person.FEMALE) == 3
```

Familier med tre døtre.

```python
mother.death.date.sortval < father.death.date.sortval
```

Familier hvor moderen døde før faderen.

Begivenheder liste:

```python
type.value == EventType.BAPTISM and place.name.value == 'Berlin'
```

Dåb i et sted ved navn Berlin.

Citations liste:

```python
confidence >= Citation.CONF_HIGH
```

Citations med høj eller meget høj tillid.

Notes liste:

```python
'David' in text.string and private == True
```

Private noter der indeholder "David".

```python
not any(backlinks)
```

Noter der ikke er knyttet til noget objekt.

## Fuld reference

For den fulde sprogreference, se [GOQL dokumentationen](https://github.com/DavidMStraub/gramps-object-query-language/blob/main/docs/where_expr.md).
