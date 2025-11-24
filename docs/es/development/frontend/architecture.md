# Arquitectura

## Componentes

El frontend está construido a partir de componentes web. Están definidos en los archivos Javascript en el directorio `src`.

Típicamente, cada archivo define un componente, comenzando con
```javascript
class GrampsjsSomeElement extends LitElement
```
y terminando con
```javascript
customElements.define('grampsjs-some-element', GrampsjsSomeElement)`
```
que define el nuevo elemento HTML `grampsjs-some-element` que puede ser utilizado en otros lugares.

El punto de entrada principal, incluido en `index.html`, es el elemento `gramps-js` definido en `GrampsJs.js`. Esto contiene la definición de todas las páginas individuales (que corresponden simplemente a elementos que se muestran u ocultan según la ruta/URL), el menú y el enrutamiento.

Los componentes en el directorio `src/views` generalmente corresponden a componentes de página completa que obtienen datos del backend (por ejemplo, la vista de lista de personas), mientras que los componentes en `src/components` suelen ser bloques de construcción más pequeños utilizados dentro de las vistas que obtienen sus datos de atributos proporcionados por su elemento padre. Sin embargo, esta separación no es estricta.

## Flujo de datos

Los datos se intercambian con el Backend/API a través de los métodos `apiGet`, `apiPut` y `apiPost` en `src/api.js`, que se encargan automáticamente de la autenticación.

Los datos se pasan de componentes padres a componentes hijos a través de propiedades (ver, por ejemplo, la [documentación de Lit](https://lit.dev/docs/components/properties/)).

Cuando los datos necesitan ser enviados de un componente hijo a un componente padre, se utilizan eventos personalizados que pueden ser disparados con la función `fireEvent` en `src/api.js` y escuchados utilizando la sintaxis `@` de Lit [(docs)](https://lit.dev/docs/components/events/).

## Autenticación

El token de actualización y el token de autenticación se almacenan en el almacenamiento local del navegador. Cada vez que se realiza una llamada a la API y el token ha expirado, se utiliza el token de actualización almacenado para obtener un nuevo token de acceso y se repite la llamada a la API.

El alcance de autorización del usuario, que se almacena en las reclamaciones del token de acceso, se obtiene con la función `getPermissions` y se utiliza en el elemento de nivel superior `GrampsJs` para establecer las propiedades booleanas `canAdd`, `canEdit`, `canManageUsers`, que se transmiten a los elementos hijos para implementar funcionalidades específicas de autorización.
