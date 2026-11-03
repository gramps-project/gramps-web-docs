# Listes

Chaque type d'objet dans Gramps Web a une vue en liste : Personnes, Familles, Événements, Lieux, Sources, Citations, Dépôts, Notes et Médias. Ils fonctionnent tous de la même manière et partagent les mêmes outils pour trier, filtrer et éditer en masse.

## Tri et pagination

Cliquez sur l'en-tête d'une colonne pour trier par cette colonne ; cliquez à nouveau pour inverser l'ordre. Le tri est effectué par le serveur, il s'applique donc à l'ensemble de la liste, pas seulement à la page que vous consultez.

Les longues listes sont divisées en pages. Utilisez les contrôles de pagination en bas pour naviguer entre elles.

Sur les écrans étroits, le tableau passe automatiquement à une mise en page compacte, de sorte que les vues en liste restent utilisables sur un téléphone.

## Choix des colonnes

Cliquez sur l'icône de réglage au-dessus de la liste pour ouvrir la boîte de dialogue **Colonnes**. Cochez ou décochez une colonne pour l'afficher ou la masquer. **Réinitialiser** restaure la sélection par défaut pour cette liste.

Au moins une colonne doit rester visible, donc la dernière colonne restante ne peut pas être décochée.

Votre sélection de colonnes est mémorisée par type d'objet et par arbre généalogique. Elle est stockée dans votre navigateur, donc elle n'est pas visible par d'autres utilisateurs – mais elle ne vous suit pas non plus sur un autre navigateur ou appareil.

## Filtrage

Cliquez sur le bouton **filtre** pour ouvrir le panneau de filtrage. Il offre trois façons de filtrer, qui peuvent être combinées :

- **Filtres prédéfinis** dans des sections repliables qui dépendent du type d'objet. Pour les personnes, par exemple, vous pouvez filtrer par année de naissance, année de décès, diverses propriétés de la personne, le nombre d'associations, des étiquettes, et si un objet est privé ou public.
- **Filtre avancé** – un constructeur de conditions pour des filtres que les filtres prédéfinis ne peuvent pas exprimer, décrit [ci-dessous](#advanced-filter).
- **GQL** – un champ de texte pour une requête dans le [Gramps Query Language](gql.md). Tapez la requête et appuyez sur Entrée ou cliquez sur **Appliquer**. Si la requête est invalide, le cadre du champ devient rouge. Une requête s'applique en plus des autres filtres.

Les filtres actifs sont affichés sous forme de chips au-dessus de la liste. Supprimez un filtre unique en cliquant sur le bouton de suppression de la chip, ou utilisez **Effacer tous les filtres** pour les supprimer tous en une seule fois.

### Filtre avancé

Cliquez sur **Filtre avancé** en bas du panneau de filtrage pour ouvrir le constructeur de conditions. Ses conditions sont les règles de filtrage connues de Gramps Desktop, telles que "Personnes avec le &lt;nom&gt;" ou "Ancêtres de &lt;personne&gt;".

- Cliquez sur **Ajouter une condition** pour choisir une règle. Les règles sont regroupées par catégories et peuvent être recherchées par nom ou description.
- Remplissez les paramètres de la règle. Chaque paramètre a une entrée correspondante, par exemple un champ de date, un sélecteur d'étiquettes, ou un sélecteur d'objet pour une personne ou un lieu.
- Choisissez comment les conditions d'un groupe sont combinées : **Toutes les conditions**, **Toute condition**, ou – via le menu à côté d'elles – **Exactement une condition**.
- Cliquez sur **Ajouter un groupe** pour ajouter un groupe de conditions à l'intérieur d'un autre groupe, avec sa propre façon de les combiner.
- Sélectionnez **Non** sur une condition ou un groupe pour l'inverser.

Cliquez sur **Appliquer** pour filtrer la liste.

Les filtres prédéfinis qui sont actifs lorsque vous ouvrez le constructeur apparaissent là comme conditions. Si le filtre que vous construisez peut être exprimé avec les filtres prédéfinis, il est affiché avec eux après application. Sinon, il est affiché comme une seule chip **Filtre avancé**, et le panneau de filtrage propose un bouton **Modifier** pour rouvrir le constructeur.

!!! note
    Les règles qui se réfèrent à des filtres personnalisés enregistrés dans Gramps Desktop ne sont pas disponibles dans le constructeur. Les règles sont affichées dans votre langue avec Gramps Web API 3.24 ou version ultérieure.

## Sélectionner des objets et agir sur eux en masse

Les utilisateurs ayant des autorisations d'édition voient un bouton **Sélectionner** à côté du bouton de filtre. Cliquez dessus pour entrer en mode de sélection, ce qui ajoute une case à cocher à chaque ligne.

Cochez les objets que vous souhaitez, et une barre d'outils apparaît montrant combien sont sélectionnés, avec un menu déroulant **Action** et un bouton **Appliquer**.

La case à cocher dans l'en-tête du tableau sélectionne tous les objets sur la page actuelle. Si d'autres objets correspondent aux filtres actuels, la barre d'outils propose alors **Sélectionner tout (N)**, ce qui sélectionne tous les N objets correspondants sur toutes les pages. Décochez une ligne, changez de page ou de filtres, ou quittez le mode de sélection met fin à cette sélection.

### Supprimer

Sélectionnez un ou plusieurs objets, choisissez **Supprimer**, et cliquez sur **Appliquer**. Une boîte de dialogue de confirmation vous demande de confirmer, en avertissant que l'action ne peut pas être annulée.

La suppression de plus de dix objets s'exécute en tant que tâche en arrière-plan. Son avancement est affiché à côté du bouton **Appliquer** et dans [Notifications](notifications.md), et la liste se recharge lorsqu'elle est terminée.

!!! tip
    Les suppressions sont enregistrées dans l'[historique des révisions](revisions.md) comme tout autre changement, donc une suppression en masse erronée peut être annulée en annulant la transaction correspondante.

### Fusionner

Sélectionnez **exactement deux** objets, choisissez **Fusionner**, et cliquez sur **Appliquer**. Une boîte de dialogue demande lequel des deux doit fournir les données principales pour l'objet fusionné ; cliquez sur celui que vous souhaitez conserver comme principal. Les données de l'autre objet sont fusionnées dans celui-ci et les références sont mises à jour.

La fusion est disponible pour les personnes, les familles, les événements, les lieux, les sources et les citations. Elle n'est pas disponible pour les dépôts, les notes et les objets multimédias.

Dans la vue multimédia, la sélection fonctionne à la fois dans la galerie et la mise en page de la liste : en mode de sélection, cliquer sur une tuile ou une ligne la bascule. **Supprimer** est la seule action disponible pour les médias.

Si vous choisissez une action sans sélection valide – par exemple une fusion avec un seul objet sélectionné – une boîte de dialogue explique ce qui est requis.
