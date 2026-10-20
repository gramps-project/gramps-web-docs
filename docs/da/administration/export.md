## Sikkerhedskopier dit slægtræ

Træejere kan oprette, downloade og gendanne komplette sikkerhedskopier af træet – inklusive dets indstillinger og brugere – i sektionen [Sikkerhedskopier](settings.md#backups) under administrationsindstillingerne.

Alternativt, for kun at oprette en sikkerhedskopi af slægtrædataene, skal du åbne eksport-siden i Gramps Web og vælge Gramps XML-formatet.

Ved at klikke på "eksport" genereres filen, og downloadet starter, når det er klar.

Bemærk, at hvis din Gramps Web-bruger ikke har tilladelse til at se private optegnelser, vil eksporten ikke være en fuld sikkerhedskopi, da den ikke vil indeholde nogen private optegnelser.

Denne Gramps XML-fil kan senere bruges til at gendanne træet til denne nøjagtige tilstand via [Gendan fra sikkerhedskopi](settings.md#restore-from-backup).

## Del dit slægtræ med brugere af andre slægtsforskningsprogrammer

Når det ikke er muligt at dele genealogiske data som Gramps XML, kan du også eksportere en GEDCOM-fil. Bemærk, at dette ikke er egnet som en sikkerhedskopi af dit Gramps Web-træ.

## Sikkerhedskopier dine mediefiler

For at sikkerhedskopiere dine mediefiler kan du oprette og downloade et ZIP-arkiv af alle mediefiler på eksport-siden.

Bemærk, at dette, især for store træer, kan være en kostbar operation for serveren og kun bør gøres, hvis det er absolut nødvendigt. Af denne grund er antallet af mediearkiver, der kan oprettes, begrænset (som standard til én pr. time). Hvis du når grænsen, vises en fejlmeddelelse.

En bedre mulighed for regelmæssigt at sikkerhedskopiere dine mediefiler er at bruge [Gramps Web Sync-tilføjelsen](sync.md) (som i sig selv ikke er en sikkerhedskopiløsning) og oprette inkrementelle sikkerhedskopier på din lokale computer.

I begge tilfælde, hvis din Gramps Web-bruger ikke har tilladelse til at se private optegnelser, vil eksporten ikke indeholde filer af private medieobjekter.

## Flyt til en anden Gramps Web-instans

Gramps Web låser dig ikke til en specifik udbyder, og du kan altid flytte til en anden Gramps Web-instans uden at miste data og uden at have direkte adgang til nogen af serverne.

For at opnå en fuld migration skal du følge disse trin (forudsat at du har ejerrettigheder til træet):

1. Gå til eksport-siden og eksportér dit træ som en Gramps XML (`.gramps`) fil. Hvis du bruger [Sync-tilføjelsen](sync.md), kan du også generere eksporten i Gramps desktop.
2. På eksport-siden skal du generere og downloade et mediearkiv. Hvis du bruger [Sync-tilføjelsen](sync.md), kan du også blot ZIP'e din lokale Gramps mediemappe.
3. Gå til Indstillinger > Administration > Administrer brugere og klik på knappen "Eksportér brugeroplysninger". Det vil downloade en JSON-fil.
4. I den nye Gramps Web-instans skal du åbne import-siden. Importér den `.gramps` fil, der blev eksporteret i trin 1.
5. På import-siden for den nye Gramps Web-instans skal du uploade mediearkivet (ZIP).
6. Gå til Indstillinger > Administration > Administrer brugere af den nye Gramps Web-instans. Klik på knappen "Importer brugerkonti" og upload JSON-filen, der blev downloadet i trin 3.

Bemærk, at mens dine brugerkonti vil blive migreret, skal alle dine brugere indstille nye adgangskoder ved at bruge linket "glemt adgangskode", da adgangskoder opbevares i krypteret form og ikke kan eksporteres.
