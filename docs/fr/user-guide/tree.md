# Arbre généalogique

La page de l'Arbre généalogique est accessible depuis la barre latérale et affiche des graphiques interactifs centrés sur une personne sélectionnée. Cinq types de graphiques sont disponibles via des onglets en haut de la page.

## Sélection de la personne de départ

Tous les graphiques commencent à partir de la personne actuellement sélectionnée dans l'arbre (indiquée dans la barre d'outils). La personne actuellement centrée est mise en évidence par une ombre portée. Utilisez le bouton **Personne d'accueil** pour revenir à votre personne d'accueil, ou le bouton **Retour** pour revenir à la personne vue précédemment. Cliquer sur la carte d'une personne dans n'importe quel graphique recentre le graphique sur cette personne.

Si aucune personne d'accueil n'a été définie, la page vous invitera à aller à la page d'accueil et à en définir une.

## Types de graphiques

### Arbre des ancêtres

Un graphique de pedigree montrant les ancêtres de la personne sélectionnée. Les parents apparaissent à gauche (ou à droite, selon la mise en page), les grands-parents plus loin, et ainsi de suite.

### Arbre des descendants

Montre les descendants de la personne sélectionnée – enfants, petits-enfants, et ainsi de suite.

### Graphique en sablier

Combine les ancêtres au-dessus et les descendants en dessous de la personne sélectionnée dans une seule vue.

### Graphique de relation

Montre le chemin de relation entre deux personnes. La personne sélectionnée est un point d'extrémité ; cliquez sur n'importe quelle autre personne dans le graphique pour définir le second point d'extrémité et afficher le chemin de relation le plus court entre elles.

!!! note
    La même personne peut apparaître plusieurs fois dans le graphique – par exemple, lorsque quelqu'un a été marié plusieurs fois et apparaît dans plusieurs unités familiales le long du chemin. Cela est intentionnel, pas un bug.

### Graphique en éventail

Un graphique de pedigree circulaire. Les ancêtres rayonnent vers l'extérieur depuis la personne sélectionnée au centre.

## Contrôles de navigation

Tous les types de graphiques partagent une barre d'outils avec les boutons suivants :

- **Personne d'accueil** – revenir à votre personne d'accueil
- **Retour** – revenir à la personne précédemment centrée
- **Détails de la personne** – ouvrir la page de profil complète de la personne actuellement centrée
- **Préférences** – ouvrir une boîte de dialogue pour ajuster les options d'affichage spécifiques au graphique (voir ci-dessous)

Tous les graphiques prennent en charge le **défilement** (cliquer et faire glisser) et le **zoom** (molette de défilement ou pincement).

## Préférences du graphique

La boîte de dialogue **Préférences** (icône d'engrenage dans la barre d'outils) vous permet d'ajuster les options suivantes, selon le type de graphique :

- **Max Générations d'ancêtres** – combien de générations d'ancêtres afficher
- **Max Générations de descendants** – combien de générations de descendants afficher
- **Max Degré de séparation** – pour le Graphique de relation, la longueur de chemin maximale à rechercher
- **Max Nombre d'images affichées** – limite les photos de profil montrées dans le graphique pour des raisons de performance
- **Format d'affichage du nom** – contrôle comment les noms sont affichés sur les cartes de personnes

Cliquez sur **Réinitialiser** pour restaurer les valeurs par défaut, ou **Fermer** pour appliquer vos modifications.

Les paramètres de préférences de graphique sont stockés dans le stockage local du navigateur, donc ils persistent entre les sessions sur le même appareil.

## Type de graphique par défaut

Le type de graphique affiché lorsque vous ouvrez pour la première fois la page de l'Arbre généalogique peut être configuré dans [Paramètres utilisateur](settings.md). Votre choix par défaut s'applique sur tous vos appareils.

## Édition de l'arbre

Les utilisateurs ayant le rôle d'Éditeur ou supérieur peuvent ajouter et lier des personnes directement depuis l'Arbre des ancêtres. Consultez [Édition de l'arbre généalogique](tree-edit.md) pour plus de détails.
