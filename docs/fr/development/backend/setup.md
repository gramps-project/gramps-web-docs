# Configuration du développement backend

Cette page liste les étapes nécessaires pour commencer à développer [Gramps Web API](https://github.com/gramps-project/gramps-web-api/), le backend (composant serveur) de Gramps Web.


## Prérequis

La configuration de développement recommandée utilise Visual Studio Code avec des devcontainers. Cette approche créera un environnement de développement préconfiguré avec tous les outils dont vous avez besoin. Pour commencer, vous aurez besoin des ingrédients suivants :

- [Docker](https://docs.docker.com/get-docker/)
- [Visual Studio Code](https://code.visualstudio.com/) avec l'[extension Dev Containers](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers) installée
- [Git](https://git-scm.com)

Vous pouvez utiliser Linux, macOS ou Windows comme système d'exploitation.


## Commencer

1. Ouvrez le [dépôt Gramps Web API](https://github.com/gramps-project/gramps-web-api) et cliquez sur "fork"
2. Clonez votre dépôt forké sur votre machine locale en utilisant Git
3. Ouvrez le dépôt cloné dans Visual Studio Code. Lorsque vous y êtes invité, sélectionnez "Reopen in Container" ou ouvrez manuellement la palette de commandes (Ctrl+Shift+P ou Cmd+Shift+P) et sélectionnez "Dev Containers: Rebuild and Reopen in Container".
4. Attendez que le dev container se construise et démarre. Cela peut prendre quelques minutes, surtout la première fois.

    **Après que la construction du Dev Container soit réussie, la commande retournera :**

    `Successfully installed gramps-webapi-x.x.x.`

    !!! info
        Pour reconstruire le conteneur dans Visual Studio Code :

        - Si vous êtes dans le conteneur, utilisez la commande de palette "Rebuild in container".

        - Si vous êtes dans la vue dossier (c'est-à-dire pas dans le conteneur), utilisez la commande de palette "Rebuild and Reopen in Container".

## Tâches

Si vous modifiez uniquement le code backend, vous n'avez pas nécessairement besoin de lancer un serveur web - les tests unitaires utilisent un client de test Flask qui permet de simuler des requêtes à l'API sans avoir besoin d'un serveur en cours d'exécution.

Cependant, exécuter un serveur est utile si vous

- souhaitez essayer vos modifications avec de vraies requêtes HTTP (voir [requêtes manuelles](queries.md)), 
- souhaitez prévisualiser l'impact des modifications sur l'application complète Gramps Web, ou
- souhaitez également apporter des modifications simultanées au frontend (voir [configuration du développement frontend](../frontend/setup.md)).

L'exécution du serveur est simplifiée dans le dev container par des tâches prédéfinies. Vous pouvez exécuter ces tâches depuis la palette de commandes (Ctrl+Shift+P ou Cmd+Shift+P) en sélectionnant "Tasks: Run Task" puis en choisissant l'une des options suivantes :
- "Serve Web API" - démarre le serveur de développement Flask sur le port 5555 avec les journaux de débogage activés
- "Start Celery worker" - démarre un worker Celery pour traiter les tâches en arrière-plan.


## Débogage

Le débogage peut parfois être difficile, surtout lorsqu'il s'agit de tracer un comportement complexe ou d'identifier des problèmes subtils. Pour faciliter cela, vous pouvez déboguer à la fois une instance API en cours d'exécution et des cas de test individuels directement dans Visual Studio Code.

### Débogage de l'API Gramps Web

Pour déboguer l'API en cours d'exécution :

1. Ouvrez Visual Studio Code et allez dans la vue **Exécuter et déboguer**.  
2. Sélectionnez la configuration **"Web API"** dans le menu déroulant.  
3. Commencez le débogage.  
4. Lorsque vous envoyez des requêtes au backend (soit manuellement, soit via l'interface Gramps Web), l'exécution s'arrêtera à tous les points d'arrêt que vous avez définis dans le code.  
   Cela vous permet d'inspecter les variables, le flux de contrôle et d'autres détails d'exécution.

### Débogage des cas de test

Pour déboguer un cas de test spécifique :

1. Ouvrez le fichier de test que vous souhaitez déboguer (par exemple, `test_people.py`).  
2. Dans Visual Studio Code, ouvrez la vue **Exécuter et déboguer**.  
3. Choisissez la configuration **"Current Test File"**.  
4. Commencez le débogage — l'exécution s'arrêtera à tous les points d'arrêt définis dans ce fichier de test.  

Cette configuration vous permet de parcourir la logique des tests, d'examiner les valeurs des variables et de mieux comprendre les échecs de tests ou les résultats inattendus.
