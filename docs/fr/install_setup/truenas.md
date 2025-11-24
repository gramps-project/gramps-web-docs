# Configuration de TrueNAS

Ce guide explique comment configurer Gramps Web sur TrueNAS Community Edition 25.04.

!!! avertissement
    Ce guide est destiné à TrueNAS Community Edition 25.04 ou version ultérieure, qui a introduit un nouveau système d'applications basé sur Docker Compose. Il ne s'applique pas aux versions antérieures de TrueNAS.

## Prérequis

- TrueNAS Community Edition 25.04 ou version ultérieure
- Familiarité de base avec l'interface web de TrueNAS
- Un dataset pour stocker les données de Gramps Web

## Aperçu

TrueNAS Community Edition 25.04 a introduit un nouveau système d'applications basé sur Docker Compose qui remplace l'approche précédente basée sur les charts Helm. Ce guide vous guidera à travers la création d'une application personnalisée pour Gramps Web en utilisant Docker Compose.

## Étape 1 : Préparer le stockage

1. Accédez à **Datasets** dans l'interface web de TrueNAS
2. Créez un nouveau dataset pour Gramps Web (par exemple, `grampsweb`). Notez le chemin complet de ce dataset, par exemple, `/mnt/storage/grampsweb`, car vous en aurez besoin plus tard.

Créez des sous-répertoires pour les différents composants :
- `users` - Base de données des utilisateurs
- `database` - Fichier(s) de base de données Gramps
- `media` - Fichiers multimédias

## Étape 2 : Créer l'application Docker Compose

1. Accédez à **Apps** dans l'interface web de TrueNAS
2. Cliquez sur **Discover Apps**
3. Recherchez "Gramps Web" et cliquez dessus
4. Cliquez sur "Installer"

Cela vous amènera à la page de configuration de l'application.

## Étape 3 : Configurer l'application

### Configuration de Gramps Web

- **Fuseau horaire :** Définissez-le sur votre fuseau horaire local (par exemple, `Europe/Berlin`)
- **Mot de passe Redis :** Définissez un mot de passe pour Redis. Cela ne sera utilisé qu'en interne par l'application.
- **Désactiver la télémétrie :** veuillez laisser cette case décochée – voir [ici pour plus de détails](telemetry.md).
- **Clé secrète :** il est crucial que vous définissiez cela sur une valeur forte et unique. Voir [configuration du serveur](configuration.md#existing-configuration-settings) pour des instructions sur la façon de générer une clé aléatoire.
- **Variables d'environnement supplémentaires :** Vous devrez définir toutes les [options de configuration](configuration.md) supplémentaires en tant que variables d'environnement préfixées par `GRAMPSWEB_`. Veuillez consulter la [documentation de configuration](configuration.md) en détail – par exemple, le fait que les valeurs booléennes doivent être définies comme `true` ou `false` (tout en minuscules) dans le cas des variables d'environnement, un piège courant.

Veuillez **au moins** définir le `GRAMPSWEB_BASE_URL` sur l'URL à laquelle votre instance Gramps Web sera accessible – cela est requis pour un fonctionnement correct.

Vous voudrez peut-être également configurer l'email à ce stade. Si vous le faites, vous pouvez sauter l'étape de configuration de l'email dans l'assistant d'intégration. Les variables d'environnement pertinentes sont :

- `GRAMPSWEB_EMAIL_HOST`
- `GRAMPSWEB_EMAIL_HOST_USER`
- `GRAMPSWEB_EMAIL_HOST_PASSWORD`
- `GRAMPSWEB_DEFAULT_FROM_EMAIL`

Tous les paramètres de configuration peuvent être modifiés ultérieurement en cliquant sur "Modifier" dans l'interface des applications TrueNAS.

### Configuration du stockage

- **Stockage des utilisateurs :** Sélectionnez le chemin vers le répertoire `users` que vous avez créé précédemment.
- **Stockage de l'index :** Vous pouvez laisser le paramètre par défaut "ixVolume (Dataset créé automatiquement par le système)"
- **Stockage du cache des vignettes :** Vous pouvez laisser le paramètre par défaut "ixVolume (Dataset créé automatiquement par le système)"
- **Stockage du cache :** Vous pouvez laisser le paramètre par défaut "ixVolume (Dataset créé automatiquement par le système)"
- **Stockage multimédia :** Sélectionnez le chemin vers le répertoire `media` que vous avez créé précédemment.
- **Stockage de la base de données Gramps :** Sélectionnez le chemin vers le répertoire `database` que vous avez créé précédemment.

### Configuration des ressources

Nous vous recommandons d'allouer au moins 2 CPU et 4096 Mo de RAM pour garantir un fonctionnement fluide.

## Étape 4 : Accéder à Gramps Web

Une fois l'application déployée, vous pouvez accéder à Gramps Web en cliquant sur le bouton "Web UI" dans l'interface des applications TrueNAS. Vous devriez voir l'assistant d'intégration "Bienvenue dans Gramps Web".

Si vous souhaitez permettre aux utilisateurs d'accéder à votre interface Gramps Web, **ne** pas exposer l'application directement sur Internet, mais passez à l'étape suivante.

## Étape 5 : Configurer un proxy inverse

Pour exposer en toute sécurité votre instance Gramps Web aux utilisateurs, il est recommandé de configurer un proxy inverse. Cela vous permet de gérer les certificats SSL/TLS et de contrôler l'accès.

L'option la plus simple est d'utiliser l'application officielle TrueNAS Nginx Proxy Manager. Recherchez l'application dans l'interface des applications TrueNAS et installez-la. Vous pouvez laisser tous les paramètres par défaut, mais nous vous recommandons de définir une variable d'environnement supplémentaire : `DISABLE_IPV6` avec la valeur `true` pour éviter d'éventuels problèmes liés à l'IPv6.

Une fois déployé, ouvrez l'interface web de Nginx Proxy Manager et créez un nouvel hôte proxy avec les paramètres suivants :

- Schéma : `http`
- Nom d'hôte / IP de transfert : le nom d'hôte de votre serveur TrueNAS (par exemple, `truenas`)
- Port de transfert : le port attribué à votre application Gramps Web (vérifiez l'interface des applications TrueNAS pour le port exact)
- Dans l'onglet "SSL", cochez "Forcer SSL"
- Sous "Certificats SSL", sélectionnez "Ajouter un certificat SSL" > "Let's Encrypt" pour créer un nouveau certificat Let's Encrypt pour votre domaine.

Veuillez consulter la [documentation de Nginx Proxy Manager](https://nginxproxymanager.com/guide/) pour plus de détails sur la configuration de votre routeur et l'obtention de certificats SSL.
