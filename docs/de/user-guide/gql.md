# Filter mit der Gramps Abfragesprache

Die Objektlistenansichten (Personen, Familien, Ereignisse, ...) haben einen optionalen erweiterten Filtermodus, der auf der [Gramps Abfragesprache](https://github.com/DavidMStraub/gramps-ql) (GQL) basiert.

Um ihn zu verwenden, geben Sie eine Abfrage in GQL-Syntax ein und drücken Sie die Eingabetaste (oder klicken Sie auf die Schaltfläche "Anwenden"). Die Ansicht wird durch die Abfrage gefiltert. Wenn die Abfrage ungültig ist, wird der Rahmen des Eingabefelds rot.

Die GQL-Syntax wird im Folgenden beschrieben, kopiert aus der GQL-Dokumentation.

## Syntax

Eine GQL-Abfrage ist eine Zeichenkette, die aus Aussagen der Form `Eigenschaft Operator Wert` besteht, die optional mit den Schlüsselwörtern `und` und `oder` sowie Klammern kombiniert werden kann.

### Eigenschaften

#### `class`

Filtert nach der Gramps-Objektklasse und kann eine der folgenden sein: `person`, `family`, `event`, `place`, `citation`, `source`, `repository`, `media` oder `note`.

#### Objekt-Eigenschaften

GQL unterstützt die Abfrage von verschachtelten Eigenschaften von Gramps-Objekten, z.B. `primary_name.date.calendar`. Siehe unten für eine vollständige Liste der Eigenschaften – siehe auch [Gramps-Datenmodell](https://gramps-project.org/wiki/index.php/Gramps_Data_Model).

#### Listenelemente nach Index

Einzelne Elemente in listenähnlichen Eigenschaften können durch den Positionsindex in eckigen Klammern zugegriffen werden. Dies kann mit verschachtelten Eigenschaften kombiniert werden, z.B. `primary_name.surname_list[0].surname`.

#### `length`

Dies ist eine spezielle Eigenschaft, die die Länge einer array-ähnlichen Gramps-Eigenschaft zurückgibt, z.B. `media_list.length > 0`, um Objekte mit Medienreferenzen zu erhalten.

#### `all`, `any`

Zwei weitere spezielle Eigenschaften für array-ähnliche Gramps-Eigenschaften. `all` erfordert, dass eine Bedingung auf alle Elemente der Liste zutrifft, `any` erfordert, dass sie auf mindestens ein Element zutrifft. Beide Eigenschaften können vor und nach anderen Eigenschaften kombiniert werden. Beispiele: `media_list.any.citation_list.length > 0`, um Objekte mit Medienreferenzen zurückzugeben, die Zitationen haben; `media_list.all.citation_list.length = 0`, um Objekte zurückzugeben, bei denen alle Medienobjekte keine Zitationen haben.

#### Array-Index

Ein numerischer Array-Index kann verwendet werden, um auf spezifische Elemente einer Liste zuzugreifen, z.B. `child_ref_list[0]` für das erste Kind.

#### `get_person`, usw.

Während alle vorhergehenden Eigenschaften auf ein einzelnes Gramps-Objekt verweisen, ist es auch möglich, nach verschiedenen Objekten zu filtern, die durch das ursprüngliche Objekt referenziert werden. Zum Beispiel hat ein Ereignis einen Platz-Handle in seiner `place`-Eigenschaft. Mit der Pseudo-Eigenschaft `get_place` wechselt GQL zu den Eigenschaften dieses Objekts. Zum Beispiel ist es möglich, nach `class = event and place.get_place.name.value ~ York` zu suchen. Dies kann auch mit `any` oder `all` kombiniert werden, z.B. `class = person and event_ref_list.any.ref.get_event.description ~ farmer`.

### Operatoren

#### `=`, `!=`

Gleichheit oder Ungleichheit. Beispiele: `class = person`, `class != family`

#### `>`, `>=`, `<`, `<=`

Vergleich. Funktioniert sowohl für Strings als auch für Zahlen. Beispiele: `confidence <= 1`, `change > 1712477760`, `gramps_id > "I2015"`

#### `~`, `!~`

Enthält oder enthält nicht. Funktioniert sowohl für Listen als auch für Strings. Beispiele: `gramps_id !~ F00`, `author ~ David`, `family_list ~ "3a16680f7d226e3ac3eefc8b57a"`

#### Kein Operator/Wert

Wenn kein Operator und Wert angegeben sind, wird der Wert als boolesch (true oder false) interpretiert. Dies funktioniert für alle Arten von Eigenschaften und die Python-Regeln für die Umwandlung in true/false werden angewendet. Zum Beispiel gibt die Abfrage `private` private Objekte zurück; `confidence` gibt Objekte zurück, bei denen das Vertrauen größer als 0 ist; `media_list` gibt Objekte mit mindestens einer Medienreferenz zurück.

### Werte

Werte können Zahlen oder Strings sein. Wenn Zahlen als Strings interpretiert werden sollen oder spezielle Zeichen wie = beteiligt sind, schließen Sie den Wert in Anführungszeichen ein. Beispiele: `gramps_id = F0001`, aber `gramps_id = "0001"`.

## Kommentierte Beispiele

```sql
class = note and private and text.string ~ David
```

Alle privaten Notizen, die den String "David" in ihrem Text enthalten


```sql
media_list.length >= 10
```

Alle Objekte (beliebiger Klasse) mit 10 oder mehr Medienreferenzen

```sql
class != person and media_list.any.rect
```

Alle Objekte, die *keine* Person sind, aber eine Medienreferenz haben, die Teil eines Bildes ist. Hier bedeutet `media_list.any.rect`, dass für jedes der Elemente in der Medienliste überprüft wird, ob die `rect` (Rechteck)-Eigenschaft einen wahrheitsgemäßen Wert hat, was bedeutet, dass es sich um eine nicht leere Liste handelt. (`media_list.any.rect.length > 0` hätte denselben Effekt.)

```sql
class = family and child_ref_list.length > 10
```

Familien mit mehr als 10 Kindern.

```sql
class = event and date.modifier = 0 and date.dateval[2] > 2020
```

Ereignisse, bei denen das Datum ein normales Datum (nicht ein Bereich usw.) ist und das Jahr nach 2020 liegt.

```sql
note_list.any.get_note.text.string ~ "David"
```

Alle Objekte mit mindestens einer Notiz, die den String "David" in ihrem Text enthält.


```sql
class = family and child_ref_list.all.ref.get_person.gender = 0 and child_ref_list.length = 3
```

Alle Familien mit drei Töchtern.


## Vollständige Liste der Gramps-Eigenschaften

Für eine vollständige Liste der Gramps-Eigenschaften siehe die [GQL-Dokumentation](https://github.com/DavidMStraub/gramps-ql#full-list-of-gramps-properties).
