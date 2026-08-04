# Personalizando el frontend

El frontend de Gramps Web es una aplicación de Javascript que se despliega como un conjunto de archivos estáticos HTML, CSS y Javascript. Normalmente, no se necesita ninguna configuración especial para el frontend. Sin embargo, algunos comportamientos se pueden cambiar configurando las opciones apropiadas en el archivo `config.js` en la raíz de la distribución.

El archivo debe tener la siguiente estructura:

```javascript
window.grampsjsConfig = {
    option: value
}
```

Las siguientes claves de opción existen.

Clave | Tipo | Descripción 
-----|-----|-----------
`hideDNALink` | booleano | Si es verdadero, oculta el enlace de ADN en la barra de navegación.
`hideRegisterLink` | booleano | Si es verdadero, oculta el enlace de registro en la página de inicio de sesión. Esto debe usarse para implementaciones de múltiples árboles.
`loginRedirect` | cadena | URL a la que redirigir cuando no se ha iniciado sesión y se navega a cualquier página que no sea "login" o "register"
`mapBaseStyleLight` | cadena | URL de estilo MapLibre para el mapa base en tema claro (predeterminado: `https://tiles.openfreemap.org/styles/liberty`)
`mapBaseStyleDark` | cadena | URL de estilo MapLibre para el mapa base en tema oscuro (predeterminado: `https://tiles.openfreemap.org/styles/dark`)
`mapOhmStyle` | cadena | URL de estilo MapLibre para la superposición de OpenHistoricalMap (predeterminado: `https://www.openhistoricalmap.org/map-styles/main/main.json`)
