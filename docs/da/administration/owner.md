# Opret en konto for træejeren

Før du kan begynde at bruge Gramps Web, skal du oprette en konto for træejeren. Hvis der ikke findes en brugerkonto for et givet træ, vises en formular til at oprette en konto. Formularen afhænger af serveropsætningen, der er til et enkelt træ eller til flere træer.

## Enkelt-træ opsætning: opret admin konto

På en server med enkelt-træ opsætning, når der endnu ikke findes nogen brugerkonto, viser åbning af Gramps Web en formular til at oprette en admin konto. Admin-brugeren vil være både ejer af det (enkle) træ og administrator for installationen. Formularen giver også mulighed for at indstille e-mailkonfigurationen, der er nødvendig for e-mailnotifikationer (f.eks. nulstilling af en brugers adgangskode). Hvis e-mailkonfigurationen allerede er tilføjet via en konfigurationsfil eller miljøvariabler på serveren, kan denne del af formularen efterlades tom.

## Multi-træ opsætning: opret admin konto

I en multi-træ opsætning vises den samme formular til at oprette en admin konto, hvis der ikke findes brugere *i noget træ*, dvs. når serveren lige er blevet oprettet.

## Multi-træ opsætning: opret træ ejer konto

I en multi-træ opsætning er hver bruger knyttet til et enkelt træ. Selv hvis brugere allerede findes i andre træer, kan en træ ejer oprettes i webgrænsefladen, hvis der endnu ikke findes nogen ejer *for dette træ*.

Ejeroprettelsesformularen vises dog ikke automatisk på Gramps Webs startside, som er den samme for alle træer. I stedet kan den nås på `https://my-gramps-instance/firstrun/my-tree-id`, hvor `https://my-gramps-instance` er basisadressen for din Gramps Web-installation, og `my-tree-id` er ID'et for dit træ.

En mulig arbejdsgang for en webadministrator til at oprette et nyt træ er at

- Oprette et træ via REST API'en og få træ-ID'et for det nye træ
- Dele linket til ejeroprettelsesformularen med det relevante træ-ID med den potentielle træ ejer

Oprettelsesformularen for træ ejeren er analog med adminoprettelsesformularen beskrevet ovenfor, bortset fra at den ikke tillader ændring af e-mailkonfigurationen (hvilket kun er tilladt for administratorer).
