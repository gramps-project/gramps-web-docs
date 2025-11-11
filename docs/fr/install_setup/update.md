# Mise à jour de Gramps Web

Si vous utilisez l'une des méthodes d'installation basées sur Docker Compose, mettre à jour Gramps Web vers la dernière version est simple. Dans le dossier où se trouve votre `docker-compose.yml`, exécutez les commandes suivantes

```bash
docker compose pull
docker compose up -d
```

Pour les mises à jour mineures de la [Gramps Web API](https://github.com/gramps-project/gramps-web-api), c'est tout ce qui est nécessaire. Veuillez suivre les [notes de version de Gramps Web API](https://github.com/gramps-project/gramps-web-api/releases), car il pourrait y avoir des changements majeurs nécessitant une attention ou des modifications de configuration supplémentaires.

Notez que l'image docker par défaut `grampsweb:latest` combine toujours la dernière version de l'API avec la dernière version du frontend. Si vous souhaitez mettre à niveau les deux composants séparément - ce qui est possible - une configuration plus complexe que celle décrite ici est nécessaire.
