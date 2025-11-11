## Préparez votre base de données Gramps

Si vous utilisez Gramps Desktop, il y a deux étapes pour préparer votre base de données afin de vous assurer que tout fonctionnera correctement par la suite. Si vous migrez depuis un autre programme de généalogie, vous pouvez sauter cette étape.

1. Vérifiez et réparez la base de données
    - Optionnel : créez une sauvegarde de la base de données en exportant au format Gramps XML
    - Exécutez l'[outil de vérification et de réparation de la base de données](https://gramps-project.org/wiki/index.php/Gramps_5.2_Wiki_Manual_-_Tools#Check_and_Repair_Database). Cela corrige certaines incohérences internes qui pourraient entraîner des problèmes dans Gramps Web.
2. Convertir les chemins des médias en relatifs
    - Utilisez le Gestionnaire de Médias Gramps pour [convertir tous les chemins des médias d'absolus en relatifs](https://gramps-project.org/wiki/index.php/Gramps_5.2_Wiki_Manual_-_Tools#Convert_paths_from_relative_to_absolute). Notez que même avec des chemins relatifs, tous les fichiers multimédias en dehors de votre répertoire de médias Gramps ne fonctionneront pas correctement lorsqu'ils seront synchronisés avec Gramps Web.

## Importer des données généalogiques

Pour importer un arbre généalogique existant, utilisez la page "Importer" et téléchargez un fichier dans l'un des formats de fichier pris en charge par Gramps &ndash; voir [Importer depuis un autre programme de généalogie](https://www.gramps-project.org/wiki/index.php/Import_from_another_genealogy_program) dans le Wiki Gramps.

Si vous utilisez déjà Gramps Desktop, il est fortement recommandé d'utiliser le format Gramps XML (`.gramps`) pour garantir que vos arbres en ligne et hors ligne utilisent les mêmes identifiants et peuvent être [synchronisés](sync.md).

## Pourquoi pas de support pour le package Gramps XML ?

Bien que Gramps XML (`.gramps`) soit le format préféré pour importer des données, le *package* Gramps XML (`.gpkg`) n'est pas pris en charge par Gramps Web. Cela est dû au fait que les routines d'importation et d'exportation pour les fichiers multimédias ne sont pas adaptées à une utilisation sur un serveur web.

Pour importer les fichiers multimédias appartenant à un fichier `.gramps` importé, consultez la section suivante.

## Importer des fichiers multimédias

Si vous avez téléchargé un arbre généalogique et devez télécharger les fichiers multimédias correspondants, vous pouvez utiliser le bouton "importer l'archive multimédia" sur la page "Importer".

Il attend un fichier ZIP contenant les fichiers multimédias manquants à l'intérieur. La structure des dossiers dans le fichier ZIP n'a pas besoin d'être la même que la structure des dossiers à l'intérieur du dossier de médias Gramps, car les fichiers sont associés aux objets multimédias par leur somme de contrôle.

Notez que cette fonctionnalité ne fonctionne que pour les fichiers ayant la somme de contrôle correcte dans la base de données Gramps (ce qui devrait être assuré en exécutant l'outil de vérification et de réparation à la première étape).

Lors de la migration vers Gramps Web depuis un autre programme de généalogie incluant des fichiers multimédias, il est recommandé d'importer d'abord tout dans Gramps Desktop, qui dispose de plus d'options pour associer des fichiers multimédias existants avec un arbre importé.
