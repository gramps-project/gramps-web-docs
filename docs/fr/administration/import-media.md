# Importer des fichiers multimédias

Si vous avez [importé un arbre généalogique](import.md) et que vous devez télécharger les fichiers multimédias correspondants, utilisez **Importer des fichiers multimédias** dans la section Données des [paramètres d'administration](settings.md). Cela attend un fichier ZIP contenant les fichiers multimédias manquants. Les fichiers sont associés aux objets multimédias dans votre arbre de l'une des deux manières suivantes :

- **Par somme de contrôle.** Pour les objets multimédias qui ont une somme de contrôle – comme c'est le cas pour les arbres importés depuis Gramps Desktop – le fichier avec la somme de contrôle correspondante est utilisé, quel que soit son nom ou la structure de dossier dans le fichier ZIP. Cela ne fonctionne que si les sommes de contrôle dans la base de données Gramps sont correctes, ce que garantit l'exécution de l'outil de vérification et de réparation.
- **Par chemin.** Les objets multimédias sans somme de contrôle – comme c'est typique après un import GEDCOM – sont associés par leur chemin : le fichier ZIP doit contenir le fichier sous exactement le chemin relatif stocké dans l'objet multimédia.

Si les chemins stockés dans votre fichier GEDCOM sont absolus (par exemple `C:\Users\...\photo.jpg`), l'association par chemin ne fonctionnera pas. Dans ce cas, il est recommandé d'importer d'abord tout dans Gramps Desktop, qui a plus d'options pour associer des fichiers multimédias existants avec un arbre importé, puis de passer à Gramps Web comme décrit dans [Provenant de Gramps Desktop](import.md#coming-from-gramps-desktop).

## État des fichiers multimédias

La section **Données** des [paramètres d'administration](settings.md) montre :

- Le nombre total d'objets multimédias dans l'arbre et si certains manquent d'une somme de contrôle
- Le nombre d'objets multimédias dont le fichier associé est manquant sur le serveur

Une coche verte indique que tout est en ordre. Si des problèmes sont détectés, des liens vers les objets concernés sont affichés. Les sommes de contrôle manquantes se produisent généralement lorsque des données ont été importées d'un format tel que GEDCOM qui inclut des références multimédias mais pas les fichiers réels. Les fichiers manquants peuvent être téléchargés comme décrit ci-dessus.
