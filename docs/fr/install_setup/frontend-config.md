# Personnalisation de l'interface

L'interface Web de Gramps est une application Javascript déployée sous forme d'un ensemble de fichiers HTML, CSS et Javascript statiques. Normalement, aucune configuration spéciale n'est nécessaire pour l'interface. Cependant, certains comportements peuvent être modifiés en définissant des options appropriées dans le fichier `config.js` à la racine de la distribution.

Le fichier doit avoir la structure suivante :

```javascript
window.grampsjsConfig = {
    option: value
}
```

Les clés d'options suivantes existent.

Clé | Type | Description 
----|-----|-----------
`hideDNALink` | boolean | Si vrai, masque le lien ADN dans la barre de navigation.
`hideRegisterLink` | boolean | Si vrai, masque le lien d'inscription sur la page de connexion. Cela doit être utilisé pour les déploiements multi-arbres.
`loginRedirect` | string | URL vers laquelle rediriger lorsque l'utilisateur n'est pas connecté et navigue vers une page autre que "login" ou "register"
`mapBaseStyleLight` | string | URL de style MapLibre pour la carte de base en thème clair (par défaut : `https://tiles.openfreemap.org/styles/liberty`)
`mapBaseStyleDark` | string | URL de style MapLibre pour la carte de base en thème sombre (par défaut : `https://tiles.openfreemap.org/styles/dark`)
`mapOhmStyle` | string | URL de style MapLibre pour la superposition OpenHistoricalMap (par défaut : `https://www.openhistoricalmap.org/map-styles/main/main.json`)
