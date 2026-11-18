# Eksportér data

Eksport-siden lader dig downloade familie trædata i forskellige formater, samt et arkiv af alle mediefiler.

## Eksportér familie træet som Gramps XML

For at få en kopi af familie trædata, åbn Eksport-siden i Gramps Web og vælg Gramps XML-formatet. Klik på **Generér** for at oprette filen, og **Download** når den er klar. For et stort træ kan det tage lidt tid at generere filen; du kan forlade siden i mellemtiden og downloade filen senere fra dens indgang i [notifikationer](../user-guide/notifications.md).

Bemærk, at hvis din Gramps Web-bruger ikke har tilladelse til at se private optegnelser, vil eksporten ikke indeholde nogen private optegnelser.

## Tag backup af dit familie træ

For komplette sikkerhedskopier af træet – inklusive dets indstillinger og brugere – se [Tag backup og gendan](backups.md). En Gramps XML-eksport kan fungere som en backup af familie trædataene alene og kan gendannes via [Gendan fra backup](backups.md#restore-from-backup).

## Del dit familie træ med brugere af andre slægtsforskningsprogrammer

Når deling af genealogiske data som Gramps XML ikke er en mulighed, kan du også eksportere en GEDCOM-fil. Bemærk, at dette ikke er velegnet som en backup af dit Gramps Web-træ.

## Tag backup af dine mediefiler

For at tage backup af dine mediefiler kan du oprette og downloade et ZIP-arkiv af alle mediefiler på Eksport-siden.

Bemærk, at dette, især for store træer, kan være en kostbar operation for serveren og kun bør gøres, hvis det er absolut nødvendigt. Af denne grund er antallet af mediearkiver, der kan oprettes, begrænset (som standard til én pr. time). Hvis du når grænsen, vises fejlmeddelelsen.

En bedre mulighed for regelmæssigt at tage backup af dine mediefiler er at bruge [Gramps Web Sync-tilføjelsen](sync.md) (som i sig selv ikke er en backup-løsning) og oprette inkrementelle sikkerhedskopier på din lokale computer.

I begge tilfælde, hvis din Gramps Web-bruger ikke har tilladelse til at se private optegnelser, vil eksporten ikke indeholde filer af private medieobjekter.

## Flyt til en anden Gramps Web-forekomst

Gramps Web låser dig ikke til en specifik udbyder, og du kan altid flytte til en anden Gramps Web-forekomst uden at miste data og uden at have direkte adgang til nogen af serverne.

For at opnå en fuld migration, følg disse trin (forudsat at du har ejerrettigheder til træet):

1. Gå til Eksport-siden og eksportér dit træ som en Gramps XML (`.gramps`) fil. Hvis du bruger [Sync-tilføjelsen](sync.md), kan du også generere eksporten i Gramps desktop.
2. På Eksport-siden, generer og download et mediearkiv. Hvis du bruger [Sync-tilføjelsen](sync.md), kan du også blot ZIP'e din lokale Gramps mediemappe.
3. Gå til Indstillinger > Administration > Administrer brugere og klik på knappen "Eksportér brugeroplysninger". Det vil downloade en JSON-fil.
4. I den nye Gramps Web-forekomst, åbn [Import-siden](import.md). Importér den `.gramps` fil, der blev eksporteret i trin 1.
5. På Import-siden i den nye Gramps Web-forekomst, upload mediearkivet (ZIP) under [Importér mediefiler](import-media.md).
6. Gå til Indstillinger > Administration > Administrer brugere i den nye Gramps Web-forekomst. Klik på knappen "Importér brugerkonti" og upload JSON-filen downloadet i trin 3.

Bemærk, at mens dine brugerkonti vil blive migreret, skal alle dine brugere sætte nye adgangskoder ved at bruge linket "glemt adgangskode", da adgangskoder gemmes i krypteret form og ikke kan eksporteres.
