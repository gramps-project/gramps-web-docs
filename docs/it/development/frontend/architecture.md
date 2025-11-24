# Architettura

## Componenti

Il frontend è costruito con componenti web. Questi sono definiti nei file Javascript nella directory `src`.

Tipicamente, ogni file definisce un componente, iniziando con
```javascript
class GrampsjsSomeElement extends LitElement
```
e terminando con
```javascript
customElements.define('grampsjs-some-element', GrampsjsSomeElement)`
```
che definisce il nuovo elemento HTML `grampsjs-some-element` che può essere utilizzato altrove.

Il punto di ingresso principale, incluso in `index.html`, è l'elemento `gramps-js` definito in `GrampsJs.js`. Questo contiene la definizione di tutte le singole pagine (che corrispondono semplicemente a elementi che vengono mostrati o nascosti in base alla rotta/URL), il menu e il routing.

I componenti nella directory `src/views` corrispondono solitamente a componenti a pagina intera che recuperano dati dal backend (ad es., la vista della lista delle persone), mentre i componenti in `src/components` sono solitamente blocchi di costruzione più piccoli utilizzati all'interno delle viste che ottengono i loro dati da attributi forniti dal loro elemento genitore. Tuttavia, questa separazione non è rigorosa.

## Flusso di dati

I dati vengono scambiati con il Backend/API tramite i metodi `apiGet`, `apiPut` e `apiPost` in `src/api.js`, che si occupano automaticamente dell'autenticazione.

I dati vengono passati dai componenti genitori ai componenti figli tramite proprietà (vedi ad es. la [documentazione di Lit](https://lit.dev/docs/components/properties/)).

Quando i dati devono essere restituiti da un componente figlio a un componente genitore, vengono utilizzati eventi personalizzati che possono essere attivati con la funzione `fireEvent` in `src/api.js` e ascoltati utilizzando la sintassi `@` di Lit [(docs)](https://lit.dev/docs/components/events/).

## Autenticazione

Il token di refresh e il token di autenticazione sono memorizzati nel local storage del browser. Ogni volta che viene effettuata una chiamata API e il token è scaduto, il token di refresh memorizzato viene utilizzato per recuperare un nuovo token di accesso e la chiamata API viene ripetuta.

L'ambito di autorizzazione dell'utente, che è memorizzato nelle rivendicazioni del token di accesso, viene ottenuto con la funzione `getPermissions` e utilizzato nell'elemento di livello superiore `GrampsJs` per impostare le proprietà booleane `canAdd`, `canEdit`, `canManageUsers`, che vengono propagate agli elementi figli per implementare funzionalità specifiche di autorizzazione.
