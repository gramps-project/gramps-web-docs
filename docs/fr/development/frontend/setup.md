# Configuration du développement frontend

Cette page décrit les étapes nécessaires pour commencer avec le développement frontend.

## Prérequis

La configuration de développement recommandée utilise Visual Studio Code avec des devcontainers. Cette approche créera un environnement de développement préconfiguré avec tous les outils dont vous avez besoin.

Voir [Configuration du développement backend](../backend/setup.md#prérequis) pour les prérequis nécessaires.

## Pour commencer

1. Ouvrez le [dépôt frontend Gramps Web](https://github.com/gramps-project/gramps-web) et cliquez sur "fork"
2. Clonez votre dépôt forké sur votre machine locale en utilisant Git
3. Ouvrez le dépôt cloné dans Visual Studio Code. Lorsque vous y êtes invité, sélectionnez "Reopen in Container" ou ouvrez manuellement la palette de commandes (Ctrl+Shift+P ou Cmd+Shift+P) et sélectionnez "Dev Containers: Rebuild and Reopen in Container".
4. Attendez que le dev container se construise et démarre. Cela peut prendre quelques minutes, surtout la première fois.

## Exécution du serveur de développement frontend

Pour exécuter le serveur de développement frontend et prévisualiser l'impact de vos modifications dans le navigateur, vous pouvez utiliser les tâches prédéfinies dans le dev container.

Pour que cela fonctionne, vous devez d'abord démarrer une instance de l'[API backend Gramps Web](../backend/setup.md#tasks). Le moyen le plus simple de le faire est d'utiliser le dev container backend et [d'exécuter la tâche "Serve Web API"](../backend/setup.md#tasks) dans une fenêtre VS Code séparée.

Une fois le backend en cours d'exécution, vous pouvez exécuter le serveur de développement frontend en sélectionnant "Tasks: Run Task" dans la palette de commandes (Ctrl+Shift+P ou Cmd+Shift+P) puis en choisissant "Serve Gramps Web frontend".

Cela démarrera le serveur de développement frontend sur le port 8001, auquel vous pouvez accéder dans votre navigateur à `http://localhost:8001`. Le navigateur se rechargera automatiquement lorsque vous apporterez des modifications au code frontend, vous permettant de voir immédiatement l'impact de vos changements.
