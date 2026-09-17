# Utilisation d'une base de données PostgreSQL

Par défaut, Gramps Web stocke chaque arbre généalogique dans son propre fichier de base de données SQLite. Cela ne nécessite aucun service supplémentaire, les sauvegardes sont aussi simples que de copier des fichiers, et cela fonctionne bien pour la plupart des installations, y compris celles [hébergeant plusieurs arbres](multi-tree.md).

Alternativement, les arbres généalogiques peuvent être hébergés sur un serveur PostgreSQL en utilisant l'addon SharedPostgreSQL, qui conserve tous les arbres dans une seule base de données. Cela peut avoir du sens si vous exécutez déjà un serveur PostgreSQL et souhaitez gérer les sauvegardes et la surveillance là-bas, ou si vous vous attendez à de nombreux utilisateurs modifiant en même temps. PostgreSQL peut également héberger la [base de données utilisateur](#using-a-postgresql-database-for-the-user-database) et l'[index de recherche](#using-a-postgresql-database-for-the-search-index), indépendamment de l'endroit où les arbres généalogiques sont stockés.

!!! warning "Addon PostgreSQL obsolète"
    L'ancien addon PostgreSQL, qui stocke un seul arbre généalogique par base de données, est obsolète et ne sera plus supporté dans une future version de l'API Gramps Web. Si vous l'utilisez, consultez [Déplacer un arbre de l'addon PostgreSQL vers SharedPostgreSQL](#moving-a-tree-from-the-postgresql-addon-to-sharedpostgresql).

## Configuration du serveur PostgreSQL

L'option la plus simple est d'exécuter le serveur PostgreSQL dans un conteneur sur le même hôte Docker que Gramps Web, en utilisant Docker Compose.

Gramps a besoin de locales installées sur le serveur PostgreSQL pour trier correctement les objets dans différentes langues, et les images PostgreSQL par défaut n'en incluent aucune. L'image [`gramps-postgres`](https://github.com/DavidMStraub/gramps-postgres-docker/) les ajoute. Pour l'utiliser, ajoutez la section suivante à votre `docker-compose.yml` :
```yaml
  postgres_gramps:
    image: ghcr.io/davidmstraub/gramps-postgres:latest
    restart: unless-stopped
    environment:
      POSTGRES_PASSWORD: postgres_password_admin
      POSTGRES_PASSWORD_GRAMPS: postgres_password_gramps
      POSTGRES_PASSWORD_GRAMPS_USER: postgres_password_gramps_user
    volumes:
      - postgres_data:/var/lib/postgresql/data
```
et ajoutez également `postgres_data:` en tant que clé sous la section `volumes:` de ce fichier YAML. L'image contient deux bases de données, chacune avec son propre utilisateur et mot de passe : `gramps` pour les données généalogiques et `grampswebuser` pour la base de données utilisateur de Gramps Web.

Si vous utilisez votre propre serveur PostgreSQL à la place, créez une base de données nommée `gramps` dans laquelle l'utilisateur configuré peut créer des tables, et assurez-vous que les locales dont vos utilisateurs ont besoin sont installées.

## Configuration de Gramps Web

De nouveaux arbres généalogiques sont créés dans la base de données SharedPostgreSQL lorsque Gramps Web fonctionne en [mode multi-arbres](multi-tree.md) et que l'option de configuration `NEW_DB_BACKEND` est définie sur `sharedpostgresql`. Avec la configuration Docker Compose ci-dessus, ajoutez ce qui suit sous la clé `environment:` du service `grampsweb` dans `docker-compose.yml` :

```yaml
      # activer le mode multi-arbres
      GRAMPSWEB_TREE: "*"
      GRAMPSWEB_MEDIA_PREFIX_TREE: true
      # créer de nouveaux arbres dans la base de données SharedPostgreSQL
      GRAMPSWEB_NEW_DB_BACKEND: sharedpostgresql
      # L'hôte et le port du serveur PostgreSQL. L'
      # hôte est le nom du service PostgreSQL ci-dessus
      GRAMPSWEB_POSTGRES_HOST: postgres_gramps
      GRAMPSWEB_POSTGRES_PORT: 5432
      # Les identifiants doivent correspondre à ceux utilisés pour
      # le conteneur PostgreSQL
      GRAMPSWEB_POSTGRES_USER: gramps
      GRAMPSWEB_POSTGRES_PASSWORD: postgres_password_gramps
```

Consultez [Configuration](configuration.md) pour une description de toutes ces options. Notez que l'hôte et le port sont enregistrés avec chaque arbre lorsqu'il est créé, donc les modifier plus tard n'affecte que les nouveaux arbres.

## Création d'un arbre et importation de données

Pour créer un nouvel arbre, envoyez une requête POST à l'endpoint `/trees/` comme décrit dans [Configuration pour héberger plusieurs arbres](multi-tree.md#create-a-new-tree). La réponse contient l'ID du nouvel arbre, dont vous avez besoin pour [créer le compte propriétaire de l'arbre](../administration/owner.md#multi-tree-setup-create-tree-owner-account).

Une fois que le propriétaire de l'arbre s'est connecté, il peut [importer](../administration/import.md) un arbre généalogique existant, par exemple un fichier XML Gramps exporté depuis Gramps Desktop, via l'interface web.

## Utilisation d'une base de données PostgreSQL pour la base de données utilisateur

La base de données utilisateur est généralement un fichier SQLite, peu importe où les arbres généalogiques sont hébergés. Pour utiliser PostgreSQL à la place, définissez l'option de configuration `USER_DB_URI` sur une URL de base de données PostgreSQL. Avec l'image `gramps-postgres` ci-dessus, utilisez sa base de données `grampswebuser` :
```
postgresql://grampswebuser:postgres_password_gramps_user@postgres_gramps:5432/grampswebuser
```

## Utilisation d'une base de données PostgreSQL pour l'index de recherche

L'index de recherche est également stocké dans SQLite par défaut. Pour utiliser PostgreSQL à la place, définissez l'option de configuration `SEARCH_INDEX_DB_URI` sur une URL de base de données PostgreSQL. Avec l'image `gramps-postgres` ci-dessus, vous pouvez utiliser sa base de données `gramps`, que vos arbres généalogiques y soient hébergés ou non :
```
postgresql://gramps:postgres_password_gramps@postgres_gramps:5432/gramps
```

## Déplacer un arbre de l'addon PostgreSQL vers SharedPostgreSQL

Les installations plus anciennes peuvent héberger leur arbre généalogique avec l'addon PostgreSQL, qui stocke un seul arbre par base de données et est obsolète. Pour savoir quel addon un arbre utilise, regardez le fichier `database.txt` dans le sous-répertoire de l'arbre du répertoire de base de données Gramps : il contient `postgresql` pour l'addon PostgreSQL obsolète et `sharedpostgresql` pour SharedPostgreSQL.

Pour déplacer un arbre de l'addon PostgreSQL vers SharedPostgreSQL au sein de la même installation, en conservant vos comptes utilisateurs et fichiers multimédias :

1. [Sauvegardez votre arbre généalogique](../administration/export.md#back-up-your-family-tree) en tant que fichier XML Gramps (`.gramps`), en utilisant un compte qui peut voir les enregistrements privés.
2. Modifiez votre configuration comme décrit dans [Configuration de Gramps Web](#configuring-gramps-web). Vous pouvez continuer à utiliser votre conteneur `gramps-postgres` existant.
3. [Créez un nouvel arbre](multi-tree.md#create-a-new-tree) et notez son ID d'arbre.
4. Assignez vos comptes utilisateurs existants au nouvel arbre, comme décrit dans [Migrer la base de données utilisateur existante](multi-tree.md#migrate-existing-user-database).
5. Déplacez vos fichiers multimédias vers l'emplacement attendu pour le nouvel arbre, comme décrit dans [Migrer les fichiers multimédias existants](multi-tree.md#migrate-existing-media-files).
6. Connectez-vous et [importez](../administration/import.md) le fichier XML Gramps dans le nouvel arbre.

Conservez le fichier XML Gramps jusqu'à ce que vous ayez vérifié que le nouvel arbre est complet.

Si vous passez à une installation Gramps Web distincte, suivez les étapes dans [Déplacer vers une autre instance Gramps Web](../administration/export.md#move-to-a-different-gramps-web-instance).

## Problèmes

En cas de problèmes, veuillez surveiller la sortie des journaux de Gramps Web et du serveur PostgreSQL. Dans le cas de Docker, cela se fait avec

```
docker compose logs grampsweb
docker compose logs postgres_gramps
```

Si vous soupçonnez qu'il y a un problème avec Gramps Web (ou la documentation), veuillez signaler un problème [sur Github](https://github.com/gramps-project/gramps-web-api/issues).
