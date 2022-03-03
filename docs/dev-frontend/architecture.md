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

To be continued ...