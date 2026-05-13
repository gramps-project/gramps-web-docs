# Rapporter

En rapport er et formateret, downloadbart dokument genereret fra dine slægtstrædata. Rapporter er de samme plugins, der er tilgængelige i Gramps Desktop – se [Gramps Wiki-siden om Rapporter](https://gramps-project.org/wiki/index.php/Gramps_5.1_Wiki_Manual_-_Reports) for en fuld oversigt. Webgrænsefladen kører den samme rapportmotor på serveren og leverer den resulterende fil til din browser.

Rapporter er tilgængelige fra sidepanelet.

## Rapportkategorier

Rapport-siden viser alle tilgængelige rapporter grupperet efter kategori:

- **Tekstrapporter** – narrative eller tabelbaserede dokumenter såsom forfædrelister, efterkommerapporter og fødselsdagskalendere. Outputformater inkluderer PDF, ODT/OpenDocument, RTF, HTML og andre.
- **Grafiske rapporter** – diagrammer og grafer såsom forfædretræer og fan-diagrammer. Outputformater inkluderer PDF, SVG, PNG og andre.
- **Træer** – slægtstrædiagrammer.
- **Bøger** – rapportbøger med flere kapitler, der kombinerer flere tekst- og grafiske rapporter til et enkelt dokument.
- **Websider** – statiske webstedsgeneratorer, der producerer et komplet sæt af HTML-sider fra dit træ.

De viste rapporter afhænger af, hvilke Gramps rapport-plugins der er installeret på serveren.

## Kørsel af en rapport

Klik på en rapport for at åbne dens indstillingsside, som viser:

- **Beskrivelse** – hvad rapporten indeholder
- **Forfatter** og **Version** af plugin'et
- **Indstillinger** – rapportspecifikke indstillinger såsom startperson, antal generationer, outputformat, sidestrørrelse og andre parametre

Justér indstillingerne efter behov, og klik derefter på **Generer**. Rapporten genereres på serveren, og den resulterende fil downloades automatisk til din browser.

!!! tip
    De fleste rapporter har som standard **database hjemmeperson** – den hjemmeperson, der er indstillet i Gramps-databasen, som kan være forskellig fra din personlige hjemmepersonindstilling i browseren. Hvis rapporten dækker den forkerte person, skal du ændre personindstillingen i rapportens indstillinger.
