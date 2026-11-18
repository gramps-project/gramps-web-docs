# Étiquettes

Les étiquettes sont des labels qui peuvent être appliqués à tout objet dans la base de données Gramps – personnes, familles, événements, lieux, sources, citations, dépôts, notes et médias. Elles sont utiles pour regrouper et filtrer les objets. Les étiquettes sont stockées dans la base de données de l'arbre généalogique Gramps et sont partagées entre tous les utilisateurs ; elles sont également entièrement compatibles avec les étiquettes créées dans Gramps Desktop.


## Gestion des étiquettes

Les étiquettes sont gérées depuis la section **Étiquettes** des [Paramètres d'administration](../administration/settings.md#tags), qui n'est disponible que pour les utilisateurs ayant le rôle de Propriétaire ou d'Administrateur. Elle affiche toutes les étiquettes existantes et vous permet de :

- **Créer** une nouvelle étiquette en utilisant le bouton **Nouvelle étiquette**
- **Renommer** une étiquette en utilisant l'icône d'édition (crayon)
- **Changer la couleur** d'une étiquette en utilisant le sélecteur de couleur
- **Supprimer** une étiquette en utilisant l'icône de suppression

!!! note
    La suppression d'une étiquette la retire de tous les objets auxquels elle a été appliquée.

## Application des étiquettes aux objets

Les étiquettes peuvent être appliquées ou retirées d'un objet sur sa page de détails lorsqu'elle est en mode édition. Pour étiqueter plusieurs objets à la fois, sélectionnez-les dans une liste et utilisez l'action **Ajouter une étiquette** ou **Retirer une étiquette**, voir [Listes](lists.md#tags-and-privacy).

Les étiquettes sont affichées dans la colonne **Étiquettes** des listes, ainsi que dans les résultats de recherche, les signets et l'historique. Si une liste ne montre pas la colonne, activez-la dans le sélecteur de colonnes.

## Filtrage par étiquette

Toutes les [pages de liste d'objets](lists.md) (Personnes, Familles, Événements, Lieux, Sources, Citations, Dépôts, Notes, Médias) incluent un filtre d'étiquette. Utilisez-le pour afficher uniquement les objets qui ont une étiquette spécifique appliquée.

## Étiquettes spéciales

Deux étiquettes ont une signification spéciale dans Gramps Web :

- **`Blog`** – toute source étiquetée `Blog` est considérée comme un article de blog et apparaît dans la vue [Blog](blog.md)
- **`ToDo`** – toute note étiquetée `ToDo` est considérée comme une tâche de recherche et apparaît dans la vue [Tâches](tasks.md)

Ces étiquettes sont créées automatiquement lorsque vous utilisez pour la première fois les fonctionnalités Blog ou Tâches. Renommer ou supprimer ces étiquettes désactivera la fonctionnalité correspondante.
