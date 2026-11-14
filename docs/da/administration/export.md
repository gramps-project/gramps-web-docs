# Eksportér data

Eksport-siden giver dig mulighed for at downloade familie trædata i forskellige formater samt et arkiv af alle mediefiler.

## Eksportér familie træet som Gramps XML

For at få en kopi af familie trædata, skal du åbne Eksport-siden i Gramps Web og vælge Gramps XML-formatet. Ved at klikke på "eksport" genereres filen, og downloadet starter, når det er klar.

Bemærk, at hvis din Gramps Web-bruger ikke har tilladelse til at se private optegnelser, vil eksporten ikke indeholde nogen private optegnelser.

## Sikkerhedskopier dit familie træ

For komplette sikkerhedskopier af træet – inklusive dets indstillinger og brugere – se [Sikkerhedskopier og gendan](backups.md). En Gramps XML-eksport kan fungere som en sikkerhedskopi af familie trædataene alene og kan gendannes via [Gendan fra sikkerhedskopi](backups.md#restore-from-backup).

## Del dit familie træ med brugere af andre slægtsforskningsprogrammer

Når deling af genealogiske data som Gramps XML ikke er en mulighed, kan du også eksportere en GEDCOM-fil. Bemærk, at dette ikke er egnet som en sikkerhedskopi af dit Gramps Web-træ.

## Sikkerhedskopier dine mediefiler

For at sikkerhedskopiere dine mediefiler kan du oprette og downloade et ZIP-arkiv af alle mediefiler på Eksport-siden.

Bemærk, at dette, især for store træer, kan være en kostbar operation for serveren og kun bør gøres, hvis det er absolut nødvendigt. Af denne grund er antallet af mediearkiver, der kan oprettes, begrænset (som standard til én pr. time). Hvis du når grænsen, vises fejlen.

En bedre mulighed for regelmæssigt at sikkerhedskopiere dine mediefiler er at bruge [Gramps Web Sync-tilføjelsen](sync.md) (som i sig selv ikke er en sikkerhedsløsning) og oprette inkrementelle sikkerhedskopier på din lokale computer.

I begge tilfælde, hvis din Gramps Web-bruger ikke har tilladelse til at se private optegnelser, vil eksporten ikke indeholde filer af private medieobjekter.

## Flyt til en anden Gramps Web-instans

Gramps Web låser dig ikke til en specifik udbyder, og du kan altid flytte til en anden Gramps Web-instans uden at miste data og uden at have direkte adgang til nogen af serverne.

For at opnå en fuld migration, følg disse trin (forudsat at du har ejerrettigheder til træet):

1. Gå til Eksport-siden og eksportér dit træ som en Gramps XML (`.gramps`) fil. Hvis du bruger [Sync-tilføjelsen](sync.md), kan du også generere eksporten i Gramps desktop.
2. På Eksport-siden, generer og download et mediearkiv. Hvis du bruger [Sync-tilføjelsen](sync.md), kan du også blot ZIP'e din lokale Gramps mediemappe.
3. Gå til Indstillinger > Administration > Administrer brugere og klik på knappen "Eksportér brugeroplysninger". Det vil downloade en JSON-fil.
4. I den nye Gramps Web-instans, åbn Import-siden. Importér den `.gramps` fil, der blev eksporteret i trin 1.
5. På Import-siden i den nye Gramps Web-instans, upload mediearkivet (ZIP).
6. Gå til Indstillinger > Administration > Administrer brugere i den nye Gramps Web-instans. Klik på knappen "Importer brugerkonti" og upload JSON-filen, der blev downloadet i trin 3.

Bemærk, at mens dine brugerkonti vil blive migreret, skal alle dine brugere indstille nye adgangskoder ved at bruge linket "glemt adgangskode", da adgangskoder gemmes i krypteret form og ikke kan eksporteres.
