# Architecture

## Composants

Le frontend est construit à partir de composants web. Ils sont définis dans les fichiers Javascript du répertoire `src`.

Typiquement, chaque fichier définit un composant, commençant par
```javascript
class GrampsjsSomeElement extends LitElement
```
et se terminant par
```javascript
customElements.define('grampsjs-some-element', GrampsjsSomeElement)`
```
qui définit le nouvel élément HTML `grampsjs-some-element` pouvant être utilisé ailleurs.

Le point d'entrée principal, inclus dans `index.html`, est l'élément `gramps-js` défini dans `GrampsJs.js`. Cela contient la définition de toutes les pages individuelles (qui correspondent simplement à des éléments affichés ou cachés en fonction de la route/URL), le menu et le routage.

Les composants dans le répertoire `src/views` correspondent généralement à des composants de page complète qui récupèrent des données du backend (par exemple, la vue de la liste des personnes), tandis que les composants dans `src/components` sont généralement des blocs de construction plus petits utilisés à l'intérieur des vues qui obtiennent leurs données à partir des attributs fournis par leur élément parent. Cependant, cette séparation n'est pas stricte.

## Flux de données

Les données sont échangées avec le Backend/API via les méthodes `apiGet`, `apiPut` et `apiPost` dans `src/api.js`, qui s'occupent automatiquement de l'authentification.

Les données sont transmises des composants parents aux composants enfants via des propriétés (voir par exemple la [documentation Lit](https://lit.dev/docs/components/properties/)).

Lorsque des données doivent être renvoyées d'un composant enfant à un composant parent, des événements personnalisés sont utilisés et peuvent être déclenchés avec la fonction `fireEvent` dans `src/api.js` et écoutés en utilisant la syntaxe `@` de Lit [(docs)](https://lit.dev/docs/components/events/).

## Authentification

Le jeton de rafraîchissement et le jeton d'authentification sont stockés dans le stockage local du navigateur. Chaque fois qu'un appel API est effectué et que le jeton est expiré, le jeton de rafraîchissement stocké est utilisé pour obtenir un nouveau jeton d'accès et l'appel API est répété.

Le champ d'autorisation de l'utilisateur, qui est stocké dans les revendications du jeton d'accès, est obtenu avec la fonction `getPermissions` et utilisé dans l'élément de niveau supérieur `GrampsJs` pour définir les propriétés booléennes `canAdd`, `canEdit`, `canManageUsers`, qui sont transmises aux éléments enfants pour implémenter des fonctionnalités spécifiques à l'autorisation.
