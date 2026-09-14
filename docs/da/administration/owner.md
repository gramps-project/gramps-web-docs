# Opret en konto for træejeren

Før du kan begynde at bruge Gramps Web, skal du oprette en konto for træejeren. Hvis der ikke findes en brugerkonto for et givet træ, vises en formular til at oprette en konto. Formularen afhænger af serveropsætningen, der er til et enkelt træ eller til flere træer.

## Enkelt-træ opsætning: opret admin konto

På en server med enkelt-træ opsætning, når der endnu ikke findes nogen brugerkonto, viser åbning af Gramps Web en formular til at oprette en admin konto. Admin-brugeren vil både være ejer af det (enkle) træ og administrator af installationen. Formularen giver også mulighed for at indstille e-mailkonfigurationen, der er nødvendig for e-mailnotifikationer (f.eks. nulstilling af en brugers adgangskode). Hvis e-mailkonfigurationen allerede er blevet tilføjet via en konfigurationsfil eller miljøvariabler på serveren, kan denne del af formularen efterlades tom.

Adgangskoden skal indtastes to gange; formularen kan kun indsendes, når begge indtastninger matcher.

Hvis instansen allerede er blevet opsat, viser åbning af formularens adresse en besked, der beder dig logge ind med en eksisterende konto i stedet.

## Multi-træ opsætning: opret admin konto

I en multi-træ opsætning vises den samme formular til at oprette en admin konto, hvis der ikke findes brugere *i noget træ*, dvs. når serveren lige er blevet oprettet.

## Multi-træ opsætning: opret træ ejer konto

I en multi-træ opsætning er hver bruger knyttet til et enkelt træ. Selv hvis brugere allerede findes i andre træer, kan en træ ejer oprettes i webgrænsefladen, hvis der endnu ikke findes en ejer *for dette træ*.

Dog vil formularen til oprettelse af ejer ikke blive vist automatisk på Gramps Web-hjemmesiden, som er den samme for alle træer. I stedet kan den nås på `https://my-gramps-instance/firstrun/my-tree-id`, hvor `https://my-gramps-instance` er basisadressen for din Gramps Web-installation, og `my-tree-id` er ID'et for dit træ.

En mulig arbejdsgang for en webadministrator til at oprette et nyt træ er at

- Oprette et træ via REST API'en, og opnå træ-ID'et for det nye træ
- Dele linket til formularen til oprettelse af ejer med det passende træ-ID med den potentielle træ ejer

Formularen til oprettelse af træ ejer er analog med formularen til oprettelse af admin, som beskrevet ovenfor, bortset fra at den ikke tillader ændring af e-mailkonfigurationen (hvilket kun er tilladt for administratorer).
