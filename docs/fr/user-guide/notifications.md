# Notifications

La cloche dans la barre d'application supérieure ouvre les notifications. Un badge sur la cloche indique le nombre de notifications non lues. Le menu liste les tâches en cours et les dernières notifications ; **Afficher tout** ouvre le journal complet des notifications. Sur les petits écrans, la cloche ouvre directement le journal.

Les notifications concernent :

- **Modifications par d'autres utilisateurs.** Lorsque d'autres utilisateurs modifient l'arbre pendant que vous utilisez Gramps Web, une notification indique qui a changé quoi, par exemple "Modifier la personne" ou "12 modifications". Cliquez dessus pour ouvrir le changement dans l'[historique des révisions](revisions.md). Les modifications qui n'ont pas d'utilisateur Gramps Web, telles que les modifications apportées directement à une base de données partagée avec Gramps Desktop, sont affichées sans nom. Cela n'est disponible que pour les utilisateurs qui peuvent voir l'historique des révisions (membres et plus).
- **Tâches en arrière-plan** – telles que les importations et exportations, la génération de rapports, la reconnaissance de texte OCR, les mises à niveau de base de données, la suppression ou l'édition de nombreux objets, et la reconstruction de l'index de recherche – montrant leur état (par exemple, en attente, démarré, en cours) et vous notifiant lorsqu'elles se terminent ou échouent.
- **Erreurs** survenues pendant votre session – requêtes API échouées, erreurs de tâches en arrière-plan, échecs de sauvegarde ou erreurs au niveau du navigateur.

Les exportations terminées et les archives multimédias peuvent être téléchargées depuis leur notification, même après que vous ayez quitté la [page d'exportation](../administration/export.md).

Certaines notifications incluent des détails structurés, tels que le message d'erreur d'une tâche échouée. Cliquer sur une telle entrée dans le journal des notifications ouvre une boîte de dialogue avec une répartition des données d'erreur et un bouton **Copier JSON**. Cela est utile lors du signalement d'un bug, car le JSON contient les informations d'erreur exactes du serveur.

Utilisez **Tout effacer** dans le journal des notifications pour rejeter toutes les notifications.

Les tâches qui changent l'ensemble de l'arbre, telles qu'une importation, une restauration, la suppression de tous les objets ou la reconstruction de l'index de recherche, ne peuvent pas s'exécuter en même temps. Si vous en démarrez une pendant qu'une autre est en cours, un message indique qu'une autre tâche est déjà en cours sur cet arbre, et la tâche en cours est affichée avec sa progression.

!!! note
    Les notifications sont stockées en mémoire uniquement et sont effacées lorsque vous rechargez la page. Gramps Web vérifie les modifications apportées par d'autres utilisateurs uniquement pendant qu'il est ouvert, donc les modifications effectuées pendant votre absence ne sont pas signalées ; voir [Historique des révisions](revisions.md) pour cela.
