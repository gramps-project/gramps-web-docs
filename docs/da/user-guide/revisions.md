# Revision Historik

Visningen af revisionshistorik viser alle redigeringer, der er blevet foretaget i slægtsforskningen.

Listevisningen viser redigeringerne grupperet efter "transaktioner". En transaktion er en gruppe af en eller flere tilføjelser, sletninger eller ændringer til Gramps-objekter. For eksempel genererer tilføjelsen af en ny familie med to eksisterende personer som far og mor en transaktion med et tilføjet familieobjekt og to ændrede personobjekter (fordi de indeholder linket til det nye familieobjekt).

Klik på en transaktion for at åbne visningen af transaktionsdetaljer. Den indeholder listen over individuelle tilføjelser, sletninger og opdateringer pr. Gramps-objekt.

Valg af en individuel ændring åbner en visning af den rå JSON-repræsentation af Gramps-objektet, hvor tilføjelser og sletninger er fremhævet i henholdsvis grønt og rødt.

## Fortryde en revision

På siden med transaktionsdetaljer giver en **Fortryd**-knap dig mulighed for at omvende den transaktion. Klik på den for at tjekke, om fortrydelsen kan udføres uden problemer.

**Ren fortrydelse** – hvis ingen af de objekter, der er påvirket af transaktionen, er blevet ændret siden, kan fortrydelsen fortsætte uden risiko. En bekræftelsesdialog vises, og ved at klikke på **Fortryd** omvender du transaktionen.

**Tvang kræves** – hvis et eller flere påvirkede objekter er blevet ændret af en senere transaktion, er en ren fortrydelse ikke mulig. Dialogen advarer om, at tvangsfortrydelse kan resultere i datainkonsistenser, da senere ændringer, der afhænger af de pågældende objekter, vil blive bevaret som de er, selvom de underliggende objekter bliver omvendt. Du kan derefter enten annullere eller klikke på **Tvang fortryd** for at fortsætte alligevel.

I begge tilfælde kører fortrydelsen som en baggrundsopgave, og en statusindikator vises.
