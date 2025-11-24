---
hide:
  - navigation
---

Si vous rencontrez des problèmes ou avez besoin d'aide avec Gramps Web, veuillez choisir l'une des options suivantes.

[Forum :material-forum:](https://gramps.discourse.group/c/gramps-web/){ .md-button }
[Problèmes de backend :material-github:](https://github.com/gramps-project/gramps-web-api/issues){ .md-button }
[Problèmes de frontend :material-github:](https://github.com/gramps-project/gramps-web/issues){ .md-button }

Voir ci-dessous pour quelques conseils sur la direction à prendre en premier.

## Poser des questions

Le forum officiel de Gramps Discourse a une [catégorie séparée pour Gramps Web](https://gramps.discourse.group/c/gramps-web/). Veuillez l'utiliser pour poser toutes les questions que vous pourriez avoir sur Gramps Web, par exemple :

- Questions sur l'utilisation de Gramps Web
- Questions sur la configuration de Gramps Web
- Dépannage d'un déploiement de Gramps Web
- Idées d'améliorations pour Gramps Web
- ...

## Signaler des problèmes

Si vous rencontrez un problème que vous pensez être un bug dans Gramps Web, veuillez le signaler via Github.

Il existe deux dépôts Github distincts pour le code utilisé dans Gramps Web, un pour l'interface utilisateur (« frontend ») et un pour le code serveur (« backend ») :

- [Problèmes de frontend](https://github.com/gramps-project/gramps-web/issues)
- [Problèmes de backend](https://github.com/gramps-project/gramps-web-api/issues)

Si vous n'êtes pas sûr de l'endroit où signaler un problème, ne vous inquiétez pas et choisissez simplement l'un des deux – les mainteneurs pourront transférer le problème si nécessaire.

Dans tous les cas, veuillez toujours inclure les informations suivantes dans votre rapport :

- Détails sur votre configuration (par exemple, un fichier docker-compose avec des valeurs sensibles masquées, ou si vous utilisez une version hébergée, comme Grampshub, ou une image préconfigurée, comme DigitalOcean)
- Informations sur la version. Pour l'obtenir, allez à l'onglet "Informations système" sur la page des paramètres dans Gramps Web et copiez/collez les valeurs dans la boîte, qui devrait ressembler à ceci :

```
Gramps 5.1.6
Gramps Web API 1.5.1
Gramps.js 24.1.0
locale: en
multi-tree: false
task queue: true
```

## Suggérer des améliorations

Pour des idées générales et des discussions sur les améliorations futures, n'hésitez pas à ouvrir une discussion dans le [forum](https://gramps.discourse.group/c/gramps-web/). Vous pouvez également vérifier les pages de problèmes (voir les liens ci-dessus) pour savoir si une fonctionnalité particulière est déjà prévue ou en cours de développement.

Pour des améliorations spécifiques avec un champ d'application limité, n'hésitez pas à ouvrir directement un problème avec une demande de fonctionnalité dans le dépôt Github approprié pour le frontend ou le backend.
