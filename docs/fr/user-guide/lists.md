# Listes

Chaque type d'objet dans Gramps Web a une vue en liste : Personnes, Familles, Événements, Lieux, Sources, Citations, Dépôts, Notes et Médias. Ils fonctionnent tous de la même manière et partagent les mêmes outils pour trier, filtrer et éditer en masse.

## Tri et pagination

Cliquez sur l'en-tête d'une colonne pour trier par cette colonne ; cliquez à nouveau pour inverser l'ordre. Le tri est effectué par le serveur, donc il s'applique à l'ensemble de la liste, pas seulement à la page que vous consultez.

Les longues listes sont divisées en pages. Utilisez les contrôles de pagination en bas pour naviguer entre elles.

Sur les écrans étroits, le tableau passe automatiquement à une mise en page compacte, de sorte que les vues en liste restent utilisables sur un téléphone.

## Choix des colonnes

Cliquez sur l'icône en forme de roue dentée au-dessus de la liste pour ouvrir la boîte de dialogue **Colonnes**. Cochez ou décochez une colonne pour l'afficher ou la masquer. **Réinitialiser** restaure la sélection par défaut pour cette liste.

Au moins une colonne doit rester visible, donc la dernière colonne restante ne peut pas être décochée.

Votre sélection de colonnes est mémorisée par type d'objet et par arbre généalogique. Elle est stockée dans votre navigateur, donc elle n'est pas visible par d'autres utilisateurs – mais elle ne vous suit pas non plus sur un autre navigateur ou appareil.

## Filtrage

Cliquez sur le bouton **filtrer** pour ouvrir le panneau de filtrage. Un bouton bascule en haut du panneau permet de passer entre deux modes :

- **simple** – un ensemble de filtres prêts à l'emploi qui dépendent du type d'objet. Pour les personnes, par exemple, vous pouvez filtrer par année de naissance, année de décès, diverses propriétés de la personne, le nombre d'associations, des étiquettes, et si un objet est privé ou public.
- **GQL** – un champ de texte unique pour une requête avancée dans le [Gramps Query Language](gql.md). Tapez la requête et appuyez sur Entrée ou cliquez sur **Appliquer**. Si la requête est invalide, le cadre du champ devient rouge.

Les filtres actifs sont affichés sous forme de jetons au-dessus de la liste. Supprimez un filtre unique en cliquant sur le bouton de suppression du jeton, ou utilisez **Tout effacer** pour les supprimer tous d'un coup.

!!! note
    Les deux modes sont alternatifs, non additifs : une requête GQL remplace les filtres simples, et revenir au mode simple supprime la requête.

## Sélectionner des objets et agir sur eux en masse

Les utilisateurs ayant des permissions d'édition voient un bouton **Sélectionner** à côté du bouton de filtrage. Cliquez dessus pour entrer en mode de sélection, ce qui ajoute une case à cocher à chaque ligne.

Cochez les objets que vous souhaitez, et une barre d'outils apparaît montrant combien sont sélectionnés, avec un menu déroulant **Action** et un bouton **Appliquer**.

### Supprimer

Sélectionnez un ou plusieurs objets, choisissez **Supprimer**, et cliquez sur **Appliquer**. Une boîte de dialogue de confirmation vous demande de confirmer, en avertissant que l'action ne peut pas être annulée.

!!! tip
    Les suppressions sont enregistrées dans l'[historique des révisions](revisions.md) comme tout autre changement, donc une suppression en masse par erreur peut être annulée en revenant sur la transaction correspondante.

### Fusionner

Sélectionnez **exactement deux** objets, choisissez **Fusionner**, et cliquez sur **Appliquer**. Une boîte de dialogue demande lequel des deux doit fournir les données principales pour l'objet fusionné ; cliquez sur celui que vous souhaitez conserver comme principal. Les données de l'autre objet sont fusionnées dans celui-ci et les références sont mises à jour.

La fusion est disponible pour les personnes, les familles, les événements, les lieux, les sources et les citations. Elle n'est pas disponible pour les dépôts, les notes et les objets multimédias.

Si vous choisissez une action sans une sélection valide – par exemple, une fusion avec un seul objet sélectionné – une boîte de dialogue explique ce qui est requis.
