# Arbre Généalogique

La page de l'Arbre Généalogique est accessible depuis la barre latérale et affiche des graphiques interactifs centrés sur une personne sélectionnée. Cinq types de graphiques sont disponibles via des onglets en haut de la page.

## Sélection de la personne de départ

Tous les graphiques commencent à partir de la personne actuellement sélectionnée dans l'arbre (indiquée dans la barre d'outils). La personne actuellement centrée est mise en évidence par une ombre portée. Utilisez le bouton **Personne D'accueil** pour revenir à votre personne d'accueil, ou le bouton **Retour** pour revenir à la personne vue précédemment. Cliquer sur la carte d'une personne dans n'importe quel graphique recentre le graphique sur cette personne.

Si aucune personne d'accueil n'a été définie, la page propose un bouton **Définir la Personne D'accueil** pour rechercher et en sélectionner une directement. Si l'arbre ne contient encore aucune personne, les utilisateurs ayant le rôle d'Éditeur ou supérieur voient à la place un bouton **Nouvelle Personne** – la première personne créée dans un arbre vide devient automatiquement votre personne d'accueil, donc le graphique est affiché immédiatement.

## Types de graphiques

### Arbre des Ancêtres

Un graphique de parenté montrant les ancêtres de la personne sélectionnée. Les parents apparaissent à gauche (ou à droite, selon la mise en page), les grands-parents plus loin, et ainsi de suite.

### Arbre des Descendants

Montre les descendants de la personne sélectionnée – enfants, petits-enfants, et ainsi de suite.

### Graphique en Sablier

Combine les ancêtres au-dessus et les descendants en dessous de la personne sélectionnée dans une seule vue.

### Graphique de Relation

Montre le chemin de relation entre deux personnes. La personne sélectionnée est un point d'extrémité ; cliquez sur une autre personne dans le graphique pour définir le deuxième point d'extrémité et afficher le chemin de relation le plus court entre elles.

!!! note
    La même personne peut apparaître plusieurs fois dans le graphique – par exemple, lorsqu'une personne a été mariée plusieurs fois et apparaît dans plusieurs unités familiales le long du chemin. C'est intentionnel, pas un bug.

### Graphique en Éventail

Un graphique de parenté circulaire. Les ancêtres rayonnent vers l'extérieur à partir de la personne sélectionnée au centre.

## Passer aux proches et étendre les branches

Dans l'Arbre des Ancêtres et le Graphique en Éventail, la personne sélectionnée a un bouton en chevron qui ouvre un menu de ses enfants. Dans l'Arbre des Descendants, il ouvre un menu de ses parents à la place. Choisir une personne dans le menu centre le graphique sur elle.

Dans l'Arbre des Ancêtres, l'Arbre des Descendants et le Graphique en Sablier, les personnes à la bordure du graphique dont les parents ou enfants ne sont pas montrés ont un chevron sur le côté où leur branche continue. Cliquer dessus ajoute une génération supplémentaire à cette branche, tandis que la personne sélectionnée reste la même. De cette façon, vous pouvez par exemple regarder tous les grands-parents puis suivre juste une lignée plus loin. Les branches étendues sont réinitialisées lorsque vous sélectionnez une autre personne ou changez de graphique.

## Contrôles de navigation

Tous les types de graphiques partagent une barre d'outils avec les boutons suivants :

- **Personne D'accueil** – revenir à votre personne d'accueil
- **Retour** – revenir à la personne précédemment centrée
- **Détails de la Personne** – ouvrir la page de profil complète de la personne actuellement centrée
- **Préférences** – ouvrir une boîte de dialogue pour ajuster les options d'affichage spécifiques au graphique (voir ci-dessous)

Tous les graphiques prennent en charge le **déplacement** (cliquer et faire glisser) et le **zoom** (molette de défilement ou pincement).

## Préférences du graphique

La boîte de dialogue **Préférences** (icône d'engrenage dans la barre d'outils) vous permet d'ajuster les options suivantes, selon le type de graphique :

- **Max Ancêtres Générations** – combien de générations d'ancêtres afficher
- **Max Descendants Générations** – combien de générations de descendants afficher
- **Max Degré de Séparation** – pour le Graphique de Relation, la longueur maximale du chemin à rechercher
- **Max Nombre d'Images affichées** – limite le nombre de photos de profil affichées dans le graphique pour des raisons de performance
- **Format d'Affichage des Noms** – contrôle comment les noms sont affichés sur les cartes de personnes

Cliquez sur **Réinitialiser** pour restaurer les valeurs par défaut, ou **Fermer** pour appliquer vos modifications.

Les paramètres de préférences de graphique sont stockés dans le stockage local du navigateur, donc ils persistent entre les sessions sur le même appareil.

## Type de graphique par défaut

Le type de graphique affiché lorsque vous ouvrez pour la première fois la page de l'Arbre Généalogique peut être configuré dans [Paramètres Utilisateur](settings.md). Votre choix par défaut s'applique sur tous vos appareils.

## Édition de l'arbre

Les utilisateurs ayant le rôle d'Éditeur ou supérieur peuvent ajouter et lier des personnes directement depuis l'Arbre des Ancêtres. Voir [Édition de l'arbre généalogique](tree-edit.md) pour plus de détails.
