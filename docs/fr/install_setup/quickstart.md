Pour essayer Gramps Web sur votre ordinateur local (Linux, Mac ou Windows) sans interférer avec votre installation Gramps Desktop, vous pouvez utiliser Docker avec la commande suivante:

```bash
docker run -p "5055:5000" -e TREE=new ghcr.io/gramps-project/grampsweb:latest
```

Cela rendra une nouvelle instance Web Gramps vide accessible à [http://localhost:5055](http://localhost:5055), où vous pouvez créer un utilisateur administrateur et importer un fichier XML Gramps.

!!! info
Comme cette configuration simple n'autorise pas l'exécution de longues tâches dans un processus séparé, l'importation d'un grand fichier XML Gramps pourrait échouer en raison d'un timeout dans l'assistant de première ligne.


Pour utiliser des fichiers multimédias de votre ordinateur, vous pouvez monter le dossier multimédia Gramps dans le conteneur avec

```bash
docker run -p "5055:5000" -e TREE=new \
  -v /path/to/my/gramps_media_folder:/app/media \
  ghcr.io/gramps-project/grampsweb:latest
```

Notez que cela ne persistera pas les modifications que vous faites à la base de données lorsque vous redémarrez le conteneur. Pour configurer correctement Gramps Web, continuez à lire sur [Deployment](deployment.md).