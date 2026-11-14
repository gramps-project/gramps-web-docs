# Index de recherche

La section **Index de recherche** des [Paramètres d'administration](settings.md) montre l'état de l'index de recherche en texte intégral et vous permet de le reconstruire.

## Gérer l'index de recherche

Gramps Web maintient un index de recherche en texte intégral qui est normalement mis à jour automatiquement chaque fois que des données changent. L'indicateur de statut montre combien d'objets sont actuellement indexés par rapport au nombre total d'objets.

Cliquez sur **Mettre à jour l'index de recherche** pour déclencher une reconstruction complète. Un indicateur de progression est affiché pendant que la tâche s'exécute en arrière-plan. Cela est rarement nécessaire.

Si un arbre n'a pas encore d'index de recherche, par exemple après une mise à niveau du serveur qui a changé le format de l'index, Gramps Web le construit en arrière-plan la première fois que l'arbre est ouvert. Pendant qu'il est en cours de construction, la section affiche "L'index de recherche est en cours de construction." au lieu des comptes, **Mettre à jour l'index de recherche** est désactivé, et les résultats de recherche peuvent être incomplets. La construction apparaît dans [Notifications](../user-guide/notifications.md) comme la tâche "Mettre à jour l'index de recherche".
