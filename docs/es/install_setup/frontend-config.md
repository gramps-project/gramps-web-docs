# Personalizando el frontend

El frontend de Gramps Web es una aplicación de Javascript que se despliega como un conjunto de archivos estáticos HTML, CSS y Javascript. Normalmente, no se necesita ninguna configuración especial para el frontend. Sin embargo, algunos comportamientos se pueden cambiar configurando las opciones adecuadas en el archivo `config.js` en la raíz de la distribución.

El archivo debe tener la siguiente estructura:

```javascript
window.grampsjsConfig = {
    option: value
}
```

Las siguientes claves de opción existen.

Clave | Tipo | Descripción 
-----|------|-----------
`hideDNALink` | booleano | Si es verdadero, oculta el enlace de ADN en la barra de navegación.
`hideRegisterLink` | booleano | Si es verdadero, oculta el enlace de registro en la página de inicio de sesión. Esto debe usarse para implementaciones de múltiples árboles.
`loginRedirect` | cadena | URL a la que redirigir cuando no se ha iniciado sesión y se navega a cualquier página que no sea "login" o "register"
`leafletTileUrl` | cadena | URL de mosaico personalizada para mapas de Leaflet
`leafletTileSize` | número | Tamaño de mosaico personalizado para mapas de Leaflet
`leafletZoomOffset` | número | Desplazamiento de zoom personalizado para mapas de Leaflet
`leafletTileAttribution` | cadena | Atribución personalizada para mapas de Leaflet
