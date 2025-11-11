# Personnalisation de l'interface utilisateur

L'interface utilisateur Web de Gramps est une application Javascript déployée sous forme d'un ensemble de fichiers HTML, CSS et Javascript statiques. Normalement, aucune configuration spéciale n'est nécessaire pour l'interface. Cependant, certains comportements peuvent être modifiés en définissant des options appropriées dans le fichier `config.js` à la racine de la distribution.

Le fichier doit avoir la structure suivante :

```javascript
window.grampsjsConfig = {
    option: value
}
```

Les clés d'option suivantes existent.

Clé | Type | Description 
----|-----|-----------
`hideDNALink` | boolean | Si vrai, cacher le lien ADN dans la barre de navigation.
`hideRegisterLink` | boolean | Si vrai, cacher le lien d'inscription sur la page de connexion. Cela doit être utilisé pour les déploiements multi-arbres.
`loginRedirect` | string | URL vers laquelle rediriger lorsqu'on n'est pas connecté et qu'on navigue vers une page autre que "login" ou "register"
`leafletTileUrl` | string | URL de tuile personnalisée pour les cartes Leaflet
`leafletTileSize` | number | Taille de tuile personnalisée pour les cartes Leaflet
`leafletZoomOffset` | number | Décalage de zoom personnalisé pour les cartes Leaflet
`leafletTileAttribution` | string | Attribution personnalisée pour les cartes Leaflet
