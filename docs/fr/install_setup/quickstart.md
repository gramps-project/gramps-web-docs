Pour essayer Gramps Web sur votre ordinateur local (Linux, Mac ou Windows) sans interférer avec votre installation de Gramps Desktop, vous pouvez utiliser Docker avec la commande suivante :

```bash
docker run -p "5055:5000" -e GRAMPSWEB_TREE=new ghcr.io/gramps-project/grampsweb:latest
```

Cela rendra une nouvelle instance vide de Gramps Web accessible à [http://localhost:5055](http://localhost:5055), où vous pourrez créer un utilisateur admin et importer un fichier XML Gramps.

!!! info
    Étant donné que cette configuration simple ne permet pas d'exécuter de longues tâches dans un processus séparé, l'importation d'un grand fichier XML Gramps pourrait échouer en raison d'un délai d'attente dans l'assistant de première exécution.

Pour utiliser des fichiers multimédias depuis votre ordinateur, vous pouvez monter le dossier multimédia de Gramps dans le conteneur avec

```bash
docker run -p "5055:5000" -e GRAMPSWEB_TREE=new \
  -v /path/to/my/gramps_media_folder:/app/media \
  ghcr.io/gramps-project/grampsweb:latest
```

Notez que cela ne persistera pas les modifications que vous apportez à la base de données lorsque vous redémarrez le conteneur. Pour configurer correctement Gramps Web, continuez à lire sur le [Déploiement](deployment.md).
