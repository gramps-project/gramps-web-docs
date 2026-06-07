# Notifications

**Notifications** est un élément de la barre latérale avec une icône de cloche. Lorsque des erreurs se sont produites ou que des tâches en arrière-plan sont en cours, un badge affiche le nombre de notifications non lues. Cliquez dessus pour ouvrir le journal des notifications.

Le journal des notifications a deux objectifs :

- C'est un enregistrement des erreurs survenues pendant votre session – échecs de requêtes API, erreurs de tâches en arrière-plan, échecs d'enregistrement ou erreurs au niveau du navigateur.
- Il suit l'avancement des tâches longues en arrière-plan – telles que les importations et exportations, la génération de rapports, la reconnaissance de texte OCR, les mises à niveau de base de données et les reconstructions d'index de recherche/sémantique – en montrant leur état (par exemple, en attente, commencé, en cours) et en vous notifiant lorsqu'elles sont terminées ou échouent.

Chaque entrée affiche un court message, la source (Réseau, Tâche, Enregistrement ou Navigateur), et un horodatage.

Certaines notifications incluent des détails structurés. En cliquant sur une telle entrée, une boîte de dialogue s'ouvre avec une répartition des données d'erreur et un bouton **Copier JSON**. Cela est utile lors du signalement d'un bug, car le JSON contient les informations d'erreur exactes du serveur.

Utilisez **Tout effacer** pour supprimer toutes les notifications.

!!! note
    Les notifications sont stockées en mémoire uniquement et sont effacées lorsque vous rechargez la page.
