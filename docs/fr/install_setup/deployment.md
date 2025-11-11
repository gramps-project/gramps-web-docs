# Déployer Gramps Web avec Docker

L'option la plus pratique pour héberger Gramps Web sur votre propre serveur (ou serveur virtuel) est d'utiliser Docker Compose.

Nous supposerons que Docker et Docker Compose sont déjà installés sur votre système. Vous pouvez utiliser Windows, Mac OS ou Linux comme système hôte. Les architectures prises en charge incluent non seulement x86-64 (systèmes de bureau), mais aussi des systèmes ARM tels qu'un Raspberry Pi, qui peut servir de serveur web à faible coût, mais suffisamment puissant.

!!! note
    Vous n'avez pas besoin d'installer Gramps sur le serveur car il est contenu dans l'image Docker.


## Étape 1 : Configuration de Docker

Créez un nouveau fichier sur le serveur nommé `docker-compose.yml` et insérez le contenu suivant : [docker-compose.yml](https://raw.githubusercontent.com/gramps-project/gramps-web-docs/main/examples/docker-compose-base/docker-compose.yml).

Cela générera six volumes nommés pour s'assurer que toutes les données pertinentes persistent lors du redémarrage du conteneur.

!!! warning
    Ce qui précède rendra l'API disponible sur le port 80 de la machine hôte **sans protection SSL/TLS**. Vous pouvez l'utiliser pour des tests locaux, mais ne l'exposez pas directement à Internet, c'est complètement non sécurisé !

## Étape 2 : Accès sécurisé avec SSL/TLS

L'API web **doit** être servie au public sur Internet via HTTPS. Il existe plusieurs options, par exemple :

- Utiliser un hébergement Docker qui inclut automatiquement SSL/TLS
- Utiliser un Nginx Reverse Proxy avec un certificat Let's Encrypt

Voir [Docker avec Let's Encrypt](lets_encrypt.md) pour savoir comment configurer la première option.

Si vous prévoyez d'utiliser Gramps Web uniquement sur votre réseau local, vous pouvez ignorer cette étape.

## Étape 3 : Démarrer le serveur

Exécutez

```
docker compose up -d
```

Lors de la première exécution, l'application affichera un assistant de première exécution qui vous permettra de

- Créer un compte pour l'utilisateur propriétaire (admin)
- Définir certaines options de configuration nécessaires
- Importer un arbre généalogique au format XML Gramps (`.gramps`)

## Étape 4 : Télécharger des fichiers multimédias

Il existe plusieurs options pour télécharger des fichiers multimédias.

- Lorsque vous utilisez des fichiers stockés sur le même serveur que Gramps Web, vous pouvez monter un répertoire dans le conteneur Docker au lieu d'utiliser un volume nommé, c'est-à-dire `/home/server_user/gramps_media/:/app/media` au lieu de `gramps_media:/app/media`, et y télécharger vos fichiers multimédias.
- Lorsque vous utilisez des fichiers multimédias [hébergés sur S3](s3.md), vous pouvez utiliser l'addon S3 Media Uploader.
- L'option sans doute la plus pratique est d'utiliser [Gramps Web Sync](../administration/sync.md).
