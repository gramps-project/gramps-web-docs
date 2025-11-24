# Personalizzazione del frontend

Il frontend di Gramps Web è un'applicazione Javascript che viene distribuita come un insieme di file statici HTML, CSS e Javascript. Normalmente, non è necessaria alcuna configurazione speciale per il frontend. Tuttavia, alcuni comportamenti possono essere modificati impostando opzioni appropriate nel file `config.js` nella radice della distribuzione.

Il file dovrebbe avere la seguente struttura:

```javascript
window.grampsjsConfig = {
    option: value
}
```

Esistono le seguenti chiavi di opzione.

Chiave | Tipo | Descrizione 
----|-----|-----------
`hideDNALink` | boolean | Se true, nascondi il link DNA nella barra di navigazione.
`hideRegisterLink` | boolean | Se true, nascondi il link di registrazione nella pagina di accesso. Questo dovrebbe essere utilizzato per distribuzioni multi-albero.
`loginRedirect` | string | URL a cui reindirizzare quando non si è connessi e si naviga verso qualsiasi pagina diversa da "login" o "register"
`leafletTileUrl` | string | URL del tile personalizzato per le mappe Leaflet
`leafletTileSize` | number | Dimensione del tile personalizzata per le mappe Leaflet
`leafletZoomOffset` | number | Offset di zoom personalizzato per le mappe Leaflet
`leafletTileAttribution` | string | Attribuzione personalizzata per le mappe Leaflet
