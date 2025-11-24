## Sikkerhedskopier dit slægtstræ

For at oprette en sikkerhedskopi af dit slægtstræ, skal du åbne eksport-siden i Gramps Web og vælge Gramps XML-formatet.

Ved at klikke på "eksport" vil filen blive genereret og downloadet, når den er klar.

Bemærk, at hvis din Gramps Web-bruger ikke har tilladelse til at se private optegnelser, vil eksporten ikke være en fuld sikkerhedskopi, da den ikke vil indeholde nogen private optegnelser.

## Del dit slægtstræ med brugere af andre slægtsforskningsprogrammer

Når deling af genealogiske data som Gramps XML ikke er en mulighed, kan du også eksportere en GEDCOM-fil. Bemærk, at dette ikke er egnet som en sikkerhedskopi af dit Gramps Web-træ.

## Sikkerhedskopier dine mediefiler

For at sikkerhedskopiere dine mediefiler kan du oprette og downloade et ZIP-arkiv af alle mediefiler på eksport-siden.

Bemærk, at dette, især for store træer, kan være en dyr operation for serveren og kun bør gøres, hvis det er absolut nødvendigt.

En bedre mulighed for regelmæssigt at sikkerhedskopiere dine mediefiler er at bruge [Gramps Web Sync-tilføjelsen](sync.md) (som i sig selv ikke er en sikkerhedsløsning) og oprette inkrementelle sikkerhedskopier på din lokale computer.

I begge tilfælde, hvis din Gramps Web-bruger ikke har tilladelse til at se private optegnelser, vil eksporten ikke indeholde filer af private medieobjekter.

## Flyt til en anden Gramps Web-instans

Gramps Web låser dig ikke til en specifik udbyder, og du kan altid flytte til en anden Gramps Web-instans uden at miste data og uden at have direkte adgang til nogen af serverne.

For at opnå en fuld migration, følg disse trin (forudsat at du har ejerrettigheder til træet):

1. Gå til eksport-siden og eksportér dit træ som en Gramps XML (`.gramps`) fil. Hvis du bruger [Sync-tilføjelsen](sync.md), kan du også generere eksporten i Gramps desktop.
2. På eksport-siden, generer og download et mediearkiv. Hvis du bruger [Sync-tilføjelsen](sync.md), kan du også blot ZIP'e din lokale Gramps mediemappe.
3. Gå til Indstillinger > Administration > Administrer brugere og klik på knappen "Eksportér brugeroplysninger". Det vil downloade en JSON-fil.
4. I den nye Gramps Web-instans, åbn import-siden. Importér den `.gramps` fil, der blev eksporteret i trin 1.
5. På import-siden af den nye Gramps Web-instans, upload mediearkivet (ZIP).
6. Gå til Indstillinger > Administration > Administrer brugere af den nye Gramps Web-instans. Klik på knappen "Importer brugerkonti" og upload JSON-filen, der blev downloadet i trin 3.

Bemærk, at mens dine brugerkonti vil blive migreret, skal alle dine brugere indstille nye adgangskoder ved at bruge linket "glemt adgangskode", da adgangskoder opbevares i krypteret form og ikke kan eksporteres.
