# Arkitektur

## Komponenter

Frontend'en er bygget op af webkomponenter. De er defineret i Javascript-filerne i `src`-mappen.

Typisk definerer hver fil én komponent, der starter med
```javascript
class GrampsjsSomeElement extends LitElement
```
og slutter med
```javascript
customElements.define('grampsjs-some-element', GrampsjsSomeElement)`
```
som definerer det nye HTML-element `grampsjs-some-element`, der kan bruges andre steder.

Hovedindgangspunktet, der er inkluderet i `index.html`, er `gramps-js`-elementet defineret i `GrampsJs.js`. Dette indeholder definitionen af alle individuelle sider (som simpelthen svarer til elementer, der vises eller skjules baseret på ruten/URL'en), menuen og routing.

Komponenterne i `src/views`-mappen svarer normalt til fuldsidekomponenter, der henter data fra backend (f.eks. visningen af personlisten), mens komponenter i `src/components` normalt er mindre byggesten, der bruges inde i visningerne og får deres data fra attributter givet af deres overordnede element. Denne opdeling er dog ikke striks.

## Dataflow

Data udveksles med Backend/API via `apiGet`, `apiPut` og `apiPost` metoderne i `src/api.js`, som automatisk tager sig af autentificering.

Data sendes fra overordnede komponenter til underordnede komponenter via egenskaber (se f.eks. [Lit-dokumentationen](https://lit.dev/docs/components/properties/)).

Når data skal sendes tilbage fra en underordnet til en overordnet komponent, anvendes brugerdefinerede begivenheder, der kan affyres med `fireEvent` funktionen i `src/api.js` og lyttes til ved hjælp af Lit's `@` syntaks [(dokumentation)](https://lit.dev/docs/components/events/).

## Autentificering

Refresh-tokenet og autentificeringstokenet gemmes i browserens lokale lager. Hver gang der foretages et API-opkald, og tokenet er udløbet, bruges det gemte refresh-token til at hente et nyt adgangstoken, og API-opkaldet gentages.

Brugerens autorisationsomfang, som er gemt i adgangstokenets claims, opnås med `getPermissions` funktionen og bruges i det øverste `GrampsJs`-element til at sætte de booleske egenskaber `canAdd`, `canEdit`, `canManageUsers`, som sendes ned til underordnede elementer for at implementere autorisationsspecifik funktionalitet.
