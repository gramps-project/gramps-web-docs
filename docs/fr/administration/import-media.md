# Importer des fichiers multimédias

Si vous avez [importé un arbre généalogique](import.md) et devez télécharger les fichiers multimédias correspondants, utilisez **Importer des fichiers multimédias** sur la [page d'importation](import.md), sous l'importation de l'arbre généalogique. Cela nécessite un fichier ZIP contenant les fichiers multimédias manquants. Le téléchargement n'est possible que lorsque l'arbre contient des objets multimédias, car les fichiers sont associés à des objets multimédias existants – un fichier d'arbre généalogique ne fait référence qu'à ses fichiers multimédias, donc importez-le d'abord.

Les fichiers sont associés aux objets multimédias dans votre arbre de l'une des deux manières suivantes :

- **Par somme de contrôle.** Pour les objets multimédias qui ont une somme de contrôle – comme c'est le cas pour les arbres importés depuis Gramps Desktop – le fichier avec la somme de contrôle correspondante est utilisé, quel que soit son nom ou la structure des dossiers dans le fichier ZIP. Cela ne fonctionne que si les sommes de contrôle dans la base de données Gramps sont correctes, ce que garantit l'exécution de l'outil de vérification et de réparation.
- **Par chemin ou nom de fichier.** Les objets multimédias sans somme de contrôle – comme c'est typique après un import GEDCOM – sont associés par le chemin relatif stocké dans l'objet multimédia. Si aucun fichier dans le ZIP n'a ce chemin, ils sont associés uniquement par le nom de fichier, en ignorant la casse (depuis Gramps Web API 3.26). Cela fonctionne également pour les chemins absolus d'autres programmes, tels que `C:\Users\...\Family\grandpa.jpg`, vous pouvez donc simplement mettre tous les fichiers dans le fichier ZIP. Un nom de fichier n'est utilisé que s'il est unique, à la fois dans le fichier ZIP et parmi les objets multimédias qui n'ont pas encore de fichier.

Après le téléchargement, le résultat indique pour combien d'objets multimédias un fichier a été trouvé, et liste ceux pour lesquels le fichier ZIP n'avait pas de fichier, avec leur ID Gramps et le chemin stocké. Utilisez cette liste pour trouver les fichiers manquants, puis téléchargez un autre fichier ZIP avec uniquement ceux-ci – les fichiers déjà sur le serveur ne sont pas affectés.

Si plusieurs objets multimédias ont le même nom de fichier dans différents dossiers, l'association par nom de fichier ne fonctionne pas pour eux. Soit recréez la structure de dossiers à partir des chemins stockés dans le fichier ZIP, soit importez tout d'abord dans Gramps Desktop, qui dispose de plus d'options pour associer des fichiers multimédias existants avec un arbre importé, puis passez à Gramps Web comme décrit dans [Provenant de Gramps Desktop](import.md#coming-from-gramps-desktop).

## État des fichiers multimédias

La section **Données** des [paramètres d'administration](settings.md) montre :

- Le nombre total d'objets multimédias dans l'arbre et si certains manquent d'une somme de contrôle
- Le nombre d'objets multimédias dont le fichier associé est manquant sur le serveur

Une coche verte indique que tout est en ordre. Si des problèmes sont détectés, des liens vers les objets affectés sont affichés. Les sommes de contrôle manquantes se produisent généralement lorsque des données ont été importées d'un format tel que GEDCOM qui inclut des références multimédias mais pas les fichiers réels. Les fichiers manquants peuvent être téléchargés comme décrit ci-dessus.
