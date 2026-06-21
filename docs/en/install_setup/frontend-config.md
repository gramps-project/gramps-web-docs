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
`hideTreeLink` | boolean | If true, hide the built-in Family Tree link on the navigation bar.
`navLinks` | array | Custom links to add to the navigation bar. See [Custom navigation links](#custom-navigation-links) below.
`hideRegisterLink` | boolean | If true, hide the registration link on the login page. This should be used for multi-tree deployments.
`loginRedirect` | string | URL to redirect to when not logged in and navigating to any page other than "login" or "register"
`leafletTileUrl` | string | Custom tile URL for Leaflet maps
`leafletTileSize` | number | Custom tile size for Leaflet maps
`leafletZoomOffset` | number | Custom zoom offset for Leaflet maps
`leafletTileAttribution` | string | Custom attribution for Leaflet maps

## Custom navigation links

The `navLinks` option adds custom links to the main navigation bar, for example to integrate another tool hosted on the same origin or to link to a user manual. It takes an array of objects with the following keys:

Key | Type | Description
----|------|------------
`title` | string | The link label shown in the navigation bar (required). It is displayed as entered and is not translated.
`url` | string | The link target (required). May be a relative path or an absolute URL.
`icon` | string | Optional SVG path of the icon to display, e.g. one of the paths from [Material Design Icons](https://pictogrammers.com/library/mdi/). Defaults to a generic link icon.
`target` | string | Optional anchor `target`. Defaults to `_self` (loads the link in the current tab). Use `_blank` to open the link in a new tab.

The default `target` of `_self` matters for links that point to another application served on the **same origin** as Gramps Web (such as a reverse-proxied tool): it ensures the browser performs a real navigation instead of the link being intercepted by the in-app router.

Custom links are added at the end of the main navigation group. To replace the built-in Family Tree link with a custom one, combine `navLinks` with `hideTreeLink`:

```javascript
window.grampsjsConfig = {
    hideTreeLink: true,
    navLinks: [
        {
            title: 'Family Tree',
            url: '/topola'
        },
        {
            title: 'User manual',
            url: 'https://www.grampsweb.org/',
            target: '_blank',
            icon: 'M14,3V5H17.59L7.76,14.83L9.17,16.24L19,6.41V10H21V3M19,19H5V5H12V3H5C3.89,3 3,3.9 3,5V19A2,2 0 0,0 5,21H19A2,2 0 0,0 21,19V12H19V19Z'
        }
    ]
}
```
