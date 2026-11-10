# Recherche

La page de recherche est accessible en cliquant sur l'icône de la loupe dans la barre d'application en haut, ou en appuyant sur le raccourci clavier `s` [raccourci clavier](shortcuts.md).

## Recherche en texte intégral

Tapez une requête dans le champ de recherche. Les résultats apparaissent au fur et à mesure que vous tapez, à partir du deuxième caractère ; appuyez sur Entrée pour rechercher un seul caractère. Gramps Web recherche dans tous les types d'objets – personnes, familles, événements, lieux, sources, citations, dépôts, notes et médias – et renvoie des résultats correspondants classés par pertinence. Pour effacer la recherche, cliquez sur le bouton d'effacement dans le champ ou appuyez sur Échap.

Chaque résultat affiche le type d'objet, son nom et quelques détails, par exemple la naissance et la mort d'une personne, le mariage d'une famille, l'auteur d'une source ou la première ligne d'une note. Cliquez sur n'importe quel résultat pour ouvrir la page de détails correspondante.

## Syntaxe de recherche

- **Tous les mots doivent correspondre.** `Müller Berlin` trouve des objets qui contiennent les deux mots.
- **`ou`** trouve des objets qui contiennent l'un ou l'autre mot, par exemple `Meyer ou Maier`. `et` peut également être tapé entre les mots, mais cela ne fait aucune différence.
- `ou` s'applique aux mots directement à côté : `Meyer ou Maier Berlin` signifie "(Meyer ou Maier) et Berlin". Les parenthèses ne sont pas prises en charge.
- **Guillemets** correspondent à une phrase, c'est-à-dire des mots dans cet ordre : `"Johann Georg"`.
- **Caractère générique :** un `*` final correspond à n'importe quelle fin, par exemple `Mey*` correspond à "Meyer", "Meyers", "Meyerhofer", etc. Cela fonctionne également pour les phrases : `"Johann Georg"*`.
- **Le dernier mot est complété.** Si la requête se termine par une lettre ou un chiffre, elle est recherchée comme si elle se terminait par `*`, donc `Anna Smi` trouve déjà "Anna Smith". Pour rechercher le dernier mot exactement, terminez la requête par un espace ou mettez le mot entre guillemets. Il en va de même pour les champs de recherche des sélecteurs d'objets et la [carte](map.md#search).
- `ou` et `et` sont reconnus dans n'importe quelle casse. Pour rechercher l'un de ces mots lui-même, mettez-le entre guillemets.
- Les mots ne peuvent pas être exclus ; il n'y a pas de "non".

## Ce que la recherche trouve

- Les accents n'ont pas besoin de correspondre : "Müller" trouve également "Muller", et "muller" trouve "Müller".
- Les familles et les événements sont également trouvés par les noms de leurs personnes, par exemple "Müller" trouve les familles et les événements de toutes les personnes nommées Müller. Ces résultats sont classés en dessous des correspondances directes.
- Les types standards sont trouvés par leurs noms dans la langue de votre interface, par exemple "Taufe" trouve des baptêmes dans l'interface allemande.
- Les underscores séparent les mots, donc "microfilm" trouve un fichier média nommé `scanned_microfilm.png`.
- Les utilisateurs qui ne peuvent pas voir les enregistrements privés ne trouvent pas d'objets par le biais d'informations privées, comme une famille par le nom d'un membre privé.

## Filtrage par type d'objet

Sous le champ de recherche, des boutons à bascule pour chaque type d'objet (Personnes, Familles, Événements, Lieux, …) vous permettent de restreindre les résultats à un ou plusieurs types spécifiques. Par défaut, tous les types sont recherchés. L'activation d'un ou plusieurs boutons à bascule limite les résultats à ces types uniquement.
