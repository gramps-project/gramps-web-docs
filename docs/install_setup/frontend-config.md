# Customizing the frontend

The Gramps Web frontend is a Javascript application that is deployed as a set of static HTML, CSS, and Javascript files. Normally, no special configuration is necessary for the frontend. However, some behaviour can be changed by setting appropriate options in the `config.js` file at the root of the distribution.

The file should have the following structure:

```javascript
window.grampsjsConfig = {
    option: value
}
```

The following option keys exist.

Key |Type | Description 
----|-----|-----------
`hideDNALink` | boolean | If true, hide the DNA link on the navigation bar.
`hideRegisterLink` | boolean | If true, hide the registration link on the login page. This should be used for multi-tree deployments.
`loginRedirect` | string | URL to redirect to when not logged in and navigating to any page other than "login" or "register"
`leafletTileUrl` | string | Custom tile URL for Leaflet maps
`leafletTileSize` | number | Custom tile size for Leaflet maps
`leafletZoomOffset` | number | Custom zoom offset for Leaflet maps
`leafletTileAttribution` | string | Custom attribution for Leaflet maps
