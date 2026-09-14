# Revisionshistorik

Visningen af revisionshistorikken viser alle redigeringer, der er blevet foretaget i slægtsforskningen.

Listevisningen viser redigeringerne grupperet efter "transaktioner". En transaktion er en gruppe af en eller flere tilføjelser, sletninger eller ændringer til Gramps-objekter. For eksempel genererer tilføjelsen af en ny familie med to eksisterende personer som far og mor en transaktion med et tilføjet familieobjekt og to ændrede personobjekter (fordi de indeholder linket til det nye familieobjekt).

Når du klikker på en transaktion, åbnes visningen af transaktionsdetaljer. Den indeholder listen over individuelle tilføjelser, sletninger og opdateringer pr. Gramps-objekt.

Valg af en individuel ændring åbner en visning af den rå JSON-repræsentation af Gramps-objektet, hvor tilføjelser og sletninger er fremhævet i henholdsvis grønt og rødt. En knap over differensen fører dig direkte til objektets egen side.

## Revisioner af et enkelt objekt

For at se historikken for en bestemt person, familie, begivenhed eller andet objekt, skal du åbne dens side og skifte til fanen **Revisioner**. Den viser hver ændring, der er foretaget på det objekt, nyeste først, med typen af ændring (tilføjet, opdateret eller slettet), brugeren der foretog den, og hvornår. Klik på en post for at åbne den transaktion, den tilhører, hvor du kan inspicere differensen eller fortryde den.

Klik på **Vis mere** for at indlæse ældre poster; for objekter med en meget lang historie vises kun de nyeste revisioner. For objekter, der sidst blev ændret før revisionshistorikken blev registreret, viser fanen kun tidspunktet for den sidste ændring.

!!! note
    Fanen Revisioner er synlig for medlemmer og derover og kræver Gramps Web API version 3.22 eller senere.

## Fortryde en revision

På transaktionsdetaljesiden giver en **Fortryd**-knap dig mulighed for at omvende den transaktion. Når du klikker på den, kontrolleres det, om fortrydelsen kan udføres uden problemer.

**Ren fortrydelse** – hvis ingen af de objekter, der er berørt af transaktionen, er blevet ændret siden, kan fortrydelsen fortsætte uden risiko. En bekræftelsesdialog vises, og ved at klikke på **Fortryd** omvender du transaktionen.

**Tvang kræves** – hvis et eller flere berørte objekter er blevet ændret af en senere transaktion, er en ren fortrydelse ikke mulig. Dialogen advarer om, at tvang af fortrydelsen kan resultere i datainkonsistenser, da senere ændringer, der afhænger af de pågældende objekter, vil blive bevaret som de er, selvom de underliggende objekter bliver omvendt. Du kan derefter enten annullere eller klikke på **Tvang fortryd** for at fortsætte alligevel.

I begge tilfælde kører fortrydelsen som en baggrundsopgave, og en statusindikator vises.
