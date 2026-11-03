# Notifications

**Notifications** est un élément de la barre latérale avec une icône de cloche. Lorsque des erreurs se sont produites ou que des tâches en arrière-plan sont en cours d'exécution, un badge indique le nombre de notifications non lues. Cliquez dessus pour ouvrir le journal des notifications.

Le journal des notifications sert à deux fins :

- C'est un enregistrement des erreurs survenues pendant votre session – requêtes API échouées, erreurs de tâches en arrière-plan, échecs de sauvegarde ou erreurs au niveau du navigateur.
- Il suit l'avancement des tâches en arrière-plan de longue durée – telles que les importations et exportations, la génération de rapports, la reconnaissance de texte OCR, les mises à niveau de base de données, la suppression de nombreux objets et la reconstruction de l'index de recherche – en montrant leur état (par exemple, en attente, démarré, en cours) et en vous notifiant lorsqu'elles sont terminées ou échouent.

Chaque entrée affiche un message court, la source (Réseau, Tâche, Sauvegarde ou Navigateur) et un horodatage. Les tâches terminées affichent "Tâche terminée" ou "Tâche échouée".

Certaines notifications incluent des détails structurés, tels que le message d'erreur d'une tâche échouée. Cliquer sur une telle entrée ouvre une boîte de dialogue avec une répartition des données d'erreur et un bouton **Copier JSON**. Cela est utile lors du signalement d'un bug, car le JSON contient les informations d'erreur exactes du serveur.

Utilisez **Tout effacer** pour rejeter toutes les notifications.

Les tâches qui modifient l'ensemble de l'arbre, telles qu'une importation, une restauration, la suppression de tous les objets ou la reconstruction de l'index de recherche, ne peuvent pas s'exécuter en même temps. Si vous en démarrez une alors qu'une autre est en cours d'exécution, un message indique qu'une autre tâche est déjà en cours sur cet arbre, et la tâche en cours est affichée avec son avancement.

!!! note
    Les notifications sont stockées en mémoire uniquement et sont effacées lorsque vous rechargez la page.
