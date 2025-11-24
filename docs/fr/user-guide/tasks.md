# Utiliser la gestion des tâches intégrée

Gramps Web contient un outil de gestion des tâches généalogiques intégré. Il est destiné à permettre aux chercheurs de planifier et de prioriser, mais aussi de documenter leurs tâches. C'est pourquoi les tâches sont représentées comme des sources dans la base de données Gramps. Après avoir terminé une tâche, le contenu associé peut servir de source documentant le processus de recherche.

## Bases des tâches

Les tâches ont les propriétés suivantes :

- Statut. Cela peut être "Ouvert", "En cours", "Bloqué" ou "Fait"
- Priorité. Cela peut être "Faible", "Moyenne" ou "Élevée"
- Étiquettes. Les étiquettes sont des étiquettes normales de Gramps de la source sous-jacente. (Notez que toutes les tâches ont également l'étiquette `ToDo` pour les identifier comme des tâches, mais cette étiquette est cachée dans la liste des tâches pour éviter l'encombrement.)
- Titre. Affiché dans la liste des tâches
- Description. Un champ de texte enrichi qui peut être utilisé pour décrire l'énoncé du problème, mais aussi pour documenter tout progrès réalisé
- Médias. Tous les fichiers multimédias attachés à la tâche

## Créer une tâche

Puisque les tâches sont des objets normaux de Gramps, elles peuvent être modifiées ou créées par le même groupe d'utilisateurs qui peut modifier ou créer d'autres objets (comme des personnes ou des événements).

Pour créer une tâche, cliquez sur le bouton + sur la page de la liste des tâches. Entrez au moins un titre. Le statut sera toujours "Ouvert" lors de la création.

## Modifier une tâche

Pour modifier les détails d'une tâche, cliquez dessus dans la liste des tâches.

La page de détails de la tâche n'a pas de "mode d'édition" séparé comme d'autres objets Gramps. Les modifications apportées au titre, au statut et à la priorité sont appliquées immédiatement. Les modifications apportées à la description en texte enrichi nécessitent de cliquer sur le bouton "enregistrer" en dessous.

## Changement en masse des propriétés des tâches

La priorité et le statut des tâches peuvent être modifiés en masse en utilisant les cases à cocher dans la liste des tâches pour la sélection et les boutons appropriés au-dessus de la liste des tâches.

## Tâches dans Gramps Desktop

Lors de l'ajout de tâches via Gramps Web, les sources et les notes auront l'étiquette `ToDo` attachée, de sorte que les tâches apparaîtront dans le [Gramplet Notes à faire](https://gramps-project.org/wiki/index.php/Addon:ToDoNotesGramplet) ainsi que dans le [Rapport à faire](https://gramps-project.org/wiki/index.php/Addon:ToDoReport).

Pour ajouter ou modifier une tâche dans Gramps Desktop, utilisez les directives suivantes :

- Ajoutez une source avec l'étiquette `ToDo` et le titre de la tâche comme titre
- Optionnellement, ajoutez une note à la source avec l'étiquette `ToDo`, tapez "À faire", et la description comme texte
- Ajoutez un attribut "Statut" et définissez-le sur "Ouvert", "En cours", "Bloqué" ou "Fait"
- Ajoutez un attribut "Priorité" et définissez-le sur 9 pour faible, 5 pour moyen, ou 1 pour élevé (ces valeurs contre-intuitives sont tirées de la spécification iCalendar)
