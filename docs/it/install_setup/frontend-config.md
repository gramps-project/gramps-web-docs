# Personalizzazione del frontend

Il frontend di Gramps Web è un'applicazione Javascript che viene distribuita come un insieme di file statici HTML, CSS e Javascript. Normalmente, non è necessaria alcuna configurazione speciale per il frontend. Tuttavia, alcuni comportamenti possono essere modificati impostando le opzioni appropriate nel file `config.js` nella radice della distribuzione.

Il file dovrebbe avere la seguente struttura:

```javascript
window.grampsjsConfig = {
    option: value
}
```

Le seguenti chiavi di opzione esistono.

Chiave | Tipo | Descrizione 
-------|------|-----------
`hideDNALink` | boolean | Se vero, nascondi il link DNA sulla barra di navigazione.
`hideRegisterLink` | boolean | Se vero, nascondi il link di registrazione nella pagina di accesso. Questo dovrebbe essere utilizzato per distribuzioni multi-albero.
`loginRedirect` | string | URL a cui reindirizzare quando non si è connessi e si naviga verso qualsiasi pagina diversa da "login" o "register"
`mapBaseStyleLight` | string | URL dello stile MapLibre per la mappa di base nel tema chiaro (predefinito: `https://tiles.openfreemap.org/styles/liberty`)
`mapBaseStyleDark` | string | URL dello stile MapLibre per la mappa di base nel tema scuro (predefinito: `https://tiles.openfreemap.org/styles/dark`)
`mapOhmStyle` | string | URL dello stile MapLibre per il sovrapposizione OpenHistoricalMap (predefinito: `https://www.openhistoricalmap.org/map-styles/main/main.json`)
`mapWikidata` | boolean | Se falso, rimuovi il layer [Wikidata buildings](../user-guide/map.md#wikidata-buildings) dalla mappa (predefinito: vero)
