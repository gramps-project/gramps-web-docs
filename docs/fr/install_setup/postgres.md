# Utilisation d'une base de données PostgreSQL

Par défaut, Gramps utilise une base de données SQLite basée sur des fichiers pour stocker l'arbre généalogique. Cela fonctionne parfaitement pour Gramps Web et est recommandé pour la plupart des utilisateurs. Cependant, à partir de la version 0.3.0 de l'API Gramps Web, un serveur PostgreSQL avec un seul arbre généalogique par base de données est également pris en charge, alimenté par le [module complémentaire Gramps PostgreSQL](https://gramps-project.org/wiki/index.php/Addon:PostgreSQL). Depuis la [version 1.0.0](https://github.com/gramps-project/gramps-web-api/releases/tag/v1.0.0), le module complémentaire SharedPostgreSQL est également pris en charge, ce qui permet d'héberger plusieurs arbres généalogiques dans une seule base de données, ce qui est particulièrement utile lorsqu'il est utilisé avec le [support multi-arbres de l'API Gramps Web](multi-tree.md).

## Configuration du serveur PostgreSQL

Si vous souhaitez configurer une nouvelle base de données pour une utilisation avec le PostgreSQLAddon, vous pouvez suivre les [instructions dans le Wiki de Gramps](https://gramps-project.org/wiki/index.php/Addon:PostgreSQL) pour configurer le serveur.

Alternativement, vous pouvez également utiliser Docker Compose pour exécuter le serveur PostgreSQL dans un conteneur sur le même hôte Docker que Gramps Web.

Utiliser un PostgreSQL dockerisé avec Gramps est seulement compliqué par le fait que les images PostgreSQL par défaut n'ont aucune locale installée, qui est cependant nécessaire pour Gramps pour le tri localisé des objets. L'option la plus simple est d'utiliser l'image `gramps-postgres` publiée dans [ce dépôt](https://github.com/DavidMStraub/gramps-postgres-docker/). Pour l'utiliser, ajoutez la section suivante à votre `docker-compose.yml` :
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
et ajoutez également `postgres_data:` comme clé sous la section `volumes:` de ce fichier YAML. Cette image contient une base de données séparée pour les données généalogiques de Gramps et pour la base de données utilisateur de Gramps ; chacune peut avoir des mots de passe séparés.

## Importation d'un arbre généalogique Gramps

Encore une fois, si vous avez configuré le serveur PostgreSQL vous-même, vous pouvez suivre les [instructions dans le Wiki de Gramps](https://gramps-project.org/wiki/index.php/Addon:PostgreSQL) pour importer un arbre généalogique dans la base de données.

Alternativement, si vous avez suivi les instructions Docker Compose ci-dessus, vous pouvez utiliser la commande suivante pour importer un fichier XML Gramps situé sur votre hôte Docker :

```bash
docker compose run --entrypoint "" grampsweb \
    gramps -C postgres \
    -i /root/.gramps/grampsdb/my_tree.gramps \
    --config=database.path:/root/.gramps/grampsdb \
    --config=database.backend:postgresql \
    --config=database.host:postgres_gramps \
    --config=database.port:5432 \
    --username=gramps --password=postgres_password_gramps
```

## Configuration de l'API Web pour une utilisation avec la base de données

Pour configurer l'API Web pour une utilisation avec la base de données PostgreSQL, ajoutez ce qui suit sous la clé `environment:` du service `grampsweb` dans `docker-compose.yml` :

```yaml
      # le module complémentaire PostgreSQL suppose que le nom de l'arbre soit
      # égal au nom de la base de données et ici le nom de base de données par défaut
      # de l'image PostgreSQL est utilisé
      TREE: postgres
      # Les identifiants doivent correspondre à ceux utilisés pour
      # le conteneur PostgreSQL
      POSTGRES_USER: gramps
      POSTGRES_PASSWORD: postgres_password_gramps
```

## Utilisation d'une base de données PostgreSQL partagée dans une installation multi-arbres

Lors de l'utilisation d'une [configuration multi-arbres](multi-tree.md), le module complémentaire SharedPostgreSQL est une option pratique pour héberger tous les arbres, y compris ceux nouvellement créés via l'API, dans une seule base de données PostgreSQL sans compromettre la confidentialité ou la sécurité.

Pour cela, configurez un conteneur basé sur l'image `gramps-postgres` comme décrit ci-dessus et définissez simplement l'option de configuration `NEW_DB_BACKEND` sur `sharedpostgresql`, par exemple via la variable d'environnement `GRAMPSWEB_NEW_DB_BACKEND`.

## Utilisation d'une base de données PostgreSQL pour la base de données utilisateur

Indépendamment de la base de données utilisée pour les données généalogiques, la base de données utilisateur peut être hébergée dans une base de données PostgreSQL en fournissant une URL de base de données appropriée. L'image Docker `gramps-postgres` mentionnée ci-dessus contient une base de données séparée `grampswebuser` qui peut être utilisée à cette fin. Dans ce cas, la valeur appropriée pour l'option de configuration `USER_DB_URI` serait
```
postgresql://grampswebuser:postgres_password_gramps_user@postgres_gramps:5432/grampswebuser
```

## Utilisation d'une base de données PostgreSQL pour l'index de recherche

Depuis la version 2.4.0 de l'API Gramps Web, l'index de recherche est hébergé soit dans une base de données SQLite (la valeur par défaut), soit dans une base de données PostgreSQL. Également pour cet objectif, l'image `gramps-postgres` peut être utilisée. Pour l'index de recherche, nous pouvons utiliser la base de données `gramps` fournie par l'image, peu importe si nous hébergeons nos données généalogiques dans PostgreSQL ou non (l'index de recherche et les données généalogiques peuvent coexister dans la même base de données). Cela peut être réalisé, dans l'exemple ci-dessus, en définissant l'option de configuration `SEARCH_INDEX_DB_URI` sur
```
postgresql://gramps:postgres_password_gramps@postgres_gramps:5432/gramps
```

## Problèmes

En cas de problèmes, veuillez surveiller la sortie des journaux de Gramps Web et du serveur PostgreSQL. Dans le cas de Docker, cela se fait avec

```
docker compose logs grampsweb
docker compose logs postgres_grampsweb
```

Si vous soupçonnez qu'il y a un problème avec Gramps Web (ou la documentation), veuillez signaler un problème [sur Github](https://github.com/gramps-project/gramps-web-api/issues).
