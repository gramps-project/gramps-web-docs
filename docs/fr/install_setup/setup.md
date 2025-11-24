# Installation / Configuration de Gramps Web

Cette section traite de l'installation et de la configuration de Gramps Web, ainsi que d'autres options pour commencer.

## Commencer avec Gramps Web

Gramps Web est une application web qui fonctionne sur un serveur et est accessible via un navigateur web. Elle est destinée à être accessible aux utilisateurs authentifiés via Internet.

Si vous souhaitez utiliser Gramps Web pour vos données de recherche généalogique, vous devez choisir l'une des options suivantes :

1. Auto-héberger sur votre propre matériel
2. Auto-héberger dans le cloud
3. S'inscrire pour une instance hébergée

Bien que la première option vous offre une flexibilité et un contrôle maximaux, elle peut également être techniquement difficile.

!!! astuce
    L'un des principaux principes de Gramps Web est de permettre aux utilisateurs de contrôler leurs propres données à tout moment, donc migrer des données d'une instance à une autre est simple. Ne vous inquiétez pas d'être bloqué après avoir choisi l'une des options !

## Auto-héberger sur votre propre matériel

La manière la plus pratique d'auto-héberger Gramps Web est via Docker Compose. Nous fournissons également des images Docker pour l'architecture ARM, afin que vous puissiez exécuter Gramps Web sur un Raspberry Pi dans votre sous-sol.

Voir [Déployer avec Docker](deployment.md) pour les instructions d'installation.

## Auto-héberger dans le cloud

Installer Gramps Web peut être plus difficile que d'autres applications web simples et n'est pas compatible avec les fournisseurs d'hébergement "partagé" ordinaires. Vous pouvez vous inscrire pour un serveur virtuel et installer Gramps Web [manuellement](deployment.md).

Une option plus simple est d'utiliser une image cloud pré-installée. Un exemple est notre [application 1-click DigitalOcean](digital_ocean.md).

## S'inscrire pour une instance hébergée

Une instance hébergée de Gramps Web est le moyen le plus simple de commencer avec Gramps Web, car aucune installation ou configuration n'est requise.

Voici une liste de fournisseurs d'hébergement dédiés pour Gramps Web (la communauté open source de Gramps ne prend pas la responsabilité de leurs services) :

- Grampshub ([www.grampshub.com](https://www.grampshub.com)), proposé par l'un des principaux contributeurs de Gramps Web

Si vous utilisez une option hébergée pour Gramps Web, vous pouvez sauter le reste de cette section et passer directement à la section [Administration](../administration/admin.md).
