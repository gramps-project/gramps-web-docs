# Utiliser la gestion des tâches intégrée

Gramps Web contient un outil de gestion des tâches généalogiques intégré. Il est destiné à permettre aux chercheurs de planifier et de prioriser, mais aussi de documenter leurs tâches. C'est pourquoi les tâches sont représentées comme des sources dans la base de données Gramps. Après avoir terminé une tâche, le contenu associé peut servir de source documentant le processus de recherche.

## Notions de base sur les tâches

Les tâches ont les propriétés suivantes :

- Statut. Cela peut être "Ouvert", "En cours", "Bloqué" ou "Fait"
- Priorité. Cela peut être "Faible", "Moyenne" ou "Élevée"
- Étiquettes. Les étiquettes sont des étiquettes Gramps normales de la source sous-jacente. (Notez que toutes les tâches ont également l'étiquette `ToDo` pour les identifier comme des tâches, mais cette étiquette est cachée dans la liste des tâches pour éviter l'encombrement.)
- Titre. Affiché dans la liste des tâches
- Description. Un champ de texte enrichi qui peut être utilisé pour décrire l'énoncé du problème, mais aussi pour documenter tout progrès réalisé
- Médias. Tous les fichiers multimédias attachés à la tâche

## Créer une tâche

Étant donné que les tâches sont des objets Gramps normaux, elles peuvent être éditées ou créées par le même groupe d'utilisateurs qui peut éditer ou créer d'autres objets (comme des personnes ou des événements).

Pour créer une tâche, cliquez sur le bouton + sur la page de la liste des tâches. Entrez au moins un titre, et éventuellement une priorité, une description, des pièces jointes et des étiquettes. Le statut sera toujours "Ouvert" à la création.

## La liste des tâches

La liste des tâches est triée par statut – les tâches terminées en dernier – et au sein de chaque statut par priorité, de la plus élevée à la plus basse.

Cliquez sur une tâche pour l'ouvrir. Les utilisateurs ayant des permissions d'édition peuvent également cliquer sur l'icône de statut d'une tâche pour changer son statut directement dans la liste, par exemple pour la marquer comme terminée.

Le bouton **filtrer** au-dessus de la liste filtre les tâches par étiquette, avec une expression [GOQL](goql.md), ou avec le [filtre avancé](lists.md#advanced-filter).

## Éditer une tâche

La page de la tâche n'a pas de "mode d'édition" séparé comme d'autres objets Gramps :

- Cliquez sur le titre pour l'éditer. Appuyez sur Entrée, cliquez sur ✓, ou cliquez ailleurs pour enregistrer ; appuyez sur Échap ou cliquez sur ✕ pour annuler.
- Les changements de statut et de priorité sont appliqués immédiatement.
- Pour éditer la description ou les pièces jointes, cliquez sur le bouton d'édition à côté du titre de la section. La description est enregistrée avec le bouton "enregistrer" en dessous ; l'édition des pièces jointes se termine par **Fait**.
- Le bouton de verrouillage détermine si la tâche est privée. La description de la tâche obtient la même confidentialité.

Les utilisateurs sans permissions d'édition voient le statut et la priorité sous forme de texte, et les sections sans contenu sont cachées.

Sous le titre, les éditeurs voient deux autres boutons : **Éditer la source** ouvre la source qui représente la tâche, où ses autres notes, citations et attributs peuvent être édités. **Supprimer** supprime la tâche après confirmation et retourne à la liste des tâches ; le message qui apparaît a un bouton d'annulation pour restaurer la tâche.

## Changement en masse des propriétés des tâches

Les utilisateurs ayant des permissions d'édition voient une case à cocher sur chaque ligne de la liste des tâches. Sélectionnez des tâches et utilisez **Définir la priorité** ou **Définir le statut** au-dessus de la liste pour changer toutes les tâches sélectionnées en une seule fois.

## Tâches dans Gramps Desktop

Lors de l'ajout de tâches via Gramps Web, les sources et les notes auront l'étiquette `ToDo` attachée, de sorte que les tâches apparaîtront dans le [Gramplet Notes à faire](https://gramps-project.org/wiki/index.php/Addon:ToDoNotesGramplet) ainsi que dans le [Rapport à faire](https://gramps-project.org/wiki/index.php/Addon:ToDoReport).

Pour ajouter ou éditer une tâche dans Gramps Desktop, utilisez les directives suivantes :

- Ajoutez une source avec l'étiquette `ToDo` et le titre de la tâche comme titre
- Éventuellement, ajoutez une note à la source avec l'étiquette `ToDo`, tapez "À faire", et la description comme texte
- Ajoutez un attribut "Statut" et définissez-le sur "Ouvert", "En cours", "Bloqué" ou "Fait"
- Ajoutez un attribut "Priorité" et définissez-le sur 9 pour faible, 5 pour moyen, ou 1 pour élevé (ces valeurs contre-intuitives sont tirées de la spécification iCalendar)
