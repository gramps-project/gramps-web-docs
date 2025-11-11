# Architecture

## Components

The frontend is built out of web components. They are defined in the Javascript files in the `src` directory.

Typically, each file defines one component, starting with
```javascript
class GrampsjsSomeElement extends LitElement
```
and ending with
```javascript
customElements.define('grampsjs-some-element', GrampsjsSomeElement)`
```
that defines the new HTML element `grampsjs-some-element` that can be used elsewhere.

The main entrypoint, included in `index.html` , is the `gramps-js` element defined in `GrampsJs.js`. This contains the definition of all individual pages (that correspond simply to elements that are shown or hidden based on the route/URL), the menu, and routing.

The components in the `src/views` directory usually corresponds to full-page components that fetch data from the backend (e.g., the people list view), while components in `src/components` are usually smaller building blocks used inside the views that get their data from attributes provided by their parent element. However, this separation is not strict.

## Data flow

Data is exchanged with the Backend/API via the `apiGet`, `apiPut`, and `apiPost` methods in `src/api.js`, which automatically take care of authentication.

Data is passed from parent components to child components via properties (see e.g. the [Lit documentation](https://lit.dev/docs/components/properties/)).

When data needs to be fed back from a child to a parent component, custom events are used that can be fired with the `fireEvent` function in `src/api.js` and listened to using Lit's `@` syntax [(docs)](https://lit.dev/docs/components/events/).

## Authentication

The refresh token and authentication token are stored in the browser's local storage. Whenever an API call is made and the token is expired, the stored refresh token is used to fetch a new access token and the API call is repeated.

The user's authorization scope, which is stored in the access token's claims, is obtained with the `getPermissions` function and used in the top-level `GrampsJs` element to set the boolean properties `canAdd`, `canEdit`, `canManageUsers`, which are flowed down to child elements to implement authorization-specific functionality.