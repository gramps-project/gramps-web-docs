# Recherche

La page de recherche est accessible en cliquant sur l'icône de la loupe dans la barre d'application en haut, ou en appuyant sur le raccourci clavier `s` [raccourci clavier](shortcuts.md).

## Recherche en texte intégral

Tapez n'importe quelle requête dans le champ de recherche et appuyez sur Entrée (ou cliquez sur le bouton de recherche). Gramps Web recherche parmi tous les types d'objets – personnes, familles, événements, lieux, sources, citations, dépôts, notes et médias – et renvoie des résultats correspondants classés par pertinence.

Les résultats affichent le type d'objet, le nom et un bref résumé. Cliquez sur n'importe quel résultat pour ouvrir la page de détails correspondante.

## Syntaxe de recherche

- **Tous les mots doivent correspondre.** `Müller Berlin` trouve des objets contenant les deux mots.
- **`or`** trouve des objets contenant l'un ou l'autre mot, par exemple `Meyer or Maier`. `and` peut également être tapé entre les mots, mais cela ne fait aucune différence.
- `or` s'applique aux mots directement à côté : `Meyer or Maier Berlin` signifie "(Meyer or Maier) et Berlin". Les parenthèses ne sont pas prises en charge.
- **Guillemets** correspondent à une phrase, c'est-à-dire des mots dans cet ordre : `"Johann Georg"`.
- **Caractère générique :** un `*` à la fin correspond à n'importe quelle terminaison, par exemple `Mey*` correspond à "Meyer", "Meyers", "Meyerhofer", etc. Cela fonctionne également pour les phrases : `"Johann Georg"*`.
- `or` et `and` sont reconnus dans n'importe quelle casse. Pour rechercher l'un de ces mots lui-même, mettez-le entre guillemets.
- Les mots ne peuvent pas être exclus ; il n'y a pas de "not".

## Ce que la recherche trouve

- Les accents n'ont pas besoin de correspondre : "Müller" trouve également "Muller", et "muller" trouve "Müller".
- Les familles et les événements sont également trouvés par les noms de leurs personnes, par exemple "Müller" trouve les familles et événements de toutes les personnes nommées Müller. Ces résultats sont classés en dessous des correspondances directes.
- Les types standards sont trouvés par leurs noms dans la langue de votre interface, par exemple "Taufe" trouve les baptêmes dans l'interface allemande.
- Les underscores séparent les mots, donc "microfilm" trouve un fichier média nommé `scanned_microfilm.png`.
- Les utilisateurs qui ne peuvent pas voir les dossiers privés ne trouvent pas d'objets via des informations privées, comme une famille par le nom d'un membre privé.

## Filtrage par type d'objet

Sous le champ de recherche, des boutons à bascule pour chaque type d'objet (Personnes, Familles, Événements, Lieux, …) vous permettent de restreindre les résultats à un ou plusieurs types spécifiques. Par défaut, tous les types sont recherchés. L'activation d'un ou plusieurs boutons limite les résultats à ces types uniquement.
