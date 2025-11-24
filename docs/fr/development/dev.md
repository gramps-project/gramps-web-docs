---
hide:
  - toc
---

# Développement Web de Gramps : aperçu

Gramps Web est une application web qui se compose de deux composants développés séparément :

- **Gramps Web API** est une API RESTful écrite en Python et basée sur Flask. Le code source est hébergé sur [github.com/gramps-project/gramps-web-api](https://github.com/gramps-project/gramps-web-api/). Elle gère l'accès à la base de données et les fonctions généalogiques en s'appuyant directement sur la bibliothèque Python Gramps. Elle sert de backend à Gramps Web. Pour la documentation de développement, voir [Backend](backend/index.md).
- **Gramps Web Frontend** est une application web Javascript qui sert de frontend à Gramps Web. Le code source est hébergé sur [github.com/gramps-project/gramps-web](https://github.com/gramps-project/gramps-web/). Pour la documentation de développement, voir [Frontend](frontend/index.md).

Une note sur la version : Gramps Web API et le frontend de Gramps Web sont versionnés indépendamment. Actuellement, "Gramps Web" &ndash; l'application combinée &ndash; n'a pas de numéro de version séparé. Les deux projets adhèrent à [SemVer](https://semver.org/).

Si vous n'êtes pas développeur Python ou Javascript mais que vous souhaitez tout de même contribuer à Gramps Web, consultez [Contribute](../contribute/contribute.md).
