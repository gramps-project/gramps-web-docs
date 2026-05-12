# Recherche

La page de recherche est accessible en cliquant sur l'icône de la loupe dans la barre d'application en haut, ou en appuyant sur la touche `s` [raccourci clavier](shortcuts.md).

## Recherche en texte intégral

Tapez n'importe quelle requête dans le champ de recherche et appuyez sur Entrée (ou cliquez sur le bouton de recherche). Gramps Web recherche dans tous les types d'objets – personnes, familles, événements, lieux, sources, citations, dépôts, notes et médias – et renvoie les résultats correspondants classés par pertinence.

Les résultats affichent le type d'objet, le nom et un bref résumé. Cliquez sur n'importe quel résultat pour ouvrir la page de détails correspondante.

Un `*` final peut être utilisé comme un caractère générique, par exemple `Mey*` correspond à "Meyer", "Meyers", "Meyerhofer", etc.

## Filtrage par type d'objet

Sous le champ de recherche, des boutons à bascule pour chaque type d'objet (Personnes, Familles, Événements, Lieux, …) vous permettent de restreindre les résultats à un ou plusieurs types spécifiques. Par défaut, tous les types sont recherchés. L'activation d'un ou plusieurs boutons à bascule limite les résultats à ces types uniquement.

## Recherche sémantique

Si l'administrateur du serveur a activé la [recherche sémantique (alimentée par l'IA)](../install_setup/configuration.md), un bouton de mode apparaît dans le coin supérieur droit de la page de recherche avec deux options :

- **Recherche** – recherche en texte intégral standard (par défaut)
- **Sémantique** – recherche alimentée par l'IA qui comprend le sens de votre requête plutôt que de correspondre à des mots exacts

La recherche sémantique est utile pour des requêtes en langage naturel telles que "agriculteur en Bavière au 19ème siècle". Elle nécessite que l'index de recherche sémantique soit peuplé ; voir [Paramètres d'administration](../administration/settings.md) pour savoir comment construire ou mettre à jour l'index.
