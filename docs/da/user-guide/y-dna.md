# Brug af Gramps Web til Y-DNA-analyse

!!! note "Bemærk"
    Denne funktion kræver Gramps Web API version 3.3.0 eller senere og Gramps Web frontend version 25.9.0 eller senere.

Y-DNA-visningen i Gramps Web kan bruge rå Y-kromosom enkelt-nukleotid polymorfi (SNP) data til at bestemme en persons mest sandsynlige Y-DNA haplogruppe og vise de afledte forfædre i det menneskelige Y-kromosomtræ sammen med tidsestimater.

## Sådan opnås og gemmes Y-DNA SNP-data

For at opnå Y-DNA SNP-data skal du have foretaget en Y-DNA-test gennem en genetisk testtjeneste. Resultatet repræsenteres som et sæt mutationer (SNP'er), hver identificeret med en streng (f.eks. `R-BY44535`) og et `+` eller `-` tegn, der angiver, om mutation er til stede eller fraværende. Gramps Web forventer strengen af alle testede SNP'er i formatet `SNP1+, SNP2-, SNP3+,...` gemt i en personattribut af brugerdefineret type `Y-DNA` (store og små bogstaver er vigtige). Du kan enten manuelt oprette denne attribut i Gramps Web eller Gramps Desktop, eller navigere til Y-DNA-visningen i Gramps Web og klikke på den blå "Tilføj" knap, vælge den person, du vil tilføje data til, og indsætte SNP-strengen. I alle tilfælde vil dataene blive gemt som en personattribut i din Gramps-database.

[Se nedenfor](#instructions-for-obtaining-snp-data-from-testing-services) for instruktioner om, hvordan du opnår SNP-data fra forskellige testtjenester.

## Hvordan det fungerer

Når en person har en `Y-DNA` attribut, der indeholder SNP-data, vil Gramps Web bruge det open-source [yclade](https://github.com/DavidMStraub/yclade) Python-bibliotek til at bestemme personens mest sandsynlige position på det menneskelige Y-kromosomtræ. Træet er blevet oprettet af [YFull](https://www.yfull.com/) projektet baseret på titusinder af Y-DNA-tests. Bemærk, at Gramps Web bruger en lokal kopi af YFull-træet, så ingen data sendes til tredjepart.

Træet gennemgås fra roden til bladene, og ved hver node sammenlignes SNP'erne, der er knyttet til den pågældende node, med personens positivt og negativt testede SNP'er, og den passende gren følges.

Det endelige resultat er en rækkefølge af klader fra roden af træet (den [Y-kromosomale "Adam"](https://en.wikipedia.org/wiki/Y-chromosomal_Adam)) til den mest afledte klade, der er konsistent med personens SNP-data. Hver klade har en anslået alder baseret på alderen af prøverne i YFull-databasen, der tilhører den pågældende klade.

Da Y-kromosomer arves fra far til søn, svarer denne rækkefølge til et uddrag af personens patrilineære forfædre.

## Sådan fortolkes resultaterne

Den vigtigste information er personens mest sandsynlige haplogruppe, vist øverst på siden. Navnet er linket til den tilsvarende side på [YFull](https://www.yfull.com/) webstedet, som indeholder mere information, såsom oprindelseslandet for testede prøver, der tilhører den haplogruppe.

I det patrilineære forfædret træ, der vises i Gramps Web, er boksen direkte over den testede person den mest recente fælles forfader (MRCA) for alle testede prøver, der tilhører personens haplogruppe. Datoen vist for denne forfader er hans anslåede omtrentlige fødselsdato. Forfaderen over ham er den forfader, hvor mutation, der definerer denne haplogruppe, først dukkede op.

På grund af den langsomme mutationsrate for Y-kromosomer kan MRCA være mange hundrede år tilbage i tiden. For sjældne haplogrupper (dvs. haplogrupper, hvor få personer er blevet testet indtil videre) kan det endda være tusinder af år.

## Instruktioner til at opnå SNP-data fra testtjenester

### [YSEQ](https://www.yseq.net/)

Når du er logget ind på "Min konto", gå til "Mine resultater / Se mine alleler" og naviger til bunden af siden. Tekstfeltet "Alleleliste kompakt" er blevet tilføjet specifikt til Gramps Web og er i præcist det rigtige format til at indsætte i `Y-DNA` attributten.
