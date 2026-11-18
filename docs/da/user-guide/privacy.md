# Private optegnelser

Enhver optegnelse i træet kan markeres som privat. Sammen med [brugerroller](../install_setup/users.md#user-roles) afgør dette, hvem der ser hvad.

## Hvem kan se hvad

Gramps Web er aldrig åbent for offentligheden: kun brugere med en konto kan se noget. "Offentlig" i Gramps betyder simpelthen "ikke privat", dvs. synlig for hver indlogget bruger af træet.

| Rolle | Offentlige optegnelser | Private optegnelser |
|---|---|---|
| Gæst | vis | – |
| Medlem | vis | vis |
| Bidragyder | vis, tilføj | vis, tilføj |
| Redaktør, Ejer, Administrator | vis, tilføj, rediger, slet | vis, tilføj, rediger, slet |

For gæster eksisterer private optegnelser ikke: de udelades fra sider, lister, søgeresultater, diagrammer, rapporter, eksporter og AI-assistentens svar. Dette håndhæves, hvor serveren læser databasen, ikke ved at skjule ting i appen, så en gæst ikke kan få adgang til private data på nogen anden måde.

Konti, der endnu ikke er godkendt (efter [selvregistrering](registration.md)), kan slet ikke logge ind.

Så hvis slægtninge eller andre personer med en gæstekonto ikke skal se visse oplysninger, skal du markere dem som private. Hvis alle brugere af et træ må se alt, skal du give dem medlemrollen (eller højere), og der er ikke behov for at markere noget som privat.

## Levende mennesker er ikke automatisk private

Intet gøres automatisk privat – ikke engang mennesker, der stadig er i live. Data om levende mennesker er synlige for gæster, indtil du markerer dem som private. Dette gælder også for importerede træer.

For at gøre de personer, der sandsynligvis er i live, private i Gramps Web:

1. I personlisten skal du åbne [det avancerede filter](lists.md#advanced-filter) og tilføje betingelsen "Personer sandsynligvis i live" (lad datoen stå tom for i dag). Anvend filteret.
2. Klik på **Vælg**, sæt flueben i headeren, og vælg **Vælg alle**.
3. Vælg **Privatliv**-handlingen og marker optegnelserne som private.

"Sandsynligvis i live" estimeres ud fra datoerne for personen og deres slægtninge. Personer uden nogen brugbare datoer betragtes som levende. Tjek resultatet, og husk, at estimatet kan ændre sig, efterhånden som du tilføjer data.

At markere en person som privat skjuler personen, men ikke deres begivenheder, noter, medier eller familier – se nedenfor. Gramps Desktop har flere værktøjer til at indstille privatlivets fred for mange relaterede optegnelser på én gang, som du kan bruge med [Sync-tilføjelsen](../administration/sync.md).

Personer, der dør senere, bliver heller ikke automatisk offentlige. Om du ønsker det, er op til dig – mange forskere foretrækker at holde indsamlede oplysninger private i nogen tid.

## Læsning af låseikoner

Brugere, der kan se private data, ser et lås ved siden af private elementer. Der er to slags:

- **Udfyldt lås** – selve optegnelsen er privat. På en persons side betyder et udfyldt lås ved siden af en begivenhed, at begivenheden er privat, og ved siden af et barn, at barnet er privat.
- **Omridslås** – kun *linket* er privat, ikke optegnelsen, det fører til. For eksempel kan en persons link til en begivenhed være privat, mens selve begivenheden er offentlig. Begivenheden er så skjult fra den pågældende persons side, men stadig synlig andre steder, såsom på siderne for andre deltagere eller i begivenhedlisten.

Hvis både optegnelsen og dens link er private, vises den udfyldte lås.

Den samme skelnen gælder for børn (barnet eller barnets link til familien), associationer, repository-links til en kilde og medier i et galleri. Navne, attributter, adresser og URL'er tilhører deres optegnelse og har kun den udfyldte lås.

## At gøre noget privat

Du har brug for redigeringsrettigheder for at ændre privatlivets fred.

- **En hel optegnelse**: åbn dens side, gå ind i redigeringstilstand, og klik på låseknappen i værktøjslinjen.
- **Del af en optegnelse** – et alternativt navn, attribut, adresse, URL, association, børnelink eller repository-link: åbn redigeringsdialogen for det element og tænd for **Privat**-kontakten. Det primære navn har ingen kontakt, da personen ellers ville vise sig som "Privat".
- **En begivenhed fra en persons eller families side**: begivenhedens redigeringsdialog har en privatlivskontakt for selve begivenheden. Hvis begivenheden deles med andre mennesker, bliver den først redigerbar efter **Rediger for alle**, da den er privat for dem alle.
- **En persons link til en begivenhed**: på begivenhedssiden skal du åbne deltagerens række i redigeringstilstand. Privatlivskontakten der gælder kun for den pågældende deltagerens link, så begivenheden forbliver synlig for de andre deltagere.
- **Et medieobjekt i et galleri**: i redigeringstilstand skal du klikke på låsen i hjørnet af flisen.
- **Mange optegnelser på én gang**: vælg dem i en liste og brug **Privatliv**-handlingen, se [Lister](lists.md#tags-and-privacy).

For at tjekke, hvilke optegnelser i en liste der er private, skal du tænde for **Privatliv**-kolonnen i kolonnevælgeren for listen.

## Ting at huske på

- At gøre en optegnelse privat gør ikke de optegnelser, den linker til, private. Hvis en person er privat, er deres begivenheder, de familier, de tilhører, og de noter, der er knyttet til dem, stadig synlige, medmindre de selv er private. Brug det avancerede filter eller **Privatliv**-kolonnen for at tjekke relaterede optegnelser.
- At gøre en familie eller begivenhed privat skjuler den, men ikke de mennesker, der er i den.
- [DNA-matcher og Y-DNA-data](dna-matches.md#private-matches) har deres egen **Privat**-kontakt i deres dialoger.
- Eksporter og mediearkiver lavet af en bruger, der ikke kan se private data, indeholder ingen private optegnelser eller filer.
- Privatliv er en Gramps-funktion, så optegnelser, der er markeret som private i Gramps Desktop, er også private i Gramps Web, og omvendt.
